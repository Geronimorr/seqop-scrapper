import json, sys
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', closefd=False)

with open('checklist_normativo_resultado.json','r',encoding='utf-8') as f:
    norm = json.load(f)
print('=== NORMATIVO ===')
cats = norm.get('categorias',[])
print(f'Categorias: {len(cats)}')
for c in cats:
    itens = c.get('itens',[])
    cid = c.get('id','?')
    nome = c.get('nome','?')
    print(f'  {cid} - {nome}: {len(itens)} itens')
# show item structure
if cats and cats[0].get('itens'):
    print(f'\nItem keys: {list(cats[0]["itens"][0].keys())}')
    print(f'Sample item: {json.dumps(cats[0]["itens"][0], ensure_ascii=False)[:300]}')

print()
with open('comentarios_mpd.json','r',encoding='utf-8') as f:
    comments = json.load(f)
print('=== COMENTARIOS ===')
print(f'Total SEQOPs: {len(comments)}')
total_c = sum(d.get('total_comentarios',0) for d in comments)
total_mpd = sum(d.get('total_mpd',0) for d in comments)
print(f'Comentarios: {total_c} (MPD: {total_mpd})')
if comments:
    print(f'Keys: {list(comments[0].keys())}')
    for d in comments:
        for cc in d.get('comentarios_mpd',[])[:1]:
            print(f'Sample: {cc["texto"][:200]}')
            break

# Count all MPD comments with text
all_mpd = []
for d in comments:
    for cc in d.get('comentarios_mpd',[]):
        if cc.get('texto'):
            all_mpd.append(cc['texto'][:100])
print(f'\nTotal MPD comments with text: {len(all_mpd)}')
for i, t in enumerate(all_mpd[:5]):
    print(f'  [{i+1}] {t}')
