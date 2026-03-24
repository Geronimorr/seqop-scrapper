import json

d = json.load(open('comentarios_mpd.json', 'r', encoding='utf-8'))

print(f"Total SEQOPs: {len(d)}")
print(f"Chaves em cada item: {list(d[0].keys())}\n")

# Amostra de conteudo_seqop
for i in [0, 50, 100, 150, 200, 255]:
    if i >= len(d):
        continue
    item = d[i]
    c = item.get('conteudo_seqop', '')
    titulo = item.get('titulo', '?')
    n_com = item.get('total_comentarios', 0)
    n_mpd = item.get('total_mpd', 0)
    print(f"[{i}] {titulo}")
    print(f"    conteudo_seqop: {len(c)} chars | comentarios: {n_com} total, {n_mpd} MPD")
    if c:
        print(f"    primeiros 300 chars:")
        print(f"    {c[:300]}")
    else:
        print(f"    ** SEM CONTEUDO SEQOP **")
    print()

# Checar quantos têm conteudo_seqop
com_conteudo = sum(1 for x in d if x.get('conteudo_seqop', '').strip())
sem_conteudo = len(d) - com_conteudo
print(f"\nCom conteudo_seqop: {com_conteudo}")
print(f"Sem conteudo_seqop: {sem_conteudo}")

# Tamanho médio
tamanhos = [len(x.get('conteudo_seqop', '')) for x in d if x.get('conteudo_seqop', '')]
if tamanhos:
    print(f"Tamanho médio: {sum(tamanhos)//len(tamanhos)} chars")
    print(f"Maior: {max(tamanhos)} chars")
    print(f"Menor: {min(tamanhos)} chars")

# Checar tipos de comentários que NÃO são CSD-MPD
tipos = {}
for item in d:
    for com in item.get('comentarios', []):
        t = com.get('tipo_csd', '?')
        tipos[t] = tipos.get(t, 0) + 1

print(f"\nTipos de comentário encontrados:")
for t, n in sorted(tipos.items(), key=lambda x: -x[1]):
    print(f"  {t}: {n}")
