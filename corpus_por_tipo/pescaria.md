# Pescaria / Recuperação

6 SEQOPs | 10 comentários MPD

## Análise IA dos Comentários

```json
{
  "sub_tipos": [
    "Pescaria de esfera de desativação",
    "Reconexão de DC para pescaria do BHA",
    "Pescaria com canguru/sub cesta",
    "Recuperação da WB da BAP com WBRT",
    "Recuperação do packer de abandono inferior",
    "Teste do BOP e recuperação do packer Archer superior"
  ],
  "pontos_verificacao": [
    {
      "item": "Aplicação de Surface Back Pressure (SBP) como medida preventiva",
      "frequencia": "alta",
      "exemplo_real": "Entendo que a proposta de instalar o Bearing Assembly para aplicar Surface Back Pressure somente após um teste estático falho ou em caso de influxo durante a manobra contraria a premissa de utilizar o MPD como ferramenta de prevenção."
    },
    {
      "item": "Critérios de estanqueidade em testes de pressão",
      "frequencia": "alta",
      "exemplo_real": "O critério primário é estanqueidade (máximo de 10 psi em 5 min)."
    },
    {
      "item": "Monitoramento de volume bombeado e retorno de gás",
      "frequencia": "alta",
      "exemplo_real": "Sugestão de monitorar o volume bombeado e monitorar o retorno de gás."
    },
    {
      "item": "Abastecimento contínuo da coluna durante descida",
      "frequencia": "alta",
      "exemplo_real": "Lembrar de abastecer a coluna periodicamente durante a descida devido NRVs."
    },
    {
      "item": "Manutenção de vazão mínima no anular para evitar migração de gás",
      "frequencia": "média",
      "exemplo_real": "Manter a vazão mínima pelo anular para evitar a migração de gás pelo anular."
    },
    {
      "item": "Teste de Hold Point com aprovação do CSD MPD",
      "frequencia": "alta",
      "exemplo_real": "Teste da NRV é Hold Point com aprovação do CSD MPD."
    },
    {
      "item": "Atenção ao alinhamento de linhas de circulação",
      "frequencia": "média",
      "exemplo_real": "Sugiro utilizar apenas linhas submarinas (kill ou choke), evitando a necessidade de mudanças de alinhamento."
    },
    {
      "item": "Critérios de teste de baixa pressão entre BA e DSIT",
      "frequencia": "alta",
      "exemplo_real": "Critério: Queda inferior a 10 psi no teste de baixa em 5 min."
    }
  ],
  "erros_frequentes": [
    "Falta de ativação do MPD como medida preventiva",
    "Omissão de critérios claros para fechamento do poço em caso de influxo",
    "Ausência de monitoramento adequado de volumes e retornos",
    "Não abastecimento contínuo da coluna durante descida",
    "Falta de alinhamento adequado das linhas de circulação",
    "Testes de pressão realizados fora dos critérios estabelecidos"
  ],
  "padroes_aprovacao": [
    "Utilização do MPD como ferramenta preventiva, com SBP aplicado previamente",
    "Monitoramento contínuo e detalhado de volumes bombeados e retornos de gás",
    "Realização de testes de pressão com critérios claros e documentados",
    "Abastecimento contínuo da coluna durante operações críticas",
    "Manutenção de vazão mínima no anular para evitar migração de gás",
    "Simplificação de alinhamentos de linhas de circulação para maior eficiência"
  ],
  "normas_aplicaveis": [
    "PE-2POC-01113"
  ]
}
```

## Comentários MPD Completos

### 7-BR-86DB-RJS — Pescaria da esfera de desativação do alargador
**Geronimo de Freitas Rolandi** | v2

Entendo que a proposta de instalar o Bearing Assembly para aplicar Surface Back Pressure somente após um teste estático falho ou em caso de influxo durante a manobra contraria a premissa de utilizar o MPD como ferramenta de prevenção, e não como recurso de controle de poço.
A sequência apresentada não explicita que, caso ocorra influxo durante a manobra sem SBP, será realizado o fechamento do poço, conforme exigido pelo padrão PE-2POC-01113.
Além disso, nossos padrões não estabelecem um limite inferior para kick que deflagre controle de poço, o que aumenta a importância de medidas preventivas.
Diante da incerteza na pressão de poros da formação, para reduzir o risco de influxo durante a manobra, considero que o MPD deveria ser ativado previamente, com SBP aplicada à priori, garantindo que a pressão de fundo permaneça dentro da janela operacional segura.

### 7-BR-86DB-RJS — Reconexão de DC para pescaria do restante do BHA
**Leonardo Mesquita Caetano** | v2

Caros, 
no passo 9, se o teste for feito por pressurização a câmara, o critério primário é estanqueidade (máximo de 10 psi em 5 min).

Sugestão de fazer o teste dinâmico, colocando 400 gpm na booster e controlando 300 psi com choke MPD (o poço já experimentou 300 psi sem perdas)

### 7-BR-86DB-RJS — Reconexão de DC para pescaria do restante do BHA
**Leonardo Mesquita Caetano** | v1

De acordo.

Não tivemos nenhum ganho, nem evento de swab, mas sendo conservador: sugestão de monitorar o volume bombeado e monitorar o retorno de gás. 

No caso de aumento de gás significativo nas peneiras , fechar DSIT e alinhar para o MGS.

### 7-BUZ-90D-RJS — Pescaria com canguru, sub cesta.
**Gustavo Costa Magalhaes Pena há um ano** | v2

Prezados, seguem comentários e sugestões:

Itens 1 a 4: Durante a montagem e descida do BHA de pescaria, prosseguir com monitoramento do poço via circuito de superfície alinhado pela linha de kill com EMW 9,45 ppg na sapata.

Item 5: Entrar com UC para monitoramento do poço, isolar BFM do Choke Manifold. Interromper circulação de superfície.

Itens 11 e 12: Lembrar de abastecer a coluna periodicamente durante a descida devido NRVs. Abastecer sem conectar TD e monitorando o volume bombeado (strokes). Velocidade restrita devido BA instalado de 2 min/sç.

Itens 13 até 23: Manter sistema MPD em modo AP 9,45 ppg nas circulações pela coluna para que o MH possa compensar a fricção no anular e evitar sobrepressurizar o poço.

> ↳ **Rafael Czepak Amabile há um ano:** De acordo.

### 7-BUZ-94D-RJS — Recuperação da WB da BAP com WBRT
**Ivani Tavares de Oliveira** | v2

Em CONSIDERAÇÕES ADICIONAIS:
Bullet #5: Teste da NRV é Hold Point com aprovação do CSD MPD.

Em MONTAGEM E DESCIDA DA WBRT - Bullet #3:
Sugestão: Deixar visível no painel do BOP o valor de referência para visualmente, qualquer um, possa perceber rapidamente uma alteração significativa.

De acordo com os comentário do CSD BUZ nos passos #3 e #10. No passo #3 analisar a possibilidade de efetuar os testes separadamente. 

passo #9) Teste Hold Point - CSD MPD.
Bullet #4: Teste feito contra DSIT. Caso não se enquadre no critério de queda de 10 psi/5min, avaliar o Trip tank por 15 min. Critério: Variação inferior a 1bph ou ganho máximo de 0,25 bbl. (DSIT não garante vedação de cima para baixo).

passo #11) Atenção: Circular o TT para monitoramento do selo do BA.
Remover Bullet #1.
Bullet #3 passa a ser bullet #1. segunda frase remover porque essa situação é com BOP aberto, manter abastecimento contínuo com bomba do trip tank (AGMAR).
Bullet #2: Enquanto o BOP estiver fechado, para evitar pressão diferencial...

passo #12) Não precisa entrar com booster porque estamos em FMCD com nível abaixo da mesa. Não há retorno com BOP aberto e não devemos encher o riser.
DEVEMOS manter bombeio contínuo de SAC pela kill...

passo #13) Destacar: ATENÇÃO Confirmar a pressão no BOP está se mantendo em valores próximos a pressão quando poço abastecido pelo anular. 
Dobrar a atenção no monitoramento de pressão no BOP enquanto o abastecimento estiver somente pela coluna.

### 7-BUZ-94D-RJS — Recuperação da WB da BAP com WBRT
**Geronimo de Freitas Rolandi** | v1

Prezados, boa noite,

Considerar simplificar o abastecimento do poço, no item 6 esta pela linha de choke, no 12 linha de kill, 16 na booster. Para facilitar o programa sugiro utilizar apenas linhas submarinas (kill ou choke), evitando a necessidade de mudanças de alinhamento para fechamentos/aberturas de BOP, não utilizar booster.
Item 11. Não é garantido que seja possível obter vedação de cima para baixo com o  BA instalado, caso apresente vazamento, tentar usar fluido viscoso no Trip Tank. Caso não vede, manter abastecimento continuo com bomba do trip tank (AGMAR).
Conforme lembrou o Trajano, para evitar pressão diferencial de cima para baixo após o assentamento da WBRT, lembrar também de desligar o abastecimento acima do BA (Trip tank).

### 7-BUZ-95-RJS — Recuperação do packer de abandono inferior
**Gustavo Costa Magalhaes Pena** | v3

Pessoal, um comentário sobre a vazão de controle em caso de conversão para cenário FMCD/PMCD dinâmico:

No padrão de Perfuração FMCD:
"Manter a vazão mínima pelo anular para evitar a migração de gás pelo anular. É importante garantir a vazão de controle da simulação, com fator de segurança de 2, considerando as condições do poço com coluna."

A simulação para o BUZ-95 (FCBA 8,7 ppg e sem coluna):
"Também foi feito o mesmo procedimento para a vazão de 3 bpm onde a vazão foi reduzida após o bullheading e para a vazão de 1 bpm não foi possível obter o controle, já para a vazão de 1,5 bpm o bullheading foi mantido."

Sendo assim, entendo que a vazão de controle deve ser ajustada para 3 bpm.

> ↳ **Gustavo Costa Magalhaes Pena:** Vi também que não estão previstas float valves no BHA. Neste caso o MPD deixa de ser uma contingência para essa corrida.

### 7-BUZ-95-RJS — Recuperação do packer de abandono inferior
**Leonardo Mesquita Caetano** | v2

Caros, bom dia

Em "30.3 [CONTINGÊNCIA] Caso ainda assim, não seja possível manter nível na mesa, descer BART+BA e instalar o BA na junta integrada de MPD para entrar em modo PMCD/FMCD. "

Caso instalado o BA: deve ser realizado o Hold Point com DSIT fechado.

### 7-BUZ-95-RJS — Teste do BOP e recuperação packer Archer superior
**Fábio Koiti Dairiki** | v4

Bom dia,

Considerando que o fluido FCBA 9,2 ppg a ser utilizado na intervenção já é OB, sugiro simplificar os testes 6,7 e 8 para cenário de FMCD simplificado (sem teste de riser e teste apenas de BA contra o DSIT), como abaixo:

Cenário #4 (FMCD simplificado)

Modalidade: Teste estático.
Alinhamento: Linha de 2" ou ported sub para câmara entre DSIT/PA e BA ou câmara ACD.
Pressão de teste: Puc = 300 psi por 5/5 min.
Critério: Queda inferior a 10 psi no teste de baixa em 5 min.

> ↳ **Fábio Koiti Dairiki:** De acordo com a versão proposta.
Reconsiderando os diferentes cenários que podem derivar da contingência do EDTA e possíveis perdas induzidas, é recomendável testar o MPD com 300 / 1900 psi novamente (perfuração)

### 7-BUZ-95-RJS — Teste do BOP e recuperação packer Archer superior
**Leonardo Mesquita Caetano** | v3

Caros, 
Qual a motivação de instalar o BA e testar?

O projeto é FMCD contingente, cenário que instalaria o BA e faria o teste de baixa entre o BA e o DSIT.

Não há recomendação Petrobras desse teste para esta operação. (os testes recomendados são os de superfície, em paralelo)

Caso se opte por ele, o número de testes pode ser reduzido para o teste 3 e 4. Com o tempo apontado conforme requerente dele. 

Não se esqueça de tirar o BA antes do packer.

> ↳ **Rafael de Magalhaes Dourado:** A Seadrill não está segura em seguir com a operação de recuperação do packer inferior sem a junta instalada e testada. Em um cenário de perdas elevadas, teríamos que retirar o packer até acima do BOP, fechar as cegas e seguir alimentando o poço com vazão de controle enquanto fazemos a instalação do BA e testamos a junta MPD. Temos autonomia para aproximadamente 5 dias de operação. Em caso de falha no teste da junta, cairíamos no risco de ter que descer novamente o packer e abandonar o poço.
