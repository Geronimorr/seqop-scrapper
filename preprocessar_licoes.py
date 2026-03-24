"""
Pré-processador de Lições Aprendidas de MPD
============================================
Filtra, categoriza e agrega as lições aprendidas relevantes a MPD de um CSV
exportado do sistema Lessons Petrobras.

Saída: licoes_aprendidas_mpd.json — pronto para alimentar gerar_checklist_combinado.py

Usa apenas Python puro (sem chamadas de IA).

Uso:
    C:\\SharedPython\\venv\\Scripts\\python.exe preprocessar_licoes.py [--csv CAMINHO]
"""

# ── Re-launch com venv ──────────────────────────────────────────────────────
import subprocess, sys
from pathlib import Path

_SHARED_PYTHON = Path(r"C:\SharedPython\venv\Scripts\python.exe")
if _SHARED_PYTHON.exists() and Path(sys.executable).resolve() != _SHARED_PYTHON.resolve():
    print(f"[LAUNCH] Relançando com {_SHARED_PYTHON}")
    result = subprocess.run([str(_SHARED_PYTHON)] + sys.argv, check=False)
    sys.exit(result.returncode)

# ── Imports ─────────────────────────────────────────────────────────────────
import argparse
import csv
import json
import re
import unicodedata
from collections import defaultdict, Counter
from datetime import datetime

SCRIPT_DIR = Path(__file__).resolve().parent

# ── Encoding console ────────────────────────────────────────────────────────
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', closefd=False)
sys.stderr = open(sys.stderr.fileno(), mode='w', encoding='utf-8', closefd=False)


# ==========================================================================
#  CONFIGURAÇÃO DE CATEGORIAS – Mapeamento por keywords
# ==========================================================================

# Cada categoria tem um ID, nome, e conjuntos de keywords para classificar.
# A ordem importa: regras mais específicas vêm antes.

CATEGORIAS = [
    {
        "id": "CAT-02",
        "nome": "Perfuração FMCD",
        "keywords_must": ["fmcd"],
        "keywords_any": ["perfura", "drill", "fase", "broca", "bha", "riser"],
        "keywords_not": ["descida de cauda", "completação inferior", "cauda"],
    },
    {
        "id": "CAT-03",
        "nome": "Perfuração PMCD",
        "keywords_must": ["pmcd"],
        "keywords_any": ["perfura", "drill", "fase", "broca", "bha", "nível"],
        "keywords_not": ["descida de cauda", "completação inferior", "cauda"],
    },
    {
        "id": "CAT-06",
        "nome": "Descida de cauda em FMCD",
        "keywords_must": ["fmcd"],
        "keywords_any": ["cauda", "completação inferior", "paci", "packer", "descida"],
    },
    {
        "id": "CAT-07",
        "nome": "Descida da Cauda em PMCD",
        "keywords_must": ["pmcd"],
        "keywords_any": ["cauda", "completação inferior", "paci", "packer", "descida"],
    },
    {
        "id": "CAT-08",
        "nome": "Descida da cauda em MPD",
        "keywords_must": [],
        "keywords_any": ["cauda", "completação inferior", "paci", "packer seal"],
        "keywords_context": ["mpd"],
        "keywords_not": ["fmcd", "pmcd"],
    },
    {
        "id": "CAT-05",
        "nome": "Instalação da Junta Integrada",
        "keywords_must": [],
        "keywords_any": [
            "junta integrada", "bearing assembly", "rcd", "rotating control",
            "riser", "junta de manuseio", "flowspool", "flow spool",
        ],
    },
    {
        "id": "CAT-04",
        "nome": "Fingerprint",
        "keywords_must": [],
        "keywords_any": ["fingerprint", "finger print", "baseline", "base line", "calibra"],
        "keywords_context": ["mpd"],
    },
    {
        "id": "CAT-09",
        "nome": "DPPT",
        "keywords_must": [],
        "keywords_any": [
            "dppt", "teste de pressão", "drill pipe pressure test",
            "teste de estanqueidade", "teste de barreira",
        ],
        "keywords_context": ["mpd", "fmcd", "pmcd"],
    },
    {
        "id": "CAT-10",
        "nome": "DFIT",
        "keywords_must": [],
        "keywords_any": [
            "dfit", "mini-frac", "minifrac", "mini frac", "leak-off",
            "leakoff", "fraturamento", "teste de integridade", "fit",
            "teste de absorção", "teste de admissão",
        ],
        "keywords_context": ["mpd", "fmcd", "pmcd"],
    },
    {
        "id": "CAT-11",
        "nome": "Circulação de influxo MPD",
        "keywords_must": [],
        "keywords_any": [
            "influxo", "kick", "circulação de influxo", "bullheading",
            "well control", "controle de poço", "fechamento de poço",
            "shut-in", "kill", "gas", "gás",
        ],
        "keywords_context": ["mpd"],
    },
    {
        "id": "CAT-01",
        "nome": "Perfuração MPD (SBP)",
        "keywords_must": [],
        "keywords_any": [
            "mpd", "managed pressure", "pressão gerenciada", "sbp",
            "back-pressure", "backpressure", "contrapressão",
            "choke mpd", "envelope operacional", "modelo hidráulico",
        ],
    },
]

# Campos do CSV com conteúdo textual relevante (para busca de keywords)
CAMPOS_TEXTO = [
    "tx_titulo", "tx_descricao", "tx_podemos_aprender",
    "tx_esperado_acontecer", "tx_realmente_aconteceu",
    "tx_por_que_diferencas", "tx_razao_pratica", "tx_detalhes_pratica",
    "tx_razoes_alerta", "tx_por_que_fazer",
    "tx_palavras_chave", "tx_atividade", "tx_operacao",
]

# Campos com conteúdo "aprendizado" (para extração de recomendação)
CAMPOS_APRENDIZADO = [
    "tx_podemos_aprender",
    "tx_detalhes_pratica",
    "tx_razoes_alerta",
    "tx_por_que_fazer",
]

# Keywords gerais que indicam relevância a MPD
KW_RELEVANCIA = [
    "mpd", "fmcd", "pmcd", "mud cap", "managed pressure",
    "pressão gerenciada", "pressao gerenciada",
]


# ==========================================================================
#  FUNÇÕES AUXILIARES
# ==========================================================================

def _normalizar(texto: str) -> str:
    """Remove acentos, HTML tags, lower-case."""
    if not texto:
        return ""
    # Remove HTML tags
    texto = re.sub(r"<[^>]+>", " ", texto)
    # Remove entidades HTML
    texto = re.sub(r"&\w+;", " ", texto)
    # Normaliza unicode
    texto = unicodedata.normalize("NFKD", texto)
    texto = texto.encode("ascii", "ignore").decode("ascii")
    return texto.lower().strip()


def _limpar_texto(texto: str) -> str:
    """Limpa HTML mas mantém acentos."""
    if not texto:
        return ""
    texto = re.sub(r"<[^>]+>", " ", texto)
    texto = re.sub(r"&nbsp;", " ", texto)
    texto = re.sub(r"&\w+;", " ", texto)
    texto = re.sub(r"\s+", " ", texto).strip()
    return texto


def _extrair_texto_completo(row: dict) -> str:
    """Concatena todos os campos de texto para busca."""
    partes = [row.get(c, "") or "" for c in CAMPOS_TEXTO]
    return _normalizar(" ".join(partes))


def _eh_relevante_mpd(texto_normalizado: str) -> bool:
    """Verifica se um registro é relevante a MPD."""
    return any(kw in texto_normalizado for kw in KW_RELEVANCIA)


def _classificar_categoria(texto_norm: str) -> list[str]:
    """Classifica um registro em uma ou mais categorias.
    
    Retorna lista de IDs de categoria (pode ser múltipla).
    """
    categorias_match = []

    for cat in CATEGORIAS:
        cat_id = cat["id"]
        must = cat.get("keywords_must", [])
        any_kw = cat.get("keywords_any", [])
        not_kw = cat.get("keywords_not", [])
        ctx = cat.get("keywords_context", [])

        # Se tem keywords obrigatórias, todas devem estar presentes
        if must and not all(kw in texto_norm for kw in must):
            continue

        # Se tem keywords "any", pelo menos uma deve estar presente
        if any_kw and not any(kw in texto_norm for kw in any_kw):
            continue

        # Se tem keywords negativas, nenhuma pode estar presente
        if not_kw and any(kw in texto_norm for kw in not_kw):
            continue

        # Se tem contexto, pelo menos um deve estar presente
        if ctx and not any(kw in texto_norm for kw in ctx):
            continue

        categorias_match.append(cat_id)

    # Se nenhuma categoria específica, mas é relevante a MPD → CAT-01
    if not categorias_match:
        categorias_match.append("CAT-01")

    return categorias_match


def _extrair_recomendacao(row: dict) -> str:
    """Extrai a recomendação principal de um registro."""
    for campo in CAMPOS_APRENDIZADO:
        texto = _limpar_texto(row.get(campo, ""))
        if texto and len(texto) > 30:
            return texto[:2000]
    # Fallback: usa a descrição
    desc = _limpar_texto(row.get("tx_descricao", ""))
    if desc and len(desc) > 30:
        return desc[:2000]
    return _limpar_texto(row.get("tx_titulo", ""))


def _extrair_evidencia(row: dict) -> str:
    """Extrai o que realmente aconteceu (evidência operacional)."""
    campos_evidencia = [
        "tx_realmente_aconteceu",
        "tx_por_que_diferencas",
        "tx_descricao",
    ]
    for campo in campos_evidencia:
        texto = _limpar_texto(row.get(campo, ""))
        if texto and len(texto) > 30:
            return texto[:2000]
    return ""


def _extrair_pontos_chave(texto: str) -> list[str]:
    """Extrai pontos numerados ou com bullet de um texto."""
    if not texto:
        return []
    
    pontos = []
    # Padrão: 1) ..., 2) ..., 1. ..., etc.
    matches = re.findall(r'(?:^|\n)\s*(?:\d+[\.\)\-]|[-•¿])\s*(.+?)(?=\n\s*(?:\d+[\.\)\-]|[-•¿])|\Z)', texto, re.DOTALL)
    if matches and len(matches) >= 2:
        for m in matches:
            ponto = _limpar_texto(m).strip()
            if len(ponto) > 15:
                pontos.append(ponto[:500])
    
    return pontos[:10]


# ==========================================================================
#  PIPELINE PRINCIPAL
# ==========================================================================

def processar_csv(csv_path: Path) -> dict:
    """Processa o CSV de lições aprendidas e retorna estrutura agregada."""
    
    print(f"{'='*70}")
    print(f"PRÉ-PROCESSAMENTO DE LIÇÕES APRENDIDAS DE MPD")
    print(f"{'='*70}")
    print(f"Arquivo: {csv_path}")
    
    # ── Ler CSV ──────────────────────────────────────────────────────
    with open(csv_path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        todas_linhas = list(reader)
    
    print(f"Total de registros no CSV: {len(todas_linhas)}")
    
    # ── Filtrar relevantes a MPD ─────────────────────────────────────
    relevantes = []
    for row in todas_linhas:
        texto_norm = _extrair_texto_completo(row)
        if _eh_relevante_mpd(texto_norm):
            row["_texto_norm"] = texto_norm
            relevantes.append(row)
    
    print(f"Registros relevantes a MPD: {len(relevantes)}")
    
    # ── Estatísticas ─────────────────────────────────────────────────
    tipos = Counter(r.get("tx_tipo_lesson", "") for r in relevantes)
    print(f"\nPor tipo de lição:")
    for t, c in tipos.most_common():
        print(f"  {t}: {c}")
    
    status = Counter(r.get("tx_status", "") for r in relevantes)
    print(f"\nPor status:")
    for s, c in status.most_common():
        if s in ("APR", "AGR", "AGL", "AGC"):
            label = {"APR": "Aprovado", "AGR": "Aguardando", "AGL": "Ag. Local", "AGC": "Ag. Corp."}.get(s, s)
            print(f"  {s} ({label}): {c}")
    
    # ── Classificar por categoria ────────────────────────────────────
    por_categoria = defaultdict(list)
    multi_cat = 0
    
    for row in relevantes:
        cats = _classificar_categoria(row["_texto_norm"])
        if len(cats) > 1:
            multi_cat += 1
        for cat_id in cats:
            por_categoria[cat_id].append(row)
    
    print(f"\nClassificação por categoria:")
    total_classificados = 0
    for cat in CATEGORIAS:
        cat_id = cat["id"]
        qtd = len(por_categoria.get(cat_id, []))
        total_classificados += qtd
        if qtd > 0:
            print(f"  {cat_id} – {cat['nome']}: {qtd} lições")
    print(f"  (registros multi-categoria: {multi_cat})")
    
    # ── Agregar por categoria ────────────────────────────────────────
    print(f"\n{'='*70}")
    print(f"AGREGANDO LIÇÕES POR CATEGORIA")
    print(f"{'='*70}")
    
    resultado = {
        "titulo": "Lições Aprendidas MPD – Pré-processado",
        "data_geracao": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "fonte": str(csv_path.name),
        "total_registros_csv": len(todas_linhas),
        "total_relevantes_mpd": len(relevantes),
        "categorias": [],
        "estatisticas": {
            "por_tipo_lesson": dict(tipos),
            "por_status": dict(status),
            "por_categoria": {},
        },
    }
    
    for cat_def in CATEGORIAS:
        cat_id = cat_def["id"]
        cat_nome = cat_def["nome"]
        licoes_cat = por_categoria.get(cat_id, [])
        
        if not licoes_cat:
            continue
        
        # Ordenar por relevância: Aprovados primeiro, depois por tipo (LA, AT, BP, OP)
        tipo_prioridade = {"Alerta Técnico": 0, "Lição Aprendida": 1, "Boas Práticas": 2, "Observação Poço": 3}
        status_prioridade = {"APR": 0, "AGR": 1, "AGL": 2, "AGC": 3, "REV": 4, "RAS": 5, "REP": 6}
        
        licoes_cat.sort(key=lambda r: (
            status_prioridade.get(r.get("tx_status", ""), 9),
            tipo_prioridade.get(r.get("tx_tipo_lesson", ""), 9),
        ))
        
        # Extrair lições únicas (deduplicar por título similar)
        licoes_processadas = []
        titulos_vistos = set()
        
        for row in licoes_cat:
            titulo = _limpar_texto(row.get("tx_titulo", ""))
            titulo_norm = _normalizar(titulo)[:80]
            
            # Deduplicar por título similar
            if titulo_norm in titulos_vistos:
                continue
            titulos_vistos.add(titulo_norm)
            
            recomendacao = _extrair_recomendacao(row)
            evidencia = _extrair_evidencia(row)
            pontos = _extrair_pontos_chave(recomendacao)
            
            licao = {
                "id": row.get("ico_id", ""),
                "tipo": row.get("tx_tipo_lesson", ""),
                "status": row.get("tx_status", ""),
                "titulo": titulo,
                "recomendacao": recomendacao,
                "evidencia": evidencia[:1000],
                "pontos_chave": pontos,
                "poco": _limpar_texto(row.get("nm_poco", "")),
                "sonda": _limpar_texto(row.get("nm_sonda", "")),
                "autor": _limpar_texto(row.get("nm_autor", "")),
                "area": row.get("tx_tipo_item", ""),
                "subarea": row.get("tx_subtipo", ""),
                "atividade": row.get("tx_atividade", ""),
                "operacao": row.get("tx_operacao", ""),
                "ganho_valor_usd": row.get("vl_ganho_valor", ""),
                "ganho_descricao": _limpar_texto(row.get("ds_ganho_descricao", ""))[:300],
            }
            
            licoes_processadas.append(licao)
        
        # Contar tipos nesta categoria
        tipos_cat = Counter(l["tipo"] for l in licoes_processadas)
        
        # Extrair os temas/tópicos mais frequentes
        # (análise simples de keywords nos títulos e recomendações)
        temas = _extrair_temas(licoes_processadas)
        
        cat_resultado = {
            "cat_id": cat_id,
            "cat_nome": cat_nome,
            "total_licoes": len(licoes_processadas),
            "por_tipo": dict(tipos_cat),
            "temas_frequentes": temas,
            "licoes": licoes_processadas,
        }
        
        resultado["categorias"].append(cat_resultado)
        resultado["estatisticas"]["por_categoria"][cat_id] = len(licoes_processadas)
        
        print(f"\n  {cat_id} – {cat_nome}: {len(licoes_processadas)} lições únicas")
        print(f"    Tipos: {dict(tipos_cat)}")
        if temas:
            print(f"    Temas: {', '.join(t['tema'] for t in temas[:5])}")
    
    return resultado


def _extrair_temas(licoes: list[dict]) -> list[dict]:
    """Extrai temas frequentes das lições via análise de keywords."""
    
    # Keywords temáticas relevantes para MPD
    temas_keywords = {
        "Teste de BOP/MPD": ["teste de bop", "teste bop", "teste simplificado", "teste periodico"],
        "Contrapressão/SBP": ["contrapressão", "contrapressao", "back-pressure", "backpressure", "sbp"],
        "Choke/Válvulas MPD": ["choke", "valvula mpd", "válvula mpd", "bfm", "choke manifold"],
        "Modelo hidráulico": ["modelo hidraulico", "modelo hidráulico", "geobalance", "pressview", "simulação", "simulacao"],
        "Influxo/Kick": ["influxo", "kick", "ganho de volume", "gas", "gás", "fechamento de poço"],
        "Perda de circulação": ["perda de circulação", "perda de circulacao", "perda severa", "perda total", "zona de perda"],
        "Fluido/Lama": ["fluido", "lama", "mud", "peso do fluido", "ppg", "reologia"],
        "Riser/Junta": ["riser", "junta integrada", "bearing assembly", "rcd", "flow spool"],
        "Cimentação": ["cimentação", "cimentacao", "cimento", "pasta", "cement"],
        "Completação inferior": ["completação inferior", "completacao inferior", "cauda", "paci", "packer"],
        "Revestimento": ["revestimento", "casing", "liner", "sapata"],
        "Equipamento MPD": ["coriolis", "flowmeter", "medidor de vazão", "sensor", "alarme"],
        "Conversão MPD/MCD": ["conversão", "conversao", "transição", "transicao", "converter"],
        "Teste de influxo/DFIT": ["teste de influxo", "teste negativo", "dfit", "mini-frac", "mini frac", "leak-off"],
        "Pressão de poros": ["pressão de poros", "pressao de poros", "pore pressure", "pp ", "gradiente de poros"],
        "Manobra/Trip": ["manobra", "trip", "retirada de coluna", "descida de coluna", "swab", "surge"],
        "Segurança/BOP": ["segurança", "seguranca", "bop", "barreira", "preventor"],
        "Sonda/Equipamentos": ["sonda", "rig", "bomba", "guincho", "compensador"],
        "Treinamento/Procedimento": ["treinamento", "procedimento", "simulado", "protocolo", "padrao", "padrão"],
        "DPPT": ["dppt", "drill pipe pressure test", "teste de pressão na coluna"],
    }
    
    contagem_temas = Counter()
    
    for licao in licoes:
        texto = _normalizar(licao.get("titulo", "") + " " + licao.get("recomendacao", ""))
        for tema, keywords in temas_keywords.items():
            if any(kw in texto for kw in keywords):
                contagem_temas[tema] += 1
    
    resultado = []
    for tema, count in contagem_temas.most_common(10):
        if count >= 2:  # Pelo menos 2 lições sobre o tema
            resultado.append({"tema": tema, "frequencia": count})
    
    return resultado


def _gerar_resumo_por_categoria(resultado: dict) -> str:
    """Gera resumo textual das lições por categoria (para debug/inspeção)."""
    linhas = []
    linhas.append("=" * 70)
    linhas.append("RESUMO DAS LIÇÕES APRENDIDAS MPD POR CATEGORIA")
    linhas.append("=" * 70)
    
    for cat in resultado["categorias"]:
        linhas.append(f"\n{'─'*60}")
        linhas.append(f"  {cat['cat_id']} – {cat['cat_nome']} ({cat['total_licoes']} lições)")
        linhas.append(f"{'─'*60}")
        
        if cat["temas_frequentes"]:
            temas_str = ", ".join(f"{t['tema']}({t['frequencia']})" for t in cat["temas_frequentes"][:5])
            linhas.append(f"  Temas: {temas_str}")
        
        # Top 10 lições (por prioridade)
        for i, licao in enumerate(cat["licoes"][:10], 1):
            tipo_sigla = {"Lição Aprendida": "LA", "Alerta Técnico": "AT",
                         "Boas Práticas": "BP", "Observação Poço": "OP"}.get(licao["tipo"], "??")
            linhas.append(f"\n  {i}. [{licao['id']}/{tipo_sigla}] {licao['titulo'][:90]}")
            if licao["pontos_chave"]:
                for p in licao["pontos_chave"][:3]:
                    linhas.append(f"     → {p[:120]}")
            elif licao["recomendacao"]:
                linhas.append(f"     → {licao['recomendacao'][:150]}")
    
    return "\n".join(linhas)


# ==========================================================================
#  MAIN
# ==========================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Pré-processador de Lições Aprendidas de MPD"
    )
    parser.add_argument("--csv", type=str, default=None,
                        help="Caminho do CSV de lições aprendidas")
    args = parser.parse_args()
    
    # Encontrar o CSV
    if args.csv:
        csv_path = Path(args.csv)
    else:
        # Auto-detect no corpus/
        import glob
        candidates = glob.glob(str(SCRIPT_DIR / "corpus" / "*aprendidas*"))
        if not candidates:
            print("ERRO: Nenhum CSV de lições aprendidas encontrado em corpus/")
            print("  Use --csv CAMINHO para especificar o arquivo")
            sys.exit(1)
        csv_path = Path(candidates[0])
    
    if not csv_path.exists():
        print(f"ERRO: Arquivo não encontrado: {csv_path}")
        sys.exit(1)
    
    # Processar
    resultado = processar_csv(csv_path)
    
    # Salvar JSON
    saida_json = SCRIPT_DIR / "licoes_aprendidas_mpd.json"
    with open(saida_json, "w", encoding="utf-8") as f:
        json.dump(resultado, f, ensure_ascii=False, indent=2)
    
    print(f"\n{'='*70}")
    print(f"JSON salvo: {saida_json}")
    print(f"  Categorias: {len(resultado['categorias'])}")
    total_licoes = sum(c["total_licoes"] for c in resultado["categorias"])
    print(f"  Total lições únicas: {total_licoes}")
    
    # Salvar resumo textual
    resumo = _gerar_resumo_por_categoria(resultado)
    saida_resumo = SCRIPT_DIR / "licoes_aprendidas_mpd_resumo.txt"
    with open(saida_resumo, "w", encoding="utf-8") as f:
        f.write(resumo)
    print(f"  Resumo: {saida_resumo}")
    print(f"{'='*70}")
    
    # Mostrar resumo no console
    print(resumo)


if __name__ == "__main__":
    main()
