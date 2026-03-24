"""Analisar a estrutura de seções dos PDFs para mapear padrões."""
import json
import re
from collections import Counter

with open("seqops_texto_pdf.json", "r", encoding="utf-8") as f:
    pdfs = json.load(f)

# Padrões que parecem cabeçalhos de seção (linhas em uppercase ou padrões típicos)
secoes_todas = Counter()

# Analisar 30 PDFs variados
indices = list(range(0, min(len(pdfs), 256), 8))[:30]  # amostra distribuída

for idx in indices:
    item = pdfs[idx]
    texto = item.get("texto_pdf", "")
    if not texto:
        continue
    
    titulo = item.get("titulo", "?")[:50]
    
    # Buscar linhas que parecem cabeçalhos de seção
    linhas = texto.split("\n")
    for i, linha in enumerate(linhas):
        l = linha.strip()
        if not l or len(l) < 4:
            continue
        
        # Padrões de seção:
        # 1. TEXTO EM MAIÚSCULAS (>10 chars, sem números no início)
        if l == l.upper() and len(l) > 8 and not re.match(r'^\d', l) and not l.startswith("•"):
            # Filtrar lixo (linhas de dados, etc)
            if not any(c.isdigit() for c in l[:5]) and len(l) < 100:
                secoes_todas[l] += 1
        
        # 2. Padrões específicos
        for padrao in [
            r'DADOS\s+D[OE]\s+PO[ÇC]O',
            r'APR\s*/\s*LV',
            r'RECOMENDA[ÇC][ÕO]ES\s+GERAIS',
            r'INFORMA[ÇC][ÕO]ES\s+GERAIS',
            r'PREPARATIVOS',
            r'OBSERVA[ÇC][ÕO]ES\s+PARA\s+OPERA',
            r'OBSERVA[ÇC][ÕO]ES\s+MPD',
            r'GEST[ÃA]O\s+DE\s+MUDAN',
            r'CONTINGÊNCIA',
            r'SEGURAN[ÇC]A\s+DE\s+PO[ÇC]O',
            r'OPERA[ÇC][ÕO]ES\s+EM\s+PARALELO',
            r'SEQU[ÊE]NCIA\s+OPERACIONAL',
            r'FINGERPRINT',
            r'TESTE\s+DE\s+PRESS',
            r'MANOBRA',
            r'PERFURA[ÇC][ÃA]O',
            r'TROCA\s+DE\s+FLUIDO',
            r'CORTE\s+DE?\s+CIMENTO',
            r'DESCIDA\s+D[OE]\s+BHA',
            r'MONTAGEM\s+D[OE]\s+BHA',
            r'FIT\b|DLOT\b|DFIT\b',
        ]:
            if re.search(padrao, l, re.IGNORECASE):
                secoes_todas[l] += 1

# Top seções
print("=" * 80)
print("SEÇÕES MAIS FREQUENTES NOS PDFs (amostra de 30 SEQOPs)")
print("=" * 80)
for secao, count in secoes_todas.most_common(60):
    print(f"  {count:>3}x  {secao[:80]}")

# Agora fazer uma análise detalhada de 3 PDFs
print("\n\n" + "=" * 80)
print("ESTRUTURA DETALHADA — 3 SEQOPs")
print("=" * 80)

for idx in [0, 10, 50]:
    if idx >= len(pdfs):
        continue
    item = pdfs[idx]
    texto = item.get("texto_pdf", "")
    titulo = item.get("titulo", "?")
    
    print(f"\n{'─'*80}")
    print(f"[{idx}] {titulo}")
    print(f"    {len(texto)} chars")
    
    # Extrair linhas que são cabeçalhos (uppercase, curtas)
    linhas = texto.split("\n")
    for i, linha in enumerate(linhas):
        l = linha.strip()
        if not l:
            continue
        # Mostrar cabeçalhos e contexto
        if (l == l.upper() and len(l) > 6 and len(l) < 100 
            and not l.startswith("•") and not re.match(r'^[\d.,]+$', l)):
            pos = texto.find(l)
            print(f"  L{i:>4}  [{pos:>6}]  {l}")
