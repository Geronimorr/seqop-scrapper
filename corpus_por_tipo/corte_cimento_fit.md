# Corte de Cimento / FIT / DLOT / DFIT

10 SEQOPs | 14 comentários MPD

## Análise IA dos Comentários

```json
{
  "sub_tipos": [
    "Corte de cimento",
    "FIT (Formation Integrity Test)",
    "DLOT (Dynamic Leak-Off Test)",
    "DFIT (Diagnostic Fracture Injection Test)",
    "Perfuração associada a corte de cimento",
    "Conversão para PMCD (Pressurized Mud Cap Drilling)",
    "Conversão para FMCD (Floating Mud Cap Drilling)",
    "Teste de injetividade",
    "Troca de fluido",
    "Teste MPD"
  ],
  "pontos_verificacao": [
    {
      "item": "Alinhamento correto do sistema MPD e bombas",
      "frequencia": "alta",
      "exemplo_real": "Confirmar alinhamento das bombas em barramentos diferentes tanto na coluna como na booster."
    },
    {
      "item": "Manutenção de overbalance necessário durante corte de cimento",
      "frequencia": "alta",
      "exemplo_real": "Os últimos 30 m devem ser cortados mantendo com overbalance necessário (com coriolis by-passado, não o choke)."
    },
    {
      "item": "Replicação das condições do simulado durante o DFIT",
      "frequencia": "alta",
      "exemplo_real": "Replicar as condições utilizadas no simulado de DFIT durante o fingerprint."
    },
    {
      "item": "Registro detalhado de parâmetros operacionais durante os testes",
      "frequencia": "alta",
      "exemplo_real": "Após estabilização de cada passo, registrar a pressão de fundo calculada pelo modelo hidráulico e medida pelo PWD, pressão do BOP, contrapressão, pressão no stand pipe, acumulado no trip tank virtual e volume do tanque ativo."
    },
    {
      "item": "Verificação da eficiência de bombas e alinhamento do coriolis",
      "frequencia": "média",
      "exemplo_real": "Avaliar possibilidade de prolongar o condicionamento do fluido a ponto alinhar o retorno para o coriolis e permitir fazer a despressurização do poço de forma mais controlada."
    },
    {
      "item": "Definição de estratégias para mitigação de perdas",
      "frequencia": "média",
      "exemplo_real": "A depender das perdas avaliar redução do AP com CSD-MPD até 50-25 psi de overbalance."
    },
    {
      "item": "Configuração e uso adequado de PRVs durante as operações",
      "frequencia": "média",
      "exemplo_real": "Manter PRV3 alinhada e substituindo PRV2, sempre que possível."
    },
    {
      "item": "Conformidade com os passos e escalonamentos definidos para testes",
      "frequencia": "alta",
      "exemplo_real": "DFIT é realizado com passos de 50 psi. Favor corrigir na sequência de fingerprint."
    }
  ],
  "erros_frequentes": [
    "Falta de alinhamento correto do sistema MPD e bombas",
    "Ausência de registro detalhado de parâmetros operacionais",
    "Não replicar condições do simulado durante o DFIT",
    "Uso inadequado de PRVs ou ausência de menção às recomendações operacionais",
    "Falta de detalhamento na transição entre testes MPD e outros testes",
    "Configuração incorreta de AP (annular pressure) durante corte de cimento ou perfuração",
    "Omissão de estratégias para mitigação de perdas"
  ],
  "padroes_aprovacao": [
    "Registro detalhado e completo de parâmetros operacionais durante os testes",
    "Alinhamento correto do sistema MPD e bombas em barramentos diferentes",
    "Replicação das condições do simulado durante o DFIT",
    "Definição clara de estratégias para mitigação de perdas",
    "Conformidade com os passos e escalonamentos definidos para testes",
    "Uso de boas práticas para equalização e drenagem de sistemas"
  ],
  "normas_aplicaveis": [
    "PE-2POC-01113",
    "PE-2POC-01232"
  ]
}
```

## Comentários MPD Completos

### 3-SPS-111D — 30 Corte do cimento e FIT na sapata 10,75 pol
**Ivani Tavares de Oliveira há um ano** | v1

item 47. a) alinhar sistema MPD.
                   Vazão na booster = 300 gpm
                    AP = 12,1ppg.

### 3-SPS-113 — Corte de Cimento, Perfuracao 5 m e FIT
**Leonardo Mesquita Caetano** | v2

Caros, 

Qual a pressão de poros?

Os últimos 30 m devem ser cortados mantendo com overbalance necessário (com coriolis by-passado, não o choke). Revisar item 3.

No DFIT pode-se colocar um comentário para confirmação de eficiência de bomba e no final, depois de holdpoint aprovado, retomar com vazão na booster.

### 3-SPS-113 — Corte de Cimento, Perfuracao 5 m e FIT
**Ramon Moreira Fernandes** | v1

Passo 12: Avaliar possibilidade de prolongar o condicionamento do fluido a ponto alinhar o retorno para o coriolis e permitir fazer a despressurização do poço de forma mais controlada, avaliando flowin x flowout (flowcheck dinâmico).

### 4-RJS-764 — 11 - Corte de cimento e DFIT
**Gustavo Costa Magalhaes Pena** | v1

Seguem comentários e sugestões:

Em observações MPD, item 2: Mencionar que o fluido do poço é FPBNA 7,8 ppg.


Em DFIT 9,4 ppg:

Item 25: Replicar as condições utilizadas no simulado de DFIT durante o fingerprint.
Item 33: DFIT é realizado com passos de 50 psi. Favor corrigir na sequencia de fingerprint, na etapa do simulado DFIT.

> ↳ **Diogo Rafael Matos Procopio:** Gustavo, grato pelos comentários.

Conforme alinhado pelo Teams, será mantida a estratégia de 25 psi por passo. Será adicionado um comentário com o arrazoado dessa escolha. Demais sugestões serão contempladas na v2.

### 4-RJS-764 — 19 - corte de cimento e DFIT
**Gustavo Costa Magalhaes Pena** | v2

Prezados, seguem comentários.

Em toda a SeqOp: Recomendo que o AP seja travado na broca e não na sapata do 14" a 3783 m. Somente após identificar o reservatório é que o AP ficará travado no topo dele.

Em condicionamento do poço, item 11: Recomendo que a broca seja mantida próxima do fundo durante a passagem do tampão viscoso, para limpar o rat role. Somente após confirmar base do tampão viscoso acima da sapata executar a retirada da broca acima da sapata.

### 4-RJS-764 — 19 - corte de cimento e DFIT
**Ivani Tavares de Oliveira** | v1

Em CORTE DE CIMENTO E PERFURAÇÃO PARA DFIT:
Item 4 - Confirmar alinhamento das bombas em barramentos diferentes tanto na coluna como na booster. Segue sugestão:
MP#1: Barramento A - Coluna 
MP#2: Barramento A - Backup 
MP#3: Barramento B - Coluna 
MP#4: Barramento B - Booster
Em DFIT:
Item 27: a vazão de circulação pela coluna tem que ser a mesma utilizada no fingerprint (conforme descrito no item 21 - a), que foi 860 gpm.
itens 28 e 31 - ECD target de 9,45 lb/gal na broca.
Item 29 - a) Após estabilização de cada passo, registrar a pressão de fundo calculada pelo modelo hidráulico e medida pelo PWD, pressão do BOP, contrapressão, pressão no stand pipe, acumulado no trip tank virtual e volume do tanque ativo. Utilizar tabela do Anexo A - padrão PE-2POC-01232.

### 4-SPS-112 — Corte de Cimento, Perfuração de 5 m e FIT
**Leonardo Mesquita Caetano há um ano** | v1

Nesta SeqOP o sistema MPD não é barreira: ajustar CSB 1.

### 7-BUZ-100D-RJS — Teste do MPD, corte cimento e substituição do fluido
**Gustavo Costa Magalhaes Pena** | v2

Seguem comentários:

Sobre as PRVs #2 e #4: Apesar de não ter sido gerada GM/FAM, entendo ser importante que as recomendações operacionais da MOC, elaborada pela Seadrill e aprovada pela Petrobras, sejam mencionadas na SeqOp: 
Manter PRV3 alinhada e substituindo PRV2, sempre que possível. Desta forma teremos 02 PRVs alinhadas durantes as operações de perfuração e manobra.
Quando a UC for alinhada para acessar o BFM, garantir que exista PRV alinhada e ajustada para proteção do sistema de superfície. Cuidado especial com o set da pop-off da UC.

No item 20, durante a homogeneização do fluido (manter booster com alta vazão para limpeza do riser), o sistema MPD (JC, by-pass coriolis e Choke MPD) poderá ser alinhado para antecipar etapas do Fingerprint. No entanto, o coriolis somente será alinhado após confirmação de que não há excesso de cimento retornando nas peneiras (geralmente obtido com 1,5 BU).

### 7-BUZ-100D-RJS — Teste do MPD, corte cimento e substituição do fluido
**Ramon Moreira Fernandes** | v1

Passo 7: Esse alinhamento para equalização e drenagem do BM não costuma ser praticado e pode desgastar as PRVs. Segue alternativa:
UC->C&K Manifold->linha de Kill via acesso lateral do C&K Manifold
Bomba de lama->C&K Manifold->BM deixando alinhamento para choke hidráulico, lado choke, mantendo-o fechado, e alinhar à jusante do choke hidráulico para o stripping tank.
Como a PRV4 está inoperante, deixar PRV5 comunicada através da abertura da BFM-V8
Caso não siga com essa alternativa especificar por qual PRV será a drenagem do BM. Entendo que será através da PRV5.

Passos 9 e 10: Todos os testes são Holdpoints, conceito novo que ainda está sendo formalizado.

Passo 12: Max Surface Pressure setada em 80% da PRV, ou seja 1360 psi.

### 7-BUZ-90D-RJS — FIT e perfuração da fase III 16 pol
**Gustavo Costa Magalhaes Pena há um ano** | v2

Comentário sobre uso de PS.

Não recomendamos o uso da PS, porém foi negociado entre CGEP e Seadrill a sua utilização nesta fase.
Atentar que ID da PS é 17,75" e que no BHA temos a broca de 16" e a BP 16,6".

Item 24: Verificar se será necessário retirar a PS nesta etapa ou se a mesma ficará instalada até o momento da instalação do BA na fase 12 1/4" x 13 1/2".

> ↳ **Romulo Luiz Pereira Ribeiro há um ano:** Incorporado na v3

### 7-BUZ-95-RJS — Corte de cimento, e perfuração 8,5 pol em MPD
**Ramon Moreira Fernandes** | v1

Passo 4 / MPD / 2º bullet: Eliminar esse item pois o ECD com choke todo aberto pode ser que fica abaixo da Pp. Substituir esse item por "Iniciar a fase com AP 9,1 ppg".

Passo 4 / MPD / 7º bullet: Substituir esse item por "A depender das perdas avaliar redução do AP com CSD-MPD até 50-25 psi de overbalance". Só seria possível trabalhar com choke todo aberto nas conexões se a Pp for menor que a hidrostática do fluido (não é o caso previsto aqui).

Passo 4 / Parâmetros / 3º bullet: limitar rotação à 150 rpm devido ao envelope operacional do BA.

### 7-BUZ-95-RJS — Corte de cimento, e perfuração 8,5 pol em MPD
**Ramon Moreira Fernandes** | v1

Passo 1: Como a Pp esperada é 8,95 ppg, sugiro usar AP 9,1 ppg no corte do cimento e no início da perfuração. Em caso de perda durante a perfuração avaliamos reduzir o AP. Quando for confirmada a Pp via pré-teste ajustamos o AP também.

Conversão para PMCD / passo d: Antes de iniciar o teste de injetividade, interromper o bombeio pela coluna e booster, registrar pressões na superfície (SBP) e no BOP, manter MPD em modo SBP e com setpoint para 750 psi, iniciar o teste de injetividade inicialmente apenas pela coluna até vazão de perfuração (em passos de 50 gpm) e ao final adicionar vazão pela linha de PMCD. Pode já deixar preenchido o escalonamento de vazão na tabela do teste de injetividade.

Essa seqop está prevendo a conversão para PMCD dinâmico direto (passo e). Eventualmente se a pressão na superfície ficar muito alta (próximo de 700 psi) durante o teste de injetividade é melhor manter LAM no anular e seguir para uma conversão para PMCD "normal" (não dinâmico).

Contingência Manobra para troca de broca:
Passo b e d: Considerar simulação de swab previamente elaborada e usar SBP para compensar efeito swab.

### 7-BUZ-95-RJS — Corte de cimento, e perfuração 8,5 pol em MPD
**Geronimo de Freitas Rolandi** | v1

Conversão para FMCD:
c. Converter para FMCD. Alinhar tanques para bombeio de SAC (AGMAR) pela coluna e anular: • Confirmar BHA acima da zona de perdas. • SAC 8,55 ppg → Bomba mixer como pré-carga (linha de baixa) > bombas #2 e #3 > Standpipe 2 > Main Standpipe > Coluna. • SAC 8,55 ppg → Bomba de pré-carga (linha de alta) > bombas #1 e #4 > Standpipe 1 > Linha de PMCD > BFM > Mangueiras do flowspool > Riser

d. Substituir fluido do riser . Zerar contador ao iniciar. Usar máxima vazão possível

e. Alinhar bomba de pré-carga (linha de alta) > bombas #1 e #4 > Standpipe 1 > Linha de Booster  e substituir fluido do poço

### 8-MRO-36-RJS — Teste MPD, corte cimento, troca de fluido e microfrac
**Fábio Koiti Dairiki** | v2

Segue sugestão para detalhar melhor a transição dos testes MPD contra o DSIT para os testes contra o ACD:

Item 10)
- 4° bullet: inserir bullets:
Para equalizar pressão abaixo do LACD (30opsi abaixo do DSIT fechado): pressurizar câmara entre LACD e UACD com 300 psi, relaxar LACD abaixo vazar para baixo no sentido do DSIT, completar pressão com 300 psi e fechar LACD. Após equalização abrir DSTI para teste #4.
Para o teste #4 de alta, compensar fechamento da ACD conforme o aumento da pressão do riser
