"""Visualiza resultados do enriquecimento."""
import json

with open("seqops_enriquecidas.json", "r", encoding="utf-8") as f:
    dados = json.load(f)

print(f"Total SEQOPs no JSON: {len(dados)}")
for r in dados:
    a = r.get("analise_ia")
    titulo = r.get("titulo", "?")[:55]
    if not a:
        print(f"  FALHA: {titulo}")
        continue
    blocos = a.get("blocos_mpd", [])
    coments = a.get("comentarios", a.get("comentarios_analisados", []))
    dp = a.get("dados_poco", {})
    print(f"\n  {titulo}")
    print(f"    tipo: {a.get('tipo_operacao','?')}")
    print(f"    {len(blocos)} blocos MPD | {len(coments)} comentários analisados")
    for b in blocos[:5]:
        nome = b.get("nome", "?")[:50]
        rel = b.get("rel", b.get("relevancia_mpd", "?"))
        itens = b.get("itens", b.get("itens_seqop", []))
        print(f"    ➤ {nome:<50} rel={rel}  ({len(itens)} itens)")
    if len(blocos) > 5:
        print(f"    ... +{len(blocos)-5} blocos")
    
    for c in coments[:4]:
        idx = c.get("i", c.get("indice", "?"))
        rel = c.get("rel", c.get("relevancia_mpd", "?"))
        check = c.get("check", c.get("ponto_verificacao"))
        resumo = c.get("resumo", "")[:80]
        print(f"    #{idx} [{rel}] {resumo}")
        if check:
            print(f"       → {check[:80]}")
    
    print(f"    dados_poco: {list(dp.keys())}")
