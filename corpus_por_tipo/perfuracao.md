# Perfuração com MPD

47 SEQOPs | 79 comentários MPD

## Análise IA dos Comentários

```json
{
  "sub_tipos": [
    "Perfuração 16\" em MPD/SBP (fase debug)",
    "Perfuração 12,25\" com MPD",
    "Perfuração 8,5\" com MPD",
    "Perfuração em FMCD",
    "Perfuração em PMCD dinâmico",
    "Contingência para perfuração em FMCD/PMCD",
    "Manobra para troca de BHA em MPD"
  ],
  "pontos_verificacao": [
    {
      "item": "Inserção de fluxograma de controle de poço com MPD",
      "frequencia": "alta",
      "exemplo_real": "Recomendo inserir o fluxograma de controle de poço com MPD."
    },
    {
      "item": "Teste de vedação do SSA com critérios específicos",
      "frequencia": "alta",
      "exemplo_real": "Testar vedação do SSA (Holdpoint MPD): estabelecer vazão no riser via booster com 600 gpm, aumentar gradativamente contrapressão até SBP de conexão (700 a 750 psi) previsto para operação e monitorar trip tank."
    },
    {
      "item": "Monitoramento do trip tank para identificar vazamentos",
      "frequencia": "alta",
      "exemplo_real": "Monitorar poço pelo trip tank durante para identificar possíveis vazamentos no bearing assembly."
    },
    {
      "item": "Definição de vazões de controle e bullheading com margem de segurança",
      "frequencia": "alta",
      "exemplo_real": "Vazão de controle simulada (AGMAR e sem coluna) de 2,5 bpm, e portanto considerar vazão de controle de 5 bpm."
    },
    {
      "item": "Critérios de aceitação para testes de estanqueidade",
      "frequencia": "alta",
      "exemplo_real": "Critério de aceitação: 0,25 bbl / 15 min (1 bph)."
    },
    {
      "item": "Alinhamento correto das bombas e sistemas MPD",
      "frequencia": "alta",
      "exemplo_real": "A vazão da booster para manobra é de 600 gpm, com 02 bombas de barramentos diferentes."
    },
    {
      "item": "Troca de fluido com controle de pressão e alinhamento adequado",
      "frequencia": "alta",
      "exemplo_real": "Troca fluido das linha de kill, mantendo circulação no circuito de superfície com fluido leve pela linha de PMCD."
    }
  ],
  "erros_frequentes": [
    "Omissão do fluxograma de controle de poço com MPD",
    "Falta de detalhamento nos critérios de parada e contingência",
    "Erro na definição de vazões de controle e bullheading",
    "Omissão de testes de pressão como Hold Point",
    "Alinhamento incorreto de bombas e sistemas MPD",
    "Falta de monitoramento adequado do trip tank"
  ],
  "padroes_aprovacao": [
    "Inserção de fluxograma atualizado de controle de poço com MPD",
    "Definição clara de critérios de aceitação para testes de pressão e vedação",
    "Utilização de vazões simuladas com margem de segurança",
    "Monitoramento contínuo do poço via trip tank e sensores",
    "Alinhamento correto de bombas e sistemas MPD para cada etapa",
    "Planejamento detalhado para troca de fluido e manobras de BHA"
  ],
  "normas_aplicaveis": [
    "PE-2POC-01113",
    "PE-2POC-01392",
    "PE-1PBR-00050"
  ]
}
```

## Comentários MPD Completos

### 1-RJS-763D — 24 - Perfuração 12,25'' com MPD
**Gustavo Costa Magalhaes Pena** | v1

De acordo. Somente 02 recomendações com relação às figuras de Controle de poço com MPD.

Em alertas com operações MPD:
Recomendo inserir o fluxograma de controle de poço com MPD.
Item 15d: Atualizar a figura conforme foi feito na SeqOp #23.

### 1-RJS-763D — 29 - Perfuração 12,25'' com MPD (RES INF)
**Gustavo Costa Magalhaes Pena** | v1

Prezados, seguem comentários e sugestões:

Em perfuração, item 6, Critérios de parada da fase: Senti falta de mais detalhes sobre o fluxograma de projeto (talvez incluí-lo na SeqOp). 

Entendo que iremos perfurar até identificar o trecho salino e faremos uma avaliação para execução ou não do DFIT (se perdas ou não). Se sem perdas, iremos fazer o DFIT (já com fluido UB).
Se resultado satisfatório, prosseguir com perfuração, caso contrario, amortecer poço e acionar fase contingência 8 1/2".

Em DFIT:
Item 2: Não vejo necessidade do viscoso. Sobre o posicionamento da broca temos 02 opções:
a) Retirar 5 m do fundo e fazer o DFIT monitorando o EMW calculado no topo do reservatório. Nesta opção pode haver um erro no cálculo de perda de carga (entre PWD e topo do reservatório), e consequentemente um erro no EMW calculado.
b) Retirar BHA até posicionar o PWD no topo do reservatório e fazer o DFIT monitorando o ECD medido. Nesta opção o monitoramento somente olhando o ECD medido, porém se faz necessário uma manobra maior.

Item 3: Não existe necessidade de circular para limpeza, pois não temos cimento retornando e o coriolis já está alinhado. Pode eliminar essa etapa.

Item 4: Se optar pela alternativa b no item 2, fazer essa etapa antes da manobra.

Item 7: Se optar pela alternativa a no item 2, registrar e monitorar o EMW calculado no AP depth pelo modelo hidráulico como resultado do DFIT (não pressão no fundo).

> ↳ **Ramon Sena Barretto:** Prezado, com o término da perfilagem e determinação da estratégia de anchor point que trazemos na V2, grupo decidiu suprimir DFIT no trecho salino, então árvore ficou bem simples. Agora ela se resume ao resultado exploratório conforme determinado a seguir:

Sequencia ficou mais simples.

### 1-RJS-763D — S11 - Perfuração 16” em MPD/SBP (fase debug)
**Gustavo Costa Magalhaes Pena** | v3

De acordo. 

Abaixo algumas recomendações:

Item 2, contingências de combate a perda: Mencionar o papel do MPD no cenário de combate a perda, conforme tratado na sequencia de contingência.

Em retirada de coluna:
Item 6b: O retorno deve estar alinhado para o trip tank e não flow diverter.
Item 7: Avaliar necessidade de compensar Swab já que o critério de parada fica 70 m acima do topo do reservatório. Se não for necessário, avaliar retirada do BA em poço aberto.

### 3-RJS-762 — 24 - Prosseguimento da perfuração 12,25 pol_3-RJS-762
**Ramon Moreira Fernandes** | v2

Passo 9: Após instalação do packer assy, é necessário testá-lo com SBP máxima (SBP de conexão). Para efetuar esse teste, fechar o BOP anular e mantém poço pressurizado via unidade de cimentação. Em seguida coloca vazão na booster e aumenta a contrapressão. Critério para avaliação do teste pelo trip tank, ganho máximo de 0,1 bbl/ 5 min. Vamos considerar Holdpoint também esse teste.

Passo 10 / c: testar vedação do BA com máxima SBP prevista. Alternativamente pode-se testar da mesma forma que o teste do packer assy: com vazão na booster + contrapressão e BOP anular fechado.

Passo 26: caso tenha dificuldade para executar essa transição de controle da contrapressão diretamente para circuito de superfície, alternativamente pode transferir primeiro o controle da contrapressão para unidade de cimentação e em segundo momento transferir o controle da contrapressão para o circuito de superfície.

### 3-SPS-111D — 31 Perfuração 8,5 x 9,5 pol
**Ivani Tavares de Oliveira há um ano** | v2

Após o adensamento do fluido no item 56 para FPBNA 12,1ppg, o choke estará todo aberto.
item 60, subitem a) Fluido já foi adensado anteriormente para FPBNA 12,1ppg? ou este item não está relacionado a sequência numérica?

> ↳ **Ramon Sena Barretto há um ano:** No item 60 nós já trocamos o fluido de fato. Corrigido!

### 3-SPS-111D — 31 Perfuração 8,5 x 9,5 pol
**Ivani Tavares de Oliveira há um ano** | v1

Em OBSERVAÇÕES PARA OPERAÇÃO COM MPD ou em ATIVIDADES PERIÓDICAS, incluir:
Toda instalação do SSA, o teste de pressão é hold point. Utilizar, no mínimo, 300 psi / 5 min, ou usar pressão de SBP (se maior que 300 psi).
Solicitar ao responsável pelo MPD da sonda a figura do alinhamento e adicionar aqui.

Item 28, corrigir repetição do texto "ppg".

Item 30 e 32. A figura do item 7 é sobre RPM x SBP. A tabela do item 6 é referência para limite de velocidade de manobra com SSA instalado. Sugiro manter o texto usado anterior: conforme OBSERVAÇÕES PARA OPERAÇÃO COM MPD – Item 6.

### 3-SPS-111D — 33 Perfuração 8 1/2" (após testemunhagem 8 1/2")
**Gustavo Costa Magalhaes Pena** | v6

Conforme conversado com fiscalização, recomendado refazer planejamento dos itens 17 a 20 para a etapa de bleed de potencial HC abaixo do DSIT utilizando a linha de 2" alinhada para o BFM, Choke Manifold da sonda, choke hidráulico da sonda e MGS.

### 3-SPS-111D — 33 Perfuração 8 1/2" (após testemunhagem 8 1/2")
**Ramon Moreira Fernandes** | v3

Prezados

Apenas descrevendo um pouco melhor o teste do SSA no item 8/d da etapa de perfuração:
Testar vedação do SSA (Holdpoint MPD): estabelecer vazão no riser via booster com 600 gpm, aumentar gradativamente contrapressão até SBP de conexão (700 a 750 psi) previsto para operação e monitorar trip tank. Critério de máximo ganho de 0,1 bbl/5min. Em paralelo manter monitoramento do poço via UC. Obs: alinhar apenas 1 trip tank para o riser durante teste do SSA.

Passo 13: Está escrito circular 10 min para quebra de gel a 200 gpm. Porém no subitem fala em Bottom´s UP. Sugiro deixar mais claro se será feito um Bottom´s Up mesmo e caso positivo usar vazão de perfuração para monitorar o ECD.

### 3-SPS-111D — 33 Perfuração 8 1/2" (após testemunhagem 8 1/2")
**Gustavo Costa Magalhaes Pena** | v2

Prezados, seguem comentários e sugestões:

Em preparativos, item 9: Sugiro incluir o fluxograma de controle de poço com MPD nesta parte.

Em montagem do BHA:
Item 9: Retirar "para operação de testemunhagem".
Item 20: Atenção para a grande chance de ocorrência de falso kick durante o relog, devido ar de abastecimento. Recomendo monitorar o BU a partir do inicio do relog.

Em perfuração:
Item 22, subitens i, j: Na ocorrência de perdas para a formação é importante conhecermos o limite inferior da janela operacional. Sendo assim, recomendo que seja realizado, o mais breve possível, uma tomada pré-teste em ponto definido pela geologia.

Em condicionamento:
Item 25.a: 600 gpm na coluna. E a booster? 300 gpm com FPBA 11,5 ppg?
Item 25.c: A vazão de 50 gpm na booster com FPBNA 12,1 ppg.
Item 25.d: Atenção que ao abrir o segundo choke manualmente. Importante ficar de prontidão para fechamento do segundo choke em caso de necessidade/ocorrência de interrupção da vazão na coluna (sistema irá precisar aumentar a SBP para compensar a perda de carga).
Item 25.g: Lembrar que temos o coriolis monitorando o peso do fluido de retorno.
Item 26: Após o flow check estático reenergizar packers da ACD para a manobra com SBP.
Item 29: Enviar relatório de desgaste do SSA para o CSD MPD (assim que ele for concluído).

Em contingência para manobra de troca de BHA:
Item 40: AP 12,1 ppg para 12,2 ppg.
Itens 41 a 47: Booster com 600 gpm.
Item 49: Enviar relatório de desgaste do SSA para o CSD MPD (assim que ele for concluído).

Em observações para operação com MPD:
Item 7, subitens c, e: Informação contraditória quanto ao alinhamento das bombas da coluna e da booster.

### 3-SPS-111D — 33 Perfuração 8 1/2" (após testemunhagem 8 1/2")
**Geronimo de Freitas Rolandi** | v1

Augusto, conforme conversamos, detalhar os passos de transferência de controle de pressão para passagem do BHA pelo BOP, considerando um limite de perda de 15 bbl/h para fazer sem utilizar a unidade de cimentação para controlar o poço.

### 3-SPS-113 — 26 Perfuração 8 1/2" em MPD
**Gustavo Costa Magalhaes Pena** | v3

Devido condição anormal do sensor de pressão no fundo (PWD Ontrak) está sendo avaliado abortar a troca de fluido 12 x 11 ppg, dos itens 5-8.

> ↳ **Nelson Rogerio Murici Brasiliense:** Prezados do CSD MPD, favor analisar a seop. A informação que temos é que o PL está correto (12 x 11 ppg).

### 3-SPS-113 — 26 Perfuração 8 1/2" em MPD
**Gustavo Costa Magalhaes Pena** | v1

Seguem comentários:

Em perfuração 8 1/2":

Itens 1.f, 1.g e 3: Atenção os eventos de abertura e fechamento de alargador podem afetar significantemente a pressão de bombeio, e consequentemente a eficiência das bombas, resultando em falsos eventos de perda e ganho quando observando a tendência do VTT.

Itens 1.b e 1.h: Pela arvore de decisão para a testemunhagem entendo que não está prevista a realização da tomada de pré-teste nesta primeira corrida, já que o TestTrak está 36 m acima da broca e iremos avançar no máximo 30 m dentro do reservatório. Uma alternativa para determinar o limite inferior da janela operacional seria um DPPT

Itens 4 até 8 - SUGESTÕES:
Primeiramente faria uma descompressão do poço no formato DPPT, até conclusão com um flow check estático com FPBNA 12,3 ppg. O EMW no topo do reservatório será da ordem de 12,45 ppg (confirmar pelos dados de ESD).
Em seguida, partir para a troca de fluido de FPBNA 12,3 ppg para FPBNA 11,3 ppg mantendo o AP igual ao EMW observado no flow check estático com FPBNA 12,3 ppg.
Ao término da troca, reduzir o AP até 12,3 ppg em steps. Avaliar nesta etapa a realização de um DPPT para determinar o limite inferior da janela operacional e permitir ajustar a SBP necessária para as manobras (retirada BHA #1, descida e retirada BHA#2 e descida BHA #3).
Efetuar verificação das condições para testemunhagem: compensador e modelo hidráulico.

Itens 17 e 18: Priorizar o uso da UC para transferir a gestão de pressão do poço via booster para circuito de superfície (alinhamento mais simples e intuitivo). O alinhamento proposto no item 18 deve ser muito bem planejado e executado para evitar despressurização do poço.

### 3-SPS-113 — 28 Perfuração 8,5" em MPD após testemunhagem
**Ramon Moreira Fernandes** | v2

Passo 9 (após troca de fluido): acrescentar a abertura do BOP anular.

### 3-SPS-113 — 28 Perfuração 8,5" em MPD após testemunhagem
**Ramon Moreira Fernandes** | v1

Passo 9, item a: critério de aceitação 0,25 bbl por 15 min.

Passo 10 item e: critério de aceitação 0,25 bbl por 15 min.

Passo 18 item e: Em caso de evento de packoff do anular operador MPD deverá avaliar o comportamento do PWDCF e se necessário desabilitá-lo (congelando o fator de correção no último valor lido antes do evento de packoff) de modo a evitar uma despressurização indevida.

Troca do fluido:
Passo 5: antes de iniciar o passo 5, sugiro estabelecer circulação pela linha de PMCD com fluido 11 ppg em circuito de superfície (realizando a função que seria da booster) para ficar protegido de uma eventual queda de bomba da coluna durante a troca de fluido do poço. Após viscoso 300 m acima do BOP, parar a circulação de FPBNA 11 ppg na linha de PMCD e estabelecer circulação de FPBNA 11 ppg pela booster.

> ↳ **Ramon Moreira Fernandes:** Correção: Passo 5: [...] e estabelecer circulação FPBNA 12,3 ppg pela booster.

### 3-SPS-113 — Perfuração 8 1/2" após perfilagem em modo MPD/SBP
**Ivani Tavares de Oliveira** | v1

Em PARTICULARIDADES DAS OPERAÇÕES EM MPD:
10) Para RPM superior a 50, deverá limitar a SBP, conforme gráfico...

> ↳ **Denes Marcel Chaves Lopes:** De acordo com o conversado, comentário não será incorporado.

### 3-SPS-114 — 25 - Perfuração 8 1/2"
**Gustavo Costa Magalhaes Pena** | v3

De acordo. Somente um pequeno ajuste.

No item 10, o critério de aprovação para condição dinâmica (booster ligada e SBP) é de no máximo 0,25 bbl em 15 min.

Na condição vigente (poço amortecido, poço aberto e BHA no fundo), existe também a possibilidade de realizar o teste em condição estática (UC pressurizando câmara da ACD pela linha de 2"), neste caso o critério é de no máximo queda de 10 psi em 5 min.

### 3-SPS-114 — 25 - Perfuração 8 1/2"
**Gustavo Costa Magalhaes Pena** | v1

De acordo.

### 4-RJS-764 — 20 - perfuração 12,25 x 13,5 pol
**Ramon Moreira Fernandes** | v3

Condicionamento e amortecimento:

Considerar o alinhamento de 2 bombas com fluido 8,2 ppg na linha de PMCD em circuito de superfície para manter circulação contínua no sistema de contrapressão enquanto faz a troca das linhas submarinas e do poço revestido por fluido 9,1 ppg.

No primeiro passo da troca de fluido fala em usar AP 9,1 ppg na broca, porém esse AP não havia ainda sido usado nos passos anteriores. Portanto é necessário fazer um flowcheck dinâmico com 9,1 ppg na broca antes de efetuar a troca de fluido com esse AP. Sugiro então no passo 18, após fazer o flowcheck com 9,35 ppg, tbm fazer o flowcheck com 9,1 ppg e manter o AP 9,1 ppg nos passos 19 e 20.

Passo 24: sugiro fazer a troca do poço revestido até 200 m acima do BOP e interromper a troca, fechar o BOP mantendo monitoramento do poço por uma linha submarina (já troca por 9,1 ppg) e por fim trocar o riser de forma isolada. Dessa forma evita o aumento de ECD no poço aberto.

### 4-RJS-764 — 20 - perfuração 12,25 x 13,5 pol
**Gustavo Costa Magalhaes Pena** | v1

Seguem comentários:

Em lembretes e alertas MPD, item a) i.: Antes de fechar o BOP será necessário fazer a retirada de bomba da coluna em modo SBP.

Em observações gerais, item 4.c): Essa condição não se aplica para perfuração em MPD.

Em perfuração:
Item 5: Especificar o AP desejado para o FC.
Item 6: Irá reduzir o AP para 9,2 ppg? Ou manter 9,45 ppg na broca?
Item 9.c: Rotações superiores a 150 rpm na coluna devem ser comunicadas ao CSD MPD para avaliação.
Item 14: Ficou fora de ordem, aparece com 1.
Item "16": Na verificação e ajuste do MH para testemunhagem será necessário variar a vazão entre vazão de perfuração e vazão de testemunhagem, sem ir a zero, para obter os ESDs da condição de testemunhagem. Sabemos que existe o risco de indexar o alargador, sendo assim, evitar fazer esta etapa com rotação para não alargar o trecho.

Em retirada da coluna, item 23.e: "avaliar aplicar SBP para compensar SWAB".

### 4-SPS-112 — Perfuração 12 1/4" x 13 1/2"
**Leonardo Mesquita Caetano há um ano** | v5

Caros, antes de tirar o BHA de perfuração para a testemunhagem, realizar uma verificação do modelo hidráulico com 200 gpm na coluna (vazão da testemunhagem)

### 4-SPS-112 — Perfuração 12 1/4" x 13 1/2"
**Ivani Tavares de Oliveira há um ano** | v4

De acordo.
Apenas atentar que toda instalação de BA, o teste é Hold Point e o CSD MPD deverá aprovar. Em caso de manobra ou substituição do BA, a pressão de teste é 300 psi contra DSIT.

> ↳ **Issamu Noce Watanabe há um ano:** Ok inserido

### 4-SPS-112 — Perfuração 12 1/4" x 13 1/2"
**Geronimo de Freitas Rolandi há um ano** | v3

Item 1 e Item 4 c: Quanto a alteração sugerida, deixar claro que seriam 1000 psi na conexão, o que daria aproximadamente 800 psi na perfuração. Avaliar a possibilidade de adensar o fluido para evitar essa situação, uma vez que o poço deverá ser amortecido com 12,4 ppg, pelo mesmo motivo não vejo necessidade de fazer o flowcheck dinâmico de 12,1 ppg, fazendo com 12,4 ppg, garante que toda a pressão abaixo do AP (no caso o topo do reservatório) estará com uma pressão superior à simulada no flowcheck dinâmico quando o poço for amortecido com 12,4 ppg.

> ↳ **Andre Luiz Tomelin há um ano:** Bom dia. Temos histórico de efetuar DPPT com até 0,3 ppg abaixo da pressão de poros abaixo da pressão real, sem constatar anomalia de fluxo (com PP constatada posteriormente com pré-teste na perfilagem) e acabar usando valor inadequado para o peso de fluido para a perfilagem. Com isso, foi definido o valor de +0,3 ppg em cima do mínimo AP alcançado como margem de segurança.

### 4-SPS-112 — Perfuração 12 1/4" x 13 1/2"
**Geronimo de Freitas Rolandi há um ano** | v1

Após o passo 17 e caso poço sem perda severa, é recomendável passar novamente o controle da pressão do poço  da UC para o sistema MPD via circuito de superfícíe -> kill line, exemplo:
1.      Fazer alinhamento do circuito de superfície MPD:
a) Isolar Riser do circuito de superfície fechando as válvulas R1 e R3 do flowspool (manter PRV1 e PRV2 alinhadas para o circuito de superfície);
b) Alinhar: Bomba da sonda -> STP -> Linha de PMCD -> BFM -> Choke MPD
c) Abrir válvulas B7 e B13, alinhando BFM para o choke manifold da sonda até válvula que está sendo pressurizada pela UC no choke manifold da sonda;
d) Circular pelo circuito de superfície com 400 gpm aumentando a pressão até SBP de manobra;
e) Abrir válvula do choke manifold comunicando circuito de superfície com linha de kill, nesse momento o poço estará vendo a pressão do circuito de superfície e da unidade de cimentação;
2.      Isolar unidade de cimentação fechando válvula no choke manifold e despressurizar UC, liberando o operador da UC;

### 4-SPS-112 — Perfuração 8,5 pol com MPD
**Gustavo Costa Magalhaes Pena** | v1

De acordo com a SeqOp. Somente 02 comentários:

Em atividades periódicas, item 10: Apesar do fluido ser FPBNA 11,7 ppg é esperado um efeito de compressibilidade de pelo menos 0,15 ppg (fluido sintético). Com isso, o rearm em 750 psi de SBP (limite recomendado em padrão) seria suficiente para manter 12,4-12,5 ppg a 6733 m.

Em retirada de coluna para troca de broca, item 8: É recomendado que após o subitem x, o sistema MPD seja alinhado pela linha submarina para monitorar o poço. A manobra de retirada, quebra do BHA, montagem do novo BHA e descida pode levar um longo tempo e o  sistema MPD é mais indicado para monitorar o poço. A unidade de cimentação permite apenas que seja possível a troca dos alinhamentos do sistema MPD do riser, para o circuito de superfície.

> ↳ **Anderson Avelar de Paula:** Obrigado pelas sugestões, entendidos os pontos, mas serão mantidos como na v1. Monitoramento pela UC tende a ser operacionalmente mais simples e mais seguro (menos equipamentos operando de modo continuo e menos pessoas envolvidas).

### 4-SPS-112 — Perfuração12 1/4" em MPD
**Gustavo Costa Magalhaes Pena há um ano** | v2

Em montagem e descida de BHA, item 7: Recomendo que se o sistema de contrapressão estiver monitorando o poço via linha submarina, que seja alterado o monitoramento do poço para a UC, liberando o sistema MPD para ser alinhado para o riser para que o HP seja realizado aos moldes do item 6. Ou seja, remover item 7. A ideia é que após a aprovação do HP, o alinhamento já esteja pronto para abertura do BOP e descida do BHA.

Em troca de fluido (amortecimento):
Item 1: Flow check dinâmico de 15 min.
Itens 3, 6 e 11: Flow check estático com FPBNA de 30 min, conforme PE-1PBR-00050.
Item 10: Não se aplica SBP sem o BA. Remover subitem a).

> ↳ **Gustavo Costa Magalhaes Pena há um ano:** Um detalhe a mais para ficar atento, a partir do item 13 (vazão pela coluna) monitorar o BU, pois existe uma grande chance de eventos de falso kick causado por ar de abastecimento (aumento do nível do tanque ativo sem detecção de anomalia pelo sistema MPD).

### 4-SPS-112 — Perfuração12 1/4" em MPD
**Gustavo Costa Magalhaes Pena há um ano** | v1

Seguem comentários:

Itens 6 e 7: A estratégia e o critério de HP MPD para instalações de BA após manobra de BHA ainda não está definido. Sugiro entrar em contato com CSD MPD para definirmos a melhor estratégia.

Itens 8 até 13: Pendente mencionar o AP (equivalente) de manobra de 12,5 ppg @ 6427 m.

Em troca de fluido (amortecimento):
Item 3: Flow check estático com BA instalado.
Itens 4 e 6: Com o peso do fluido em 9,4 ppg, entendo que a ideia seja retirar o BHA com AP 9,5 ppg a 6427 m, certo? Ou querem usar a modalidade de compensação automática swab do sistema MPD?

Manobra para troca de broca/BHA:
Item 2: Sugiro fazer o flowcheck dinâmico somente com booster.
Itens 3, 16 e 19: Retirar o BHA com AP 9,5 ppg a 6427 m ou usar a modalidade de compensação automática swab do sistema MPD?
Item 22: Entendo ser possível a manobra (NS39 vem praticando nos poços de Mero), no entanto atentar para a complexidade e a quantidade de pontos de falhas possíveis nesta estratégia. É possível utilizar a UC mesmo em cenário de perdas, somente durante a transição do sistema MPD via booster para sistema MPD via circuito de superfície. E a utilização da UC para essa função possui alinhamento bem mais simples e intuitivo para a equipe da sonda.

> ↳ **Issamu Noce Watanabe há um ano:** Boa tarde Gustavo...Itens 6 e 7: Como conversado adicionei o critério: 01 bbl em 5 min
Itens 8 a 13: Adicionado

Em troca de fluido (amortecimento). 
Item 3: Flow check estático com BA instalado. Sim
Itens 4 e 6: O fluido do poço após a troca vai ser 12,4 ppg. Como a compressibilidade é 0.17 ppg e a simulação passada o SWAB para 18 m/min foi 180 psi O swab = compressibilidade e estaríamos 0,2 ppg acima da PP..como o GEP pediu para retirar com AP=12,5 ppg, .a troca do BA vai ser alguma coisa acima da sapata...a simulação está em andamento para informar a profundidade de troca de BA e velocidades. 

Manobra para troca de broca/BHA.
Item 2: Sim, como realizado na retirada anterior fizemos pela booster e vamos repetir....esse item é repetição da SEQOP passada..... vou reforçar que será pela booster
Itens 3, 16 e 19: Na retirada passada o pessoal da HALL disse que se sentiriam mais confiantes retirar no modo SBP..... como a simulação estava demorando muito....e no caminho critico...pedimos para considerar o maior valor simulado para toda a retirada......agora já temos a simulação, então o combinado é retirar em SBP, conforme simulação que fizeram. Vou colocar essa observação na SEQOP. 
 Item 22: Correto estamos cientes disso, entendo que vai depender do nível de perda. Na hora da operação a depender da perda com certeza será discutido. Também acho melhor fazer pela UC, principalmente para dar tempo de manutenção no CM.... vou acrescentar essa observação.

### 7-BUZ-100D-RJS — Perfuração 8,5 pol em MPD
**Gustavo Costa Magalhaes Pena** | v1

Em considerações para operação MPD, se convertido para FMCD ou PMCD dinâmico as vazões aplicadas deverão conter fator de segurança 2 em relação ao resultado da simulação. Importante conhecer as vazões para os cenários com e sem coluna.

Item 3: Recomendo avaliar a possibilidade de não precisar circular o tampão viscoso com a coluna parada. Como estamos com fluido hidrostaticamente OB, podemos iniciar a perfuração em modo convencional com BA instalado e após concluir a limpeza do poço, geralmente com 1,5 BU (cerca de 6h), podemos alinhar o sistema MPD e perfurar dali em diante com SBP e coriolis alinhado. Fizemos essa estratégia recentemente no BUZ-96, com FAM já que o projeto previa uso do MPD durante toda a fase.

Item 7: O recalque do anular é iniciado pela linha de PMCD. Depois de completar o recalque do volume do riser, ai pode migrar para booster.


Item 10: Manter em mente a opção de prosseguir expondo formação para tentar converter para FMCD mais rápido, se conseguir perda total. Se converter para PMCD, provavelmente será PMCD dinâmico (após troca do fluido do anular por SAC no FMCD) já que a pressão de poros estimada é menor que o peso de fluido.

> ↳ **Thiago Rodrigo de Souza:** Bom dia, meu caro. Obrigado pelas sugestões. Vamos aos comentários:

Em considerações para operação MPD:
 - Conforme conversado pelo TEAMS, aplicado fator de segurança 2 apenas à vazão de controle, conforme padrão PE-2POC-01392.
 - A simulação que recebemos, do poço 7-BUZ-85-RJS por similaridade, tem apenas o cenário com 'poço equipado', ou seja, com coluna. Adotamos para o cenário sem coluna 1,5 x o valor para poço com coluna, ou seja, vazão de controle de 3 bpm para FPBA e 6 bpm para SAC, e vazão de bullheading 15 bpm. Será contemplado na V2. Esse fator de 1,5 foi estimado pela razão entre as áreas de fluxo sem e com coluna, com alguma margem de segurança. Os valores também ficaram coerentes com o que está sendo executado no 8-BUZ-96D-RJS com NS47.

Item 3: Devido a demanda de coletar cascalho desse poço para desembarque, e ao fato de que a qualquer momento podemos entrar em MCD (e não ter mais cascalho para coletar), o CGEP preferiu manter o plano conforme sequência operacional.

Item 7: Conforme conversado pelo TEAMS, estamos prevendo alinhar inicialmente para a linha de booster porque no passo 8 é feita a troca de fluido das linhas. Em seguida, no próprio passo 8, troca-se o fluido do anular (via linha de PMCD) antes de voltar o alinhamento para a booster.

Item 10: 100% de acordo. Será contemplado na V2.

Abraço!

### 7-BUZ-100D-RJS — [Contingência] Perfuração 8,5 em FMCD ou PMCD dinâmico
**Gustavo Costa Magalhaes Pena** | v1

Seguem comentários:

Em considerações para operação MPD, recomendo retirar a tabela de matriz de perfuração FMCD. A tabela da parte de perfuração é mais completa (considera mais manômetros e melhora a capacidade de diagnóstico). 
Desta tabela é importante a parte da incapacidade de manter vazão no anular. Para esse fim temos bombas de lama e UC de prontidão. Itens mencionados abaixo da tabela.

A figura que trata sobre controle de poço não se aplica para o cenário MCD. É só bullheading.

Em manobra para troca de broca:

Itens 4 e 5: Com a retirada da vazão de coluna, é provável que o PMCD dinâmico vá para o modo FMCD.

Item 6: Não precisa de 420 gpm. Pode manter 6 bpm.

Item 8: Atenção para o diferencial de pressão na LBSR, a depender a pressão da zona de perda.

Itens 15 e 16: Se em FMCD procurar manter FPBA no trip tank, e antes de instalar o BA, posicionar FPBA acima da RCD utilizando a linha de 2" ou de 6". A ideia é que ao abrir o BOP, o fluido acima do BA com viscosidade vai reduzir a intensidade do vazamento do mesmo no sentido superfície x poço.

Item 17: Teste Hold Point MPD.

Item 19: Não é necessário, pois o BA foi testado no item 17.

Itens 21, 22 e 23: Caso seja observado um vazamento muito grande do BA no sentido superfície x poço. Contactar CSD MPD para mudar "monitoramento" e lubrificação do BA utilizando linha de Fill-up diverter.

Item 24: ou PMCD dinâmico.

> ↳ **Stefano Primo:** Em considerações para operação MPD, retirada a tabela de matriz de perfuração FMCD.

> ↳ **Stefano Primo:** A figura que trata sobre controle de poço foi removida.

### 7-BUZ-100DA-RJS — [Contingência] Conversão e perfuração da fase V 8,5" em FMCD
**Ramon Moreira Fernandes há um mês** | v3

Pessoal

Revendo melhor a etapa de retirada em FMCD, é necessário considerar uma vazão de abastecimento anular maior para compensar a vazão de retirada de coluna cheia (sendo mais conservador). A vazão correspondente a retirada de coluna cheia é de ~2,1 bbl/min. Essa vazão deve ser adicionada da vazão de controle praticada (4 bpm). Portanto para manter o poço com o mesmo perfil de abastecimento durante a retirada, podemos considerar um abastecimento de 4 + 2,1 = 6,1 bpm (4,5 bpm atende também consierando a vazão mínima de bullhead). Em resumo vamos alterar a vazão de abastecimento para 5 bpm durante a retirada da coluna em FMCD.

### 7-BUZ-100DA-RJS — [Contingência] Conversão e perfuração da fase V 8,5" em FMCD
**Leonardo Mesquita Caetano há um mês** | v2

Caros, bom dia
Em manobra de retirada, compensar o volume de aço retirado na vazão de ataque com fator de segurança de 20%.

> ↳ **Leonardo Mesquita Caetano há um mês:** Sugestão também de tirar:
vazão mínima: 1,8 bpm

Usar valores simulados de bullhead  2,4 bpm ou duas vezes vazão mínima de controle.

### 7-BUZ-100DA-RJS — [Contingência] Conversão e perfuração da fase V 8,5" em FMCD
**Ramon Moreira Fernandes há um mês** | v1

Prezados

Informações preliminares / 2º item: "[...] coluna até 500 gpm (vazão máxima permitida aplicável por tempo limitado a 30 min, reduzir para 450 gpm em seguida) e na booster até o máximo possível, e verificar se será possível manter retorno de fluido na superfície".

Informações preliminares: A vazão de controle e de bullheading que aparecem na seqop estão considerando um fluido de perfuração FPBA 8,7 ppg. Para cenário FMCD o correto é considerar agmar na simulação.

Conversão:
Passo 2: Após confirmar perda total (sem retorno mesmo com vazão máxima na coluna e booster), interromper vazão na coluna e manter vazão na booster com FPBA 8,7 ppg a 4 bpm. Nesse momento ainda não inicia o bombeio de SAC (AGMAR).

Passo 3/c: manter bombeio contínuo de FPBA 8,7 ppg a 4 bpm pela booster.

Passos 4/a e 5/g: Manter bombeio contínuo de FPBA 8,7 ppg a 4 bpm pela booster.

### 7-BUZ-90D-RJS — (Contingência) Perfuração 8.5 pol em PMCD
**Leonardo Mesquita Caetano há um ano** | v1

Caros, boa tarde.
A sequência tenta ser genérica e aborda todas as operações de MCD. Ela faz isso bem, mas gera algumas confusões e precisa de alguns ajustes.

De acordo com os comentários já feitos e segue outros:

OPERAÇÕES PARALELAS
Avaliar se Kelly hose da coluna está instalada no Bengala 2. Begala 2 (st2) deverá ficar dedicado a linha de PMCD conforme pendência:
https://sondasmar.ep.petrobras.com.br/SondasMar/pendencias/editaPendencia/68671#/editaAnexos

CONSIDERAÇÕES DE SEGURANÇA OPERACIONA
Em "Monitorar poço pelo trip tank durante para identificar possíveis vazamentos no bearing assembly." considerar ações da FAM relacionada.

CONSIDERAÇÕES PARA OPERAÇÃO MPD

Dados da simulação (SIP) para PMCD/FMCD.
O ideal seria termos uma referência da simulação, porém não encontrei para poço sem coluna nas simulações dos poços de Buzios. No procedimento de manual de projeto MPD recomenda-se usar a equação de Norton Lapeyrouse nesses casos; que dá 30 pés/min. Usando essa equação com fator 2 daria 350 gpm no line de 11 7/8" sem coluna para compensar a migração do gás.

Monitoramento do BA
Usar FAM do trip tank. Em caso de PMCD, sem retorno, qualquer ganho no tanque deve-se fechar o DSIT, para posterior troubleshooting

Item 1 - retirar broca ~10 m do fundo ou da região de perda

Item 1 e 2 - Fechar DSIT para isolar possível vazamento pelo BA

Itens 5, 6 e 7 não estão previsto considerando a pressão de poros p10 de 9 ppg. PMCD Dinâmico também não é uma operação prevista no projeto.

Item 8. Suspeita de vazamento no BA serão identificadas através de ganho nos tanques (PMCD não há retorno do poço). Em caso de qualquer ganho no tanque, fechar DSIT imediatamente e realizar bullheading.

Item 13.

Parâmetros de perfuração: limitar rotação em 150 rpm para minimizar risco de vazamento no BA.

Ajustar condições de "trip tank" com a FAM. Fechar DSIT no caso de ganho no tanque, caso vazamento persista, fechar válvula jusante do choke para troubleshooting

MWD: Ajustar para condição PMCD alterando o texto "Manter booster ligada durante todo o processo, com MPD em modo AP conforme estiver sendo praticado no momento do pré-test"

MANOBRA EM MODO PMC

Item 14. Trocar SAC por LAM no texto.

Item 16. Volume da coluna deverá ser trocado por LAM

Item 17. Ajustar para PMCD: LAM através da linha de PMCD na vazão necessária para compensar 1,2 vezes o volume da coluna molhada. Sugestão de manter essa vazão de compensação de forma constante

Item 19. Nesse momento o anular do poço abaixo do BOP deverá ser monitorado pelas linhas auxiliares, com bombeios periódicos a cada 6 horas

Item 20. Realizar bullheading periódico e monitorar pressão no BOP. Realizar bombeios reativos se a pressão for maior que 100 psi mais a pressão do anular livre da gás. 

Item 24. Trocar "Injetar SAC pela Linha de Booster" por "Retomar alinhamento de LAM pela linha de PMCD e bombear conforme necessário"

Item 26. Trocar SAC por LAM

> ↳ **Leonardo Mesquita Caetano há um ano:** Adicionar o volume no trechos com bullheading. Sugestão de usar vazão 10 bpm

### 7-BUZ-90D-RJS — Perfuração 8.5 pol em MPD
**Geronimo de Freitas Rolandi há um ano** | v7

De acordo com a sequencia, sobre o comentário do Trajano a respeito do flow check dinâmico, poderíamos fazer essa redução do AP para 9,3 ppg após o relog  (quando já tivermos circulado mais de 1 BU), para evitar dúvidas.

> ↳ **Rafael Czepak Amabile há um ano:** De acordo.

### 7-BUZ-90D-RJS — Perfuração 8.5 pol em MPD
**Ramon Moreira Fernandes há um ano** | v4

Prezados

Confirmar a estratégia de troca de fluido após condicionamento (passo 12 em diante). Exemplo do BUZ-93 foi feito diferente, em linhas gerais: 1) posicionar o camai de sacrifício em poço aberto, 2) avaliar perda com AP equivalente a 150 psi de OB, 3) trocar fluido do poço até 500 m abaixo do BOP, 4) trocar riser com BOP fechado, 5) desinstalar BA, 6) retirar BHA até 500 m abaixo BOP, 6) posicionar tampão viscoso de sustentação, 7) Retirar BHA até BOP e jatear via PBL, 8) voltar com BHA até 500 m abaixo do BOP e deslocar o viscoso até superfície.

### 7-BUZ-90D-RJS — Perfuração 8.5 pol em MPD
**Gustavo Costa Magalhaes Pena há um ano** | v1

Em condições adicionais de segurança operacional:
Incluir as considerações para operação MPD, aos moldes do que foi feito na sequencia de perfuração do BUZ-85.
Mencionar a contingência para MCD a ser tratada em sequencia especifica. 
Configurações de bombas.
Offset de PWD x Broca.
Monitoramento do BA.
Configuração dos dispositivos de segurança MPD.
Fluxograma de controle de poço com MPD.

Item 5:
Existe a possibilidade de seguir perfuração do topo do reservatório em paralelo ao BU do tampão viscoso (remoção do excesso de cimento). 
Geralmente com menos de 1,5 BU (cerca de 6h) já temos um retorno adequado para alinhamento do coriolis.
Durante esse período sem o coriolis o monitoramento do poço seria realizado de forma convencional utilizando tanque ativo e sensor de vazão de retorno da sonda. 
Sem o EKD para detecção antecipada de eventos de anomalia de fluxo: kick e perda.
Sem função de controle de poço com MPD.
Sem possibilidade de circulação de kick pelo sistema MPD.

Item 9:
3º bullet: Aguardar dados de ECD antes de iniciar retirada com circulação para corrigir o MH, se necessário.

Item 11: 
SBP gerando ESD de 9,2 ppg na sapata ou 100 psi acima da PP obtida no pré-teste.

Item 14:
Flowcheck estático com BA instalado.

### 7-BUZ-90D-RJS — Perfuração da fase IV 12,25 x 13,5 com MPD
**Ramon Moreira Fernandes há um ano** | v2

De acordo. Se houver nova revisão, acrescentar no passo 14:
Compartilhar dados do PWD de memória com equipe MPD SLB e CSD MPD para posterior análise de qualidade da manutenção de pressão de fundo.

### 7-BUZ-90D-RJS — Perfuração da fase IV 12,25 x 13,5 com MPD
**Ramon Moreira Fernandes há um ano** | v1

Conforme comentado pela Ivani, a Max Surface Pressure será definida em função do resultado do DLOT/DFIT. Segue gráfico do envelope de controle/circulação de kick com MPD/Sonda deixando indefinido esse valor por enquanto:

### 7-BUZ-90D-RJS — Perfuração da fase IV 12,25 x 13,5 com MPD
**Ivani Tavares de Oliveira há um ano** | v1

Em considerações adicionais de segurança operacional:
BIAS com 50 psi.
Max Surface Pressure: a definir após DLOT.
Verificado diferença do envelope operacional da pág.3 com o envelope da pag. 6.

> ↳ **Tomas de Paiva Cardoso há um ano:** De acordo

### 7-BUZ-94D-RJS — Corte do BPP, bullheading e perfuração 8,5 pol em PMCD dinâm
**Leonardo Mesquita Caetano** | v3

Caros, segue comentários.

- No itens 12. sempre que terminar a vazão nas linhas submarinas for interrompida, fechar imediatamente as respectivas válvulas para evitar linhas vazias (especialmente kill, choque e booster)

- No item 4. adicionar a limpeza do riser com o BOP fechado

- No item 16. Deve-se utilizar uma ROP baixa (iniciar com 3m/h), observando os indícios de boa limpeza para aumentar a taxa gradativamente, sem limite sem indícios de má limpeza.

- itens 27-34: deixar claro que o abastecimento deverá ser mantido abaixo do BOP.

### 7-BUZ-94D-RJS — Corte do BPP, bullheading e perfuração 8,5 pol em PMCD dinâm
**Ramon Moreira Fernandes** | v1

Passo 3: Para avaliação de perda, nesse momento é importante fazê-la sem vazão na coluna, apenas vazão na booster, afim de garantir que não haverá fluxo ascendente no anular revestido.

Passo 11 / bullet 4: Não há necessidade de dividir a sucção das bombs uma vez que tanto no cenário de FMCD como em PMCD dinâmica será usado SAC 8,55 ppg na coluna e no anular.

Passos 19, 22, 24 e 26: abastecer poço pelo anular com vazão 2 x vazão de controle + vazão de retirada de coluna fechada.

### 7-BUZ-95-RJS — [Contingência] Perfuração 8,5 pol em FMCD ou PMCD
**Gustavo Costa Magalhaes Pena** | v1

Prezados, seguem comentários e sugestões.

Em dados básicos, barreiras de segurança: Pelo que consta como Pp min não faz sentido falar de FMCD nesta fase ou SeqOp. Entendo que a contingência seja PMCD, quiçá PMCD dinâmico.
Outra recomendação é que as contingências FMCD e PMCD, quando aplicáveis, sejam separadas em sequencias distintas já que cada técnica possui suas peculiaridades de conversão e monitoramento.

Em segurança:
1º bullet: Em PMCD o poço é monitorado pelos sensores de SPP, PWD, PBOP e SBP. Quando sem circulação no poço, somente PBOP e SBP.
6º bullet: Trip tank vai monitorar a estanqueidade do conjunto BA/RCD.

Em considerações para operação MPD, matriz de perfuração PMCD: O que determina se será PMCD ou FMCD não é só a intensidade da perda, mas também a relação entre pressão de poros da zona de perda e peso de fluido no anular. Pra converter para FMCD a pressão de poros da zona de perda precisa ser inferior a 8,5 ppg.

Em resumo dos alinhamentos, 2º bullet: Em PMCD normal é utilizado LAM no anular.

Em dados das ferramentas LWD, 1º bullet: Mencionar o range utilizando SAC na coluna.

Em perfuração PMCD:
Parâmetros:
5º bullet: A vazão no anular (booster) vai depender se PMCD ou PMCD dinâmico. Atentar que em PMCD dinâmico deve ser utilizada a o dobro da vazão mínima de SAC com coluna apontada na simulação SIP. No caso desta sequencia, recomendo 2-3 bpm (não temos simulação SIP com coluna).
8º bullet: Choke MPD fechado com retorno alinhado para trip tank. Caso seja observado aumento do trip tank, fechar válvula de acionamento remoto a montante do choke para determinar se o vazamento é no BA/RCD ou no Choke MPD.

Sonda, 7º bullet: Para cada cenário de bullheading, mencionar o volume e a vazão.

Rotina e registros, tabela: A segunda coluna é a SBP/PBOP.

Em manobra para troca de broca:
Item c, 4º bullet: 
Se em PMCD normal, bombear LAM no anular para compensar volume de aço + 20% de excesso, e evitar pistoneio.
Se em PMCD dinâmico utilizar uma maior vazão de controle na retirada volume de aço + 20% de excesso, e evitar pistoneio.

Item G: Riser já estará cheio. A partir deste ponto, em caso de PMCD normal, seguir com bullheadings preventivos a cada 6h ou reativos, se necessário.

Item O: Recomenda-se que o teste seja realizado em dinâmica, com booster e Choke MPD, com SBP igual a pressão na linha de kill + 300 psi (aplicar um diferencial de 300 psi de cima para baixo na gaveta cega). Critério de aprovação: variação do trip tank igual ou inferior a 0,25 bbl em 15 min (equivalente a 1 bph).

Item Q: Já realizado no item O.

Item R: Efetuar bullheading de 20 bbl pela kill. Equalizar acima e abaixo da gaveta cega, interromper vazão na booster e observar fechamento do Choke MPD. Preparar alinhamento para monitorar estanqueidade do choke MPD. Abrir BOP. Fechar linha submarina. Prosseguir com manobra.

Item U: Descer ultimas 2-3 seções com circulação SAC pela coluna para evitar plugueamento em fundo falso.

### 7-ITP-7-RJS — [CONTINGÊNCIA] Conversão e Perfuração 8 1/2" em FMCD
**Gustavo Costa Magalhaes Pena** | v1

Em vazões de controle e BH: Ficou faltando mencionar qual será a vazão de controle a ser utilizada na fase. Por padrão: Manter a vazão mínima pelo anular para evitar a migração de gás pelo anular. É importante garantir a vazão de controle da simulação, com fator de segurança de 2, considerando as condições do poço com coluna.
Sugestão:
Vazão de controle: 4-5 bpm (170-210 gpm), constante.
Vazão de BH: 8-10 bpm (340-420 gpm), por pelo menos 40 min.

Esses valores propostos já são adequados para o cenário sem coluna, portanto à favor da segurança.

Em perfuração fase 8 1/2":
Corrigir titulo de PMCD para FMCD.

Itens 1, 2 e 3: Vazão de controle 4-5 bpm com o fluido de perfuração (se for AGMAR, então AGMAR), pela booster.

Item 6, 7º bullet: 1 bph, ou 0,25 bbl em 15 min.

Item 7, 3º bullet: No top down (pelo FS), utilizar a máxima vazão. Após concluir o volume do riser, retornar alinhamento para a booster na máxima vazão.

Itens 8 e 9: Não precisa alinhar para a kill durante a perfuração, pode manter a vazão de controle na booster.

Item 10: 
Fala de booster a 200-300 gpm (2º bullet) e de kill a 8 bpm (em vazões recomendadas). Sugiro manter booster na vazão de controle de 4-5 bpm.
Começar a perfuração com ROP 5 m/h para avaliar comportamento do poço, e ir aumentando ROP gradativamente.
Em caso de manobra para troca de broca,
Aumentar a vazão de controle para compensar a retirada de aço.
Após instalação do SSA, atentar que o teste de pressão trata-se de Hold point CSD MPD.

Item 21: Se estiver utilizando a booster, ajustar alinhamento para linha submarina antes de fechar o BOP.

### 7-JUB-78DA-ESS — Perfuração 8 1/2" com MPD
**Gustavo Costa Magalhaes Pena** | v1

Prezados, seguem comentários.

Nas etapas que tratam sobre manobra com 600 gpm (booster ou circuito de superfície), atentar para que existam bombas de barramentos diferentes.

Em perfuração com MPD:

Item 8.f: Atenção e boa comunicação no fornecimento de FPBA 8,8 ppg para a UC.

Item 8.2.k: Alinhar as bombas de lama que estavam alinhadas para a booster para a coluna de forma que seja possível bombear tampão de manobra, shallow test e abastecimento da coluna.

Item 15: Acredito que da mesma forma que foram detalhadas as alternativas para monitoramento do poço no item 8, no item 15 deve-se tratar da reversão para cada uma.

Se poço monitorado por UC, reestabelecer booster com 600 gpm, pressurizar riser com SBP = UC + 100 psi e monitorar estanqueidade do BA por 15 min, em dinâmica. Após aprovação, abrir BOP e prosseguir com manobra.
Se poço monitorado por circuito de superfície (sem usar UC), pressurizar riser com UC = SBP + 100 psi e monitorar estanqueidade do BA por 5 min, em estática. Após aprovação, equalizar com booster, comunicar riser com BFM, trocar circuito de superfície por booster, abrir o BOP, ajustar alinhamento e prosseguir com manobra.

Item 20: Descer conectado e circulando últimas 2 seções.

### 7-MRO-37-RJS — Perfuração da fase de 8,5 pol com MPD
**Geronimo de Freitas Rolandi há um ano** | v1

Bom dia, fiscais
O fluxograma de influxo foi atualizado no padrão: Padrões, PE-2POC-01113
De resto, excelente sequencia, em especial algumas boas práticas como a de colocar a tabelinha com as SBP's em função da perda e a drenagem abaixo da RCD utilizando o choke da sonda.

### 7-MRO-37-RJS — Perfuração da fase de 8,5 pol com MPD - Corrida #2
**Leonardo Mesquita Caetano há um ano** | v2

Caros, 
de acordo com a sequência, aprovada.

Comentários extras:
Item 5 - Para mim está claro, mas acho prudente especificar sem vazão na coluna:
"Descer coluna até o fundo sem rotação e sem vazão *na coluna* a 3 min/sç."


Item 28. Sugestão de realizar uma despressurização gradual para que seja observado qualquer indicio de vazamento precocemente.

Item 31. Sugestão de avaliar chegada da interface através das propriedades do fluido com o coriolis.

> ↳ **Leonardo Mesquita Caetano há um ano:** Comentei na sequência errada. Ignorar.

### 7-MRO-37-RJS — Perfuração da fase de 8,5 pol com MPD - Corrida #2
**Leonardo Mesquita Caetano há um ano** | v1

De acordo com a sequência.

### 7-STUP-10DA-RJS — Contingência perfuração da fase 8 1/2" com FMCD
**Leonardo Mesquita Caetano há um ano** | v2

ALERTAS E LEMBRETES:

Atentar para que nas interrupções de bomba a coluna ou a booster podem perder nível.
Avaliar regulamente se a perda de volumes nos tanques está compatível com a vazão de bombeio (Risco de cavitação das bombas levando a falta de abatecimento)

item 5: 

"Retirar a vazão da booster, sempre mantendo pelo menos 5 bpm de vazão total (ou 7,5 bpm no caso de retirada de coluna) e fechar válvula submarina de booster." 
Item 16:
Entrar com 2 mud pumps pela linha submarina incrementando até 5 bpm e ao mesmo tempo retirando bombas da booster até zero e fechar válvula submarina de booster.

### 7-STUP-10DA-RJS — Contingência perfuração da fase 8 1/2" com FMCD
**Gustavo Costa Magalhaes Pena há um ano** | v1

Seguem comentários:

Em alertas e lembretes:

Principais pontos operacionais:
7º bullet: Vazão de controle simulada (AGMAR e sem coluna) de 2,5 bpm, e portanto considerar vazão de controle de 5 bpm.
8º bullet: Vazão de recalque simulada (AGMAR e sem coluna) de 10 bpm por 15 min (volume de 150 bbl).
10º bullet: Vazão de recalque 10 bpm / 15 min / 150 bbl.

Limites:
4º bullet: Para aplicar rotações superiores a 150 RPM comunicar CSD MPD.


Em contingência - Perfuração 8,5" em FCMD:

Item 1:
2º bullet: Durante a perfuração é preferível utilizar a booster para manutenção da vazão de controle.
4º bullet: Não existe correlação entre pressão de bombeio da booster e fratura durante a perfuração FMCD (riser ventilado).

Item 2, 3º e 4º bullet: Essas avaliações são feitas previamente à decisão de converter para FMCD, e consequentemente partir para instalar o SSA.

Item 3: 
Incluir: Manter vazão de controle de 5 bpm na booster (AGMAR ou FPBA 8,6 ppg).
6º bullet: Retirar o strippando.
12º bullet: Retirar trecho sobre "manter pressão de vedação dos selos".

Item 4, 4º bullet: Se confirmado que o vazamento se dá pelo selo inferior, efetuar teste dinâmico da câmara da ACD com 250-350 psi por 5 min, monitorando o trip tank.

Item 5: 
Incluir: Antes de registrar as pressões de referência, efetuar recalque de 1,5 x o volume da coluna com SAC a máxima vazão possível.
Incluir: Necessidade de 02 bombas na booster de barramentos diferentes.

Item 6, em caso de perda de injetividade: Observando os sensores SPP, PWD e BOP subindo juntos e verificação de retorno, considerar embuchamento da formação e reestabelecimento da condição overbalance. Avaliar necessidade de:
combate a perda (para aumentar a vazão de retorno e limpeza do poço);
troca de fluido ou manutenção de AGMAR + viscosos (limpeza do poço);
retirada ou manutenção do SSA (perda de carga no anular).

Itens 11 e 12: Manter vazão de pelo menos 5 bpm (coluna + anular). 

Item 17: Enviar relatório de desgaste do SSA para csd.mpd@petrobras.com.br, assim que o documento estiver disponível.

> ↳ **Walleska Monyele Lopes de Almeida há um ano:** De acordo.

### 7-TUP-129D-RJS — Contingencia_ Perfuração 8,5 FMCD
**Leonardo Mesquita Caetano** | v1

Caros, 
Segue pequeno comentário.
Item 4 é Hold Point, informar em vermelho.

### 7-TUP-133-RJS — Conversão e Perfuração 8 1/2 em FMCD
**Ramon Moreira Fernandes** | v1

Preparativos para operação de FMCD:
Se for usar a linha de kill para abastecer o anular (onforme 1º bullet), no 6º bullet/a mantem a injeção de fluido também pela linha de kill. Da mesma forma no 7º bullet a unidade de cimentação entra abastecendo pela linha de kill também.

Vazões de controle e recalque:
Padrão pede fator de segurança de 2 sobe a vazão de controle.

Teste de injetividade Conversão para FMCD:
Para conversão para FMCD não é previsto fazer teste de injetividade. Supõem-se que a perda é total, sem nível na mesa, portanto pode eliminar esta etapa. O teste de injetividade só é necessário em cenário de PMCD ou MCD dinâmico.

Conversão para FMCD:
Cenário inicial: perda total com vazão de perfuração + 2x vazão de controle na linha de kill.
Sequencia de conversão:
Mantem máxima vazão na linha de kill e interrompe vazão na coluna.
Puxa coluna pra cima da região de perda
Alinha SAC para linha de PMCD, inicia top down do anular com SAC a máxima vazão e interrompe vazão na linha de kill.
Alinha SAC para linha de kill, estabelece vazão = 2 x vazão de controle e interrompe vazão na linha de PMCD.
Alinha SAC pra coluna e estabelece vazão de perfuração.
Ponto de atenção: controlar vazão do anular não somente pela estrocagem das bombas, mas também no físico (nível dos tanques).

Perfuração em modo FMCD:
Vazão mínima no anular = 2 x vazão de controle

Contingências diversas / Vazamento do Seal Assembly:
O vazamento do SSA em cenário de FMCD ocorre de cima pra baixo. Como medida pode ajustar a pressão nos elementos LACD e UACD. Importante apenas deixar o riser acima do ACD cheio. Se necessário abastecer acima da ACD via linha de bleed/topfill do standpipe.

Em caso de manobra para troca de BHA:
Considerar vazão de abastecimento no anular = 2 x vazão de controle + vazão de retirada de coluna cheia (igual ao passo 6 - retirada do BHA).

### 7-TUP-133-RJS — Perfuração fase IV com BHA 8 1/2" em MPD
**Ramon Moreira Fernandes** | v4

Sugestão: Mantém flowcheck dinâmico somento com booster e choke todo aberto ao final da perfuração (passo 4) e faz o o flowcheck estático somente antes de desinstalar o SSA (inverte passo 5 com passo 6).

> ↳ **Raoni Novais Carvalho Brasileiro:** Alterado momento do flow check estático na V05 conforme solicitação.

### 7-TUP-133-RJS — Perfuração fase IV com BHA 8 1/2" em MPD
**Ramon Moreira Fernandes** | v3

Adicionar o P&ID simplificado do sistema de desvio de fluxo MPD da sonda.

Passo 6: sugiro manter o mesmo AP do final da perfuração (sem necessidade de aumentar 100 psi).

Passo 7: está descrito 2 formas de comunicar a contrapressão de superfície para o poço durante a ciclagem do BOP: 1) bypassando os elementos que serão ciclados, 2) alinhando circuito de superfície para linha de kill abaixo da LPR. Sugiro usar apenas a segunda opção. Requer cuidado de equalização das válvulas antes de interligar o buffer com o choke da sonda e antes de abrir as FSVs da linha de kill, exemplo de passo a passo:
Alinha unidade de cimentação para choke, linha de kill e linha que interliga choke ao buffer.
Pressuriza unidade de cimentação com valor de SBP para equalizar GV1 e FSVs de kill abaixo da LPR.
Abre GV1 e FSVs. A partir daí temos o circuito de superfície interligado ao poço tanto pelo riser quanto pela linha de kill abaixo da LPR.

Passo 8, 9 e 10: No amortecimento do poço temos sugerido a boa prática de usar a linha de PMCD circulando em circuito de superfície enquanto troca-se o fluido das linhas submarinas (kill, choke e booster) e enquanto troca-se o fluido do poço até acima do BOP. Sugiro restruturar a sequência da seguinte forma:
Preenche o poço aberto com FCBA 8,9 ppg (490 bbl)
Retira BHA até acima da sapata circulando apenas pela booster (fazer simulação de swab e aplicar SBP para compensar)
Efetua flowcheck dinâmico circulando apenas pela booster com AP equivalente ao ESD após final da troca (150 psi de overbalance com FC) e avalia estratégia de combate a perda (se necessário).
Alinha STP2->PMCD->BM (comunicado para flowspool), estabelece circulação pela linha de PMCD com fluido leve e interrompe bombeio pela booster.
Troca fluido das linha de kill, mantendo circulação no circuito de superfície com fluido leve pela linha de PMCD
Troca fluido do poço revestido até X m acima do BOP, mantendo AP final da perfuração, mantendo circulação no circuito de superfície com fluido leve pela linha de PMCD.
Alinha unidade de cimentação para linha de kill (linha de kill já com fluido 8,9 ppg) e comunica com poço.
Fecha BOP (mantendo monitoramento do poço com unidade de cimentação - ~50 psi).
Troca fluido do riser.

Passo 19: após desinstalar o SSA trocar o trip tank e fluido acima do ACD por fluido de completação.

Anexo V - Manobra para troca de broca
Passo 3: pode simplificar um pouco a redação: retirar BHA compensando swab ajustando a contrapressão de acordo com a simulação dos químicos/MPD. Se aumentar ou induzir a perda para formação, avaliar retirar com circulação até acima do revestimento de menor ID e prosseguir sem circulação pela coluna compensando swab menor.

Passo 3 / bullet 4: essa recomendação é pertinente porém não apenas para essa etapa. Pode colocá-la nas recomendações gerais ou na etapa de perfuração (passo 2 da sequência principal)

Passo 5 / item e): Não entendi a frase "Em caso de perda elevada avaliar a despressurização do riser via SSA (fluido do poço limpo)". Nesse item cabe avaliar a transição do controle e monitoramento do poço para o circuito de superfície MPD. Sugiro adicionar um passo de contingência descrevendo a transição de monitoramento do poço da Unidade de Cimentação para o Circuito de Superfície (pode ser feito em paralelo à desinstalação do SSA ou à retirada do BHA no riser).
Obs: a recomendação geral para monitoramento do poço em MPD com BHA acima do BOP é:
Em cenário sem perdas (ou perdas baixas): monitoramento com unidade de cimentação.
Em cenário de perdas elevadas: usar circuito de superfície MPD alinhado para linha submarina.

### 7-TUP-133-RJS — Perfuração fase IV com BHA 8 1/2" em MPD
**Leonardo Mesquita Caetano** | v2

Caros, bom dia.

Item 5. "a) Alinhar linha de 2” do ACD para choke manifold -> MGS. Aumentar pressão de acionamento do upper ACD para evitar vazamentos"

Item 7. 
DE: "Efetuar by-pass do BOP pelas linhas submarinas. By-passar UA também com as mangueiras MPD." 
PARA: "Manter pressão no poço através do circuito de superfície com alinhamento pela linha de kill abaixo da LPR"



O "AMORTECIMENTO / TROCA DO FLUIDO DO POÇO POR FCB" pode ser feito mantendo o circuito de superfície com alinhamento pra as mangueiras do flowspool. 

Vantagens: deixar a troca das linhas auxiliares mais simples e evitar momentos só com coluna (risco de queda de bomba)

Caso seja considerado a manutenção da pressão do poço pelo circuito de superfície, mudar: 
Item 8. "Manter pressão no poço através do circuito de superfície com alinhamento pelas mangueiras do flowspool".
Daí pode-se substituir o fluido da booster aqui também.

### 7-TUP-133-RJS — Perfuração fase IV com BHA 8 1/2" em MPD
**Ramon Moreira Fernandes** | v1

Mais um ponto: após amortecer o poço com fluido salino (sem reologia), retira o BHA até a sapata e já desinstala o SSA. Só mantém o SSA instalado caso siga em operação de MCD.

### 7-TUP-133-RJS — Perfuração fase IV com BHA 8 1/2" em MPD
**Ramon Moreira Fernandes** | v1

Prezados

Reforçando o que já foi comentado anteriormente e reformulando um pouco o texto:


OBSERVAÇÕES PARA OPERAÇÃO COM MPD
III - Monitorar funcionamento e integridade do SSA:
a) O SSA deverá ser lubrificado em circuito fechado: Riser FLuid Trip Tank -> LubSkid -> ACD -> Riser Fluid Trip Tank.
b) Não é aceitável conviver com vazamento no SSA no sentido poço->superfície. Atentar para correta pressurização da câmara do ACD (pressão superior à pressão do poço).
c) É normal conviver com pequeno vazamento de cima pra baixo no selo inferior  do SSA (LACD) na ordem de 2 gpm.

Item 7: Para cenário MPD SBP, prever amortecimento com peso de fluido que garanta um overbalance de pelo menos 150 psi. Para cenário de MCD, a perfuração será finalizada e seguida de uma completação em MCD (sem amortecimento).

### 7-TUP-133-RJS — Perfuração fase IV com BHA 8 1/2" em MPD
**Geronimo de Freitas Rolandi** | v1

OBSERVAÇÕES PARA OPERAÇÃO COM MPD
III - Recomendação Operacional: Monitorar funcionamento do seal sleeve assembly (SSA) pelo riser trip tank (DGD).
PRINCÍPIO:
Pressão do Lub Skid > SBP.
OPERAÇÃO NORMAL:
Nível do DGD caindo = Injeção no poço.
Ação: Insira esta taxa como Ganho no MPD
ALERTA DE FALHA:
Nível do DGD subindo (> 1 bbl/h) = Vazamento do poço para superfície.
Ação: Verifique a integridade da vedação, aumentado a pressão de fechamento para manter a pressão do LubSkid > SBP

### 8-BUZ-89D-RJS — Perfuração 8,5 pol e manobra em MPD
**Ramon Moreira Fernandes** | v1

Passo 4 / h: Iniciar com modo AP na sapata 10 3/4" com equivalente de 9,2 ppg.

Passo 8 /c: [...] retirada da coluna em poço revestido

Passo 21: Testar estanqueidade do BA, circulando pela booster a 600 gpm, aplicando contrapressão de SBP de conexão + 300 psi e monitorando o trip tank.

Passo 21 / a: critério de aprovação 0,25 bbl/15min.

> ↳ **Matheus Marins Gonzaga:** Obrigado pelos comentários, Ramon,

Sobre o passo 4/h), realmente ficaram informações divergentes sobre o AP definido para a perfuração. O AP será 8,8 ppg, com ECD esperado de 9,2 ppg durante o início da perfuração, mesmo com choke aberto. Informação já corrigida na versão 2.
Demais comentários implementados.

### 8-BUZ-89D-RJS — [Contingência] Perfuração 8,5 pol em F/PMCD
**Leonardo Mesquita Caetano** | v5

De acordo com a SeqOP.

Comentário para nota da atualização (em azul):
O Fluxo cruzado é uma possibilidade constante na operação.

### 8-BUZ-89D-RJS — [Contingência] Perfuração 8,5 pol em F/PMCD
**Geronimo de Freitas Rolandi** | v3

Em dados da simulação (SIP) para PMCD/FMCD.
Para simplificar as vazões de controle e bullhead com ou sem coluna no poço: 
Bullhead  = 12 bpm
Controle =  4 bpm
Ajustar demais itens (4a, 10b iv, 10 Conexão l, 13, 32 c, 33a)
A manobra em PMCD dinâmico deve sim ser com vazão de controle continua, pois como o fluido AGMAR não possui viscosidade a velocidade de migração é muito rápida, 46 min até ao riser, pela simulação, (item 32, ajustar somente vazão 6,5 bpm). Já os bulheads preventivos de 60 bbl, em PMCD dinâmico, não são necessários (10 Fluidos g, 38 d, 42, 44, 45)

> ↳ **Marcus Vinicius Duarte Ferreira:** Gerônimo, bom dia.

Agradeço os comentários.
Efetuada revisão conforme conversa pelo Teams.

> ↳ **Eduardo Oliveira de Barros:** Blz Marcus, não sei se vamos cair nesse cenário, então nem adianta estressar tanto a discussão agora. Mas basicamente FCMD e PMCD dinâmico (fluido no anular = SAC) a gente mantém bombeio contínuo. PMCD tradicional (fluido no anular = LAM), não tem bombeio contínuo e sim BH rotineiros preventivos. Depois o Gerônimo confirma isso.

### 8-BUZ-89D-RJS — [Contingência] Perfuração 8,5 pol em F/PMCD
**Fábio Koiti Dairiki** | v2

No item CONSIDERAÇÕES PARA OPERAÇÃO MPD (Hall) Dados da simulação (SIP) para PMCD/FMCD, considerar margem de segurança (dobro da vazão) apenas para a vazão de controle. Para vazão de bullhead, usar os valores da simulação.

### 8-BUZ-96D-RJS — Perfuração 8,5 pol e manobra em MPD
**Ramon Moreira Fernandes** | v3

Passo 3: manter Coriolis e Choke MPD by-passados.

Passo 4/MPD:
Iniciar perfuração com sistema MPD by-passado limitado a 100 m de fase.
Alinhar retorno para sistema MPD após confirmar que não há excesso de cimento retornando nas peneiras.
Obs: Enquanto o Coriolis estiver em by-pass evento de ganho ou perda só poderá ser detectado pelo sistema da sonda.

> ↳ **Ramon Moreira Fernandes:** Desconsiderar comentário. Passo 3 já contempla a perfuração dos 100 m iniciais.

### 8-BUZ-96D-RJS — Perfuração 8,5 pol e manobra em MPD
**Gustavo Costa Magalhaes Pena** | v1

Seguem comentários:

Item 3: Não ficou claro pra mim qual a opção iremos seguir:

a) Circular o viscoso até limpeza com o bloco parado. Quando o retorno estiver adequado para o coriolis, alinhar sistema MPD e iniciar perfuração da fase em modo convencional.

b) Bombear viscoso e iniciar perfuração da fase com o sistema MPD by-passado. Quando o retorno estiver adequado para o coriolis, alinhar sistema MPD e retomar perfuração da fase com AP 9,21 ppg na sapata.

Entendo que seja possível adotar ambas as estratégias. A opção a) é conservadora e toma mais tempo, mas permite que o MPD esteja 100% disponível no trecho inicial da fase. Já a opção b) é mais ousada na medida que não teremos o MPD disponível por pelo menos 1,5 BU (5 a 6h de perfuração em modo convencional).

Item 4: Na sequencia está dizendo para utilizar 200 gpm na booster durante a perfuração e aumentar na conexão. Recomendo que seja utilizada a mesma configuração prevista no fingerprint: booster com 400 gpm para perfuração e conexão.

Item 13: 600 gpm.

Item 14: Não vejo necessidade de efetuar flow check de 15 min antes de retirar o BA (somente em caso de ter circulado kick pelo sistema MPD).

Item 20: Retornar com a UC monitorando o poço pela linha submarina, e voltar alinhamento do MPD para o riser.

Item 21: Após instalar o BA será necessário realizar o teste de estanqueidade do mesmo no critério Hold Point, com booster a 600 gpm e monitorando o trip tank. Uma vez com o teste aprovado, abrir o BOP, fechar submarina e liberar UC.

> ↳ **Gustavo Costa Magalhaes Pena:** no comentário do item 3a, considerar no trecho final "iniciar perfuração em modo AP 9,21 ppg."

### 8-MRO-36-RJS — Perfuraçao fase 8,5 em MPD (3a corrida)
**Gustavo Costa Magalhaes Pena** | v1

De acordo. 

Itens 6, 10, 11 e 13: Atentar que a vazão da booster para manobra é de 600 gpm, com 02 bombas de barramentos diferentes.

### 8-MRO-36-RJS — Perfuraçao fase 8,5 em MPD (4a corrida)
**Ivani Tavares de Oliveira** | v2

Item 14. Em caso de manobra para troca de BHA:
Critério de aceitação: 0,25 bbl / 15 min (1 bph).

### 8-MRO-36-RJS — Perfuraçao fase 8,5 em MPD (4a corrida)
**Ivani Tavares de Oliveira** | v1

item 7. acrescentar um bullet (após critério de aceitação):
Drenar os 300 psi usado para o teste.
Prosseguir após estabilização do sistema.

### 8-MRO-36-RJS — Perfuraçao fase 8,5 em MPD (4a corrida)
**Geronimo de Freitas Rolandi** | v1

Item 5. A vazão de perda agora está em 1,4 bpm, avaliar qual é a vazão de perda antes de entrar com a cimentação, caso se decida utilizar a UC prosseder conforme abaixo:
Ainda mantendo a pressão do poço pela linha de choke via circuito de superfície:
Alinhar unidade de cimentação via linha de kill até válvula submarina interna
Pressurizar com UC até a SBP lida no sistema MPD
Abrir válvula submarina interna e começar a bombear com 1,4 bpm (o TTV deverá ficar sem ganho);
Fechar linha submarina de choke 
Manter bombeio com UC mantendo a pressão entre 600 e 900 psi

Alternativamente, para evitar ter que controlar a pressão do poço com a unidade de cimentação em um cenário com perdas, minha sugestão é: 
Utilizando a UC, equalizar o riser com o poço; aplicando SBP (aproveita e já faz o teste)
Abrir as válvulas do queixo duro comunicando o riser com o circuito de superfície;
Entrar com as bombas na booster e retirar as bombas da linha de PMCD gradualmente;
Abrir o BOP, fechar linhas submarinas e isolar o choke manifold.

> ↳ **Geronimo de Freitas Rolandi:** proceder!!

### 8-MRO-36-RJS — Perfuração 12 1/4" x 13 1/2" em MPD (debug)
**Gustavo Costa Magalhaes Pena** | v1

Seguem comentários:

Sobre o ajuste do SPL durante a perfuração da fase. Conforme mencionado em informações gerais e preparativos MPD, o ajuste do SPL será realizado após a conclusão do Microfrac. Portanto, sugiro retirar a informação de SPL igual a 1500 psi da figura da página 6.

Risco de influxo de água no sal durante a perfuração da fase. Conforme mencionado na APR, equipe deverá ficar atenta para o risco de influxo no sal, apesar de estar em fase Debug, e em teoria, com fluido estaticamente OB.

Risco de PMCD. Em perfuração, na parte de perda de circulação é mencionado o risco de PMCD. Acho difícil um cenário e PMCD nesta fase (já tivemos PMCD em fases intermediárias, mas ocorreram em ígneas e não no sal).

Item 4: 
Sobre momento de retirada do SSA. Entendo que temos 02 opções, e que devemos optar por uma delas levando em consideração o contexto da perfuração e também da condição de heave:
1) Retirar SSA com broca dentro do trecho alargado.
Vantagem de manobrar sem SSA e sem restrição de velocidade já no início da manobra. Retira 3 a 4 seções com SSA e SBP (se necessário) e desce SSART.
2) Retirar SSA com broca dentro do revestimento.
Vantagem de ter o SSA disponível para aplicação de SBP em caso de dificuldade de retirada do BHA no trecho não alargado, entre 3741 e 4542 m.

Se manobrar sem SBP, manter riser alinhado para o trip tank.
Se manobrar com SBP, manter booster a 600 gpm e sistema MPD alinhado.

### 8-MRO-36-RJS — S11 - Perfuração fase 8 1/2" em MPD
**Ramon Moreira Fernandes** | v2

Conforme conversado com a fiscalização, os comentários que fiz na v2 serão inclusos na sequência de manobra. Portanto estou aprovando a v2 desta seqop.

### 8-MRO-36-RJS — S11 - Perfuração fase 8 1/2" em MPD
**Ramon Moreira Fernandes** | v2

Passo 2 / contingências diversas / vazamento da Seal Assembly / 3º bullet: Após instalar novo SSA mantendo contrapressão baixo do DSIT, será feito teste do SSA via linha de 2" entre selos com máxima SBP. Esse teste é Holdpoint MPD (critério de aceitação igual ao teste de alta). Em seguida equaliza a câmara entre SSA e DSIT e abre o DSIT.

Passo 2 / Em caso de manobra para troca de BHA / 4º bullet: Essa etapa é Holdpoint MPD.
Ao invés de "Estanqueidade de vazamento" melhor colocar critério de aceitação: ganho máximo de 0,1 bbl/5min na linha de tendência do trip tank.

Passo 15 / 7º bullet: Essa etapa tbm será Holdpoint (critério de aceitação via trip tank 0,1 bbl / 5 min).

### 8-MRO-36-RJS — S11 - Perfuração fase 8 1/2" em MPD
**Ramon Moreira Fernandes** | v1

Observações para operação MPD / Passo III: O título da figura 1 está com as cores invertidas: linha amarela é a sucção e descarga enquanto que a linha verde é o retorno.

Perfuração fase 8 1/2" / passo 2 / parâmetros / 4º bullet:
De acordo com a estratégia de AP na broca até 5562 m e em seguida AP @ 5662 m até TD. Segue perfil de pressão estimado (a confirmar com simulação via software MPD Halliburton):

Perfuração fase 8 1/2" / passo 2 / Em caso de manobra para troca do BHA / 4º bullet: testar SSA com circulação no riser e contrapressão de SBP de conexão máxima prevista.

Passo 7: detalhar procedimento de retirada de gás trapeado abaixo do SSA. Sugestão: Alinhar linha de 2” do ACD para choke manifold -> MGS e abrir progressivamente o choke hidráulico até observar redução de 200 gpm no flowout (coriolis).

Passo 13 / 1º bullet: registrar desgaste nos elementos de vedação do SSA.

Passo 15 / 7º bullet: Ao retornar ao poço em modo MPD, instalar SSA com elementos de vedação novos.

### 8-MRO-36-RJS — S12 - Perfuração fase 8 1/2" em MPD (2a corrida)
**Gustavo Costa Magalhaes Pena** | v1

Seguem comentários:

Item 1, 3º bullet: Como estamos em modo SBP, se ocorrer alguma falha com despressurização abaixo da pressão de poros, iremos avaliar a melhor opção: 
a) aguardar descida do BHA para circulação e condicionamento do poço com MPD ou BOP (a depender do volume estimado de kick).
b) forçar um recalque, considerando as recomendações do CSD SIP.

Item 5: Detalhar procedimento do teste do SSA e seu critério de aprovação. Sugestão abaixo:
Instalação do SSA. Poço aberto porém com o BOP fechado (gaveta cega), e unidade de cimentação monitorando poço pela linha submarina com Puc. Acionar packers da ACD. Pressurizar câmara da ACD com lub skid. Pressurização do riser contra a gaveta cega, em dinâmica (booster) usando o choke MPD, com SBP, sendo SBP = Puc + 300. Monitoramento do trip tank ou outro tanque de monitoramento em circuito fechado. Critério de aprovação proposto: Variação inferior a 1 bph ou ganho máximo de 0,25 bbl em um período de observação de 15 min.

Se acatada sugestão, atentar que após a conclusão do teste já estaremos com alinhamento de manobra com SBP, prontos para o item 8.

Itens 12 e 13: Monitorar o primeiro BU, pois é comum a ocorrência de falso kick causado por ar de abastecimento (variação do ativo sem detecção pelo sistema MPD).

Item 13, em manobra para troca de BHA, 4º bullet: Avaliar replicar a sugestão apresentada para o item 5.

### 8-MRO-36-RJS — S13a - (CONTINGÊNCIA) Conversão de perfuração 8 ½” para PMCD
**Gustavo Costa Magalhaes Pena** | v2

De acordo, somente uma ressalva para o caso de nova revisão:

Em procedimentos para operação em PMCD,
Item E-b: Manter 60 bbl de volume e utilizar a mesma vazão estabelecida no bullheading, no caso 8 bpm.

Ajustar vazões e volumes também no item 12 que trata sobre perfuração.

### 8-MRO-36-RJS — S13a - (CONTINGÊNCIA) Conversão de perfuração 8 ½” para PMCD
**Gustavo Costa Magalhaes Pena** | v1

Seguem comentários:

Em dados do poço, inserir a pressão de poros tomada em pré-teste:  5273m (ponto do teste), com pressão da formação 7916,3 psi. Pp = 8,81 ppg.

Sobre influxo com sistema MPD, por se tratar de uma SeqOp contingencial para PMCD, considerar que que a modalidade de controle de poço será bullheading. Não se aplica o fluxograma de controle e circulação.

Em operações paralelas, estão instruções importantes para o MPD. Sugiro mudar de operações paralelas para Detalhes operando em PMCD.
No 2º bullet, inserir que o trip tank deverá monitorar a estanqueidade do choke MPD. Importante confirmar com a sonda se o trip tank será capaz de monitorar uma vez que temos a questão do DGD nesta sonda.
Em vazões recomendadas, por estarmos com FPBA 8,6 ppg ao invés de FPBA 9,4 ppg simulado no MRO-37 (utilizado de referência), e por se tratar de um poço injetor, entendo que temos 02 opções:
Prosseguir com FPBA 8,6 ppg no anular, e avaliar ser mais conservador no que diz respeito ao volume e vazão de bullheading com e sem coluna. Recomendo que as vazões tanto preventiva, quanto reativa sejam superior a 7 bpm, com coluna. Já o volume de bulheading reativo poderíamos arredondar para 300 bbl.
Ou partir para um PMCD dinâmico com injeção continua de AGMAR no anular (hidrostática bem próxima do FPBA, porém com autonomia infinita e monitoramento mais simples - vazão de controle continua no anular). A vazão de controle precisaríamos verificar com o SIP, mas acho que 3-5 bpm de AGMAR com coluna e 6-10 bpm de AGMAR sem coluna nos atenderia.

Em teste de injetividade, item 5: corrigir o número de bombas de lama.

Em conversão para PMCD, 2º bullet: Deixar o SBP setado em 750 psi.

Em perfuração em modo PMCD, bullheading:
1º bullet: Utilizar a mesma vazão de bullheading.
2º bullet: Deve ser analisada a diferença entre os Deltas de SBP e SPP (anular limpo x anular atual).

Em perfuração em modo PMCD, sonda/MPD:
2º, 3º bullet: O fechamento da válvula do BFM visa tentar identificar se o ganho no TT é devido vazamento do SSA ou choke MPD. Como nesta sonda o SSA é monitorado no DGD, não existe necessidade de investigar. Se TT subir é pq o choke MPD está vazando.
4º bullet: É SSA.

Em contingência para manobra para troca: ajustar as vazões de bullheading.
No item 16, 5º bullet: Em caso de suspeita de HC migrando no anular interromper a manobra e realizar bullheading (não precisa considerar reposição de aço neste momento).
No item 18: a retirada será realizada em modo PMCD, com SP SBP 750 psi, e não modo AP.

### 8-MRO-36-RJS — S15 - Perfuraçao fase 8,5 em MPD (5a corrida)
**Ramon Moreira Fernandes** | v1

Passo 12: De acordo com estratégia de seguir com AP 9,3 ppg na broca até passar pelo próximo trecho de ígneas e realizar uma tomada de pressão.
Se confirmar pressão de poros abaixo de 9,0 ppg na próxima tomada de pressão (abaixo das ígneas), temos 2 estratégias possíveis para o AP:
AP 9,15 ppg na sapata - segue gráfico de ECD x ESD esperado:

AP 9,15 ppg na base das ígenas (por volta de 5791 m) - segue gráfico de ECD x ESD esperado:

Passo 19: em caso de perda elevada, é preferível manter o monitoramento do poço com MPD via circuito de superfície. Para isso após após despressurização do riser, efetuar transição de monitoramento do poço pela UC para circuito de superfície.

### 9-BUZ-103D-RJS — 20 - Perfuração 12 1/4" x 13 1/2" com MPD
**Leonardo Mesquita Caetano** | v1

De acordo.

Em: "Limite eqptos dinâmico / SPL: a definir"
-Usar valores tradicionais: 1700 psi para as PRVs do poço; 
-2400 psi para PRVs do Buffer-Stand Pipe e Buffer-Choke/;
-SPL conforme limite de fratura

### 9-BUZ-103DA-RJS — Sidetrack e perfuração 12,25 x 13,5
**Leonardo Mesquita Caetano** | v1

5) realizar calibração do PID e eficiência de bomba do MPD nos primeiros metros perfurados.

### 9-BUZ-103DA-RJS — Sidetrack e perfuração 12,25 x 13,5 - 2ª tentativa
**Ivani Tavares de Oliveira** | v2

De acordo.
Só faltou uma observação: Toda instalação do SSA é obrigatório teste Hold Point, conforme padrão PE-1PBR-00486, anexo B, 4.18. Critério de aceitação:

### 9-BUZ-103DA-RJS — Sidetrack e perfuração 12,25 x 13,5 - 2ª tentativa
**Gustavo Costa Magalhaes Pena** | v1

Seguem comentários e sugestões:

O entendimento é de que iremos utilizar o sistema MPD no início do sidetrack. Portanto recomendo inserir a partir do item 4:
O momento que o choke MPD será alinhado,
Qual o AP que será utilizado (setpoint e profundidade).
Quando o coriolis será alinhado para monitorar vazão de retorno.
Retorno sem excesso de cimento nas peneiras
Pelo menos 1,5 BU após concluir corte de cimento 
Avaliar necessidade de tampão viscoso.

No item 10, confirma com a sonda se eles manobram com SSA instalado e packers da ACD despressurizados.

> ↳ **Matheus Marins Gonzaga:** Obrigado pelos comentários, Pena,

Colocaremos as recomendações do choke MPD e Coriolis na v2. Quanto à manobra com packers despressurizados, a sonda faz essa operação, inclusive já fizemos na retirada anterior. A restrição seria apenas circular com os ACD despressurizados. Vamos inserir também essa observação na v2.

### 9-MLL-95A-RJS — Perfuração fase 8 1/2" - FMCD contingencial
**Gustavo Costa Magalhaes Pena** | v1

Seguem comentários:

Em informações preliminares:
3º bullet: Importante mencionar todas as vazões de controle de poço. As vazões de controle com, e sem coluna, e vazão e volume de de bullheading.
6º bullet: Se o sistema foi testado com 300 psi, então as PRVs devem ficar setadas para abertura com 200 psi.

Em contingência FMCD:
Item 8a): Manter vazão na booster independente se SAC ou FPBA. Tentar aumentar vazão na booster para ver se é possível obter nível na MR.
Item 11: Verificar funcional das PRVs em paralelo, durante a montagem e descida do BHA.
Antes do item 13: Deve ser realizada a troca de fluido do anular por SAC via bulheading. Depois com o poço todo com SAC, ajustar as vazões de perfuração e controle e registrar as pressões. Dai então partir para a perfuração (acho que é o item 15 que esta fora de posição).
Item 13, em fluidos, 3º bullet: As vazões de controle com coluna e sem coluna são diferentes.
Item 14: 3x o volume.

> ↳ **Fernando Fonseca Kogik:** bom dia!

Na simulação que tenho do SIP, ambas as vazões de controle (com e sem coluna no poço) são com 4 bpm


O restante dos comentários estará na v2
