"""
Parseador de Seções de SEQOP
=============================
Divide o texto bruto do PDF em seções estruturadas.
Cada SEQOP segue um padrão previsível com seções como:
  DADOS DO POÇO, PREPARATIVOS, OBSERVAÇÕES PARA OPERAÇÃO COM MPD, etc.

O parser identifica as seções e retorna um dict com o conteúdo de cada uma.
Seções são classificadas por relevância MPD (ALTA, MEDIA, BAIXA, META).
"""
import re
from dataclasses import dataclass, field

# ── Definição das seções conhecidas ────────────────────────────────────────
# Cada tupla: (regex_padrão, nome_normalizado, relevância_mpd)
# A ordem importa: o parser testa de cima para baixo

SECOES_CONHECIDAS = [
    # ── META (dados do poço / cabeçalho) ──
    (r'SEQU[ÊE]NCIA\s+OPERACIONAL', "CABECALHO", "META"),
    (r'DADOS\s+D[OE]\s+PO[ÇC]O(?:\s+E\s+D[AE]\s+SONDA)?', "DADOS_POCO", "META"),
    (r'DADOS\s+D[OE]\s+RESERVAT[ÓO]RIO', "DADOS_RESERVATORIO", "META"),
    (r'PROFUNDIDADES\s+RELEVANTES', "PROFUNDIDADES", "META"),
    (r'PREVIS[ÕO]ES\s*/?\s*DADOS\s+D[OE]\s+RESERVAT', "DADOS_RESERVATORIO", "META"),
    (r'LIMITES\s+OPERACIONAIS', "LIMITES_OPERACIONAIS", "MEDIA"),

    # ── ALTA relevância MPD ──
    (r'OBSERVA[ÇC][ÕO]ES\s+PARA\s+OPERA[ÇC][ÃA]O\s+COM\s+MPD', "OBS_MPD", "ALTA"),
    (r'ALERTAS?\s+PARA\s+OPERA[ÇC][ÃA]O\s+COM\s+MPD', "OBS_MPD", "ALTA"),
    (r'OBSERVA[ÇC][ÕO]ES\s+(?:DE\s+)?MPD', "OBS_MPD", "ALTA"),
    (r'CIRCULA[ÇC][ÃA]O\s+DE\s+INFLUXO\s+COM\s+SISTEMA\s+MPD', "CIRCULACAO_INFLUXO_MPD", "ALTA"),
    (r'FLUXOGRAMA\s+DE\s+CONTROLE\s+DE\s+PO[ÇC]O\s+COM\s+MPD', "FLUXOGRAMA_MPD", "ALTA"),
    (r'FINGERPRINT', "FINGERPRINT", "ALTA"),
    (r'TESTE\s+DE?\s+PRESS[ÃA]O', "TESTE_PRESSAO", "ALTA"),
    (r'TESTE\s+(?:DE?\s+)?PERI[ÓO]DICO\s+BOP', "TESTE_BOP", "ALTA"),

    # ── MEDIA relevância MPD ──
    (r'PREPARATIVOS(?:\s+E\s+ATIVIDADES\s+PERI[ÓO]DICAS)?', "PREPARATIVOS", "MEDIA"),
    (r'ATIVIDADES\s+PERI[ÓO]DICAS', "ATIVIDADES_PERIODICAS", "MEDIA"),
    (r'OBSERVA[ÇC][ÕO]ES\s+DE\s+PERFURA[ÇC][ÃA]O', "OBS_PERFURACAO", "MEDIA"),
    (r'OBSERVA[ÇC][ÕO]ES\s+GERAIS', "OBS_GERAIS", "MEDIA"),
    (r'OBSERVA[ÇC][ÕO]ES\s+DE\s+SEGURAN[ÇC]A', "OBS_SEGURANCA", "MEDIA"),
    (r'OPERA[ÇC][ÕO]ES\s+EM\s+PARALELO', "OPERACOES_PARALELO", "MEDIA"),
    (r'OPERA[ÇC][ÕO]ES\s+PARALELAS', "OPERACOES_PARALELO", "MEDIA"),
    (r'MESA\s+AUXILIAR\s+\(OFFLINE\)', "OPERACOES_PARALELO", "MEDIA"),
    (r'MONTAGEM\s+(?:E\s+DESCIDA\s+)?D[OE]\s+BHA', "MONTAGEM_BHA", "MEDIA"),
    (r'DESCIDA\s+D[OE]\s+BHA', "DESCIDA_BHA", "MEDIA"),
    (r'RETIRADA\s+D[AE]\s+COLUNA', "RETIRADA_COLUNA", "MEDIA"),
    (r'CONDICIONAMENTO(?:\s+D[OE]\s+PO[ÇC]O)?', "CONDICIONAMENTO", "MEDIA"),
    (r'SUBSTITUI[ÇC][ÃA]O\s+DE?\s+FLUIDO', "TROCA_FLUIDO", "MEDIA"),
    (r'TROCA\s+DE\s+FLUIDO', "TROCA_FLUIDO", "MEDIA"),
    (r'PERFURA[ÇC][ÃA]O\s+\d', "PERFURACAO", "MEDIA"),
    (r'OPERA[ÇC][ÃA]O\s+PRINCIPAL', "OPERACAO_PRINCIPAL", "MEDIA"),
    (r'CORTE\s+DE?\s+CIMENTO', "CORTE_CIMENTO", "MEDIA"),
    (r'(?:FIT|DLOT|DFIT)\b', "FIT_DLOT", "MEDIA"),

    # ── MEDIA (segurança / APR) ──
    (r'SEGURAN[ÇC]A\s+(?:DE\s+)?PO[ÇC]O', "SEGURANCA_POCO", "MEDIA"),
    (r'SEGURAN[ÇC]A\s+OPERACIONAL', "SEGURANCA_OPERACIONAL", "MEDIA"),
    (r'APR\s*/\s*LV', "APR_LV", "MEDIA"),
    (r'ALERTAS?\s*/?\s*PGSP', "ALERTAS", "MEDIA"),
    (r'LEMBRETES\s+E\s+ALERTAS', "LEMBRETES", "MEDIA"),
    (r'INFORMA[ÇC][ÕO]ES\s+GERAIS', "INFO_GERAIS", "MEDIA"),
    (r'PONTOS\s+DE\s+ATEN[ÇC][ÃA]O', "PONTOS_ATENCAO", "MEDIA"),

    # ── MEDIA (contingência) ──
    (r'CONTING[ÊE]NCIA', "CONTINGENCIA", "MEDIA"),
    (r'\[CONTING[ÊE]NCIA\]', "CONTINGENCIA", "MEDIA"),
    (r'TESTE\s+DE\s+PLUGUEAMENTO', "PLUGUEAMENTO", "MEDIA"),
    (r'RVORE\s+DE\s+DECIS[ÃA]O\s+DE\s+COMBATE', "ARVORE_DECISAO_PERDA", "MEDIA"),

    # ── BAIXA relevância MPD ──
    (r'PR[ÓO]XIMAS?\s+OPERA[ÇC][ÕO]ES?', "PROXIMA_OPERACAO", "BAIXA"),
    (r'CONTING[ÊE]NCIAS?\s+DE\s+POSICIONAMENTO\s+DIN[ÂA]MICO', "CONTINGENCIA_DP", "BAIXA"),
    (r'MUDAN[ÇC]AS\s+DE\s+APROAMENTO', "MUDANCAS_APROAMENTO", "BAIXA"),
    (r'IMPORTANTE:\s+ALTERA[ÇC][ÕO]ES\s+DE\s+HEADING', "MUDANCAS_HEADING", "BAIXA"),
    (r'EDS\s+#\d', "EDS_PROCEDIMENTOS", "BAIXA"),
    (r'GEST[ÃA]O\s+DE\s+MUDAN', "GESTAO_MUDANCAS", "BAIXA"),
    (r'ROTINAS:', "ROTINAS", "BAIXA"),
]


# ── Palavras-chave MPD ─────────────────────────────────────────────────────
# Se uma seção contém ≥N hits dessas palavras, sua relevância é promovida.

PALAVRAS_CHAVE_MPD_SIGLAS = [
    "MPD", "NRV", "NRVs", "BA", "BART", "MBART", "M-BART",
    "RCD", "SSA", "ACD", "DSIT", "SBP", "AP", "PMCD", "FMCD", "FCMD",
    "TTV", "DPPT", "DLOT", "DFIT", "PS",
]

PALAVRAS_CHAVE_MPD_TERMOS = [
    "Bearing Assembly", "junta integrada", "junta MPD",
    "FlowSpool", "Flow Spool", "buffer", "buffer manifold",
    "packer assy", "Seal Sleeve Assembly", "Seal Sleeve",
    "Cabeça Rotativa MPD", "Choke MPD",
    "PMCD dinâmico", "FMCD simplificado", "FCMD simplificado",
    "Trip Tank Virtual", "Non ported", "No ported",
    "Holdpoint MPD", "Hold point MPD", "HP MPD",
    "CSD MPD", "CSD-MPD",
    "Junk Catcher", "Junk-Catcher",
    "Mangueira de 6\"", "Mangueiras de 6\"",
    "fingerprint", "MPD Drill", "MPD-Drill", "Protect Sleeve",
]

# Regex compilado para busca rápida
_SIGLAS_RE = re.compile(
    r'\b(' + '|'.join(re.escape(s) for s in PALAVRAS_CHAVE_MPD_SIGLAS) + r')\b'
)
_TERMOS_RE = re.compile(
    '|'.join(re.escape(t) for t in PALAVRAS_CHAVE_MPD_TERMOS),
    re.IGNORECASE,
)


def contar_hits_mpd(texto: str) -> int:
    """Conta quantas ocorrências de palavras-chave MPD existem no texto."""
    if not texto:
        return 0
    return len(_SIGLAS_RE.findall(texto)) + len(_TERMOS_RE.findall(texto))


def destacar_hits_mpd(texto: str) -> list[str]:
    """Retorna lista dos termos MPD encontrados (únicos)."""
    encontrados = set()
    encontrados.update(_SIGLAS_RE.findall(texto))
    encontrados.update(m.group() for m in _TERMOS_RE.finditer(texto))
    return sorted(encontrados)


@dataclass
class SecaoSeqop:
    """Uma seção identificada no texto da SEQOP."""
    nome: str               # Nome normalizado (ex: "OBS_MPD")
    relevancia: str          # ALTA, MEDIA, BAIXA, META
    titulo_original: str     # Título como aparece no PDF
    inicio: int              # Posição no texto
    fim: int                 # Posição final
    conteudo: str = ""       # Texto da seção
    hits_mpd: int = 0        # Qtd de palavras-chave MPD no conteúdo
    termos_mpd: list = field(default_factory=list)  # Quais termos MPD


def parsear_secoes(texto: str) -> list[SecaoSeqop]:
    """
    Divide o texto do PDF em seções estruturadas.
    Retorna lista ordenada por posição no texto.
    """
    if not texto:
        return []

    # Encontrar todas as posições de cabeçalhos de seção
    marcadores: list[tuple[int, str, str, str]] = []  # (pos, nome, relevância, titulo_original)

    linhas = texto.split("\n")
    pos_acumulada = 0

    for linha in linhas:
        l = linha.strip()
        if len(l) < 4:
            pos_acumulada += len(linha) + 1
            continue

        for regex, nome, relevancia in SECOES_CONHECIDAS:
            if re.search(regex, l, re.IGNORECASE):
                marcadores.append((pos_acumulada, nome, relevancia, l))
                break  # primeiro match ganha

        pos_acumulada += len(linha) + 1

    if not marcadores:
        # Sem seções identificadas, retornar tudo como seção única
        return [SecaoSeqop(
            nome="TEXTO_COMPLETO", relevancia="MEDIA",
            titulo_original="(texto completo)", inicio=0, fim=len(texto),
            conteudo=texto,
        )]

    # Ordenar por posição e remover duplicatas próximas (< 50 chars)
    marcadores.sort(key=lambda x: x[0])
    filtrados = [marcadores[0]]
    for m in marcadores[1:]:
        if m[0] - filtrados[-1][0] > 50:
            filtrados.append(m)

    # Construir seções com conteúdo + boost por palavras-chave
    secoes = []
    for i, (pos, nome, rel, titulo) in enumerate(filtrados):
        fim = filtrados[i + 1][0] if i + 1 < len(filtrados) else len(texto)
        conteudo = texto[pos:fim].strip()
        hits = contar_hits_mpd(conteudo)
        termos = destacar_hits_mpd(conteudo) if hits > 0 else []

        # Boost: seção BAIXA com ≥3 hits → MEDIA; MEDIA com ≥5 hits → ALTA
        rel_final = rel
        if rel == "BAIXA" and hits >= 3:
            rel_final = "MEDIA"
        elif rel == "MEDIA" and hits >= 5:
            rel_final = "ALTA"

        secoes.append(SecaoSeqop(
            nome=nome, relevancia=rel_final,
            titulo_original=titulo,
            inicio=pos, fim=fim,
            conteudo=conteudo,
            hits_mpd=hits,
            termos_mpd=termos,
        ))

    return secoes


def filtrar_secoes_mpd(secoes: list[SecaoSeqop],
                       incluir: set[str] = {"ALTA", "MEDIA", "META"}
                       ) -> list[SecaoSeqop]:
    """Filtra seções por relevância MPD."""
    return [s for s in secoes if s.relevancia in incluir]


def montar_texto_resumido(secoes: list[SecaoSeqop],
                          max_chars: int = 12000) -> str:
    """
    Monta um texto resumido com as seções mais relevantes.
    Prioriza: META (dados poço) + ALTA (obs MPD) + MEDIA (operacional).
    Dentro de cada nível, prioriza seções com mais hits de palavras-chave MPD.
    Limita ao max_chars total.
    """
    # Agrupar por prioridade; dentro do nível desempatar por hits_mpd desc
    prioridade = {"META": 0, "ALTA": 1, "MEDIA": 2, "BAIXA": 3}
    ordenadas = sorted(
        secoes,
        key=lambda s: (prioridade.get(s.relevancia, 9), -s.hits_mpd, s.inicio),
    )

    partes = []
    chars_usados = 0

    for s in ordenadas:
        if s.relevancia == "BAIXA":
            continue  # pular seções irrelevantes

        # Calcular espaço disponível
        disponivel = max_chars - chars_usados
        if disponivel < 200:
            break

        # META: incluir completo (dados do poço são curtos e essenciais)
        if s.relevancia == "META":
            trecho = s.conteudo[:min(2000, disponivel)]
        # ALTA: incluir quase completo
        elif s.relevancia == "ALTA":
            trecho = s.conteudo[:min(4000, disponivel)]
        # MEDIA: truncar se necessário
        else:
            trecho = s.conteudo[:min(2000, disponivel)]

        # Anotar termos MPD encontrados na seção
        label_hits = f" [MPD: {', '.join(s.termos_mpd[:8])}]" if s.termos_mpd else ""
        partes.append(f"══ {s.nome} ({s.relevancia}){label_hits} ══\n{trecho}")
        chars_usados += len(trecho) + len(s.nome) + 20 + len(label_hits)

    return "\n\n".join(partes)


def resumo_secoes(secoes: list[SecaoSeqop]) -> dict:
    """Retorna um resumo das seções encontradas."""
    return {
        "total": len(secoes),
        "por_relevancia": {
            rel: sum(1 for s in secoes if s.relevancia == rel)
            for rel in ["ALTA", "MEDIA", "BAIXA", "META"]
        },
        "total_hits_mpd": sum(s.hits_mpd for s in secoes),
        "secoes": [
            {
                "nome": s.nome, "relevancia": s.relevancia,
                "chars": len(s.conteudo), "hits_mpd": s.hits_mpd,
                "termos_mpd": s.termos_mpd[:10],
            }
            for s in secoes
        ],
    }


def classificar_comentario_por_keywords(texto: str) -> dict:
    """
    Pré-classifica um comentário com base nas palavras-chave MPD.
    Retorna dict com hits, termos encontrados e provável relevância.
    """
    hits = contar_hits_mpd(texto)
    termos = destacar_hits_mpd(texto)
    if hits >= 3:
        provavel = "DIRETA"
    elif hits >= 1:
        provavel = "INDIRETA"
    else:
        provavel = "NENHUMA"
    return {"hits": hits, "termos": termos, "provavel_relevancia": provavel}


# ── Teste standalone ───────────────────────────────────────────────────────
if __name__ == "__main__":
    import json
    from collections import Counter

    with open("seqops_texto_pdf.json", "r", encoding="utf-8") as f:
        pdfs = json.load(f)

    total_secoes = Counter()
    total_chars_original = 0
    total_chars_resumido = 0

    total_hits_mpd = 0
    secoes_promovidas = 0

    for item in pdfs:
        texto = item.get("texto_pdf", "")
        if not texto:
            continue

        secoes = parsear_secoes(texto)
        resumido = montar_texto_resumido(secoes)

        total_chars_original += len(texto)
        total_chars_resumido += len(resumido)
        total_hits_mpd += sum(s.hits_mpd for s in secoes)

        for s in secoes:
            total_secoes[s.nome] += 1

    # Relatório
    print(f"PDFs analisados: {len(pdfs)}")
    print(f"Chars total original: {total_chars_original:,}")
    print(f"Chars total resumido: {total_chars_resumido:,}")
    reducao = (1 - total_chars_resumido / total_chars_original) * 100 if total_chars_original else 0
    print(f"Redução: {reducao:.0f}%")
    print(f"Hits palavras-chave MPD: {total_hits_mpd:,}")
    print(f"\nSeções encontradas:")
    for nome, count in total_secoes.most_common(30):
        print(f"  {count:>4}x  {nome}")

    # Amostra de 3 SEQOPs
    print(f"\n{'='*60}")
    for idx in [0, 10, 50]:
        if idx >= len(pdfs):
            continue
        item = pdfs[idx]
        texto = item.get("texto_pdf", "")
        secoes = parsear_secoes(texto)
        resumido = montar_texto_resumido(secoes)

        print(f"\n[{idx}] {item.get('titulo','?')[:60]}")
        print(f"  Original: {len(texto):,} chars → Resumido: {len(resumido):,} chars")
        for s in secoes:
            marcador = "★" if s.relevancia == "ALTA" else "●" if s.relevancia == "MEDIA" else "○"
            kw = f"  KW: {', '.join(s.termos_mpd[:5])}" if s.termos_mpd else ""
            print(f"  {marcador} {s.nome:<30} {s.relevancia:<6} {len(s.conteudo):>5} chars  h={s.hits_mpd}{kw}")
