import json

with open('checklist_combinado_resultado.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

cats = data.get('categorias', [])
print(f"Categorias: {len(cats)}")
total_itens = 0
itens_normativo = 0
itens_comentarios = 0
itens_licoes = 0
itens_com_evidencia = 0
itens_com_licoes = 0

for cat in cats:
    itens = cat.get('itens', [])
    total_itens += len(itens)
    for item in itens:
        origem = item.get('origem', '')
        if origem == 'NORMATIVO':
            itens_normativo += 1
        elif origem == 'COMENTARIOS':
            itens_comentarios += 1
        elif origem == 'LICOES':
            itens_licoes += 1
        
        ev = item.get('evidencia_comentarios', '')
        if ev and 'Sem' not in ev and ev != 'N/A':
            itens_com_evidencia += 1
        
        lic = item.get('licoes_aprendidas', '')
        if lic and lic not in ('', 'N/A', 'Sem lições'):
            itens_com_licoes += 1
    
    print(f"  {cat.get('id','?')}: {cat.get('nome','?')[:50]} -> {len(itens)} itens")
    for item in itens:
        status = []
        if item.get('origem') == 'COMENTARIOS':
            status.append('COMENT')
        elif item.get('origem') == 'LICOES':
            status.append('LICAO')
        ev = item.get('evidencia_comentarios', '')
        if ev and 'Sem' not in ev and ev != 'N/A':
            status.append(f'EVID({len(ev)} chars)')
        lic = item.get('licoes_aprendidas', '')
        if lic and lic not in ('', 'N/A', 'Sem lições'):
            status.append(f'LIC({len(lic)} chars)')
        
        if status:
            print(f"    - {item.get('item','?')[:60]} [{', '.join(status)}]")

print(f"\nTotal: {total_itens}")
print(f"  Normativo: {itens_normativo}")
print(f"  Comentários: {itens_comentarios}")
print(f"  Lições: {itens_licoes}")
print(f"  Com evidência: {itens_com_evidencia}")
print(f"  Com lições: {itens_com_licoes}")

# Show _estatisticas
estat = data.get('_estatisticas', {})
if estat:
    print(f"\nEstatísticas do pipeline:")
    for k, v in estat.items():
        print(f"  {k}: {v}")
