"""
Fase B — Enriquecer SEQOPs com IA
==================================
Lê o texto dos PDFs (seqops_texto_pdf.json) + comentários (comentarios_mpd.json),
envia cada SEQOP ao modelo de IA para:

1. Identificar BLOCOS de operação MPD dentro da sequência
2. Classificar TODOS os comentários (MPD e não-MPD) quanto à relevância MPD
3. Mapear comentários aos blocos operacionais
4. Gerar JSON enriquecido com estrutura completa

Resultado: seqops_enriquecidas.json

Uso:
    python enriquecer_seqops.py               # todas as SEQOPs
    python enriquecer_seqops.py --max 3        # testar com 3
    python enriquecer_seqops.py --resume       # continuar de onde parou
"""
import argparse
import json
import logging
import re
import sys
import time
from pathlib import Path
from textwrap import dedent

import requests
import urllib3
urllib3.disable_warnings()

from parsear_secoes import (
    parsear_secoes, montar_texto_resumido, resumo_secoes,
    classificar_comentario_por_keywords, contar_hits_mpd,
    PALAVRAS_CHAVE_MPD_SIGLAS, PALAVRAS_CHAVE_MPD_TERMOS,
)

# ── Configuração ───────────────────────────────────────────────────────────
SCRIPT_DIR = Path(__file__).resolve().parent

ENTRADA_PDF   = SCRIPT_DIR / "seqops_texto_pdf.json"
ENTRADA_COMENT = SCRIPT_DIR / "comentarios_mpd.json"
SAIDA_JSON    = SCRIPT_DIR / "seqops_enriquecidas.json"

API_BASE = "https://apid.petrobras.com.br/ia/generativos/v1/litellm-chat-petrobras/litellm"
API_KEY  = "b320f1f58c9743e9a74048ce64717c89"

MODELOS = [
    "gpt-5.1",
    "qwen3-32b-v1",
    "claude-sonnet-4-5",
    "gpt-4.1",
]

# Limite de contexto: agora usa seções parseadas (muito menor)
MAX_CHARS_RESUMO = 12000  # ~3K tokens (seções relevantes)
MAX_COMPLETION_TOKENS = 6144

# ── Logging ────────────────────────────────────────────────────────────────
log = logging.getLogger("enriquecer")
log.setLevel(logging.INFO)
_fmt = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")

import io
_ch = logging.StreamHandler(
    io.open(sys.stdout.fileno(), mode='w', encoding='utf-8', closefd=False)
)
_ch.setFormatter(_fmt)
log.addHandler(_ch)

_fh = logging.FileHandler(SCRIPT_DIR / "enriquecer_seqops.log", encoding="utf-8")
_fh.setFormatter(_fmt)
log.addHandler(_fh)


# ── Prompt ─────────────────────────────────────────────────────────────────

SYSTEM_PROMPT = dedent("""\
Você é um especialista em perfuração MPD (Managed Pressure Drilling) da Petrobras.

Sua tarefa é analisar seções relevantes de uma Sequência Operacional (SEQOP) e seus
comentários de revisão para identificar TODOS os blocos de operação relevantes para MPD.

VOCABULÁRIO MPD DE REFERÊNCIA (use para detectar relevância):
Siglas: MPD, NRV, NRVs, BA, BART, MBART, M-BART, RCD, SSA, ACD, DSIT, SBP, AP,
        PMCD, FMCD, FCMD, TTV, DPPT, DLOT, DFIT, PS
Termos: Bearing Assembly, junta integrada, junta MPD, FlowSpool, Flow Spool,
        buffer, buffer manifold, packer assy, Seal Sleeve Assembly, Seal Sleeve,
        Cabeça Rotativa MPD, Choke MPD, PMCD dinâmico, FMCD simplificado,
        FCMD simplificado, Trip Tank Virtual, Non ported, No ported,
        Holdpoint MPD, Hold point MPD, HP MPD, CSD MPD, CSD-MPD,
        Junk Catcher, Junk-Catcher, Mangueira de 6", Mangueiras de 6",
        fingerprint, MPD Drill, MPD-Drill, Protect Sleeve

Responda SOMENTE em JSON válido, sem markdown, sem ```json, sem explicações.""")


def montar_prompt_usuario(titulo: str, poco: str, texto_resumido: str,
                          comentarios: list[dict],
                          resumo_sec: dict | None = None) -> str:
    """Monta o prompt do usuário com seções parseadas e comentários."""

    pdf_truncado = texto_resumido

    # Formatar comentários
    # Formatar comentários com pré-classificação por keywords
    linhas_com = []
    for i, c in enumerate(comentarios):
        tipo = c.get("tipo_csd", "?")
        autor = c.get("autor", "?")
        versao = c.get("versao", "?")
        texto = c.get("texto", "").strip()
        pre = classificar_comentario_por_keywords(texto)
        kw_label = f" KW:{pre['provavel_relevancia']}" if pre['hits'] > 0 else ""
        linhas_com.append(f"[#{i} {tipo} | v{versao} | {autor}{kw_label}]\n{texto}")
        # Respostas
        for r in c.get("respostas", []):
            linhas_com.append(f"  └─ [{r.get('autor','?')}] {r.get('texto','')}")

    bloco_comentarios = "\n---\n".join(linhas_com) if linhas_com else "(sem comentários)"

    # Resumo das seções encontradas
    secoes_info = ""
    if resumo_sec:
        secoes_info = (f"\nSeções parseadas: {resumo_sec['total']} total, "
                       f"hits MPD: {resumo_sec.get('total_hits_mpd', 0)}")

    return dedent(f"""\
SEQOP: {titulo}
POÇO: {poco}{secoes_info}

═══ SEÇÕES RELEVANTES DA SEQUÊNCIA OPERACIONAL ═══
{pdf_truncado}

═══ COMENTÁRIOS DE REVISÃO ({len(comentarios)} total) ═══
{bloco_comentarios}

═══ TAREFA ═══
Analise a SEQOP acima e seus comentários. Produza um JSON COMPACTO com:

1. "tipo_operacao": string — classificação (ex: "descida_bha_teste_mpd", "perfuracao_mpd")

2. "blocos_mpd": array — blocos/seções RELEVANTES para MPD. Cada item:
   {{"nome": str, "itens": ["17) Testar SSA..."], "rel": "ALTA|MEDIA", "motivo": str curto}}

3. "comentarios": array — para CADA comentário (#0, #1, ...): 
   {{"i": int, "rel": "DIRETA|INDIRETA|NENHUMA", "bloco": str|null,
    "temas": ["sbp","ssa",...], "resumo": str 1 frase, "check": str|null}}
   (check = ponto de verificação acionável: "Verificar se..." ou null)

4. "dados_poco": object — dados extraídos (fase, modo_mpd, fluido_peso, sapata, etc.)
   Inclua só o que estiver disponível.

JSON:
""")


# ── Chamada à API ──────────────────────────────────────────────────────────

def chamar_ia(mensagens: list[dict], max_tokens: int = MAX_COMPLETION_TOKENS) -> str | None:
    """Chama a API com fallback de modelos. Retorna conteúdo ou None."""
    headers = {"Content-Type": "application/json", "api-key": API_KEY}
    payload = {"messages": mensagens, "max_tokens": max_tokens, "temperature": 0.15}

    for modelo in MODELOS:
        url = f"{API_BASE}/engines/{modelo}/chat/completions"
        try:
            resp = requests.post(url, headers=headers, json=payload, timeout=180, verify=False)
            if resp.status_code != 200:
                log.warning(f"  {modelo}: HTTP {resp.status_code}")
                continue
            data = resp.json()
            content = data.get("choices", [{}])[0].get("message", {}).get("content", "")
            usage = data.get("usage", {})
            log.info(f"  ✓ {modelo} – pt={usage.get('prompt_tokens')} ct={usage.get('completion_tokens')}")
            return content
        except requests.exceptions.Timeout:
            log.warning(f"  {modelo}: timeout")
        except Exception as e:
            log.warning(f"  {modelo}: {e}")

    return None


def parse_json_resposta(texto: str) -> dict | None:
    """Tenta extrair JSON da resposta da IA."""
    if not texto:
        return None
    # Direto
    try:
        return json.loads(texto)
    except json.JSONDecodeError:
        pass
    # Extrair bloco JSON
    m = re.search(r'\{.*\}', texto, re.DOTALL)
    if m:
        try:
            return json.loads(m.group())
        except json.JSONDecodeError:
            pass
    # Remover markdown code block
    limpo = re.sub(r'^```json\s*', '', texto.strip())
    limpo = re.sub(r'\s*```$', '', limpo)
    try:
        return json.loads(limpo)
    except json.JSONDecodeError:
        pass
    return None


# ── Pipeline Principal ─────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Enriquecer SEQOPs com IA")
    parser.add_argument("--max", type=int, default=0, help="Máximo de SEQOPs (0=todas)")
    parser.add_argument("--resume", action="store_true", help="Continuar de onde parou")
    args = parser.parse_args()

    # Carregar PDFs
    if not ENTRADA_PDF.exists():
        log.error(f"Rode primeiro: python baixar_pdfs.py")
        sys.exit(1)

    with open(ENTRADA_PDF, "r", encoding="utf-8") as f:
        pdfs = json.load(f)
    pdf_por_mongo = {p["mongo_id"]: p for p in pdfs}
    log.info(f"PDFs carregados: {len(pdfs)}")

    # Carregar comentários
    with open(ENTRADA_COMENT, "r", encoding="utf-8") as f:
        seqops_coment = json.load(f)
    log.info(f"SEQOPs com comentários: {len(seqops_coment)}")

    # Carregar existentes (resume)
    resultados = {}
    if args.resume and SAIDA_JSON.exists():
        with open(SAIDA_JSON, "r", encoding="utf-8") as f:
            existentes = json.load(f)
        # Só considerar como "já feita" se tiver analise_ia válida
        resultados = {
            r.get("mongo_id", r.get("url", "")): r
            for r in existentes
            if isinstance(r.get("analise_ia"), dict) and "blocos_mpd" in r.get("analise_ia", {})
        }
        log.info(f"Já enriquecidas: {len(resultados)} (de {len(existentes)} no JSON)")

    # Processar
    total = len(seqops_coment) if args.max == 0 else min(args.max, len(seqops_coment))
    processadas = 0
    erros = 0
    t0 = time.time()

    log.info("=" * 60)
    log.info(f"ENRIQUECIMENTO IA — {total} SEQOPs")
    log.info("=" * 60)

    for idx, item in enumerate(seqops_coment[:total]):
        url = item.get("url", "")
        mongo_id = ""
        m = re.search(r'([a-f0-9]{24})', url)
        if m:
            mongo_id = m.group(1)

        # Pular já processadas
        if args.resume and (mongo_id in resultados or url in resultados):
            continue

        titulo = item.get("titulo", "?")
        poco = item.get("poco", "?")
        comentarios = item.get("comentarios", [])

        # Texto do PDF
        pdf_info = pdf_por_mongo.get(mongo_id, {})
        texto_pdf = pdf_info.get("texto_pdf", "")

        if not texto_pdf:
            log.warning(f"  [{idx+1}/{total}] SEM PDF: {poco} — {titulo[:50]}")
            texto_pdf = f"[PDF não disponível]\nTítulo: {titulo}\nPoço: {poco}"

        # Parsear seções e montar resumo
        secoes = parsear_secoes(texto_pdf)
        texto_resumido = montar_texto_resumido(secoes, max_chars=MAX_CHARS_RESUMO)
        res_sec = resumo_secoes(secoes)
        n_alta = res_sec["por_relevancia"].get("ALTA", 0)
        hits_total = res_sec.get("total_hits_mpd", 0)

        log.info(f"[{idx+1}/{total}] {poco} — {titulo[:50]} "
                 f"(PDF {len(texto_pdf):,}→{len(texto_resumido):,} chars, "
                 f"{len(secoes)} seções, {n_alta} ALTA, {hits_total} hits MPD, "
                 f"{len(comentarios)} coments)")

        # Montar prompt
        prompt_user = montar_prompt_usuario(
            titulo, poco, texto_resumido, comentarios, res_sec
        )
        mensagens = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt_user},
        ]

        # Chamar IA
        resposta_raw = chamar_ia(mensagens)
        analise = parse_json_resposta(resposta_raw)

        if analise:
            resultado = {
                "mongo_id": mongo_id,
                "url": url,
                "poco": poco,
                "titulo": titulo,
                "n_paginas_pdf": pdf_info.get("n_paginas", 0),
                "n_chars_pdf": len(texto_pdf),
                "n_chars_resumido": len(texto_resumido),
                "n_secoes": len(secoes),
                "n_secoes_alta": n_alta,
                "hits_mpd": hits_total,
                "secoes_resumo": res_sec,
                "n_comentarios_total": len(comentarios),
                "n_comentarios_mpd": sum(1 for c in comentarios if "MPD" in c.get("tipo_csd", "").upper()),
                "analise_ia": analise,
            }
            resultados[mongo_id or url] = resultado
            processadas += 1

            # Contar relevância
            analisados = analise.get("comentarios", analise.get("comentarios_analisados", []))
            diretos = sum(1 for c in analisados if c.get("rel", c.get("relevancia_mpd")) == "DIRETA")
            indiretos = sum(1 for c in analisados if c.get("rel", c.get("relevancia_mpd")) == "INDIRETA")
            n_blocos = len(analise.get("blocos_mpd", []))
            log.info(f"  → {n_blocos} blocos MPD, {diretos} diretos, {indiretos} indiretos")
        else:
            log.error(f"  FALHA IA: resposta inválida")
            resultados[mongo_id or url] = {
                "mongo_id": mongo_id,
                "url": url,
                "poco": poco,
                "titulo": titulo,
                "analise_ia": None,
                "erro": "ia_parse_falhou",
                "resposta_raw": (resposta_raw or "")[:2000],
            }
            erros += 1

        # Progresso
        elapsed = time.time() - t0
        if processadas > 0:
            rate = processadas / elapsed
            remaining = (total - idx - 1) / rate / 60 if rate > 0 else 0
            if processadas % 5 == 0:
                log.info(f"  Progresso: {processadas}/{total} ({elapsed:.0f}s, ETA {remaining:.1f}min)")

        # Salvar a cada 10
        if processadas % 10 == 0 and processadas > 0:
            _salvar(resultados)

        # Rate limit (ser gentil com a API)
        time.sleep(0.5)

    # Salvar final
    _salvar(resultados)
    elapsed = time.time() - t0

    # Estatísticas
    todos = list(resultados.values())
    com_analise = [r for r in todos if r.get("analise_ia")]
    total_blocos = sum(
        len(r.get("analise_ia", {}).get("blocos_mpd", []))
        for r in com_analise
    )
    total_indiretos = sum(
        sum(1 for c in r.get("analise_ia", {}).get("comentarios",
                r.get("analise_ia", {}).get("comentarios_analisados", []))
            if c.get("rel", c.get("relevancia_mpd")) == "INDIRETA")
        for r in com_analise
    )

    log.info(f"\n{'='*60}")
    log.info(f"ENRIQUECIMENTO COMPLETO em {elapsed:.0f}s ({elapsed/60:.1f}min)")
    log.info(f"  Processadas: {processadas}")
    log.info(f"  Erros: {erros}")
    log.info(f"  Total blocos MPD identificados: {total_blocos}")
    log.info(f"  Comentários não-MPD relevantes: {total_indiretos}")
    log.info(f"  JSON: {SAIDA_JSON}")
    log.info("=" * 60)


def _salvar(resultados: dict):
    """Salva resultados no JSON."""
    dados = list(resultados.values())
    with open(SAIDA_JSON, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
