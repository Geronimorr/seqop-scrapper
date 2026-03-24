# Contingência / FMCD / PMCD

21 SEQOPs | 30 comentários MPD

## Análise IA dos Comentários

```json
{
  "sub_tipos": [
    "Combate à perda com LCM via PBL",
    "Combate à perda com Well Defend",
    "Combate à perda com cimento por injeção direta",
    "Conversão para perfuração em PMCD",
    "Instalação de cauda PACI em FMCD",
    "Treinamento FMCD"
  ],
  "pontos_verificacao": [
    {
      "item": "Monitoramento do AP (Annular Pressure) durante toda a operação",
      "frequencia": "alta",
      "exemplo_real": "Item 6. O AP deverá ser monitorado pelos dados do PWD enquanto disponíveis."
    },
    {
      "item": "Compensação de perda de carga no modelo hidráulico",
      "frequencia": "alta",
      "exemplo_real": "Adicionar tabela do MPD SLB para compensar o valor da perda de carga no modelo hidráulico."
    },
    {
      "item": "Realização de testes de estanqueidade do BA (BOP Anular)",
      "frequencia": "alta",
      "exemplo_real": "Item 3: Incluir procedimento de teste Hold Point do BA com 300 psi por 5 min contra o DSIT."
    },
    {
      "item": "Verificação de vazamentos no SSA/ACD e ajuste de pressão dos packers",
      "frequencia": "média",
      "exemplo_real": "Monitorar vazamento do SSA/ACD de cima para baixo (esse vazamento se soma à vazão de controle no anular)."
    },
    {
      "item": "Simulação de vazões e recalques preventivos para quebra de gel",
      "frequencia": "média",
      "exemplo_real": "Recalques periódicos para quebra de gel: Deslocar 60 bbl de Fluido FPBA Polimérico 8,7 ppg (LAM) a cada 6 h pelo anular."
    },
    {
      "item": "Manutenção da lubrificação do BA durante operações",
      "frequencia": "alta",
      "exemplo_real": "Manter firme a lubrificação do BA utilizando uma bomba de lama alinhada para a fill-up diverter com 0,5-1,0 bpm."
    },
    {
      "item": "Verificação de alinhamentos de bombas e válvulas durante descidas e manobras",
      "frequencia": "alta",
      "exemplo_real": "Manter desde o início o alinhamento para evitar que as bombas de pré-carrega superem as bombas de ataque ao poço."
    }
  ],
  "erros_frequentes": [
    "Falta de monitoramento adequado do AP durante a operação",
    "Omissão de simulações específicas para cenários de PMCD",
    "Duplicidade de itens em procedimentos (exemplo: bactericida duplicado)",
    "Falhas na descrição de volumes e vazões de controle",
    "Ausência de testes de estanqueidade do BA em momentos críticos",
    "Desalinhamento de bombas e válvulas durante operações"
  ],
  "padroes_aprovacao": [
    "Utilização de tabelas e simulações para compensação de perda de carga",
    "Realização de testes Hold Point com acompanhamento do CSD MPD",
    "Manutenção de vazão de controle durante toda a operação",
    "Monitoramento contínuo de vazamentos e ajustes de pressão em equipamentos críticos",
    "Detalhamento claro de procedimentos e alinhamentos de bombas e válvulas"
  ],
  "normas_aplicaveis": [
    "PE-2POC-01113",
    "API RP 92M",
    "API RP 92P"
  ]
}
```

## Comentários MPD Completos

### 1-RJS-763D — 29a - Combate a perda com LCM via PBL
**Leonardo Mesquita Caetano** | v1

Caros, segue comentários.

Recomendo usar o valor de 2 vezes a vazão de controle se for optado por esse método.

Item 6. O AP deverá ser monitorado pelos dados do PWD enquanto disponíveis 
a) Qual seria o AP (AP > 9,026 ppg @ Topo do Reservatório SUPERIOR)?
O valor do AP deverá ser monitorado pelo PWD, enquanto disponível.
Adicionar tabela do MPD SLB para compensar o valor da perda de carga no modelo hidráulico 


Item 8. O MPD deverá compensar a perda de carga considerando a circulação pela PBL e não pela broca.

item 18. b) o incremento de SBP deve partir do AP inicial mais 100 psi (não ficou claro que estamos falando do delta_p)

> ↳ **Leonardo Mesquita Caetano:** Caros, 
 em caso de perda total, usar o valor inicialmente proposto de 2 bpm para controle. 
Em caso de perda total, anotar as pressões de referencia no BOP e SBP para monitoramento.

> ↳ **Ramon Sena Barretto:** Conforme conversamos, o valor do AP ficou em aberto, poderá ser ajustado conforme andamento da perfuração.

Comentários do item 6 inseridos no item 8, pois para lançamento da esfera, quebramos conexão da coluna e interrompemos vazão pela coluna.

Tabela com simulação SLB inserida nas recomendações de MPD conforme alinhado.

### 1-RJS-763D — [CONTINGÊNCIA] Combate à perda com LCM via PBL _ com sistema
**Geronimo de Freitas Rolandi** | v2

Mantenho os comentários do Gustavo Pena, lembrando que antes de fazer stripping pelo BOP submarino, como teremos o BA instalado, poderíamos contar com essa barreira para migração de gás para a mesa rotativa.

> ↳ **Geronimo de Freitas Rolandi:** Lembrando que não temos simulação de controle ou bulhead pra essa fase

### 1-RJS-763D — [CONTINGÊNCIA] Combate à perda com LCM via PBL _ com sistema
**Gustavo Costa Magalhaes Pena** | v1

Prezados, entendo que o papel do MPD nesta sequencia operacional seja o de impactar o mínimo possível na avaliação e no combate a perda, uma vez que estamos com fluido estaticamente OB e sem sal exposto (fluência).

Sendo assim, temos as seguintes ações:

Abertura do choke MPD (redução da pressão no poço).
Redução ou retirada da vazão na coluna (reduzir fricção no anular).
Se necessário circular com o menor impacto do MPD (ainda com o BA instalado), existe a possibilidade de by-passar o sistema MPD no BFM. Atentar que nesta condição não teremos o Coriolis monitorando o poço.

Outra questão é em relação à vazão de controle de 2 bpm para uma fase de 16". Entendo ser somente para manter o poço abastecido, uma vez que o potencial IPF que temos é de água (-3553 m) - Vazão de controle sem compromisso de conter migração de HC.

> ↳ **Gustavo Costa Magalhaes Pena:** Após concluir o combate a perda, avaliar possibilidade de retomar o Debug do MPD.

### 3-RJS-762 — 11a - [CONTINGÊNCIA] Combate à perda com LCM via Well Defend
**Ramon Moreira Fernandes** | v1

Prezados

Passo 2 / b: Em cenários de perda severa, reduz-se SBP até OB mínimo de 50 psi e avalia-se entre combate a perda ou conversão para PMCD. Combate com cimento somente se o combate com LCM não for efetivo e se a conversão para PMCD não for viável (pressões muito alta no teste de injetividade).

Não vejo necessidade de fechar o choke totalmente e manter 2 bpm na booster enquanto prepara-se para o combate a perda. Isso seria equivalente a conviver com perda de 120 bph. Só é necessário manter vazão de controle em caso de FMCD (sem nível na mesa) que acredito que não será o caso dado o MW 7,8 ppg muito leve.

Notas: Em cenário de perda severa com MPD não há necessidade de fechar o BOP, reduz-se a contrapressão mantendo overbalance mínimo de 50 psi e em caso de perda total mantém o abastecimento do riser com vazão de controle de 2 bpm.

Passo 5 a 10: pode manter modo AP já que haverá bombeio pela coluna com bomba da sonda mapeada pelo sistema MPD. Dessa forma o modelo contabiliza a fricção no anular.

Passo 13: voltar ao modo AP.

### 3-RJS-762 — 21A - Combate à perda com cimento por injeção direta
**Fábio Koiti Dairiki** | v2

Sugiro detalhar o item 19 da seguinte maneira:

a) Estabelecer circuito de superfície com MPD em modo SBP com pressão suficiente para manter 3650 psi no BOP stack wellbore.
b)Equalizar Circuito de superfície com a linha de choke. Abrir válvula submarina da linha de choke, equalizando circuito de superfície com poço em modo SBP.
c)Equalizar linha de kill com poço. Abrir válvula submarina.
d)Mapear bomba a ser usada no deslocamento.
e)Deslocar 250 bbl de FPBNA 8,2 ppg a 250 gpm pelo alinhamento linha de kill=>poço=>linha de choke=>Sistema
MPD (circuito de superfície)=>MGS.

> ↳ **Fábio Koiti Dairiki:** f) Como o circuito passa pelo poço, contabilizar o deslocamento pelo volume retornado.

### 3-RJS-762 — 21A - Combate à perda com cimento por injeção direta
**Fábio Koiti Dairiki** | v1

Continuação:
Caso não seja mantido o AP 9,0 ppg no riser após o fechamento do BOP, incluir:
item 17. f) Realinhar bombas para circulação pela booster.

### 3-RJS-762 — 21A - Combate à perda com cimento por injeção direta
**Fábio Koiti Dairiki** | v1

Caros, boa noite
Não ficou claro se vamos manter circulação pela booster com AP 9,0 ppg durante toda a operação ou parte dela (e se isto é possível, dada a configuração de bombas para atender ao tampão).
Caso não seja mantido o AP 9,0 ppg no riser após o fechamento do BOP, sugiro modificar:
item 5: a) Fechar BOP Anular, registrar pressão no BOP. Parar circulação pela booster e alinhar bombas para atender a cimentação.
item 20. [Sonda] Reestabelecer circulação pela booster e manter AP 9,0 ppg pela MPD. Abrir BOP e efetuar flow check dinamico pelo sistema MPD por 15 min. Anotar perdas: _________ bph

### 3-RJS-762 — 21C -[Contingência] - Combate à perda com cimento por injeçã
**Ivani Tavares de Oliveira** | v1

Verificar o item 24 se o AP está correto: AP 9,2ppg?

item 32 b) Confirmar leitura de PWD e manter AP 9,0 ppg@3950m em "hydraulic mode" com 450 gpm na booster. 

item 33) b) durante o corte do cimento "by-passar" o coriolis.

### 3-RJS-762 — Combate a perda com tampão de cimento por injeção direta
**Fábio Koiti Dairiki** | v1

Prezados, boa tarde,
Sugestões:
No item 6, letra a: inserir o fechamento da linha de choke, aberta no item anterior.
No item 6, letra b: Se for necessário iniciar o bombeio imediatamente após o fechamento do BOP, inserir esta parte (fechamento do BOP) e o alinhamento de bombas no item 5 anterior ao teste de injetividade.

Nos itens 32 e 33, o Coriolis deve estar bypassado para evitar a deposição do cimento no seu interior, interferindo no seu funcionamento e precisão.
Avaliar se não seria recomendável aumentar o overbalance durante o corte do cimento pela ausência do Coriolis (sem detecção automática de influxo) e fluido heterogêneo no anular (modelo hidráulico prejudicado).

### 3-RJS-762 — [Contingência] - Combate à perda com LCM
**Gustavo Costa Magalhaes Pena** | v1

Seguem comentários:

Durante toda a operação manter booster com 02 bombas alinhadas (barramentos diferentes) e vazão de 600 gpm.

Itens 8-11: Como iremos trabalhar com vazões intermediárias (nem conexão e nem perfuração) pode ser que o MH não esteja bem ajustado. O AP 9,0 ppg nos dá alguma margem para erro, já que investigamos até 8,9 ppg (MS: 67 psi). No entanto, recomendo uma MS maior, por exemplo um AP 9,1 ppg (MS: 134 psi).

> ↳ **Gustavo Costa Magalhaes Pena:** De acordo com a SeqOp.

### 7-BR-86DB-RJS — Conversão para perfuração em PMCD (fase 4)
**Ivani Tavares de Oliveira** | v2

De acordo.
Se houver uma nova versão retirar a duplicidade no último bullet da pág 5/14, sobre a verificação da equipe MPD da proteção de seus equipamentos, antes dos realinhamentos.

Em PERFURAÇÃO PMCD:
#11 - SONDA/MPD: bullet #4) acrescentar o seguinte texto: O teste do BA é Hold Point com aprovação pelo CSD MPD. Critério de aprovação:

#11 - FLUIDOS: bullet #7, explicar melhor o texto. Segue sugestão)  O recalque reativo deverá ser realizado caso a pressão no anular aumente em relação à pressão do anular livre de gás (GFP - gas free pressure). O valor de referência para esse aumento de pressão será 100 psi. Ou seja, caso a diferença entre SBP ou BOP e SPP diminua mais que 100 psi ao longo do tempo, efetuar bullheading reativo de 1087 bbl de LAM 9,0 ppg pelo anular via flow spool a 806 gpm, para recalcar possível hidrocarboneto. Caso a diferença entre SBP ou BOP e SPP não retorne ao valor anterior, repetir o processo até obter êxito, ou aumentar vazão.

### 7-BR-86DB-RJS — Conversão para perfuração em PMCD (fase 4)
**Geronimo de Freitas Rolandi** | v1

Em todos os itens: O objetivo do bulhead preventivo de 6 em 6 h é para quebrar o gel do anular, geralmente não é suficiente para fazer a pressão voltar à pressão do anular livre de hidrocarbonetos (GFP), essa pressão vai ser obtida ao final do teste de injetividade  (item 8)

Em orientação para bombeios de LAM pelo anular :

Bullheading Preventivo: Deslocar 60 bbl de LAM a cada 6 h pelo anular com vazão mínima de 210 gpm e comparar pressão final com GFP.

Bullheading Reativo: Caso seja identificado indício de migração de HC pelo anular (variações maiores que 100 psi frente a pressão de referência (GFP) sem aumento equivalente da pressão de bombeio), injetar no mínimo 1087 bbl de LAM 9,0 ppg com vazão mínima de 806 gpm até que a pressão no anular retorne ao GFP. Caso a pressão não retorne ao patamar inicial após um ciclo de bullheading (volume de 1087 bbl), aumentar a vazão e efetuar novo ciclo. Caso a pressão não retorne ao patamar inicial após dois ciclos de bullheading, interromper o bombeio e avaliar, com suporte da equipe de MPD.

no Item 5, teste de injetividade pela coluna, em caso de perda total, aumentar vazão na coluna até obter leitura de SBP e iniciar teste a partir dessa vazão.

### 7-BUZ-100DA-RJS — Instalação cauda PACI 2z em FMCD
**Geronimo de Freitas Rolandi** | v6

De cordo com comentário do Trajano sobre adiantar o passo 42, evitando stripping desnecessário no DSIT

### 7-BUZ-100DA-RJS — Instalação cauda PACI 2z em FMCD
**Gustavo Costa Magalhaes Pena** | v4

De acordo.

Sugestão: Nos itens 39 e 40 lembrar as falhas presentes na RCD (vazamento na função latch, falha dos sensores de pressão e de posição do latch), e também os cuidados adicionais para a recuperação do BA (risco do BA vir no TJ ou alguma possível dificuldade para destravar o mesmo - função unlatch não foi testada ainda).

### 7-BUZ-100DA-RJS — Instalação cauda PACI 2z em FMCD
**Gustavo Costa Magalhaes Pena** | v1

Seguem comentários abaixo:

Em dados de poço e sonda: A figura está com FPBA 8,8 ppg no poço.

Item 7: Menciona que o limite é 500 psi mas no 2º bullet pede para setar pop-off em 150 psi. 

Item 29: Não temos sistema MPD (coriolis) disponível. Após encher o riser, efetuar alinhamento de flow check estático com BA instalado utilizando o BFM.

Item 40: Antes de recuperar o BA é necessário retirar pelo menos 2 seções para descer a BART.

A estratégia adotada nesta seqop é de mencionar as vazões e alinhamentos da vazão de controle somente quando existe alguma alteração. Não vejo problemas em manter desse jeito, mas vale a pena conversar sobre essa estratégia com as equipes executoras: Não é por que não está detalhado no item, que não precisa manter a vazão de controle.

### 7-BUZ-100DA-RJS — Montagem e descida da cauda PACI 2 em FMCD
**Gustavo Costa Magalhaes Pena há um mês** | v1

Prezados, seguem comentários:

Item 40, 7º bullet: Bactericida duplicado.

Item 41: Após instalar BA, retirar BART uns 5 m acima da RCD antes de partir para o teste do BA. Garantir que não exista TJ em frente ao BA e DSIT.

Item 42: 
O teste de estanqueidade do BA pode ser realizado conforme planejado, porém existe também a opção de testar contra o DSIT com as vantagens de não precisar pressurizar o riser todo e nem aplicar diferencial adicional de pressão na LBSR.
4º bullet: Bactericida duplicado e CSR estará aberta.

Item 44: CSR estará aberta. By-passar e depois abrir a LBSR.

Item 45: Poço estará aberto.

Item 46:
1º bullet: Em caso de retirada aumentar vazão para 6 bpm.

Monitorar trip tank para verificar estanqueidade do BA de cima para baixo, e atentar que vazamento do BA se soma a vazão de controle no anular (limitação dos elementos da cauda). Se necessário, utilizar a linha de fill-up diverter com 1 bpm para manter o BA lubrificado (conforme recomendação da página 4).

### 7-BUZ-94D-RJS — Montagem e descida cauda PACI (2+1) em FMCD
**Leonardo Mesquita Caetano** | v4

Caros, de acordo com a seqop. 
Apenas um comentário.

No item 63), manter  as válvulas submarinas abertas para caso em que o BOP seja fechado, a vazão de ataque feita pela booster não seja interrompida.

### 7-BUZ-94D-RJS — Montagem e descida cauda PACI (2+1) em FMCD
**Leonardo Mesquita Caetano** | v3

Caros, 
segue comentários em complemento ao CSD de Búzios.

-Manter desde o início o alinhamento para evitar que as bombas de pré-carrega superem as bombas de ataque ao poço: bomba da sonda> choke manifold > kill > anular poço x coluna > revestimento> formação.

-Durante a descida, com mudanças na área de passagem do fluido é esperado que a pressão no BOP mude. Em caso de aumento de pressão deverá ser avaliado se ela está relacionada a essa condições. 

59) Manter firme a lubrificação do BA.

### 7-BUZ-94D-RJS — Montagem e descida cauda PACI (2+1) em FMCD
**Ramon Moreira Fernandes** | v2

Passo 55: Esse teste é Holdpoint MPD. Só há necessidade de retirar BA, jatear RCD e reinstalar BA se houver indicativo de vazamento do BA pelo trip tank.

### 7-BUZ-94D-RJS — Montagem e descida cauda PACI (2+1) em FMCD
**Geronimo de Freitas Rolandi** | v1

De acordo com a sequencia. Uma possível simplificação sugerida seria manter o abastecimento do poço sempre pela linha de kill, evitando necessidade de manobras de válvulas para o fechamento do BOP anular.

### 7-ITP-7-RJS — Montagem e descida da cauda PACI 2Z em FMCD
**Leonardo Mesquita Caetano** | v1

Caros, 
sobre o abastecimento:
verificar fisicamente pelos tanques o volume bombeado e, 
caso a pressão de bombeio seja baixa, desligas as pré cargas para evitar que elas superem as bombas de lama.

Item 36. Realizar teste pressurizando a câmara entre os selos superior e inferior da SSA.

> ↳ **Leandro Lourenço Vieira da Rocha:** Bom dia, Leonardo!

A solução sobre o abastecimento que está contemplada é alinhar o choke manifold para estabelecer contrapressão. Vou incluir o reforço sobre verificar fisicamente pelos tanques o volume bombeado.

### 7-ITP-7-RJS — instalação da cauda PACI 2z em FMCD
**Gustavo Costa Magalhaes Pena** | v1

Monitorar vazamento do SSA/ACD de cima para baixo (esse vazamento se soma à vazão de controle no anular), e se necessário ajustar pressão dos packers da ACD.

Pendente incluir etapa de retirada do SSA.

> ↳ **Danilo Signorini Gozzi:** Ok, incluirei em uma nova versão. Só vou aguardar demais comentários para emitir

### 7-JUB-78DA-ESS — Conversão para Perfuração em PMCD
**Ramon Moreira Fernandes** | v1

Observações PMCD / Passo 12:
Sugiro colocar a tabela de resumo das simulações de vazão de controle e BH do SIP. No pocoweb encontrei simulações com cenários diferentes (sem coluna, fluido 8,5 ppg newtoniano). Entendo que precisa de uma simulação específica para recalque/controle no cenário de PMCD com LAM no anular.

Observações PMCD / Passo 12 / 2º bullet: O volume de bullhead não está muito claro: "injetar no mínimo 60 bbl" e "após um ciclo de bullheading (volume de 540 bbl)".

Teste de injetividade / passo 7: completar primeira coluna da tabela com 490 gpm de vazão na coluna (SAC).

Manobra / passo 17: para velocidade de retirada de 2 min/sç é preciso recalcular a vazão de abastecimento do anular: 1,4 * 0,1132 * 39 * 42 / 2 = 130 gpm. Se for usar o mesmo fator (x2) teria que usar uma vazão de 260 gpm. Acho desnecessário usar esse fator de 2x, pois já estamos considerando uma margem de 40%.
Uma opção para poupar fluido: durante a conexão (coluna parada) reduzir vazão de injeção pelo anular para 50 gpm. Estabelecer 130 gpm apenas durante retirada da coluna.

> ↳ **Gabriel Gonçalves Rosa:** Em relação as simulações estamos utilizando essa abaixo por falta de outra mais adequada:

Já a manobra a 2 min/seção realmente mantivemos o 130 gpm sem o fator 2x. Estamos aplicando o fator apenas na manobra até o XO do revestimento. Vou adicionar o comentário para ficar mais claro.

### 7-JUB-78DA-ESS — Instalação da completação inferior em FMCD
**Gustavo Costa Magalhaes Pena** | v6

Prezados, seguem comentários:

Em operações anteriores a montagem da cauda:
Item 3: Incluir procedimento de teste Hold Point do BA com 300 psi por 5 min contra o DSIT. Notificar CSD MPD para acompanhamento do teste.

Em descida da cauda inferior:
Item 15: Incluir procedimento de teste Hold Point do BA com 300 psi por 5 min contra o DSIT. Notificar CSD MPD para acompanhamento do teste.

Item 16 em diante: Caso o BA em algum momento passe a vazar de cima para baixo, avaliar trocar o monitoramento do trip tank pela manutenção da lubrificação do BA utilizando uma bomba de lama alinhada para a fill-up diverter com 0,5-1,0 bpm.

### 7-JUB-78DA-ESS — Instalação da completação inferior em FMCD
**Ramon Moreira Fernandes** | v1

A partir do passo 17, eliminar o trecho "Manter LBSR fechada". Apenas manter o abastecimento contínuo pel linha de kill com 170 gpm de AGMAR com bactericida e alcalinizante.

Sugiro marcar também o CSD FLUI para revisão e aprovação da seqop. Normalmente o bombeio de SAC com alcalinizante e bactericida é feito nos últimos 20000 bbl de fluido. Precisa verificar o timing para o início do bombeio de bactericida e alcalinizante.

### 7-MRO-37-RJS — Conversão e perfuração de 8 1/2” em modo PMCD
**Ramon Moreira Fernandes há um ano** | v1

Orientações de segurança de processo / Rotina: adicionar a fórmula da PRC em MPD: PRC = Pbombeio - PRCD + HidrostáticaRCD.

Recomendações para PMCD / Vazões recomendadas / 2º bullet: "Recalques periódicos para quebra de gel: Deslocar 60 bbl de Fluido FPBA Polimérico 8,7 ppg (LAM) a cada 6 h pelo anular para quebra de gel com vazão simulada que garanta bullheading.

Passo 11 / Fluidos / 6º bullet: mesmo comentário do item anterior com relação à vazão do recalque preventivo.

Contingência 1 / passos 4 e 5: os volumes para o bullheaing em caso de aumento de 100 psi na SBP, parecem estar desajustados: 620 bbl na retirada em poço aberto e 210 bbl na retirada em poço revestido.

Contingência 1 / passo 10 / 4º bullet: usar vazão de BH para os recalques preventivos.

### 7-MRO-37-RJS — Conversão e perfuração de 8 1/2” em modo PMCD
**Geronimo de Freitas Rolandi há um ano** | v1

RECOMENDAÇÕES PARA PMCD:
• Vazão de Controle com coluna (prevenção de migração de gás): Esse bombeio de controle de 60 bbl não é aplicável no cenário de PMCD. Usar somente a vazão de bulhead. A vazão de controle será utilizada somente se for utilizada AGMAR no anular e de forma contínua (PMCD dinâmico). 
De acordo com demais comentários do Grabarski

### 8-BUZ-89D-RJS — Combate à perda com Barablend e Baralock
**Ramon Moreira Fernandes** | v1

Passo 2: Para o flowcheck dinâmico com AP 8,8 ppg, considerar vazão somente pela booster.

Passo 3: Verificar simulação de swab e ECD na sapata com efeito de swab. Caso ECD na sapata com margem muito reduzida em relação à Pp, aplicar AP maior para compensar o swab.

### 8-ITP-9D-RJS — S03a - Treinamento FMCD (sequência complementar)
**Gustavo Costa Magalhaes Pena há um ano** | v2

Enviados esboço com desenho do sistema SSA/ACD para atualizar na SeqOp, caso achem oportuno.

> ↳ **Rafael Valadares Leite há um ano:** Obrigado, entrará na próxima versão da sequência #3 (treinamento estará como anexo).

### 8-ITP-9D-RJS — S03a - Treinamento FMCD (sequência complementar)
**Gustavo Costa Magalhaes Pena há um ano** | v1

Seguem comentários:

Item 2: O sistema de desvio de fluxo do NS61 é da AFG/NOV, e ao invés de BA, BART e RCD (Weatherford), temos SSA, SSART e ACD.

Item 2, h: O SSA/ACD por ter elementos de vedação ativos, possuem maior capacidade de manter o nível de fluido monitorado no trip tank.

Item 6: Não faz parte do escopo desta intervenção.
