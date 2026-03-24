# Fluxo Cronológico de Operações MPD — Checklist por Abas
# ========================================================
# Este arquivo define a ordem e agrupamento das operações MPD
# para geração do checklist com abas.
# Editável: altere ordem, nomes, descrições, agrupamentos livremente.
#
# Atualizado: 2026-02-26
# Fonte: 256 SEQOPs classificadas de 28 poços Petrobras

# ─── CICLO PRINCIPAL (repete por fase: superfície → intermediária → produção) ──

FLUXO_OPERACOES = [
    {
        "ordem": 1,
        "aba_id": "instalacao_bop",
        "aba_nome": "Instalação BOP",
        "aba_nome_curto": "BOP",
        "descricao": "Descida do BOP com junta integrada, assentamento, testes pós-assentamento",
        "total_seqops": 59,
        "sub_tipos": [
            "Descida do BOP com junta integrada",
            "Descida de BHA e testes do BOP",
            "Teste de pressão de linhas e válvulas",
            "Troca de fluido e equalização de pressão",
            "Teste funcional de sistemas MPD",
            "Montagem e descida de BHA liso",
            "Instalação de junta integrada e testes subsequentes",
        ],
        "quando": "Início de cada fase do poço, após posicionamento da sonda",
        "fase_tipica": ["superficie", "intermediaria", "producao"],
    },
    {
        "ordem": 2,
        "aba_id": "descida_bha_teste",
        "aba_nome": "Descida BHA / Teste MPD",
        "aba_nome_curto": "BHA+Teste",
        "descricao": "Montagem e descida do BHA (16\", 12¼\", 8½\"), teste do sistema MPD e BOP",
        "total_seqops": 49,
        "sub_tipos": [
            "Descida de BHA 16\"",
            "Descida de BHA 12¼\" x 13½\"",
            "Descida de BHA 8½\"",
            "Teste do sistema MPD",
            "Teste do BOP",
            "Fingerprint offline (pós-descida)",
            "Troca de fluido (pós-descida)",
            "Montagem de BHA",
            "Sidetrack",
        ],
        "quando": "Após instalação do BOP, antes de iniciar perfuração de cada fase",
        "fase_tipica": ["superficie", "intermediaria", "producao"],
    },
    {
        "ordem": 3,
        "aba_id": "fingerprint",
        "aba_nome": "Fingerprint / Treinamento",
        "aba_nome_curto": "FP/Treino",
        "descricao": "Fingerprint offline/online, MPD drill, choke drill, treinamento prático MPD, calibração hidráulica",
        "total_seqops": 42,
        "sub_tipos": [
            "Fingerprint offline",
            "Fingerprint online",
            "Treinamento prático MPD",
            "MPD Drill",
            "Choke Drill",
            "DLOT",
            "Corte de cimento (dentro do fingerprint)",
            "Troca de fluido (dentro do fingerprint)",
            "Simulado de Hang-off",
            "Calibração do modelo hidráulico",
            "Teste de influxo (DPPT/DFIT)",
        ],
        "quando": "Após descida do BHA, antes da perfuração — calibração e treinamento da equipe",
        "fase_tipica": ["superficie", "intermediaria", "producao"],
    },
    {
        "ordem": 4,
        "aba_id": "troca_fluido",
        "aba_nome": "Troca de Fluido / Condicionamento",
        "aba_nome_curto": "Fluido",
        "descricao": "Substituição de fluido (leve⇄pesado), condicionamento do poço, preparação para próxima etapa",
        "total_seqops": 54,
        "sub_tipos": [
            "Troca de fluido em modo MPD",
            "Condicionamento após perfilagem",
            "Retirada de coluna com troca de fluido",
            "Amortecimento e troca de fluido",
            "Condicionamento para descida de calha",
            "Teste de sistemas MPD durante troca de fluido",
        ],
        "quando": "Transição entre etapas: antes/depois da perfuração, perfilagem, testemunhagem",
        "fase_tipica": ["superficie", "intermediaria", "producao"],
    },
    {
        "ordem": 5,
        "aba_id": "corte_cimento_fit",
        "aba_nome": "Corte Cimento / FIT / DLOT",
        "aba_nome_curto": "Cimento/FIT",
        "descricao": "Corte de cimento na sapata, testes de integridade da formação (FIT, DLOT, DFIT)",
        "total_seqops": 23,
        "sub_tipos": [
            "Corte de cimento",
            "FIT (Formation Integrity Test)",
            "DLOT (Dynamic Leak-Off Test)",
            "DFIT (Diagnostic Fracture Injection Test)",
            "Perfuração associada a corte de cimento",
            "Conversão para PMCD",
            "Conversão para FMCD",
            "Teste de injetividade",
            "Troca de fluido (pós-corte)",
            "Teste MPD (pós-corte)",
        ],
        "quando": "Após fingerprint/treinamento, antes de iniciar a perfuração da fase",
        "fase_tipica": ["superficie", "intermediaria", "producao"],
    },
    {
        "ordem": 6,
        "aba_id": "perfuracao",
        "aba_nome": "Perfuração com MPD",
        "aba_nome_curto": "Perfuração",
        "descricao": "Perfuração da fase em modo MPD/SBP/FMCD/PMCD",
        "total_seqops": 59,
        "sub_tipos": [
            "Perfuração 16\" em MPD/SBP (fase debug/superfície)",
            "Perfuração 12¼\" com MPD (intermediária)",
            "Perfuração 8½\" com MPD (produção)",
            "Perfuração em FMCD",
            "Perfuração em PMCD dinâmico",
            "Contingência para perfuração em FMCD/PMCD",
            "Manobra para troca de BHA em MPD",
        ],
        "quando": "Etapa principal de cada fase do poço",
        "fase_tipica": ["superficie", "intermediaria", "producao"],
    },
    {
        "ordem": 7,
        "aba_id": "testemunhagem",
        "aba_nome": "Testemunhagem",
        "aba_nome_curto": "Testem.",
        "descricao": "Testemunhagem com controle MPD (fases intermediária e produção)",
        "total_seqops": 8,
        "sub_tipos": [
            "Testemunhagem 8½\" em MPD",
            "Testemunhagem 12¼\" em MPD",
            "Testemunhagem com troca de fluido sem PWD",
            "Testemunhagem com PRC em modo MPD",
        ],
        "quando": "Durante ou após perfuração, quando há necessidade de amostragem de rocha",
        "fase_tipica": ["intermediaria", "producao"],
    },
    {
        "ordem": 8,
        "aba_id": "retirada_bha",
        "aba_nome": "Retirada BHA / Manobra",
        "aba_nome_curto": "Manobra",
        "descricao": "Troca de broca, manobra para perfilagem, retirada de coluna",
        "total_seqops": 19,
        "sub_tipos": [
            "Troca de broca",
            "Teste de pressão Hold Point",
            "Controle do poço via circuito de superfície",
        ],
        "quando": "Entre corridas de perfuração, para perfilagem, ou troca de BHA",
        "fase_tipica": ["intermediaria", "producao"],
    },
    {
        "ordem": 9,
        "aba_id": "teste_influxo",
        "aba_nome": "Teste Influxo / Teste BOP",
        "aba_nome_curto": "Tst Influxo",
        "descricao": "Teste periódico do BOP com ITT PUAO, teste de influxo",
        "total_seqops": 16,
        "sub_tipos": [
            "Teste do BOP com ITT PUAO",
            "Teste do sistema MPD",
            "Corte do cimento (dentro do teste)",
            "Troca do fluido (dentro do teste)",
        ],
        "quando": "Periodicamente (a cada 14 dias ou mudança de fase)",
        "fase_tipica": ["superficie", "intermediaria", "producao"],
    },

    # ─── OPERAÇÕES TRANSVERSAIS (podem ocorrer a qualquer momento) ─────────

    {
        "ordem": 10,
        "aba_id": "contingencia_pmcd_fmcd",
        "aba_nome": "Contingência / FMCD / PMCD",
        "aba_nome_curto": "Conting.",
        "descricao": "Combate a perda, conversão para PMCD/FMCD, ações emergenciais",
        "total_seqops": 38,
        "sub_tipos": [
            "Combate à perda com LCM via PBL",
            "Combate à perda com Well Defend",
            "Combate à perda com cimento por injeção direta",
            "Conversão para perfuração em PMCD",
            "Instalação de cauda PACI em FMCD",
            "Treinamento FMCD",
        ],
        "quando": "A qualquer momento durante a perfuração quando há perda de circulação",
        "fase_tipica": ["intermediaria", "producao"],
        "inclui_pescaria": True,
        "pescaria_sub_tipos": [
            "Pescaria de esfera de desativação",
            "Reconexão de DC para pescaria do BHA",
            "Pescaria com canguru/sub cesta",
            "Recuperação da WB da BAP com WBRT",
            "Recuperação do packer de abandono inferior",
            "Teste do BOP e recuperação do packer Archer superior",
        ],
        "pescaria_total_seqops": 6,
    },

    # ─── FASE FINAL ──────────────────────────────────────────────────────

    {
        "ordem": 11,
        "aba_id": "completacao_paci",
        "aba_nome": "Completação / PACI / Cauda",
        "aba_nome_curto": "Completação",
        "descricao": "Instalação de cauda PACI, teste VIF, estimulação ácida, abandono",
        "total_seqops": 15,
        "sub_tipos": [
            "Teste de VIF",
            "Instalação de cauda PACI",
            "Manobra com STX e Shifter SSD",
            "Teste e inspeção de NRVs",
        ],
        "quando": "Após completar todas as fases de perfuração",
        "fase_tipica": ["completacao"],
        "inclui_tampao": True,
        "tampao_sub_tipos": [
            "Tampão de cimento",
            "Amortecimento do poço",
            "Abandono temporário",
            "Abandono definitivo",
        ],
        "tampao_total_seqops": 7,
    },
]


# ─── METADADOS ──────────────────────────────────────────────────────────

METADADOS = {
    "total_seqops": 256,
    "total_pocos": 28,
    "total_comentarios": 1332,
    "total_comentarios_mpd": 377,
    "modos_mpd": ["MPD", "SBP", "FMCD", "PMCD", "MCD"],
    "fases_poco": ["superficie", "intermediaria", "producao", "completacao"],
    "data_atualizacao": "2026-02-26",
    "nota": (
        "O ciclo principal (abas 1-9) repete-se para cada fase do poço. "
        "Contingência (aba 10) pode ocorrer a qualquer momento. "
        "Completação (aba 11) é a fase final."
    ),
}


# ─── RESUMO VISUAL ──────────────────────────────────────────────────────
#
#  ┌─────────────────── CICLO POR FASE (superfície → intermediária → produção) ──────┐
#  │                                                                                  │
#  │  1. Instalação BOP  ──►  2. Descida BHA/Teste  ──►  3. Fingerprint/Treino      │
#  │         │                                                     │                  │
#  │         │            4. Troca Fluido  ◄──────────────────────┘                  │
#  │         │                    │                                                   │
#  │         │            5. Corte Cimento / FIT                                      │
#  │         │                    │                                                   │
#  │         │            6. PERFURAÇÃO MPD  ◄──── etapa principal                    │
#  │         │                    │                                                   │
#  │         │            7. Testemunhagem (quando aplicável)                          │
#  │         │                    │                                                   │
#  │         │            8. Retirada BHA / Manobra  ──────►  (volta ao passo 2       │
#  │         │                    │                            para próxima corrida)   │
#  │         │            9. Teste Influxo / Teste BOP (periódico)                    │
#  │         │                                                                        │
#  │         └──► (próxima fase)                                                      │
#  │                                                                                  │
#  │  ═══ TRANSVERSAL ═══                                                            │
#  │  10. Contingência / FMCD / PMCD / Pescaria  (a qualquer momento)                │
#  │                                                                                  │
#  │  ═══ FASE FINAL ═══                                                             │
#  │  11. Completação / PACI / Cauda / Tampão / Abandono                              │
#  │                                                                                  │
#  └──────────────────────────────────────────────────────────────────────────────────┘
#
