# Descida de BHA e Teste do MPD/BOP

25 SEQOPs | 32 comentários MPD

## Análise IA dos Comentários

```json
{
  "sub_tipos": [
    "Descida de BHA 12 ¼” x 13 ½”",
    "Descida de BHA 8 ½”",
    "Descida de BHA 16”",
    "Teste do sistema MPD",
    "Teste do BOP",
    "Fingerprint offline",
    "Troca de fluido",
    "Montagem de BHA",
    "Sidetrack"
  ],
  "pontos_verificacao": [
    {
      "item": "Testar todas as válvulas nos dois sentidos, sempre que possível",
      "frequencia": "alta",
      "exemplo_real": "Em OPERAÇÕES EM PARALELO (OFFLINE FORAS DAS MESAS ROTATIVAS); item 4, a sonda, em seu procedimento, deve prever testar todas as válvulas nos dois sentidos, sempre que possível."
    },
    {
      "item": "Realizar testes de pressão com critérios claros de aprovação",
      "frequencia": "alta",
      "exemplo_real": "Nos testes de pressão, realizar apenas 3 testes (de alta e baixa)). Realizar os 2 primeiros testes e o terceiro contra: DSIT; MPDV19 e MPD20."
    },
    {
      "item": "Monitorar pressão no standpipe durante testes de UPA e LPA",
      "frequencia": "média",
      "exemplo_real": "Descida do BHA / passo 29: Acrescentar um item para monitorar pressão no standpipe (via ported sub) durante os testes do UPA e LPA."
    },
    {
      "item": "Garantir backup de pressurização do poço durante troca de fluido",
      "frequencia": "alta",
      "exemplo_real": "Durante a troca de fluido, será necessário garantir backup de pressurização do poço, já que a booster não estará disponível."
    },
    {
      "item": "Efetuar testes Hold Point com aprovação do CSD-MPD",
      "frequencia": "alta",
      "exemplo_real": "Toda instalação do BA deve ser testada por metodologia Hold Point com aprovação do CSD-MPD."
    },
    {
      "item": "Evitar sobrepressurização do poço durante testes",
      "frequencia": "alta",
      "exemplo_real": "Para executar o teste do SSA sem sobrepressurizar o poço aberto, considerar o fechamento do BOP (anular ou gaveta) para execução do teste."
    }
  ],
  "erros_frequentes": [
    "Omissão de testes funcionais das válvulas em operações paralelas",
    "Falta de alinhamento adequado para testes de estanqueidade",
    "Erro na configuração de limites de pressão no sistema MPD",
    "Utilização inadequada do sistema de contrapressão MPD para equalização e ventilação",
    "Confusão nos critérios de aprovação de testes de pressão",
    "Falta de clareza nos alinhamentos durante troca de fluido"
  ],
  "padroes_aprovacao": [
    "Testes realizados com critérios claros e monitoramento adequado",
    "Backup de pressurização garantido durante operações críticas",
    "Utilização de metodologia Hold Point com aprovação do CSD-MPD",
    "Alinhamentos bem definidos e documentados para todas as etapas",
    "Evitar impactos no caminho crítico durante operações paralelas"
  ],
  "normas_aplicaveis": [
    "PE-2POC-01113"
  ]
}
```

## Comentários MPD Completos

### 1-RJS-763D — 22 - Descida do BHA 12,25 com teste do MPD
**Leonardo Mesquita Caetano** | v2

Caros, 
de acordo com a sequência.

Em OPERAÇÕES EM PARALELO (OFFLINE FORAS DAS MESAS ROTATIVAS); item 4, a sonda, em seu procedimento, deve prever testar todas as válvulas nos dois sentidos, sempre que possível.

### 1-RJS-763D — 22 - Descida do BHA 12,25 com teste do MPD
**Leonardo Mesquita Caetano** | v1

Caros, segue comentários.

Item 17) ao 27).
Nos testes de pressão, realizar apenas 3 testes (de alta e baixa)). Realizar os 2 primeiros testes e o terceiro contra:
DSIT; MPDV19 e MPD20.

Todas demais válvulas do buffer devem ser feitas nos testes de superfície em paralelo.

> ↳ **Leonardo Mesquita Caetano:** Teste 3, usar válvulas remotas:
DSIT; MPDV19 e MPD20.
DSIT; MPDV01 e MPD02.

### 1-RJS-763D — Descida do BHA 16'' e teste do MPD
**Gustavo Costa Magalhaes Pena** | v1

Seguem comentários:

Em alertas operação MPD, item 9: O CSD MPD deverá ser acionado se for necessário operar com rotação na coluna superior a 150 rpm.

Em montagem e descida do BHA, item 5: Conferir as pressões no anular por ambos os sensores (Copilot e Ontrak).

Em teste do sistema MPD, item 19: Mencionar as válvulas do FS que serão testadas também (por exemplo nos testes #1 e #4 testar as FS internas e nos testes #2 e #3 as FS externas). Senti falta de alinhamento para teste de estanqueidade do DSIT.

Em descida até o fundo, item 28: Pendente estabelecer o AP de manobra.

> ↳ **João Paulo Luz Alves:** Gustavo, bom dia.

Resposta parcial do item 19:
O teste da DSIT é previsto na sequência anterior de reconexão do LMRP.

Item 28:
O AP será definido com base no valor obtido no item 27c.

> ↳ **Gustavo Costa Magalhaes Pena:** Obrigado pelos esclarecimentos.

### 3-RJS-762 — 18 Descida BHA 12,25 x 13,5 pol+ teste MPD_3rjs762
**Gustavo Costa Magalhaes Pena** | v2

Seguem comentários:

Em operações em paralelo, o item 4, com os testes do sistema MPD de superfície, deve ocorrer antes do item 3, com as etapas do fingerprint offline.

No item 20, a pressão de teste do sistema é 300/1900 psi. O teste com 300/2000 psi foi só no primeiro teste (recebimento). 
a e b: São somente 3 alinhamentos.
f: Não temos UACD nesta junta.

### 3-SPS-113 — 31 - Descida BHA 8 1/2", teste RCD/BA, condicionamento poço 
**Ivani Tavares de Oliveira** | v2

Em PARTICULARIDADES DAS OPERAÇÕES EM MPD:
item 3) Acrescentar o texto: Toda instalação do BA deve ser testada por metodologia Hold Point com aprovação do CSD-MPD.
Teste estático / alinhamento pela linha de 2" contra DSIT: Pressão de teste = (SBP + 100 psi) / 5min. Critério de aceitação: Queda inferior a 10 psi no teste de baixa ou 40 psi no teste de alta.
Teste Dinâmico / alinhamento pela booster->riser->sistema MPD: Pressão de teste = (Pressão da Un. Cimentação + 300 psi) / 15min. Critério de aceitção: Variação infeior a 1bph (ou 0,25 bbl) / 15min.

Em Montagem e descida do BHA 8 ½”:
item 11-f) Configurar SPL para 1400 psi.

> ↳ **Denes Marcel Chaves Lopes:** Sugiro não acrescentar os 2 bullets (teste estático e dinâmico) pois nessa Seqop o teste do BA sendo executado não está conforme esses bullets devido ao cenário incomum.

### 3-SPS-113 — 31 - Descida BHA 8 1/2", teste RCD/BA, condicionamento poço 
**Geronimo de Freitas Rolandi** | v2

Item 27. Atenção para não contar os strokes da bomba do circuito de superfície.
ttem 31  e 32. Registar PRC após fingerprint simplificado, já que as baixas vazões do PRC podem levar o choke a trabalhar em uma posição com pouca controlabilidade.

### 3-SPS-113 — Montagem BHA 8,5x9,5 pol e teste MPD
**Ivani Tavares de Oliveira** | v2

Corrigir os subitens do item 10. em DESCIDA DO BHA 8 ½” X 9 ½”, pois inicia com "d" e deveria iniciar em "a".

TESTE SISTEMA MPD, item 21 - a) corrigir "item 18" ao invés de item16.

IMPORTANTE: item 32. a) Válvulas abertas, substituir R1 (que está fechada) por R3 que deverá ficar aberta.

### 3-SPS-113 — Montagem BHA 8,5x9,5 pol e teste MPD
**Gustavo Costa Magalhaes Pena** | v1

Prezados, seguem comentários.

Em operações paralelas, itens 9d e 9e: Num circuito de superfície (pequeno volume) pode ser arriscado efetuar testes funcionais das PRVs com esses níveis de arm/rearm. Minha sugestão é realizar o teste funcional com pressões menores e se possível alinhar as linhas submarinas para aumentar o volume do sistema.

Em descida do BHA, item 9g: É importante que o FP paralelo não cause impactos no caminho crítico. Em caso de indisponibilidade da sonda e/ou MPD, a fiscalização deverá ser notificada.

Em teste do sistema MPD:

Item 19f: Recomendo não utilizar o sistema de contrapressão MPD para essa etapa dos testes do sistema de desvio de fluxo. Para utilizar o Choke Manifold da sonda, atentar para o item 4 das particularidades das operações MPD, na página 4 desta sequência.

Item 20: Antes de iniciar o teste, efetuar flush para confirmar alinhamento. O alinhamento na figura precisa de ajustes.

Itens 21 até 34: Como mencionado anteriormente, utilizar o choke hidráulico da sonda para a drenagens. Replicar a recomendação nos alinhamentos das figuras.

Itens 26 e 28: Abrir B1 e fechar B4 e B5, desta forma irá testar a B5 no sentido poço x superfície.

Item 35: Drenar a pressão do riser pelo choke hidráulico. Atentar para o grande volume a ser drenado.

Item 36: É possível utilizar a linha de by-pass abrindo a B14.

### 4-RJS-764 — Descida de BHA 12 ¼” x 13 ½” e teste do sistema MPD
**Ramon Moreira Fernandes** | v1

Operações em paralelo / passo 2 / b): Calibrar parâmetros de PID em circuito de superfície.

Descida do BHA / passo 29 / f): Monitorar trip tank (estanqueidade do BA) e [...].

Descida do BHA / passo 29: Acrescentar um item para monitorar pressão no standpipe (via ported sub) durante os testes do UPA e LPA (testes #1 e #2): Não deverá ocorrer aumento na pressão do standpipe assegurando estanqueidade do packer assy.

> ↳ **Andre Santos Doria:** Ajustado.

### 4-SPS-112 — Descida BHA 8,5 pol, troca de fluido e Teste MPD
**Gustavo Costa Magalhaes Pena há um ano** | v1

Prezados, seguem comentários e sugestões:

Em operações em paralelo:

Itens 8d e 8e: Evitar realizar o teste de funcionamento das PRVs, em circuito de superfície, com pressões dessa magnitude (alta pressão e pequeno volume). Recomendo realizar o teste funcional com 800 psi de abertura e 300 psi de fechamento.

Item 9: Caso a perfuração em PMCD seja uma contingência, testar as NRVs com 5500 psi. Caso contrário, manter 2500 psi.


Em descida do BHA 8 1/2":

Itens 14d e 17j: TD desconectado.

Item 18: Atentar que acima do BA até o diverter permanecerá com FPBNA 12,4 ppg durante a primeira corrida da fase 8 1/2".

Item 19e: Não utilizar o sistema MPD para ventilação e equalização. O sistema de contrapressão deverá permanecer isolado durante os testes. Para equalização e ventilação utilizar o choke hidráulico do choke manifold (oposto ao lado que estiver sendo utilizado para o teste). Atentar que no NS54 o BFM e a UC compartilham o acesso ao Choke manifold (pendência contratual), e portanto é necessário a conexão de uma mangueira (antecipadamente e sem impacto no caminho crítico) para permitir o alinhamento proposto. Corrigir os itens 20 a 35 considerando essa alteração.

Itens 39a e 40a: Recomendo que não seja realizado o corte desses 25 m de cimento em paralelo à troca de fluido. Minha sugestão é de concluir a troca do fluido com AP 12,4 ppg, e em seguida executar o fingerprint, MPD drill, simulado hang-off, e choke drill (todas essas etapas com a premissa de manter o AP 12,4 ppg no fundo, sem a necessidade de teste negativo). Só então, com todos os preparativos concluídos, partir para o corte de cimento/sapata e execução do DFIT.

> ↳ **Anderson Avelar de Paula:** Bom dia, não está claro como contornar o comentário do CSD sobre o item 19e dada a pendência do recebimento. Aguardamos hoje uma proposta da Valaris para alguma solução com alinhamentos alternativos (toolpusher ficou de avaliar e propor), já que a informação recebida de bordo é que não existe possibilidade de usar bleed do STP  (check valve impede drenagem) e nem instalar a mangueira comentada pelo CSD para segregar o choke da kill no tramo hoje comum. Aparentemente temos um impacto real operacional do recebimento da sonda nessas condições. Não temos solução clara a bordo no momento para propor outros alinhamentos.

> ↳ **Anderson Avelar de Paula:** Após extensa discussão a bordo com equipe Valaris, foi proposta solução similar à sugestão do CSD para contornar a pendência. Alterações incluídas na v2 postada.

### 4-SPS-112 — Montagem BHA 12,25x13,5 pol e Teste MPD
**Gustavo Costa Magalhaes Pena há um ano** | v1

Seguem comentários:

Em operações em paralelo:

- Inserir etapa do Fingerprint offline, conforme sequencia especifica de FP e TP. Geralmente é realizado durante a descida do BHA.

Item 7: Não recomendo realização de testes de acionamento das PRVs em circuito de superfície com altos níveis de pressão. Os testes funcionais das PRVs já estão contemplados na SeqOp de FP e TP.

Em montagem do BHA 12 1/4" x 13 1/2":

Item 4: No BHA os SN das Floats estão iguais. Favor inserir na Seqop os SN das NRVs/Sub que serão instaladas no BHA.

Item 8: Efetuar etapas do fingerprint offline (caso não tenha sido feito até então).

Em descida do BHA 12 1/4" x 13 1/2":

Item 16: Efetuar etapas do fingerprint offline (caso não tenha sido feito até então).

Item 19 e): Entendo a opção de utilizar o sistema de contrapressão para equalização e ventilação das linhas de superfície nos testes. Importante esclarecer que é possível fazer equalizações e ventilação sem a necessidade do Choke MPD, utilizando o choke hidráulico da sonda.

Itens 24, 26, 27 e 29: Testes Hold Point CSD-MPD.

Item 40: Recomendo que não seja realizado o corte do cimento em paralelo à troca de fluido. Pelas minhas contas seriam cortados só 20 m de cimento, com um ganho marginal de tempo. Em contrapartida, o corte do cimento vai exigir a circulação de 1,5 BU para limpeza do poço além de colocar cimento no sistema de contrapressão (no caso do NS54 o choke é de 3", mais sensível a plugeamento). Sugiro que durante e após a troca do fluido sejam realizadas as etapas de FP e TP, com o coriolis alinhado o tempo todo.

> ↳ **Gustavo Costa Magalhaes Pena há um ano:** Ainda sobre o item 19e.

Sugerimos que as equalizações sejam realizadas em estática e by-passando o coriolis.

> ↳ **Diego Vieira Santos há um ano:** Comentários adicionados na V2

### 7-BR-86DB-RJS — Descida do BHA 12 1/4" x 14 3/4", Sidetrack e Perf fase 4 MP
**Geronimo de Freitas Rolandi** | v6

Ajustar, em toda a sequencia,  o AP de 9,7 ppg para 9,75 ppg, conforme GM 2261.00-2025-0023-0

### 7-BR-86DB-RJS — Descida do BHA 12 1/4" x 14 3/4", Sidetrack e Perf fase 4 MP
**Leonardo Mesquita Caetano** | v3

Item 23. Mudar referência do DPPT em "Efetuar DPPT assim que constatar topo do Quissamã, conforme orientações dos itens 24-26."

item 25. Fechar DSIT para menor influência do heave e para circulação do possível HC do DPPT
Item 27. Abrir DSIT

Item 48. Em caso de perda, considerar a manutenção da pressão pelo circuito de superfície com MPD.

### 7-BR-86DB-RJS — Descida do BHA 12 1/4" x 14 3/4", Sidetrack e Perf fase 4 MP
**Gustavo Costa Magalhaes Pena** | v1

Prezados, seguem comentários.

Em dados do poço:
Existe uma incerteza em relação à PP na Fm. Quissamã (pós-sal), e portanto o sistema MPD compõe o CSB primário.

Em observações para operação com MPD:
Item IX: Se necessário rotações acima de 150 rpm, informar CSD MPD.
Item XV: 
Temos simulação para circular influxo pelo sistema MPD nesta fase?
A nota e a figura, que tratam sobre interromper o controle do poço com MPD após contabilizar 20 bbl de influxo no sistema MPD, estão em desacordo com o padrão da Petrobras (item XII da SeqOp). É importante mencionar que a decisão de interromper o controle com o MPD incorre num maior volume de kick (quando o sistema MPD está funcionando dentro da normalidade).
Acredito que a sonda esteja confundido volume total de influxo, necessário para conferir capacidade de circular o influxo pelo MPD, com volume de detecção do influxo. Vale ressaltar que conforme o item XI, o sistema MPD é um sistema auxiliar, e caso a sonda identifique um indicio primário de kick, mesmo que o MPD não tenha identificado, o sondador deverá proceder com o procedimento de fechamento de poço convencional.

Em descida o BHA:
Item 4.L: DSIT já estará aberto. 
Item 4.M: O teste do BA é realizado com a BART destravada e acima do BA (após item o). Especificar que o HP será realizado conforme item III.b de Observações para operação com MPD.
Itens 6 e 7: Não são necessárias. Nada mudou do último FP para esse momento (mesmo fluido e mesmo poço).


Em sidetrack:
Item 17.b: Menciona que o desvio (sem MPD) deve ocorrer até 3460 m, porém o topo da Fm. Quissamã está previsto para 3437 m. Sendo assim, entendo necessário estabelecer um momento para o alinhamento do MPD para evitar entrar no reservatório (pós-sal) sem MPD.
Item 19.b: Atentar para alinhar coriolis somente se peneiras sem excesso de cimento. Caso contrário, poderá alinhar choke, mas manter coriolis by-passado, ou circular para limpeza.

Em DPPT:
Item 21: Circulação para limpeza somente se retorno nas peneiras com excesso de cimento.
Item 23: Opção de DPPT adaptado (somente com a booster) em caso de não identificação de influxo no DPPT convencional (somente com vazão na coluna).

Em troca de monitoramento do poço, item 45.

> ↳ **Gustavo Costa Magalhaes Pena:** Favor ignorar última linha.

### 7-BUZ-95-RJS — Descida do BHA 8,5 pol e teste do MPD
**Gustavo Costa Magalhaes Pena** | v3

De acordo. Somente uma recomendação:

Em teste do sistema MPD, item 15: Drenar pressão pelo choke hidráulico da sonda para stripping tank e trip tank. O volume drenado costuma ser grande e pode topar a UC.

### 7-BUZ-95-RJS — Descida do BHA 8,5 pol e teste do MPD
**Ramon Moreira Fernandes** | v1

Passo 9: Após travamento do BA na RCD e teste de overpull, sugerimos desconectar a mangueira da função de unlatch devido ao evento recente de desconexão espúria do BA ainda em investigação no NS57. Verificar e registrar a pressão setada no "Latch Safety Rating" que corresponde ao intertravamento entre unlatch e pressão trapeada abaixo do BA. Garantir que o intertravamento está habilitado.

Passo 11: Alinhamento para equalização do BM: Bomba da sonda -> StandPipe principal -> Choke Manifold -> Buffer manifold. Se alinhar diretamente do StandPipe para o Buffer não tem como drenar a pressão do buffer devido à check valve na linha de PMCD...

Passo 13:
Teste #2: após aprovação sugiro manter BFM-V3 aberta e BFM-V10 fechada (evitando assim de abrir a BFM-V10 com diferencial).
Teste #3: após aprovação fechar BFM-V3 (e manter BFM-V10 fechada).
Passo 14:
Teste #4: BFM-V6 já deveria estar fechada desde o início (e permanece fechada durante todos os testes). Sugiro abrir BFM-V3 e manter fechada a BFM-V10 (para evitar de abrir com diferencial de pressão).
Teste #3: BFM-V3 já aberta ao término do teste #4 (conforme sugestão).
Teste #2: É Holdpoint MPD tbm
Teste #1: É Holdpoint MPD tbm

> ↳ **Ramon Moreira Fernandes:** Desconsiderar comentário do passo 11. O alinhamento proposto está adequado. Pressuriza pela linha de PMCD (STP manifold -> Buffer Manifold) e despressurização pela linha do choke (Buffer Manifold -> Choke Manifold).

### 7-JUB-78D-ESS — Descida de BHA de perfuração, troca de fluido, fingerprint e
**Gustavo Costa Magalhaes Pena** | v5

Prezados, seguem comentários.

Em observações de segurança de poço, item 12: Utilizar fluxograma atualizado do padrão.

Em troca de fluido, Item 17: 
a) Inserir diagrama para facilitar identificação dos alinhamentos propostos. 
c) Deve-se evitar isolar PRV, se necessário ajustar o setpoint de abertura.
d) Teste de BA contra AID é somente teste de baixa pressão com 300 psi. O AID não suporta grande diferencial de pressão de cima para baixo.

Em fingerprint a poço aberto: Estas etapas já foram realizadas em poço revestido. Nesta etapa, a Halliburton irá confirmar se as configurações ajustadas em poço revestido estão válidas ou se é necessário algum ajuste adicional. Incluir alerta para que o AP seja mantido em 9,6 ppg na sapata, durante todas as etapas.

Em contingência DPPT, 1º bullet: Não é necessário poço limpo para execução do DPPT, somente não pode haver retorno excessivo de cimento para que o coriolis fique alinhado.

### 7-JUB-78D-ESS — Descida de BHA de perfuração, troca de fluido, fingerprint e
**Ivani Tavares de Oliveira** | v4

Em OBSERVAÇÕES DE MPD:
#6) adicionar b) Se necessário substituição do BA, o teste realizado após a instalação deverá atender metodologia Hold Point com aprovação do CSD-MPD.
#14 e #15 se repetem.
#19  adicionar b) Se necessário substituição do BA, o teste realizado após a instalação deverá atender metodologia Hold Point com aprovação do CSD-MPD. 
Observe que #6 e #19 são praticamente a mesma coisa, sugiro deixar apenas um deles.

Em TROCA DE FLUIDO:
#16) Não ficou claro como será feito as operações em paralelo a instalação do BA, ou seja, em que momento irá manter a booster com FPBA 9,6 ppg, pois ao instalar o BA o fluxo passa a ser pela flowspool e o alinhamento para o sistema MPD precisa ser efetuado.
Acrescentar o teste do BA, que deverá atender metodologia Hold Point com aprovação do CSD-MPD.
Sugiro verificar com o químico para melhorar a clareza do passo #20:
#20 b) Já foi bombeado o tampão viscoso? "prosseguir deslocando o fluido 8,8 ppg..."?
#20 c) Não entendi este passo, pois no caso de interrupção de bombeio pela coluna, a booster deverá estar no circuito para manter AP 9,6 ppg na sapata.
#20 e) Se é para controlar AP = 9,6 ppg na sapata, conforme "#20 b", não faz sentido deixar o choke MPD totalmente aberto quando "iniciar bombeio pela booster". Qual fluido estaria sendo bombeado? No passo #19 a booster está com as bombas #1 e #3 (barramentos diferentes) e fluido FPBA 9,6 ppg...
#20 f) Neste momento é para retirar a bomba#3 da booster (passo #19) e colocar na coluna?
#21) Esclarecer os pontos do "sistema de MPD" que precisam ser preenchidos nesse momento.

Em FINGERPRINT A POÇO ABERTO:
#22) Se necessário ajustar as vazões da coluna e booster de acordo com o que será usado na perfuração de modo a atender DD/MWD/fluido.
#25) Verificar se este é o melhor arranjo das bombas. Alterar se necessário.
#28) Antes de iniciar o DPPT, verificar os parâmetros (bomba, vazão e ajustes de eficiência de bombas) usado na simulação do DPPT no fingerprint. É necessário replicar os mesmos parâmetros, caso não seja possível, efetuar alguns passos para verificar descompressão correta do fluido com os novos parâmetros, efetuando alguns passos de 25 psi, desde que não fique underbalance. Importante não está em perda para ajuste de eficiência de bomba.

> ↳ **Tiago Britto Liberato:** Bom dia,

Sobre o item 20, os subitens "a-d" são orientações gerais para a troca. A troca de fato começa no item "e". Vou renumerar de forma a evitar confusão. 

#20.c, a orientação é pressurizar o poço em caso de "interrupção de bombeio", ou seja, nenhuma bomba ligada.

#20.e: Inicio da troca com bombeio de FPBA 9,6 ppg e AP 9,6 ppg. Ou seja, choke totalmente aberto pois o ECD real será acima de 9,6 ppg com as perdas de carga no sistema.

#20.f: Erro de digitação, vamos ajustar para refletir o planejamento de bombas do fingerprinting (#1 e #3 na booster; #2 e #4 na coluna). A parada de bomba na booster é para passagem do viscoso pelo BOP.

Sobre os itens do fingerprinting, vamos ajustar conforme fingerprinting anterior.

Obrigado!

### 7-JUB-78D-ESS — Descida de BHA de perfuração, troca de fluido, fingerprint e
**Geronimo de Freitas Rolandi** | v2

Considerar esse:

Durante a troca de fluido, será necessário garantir backup de pressurização do poço, já que a booster não estará disponível. Para isso:
Alinhar uma das bombas para o circuito:
 PMCD → BFM → Choke MPD.
Comunicar esse circuito com uma das linhas submarinas via:
 BFM → C&K manifold → Linha Submarina → Riser
Dessa forma, caso seja necessário interromper a circulação na coluna ou fechar o BOP, a SBP continuará sendo aplicada ao poço.

### 7-JUB-78D-ESS — Descida de BHA de perfuração, troca de fluido, fingerprint e
**Geronimo de Freitas Rolandi** | v2

Durante a troca de fluido, será necessário garantir backup de pressurização do poço, já que a booster não estará disponível. Para isso:
Alinhar uma das bombas para o circuito:
 PMCD → BFM → Choke MPD.
Comunicar esse circuito com uma das linhas submarinas via:
 BFM → C&K manifold.
Dessa forma, caso seja necessário interromper a circulação na coluna ou fechar o BOP, a SBP continuará sendo aplicada ao poço.

### 7-JUB-78D-ESS — Descida de BHA de perfuração, troca de fluido, fingerprint e
**Geronimo de Freitas Rolandi** | v1

Observações Gerais
RCD com Protect Sleeve Instalada
Em Observações de MPD, verificar necessidade de três bombas na coluna durante a perfuração, o fingerprint foi feito com duas bombas na coluna e duas na booster, caso seja necessário usar três bombas na coluna deixar claro que o alinhamento padrão de conexão vai ser realmente feito com duas bombas na booster, como está escrito agora, parece opcional. Verificar com químico qual seria o arranjo de tanques necessário. Sugestão de redação:
 e.  Alinhamento padrão para booster durante conexão:
   i. MP2: Antes da conexão, ainda com MP2, MP3 e MP4 na coluna, retirar vazão da MP2 e alinhar para a linha de booster.

Troca de Fluido

Manter controle paralelo com strokes bombeados x SBP necessário (estático e dinâmico) em caso de falha ou duvidas das leituras  do PWD. 

Fingerprint Poço Aberto

Esse fingerprint vai ser apenas uma verificação da sintonia de PID que já foi feita, portanto não vejo necessidade de pressurizar o poço aberto com esse delta de 300 psi 

Passo 18, Verificação do PID :
usar SBP no final da troca = X, aplicar os passos de  X+50, X+100, X+50, X.
Idem no passo 19:

22 e 23, fazer apenas uma verificação da calibração do Modelo Hidráulico
Executar pumps off (conexões) com o objetivo de verificar os valores de ESD. Para esta etapa, recomenda-se adotar AP com valor ligeiramente superior, considerando que a condição será de poço aberto. Sugestão: utilizar referência inicial de 9,6 ppg e, em seguida, confirmar os valores de ESD para 9,5 ppg.

DPPT
27. Obrigatório fechamento do DSIT para circular gás de acordo com PE-2POC-01113

### 8-BUZ-96D-RJS — Montagem de BHA 8,5 e relogging
**Gustavo Costa Magalhaes Pena** | v1

De acordo.

O alinhamento do item 12 é para facilitar a manutenção da vazão de controle em caso de pré-teste com o BHA fora do fundo e BOP anular fechado.
Na retirada do BHA retornar para a booster conforme item 18.

### 8-BUZ-96D-RJS — Montagem e descida de BHA após manobra, perfuração 8,5 pol, 
**Ivani Tavares de Oliveira** | v1

De acordo.
Só um alerta no item 5: usar o FPBA 8,55ppg viscosificado recém fabricado para minimizar risco de H2S. 
 item 8, 9, 10, 11, 13... retomar abastecimento pela linha de booster.

### 8-BUZ-96D-RJS — Montagem e descida de BHA após manobra, perfuração 8,5 pol, 
**Gustavo Costa Magalhaes Pena** | v1

Em considerações para operação MPD, o fator de segurança de 2x deve ser aplicado para os dois cenários, com e sem coluna.

Item 6: O hold point MPD pode ser realizado com 300 psi, não há necessidade de aplicar um diferencial grande na LBSR, pois estamos em FMCD (diferencial total deve ficar na ordem de 700 psi - riser cheio mais SBP).

Item 7e: É preferível usar a booster ao invés da linha de PMCD.

> ↳ **Gustavo Costa Magalhaes Pena:** Item 6 monitorar por 15 min.

### 8-BUZ-96D-RJS — Montagem e descida de BHA com MF, perfuração 8,5 pol, manobr
**Ramon Moreira Fernandes** | v1

Passo 6: "[...] monitorando volume do trip tank"

Passo 24 a 26: Não há necessidade de preencher o riser e efetuar o flowcheck estático. Pode partir direto para retirada do BA. Além de reduzir o tempo da operação, evita aplicar diferencial de cima pra baixo na gaveta cega.

### 8-MRO-36-RJS — Conexão do BOP, descida do BHA 12 ¼” x 13 ½” e teste com col
**Ramon Moreira Fernandes** | v1

Prezados

O teste do buffer manifold é com 300 / /3000 psi (preparativos).

Próximas operações: Instalar SSA no ACD e testar sistema MPD.

### 9-BUZ-103D-RJS — Montagem do BHA #3 (PDC 16 pol + RSS) e teste do BOP
**Gustavo Costa Magalhaes Pena** | v2

De acordo.

Somente lembrar que o item 1 ocorrerá junto logo em seguida ao teste funcional do diverter.

### 9-BUZ-103D-RJS — Montagem do BHA #3 (PDC 16 pol + RSS) e teste do BOP
**Gustavo Costa Magalhaes Pena** | v1

De acordo. Somente alguns comentários e sugestões.

Sobre o sistema MPD:

Teste funcional do DSIT: Da forma que está escrito deveria ter sido realizado na instalação da junta. Como o teste ficou para ser realizado durante os preparativos da fase 4, o teste funcional irá acontecer junto com o teste de estanqueidade do sistema MPD (só que sem as marcas).

Teste das PRVs e das válvulas do BFM: Deve ser planejado para ser realizado nas operações em paralelo: durante os testes do BFM e fingerprint offline. Durante o treinamento prático faremos mais testes funcionais, só que no caminho crítico com a função de treinamento das equipes.

Teste de circulação com AGMAR: 
A recomendação neste item é dividir em 02 partes:

a) Verificação de perda de carga FS até BFM - Caminho crítico:
Em momento oportuno durante a descida do BHA #3, interromper a manobra, conectar TD, fechar o DSIT (aproveitar para fechar pelo painel HPU), circular AGMAR a 300/900/1500 gpm (coluna + booster), com retorno para mangueiras #1 e #2, mangueira #1 e mangueira #2, e registrar as pressões nos manômetros. Cessar circulação, abrir DSIT, desconectar TD e seguir com manobra/operação. Importante nesta etapa ter pelo menos uma PRV alinhada (testada, funcional e setada) para proteção do circuito de superfície. 

b) Verificação de perda de carga BFM para peneiras ou MGS (via by-pass já que não temos equipe SLB MPD a bordo para alinhar para os equipamentos deles) - Offline:
Esta etapa eu sugiro que seja realizada em paralelo à decida do BHA da fase #3, enquanto ainda com AGMAR no sistema. Basta preparar um alinhamento com bombas de lama para a linha de PMCD e efetuar registros dos diferentes manômetros, para os diferentes alinhamentos disponíveis com 300/600/900/1200 gpm. Importante nesta etapa ter pelo menos uma PRV alinhada (testada, funcional e setada) para proteção do circuito de superfície.

### 9-BUZ-103D-RJS — Montagem e descida BHA para sidetrack
**Ramon Moreira Fernandes** | v1

Passo 8: se for observado arraste elevado e/ou ameaça de prisão na manobra de descida em poço aberto, poderá ser antecipado o uso do MPD.

Passo 11: para executar o teste do SSA sem sobrepressurizar o poço aberto, considerar o fechamento do BOP (anular ou gaveta) para execução do teste.

### 9-BUZ-103D-RJS — Montagem e descida BHA para sidetrack - 2ª tentativa
**Gustavo Costa Magalhaes Pena** | v1

De acordo com a SeqOp.

Sugestões no item 11: 
Acredito que será necessário retirar pelo menos 02 seções para ter espaço para instalar o SSA. 
O cenário em que estamos, podemos executar o HP MPD aplicando 300 psi na câmara da ACD, com a UC e monitorar por 5 min (critério de aprovação de baixa pressão).

### 9-BUZ-103D-RJS — [Contingencial] Montagem e descida BHA para sidetrack - 3ª t
**Ramon Moreira Fernandes** | v1

Passo 11: Efetuar teste de estanqueidade do SSA com 300 psi / 5 min.
Passo 11 / 2º bullet: pressurizar com unidade de cimentação de modo a permitir monitoramento e validação do holdpoint via RTO-Live.

> ↳ **Matheus Marins Gonzaga:** Obrigado pelos comentários, Ramon,

Corrigido período de teste na v2. Quanto à pressurização da câmara entre os ACDs, na corrida anterior foi feita pelo skid de lubrificação com monitoramento no sensor de SBP, com sucesso. Dessa forma evita uma sobrepressurização acidental com a UC, classificada para uma pressão muito maior que o skid.

### 9-BUZ-103DA-RJS — Descida do BHA e perfuração 12,25 x 13,5 pol
**Leonardo Mesquita Caetano** | v2

Caros,
ajustar nos limites do MPD a MaxSP: 

De:1400 psi
Para: 515 psi

> ↳ **Thiago Rodrigo de Souza:** Olá, Leo. Obrigado pela sugestão. Vamos ajustar para a V3. Abraço!
