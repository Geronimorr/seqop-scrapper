import json

with open('seqops_enriquecidas.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Filter seqops related to PMCD conversion
pmcd_seqops = []
for sq in data:
    ia = sq.get('analise_ia', {})
    dp = ia.get('dados_poco', {})
    tipo = ia.get('tipo_operacao', '') or ''
    
    modo_mpd = str(dp.get('modo_mpd', '') or '')
    modo_mpd_plan = str(dp.get('modo_mpd_planejado', '') or '')
    modo_mpd_prev = str(dp.get('modo_mpd_previsto', '') or '')
    modo_mpd_princ = str(dp.get('modo_mpd_principal', '') or '')
    
    all_modes = modo_mpd + modo_mpd_plan + modo_mpd_prev + modo_mpd_princ + tipo
    
    if 'PMCD' in all_modes.upper() or 'pmcd' in tipo.lower():
        pmcd_seqops.append({
            'titulo': sq.get('titulo', ''),
            'poco': sq.get('poco', ''),
            'url': sq.get('url', ''),
            'hits_mpd': sq.get('hits_mpd', 0) or 0,
            'n_secoes_alta': sq.get('n_secoes_alta', 0) or 0,
            'n_chars_pdf': sq.get('n_chars_pdf', 0) or 0,
            'n_comentarios_mpd': sq.get('n_comentarios_mpd', 0) or 0,
            'n_comentarios_total': sq.get('n_comentarios_total', 0) or 0,
            'tipo_operacao': tipo,
            'modo': all_modes[:300]
        })

# Sort by hits_mpd descending 
pmcd_seqops.sort(key=lambda x: x.get('hits_mpd', 0), reverse=True)
print(f"Total seqops com PMCD: {len(pmcd_seqops)}")
print()
for i, s in enumerate(pmcd_seqops[:25]):
    print(f"{i+1:2d}. hits_mpd={s['hits_mpd']:4d} | secoes_alta={s['n_secoes_alta']:2d} | coment_mpd={s['n_comentarios_mpd']:2d} | chars={s['n_chars_pdf']:6d}")
    print(f"    Poco: {s['poco']} | Titulo: {s['titulo'][:90]}")
    print(f"    Tipo: {s['tipo_operacao']}")
    print(f"    URL: {s['url']}")
    print()

# Now check classificadas for the contingencia_pmcd_fmcd specific analysis
print("=" * 100)
print("ANALISE DO TIPO contingencia_pmcd_fmcd em seqops_classificadas.json:")
print("=" * 100)
with open('seqops_classificadas.json', 'r', encoding='utf-8') as f:
    clas = json.load(f)

pmcd_tipo = clas.get('analise_ia', {}).get('contingencia_pmcd_fmcd', {})
if pmcd_tipo:
    print(f"Tipo: {pmcd_tipo.get('tipo_nome', '')}")
    print(f"Total seqops: {pmcd_tipo.get('total_seqops', 0)}")
    print(f"Total comentarios MPD: {pmcd_tipo.get('total_comentarios_mpd', 0)}")
    
    sub_analise = pmcd_tipo.get('analise_ia', {})
    if sub_analise:
        print(f"\nSub-tipos: {sub_analise.get('sub_tipos', [])}")
        print(f"\nPadroes recorrentes: {sub_analise.get('padroes_recorrentes', [])}")
        print(f"\nLacunas: {sub_analise.get('lacunas', [])}")
        
        # Look for score/ranking info
        for k, v in sub_analise.items():
            if 'score' in k.lower() or 'rank' in k.lower() or 'melhor' in k.lower() or 'pont' in k.lower():
                print(f"\n{k}: {v}")
