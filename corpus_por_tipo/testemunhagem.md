# Testemunhagem com MPD

6 SEQOPs | 10 comentários MPD

## Análise IA dos Comentários

```json
{
  "sub_tipos": [
    "Testemunhagem 8 1/2\" em MPD",
    "Testemunhagem 12 1/4\" em MPD",
    "Testemunhagem com troca de fluido sem PWD",
    "Testemunhagem com PRC em modo MPD"
  ],
  "pontos_verificacao": [
    {
      "item": "Avaliação do arraste adicional causado pelo BA",
      "frequencia": "alta",
      "exemplo_real": "Garantir que o técnico de testemunhagem esteja ciente do arraste adicional causado pelo BA e que este seja medido antes do início da operação."
    },
    {
      "item": "Isolamento do poço durante testes do packer assy e BA",
      "frequencia": "alta",
      "exemplo_real": "Passos 8 e 10: é necessário isolar o poço aberto durante os testes do packer assy e do BA."
    },
    {
      "item": "Simulação hidráulica para troca de fluido sem PWD",
      "frequencia": "média",
      "exemplo_real": "Passo 21: Sugiro fazer uma simulação hidráulica específica para essa troca de fluido prevendo o aumento gradual da SBP."
    },
    {
      "item": "Teste de estanqueidade do SSA (Hold Point MPD)",
      "frequencia": "alta",
      "exemplo_real": "O critério de aprovação do teste de estanqueidade do SSA será realizado com o BOP fechado e poço sendo monitorado pela UC."
    },
    {
      "item": "Monitoramento do trip tank para identificar vazamentos",
      "frequencia": "alta",
      "exemplo_real": "Item 4: Importante se balizar pelo modelo preditivo de desgaste, pressão de acionamento dos packers da ACD e nível do trip tank para decidir por prosseguir ou trocar o SSA."
    },
    {
      "item": "Registro de pressão de acionamento da SSA",
      "frequencia": "média",
      "exemplo_real": "Item 25: Incluir registro de pressão de acionamento da SSA e efeito no arraste na coluna."
    },
    {
      "item": "Configuração de PRVs conforme padrão PE-2POC-01247",
      "frequencia": "alta",
      "exemplo_real": "O padrão PE-2POC-01247 recomenda: PRVs (3 e 5) Choke Manifold e Standpipe Manifold x Buffer: Pressão de teste 3000 psi."
    },
    {
      "item": "Velocidade de retirada da coluna (m/min)",
      "frequencia": "média",
      "exemplo_real": "Itens 29 e 41: Verificar a velocidade de retirada (m/min) da tabela, trecho 2."
    },
    {
      "item": "Verificação de pressão trapeada entre testemunho e NRV",
      "frequencia": "baixa",
      "exemplo_real": "No item 33, atentar para possível pressão trapeada entre o testemunho e a NRV na quebra do BHA."
    },
    {
      "item": "Compatibilidade de esferas com drift das NRVs",
      "frequencia": "baixa",
      "exemplo_real": "Em caso de necessidade de bombeio de esferas para queimar o testemunho, garantir compatibilidade com o drift das NRVs."
    }
  ],
  "erros_frequentes": [
    "Falta de medição do arraste adicional causado pelo BA",
    "Ausência de simulação hidráulica para troca de fluido sem PWD",
    "Não monitorar o trip tank durante a operação",
    "Configuração incorreta das PRVs em relação ao padrão PE-2POC-01247",
    "Falta de registro de pressão de acionamento da SSA"
  ],
  "padroes_aprovacao": [
    "Realização de testes de estanqueidade do SSA com critérios claros",
    "Monitoramento contínuo do trip tank para identificar vazamentos",
    "Simulação hidráulica para prever aumento gradual de SBP",
    "Configuração de PRVs conforme padrão PE-2POC-01247",
    "Registro detalhado de parâmetros operacionais, como pressão de acionamento da SSA"
  ],
  "normas_aplicaveis": [
    "PE-2POC-01113",
    "PE-2POC-01247"
  ]
}
```

## Comentários MPD Completos

### 3-RJS-762 — 23 - Testemunhagem
**Geronimo de Freitas Rolandi** | v2

Corrigir numeração após o item 10. 

Garantir que o técnico de testemunhagem esteja ciente do arraste adicional causado pelo BA e que este seja medido antes do inicio da operação.
Caso haja vazamento significativo (dificuldade de manter SBP) ou com tendencia de aumento e se descida interromper a testemunhagem, interromper rotação, queimar testemunho, livrar tool joint do AID e fechar AID para troca de BA com contrapressão.

### 3-RJS-762 — 23 - Testemunhagem
**Ramon Moreira Fernandes** | v1

Passos 8 e 10: é necessário isolar o poço aberto durante os testes do packer assy e do BA. Sugiro fechar o BOP anular (deixando poço monitorado pela UC).

Passo 21: Atenção nessa etapa de troca de fluido sem PWD. Sugiro fazer uma simulação hidráulica específica para essa troca de fluido prevendo o aumento gradual da SBP.

Passos 22 a 24: replicar informação de AP 9,3 ppg

Passo 23, 24 e 29: Manter circulação com booster a 400 gpm ou maior.

Passo 43: Avaliar cenário de perda. Se não estiver com perdas pode optar por manter o monitoramento do poço com UC.

### 3-SPS-111D — 32 Testemunhagem 8 1/2" em MPD
**Gustavo Costa Magalhaes Pena há um ano** | v2

Prezados, seguem comentários e sugestões:

Em observações para operação com MPD:

Item 4: É tolerável algum vazamento quando na passagem de TJ pelos SSs. Importante se balizar pelo modelo preditivo de desgaste, pressão de acionamento dos packers da ACD e nível do trip tank para decidir por prosseguir ou trocar o SSA.

Item 6: Para rotações superiores a 150 rpm, consultar CSD MPD. 

Item 7c: Utilizar o alinhamento proposto no item 7b, com 02 na coluna e 02 na booster, de preferência com a configuração utilizada na calibração de eficiência e verificação de MH realizado na primeira corrida da fase (#2 e #3 na coluna e #1 e #4 na booster).

Item 13: Recomendo incluir o fluxograma de controle de poço com MPD.

Em montagem e descida do BHA de testemunhagem:

Item 7: O critério de aprovação do teste de estanqueidade do SSA (Hold point MPD) será realizado o BOP fechado e poço sendo monitorado pela UC, packers da ACD pressurizados, booster a 600 gpm e SBP (AP 12,2 ppg a 6517 m MD), observando o trip tank por 15 min. Após aprovação do teste, partir para item 8d.

A partir do item 15: Com o início da circulação pela coluna, procurar monitorar o BU para auxiliar na identificação de potencial falso kick de ar de abastecimento de coluna. Evitar ter que lidar com evento de falso kick enquanto testemunhando (talvez completar o BU antes de iniciar a testemunhagem).

Item 24: PRC em modo MPD.

Item 25: Nesta etapa, efetuar flow check dinâmico com AP 12,2 ppg a 6517 m MD, e verificar se há necessidade de ajuste de eficiência de bomba para a configuração de testemunhagem.

> ↳ **Bruno da Cruz Schaefer há um ano:** ajustado na V3.

### 3-SPS-111D — 32 Testemunhagem 8 1/2" em MPD
**Leonardo Mesquita Caetano há um ano** | v1

Caros, boa noite.

No item 5, avaliar capacidade da unidade de cimentação de manter poço pressurizado devido as perdas. No item 2) (1) "Monitorar poço pelo sensor do BOP manter unidade de cimentação com vazão igual a vazão de perda observada. OU


Caso necessário, instalar SSA antes e pressurizar Riser deverá ser realizado para verificar (Hold Point MPD). Depois stabelecer alinhamento para transição continua com circuito de superfície transferindo a vazão da linha de PMCD para booster de forma gradual (atenção para os ajustes do parâmetro PID)

Item 7.  Testar vedação da SSA (Hold Point MPD); De forma dinâmica (critério de 0 ganho no TT) ou teste de pressão com SBP de conexão 

Item 15. Avaliar arraste provocado pela SSA, com e sem tool joint (pode dificultar o enquadramento nos +/- 7 klbf do item 21)

Item 25.Incluir registro de pressão de acionamento da SSA e efeito no arraste na coluna, com e sem tool joint na frente, para compensar nos parâmetros da testemunharem, se necessário.

> ↳ **Bruno da Cruz Schaefer há um ano:** ajustado na V2.

### 3-SPS-113 — 27 Testemunhagem 8 1/2" em MPD
**Geronimo de Freitas Rolandi** | v1

passo 32: nesse ponto o TT só monitora o BA para verifica se há vazamento.
passo 40. Seria possível efetuar a circulação de um Bottons Up alinhado para o MGS para remover eventual gas trapeado abaixo das NRV's?

Em caso de necessidade de bombeio de esferas para queimar o testemunho, garantir compatibilidade com o drift das NRV's

### 3-SPS-113 — 27 Testemunhagem 8 1/2" em MPD
**Ivani Tavares de Oliveira** | v1

De acordo com a sequência. Apenas um comentário para ajuste se tiver uma nova versão.
Em PREPARATIVOS E ATIVIDADES PERIÓDICAS, item 8. O padrão PE-2POC-01247 recomenda:
PRVs (3 e 5) Choke Manifold e Standipipe Manifold x Buffer: Pressão de teste 3000 psi, o set de abertura está correto com 2400 psi e o set de fechamento 1900 psi.
SPL = 1400 psi ou FIT - 100 psi, o que for menor.

### 3-SPS-113 — 27a Testemunhagem #2 de 8 1/2" em MPD
**Gustavo Costa Magalhaes Pena** | v2

De acordo.

Item opcional:
Em montagem e descida do BHA, itens 5-6: Nesta etapa é possível registrar o arraste das borrachas do BA no tubo e no tool joint com SBP, e com o BHA ainda dentro do riser (sem interferência de arraste do poço).

### 3-SPS-113 — 27a Testemunhagem #2 de 8 1/2" em MPD
**Ivani Tavares de Oliveira** | v1

Estou de acordo com a sequência, segue alguns pontos de atenção:
Em PREPARATIVOS E ATIVIDADES PERIÓDICAS:
Item 8 - f) Reavaliar o set da SPL, porque de acordo com o padrão PE-2POC-01247, a pressão máxima a ser atingida numa operação é 1520 psi em caso de controle de poço ou plugueamento acidental do choke. Além disso a SPL deve ser configurada para a menor pressão entre 1400 psi e FIT-100 psi.

item 28. Corrigir a frase deste item porque mantendo SBP em 1340 psi, o sistema automático da Halliburton para compensar swab não tem como ser ativado.

itens 29 e 41. Verificar a velocidade de retirada (m/min) da tabela, trecho 2.

### 4-SPS-112 — Testemunhagem 12 1/4" em MPD
**Ramon Moreira Fernandes há um ano** | v1

Passo 10: informar restrição de velocidade de manobra devido ao BA estar instalado.

> ↳ **Issamu Noce Watanabe há um ano:** Adicionado

### 4-SPS-112 — Testemunhagem 12 1/4" em MPD
**Leonardo Mesquita Caetano há um ano** | v1

No item 33, atentar para possível pressão trapeada entre o testemunho e a NRV na quebra do BHA.

> ↳ **Leonardo Mesquita Caetano há um ano:** Caros, aproveitando, o Hold Point do item 6 ou 7 podem ser feitos pelo critério de pressão, fechando o DSIT e pressurizando a câmara pela unidade de cimentação.
