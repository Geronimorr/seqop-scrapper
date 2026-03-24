import json

with open('seqops_enriquecidas.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Focus on seqops specifically about PMCD conversion
conversion_keywords = ['conversao', 'conversão', 'pmcd']

pmcd_conversion = []
for sq in data:
    titulo = (sq.get('titulo', '') or '').lower()
    tipo = (sq.get('analise_ia', {}).get('tipo_operacao', '') or '').lower()
    
    is_conversion = ('convers' in titulo and 'pmcd' in titulo) or \
                    ('convers' in tipo and 'pmcd' in tipo) or \
                    ('pmcd' in tipo and 'perfuracao' not in tipo and 'fingerprint' not in tipo and 'treinamento' not in tipo) or \
                    ('perfuracao' in tipo and 'pmcd' in tipo) or \
                    ('pmcd' in titulo.lower())
    
    if is_conversion:
        # Calculate a composite score
        hits = sq.get('hits_mpd', 0) or 0
        secoes_alta = sq.get('n_secoes_alta', 0) or 0
        coment_mpd = sq.get('n_comentarios_mpd', 0) or 0
        chars = sq.get('n_chars_pdf', 0) or 0
        
        # Composite score weighting: hits (40%), secoes_alta (30%), comentarios (20%), chars (10%)
        score = (hits * 0.4) + (secoes_alta * 10 * 0.3) + (coment_mpd * 20 * 0.2) + (chars / 1000 * 0.1)
        
        pmcd_conversion.append({
            'titulo': sq.get('titulo', ''),
            'poco': sq.get('poco', ''),
            'url': sq.get('url', ''),
            'hits_mpd': hits,
            'n_secoes_alta': secoes_alta,
            'n_comentarios_mpd': coment_mpd,
            'n_chars_pdf': chars,
            'tipo_operacao': sq.get('analise_ia', {}).get('tipo_operacao', ''),
            'score': round(score, 1)
        })

pmcd_conversion.sort(key=lambda x: x['score'], reverse=True)

print(f"=== SEQOPS RELACIONADAS A PMCD (SCORE COMPOSTO) ===")
print(f"Total: {len(pmcd_conversion)}")
print()
print(f"{'#':>2} {'Score':>7} {'Hits':>5} {'Alta':>4} {'CMpd':>4} {'Chars':>6}  {'Poco':<20} {'Titulo'}")
print("-" * 130)
for i, s in enumerate(pmcd_conversion[:30]):
    print(f"{i+1:2d} {s['score']:7.1f} {s['hits_mpd']:5d} {s['n_secoes_alta']:4d} {s['n_comentarios_mpd']:4d} {s['n_chars_pdf']:6d}  {s['poco']:<20} {s['titulo'][:70]}")
    print(f"   Tipo: {s['tipo_operacao']}")
    print(f"   URL: {s['url']}")
    print()
