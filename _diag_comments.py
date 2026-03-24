import json, sys
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', closefd=False)

# 1) Comentarios disponiveis
with open('comentarios_mpd.json', 'r', encoding='utf-8') as f:
    coment = json.load(f)

print('=== COMENTARIOS MPD ===')
print(f"SEQOPs: {len(coment.get('seqops', []))}")
agregados = coment.get('comentarios_agregados', [])
print(f"Agregados: {len(agregados)}")
for c in agregados:
    cat = c.get('categoria_normativa', '?')
    resumo = c.get('resumo', c.get('texto', ''))[:120]
    freq = c.get('frequencia', 1)
    print(f"  [{cat}] (freq={freq}) {resumo}")

# 2) Resultado v2.0 - itens com evidencia de comentarios
print('\n=== RESULTADO v2.0 - ITENS COM EVIDENCIA DE COMENTARIOS ===')
with open('checklist_combinado_resultado.json', 'r', encoding='utf-8') as f:
    res = json.load(f)

n_com_ev = 0
n_com_lic = 0
n_coment = 0
for cat in res.get('categorias', []):
    for item in cat.get('itens', []):
        ev = item.get('evidencia_comentarios', '')
        lic = item.get('licoes_aprendidas', '')
        orig = item.get('origem', '')
        if ev and 'sem evid' not in ev.lower():
            n_com_ev += 1
            print(f"  {item.get('id')} [{orig}] ev={ev[:120]}")
        if lic:
            n_com_lic += 1
        if orig == 'COMENTARIOS':
            n_coment += 1
            print(f"  ** NOVO COMENT: {item.get('id')} - {item.get('descricao','')[:100]}")

print(f"\nResumo: {n_com_ev} com evidencia, {n_com_lic} com licoes, {n_coment} novos de comentarios")

# 3) Comparar com v1.0 - se houver backup
print('\n=== MAPEAMENTO PASSO A (ultimo run) ===')
# Vamos ver o que o Passo A mapeou - checar se os comentarios estao chegando no enriquecimento
print('Comentarios por categoria (agregados):')
cat_map = {}
for c in agregados:
    cat = c.get('categoria_normativa', 'SEM_CAT')
    cat_map.setdefault(cat, []).append(c)
for cat_id, items in sorted(cat_map.items()):
    print(f"  {cat_id}: {len(items)} comentarios")
    for it in items:
        print(f"    - {it.get('resumo', it.get('texto',''))[:100]}")
