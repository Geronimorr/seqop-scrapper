"""
Classificador de SEQOPs com IA — Etapa 1 da Nova Estratégia
============================================================
Usa a API de IA Petrobras (sem custo) para classificar cada SEQOP por:
  - Tipo de operação (instalação BOP, fingerprint, perfuração, etc.)
  - Fase do poço (superfície, intermediária, produção, completação)
  - Presença de MPD/SBP/FMCD/PMCD
  - Temas dos comentários MPD

O resultado é um corpus CLASSIFICADO e ORGANIZADO, pronto para ser
analisado pelo Claude Opus via GitHub Copilot para gerar o checklist final.

Fases:
  1. Classificação rápida por título (regex + heurística) → 100% dos títulos
  2. Classificação refinada por conteúdo (API) → lotes de SEQOPs por tipo
  3. Extração temática dos comentários MPD (API) → temas e padrões por tipo
  4. Exportar corpus estruturado (JSON + Markdown)

Uso:
    C:\\SharedPython\\venv\\Scripts\\python.exe classificar_seqops.py [opções]

    Opções:
      --skip-api          Usar apenas classificação heurística (sem chamar IA)
      --max-lotes N       Limite de lotes para API (0 = todos)
      --comentarios JSON  Caminho do JSON de comentários (default: comentarios_mpd.json)
      --force             Reclassificar mesmo se já existe resultado

Pré-requisitos:
    - comentarios_mpd.json (saída de coletar_comentarios.py)
    - Acesso à API de IA Petrobras (opcional se --skip-api)
"""

# ── Re-launch com o venv compartilhado ──────────────────────────────────────
import subprocess
import sys
from pathlib import Path

_SHARED_PYTHON = Path(r"C:\SharedPython\venv\Scripts\python.exe")
if _SHARED_PYTHON.exists() and Path(sys.executable).resolve() != _SHARED_PYTHON.resolve():
    print(f"[LAUNCH] Relançando com {_SHARED_PYTHON}")
    result = subprocess.run([str(_SHARED_PYTHON)] + sys.argv, check=False)
    sys.exit(result.returncode)

# ── Imports ─────────────────────────────────────────────────────────────────
import argparse
import io
import json
import logging
import re
import time
from collections import Counter, defaultdict
from datetime import datetime
from textwrap import dedent

import requests

# Prompts centralizados
try:
    from prompts_api import P1_SYSTEM, p1_user_classificacao
    from fluxo_operacoes_mpd import FLUXO_OPERACOES
    _HAS_PROMPTS = True
except ImportError:
    _HAS_PROMPTS = False

# ── Configuração ────────────────────────────────────────────────────────────

SCRIPT_DIR = Path(__file__).resolve().parent

# Entradas
COMENTARIOS_JSON = SCRIPT_DIR / "comentarios_mpd.json"

# Saídas
CLASSIFICACAO_JSON = SCRIPT_DIR / "seqops_classificadas.json"
CORPUS_MD = SCRIPT_DIR / "corpus_seqops_classificado.md"
CORPUS_POR_TIPO_DIR = SCRIPT_DIR / "corpus_por_tipo"
ESTATISTICAS_JSON = SCRIPT_DIR / "estatisticas_seqops.json"

# API de IA
API_BASE = "https://apid.petrobras.com.br/ia/generativos/v1/litellm-chat-petrobras/litellm"
API_KEY = "b320f1f58c9743e9a74048ce64717c89"
MODELO_IA = "gpt-5.1"                       # benchmark: JSON_OK(4p), 1.7s

MODELOS_FALLBACK = [
    MODELO_IA,                               # gpt-5.1        — 1.7s, JSON perfeito
    "qwen3-32b-v1",                          # Qwen 3 32B     — 1.6s, JSON perfeito, outro provider
    "claude-sonnet-4-5",                     # Claude Sonnet 4.5 — 4.1s, JSON extr(4p), robusto
    "gpt-4.1",                               # GPT-4.1        — 1.6s, JSON OK(3p), estável
    "gpt-5.2",                               # GPT-5.2        — 2.2s, JSON OK(4p), mais novo
    "claude-3-7-sonnet",                     # Claude 3.7     — 4.1s, JSON extr(4p), fallback
]

# ── Logging ─────────────────────────────────────────────────────────────────

LOG_FILE = SCRIPT_DIR / "classificar_seqops.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler(
            io.open(sys.stdout.fileno(), mode='w', encoding='utf-8', closefd=False)
        ),
    ],
)
log = logging.getLogger("classificar_seqops")

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# ==========================================================================
#  FASE 1: CLASSIFICAÇÃO HEURÍSTICA (por título — sem API)
# ==========================================================================

# Mapeamento de padrões de título → tipo de operação
TIPOS_OPERACAO = {
    "instalacao_bop": {
        "nome": "Instalação / Descida do BOP",
        "descricao": "Descida, montagem e instalação do BOP com junta integrada de MPD",
        "patterns": [
            r"descida.*bop",
            r"instala[cç][aã]o.*bop",
            r"bop.*junta\s*(integrada|mpd)",
            r"junta\s*integrada",
            r"navega[cç][aã]o.*bop",
            r"dmm.*bop",
            r"desconex[aã]o.*bop",
            r"retirada.*bop",
            r"reconex[aã]o.*lmrp",
            r"retirada.*lmrp",
        ],
    },
    "descida_bha_teste": {
        "nome": "Descida de BHA e Teste do MPD/BOP",
        "descricao": "Montagem e descida de BHA com testes de BOP e/ou sistema MPD",
        "patterns": [
            r"descida.*bha.*test",
            r"montagem.*bha.*test",
            r"descida.*bha.*\d",
            r"montagem.*bha.*\d",
            r"descida\s+de?\s*bha",
            r"montagem.*descida.*bha",
            r"bha.*liso",
        ],
    },
    "fingerprint": {
        "nome": "Fingerprint / Treinamento MPD",
        "descricao": "Fingerprint do sistema MPD, MPD drill, choke drill e treinamento prático",
        "patterns": [
            r"fingerprint",
            r"treinamento\s*(pr[aá]tico|mpd)",
            r"mpd\s*drill",
            r"choke\s*drill",
        ],
    },
    "corte_cimento_fit": {
        "nome": "Corte de Cimento / FIT / DLOT / DFIT",
        "descricao": "Corte de cimento, teste de integridade (FIT/LOT/DLOT/DFIT), troca de fluido associada",
        "patterns": [
            r"corte\s*(de\s*)?cimento",
            r"\bfit\b",
            r"\bdlot\b",
            r"\bdfit\b",
            r"\blot\b",
            r"microfrac",
        ],
    },
    "troca_fluido": {
        "nome": "Troca de Fluido / Condicionamento",
        "descricao": "Troca de fluido, condicionamento de poço, substituição de fluido em modo MPD, preparação para perfurar",
        "patterns": [
            r"troca\s*(de\s*)?fluido",
            r"substitui[cç][aã]o.*fluido",
            r"condicionamento",
            r"amortecimento",
            r"rebaixamento.*cimento",
            r"preparar\s*para\s*perfurar",
        ],
    },
    "perfuracao": {
        "nome": "Perfuração com MPD",
        "descricao": "Perfuração de fases (16\", 12¼\", 8½\") em modo MPD/SBP",
        "patterns": [
            r"perfura[cç][aã]o\s*\d",
            r"perfura[cç][aã]o\s*fase",
            r"perfura[cç][aã]o\s*da\s*fase",
            r"perfura[cç][aã]o.*mpd",
            r"prosseguimento.*perfura",
            r"sidetrack.*perfura",
        ],
    },
    "teste_influxo": {
        "nome": "Teste de Influxo / Teste BOP",
        "descricao": "Testes de influxo, teste periódico do BOP, teste com ITT/PUAO",
        "patterns": [
            r"teste\s*(de\s*)?influxo",
            r"teste.*bop.*itt",
            r"teste\s*peri[oó]dico.*bop",
            r"teste.*bsr",
            r"teste.*mpd.*corte",
        ],
    },
    "contingencia_pmcd_fmcd": {
        "nome": "Contingência / FMCD / PMCD",
        "descricao": "Perfuração em FMCD, PMCD, combate à perda, contingências MPD",
        "patterns": [
            r"conting[eê]ncia",
            r"contingencia",
            r"\bfmcd\b",
            r"\bpmcd\b",
            r"combate.*perda",
            r"lcm",
            r"convers[aã]o.*pmcd",
            r"convers[aã]o.*fmcd",
        ],
    },
    "testemunhagem": {
        "nome": "Testemunhagem com MPD",
        "descricao": "Operações de testemunhagem em modo MPD",
        "patterns": [
            r"testemunhagem",
        ],
    },
    "completacao_paci": {
        "nome": "Completação / PACI / Cauda",
        "descricao": "Instalação de cauda PACI, completação inferior, operações de completação em FMCD",
        "patterns": [
            r"\bpaci\b",
            r"cauda",
            r"completa[cç][aã]o\s*inferior",
            r"estimula[cç][aã]o",
            r"fechamento.*vif",
            r"ajuste.*ssd",
            r"manobra.*mpd.*sbp",
        ],
    },
    "retirada_bha": {
        "nome": "Retirada de BHA / Manobra",
        "descricao": "Retirada de BHA, manobra para troca de broca, condicionamento pós-perfilagem",
        "patterns": [
            r"retirada.*bha",
            r"manobra.*troca.*broca",
            r"condicionamento.*p[oó]s.*perfil",
            r"condicionamento.*perfil",
            r"descida.*ap[oó]s\s*(troca|perfil)",
        ],
    },
    "pescaria": {
        "nome": "Pescaria / Recuperação",
        "descricao": "Operações de pescaria e recuperação de equipamentos",
        "patterns": [
            r"pescaria",
            r"recupera[cç][aã]o",
        ],
    },
    "tampao_abandono": {
        "nome": "Tampão / Abandono",
        "descricao": "Tampão de cimento, abandono temporário, desvio",
        "patterns": [
            r"tamp[aã]o",
            r"abandono",
            r"desvio",
            r"bullheading",
        ],
    },
}

# Detecção de fase do poço
FASES_POCO = {
    "superficie": [r"16[\"\s]*pol", r"16[\"\s]*\"", r"fase\s*(iii|3|16)", r"bha\s*16"],
    "intermediaria": [r"12[\.,]?\s*25|12\s*1/4|12¼|13[\.,]?\s*5|13\s*1/2|14\s*3/4", r"fase\s*(iv|4)"],
    "producao": [r"8[\.,]?\s*5|8\s*1/2|8½|9[\.,]?\s*5|9\s*\"", r"fase\s*(v|5)"],
    "completacao": [r"paci|cauda|completa[cç]|vif|ssd|estimula"],
}

# Detecção de modo MPD
MODOS_MPD = {
    "MPD": [r"\bmpd\b"],
    "SBP": [r"\bsbp\b"],
    "FMCD": [r"\bfmcd\b"],
    "PMCD": [r"\bpmcd\b"],
    "MCD": [r"\bmcd\b"],
}


def classificar_por_titulo(titulo: str) -> dict:
    """Classifica uma SEQOP por padrões no título (heurística rápida)."""
    titulo_lower = titulo.lower().strip()
    resultado = {
        "tipos": [],
        "fase_poco": "indefinida",
        "modos_mpd": [],
        "eh_contingencia": False,
    }

    # Detectar tipo(s) de operação
    for tipo_id, tipo_info in TIPOS_OPERACAO.items():
        for pattern in tipo_info["patterns"]:
            if re.search(pattern, titulo_lower, re.IGNORECASE):
                if tipo_id not in resultado["tipos"]:
                    resultado["tipos"].append(tipo_id)
                break

    # Se não encontrou nenhum tipo, marcar como "nao_classificado"
    if not resultado["tipos"]:
        resultado["tipos"] = ["nao_classificado"]

    # Detectar fase do poço
    for fase, patterns in FASES_POCO.items():
        for pattern in patterns:
            if re.search(pattern, titulo_lower, re.IGNORECASE):
                resultado["fase_poco"] = fase
                break
        if resultado["fase_poco"] != "indefinida":
            break

    # Detectar modos MPD
    for modo, patterns in MODOS_MPD.items():
        for pattern in patterns:
            if re.search(pattern, titulo_lower, re.IGNORECASE):
                if modo not in resultado["modos_mpd"]:
                    resultado["modos_mpd"].append(modo)
                break

    # Detectar contingência
    if re.search(r"conting[eê]ncia|contingencia|\[conting", titulo_lower, re.IGNORECASE):
        resultado["eh_contingencia"] = True

    return resultado


def classificar_por_conteudo(conteudo: str, titulo: str) -> dict:
    """Enriquece classificação analisando o conteúdo da SEQOP."""
    conteudo_lower = (conteudo or "").lower()
    titulo_lower = titulo.lower()
    texto = f"{titulo_lower} {conteudo_lower}"

    extras = {
        "temas_conteudo": [],
        "equipamentos_mencionados": [],
        "normas_mencionadas": [],
    }

    # Temas detectáveis no conteúdo
    temas = {
        "teste_pressao": r"teste\s*(de\s*)?press[aã]o|test[ea]r.*v[aá]lvula",
        "calibracao_pid": r"calibra[cç][aã]o.*pid|pid.*calibra|ajust.*efici[eê]ncia.*bomb",
        "fluxograma": r"fluxograma|flowchart",
        "controle_poco": r"controle\s*(de\s*)?po[cç]o|kick|influxo|well\s*control",
        "perda_circulacao": r"perda\s*(de\s*)?(circula|retorno)|lost.*circulat|lcm|barab",
        "buffer_manifold": r"buffer|manifold|p&id|pid.*genéric",
        "envelope_operacional": r"envelope\s*operacional|limites.*opera",
        "vedacao": r"veda[cç][aã]o|packer|seal|bearing|rbp|rcd",
        "cimentacao": r"cimenta[cç][aã]o|ciment[oa]|sapata",
        "perfilagem": r"perfilagem|logging|relogging",
    }
    for tema_id, pattern in temas.items():
        if re.search(pattern, texto, re.IGNORECASE):
            extras["temas_conteudo"].append(tema_id)

    # Equipamentos MPD
    equipamentos = {
        "RCD": r"\brcd\b",
        "BA (Barreira Anular)": r"\bba\b.*barreir|\bbarreira\s*anular",
        "Choke MPD": r"choke\s*mpd|mpd\s*choke",
        "Booster": r"\bbooster\b",
        "Well Defender": r"well\s*defender",
        "DSIT": r"\bdsit\b",
        "PBL": r"\bpbl\b",
        "MPDV": r"\bmpdv\d*",
        "BOP": r"\bbop\b",
        "Junta Integrada": r"junta\s*(integrada|mpd|jir)",
    }
    for equip, pattern in equipamentos.items():
        if re.search(pattern, texto, re.IGNORECASE):
            extras["equipamentos_mencionados"].append(equip)

    # Normas/padrões
    normas = re.findall(r"PE-\d[A-Z]{3}-\d{5}", texto, re.IGNORECASE)
    extras["normas_mencionadas"] = list(set(normas))

    return extras


# ==========================================================================
#  FASE 2: CLASSIFICAÇÃO REFINADA COM API (por lotes temáticos)
# ==========================================================================

def _chamar_ia(mensagens: list[dict], max_tokens: int = 4096, temperature: float = 0.2) -> str:
    """Chama a API de IA generativa. Tenta múltiplos modelos."""
    headers = {
        "Content-Type": "application/json",
        "api-key": API_KEY,
    }
    payload = {
        "messages": mensagens,
        "max_tokens": max_tokens,
        "temperature": temperature,
    }

    for modelo in MODELOS_FALLBACK:
        url = f"{API_BASE}/engines/{modelo}/chat/completions"
        log.info(f"  → Chamando modelo: {modelo}")

        try:
            resp = requests.post(url, headers=headers, json=payload, timeout=180, verify=False)
            if resp.status_code != 200:
                log.warning(f"    {modelo}: HTTP {resp.status_code} – {resp.text[:200]}")
                continue

            data = resp.json()
            choices = data.get("choices", [])
            if not choices:
                log.warning(f"    {modelo}: Resposta sem choices")
                continue

            content = choices[0].get("message", {}).get("content", "")
            usage = data.get("usage", {})
            log.info(f"    ✓ {modelo} – tokens: {usage.get('prompt_tokens')}/{usage.get('completion_tokens')}")
            return content

        except requests.exceptions.Timeout:
            log.warning(f"    {modelo}: Timeout")
        except Exception as e:
            log.warning(f"    {modelo}: Erro – {e}")

    raise RuntimeError(f"Todos os modelos falharam: {MODELOS_FALLBACK}")


def refinar_classificacao_ia(seqops_por_tipo: dict[str, list]) -> dict[str, list]:
    """Usa IA para refinar classficação, identificar sub-tipos e extrair temas dos comentários."""
    log.info("=" * 60)
    log.info("FASE 2: Refinamento com IA")
    log.info("=" * 60)

    resultados = {}

    for tipo_id, seqops in seqops_por_tipo.items():
        if not seqops:
            continue

        tipo_nome = TIPOS_OPERACAO.get(tipo_id, {}).get("nome", tipo_id)
        log.info(f"\n  Tipo: {tipo_nome} ({len(seqops)} SEQOPs)")

        # Montar resumo dos comentários MPD deste tipo
        comentarios_bloco = []
        chars = 0
        for seq in seqops:
            for c in seq.get("comentarios_mpd", []):
                if c.get("texto"):
                    bloco = (
                        f"[{seq['poco']} | {seq['titulo'][:60]}]\n"
                        f"Autor: {c.get('autor', '?')} | Versão: {c.get('versao', '?')}\n"
                        f"{c['texto']}\n"
                    )
                    if c.get("respostas"):
                        for r in c["respostas"]:
                            bloco += f"  → Resposta ({r.get('autor','?')}): {r.get('texto','')}\n"
                    bloco += "---\n"

                    if chars + len(bloco) > 60000:
                        break
                    comentarios_bloco.append(bloco)
                    chars += len(bloco)

        if not comentarios_bloco:
            log.info(f"    Sem comentários MPD para este tipo. Pulando IA.")
            resultados[tipo_id] = {
                "tipo_id": tipo_id,
                "tipo_nome": tipo_nome,
                "total_seqops": len(seqops),
                "total_comentarios_mpd": 0,
                "analise_ia": None,
            }
            continue

        log.info(f"    {len(comentarios_bloco)} comentários MPD ({chars} chars)")

        # Determinar posição no fluxo operacional
        posicao_fluxo = 0
        if _HAS_PROMPTS:
            for op in FLUXO_OPERACOES:
                if op["aba_id"] == tipo_id:
                    posicao_fluxo = op["ordem"]
                    break

        if _HAS_PROMPTS and posicao_fluxo > 0:
            # Usar prompts melhorados com contexto do fluxo operacional
            system_msg = P1_SYSTEM
            prompt = p1_user_classificacao(tipo_nome, len(comentarios_bloco), posicao_fluxo)
        else:
            # Fallback: prompt original (para tipos sem posição no fluxo)
            system_msg = "Responda SOMENTE em JSON válido, em português. Sem markdown, sem ```json."
            prompt = dedent(f"""\
            Você é um especialista em perfuração MPD (Managed Pressure Drilling) da Petrobras.

            Abaixo estão {len(comentarios_bloco)} comentários REAIS de revisores CSD-MPD sobre SEQOPs
            do tipo: **{tipo_nome}**

            TAREFA: Analise os comentários e extraia:

            1. **sub_tipos**: Identifique sub-categorias dentro deste tipo de operação
            2. **pontos_verificacao**: Os itens que o revisor MPD MAIS cobra/verifica
            3. **erros_frequentes**: Erros ou omissões recorrentes que o revisor encontra
            4. **padroes_aprovacao**: O que o revisor gosta de ver (boas práticas)
            5. **normas_aplicaveis**: Normas/padrões técnicos mencionados ou implícitos

            Responda EXCLUSIVAMENTE em JSON válido:
            {{
              "sub_tipos": ["sub-tipo 1", "sub-tipo 2"],
              "pontos_verificacao": [
                {{
                  "item": "Descrição da verificação",
                  "frequencia": "alta/media/baixa",
                  "exemplo_real": "Trecho do comentário que motivou este ponto"
                }}
              ],
              "erros_frequentes": ["erro 1", "erro 2"],
              "padroes_aprovacao": ["boa prática 1"],
              "normas_aplicaveis": ["PE-2POC-01113"]
            }}

            COMENTÁRIOS:
            """)

        try:
            resposta = _chamar_ia([
                {"role": "system", "content": system_msg},
                {"role": "user", "content": prompt + "\n".join(comentarios_bloco)},
            ], max_tokens=6000)

            # Parsear JSON
            json_match = re.search(r'\{.*\}', resposta, re.DOTALL)
            if json_match:
                analise = json.loads(json_match.group())
            else:
                analise = {"raw": resposta}

            resultados[tipo_id] = {
                "tipo_id": tipo_id,
                "tipo_nome": tipo_nome,
                "total_seqops": len(seqops),
                "total_comentarios_mpd": len(comentarios_bloco),
                "analise_ia": analise,
            }
            log.info(f"    ✓ Análise concluída: {len(analise.get('pontos_verificacao', []))} pontos")

        except Exception as e:
            log.error(f"    ✗ Erro na análise: {e}")
            resultados[tipo_id] = {
                "tipo_id": tipo_id,
                "tipo_nome": tipo_nome,
                "total_seqops": len(seqops),
                "total_comentarios_mpd": len(comentarios_bloco),
                "analise_ia": None,
                "erro": str(e),
            }

        # Pausa entre chamadas para não sobrecarregar
        time.sleep(2)

    return resultados


# ==========================================================================
#  FASE 3: EXPORTAR CORPUS ESTRUTURADO
# ==========================================================================

def gerar_estatisticas(seqops_classificadas: list[dict]) -> dict:
    """Gera estatísticas detalhadas da classificação."""
    stats = {
        "total_seqops": len(seqops_classificadas),
        "total_comentarios": sum(s.get("total_comentarios", 0) for s in seqops_classificadas),
        "total_comentarios_mpd": sum(s.get("total_mpd", 0) for s in seqops_classificadas),
        "por_tipo": Counter(),
        "por_fase": Counter(),
        "por_modo_mpd": Counter(),
        "contingencias": 0,
        "pocos_unicos": set(),
        "seqops_sem_comentario_mpd": 0,
        "distribuicao_comentarios": {},
    }

    for s in seqops_classificadas:
        classificacao = s.get("classificacao", {})

        for tipo in classificacao.get("tipos", ["nao_classificado"]):
            stats["por_tipo"][tipo] += 1

        stats["por_fase"][classificacao.get("fase_poco", "indefinida")] += 1

        for modo in classificacao.get("modos_mpd", []):
            stats["por_modo_mpd"][modo] += 1

        if classificacao.get("eh_contingencia"):
            stats["contingencias"] += 1

        stats["pocos_unicos"].add(s.get("poco", ""))

        if s.get("total_mpd", 0) == 0:
            stats["seqops_sem_comentario_mpd"] += 1

    stats["pocos_unicos"] = sorted(stats["pocos_unicos"])
    stats["total_pocos"] = len(stats["pocos_unicos"])

    # Converter Counters para dict serializável
    stats["por_tipo"] = dict(stats["por_tipo"].most_common())
    stats["por_fase"] = dict(stats["por_fase"].most_common())
    stats["por_modo_mpd"] = dict(stats["por_modo_mpd"].most_common())

    return stats


def exportar_corpus_markdown(seqops_classificadas: list[dict], analise_ia: dict):
    """Exporta corpus completo em Markdown, organizado por tipo, pronto para o Claude Opus."""
    log.info("Exportando corpus em Markdown...")

    # ── Arquivo consolidado ────────────────────────────────────────
    linhas = [
        "# Corpus Classificado de SEQOPs — CSD-MPD Petrobras",
        f"\nGerado em: {datetime.now().strftime('%d/%m/%Y %H:%M')}",
        f"\nTotal: {len(seqops_classificadas)} SEQOPs",
        "",
    ]

    # Agrupar por tipo principal
    por_tipo = defaultdict(list)
    for s in seqops_classificadas:
        tipo_principal = (s.get("classificacao", {}).get("tipos", ["nao_classificado"]))[0]
        por_tipo[tipo_principal].append(s)

    # Sumário
    linhas.append("## Sumário por Tipo de Operação\n")
    linhas.append("| Tipo | Qtd SEQOPs | Qtd Comentários MPD | Poços |")
    linhas.append("|------|-----------|---------------------|-------|")

    for tipo_id, seqops in sorted(por_tipo.items(), key=lambda x: -len(x[1])):
        tipo_nome = TIPOS_OPERACAO.get(tipo_id, {}).get("nome", tipo_id)
        total_mpd = sum(s.get("total_mpd", 0) for s in seqops)
        pocos = sorted(set(s.get("poco", "") for s in seqops))
        linhas.append(f"| {tipo_nome} | {len(seqops)} | {total_mpd} | {', '.join(pocos[:5])}{'...' if len(pocos) > 5 else ''} |")

    linhas.append("")

    # ── Seções por tipo ────────────────────────────────────────────
    for tipo_id, seqops in sorted(por_tipo.items(), key=lambda x: -len(x[1])):
        tipo_nome = TIPOS_OPERACAO.get(tipo_id, {}).get("nome", tipo_id)
        tipo_descricao = TIPOS_OPERACAO.get(tipo_id, {}).get("descricao", "")

        linhas.append(f"---\n## {tipo_nome}")
        linhas.append(f"*{tipo_descricao}*\n")
        linhas.append(f"**{len(seqops)} SEQOPs** | "
                      f"{sum(s.get('total_mpd', 0) for s in seqops)} comentários MPD\n")

        # Análise IA se disponível
        ia_result = analise_ia.get(tipo_id, {})
        ia_data = ia_result.get("analise_ia")
        if ia_data and isinstance(ia_data, dict):
            # Sub-tipos
            if ia_data.get("sub_tipos"):
                linhas.append("### Sub-tipos identificados")
                for st in ia_data["sub_tipos"]:
                    linhas.append(f"- {st}")
                linhas.append("")

            # Pontos de verificação
            if ia_data.get("pontos_verificacao"):
                linhas.append("### Pontos de Verificação (extraídos dos comentários reais)")
                for pv in ia_data["pontos_verificacao"]:
                    freq = pv.get("frequencia", "?")
                    linhas.append(f"- **[{freq.upper()}]** {pv.get('item', '')}")
                    exemplo = pv.get("exemplo_real", "")
                    if exemplo:
                        linhas.append(f'  > *"{exemplo}"*')
                linhas.append("")

            # Erros
            if ia_data.get("erros_frequentes"):
                linhas.append("### Erros Frequentes")
                for e in ia_data["erros_frequentes"]:
                    linhas.append(f"- ⚠ {e}")
                linhas.append("")

            # Boas práticas
            if ia_data.get("padroes_aprovacao"):
                linhas.append("### Boas Práticas (padrões de aprovação)")
                for bp in ia_data["padroes_aprovacao"]:
                    linhas.append(f"- ✓ {bp}")
                linhas.append("")

            # Normas
            if ia_data.get("normas_aplicaveis"):
                linhas.append(f"### Normas Aplicáveis: {', '.join(ia_data['normas_aplicaveis'])}")
                linhas.append("")

        # Lista de SEQOPs
        linhas.append("### SEQOPs neste tipo")
        linhas.append("")

        for s in sorted(seqops, key=lambda x: x.get("poco", "")):
            titulo = s.get("titulo", "")
            poco = s.get("poco", "")
            total_mpd = s.get("total_mpd", 0)
            fase = s.get("classificacao", {}).get("fase_poco", "?")
            eh_cont = "🔴 CONTINGÊNCIA" if s.get("classificacao", {}).get("eh_contingencia") else ""

            linhas.append(f"#### {poco} — {titulo} {eh_cont}")
            linhas.append(f"Fase: {fase} | Comentários MPD: {total_mpd}")

            # Comentários MPD
            for c in s.get("comentarios_mpd", []):
                if c.get("texto"):
                    autor = c.get("autor", "?")
                    versao = c.get("versao", "?")
                    texto = c["texto"].replace("\n", "\n> ")
                    linhas.append(f"\n**{autor}** (v{versao}):")
                    linhas.append(f"> {texto}")

                    for r in c.get("respostas", []):
                        if r.get("texto"):
                            r_autor = r.get("autor", "?")
                            r_texto = r["texto"].replace("\n", "\n>> ")
                            linhas.append(f">> **↳ {r_autor}:** {r_texto}")

            linhas.append("")

    texto_md = "\n".join(linhas)
    CORPUS_MD.write_text(texto_md, encoding="utf-8")
    log.info(f"  Corpus MD salvo: {CORPUS_MD} ({len(texto_md)} chars)")

    # ── Arquivos por tipo (para facilitar carga parcial no Claude Opus) ──
    CORPUS_POR_TIPO_DIR.mkdir(exist_ok=True)
    for tipo_id, seqops in por_tipo.items():
        tipo_linhas = []
        tipo_nome = TIPOS_OPERACAO.get(tipo_id, {}).get("nome", tipo_id)

        tipo_linhas.append(f"# {tipo_nome}")
        tipo_linhas.append(f"\n{len(seqops)} SEQOPs | "
                           f"{sum(s.get('total_mpd', 0) for s in seqops)} comentários MPD\n")

        # Incluir análise IA
        ia_result = analise_ia.get(tipo_id, {})
        ia_data = ia_result.get("analise_ia")
        if ia_data and isinstance(ia_data, dict):
            tipo_linhas.append("## Análise IA dos Comentários\n")
            tipo_linhas.append(f"```json\n{json.dumps(ia_data, ensure_ascii=False, indent=2)}\n```\n")

        # Todos os comentários MPD deste tipo
        tipo_linhas.append("## Comentários MPD Completos\n")
        for s in sorted(seqops, key=lambda x: x.get("poco", "")):
            for c in s.get("comentarios_mpd", []):
                if c.get("texto"):
                    tipo_linhas.append(f"### {s['poco']} — {s['titulo'][:60]}")
                    tipo_linhas.append(f"**{c.get('autor', '?')}** | v{c.get('versao', '?')}")
                    tipo_linhas.append(f"\n{c['texto']}\n")
                    for r in c.get("respostas", []):
                        if r.get("texto"):
                            tipo_linhas.append(f"> ↳ **{r.get('autor','?')}:** {r['texto']}\n")

        path = CORPUS_POR_TIPO_DIR / f"{tipo_id}.md"
        path.write_text("\n".join(tipo_linhas), encoding="utf-8")

    log.info(f"  Corpus por tipo salvo em: {CORPUS_POR_TIPO_DIR}/")


# ==========================================================================
#  PIPELINE PRINCIPAL
# ==========================================================================

def main():
    parser = argparse.ArgumentParser(description="Classificador de SEQOPs com IA")
    parser.add_argument("--skip-api", action="store_true",
                        help="Usar apenas classificação heurística")
    parser.add_argument("--max-lotes", type=int, default=0,
                        help="Limite de lotes para API (0 = todos)")
    parser.add_argument("--comentarios", type=str, default="",
                        help="Caminho do JSON de comentários")
    parser.add_argument("--force", action="store_true",
                        help="Reclassificar mesmo se já existe resultado")
    args = parser.parse_args()

    log.info("=" * 60)
    log.info("CLASSIFICADOR DE SEQOPs — Nova Estratégia")
    log.info(f"Data/hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    log.info("=" * 60)

    # ── Carregar comentários ─────────────────────────────────────────
    json_path = Path(args.comentarios) if args.comentarios else COMENTARIOS_JSON
    if not json_path.exists():
        log.error(f"Arquivo não encontrado: {json_path}")
        log.error("Execute primeiro: coletar_comentarios.py")
        return

    log.info(f"Carregando: {json_path}")
    with open(json_path, "r", encoding="utf-8") as f:
        dados = json.load(f)
    log.info(f"  {len(dados)} SEQOPs carregadas")

    # ── Verificar se já existe classificação ─────────────────────────
    if CLASSIFICACAO_JSON.exists() and not args.force:
        log.info(f"Classificação existente encontrada: {CLASSIFICACAO_JSON}")
        log.info("Use --force para reclassificar.")

        # Carregar existente e regenerar exports
        with open(CLASSIFICACAO_JSON, "r", encoding="utf-8") as f:
            resultado_salvo = json.load(f)
        seqops_classificadas = resultado_salvo.get("seqops", dados)
        analise_ia = resultado_salvo.get("analise_ia", {})

        # Regenerar Markdown
        exportar_corpus_markdown(seqops_classificadas, analise_ia)

        log.info("Corpus atualizado com classificação existente.")
        return

    # ── FASE 1: Classificação heurística ─────────────────────────────
    log.info("\n" + "=" * 60)
    log.info("FASE 1: Classificação heurística por título e conteúdo")
    log.info("=" * 60)

    for s in dados:
        titulo = s.get("titulo", "")
        conteudo = s.get("conteudo_seqop", "")

        # Classificação por título
        classif = classificar_por_titulo(titulo)

        # Enriquecer com análise de conteúdo
        extras = classificar_por_conteudo(conteudo, titulo)
        classif.update(extras)

        s["classificacao"] = classif

    # Estatísticas pós-classificação
    stats = gerar_estatisticas(dados)

    log.info(f"\n  Distribuição por tipo:")
    for tipo, qtd in stats["por_tipo"].items():
        nome = TIPOS_OPERACAO.get(tipo, {}).get("nome", tipo)
        log.info(f"    {nome}: {qtd}")

    log.info(f"\n  Distribuição por fase:")
    for fase, qtd in stats["por_fase"].items():
        log.info(f"    {fase}: {qtd}")

    log.info(f"\n  Modos MPD detectados:")
    for modo, qtd in stats["por_modo_mpd"].items():
        log.info(f"    {modo}: {qtd}")

    log.info(f"  Contingências: {stats['contingencias']}")
    log.info(f"  SEQOPs sem comentário MPD: {stats['seqops_sem_comentario_mpd']}")
    log.info(f"  Poços únicos: {stats['total_pocos']}")

    # ── FASE 2: Refinamento com IA ───────────────────────────────────
    analise_ia = {}

    if not args.skip_api:
        # Agrupar por tipo principal
        por_tipo = defaultdict(list)
        for s in dados:
            tipo_principal = s["classificacao"]["tipos"][0]
            por_tipo[tipo_principal].append(s)

        # Filtrar tipos com comentários MPD
        tipos_com_mpd = {
            k: v for k, v in por_tipo.items()
            if any(s.get("total_mpd", 0) > 0 for s in v)
        }

        if args.max_lotes > 0:
            # Limitar aos N tipos com mais comentários
            tipos_ordenados = sorted(
                tipos_com_mpd.items(),
                key=lambda x: sum(s.get("total_mpd", 0) for s in x[1]),
                reverse=True,
            )[:args.max_lotes]
            tipos_com_mpd = dict(tipos_ordenados)

        log.info(f"\n  Tipos com comentários MPD: {len(tipos_com_mpd)}")
        analise_ia = refinar_classificacao_ia(tipos_com_mpd)
    else:
        log.info("\n  Pulando refinamento IA (--skip-api)")

    # ── FASE 3: Salvar resultado completo ────────────────────────────
    log.info("\n" + "=" * 60)
    log.info("FASE 3: Exportando corpus classificado")
    log.info("=" * 60)

    resultado = {
        "data_classificacao": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "estatisticas": stats,
        "analise_ia": analise_ia,
        "seqops": dados,
    }

    with open(CLASSIFICACAO_JSON, "w", encoding="utf-8") as f:
        json.dump(resultado, f, ensure_ascii=False, indent=2)
    log.info(f"  Classificação salva: {CLASSIFICACAO_JSON}")

    with open(ESTATISTICAS_JSON, "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)
    log.info(f"  Estatísticas salvas: {ESTATISTICAS_JSON}")

    # Exportar corpus em Markdown
    exportar_corpus_markdown(dados, analise_ia)

    # ── Resumo final ─────────────────────────────────────────────────
    log.info("\n" + "=" * 60)
    log.info("CLASSIFICAÇÃO CONCLUÍDA!")
    log.info("=" * 60)
    log.info(f"  {len(dados)} SEQOPs classificadas")
    log.info(f"  {len(analise_ia)} tipos analisados com IA")
    log.info(f"\nArquivos gerados:")
    log.info(f"  JSON:        {CLASSIFICACAO_JSON}")
    log.info(f"  Estatísticas: {ESTATISTICAS_JSON}")
    log.info(f"  Corpus MD:   {CORPUS_MD}")
    log.info(f"  Corpus Tipo: {CORPUS_POR_TIPO_DIR}/")
    log.info(f"\n{'=' * 60}")
    log.info("PRÓXIMO PASSO:")
    log.info("  Abra o corpus_seqops_classificado.md ou os arquivos em")
    log.info("  corpus_por_tipo/ e envie para o Claude Opus via GitHub Copilot")
    log.info("  para gerar o checklist final.")
    log.info("=" * 60)


if __name__ == "__main__":
    main()
