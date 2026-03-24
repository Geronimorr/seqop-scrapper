import json

d = json.load(open('seqops_enriquecidas.json','r',encoding='utf-8'))
for item in d:
    ai = item.get('analise_ia')
    titulo = item.get('titulo','?')[:60]
    if ai:
        print(f"OK: {titulo}")
        print(f"  blocos: {len(ai.get('blocos_mpd',[]))}")
        print(f"  comentarios_analisados: {len(ai.get('comentarios_analisados',[]))}")
        for b in ai.get('blocos_mpd',[])[:4]:
            print(f"    BLOCO: {b['nome']} ({b['relevancia_mpd']})")
            for i in b.get('itens_seqop',[])[:2]:
                print(f"      - {str(i)[:80]}")
        for c in ai.get('comentarios_analisados',[]):
            rel = c.get('relevancia_mpd','?')
            tipo = c.get('tipo_csd','?')
            bloco = str(c.get('bloco_referenciado','?'))[:30]
            print(f"    COM [{tipo}] rel={rel} bloco={bloco}")
            pv = c.get('ponto_verificacao','')
            if pv:
                print(f"      PV: {pv[:100]}")
        dp = ai.get('dados_poco',{})
        if dp:
            print(f"  DADOS_POCO: {json.dumps(dp, ensure_ascii=False)[:200]}")
    else:
        raw = item.get('resposta_raw','')
        print(f"FALHA: {titulo}")
        print(f"  raw[-300:]: {raw[-300:]}")
    print()
