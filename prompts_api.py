# =============================================================================
# CATÁLOGO DE PROMPTS — Pipeline de Classificação e Checklist MPD
# =============================================================================
# 
# Este arquivo centraliza TODOS os prompts utilizados nas chamadas de API do
# pipeline. Cada prompt tem:
#   - ID único para referência
#   - Script de origem
#   - Papel (system / user)
#   - Contexto de uso
#   - O texto completo
#
# Para alterar um prompt, edite aqui e depois atualize no script correspondente.
#
# Atualizado: 2026-02-26
# =============================================================================

from textwrap import dedent
from fluxo_operacoes_mpd import FLUXO_OPERACOES


# ─────────────────────────────────────────────────────────────────────────────
# CONTEXTO COMPARTILHADO: inserido em todos os prompts como preâmbulo
# ─────────────────────────────────────────────────────────────────────────────

CONTEXTO_MPD = dedent("""\
Você é um especialista em perfuração MPD (Managed Pressure Drilling) da Petrobras,
com profundo conhecimento do fluxo operacional completo de um poço offshore.

FLUXO CRONOLÓGICO DAS OPERAÇÕES MPD (por fase do poço):
  1. Instalação BOP — descida do BOP com junta integrada, assentamento, testes
  2. Descida BHA / Teste MPD — montagem e descida do BHA, teste do sistema MPD e BOP
  3. Fingerprint / Treinamento — fingerprint offline/online, MPD drill, choke drill, calibração
  4. Troca de Fluido — substituição de fluido, condicionamento, preparação
  5. Corte Cimento / FIT / DLOT — corte de cimento na sapata, testes de integridade
  6. Perfuração MPD — perfuração da fase (MPD/SBP/FMCD/PMCD)
  7. Testemunhagem — amostragem com controle MPD (quando aplicável)
  8. Retirada BHA / Manobra — troca de broca, manobra para perfilagem
  9. Teste Influxo / Teste BOP — teste periódico (14 dias ou mudança de fase)
  Transversal: Contingência / FMCD / PMCD / Pescaria (a qualquer momento)
  Final: Completação / PACI / Cauda / Tampão / Abandono

Modos MPD: MPD (SBP), FMCD, PMCD, MCD
Fases do poço: superfície (16"), intermediária (12¼"), produção (8½"), completação
""")


# ─────────────────────────────────────────────────────────────────────────────
# FUNÇÕES AUXILIARES PARA CONSTRUIR NOMES DE TIPO
# ─────────────────────────────────────────────────────────────────────────────

def _nome_tipo(aba_id: str) -> str:
    """Retorna o nome legível de um tipo de operação dado o aba_id."""
    for op in FLUXO_OPERACOES:
        if op["aba_id"] == aba_id:
            return op["aba_nome"]
    return aba_id


# =============================================================================
# PROMPT 1 — classificar_seqops.py → refinar_classificacao_ia()
# =============================================================================
# Usado em: classificar_seqops.py, função refinar_classificacao_ia()
# Quando: Fase 2 da classificação — análise IA por tipo de operação
# Entrada: Comentários MPD agrupados por tipo de operação
# Saída: JSON com sub_tipos, pontos_verificacao, erros_frequentes, padroes, normas
# =============================================================================

P1_SYSTEM = dedent("""\
{contexto}

Responda SOMENTE em JSON válido, em português brasileiro.
Sem markdown, sem ```json, sem explicações fora do JSON.
""").format(contexto=CONTEXTO_MPD)

def p1_user_classificacao(tipo_nome: str, total_comentarios: int, posicao_fluxo: int) -> str:
    """
    Prompt do usuário para classificação IA de um tipo de operação.
    
    Args:
        tipo_nome: Nome legível do tipo (ex: "Perfuração com MPD")
        total_comentarios: Quantidade de comentários MPD do tipo
        posicao_fluxo: Posição no fluxo cronológico (1-11)
    
    Returns:
        String do prompt (deve ser concatenada com os comentários)
    """
    return dedent(f"""\
    Abaixo estão {total_comentarios} comentários REAIS de revisores CSD-MPD sobre SEQOPs
    do tipo: **{tipo_nome}** (etapa {posicao_fluxo} do fluxo operacional MPD).

    CONTEXTO DA OPERAÇÃO NO FLUXO:
    - Esta operação é a etapa #{posicao_fluxo} do ciclo de perfuração de cada fase
    - Etapa anterior: {_etapa_adjacente(posicao_fluxo, -1)}
    - Etapa seguinte: {_etapa_adjacente(posicao_fluxo, +1)}

    TAREFA: Analise os comentários e extraia:

    1. **sub_tipos**: Sub-categorias dentro deste tipo de operação
       (ex: dentro de "Perfuração", há perfuração 16", 12¼", 8½", debug, FMCD, etc.)

    2. **pontos_verificacao**: Os itens que o revisor MPD MAIS cobra/verifica
       neste tipo de operação. Cada ponto deve ser uma verificação CONCRETA e ACIONÁVEL
       que possa ser transformada em item de checklist (SIM/NÃO).
       Formato: "Verificar se...", "Confirmar que...", "A SEQOP inclui..."

    3. **erros_frequentes**: Erros ou omissões recorrentes que o revisor encontra
       nas SEQOPs deste tipo

    4. **padroes_aprovacao**: O que o revisor gosta de ver — boas práticas que
       facilitam a aprovação da SEQOP

    5. **normas_aplicaveis**: Normas/padrões técnicos Petrobras mencionados ou implícitos
       (ex: PE-2POC-01113, PE-1PBR-00486, etc.)

    6. **interface_etapas_adjacentes**: Pontos de verificação que dizem respeito à
       TRANSIÇÃO entre esta etapa e a anterior/seguinte no fluxo operacional
       (ex: "Confirmar que o teste do BOP foi concluído antes de iniciar fingerprint")

    Responda EXCLUSIVAMENTE em JSON válido:
    {{
      "sub_tipos": ["sub-tipo 1", "sub-tipo 2"],
      "pontos_verificacao": [
        {{
          "item": "Verificar se... (descrição clara e acionável)",
          "frequencia": "alta/media/baixa",
          "exemplo_real": "Trecho do comentário que motivou este ponto"
        }}
      ],
      "erros_frequentes": ["erro 1", "erro 2"],
      "padroes_aprovacao": ["boa prática 1"],
      "normas_aplicaveis": ["PE-2POC-01113"],
      "interface_etapas_adjacentes": [
        {{
          "direcao": "anterior/posterior",
          "etapa_relacionada": "Nome da etapa",
          "verificacao": "O que verificar na interface entre as etapas"
        }}
      ]
    }}

    COMENTÁRIOS:
    """)


def _etapa_adjacente(posicao: int, delta: int) -> str:
    """Retorna o nome da etapa adjacente no fluxo."""
    pos_alvo = posicao + delta
    for op in FLUXO_OPERACOES:
        if op["ordem"] == pos_alvo:
            return f"{op['aba_nome']} (etapa {pos_alvo})"
    if delta < 0:
        return "(início do ciclo)"
    return "(fim do ciclo / próxima fase)"


# =============================================================================
# PROMPT 2 — gerar_checklist.py → fase_analise() — Etapa 1: Categorias
# =============================================================================
# Usado em: gerar_checklist.py (pipeline original, NÃO USA fluxo cronológico)
# Quando: Primeira chamada IA — identificar categorias e padrões nos comentários
# Entrada: Comentários MPD brutos de todos os tipos (sem classificação)
# =============================================================================

P2_SYSTEM = (
    "Você é um especialista em perfuração MPD da Petrobras. "
    "Responda sempre em JSON válido, em português."
)

P2_USER_CATEGORIAS = dedent("""\
Você é um especialista em perfuração de poços de petróleo, especificamente em operações MPD.

Abaixo estão comentários reais de revisores CSD-MPD sobre SEQOPs de poços da Petrobras.
Cada comentário está no formato: [poço | título da seqop | versão | autor]

TAREFA: Analise todos os comentários e identifique:
1. As CATEGORIAS principais de itens que os revisores MPD verificam/cobram
2. Os PADRÕES recorrentes (itens que aparecem em múltiplas revisões)
3. Os ERROS COMUNS que costumam ser corrigidos
4. Os PADRÕES NORMATIVOS mencionados (ex: PE-2POC-01113)

IMPORTANTE: Organize as categorias seguindo o fluxo cronológico operacional MPD:
  BOP → BHA/Teste → Fingerprint → Troca Fluido → Corte Cimento → Perfuração →
  Testemunhagem → Manobra → Teste Influxo → Contingência → Completação

Responda em JSON com a seguinte estrutura:
{
  "categorias": [
    {
      "nome": "Nome da Categoria (correspondendo ao tipo de operação)",
      "descricao": "Descrição breve",
      "posicao_fluxo": 1,
      "frequencia": "alta/media/baixa",
      "exemplos_comentarios": ["resumo do comentário 1", "resumo 2"]
    }
  ],
  "padroes_recorrentes": [
    {
      "padrao": "Descrição do padrão",
      "frequencia": N,
      "categoria": "categoria relacionada"
    }
  ],
  "erros_comuns": ["erro 1", "erro 2"],
  "normas_mencionadas": ["PE-2POC-01113", ...]
}

COMENTÁRIOS PARA ANÁLISE:
""")


# =============================================================================
# PROMPT 3 — gerar_checklist.py → fase_analise() — Etapa 2: Checklist
# =============================================================================
# Usado em: gerar_checklist.py
# Quando: Segunda chamada IA — gerar checklist a partir das categorias extraídas
# Entrada: Resultado do Prompt 2 (categorias)
# =============================================================================

P3_SYSTEM = (
    "Você é um especialista em perfuração MPD da Petrobras. "
    "Gere o checklist em JSON válido, em português."
)

def p3_user_checklist(analise_categorias: str, total_comentarios: int,
                       total_pocos: int, data_geracao: str) -> str:
    """
    Prompt para gerar o checklist estruturado a partir da análise de categorias.
    """
    return dedent(f"""\
    Você é um especialista em perfuração MPD na Petrobras.

    Com base na análise de categorias abaixo (extraída de {total_comentarios} comentários
    reais de revisores CSD-MPD de {total_pocos} poços), gere um CHECKLIST COMPLETO
    para revisão de SEQOPs que envolvam MPD.

    ESTRUTURA OBRIGATÓRIA: O checklist deve ter UMA CATEGORIA POR TIPO DE OPERAÇÃO,
    seguindo a ordem cronológica do fluxo MPD:
      1. Instalação BOP
      2. Descida BHA / Teste MPD
      3. Fingerprint / Treinamento
      4. Troca de Fluido / Condicionamento
      5. Corte Cimento / FIT / DLOT
      6. Perfuração MPD
      7. Testemunhagem
      8. Retirada BHA / Manobra
      9. Teste Influxo / Teste BOP
      10. Contingência / FMCD / PMCD
      11. Completação / PACI / Cauda

    ANÁLISE DE CATEGORIAS:
    {analise_categorias}

    Responda em JSON:
    {{
      "titulo": "Checklist de Revisão de SEQOPs - CSD-MPD",
      "versao": "2.0",
      "data_geracao": "{data_geracao}",
      "baseado_em": "{total_comentarios} comentários de {total_pocos} poços",
      "categorias": [
        {{
          "id": "CAT-01",
          "nome": "Instalação BOP",
          "descricao": "...",
          "posicao_fluxo": 1,
          "prioridade": "ALTA/MEDIA/BAIXA",
          "itens": [
            {{
              "id": "CAT-01-001",
              "descricao": "Verificar se... (ação clara e objetiva)",
              "detalhes": "Detalhes técnicos e justificativa",
              "referencia_normativa": "PE-XXXX §X.Y",
              "exemplo_comentario": "Exemplo real de comentário de revisor",
              "criticidade": "CRITICA/IMPORTANTE/RECOMENDADA"
            }}
          ]
        }}
      ],
      "observacoes_gerais": ["observação 1"]
    }}

    REQUISITOS:
    - 11 categorias obrigatórias (uma por tipo de operação)
    - Cada categoria: 3 a 12 itens de verificação
    - Itens devem ser verificações CONCRETAS (SIM/NÃO na SEQOP)
    - Linguagem imperativa: "Verificar se...", "Confirmar que...", "A SEQOP inclui..."
    - Inclua limites numéricos quando relevantes (pressões psi, volumes bbl)
    - Inclua referências normativas quando mencionadas
    - Todos os itens devem derivar dos comentários reais analisados
    """)


# =============================================================================
# PROMPT 4 — gerar_checklist_normas.py → PROMPT_SISTEMA_EXTRACAO
# =============================================================================
# Usado em: gerar_checklist_normas.py, fase2_extrair_requisitos()
# Quando: Extração de requisitos de documentos normativos (corpus/ PDFs)
# Entrada: Documentos normativos por lote temático
# =============================================================================

P4_SYSTEM_EXTRACAO = dedent("""\
{contexto}

Sua tarefa é analisar documentos normativos Petrobras e extrair TODOS os pontos
de verificação relevantes para revisão de SEQOPs (sequências operacionais).

Responda SEMPRE em JSON válido, em português brasileiro.
""").format(contexto=CONTEXTO_MPD)

def p4_user_extracao_lote(lote_id: str, lote_nome: str, lote_descricao: str) -> str:
    """
    Prompt para extração de requisitos de um lote de documentos normativos.
    Deve ser concatenado com os textos dos documentos.
    """
    return dedent(f"""\
    Analise os documentos normativos abaixo e extraia TODOS os requisitos, verificações
    e pontos de checklist relevantes para revisão de SEQOPs MPD.

    CONTEXTO DO LOTE: {lote_nome}
    {lote_descricao}

    TAREFA: Para cada requisito encontrado, extraia:
    - categoria: O TIPO DE OPERAÇÃO ao qual o requisito se aplica
      (use os nomes do fluxo: Instalação BOP, Descida BHA, Fingerprint, Troca Fluido,
       Corte Cimento/FIT, Perfuração MPD, Testemunhagem, Manobra, Teste Influxo,
       Contingência, Completação — ou "Geral" se aplicável a todos)
    - requisito: descrição clara do que deve ser verificado na SEQOP
    - detalhes: informações adicionais, limites numéricos, condições
    - secao: seção/parágrafo do documento (se identificável)
    - documento_fonte: nome do PE/Anexo de onde foi extraído
    - criticidade: CRITICA (segurança/mandatory), IMPORTANTE (best practice), RECOMENDADA (nice-to-have)

    Responda em JSON:
    {{
      "lote_id": "{lote_id}",
      "lote_nome": "{lote_nome}",
      "requisitos": [
        {{
          "categoria": "Tipo de operação no fluxo MPD",
          "requisito": "Verificar se...",
          "detalhes": "limites, condições, referências",
          "secao": "§X.Y",
          "documento_fonte": "PE-XXXX-XXXXX",
          "criticidade": "CRITICA|IMPORTANTE|RECOMENDADA"
        }}
      ]
    }}

    INSTRUÇÕES IMPORTANTES:
    - Extraia TODOS os requisitos, não apenas os mais importantes
    - Inclua limites numéricos específicos (pressões, volumes, percentuais)
    - Mantenha a rastreabilidade: indique a seção de origem
    - Foque em itens verificáveis em uma SEQOP
    - Não invente requisitos — extraia apenas o que está nos documentos
    - CLASSIFIQUE cada requisito no tipo de operação correto do fluxo MPD

    DOCUMENTOS PARA ANÁLISE:
    {"=" * 60}
    """)


# =============================================================================
# PROMPT 5 — gerar_checklist_normas.py → fase3_gerar_checklist()
# =============================================================================
# Usado em: gerar_checklist_normas.py
# Quando: Geração do checklist normativo estruturado por tipo de SEQOP
# Entrada: Requisitos extraídos na fase 2
# =============================================================================

P5_SYSTEM_CHECKLIST_NORM = (
    "Você é um especialista em perfuração MPD da Petrobras que revisa SEQOPs. "
    "Gere o checklist em JSON válido, em português brasileiro. "
    "Seja COMPLETO: inclua TODOS os itens relevantes para cada tipo de SEQOP. "
    "Produza de 5 a 12 itens por categoria. Cada item deve ser verificável na SEQOP."
)

def p5_user_checklist_normativo(total_requisitos: int, categorias: list, id_inicio: int) -> str:
    """
    Prompt para gerar checklist normativo por tipos de SEQOP.
    
    Args:
        total_requisitos: Total de requisitos normativos disponíveis
        categorias: Lista de tuplas (nome, descricao) dos tipos de SEQOP
        id_inicio: Número inicial para os IDs de categoria
    
    Returns:
        String do prompt (deve ser concatenada com os requisitos)
    """
    cats_str = "\n".join(f"  - **{nome}**: {desc}" for nome, desc in categorias)
    return dedent(f"""\
    Você é um especialista em perfuração MPD na Petrobras, revisando SEQOPs.

    Abaixo estão {total_requisitos} requisitos extraídos de documentos normativos MPD Petrobras.

    TAREFA: Gere um checklist de revisão para os seguintes TIPOS DE SEQOP:

{cats_str}

    CONTEXTO: Estes tipos correspondem a etapas do fluxo operacional MPD.
    Os itens devem refletir o que um REVISOR CSD-MPD precisa verificar na SEQOP
    daquele tipo específico de operação.

    Para CADA tipo de SEQOP, gere de 5 a 12 itens de verificação.

    REGRAS:
    - Cada item deve ser uma VERIFICAÇÃO CONCRETA que o revisor pode marcar SIM/NÃO
    - Use linguagem imperativa: "Verificar se...", "Confirmar que...", "A SEQOP inclui..."
    - INCLUA limites numéricos específicos (pressões em psi, volumes em bbl, percentuais)
    - Preserve referências normativas (PE-2POC-XXXXX §X.Y)
    - Criticidade: CRITICA (segurança/mandatory), IMPORTANTE (norma), RECOMENDADA (boa prática)
    - NÃO invente requisitos — baseie-se APENAS nos dados normativos fornecidos
    - Foque no que deve CONSTAR NA SEQOP, não em procedimentos operacionais genéricos
    - Para cada item, inclua APLICABILIDADE: em que contexto/fase esse item se aplica

    Responda em JSON:
    {{
      "categorias": [
        {{
          "id": "CAT-{id_inicio:02d}",
          "nome": "Nome do tipo de SEQOP",
          "descricao": "Descrição do escopo",
          "posicao_fluxo": N,
          "prioridade": "ALTA/MEDIA/BAIXA",
          "itens": [
            {{
              "id": "CAT-{id_inicio:02d}-001",
              "descricao": "Verificar se... (verificação concreta)",
              "detalhes": "Detalhes, limites numéricos e condições",
              "referencia_normativa": "PE-XXXX §X.Y",
              "criticidade": "CRITICA/IMPORTANTE/RECOMENDADA",
              "aplicabilidade": "Fase/contexto de aplicação"
            }}
          ]
        }}
      ]
    }}

    REQUISITOS NORMATIVOS EXTRAÍDOS:
    """)


# =============================================================================
# PROMPT 6 — gerar_checklist_combinado.py → Passo A: Mapeamento
# =============================================================================
# Usado em: gerar_checklist_combinado.py
# Quando: Mapeamento de comentários reais → itens do checklist normativo
# Entrada: Checklist normativo + comentários dos revisores
# =============================================================================

P6_SYSTEM_MAPEAMENTO = (
    "Você é um especialista em perfuração MPD da Petrobras que revisa SEQOPs. "
    "Analise com precisão. Responda em JSON válido, em português brasileiro."
)

def p6_user_mapeamento(total_itens_norm: int, total_categorias: int,
                        total_comentarios: int, texto_normativo: str,
                        texto_comentarios: str) -> str:
    """
    Prompt para mapear comentários de revisores aos itens do checklist normativo.
    Identifica evidências e lacunas.
    """
    return dedent(f"""\
    Você é um especialista em perfuração MPD na Petrobras.

    Abaixo está um CHECKLIST NORMATIVO com {total_itens_norm} itens de verificação
    organizados em {total_categorias} categorias (tipos de SEQOP no fluxo operacional MPD),
    seguido de {total_comentarios} COMENTÁRIOS REAIS de revisores CSD-MPD.

    TAREFA: Para cada comentário, identifique:
    1. Qual(is) item(ns) normativo(s) o comentário se relaciona (pelo ID, ex: CAT-01-003)
    2. Se o comentário traz um ponto que NÃO está no checklist normativo (LACUNA)
    3. Em qual etapa do fluxo operacional o comentário se encaixa

    CHECKLIST NORMATIVO:
    {texto_normativo}

    COMENTÁRIOS DOS REVISORES:
    {texto_comentarios}

    Responda em JSON:
    {{
      "mapeamentos": [
        {{
          "comentario_id": "C1",
          "itens_relacionados": ["CAT-01-003", "CAT-05-002"],
          "resumo": "Resumo do ponto cobrado pelo revisor",
          "etapa_fluxo": "Nome da etapa no fluxo operacional",
          "eh_lacuna": false,
          "lacuna_descricao": ""
        }}
      ],
      "lacunas": [
        {{
          "descricao": "Item cobrado nos comentários mas ausente no checklist normativo",
          "comentarios_relacionados": ["C3", "C7"],
          "etapa_fluxo": "Nome da etapa no fluxo operacional",
          "categoria_sugerida": "CAT-01",
          "criticidade_sugerida": "IMPORTANTE",
          "frequencia": 2
        }}
      ],
      "estatisticas": {{
        "itens_com_evidencia": 15,
        "itens_sem_evidencia": 53,
        "total_lacunas": 3,
        "comentarios_mapeados": {total_comentarios},
        "comentarios_sem_match": 0
      }}
    }}
    """)


# =============================================================================
# PROMPT 7 — gerar_checklist_combinado.py → Passo B: Enriquecimento
# =============================================================================
# Usado em: gerar_checklist_combinado.py
# Quando: Enriquecer checklist normativo com evidências dos comentários e lições
# Entrada: Categorias do checklist + mapeamento + lições aprendidas
# =============================================================================

P7_SYSTEM_ENRIQUECER = (
    "Você é um especialista em perfuração MPD da Petrobras que revisa SEQOPs. "
    "Gere o checklist enriquecido em JSON válido, em português brasileiro. "
    "REGRA CRÍTICA: MANTENHA ABSOLUTAMENTE TODOS os itens normativos SEM EXCEÇÃO – "
    "não condense, mescle ou omita nenhum. "
    "ADICIONE os itens de lacuna (COMENTARIOS) e os novos de lições (LICOES). "
    "O número de itens na saída deve ser MAIOR OU IGUAL ao da entrada."
)

def p7_user_enriquecer(cats_texto: str, lacunas_texto: str,
                        total_categorias: int, contagem_minima: str) -> str:
    """
    Prompt para enriquecer o checklist normativo com evidências e lições.
    
    Args:
        cats_texto: Texto das categorias com evidências mapeadas
        lacunas_texto: Texto das lacunas identificadas
        total_categorias: Número de categorias sendo enriquecidas
        contagem_minima: Texto com a contagem mínima por categoria
    """
    return dedent(f"""\
    Você é um especialista em perfuração MPD na Petrobras.

    Abaixo estão categorias de um checklist normativo (organizadas pelo fluxo operacional MPD) com:
    - EVIDÊNCIAS DE COMENTÁRIOS REAIS de revisores CSD-MPD mapeadas a cada item
    - LIÇÕES APRENDIDAS do sistema Lessons Petrobras

    TAREFA: Gere a versão ENRIQUECIDA dessas categorias:
    1. MANTENHA todos os itens normativos existentes, ENRIQUECENDO com:
       - "evidencia_comentarios": resumo da evidência real
       - "frequencia_real": quantas vezes apareceu nos comentários
       - "score_combinado": ALTO/MEDIO/BAIXO
       - "origem": "NORMATIVO"
       - "licoes_aprendidas": resumo das lições relevantes ao item

    2. ADICIONE itens novos das lacunas e lições aprendidas:
       - "origem": "COMENTARIOS" para itens de revisores
       - "origem": "LICOES" para itens exclusivos das lições aprendidas
       - Coloque-os na categoria mais adequada pelo fluxo operacional

    CATEGORIAS PARA ENRIQUECER:
    {cats_texto}
    {lacunas_texto}

    Responda em JSON:
    {{
      "categorias": [
        {{
          "id": "CAT-XX",
          "nome": "Nome (correspondendo à etapa do fluxo MPD)",
          "descricao": "...",
          "posicao_fluxo": N,
          "prioridade": "ALTA/MEDIA/BAIXA",
          "itens": [
            {{
              "id": "CAT-XX-001",
              "descricao": "Verificar se...",
              "detalhes": "...",
              "referencia_normativa": "PE-XXXX §X.Y",
              "criticidade": "CRITICA/IMPORTANTE/RECOMENDADA",
              "aplicabilidade": "Fase/contexto",
              "evidencia_comentarios": "Resumo da evidência real ou 'Sem evidência direta'",
              "licoes_aprendidas": "Resumo das lições relevantes ou ''",
              "frequencia_real": 0,
              "score_combinado": "ALTO/MEDIO/BAIXO",
              "origem": "NORMATIVO|COMENTARIOS|LICOES"
            }}
          ]
        }}
      ]
    }}

    REGRAS OBRIGATÓRIAS:
    - Retorne EXATAMENTE {total_categorias} categorias
    - NÃO remova, mescle, ou omita NENHUMA categoria
    - NÃO remova, mescle, condense, ou omita NENHUM item normativo existente
    - Mantenha IDs originais dos itens normativos
    - OBRIGATÓRIO: Cada lacuna DEVE ser adicionada como item novo com origem "COMENTARIOS"
    - Score ALTO = normativo CRITICA + freq > 0 OU tem lições/alertas
    - Score MEDIO = normativo IMPORTANTE ou freq > 0
    - Score BAIXO = RECOMENDADA + sem freq + sem lições
    - Preserve referências normativas e detalhes técnicos

    CONTAGEM MÍNIMA DE ITENS POR CATEGORIA:
    {contagem_minima}
    """)


# =============================================================================
# REFERÊNCIA RÁPIDA
# =============================================================================
#
# ID  | Script                      | Função/Etapa              | Finalidade
# ----|-----------------------------|---------------------------|------------------
# P1  | classificar_seqops.py       | refinar_classificacao_ia  | Classificar comentários por tipo
# P2  | gerar_checklist.py          | fase_analise (etapa 1)    | Identificar categorias/padrões
# P3  | gerar_checklist.py          | fase_analise (etapa 2)    | Gerar checklist de comentários
# P4  | gerar_checklist_normas.py   | fase2 (extração)          | Extrair requisitos normativos
# P5  | gerar_checklist_normas.py   | fase3 (checklist)         | Gerar checklist normativo
# P6  | gerar_checklist_combinado.py| passo A (mapeamento)      | Mapear comentários → normas
# P7  | gerar_checklist_combinado.py| passo B (enriquecimento)  | Enriquecer com evidências
#
