import os
import re
import argparse
import pandas as pd
from datetime import timedelta
from databricks_loader import DatabricksWellLoader
from openai import OpenAI

# Configuracoes
POCO = "8-MRO-35DA-RJS"  # Poco padrao
HOST = "adb-671799829240675.15.azuredatabricks.net"
PATH = "/sql/1.0/warehouses/1fd972f888afd086"
TOKEN = os.environ.get("DATABRICKS_TOKEN")
DIAS = 7
MAX_REGISTROS_PROMPT = 220
MAX_CHARS_CAMPO = 200
MAX_TOKENS_RESPOSTA = 2200


def _parse_args():
    parser = argparse.ArgumentParser(description="Resume operacoes de um poco por dia.")
    parser.add_argument("--poco", default=POCO, help="Nome do poco para consultar.")
    return parser.parse_args()


def _resolver_coluna(df, aliases):
    cols_upper = {c.upper(): c for c in df.columns}
    for alias in aliases:
        if alias in df.columns:
            return alias
        real = cols_upper.get(alias.upper())
        if real:
            return real
    return None


def _clean(v, max_chars=200):
    if pd.isna(v):
        return ""
    t = str(v).replace("\n", " ").replace("\r", " ").strip()
    if len(t) > max_chars:
        return t[: max_chars - 3] + "..."
    return t


def _kw_match(texto_upper, kw):
    """Casa keyword inteira (sigla/palavra/frase), nunca como parte de outra palavra."""
    kw_upper = kw.upper().strip()
    if not kw_upper:
        return False
    # Espaços flexíveis para frases; match protegido por bordas alfanuméricas.
    kw_pattern = re.escape(kw_upper).replace(r"\ ", r"\s+")
    pattern = rf"(?<![A-Z0-9]){kw_pattern}(?![A-Z0-9])"
    return re.search(pattern, texto_upper) is not None


def _is_ma_parallel(texto_upper):
    """MA (Mesa Auxiliar) deve ser tratada como operacao paralela."""
    return (" MESA AUXILIAR" in texto_upper) or (" MA " in f" {texto_upper} ")


def _build_search_text_all_cols_except_desc(row, colunas_busca):
    """Concatena todas as colunas de busca (exceto descricao) para matching de keywords."""
    partes = []
    for c in colunas_busca:
        v = row.get(c, None)
        if pd.isna(v):
            continue
        partes.append(str(v))
    return " | ".join(partes).upper()


def _build_search_text_all_cols(row):
    partes = []
    for c in row.index:
        v = row.get(c, None)
        if pd.isna(v):
            continue
        partes.append(str(v))
    return " | ".join(partes)


def _to_float_ptbr(valor):
    """Converte numero em formato PT-BR/EN para float (suporta milhar com ponto)."""
    s = str(valor).strip()
    if not s:
        raise ValueError("valor numerico vazio")

    if "," in s and "." in s:
        # Ex.: 15.427,5 -> 15427.5
        if s.rfind(",") > s.rfind("."):
            s = s.replace(".", "").replace(",", ".")
        else:
            s = s.replace(",", "")
    elif "," in s:
        s = s.replace(",", ".")
    elif re.fullmatch(r"\d{1,3}(?:\.\d{3})+", s):
        # Ex.: 15.427 -> 15427
        s = s.replace(".", "")

    return float(s)


def _extrair_perdas_bblh(texto):
    """Extrai taxas de perda do texto e converte tudo para bbl/h."""
    if not texto:
        return []

    base = str(texto)
    perdas = []
    spans_faixa = []

    # Ex.: 0,5-1,0 bbl/min | 0.5 a 1.0 bbl/h
    padrao_faixa = re.compile(
        r"(?P<v1>\d+(?:[\.,]\d+)?)\s*(?:-|–|—|a|ate|até)\s*"
        r"(?P<v2>\d+(?:[\.,]\d+)?)\s*(?:bbl|bl|barris?)\s*/\s*"
        r"(?P<unit>h|hr|hora|min)\b",
        flags=re.IGNORECASE,
    )
    for m in padrao_faixa.finditer(base):
        v1 = _to_float_ptbr(m.group("v1"))
        v2 = _to_float_ptbr(m.group("v2"))
        unit = m.group("unit").lower()
        media = (v1 + v2) / 2.0
        if unit == "min":
            media *= 60.0
        perdas.append(media)
        spans_faixa.append(m.span())

    # Ex.: 1,5 bbl/h | 0.8 bbl/min
    padrao_unico = re.compile(
        r"(?P<v>\d+(?:[\.,]\d+)?)\s*(?:bbl|bl|barris?)\s*/\s*(?P<unit>h|hr|hora|min)\b",
        flags=re.IGNORECASE,
    )
    for m in padrao_unico.finditer(base):
        s, e = m.span()
        if any(s >= a and e <= b for a, b in spans_faixa):
            continue
        v = _to_float_ptbr(m.group("v"))
        unit = m.group("unit").lower()
        if unit == "min":
            v *= 60.0
        perdas.append(v)

    return perdas


def _extrair_volumes_perda_bbl(texto):
    """Extrai volume perdido no dia e acumulado na fase a partir de texto livre."""
    if not texto:
        return [], []

    base = str(texto)
    vols_dia = []
    vols_fase = []

    padrao_dia = re.compile(
        r"(?:volume\s+de\s+fluido\s+perdido\s+no\s+dia|perdido\s+no\s+dia|perda\s+no\s+dia)\s*[:=]?\s*"
        r"(?P<v>\d+(?:[\.,]\d+)*)\s*(?:bbl|bl|barris?)",
        flags=re.IGNORECASE,
    )
    for m in padrao_dia.finditer(base):
        try:
            vols_dia.append(_to_float_ptbr(m.group("v")))
        except ValueError:
            continue

    padrao_fase = re.compile(
        r"(?:total\s+de\s+fluido\s+perdido\s+na\s+fase|perda\s+acumulada\s+na\s+fase|acumulado\s+na\s+fase)\s*[:=]?\s*"
        r"(?P<v>\d+(?:[\.,]\d+)*)\s*(?:bbl|bl|barris?)",
        flags=re.IGNORECASE,
    )
    for m in padrao_fase.finditer(base):
        try:
            vols_fase.append(_to_float_ptbr(m.group("v")))
        except ValueError:
            continue

    return vols_dia, vols_fase


def _is_combate_perda(texto_upper):
    """Sinaliza registros de combate a perda para analise antes/depois."""
    padroes = [
        r"COMBATE\s+A\s+PERDA",
        r"COMBATE\s+PERDA",
        r"PERDA\s+DE\s+CIRCUL",
        r"LOSS\s+CIRC",
        r"WELL\s*DEFEND",
        r"LCM",
        r"FMCD",
        r"PMCD",
    ]
    return any(re.search(p, texto_upper) for p in padroes)


if not TOKEN:
    raise RuntimeError("Defina a variavel de ambiente DATABRICKS_TOKEN com seu token Databricks.")

args = _parse_args()
poco = args.poco

loader = DatabricksWellLoader(
    server_hostname=HOST,
    http_path=PATH,
    access_token=TOKEN,
)

df_ops = loader.get_tempos_operacoes(poco)
if df_ops.empty:
    raise RuntimeError(f"Nenhum registro de operacoes encontrado para o poco {poco}.")

agora_utc = pd.Timestamp.now(tz="UTC")
data_limite = agora_utc - timedelta(days=DIAS)

df_ops["DT_INICIO_ATIVIDADE"] = pd.to_datetime(df_ops["DT_INICIO_ATIVIDADE"], errors="coerce", utc=True)
df_ops = df_ops[df_ops["DT_INICIO_ATIVIDADE"] >= data_limite].copy()
if df_ops.empty:
    raise RuntimeError(f"Nenhuma operacao nos ultimos {DIAS} dias para o poco {poco}.")

df_ops = df_ops.sort_values("DT_INICIO_ATIVIDADE", ascending=False).head(MAX_REGISTROS_PROMPT)
df_ops = df_ops.sort_values("DT_INICIO_ATIVIDADE", ascending=True)

col_operacao = _resolver_coluna(df_ops, ["TX_OPERACAO", "OPERACAO", "OPERATION"])
col_estagio = _resolver_coluna(df_ops, ["TX_ETAPA", "ETAPA", "STAGE"])
col_atividade = _resolver_coluna(df_ops, ["TX_ATIVIDADE", "ATIVIDADE", "ACTIVITY"])
col_descricao = _resolver_coluna(df_ops, [
    "DS_DESCRICAO_ATIVIDADE", "TX_DESCRICAO_ATIVIDADE", "DESCRIPTION", "DESCRICAO",
    "TX_DESCRICAO", "TX_OBJETIVO_EVENTO", "OBSERVACAO", "OBS"
])
col_duracao = _resolver_coluna(df_ops, ["MD_DURACAO_TOTAL", "DURACAO", "DURATION_HOURS"])

if col_descricao is None:
    col_descricao = col_atividade or col_operacao
if col_descricao is None:
    raise KeyError(f"Sem coluna de descricao/atividade/operacao. Colunas: {list(df_ops.columns)}")

if col_duracao:
    df_ops[col_duracao] = pd.to_numeric(df_ops[col_duracao], errors="coerce").fillna(0.0)
else:
    df_ops["_dur_h"] = 0.0
    col_duracao = "_dur_h"

# Colunas usadas para procurar keywords: todas, exceto a coluna de descricao.
colunas_busca_keywords = [c for c in df_ops.columns if c != col_descricao]

palavras_chave = [
    "MPD", "NRV", "NRVs", "BA", "BART", "MBART", "M-BART", "RCD", "SSA", "ACD", "DSIT", "SBP", "AP", "PMCD", "FMCD", "FCMD", "TTV", "DPPT", "DLOT", "DFIT", "PS",
    "Bearing Assembly", "junta integrada", "junta MPD", "FlowSpool", "Flow Spool", "buffer", "buffer manifold", "packer assy", "Seal Sleeve Assembly", "Seal Sleeve", "Cabeca Rotativa MPD",
    "Choke MPD", "PMCD dinamico", "FMCD simplificado", "FCMD simplificado", "Trip Tank Virtual", "Non ported", "No ported", "Holdpoint MPD", "Hold point MPD", "HP MPD", "CSD MPD", "CSD-MPD",
    "Junk Catcher", "Junk-Catcher", "Mangueira de 6\"", "Mangueiras de 6\"", "fingerprint", "MPD Drill", "MPD-Drill", "Protect Sleeve"
]

# Monta linhas de eventos por dia + totalizacao de horas por keyword em cada dia.
blocos_dia = []
for dia, g in df_ops.groupby(df_ops["DT_INICIO_ATIVIDADE"].dt.strftime("%d/%m/%Y")):
    g = g.sort_values("DT_INICIO_ATIVIDADE")
    linhas_eventos = []
    totais_dia = {kw: 0.0 for kw in palavras_chave}
    perdas_dia_bblh = []
    perdas_amostras = []
    volumes_perdidos_dia_bbl = []
    volumes_perdidos_fase_bbl = []
    ts_primeiro_combate = None

    for _, r in g.iterrows():
        desc = _clean(r.get(col_descricao, ""), MAX_CHARS_CAMPO)
        ativ = _clean(r.get(col_atividade, ""), 110)
        oper = _clean(r.get(col_operacao, ""), 90)
        estg = _clean(r.get(col_estagio, ""), 90)
        dur_h = float(r.get(col_duracao, 0.0))

        texto_busca = _build_search_text_all_cols_except_desc(r, colunas_busca_keywords)
        texto_perdas = _build_search_text_all_cols(r)
        perdas_extraidas = _extrair_perdas_bblh(texto_perdas)
        perdas_dia_bblh.extend(perdas_extraidas)

        texto_upper = texto_perdas.upper()
        is_combate = _is_combate_perda(texto_upper)
        if is_combate and ts_primeiro_combate is None:
            ts_primeiro_combate = r["DT_INICIO_ATIVIDADE"]

        for p in perdas_extraidas:
            perdas_amostras.append(
                {
                    "ts": r["DT_INICIO_ATIVIDADE"],
                    "valor": float(p),
                    "combate": is_combate,
                }
            )

        vol_dia, vol_fase = _extrair_volumes_perda_bbl(texto_perdas)
        volumes_perdidos_dia_bbl.extend(vol_dia)
        volumes_perdidos_fase_bbl.extend(vol_fase)
        kws_encontradas = [kw for kw in palavras_chave if _kw_match(texto_busca, kw)]
        par_ma = _is_ma_parallel(texto_busca)
        for kw in kws_encontradas:
            totais_dia[kw] += dur_h

        linhas_eventos.append(
            f"- {r['DT_INICIO_ATIVIDADE'].strftime('%H:%M')} | OPERACAO={oper} | ESTAGIO={estg} | "
            f"ATIVIDADE={ativ} | DESCRIPTION={desc} | DUR={dur_h:.2f} h | "
            f"PAR_MA={'SIM' if par_ma else 'NAO'} | KWS={', '.join(kws_encontradas) if kws_encontradas else '-'}"
        )

    totais_filtrados = [f"{k}={v:.2f}h" for k, v in totais_dia.items() if v > 0]
    txt_totais = ", ".join(totais_filtrados) if totais_filtrados else "sem palavras-chave com horas no dia"
    if volumes_perdidos_dia_bbl:
        # Regra principal solicitada: media do dia vem do volume perdido no dia / 24h.
        vol_dia_ref = volumes_perdidos_dia_bbl[-1]
        perda_media = vol_dia_ref / 24.0
        origem_perda_media = "VOLUME_DIA_DIV24H"
    elif perdas_dia_bblh:
        perda_media = sum(perdas_dia_bblh) / len(perdas_dia_bblh)
        origem_perda_media = "TAXA_EXTRAIDA_DO_TEXTO"
    else:
        perda_media = None
        origem_perda_media = "SEM_DADOS"

    # Faixa do dia prioriza taxas extraidas ao longo do dia (antes/depois).
    if perdas_dia_bblh:
        perda_min = min(perdas_dia_bblh)
        perda_max = max(perdas_dia_bblh)
        origem_faixa = "TAXA_EXTRAIDA_DO_TEXTO"
    elif volumes_perdidos_dia_bbl:
        perda_min = volumes_perdidos_dia_bbl[-1] / 24.0
        perda_max = volumes_perdidos_dia_bbl[-1] / 24.0
        origem_faixa = "DERIVADA_DE_VOLUME_DIA"
    else:
        perda_min = None
        perda_max = None
        origem_faixa = "SEM_DADOS"

    perda_antes_min = None
    perda_antes_max = None
    perda_depois_min = None
    perda_depois_max = None
    if ts_primeiro_combate is not None and perdas_amostras:
        antes = [x["valor"] for x in perdas_amostras if x["ts"] < ts_primeiro_combate]
        depois = [x["valor"] for x in perdas_amostras if x["ts"] >= ts_primeiro_combate]
        if antes:
            perda_antes_min = min(antes)
            perda_antes_max = max(antes)
        if depois:
            perda_depois_min = min(depois)
            perda_depois_max = max(depois)

    if perda_media is not None:
        txt_perda = (
            f"PERDA_BBLH_FAIXA_DIA_EXTRAIDA_TEXTO={perda_min:.2f}-{perda_max:.2f}\n"
            f"PERDA_BBLH_MEDIA_DIA_EXTRAIDA_TEXTO={perda_media:.2f}\n"
            f"PERDA_BBLH_AMOSTRAS_DIA={len(perdas_dia_bblh) if perdas_dia_bblh else len(volumes_perdidos_dia_bbl)}\n"
            f"PERDA_BBLH_ORIGEM_MEDIA={origem_perda_media}\n"
            f"PERDA_BBLH_ORIGEM_FAIXA={origem_faixa}"
        )
    else:
        txt_perda = (
            "PERDA_BBLH_FAIXA_DIA_EXTRAIDA_TEXTO=SEM_DADOS\n"
            "PERDA_BBLH_MEDIA_DIA_EXTRAIDA_TEXTO=SEM_DADOS\n"
            "PERDA_BBLH_AMOSTRAS_DIA=0\n"
            "PERDA_BBLH_ORIGEM_MEDIA=SEM_DADOS\n"
            "PERDA_BBLH_ORIGEM_FAIXA=SEM_DADOS"
        )

    if perda_antes_min is not None and perda_antes_max is not None:
        txt_perda_antes = f"PERDA_BBLH_FAIXA_ANTES_COMBATE={perda_antes_min:.2f}-{perda_antes_max:.2f}"
    else:
        txt_perda_antes = "PERDA_BBLH_FAIXA_ANTES_COMBATE=SEM_DADOS"

    if perda_depois_min is not None and perda_depois_max is not None:
        txt_perda_depois = f"PERDA_BBLH_FAIXA_DEPOIS_COMBATE={perda_depois_min:.2f}-{perda_depois_max:.2f}"
    else:
        txt_perda_depois = "PERDA_BBLH_FAIXA_DEPOIS_COMBATE=SEM_DADOS"

    if volumes_perdidos_dia_bbl:
        txt_vol_dia = (
            f"VOLUME_PERDIDO_DIA_BBL_EXTRAIDO={min(volumes_perdidos_dia_bbl):.2f}-{max(volumes_perdidos_dia_bbl):.2f}"
        )
    else:
        txt_vol_dia = "VOLUME_PERDIDO_DIA_BBL_EXTRAIDO=SEM_DADOS"

    if volumes_perdidos_fase_bbl:
        txt_vol_fase = (
            f"VOLUME_PERDIDO_ACUM_FASE_BBL_EXTRAIDO={min(volumes_perdidos_fase_bbl):.2f}-{max(volumes_perdidos_fase_bbl):.2f}"
        )
    else:
        txt_vol_fase = "VOLUME_PERDIDO_ACUM_FASE_BBL_EXTRAIDO=SEM_DADOS"

    blocos_dia.append(
        f"DIA {dia}\nTotais keywords: {txt_totais}\n{txt_perda}\n{txt_perda_antes}\n{txt_perda_depois}\n{txt_vol_dia}\n{txt_vol_fase}\n" + "\n".join(linhas_eventos)
    )

dados_por_dia = "\n\n".join(blocos_dia)

prompt = (
    f"Voce eh especialista em MPD no contexto Petrobras/CSD-MPD. Este texto eh para passagem de servico entre turnos.\n\n"
    f"Gere um resumo por dia, em portugues do Brasil, usando somente os dados abaixo e consolidando o dia inteiro em FAIXAS (min-max).\n"
    f"Regras obrigatorias:\n"
    f"1) Nao explique siglas.\n"
    f"2) Quando houver operacao com palavra-chave MPD (ou outra keyword relevante), inclua o tempo entre parenteses.\n"
    f"3) Foque em perdas, instalacao/desinstalacao de equipamentos MPD, AP, Surge/Swab, SBP, BA, BHA, fingerprint e manobras.\n"
    f"4) Escreva por dia, com frases objetivas, no estilo passagem de servico.\n"
    f"5) Traga total de tempo da manobra quando possivel.\n"
    f"6) MA significa Mesa Auxiliar: tudo que ocorrer em MA deve ser tratado como operacao paralela, fora da linha critica principal.\n"
    f"7) Nao invente dados; use somente o que esta informado.\n"
    f"8) Reporte SEMPRE em formato de faixa diaria (min-max) quando houver variacao no dia; nao reporte valor pontual se houver faixa disponivel.\n"
    f"8.1) Consolide o dia inteiro; nao descreva cronologia hora a hora e nao liste passos operacionais longos.\n"
    f"9) Formato fixo com 3 linhas por dia, exatamente nesta ordem:\n"
    f"   Dia DD/MM | MP: <resumo da operacao principal do dia, consolidado>\n"
    f"   Dia DD/MM | Notas: <eventos relevantes e operacoes paralelas MA, consolidado>\n"
    f"   Dia DD/MM | Parametros MPD do dia: <somente parametros em faixa diaria + perdas>\n"
    f"9.1) Limite de tamanho por dia: maximo 3 linhas e cada linha com no maximo 240 caracteres.\n"
    f"10) Na linha 'Parametros MPD do dia', priorize e ordene assim: AP (ppg), SBP (psi), booster (gpm/psi), stack wellbore (psi), choke A/B (%), vazao coluna (gpm/psi), velocidade (min/secao), WOB, RPM.\n"
    f"10.1) Na linha de parametros, use apenas pares parametro=faixa no formato 'nome X-Y unidade'; sem narracao.\n"
    f"10.2) Quando houver apenas um valor no dia, represente como faixa fechada (ex.: SBP 230-230 psi).\n"
    f"11) Para perdas, use os campos extraidos automaticamente do texto bruto do dia: PERDA_BBLH_FAIXA_DIA_EXTRAIDA_TEXTO, PERDA_BBLH_MEDIA_DIA_EXTRAIDA_TEXTO, PERDA_BBLH_AMOSTRAS_DIA, PERDA_BBLH_ORIGEM_MEDIA, PERDA_BBLH_ORIGEM_FAIXA.\n"
    f"12) Regra da media diaria: se VOLUME_PERDIDO_DIA_BBL_EXTRAIDO tiver dado, a media diaria obrigatoria eh volume_dia/24h (origem VOLUME_DIA_DIV24H).\n"
    f"13) Regra da faixa diaria: usar PERDA_BBLH_FAIXA_DIA_EXTRAIDA_TEXTO com base nas taxas encontradas no dia; se nao houver taxas, usar faixa fechada derivada de volume/24h.\n"
    f"14) Se PERDA_BBLH_FAIXA_DIA_EXTRAIDA_TEXTO for diferente de SEM_DADOS, incluir obrigatoriamente no fim da linha de parametros: 'perdas: X,XX-Y,YY bbl/h (media M,MM bbl/h; N amostras; media-origem ORIGEM_MEDIA; faixa-origem ORIGEM_FAIXA)'.\n"
    f"15) Se houver PERDA_BBLH_FAIXA_ANTES_COMBATE e PERDA_BBLH_FAIXA_DEPOIS_COMBATE diferentes de SEM_DADOS, incluir tambem: 'antes combate: A,AA-B,BB bbl/h; depois combate: C,CC-D,DD bbl/h'.\n"
    f"16) Se PERDA_BBLH_FAIXA_DIA_EXTRAIDA_TEXTO for SEM_DADOS, NAO escreva nada sobre perdas.\n"
    f"16.1) Texto proibido: nunca escreva literalmente 'perdas: sem dados'.\n"
    f"17) Para volumes perdidos, use VOLUME_PERDIDO_DIA_BBL_EXTRAIDO e VOLUME_PERDIDO_ACUM_FASE_BBL_EXTRAIDO. Se houver dados, incluir ao final da linha de parametros no formato: 'volume perdido dia: XXX-YYY bbl; acumulado fase: AAA-BBB bbl'. Se nao houver, omitir esse trecho.\n"
    f"18) Se algum parametro nao aparecer no dia, omita o parametro (nao invente).\n"
    f"19) Nao use markdown, bullets ou cabecalhos extras: apenas linhas no formato 'Dia DD/MM | ...'.\n\n"
    f"Exemplo de estilo desejado:\n"
    f"Dia 10/03 | MP: retirando BHA #10 em backreaming de 6.060 m ate 5.686 m para remocao de reboco, em AP 8,95 ppg na sapata 10 3/4\" (MPD 48 h).\n"
    f"Dia 10/03 | Notas: parada de rotacao/vazao em zonas de perda ja mapeadas; em MA, atividades paralelas fora da linha critica.\n"
    f"Dia 10/03 | Parametros MPD do dia: AP 8,95 ppg; SBP 56-390 psi; booster 450 gpm / 390 psi; stack wellbore 2920 psi; choke A 0%; choke B 46,2%; vazao coluna 480-550 gpm / 1.550-1.610 psi; velocidade 3 min/secao; perdas: 1,50-37,71 bbl/h (media 19,60 bbl/h; 2 amostras); volume perdido dia: 905 bbl; acumulado fase: 15427 bbl.\n\n"
    f"DADOS POR DIA:\n{dados_por_dia}"
)

client = OpenAI(
    api_key=TOKEN,
    base_url="https://adb-671799829240675.15.azuredatabricks.net/serving-endpoints"
)

response = client.chat.completions.create(
    model="databricks-claude-opus-4-6",
    messages=[{"role": "user", "content": prompt}],
    max_tokens=MAX_TOKENS_RESPOSTA,
)

print("\nResumo das operacoes por dia:")
print(response.choices[0].message.content)
