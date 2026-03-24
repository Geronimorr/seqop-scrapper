"""
Análise completa dos resultados de enriquecimento.
Gera estatísticas detalhadas e identifica falhas para retry.
"""
import json
from collections import Counter, defaultdict
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
SAIDA = SCRIPT_DIR / "seqops_enriquecidas.json"

with open(SAIDA, "r", encoding="utf-8") as f:
    dados = json.load(f)

# ── Classificação ──────────────────────────────────────────────────────────
def _tem_blocos(s):
    ai = s.get("analise_ia")
    return isinstance(ai, dict) and "blocos_mpd" in ai

ok = [s for s in dados if _tem_blocos(s)]
falha = [s for s in dados if s.get("analise_ia") is None and s.get("n_chars_pdf", 0) > 0]
pend = [s for s in dados if not _tem_blocos(s) and s not in falha]

print("=" * 70)
print("RESULTADO DO ENRIQUECIMENTO")
print("=" * 70)
print(f"  Total SEQOPs:   {len(dados)}")
print(f"  ✓ Sucesso:      {len(ok):>4} ({100*len(ok)/len(dados):.1f}%)")
print(f"  ✗ Falha IA:     {len(falha):>4}")
print(f"  ⏳ Pendente:     {len(pend):>4}")

# ── Estatísticas dos bem-sucedidos ─────────────────────────────────────────
if ok:
    total_blocos = 0
    total_coments = 0
    total_diretos = 0
    total_indiretos = 0
    total_nenhuma = 0
    total_checks = 0
    n_blocos_list = []
    tipos_op = Counter()
    pocos = Counter()
    modelos = Counter()

    for s in ok:
        a = s.get("analise_ia", {})
        blocos = a.get("blocos_mpd", [])
        coments = a.get("comentarios", [])
        
        total_blocos += len(blocos)
        total_coments += len(coments)
        n_blocos_list.append(len(blocos))
        
        for c in coments:
            rel = c.get("rel", "")
            if rel == "DIRETA":
                total_diretos += 1
            elif rel == "INDIRETA":
                total_indiretos += 1
            else:
                total_nenhuma += 1
            if c.get("check"):
                total_checks += 1
        
        tipos_op[a.get("tipo_operacao", "?")] += 1
        pocos[s.get("poco", "?")] += 1
        modelos[s.get("modelo_ia", "?")] += 1

    print(f"\n{'─'*70}")
    print(f"ESTATÍSTICAS DOS {len(ok)} SEQOPs BEM-SUCEDIDOS")
    print(f"{'─'*70}")
    print(f"  Total de blocos MPD:     {total_blocos:>5}  (média: {total_blocos/len(ok):.1f}/SEQOP)")
    print(f"  Comentários analisados:  {total_coments:>5}  (média: {total_coments/len(ok):.1f}/SEQOP)")
    print(f"    ● DIRETA:              {total_diretos:>5}")
    print(f"    ● INDIRETA:            {total_indiretos:>5}")
    print(f"    ● NENHUMA:             {total_nenhuma:>5}")
    print(f"  Check points gerados:    {total_checks:>5}")
    print(f"  Blocos/SEQOP (min/max):  {min(n_blocos_list)}-{max(n_blocos_list)}")

    print(f"\n  Tipos de operação:")
    for tipo, cnt in tipos_op.most_common(20):
        print(f"    {tipo:<40} {cnt:>3}")

    print(f"\n  Poços ({len(pocos)} únicos):")
    for poco, cnt in pocos.most_common():
        print(f"    {poco:<25} {cnt:>3} SEQOPs")

    print(f"\n  Modelos usados:")
    for m, cnt in modelos.most_common():
        print(f"    {m:<25} {cnt:>3}")

    # Tokens (dentro do bloco ok)
    pt_total = sum(s.get("prompt_tokens", 0) or s.get("analise_ia",{}).get("prompt_tokens",0) for s in ok)
    ct_total = sum(s.get("completion_tokens", 0) or s.get("analise_ia",{}).get("completion_tokens",0) for s in ok)
    if pt_total:
        print(f"\n{'─'*70}")
        print("CONSUMO DE TOKENS")
        print(f"{'─'*70}")
        print(f"  Prompt tokens total:     {pt_total:>10,}")
        print(f"  Completion tokens total: {ct_total:>10,}")
        print(f"  Total tokens:            {pt_total+ct_total:>10,}")
        print(f"  Média pt/SEQOP:          {pt_total/len(ok):>10,.0f}")
        print(f"  Média ct/SEQOP:          {ct_total/len(ok):>10,.0f}")

# ── Detalhes das falhas ────────────────────────────────────────────────────
if falha:
    print(f"\n{'─'*70}")
    print(f"FALHAS / SEM ENRIQUECIMENTO ({len(falha)})")
    print(f"{'─'*70}")
    for s in falha:
        titulo = s.get("titulo", "?")[:60]
        poco = s.get("poco", "?")
        print(f"  [{poco}] {titulo}")

# ── Pendentes ──────────────────────────────────────────────────────────────
if pend:
    print(f"\n{'─'*70}")
    print(f"PENDENTES ({len(pend)})")
    print(f"{'─'*70}")
    for s in pend[:10]:
        titulo = s.get("titulo", "?")[:60]
        poco = s.get("poco", "?")
        print(f"  [{poco}] {titulo}")
    if len(pend) > 10:
        print(f"  ... +{len(pend)-10} pendentes")

print(f"\n{'='*70}")
