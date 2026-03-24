"""Inspeciona estrutura dos dados enriquecidos."""
import json
from pathlib import Path
from collections import Counter

SAIDA = Path(__file__).resolve().parent / "seqops_enriquecidas.json"

d = json.load(open(SAIDA, "r", encoding="utf-8"))

# Encontrar SEQOP com comentários
for s in d:
    ai = s.get("analise_ia", {})
    c = ai.get("comentarios_analisados", [])
    if len(c) >= 3:
        print(f'=== {s["poco"]} - {s["titulo"][:60]}')
        print(f'tipo_operacao: {ai.get("tipo_operacao")}')
        print(f'blocos: {len(ai.get("blocos_mpd",[]))} | comentarios: {len(c)}')
        print(f'coment[0] keys: {list(c[0].keys())}')
        print(f'coment[0]: {json.dumps(c[0], ensure_ascii=False)[:400]}')
        print()
        b = ai.get("blocos_mpd", [])
        print(f'bloco[0]: {json.dumps(b[0], ensure_ascii=False)[:300]}')
        break

# Coleta de tipos de operação
tipos = Counter()
for s in d:
    ai = s.get("analise_ia", {})
    t = ai.get("tipo_operacao", "?")
    tipos[t] += 1

print(f"\n=== TODOS OS TIPOS ({len(tipos)} únicos) ===")
for t, cnt in tipos.most_common():
    print(f"  {t:<55} {cnt:>3}")

# Contar checks
total_checks = 0
for s in d:
    ai = s.get("analise_ia", {})
    for c in ai.get("comentarios_analisados", []):
        if c.get("check"):
            total_checks += 1
print(f"\nTotal check points: {total_checks}")

# Temas mais frequentes nos comentários
temas = Counter()
for s in d:
    ai = s.get("analise_ia", {})
    for c in ai.get("comentarios_analisados", []):
        for t in c.get("temas", []):
            temas[t] += 1
print(f"\n=== TOP 30 TEMAS ===")
for t, cnt in temas.most_common(30):
    print(f"  {t:<55} {cnt:>3}")
