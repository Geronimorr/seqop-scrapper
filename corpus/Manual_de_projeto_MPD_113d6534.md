## Página 1

 
 
 
GERÊNCIA EXECUTIVA DE POÇOS 
 
 
MANUAL DE PROJETO DE MPD 
 
Anexo do Sinpep 
[PE-2POC-01204] 
 
Segunda edição 
 
 
 
 
 
 
Órgão Gestor POCOS/EP/IDE 
Órgão Aprovador POCOS/SPO/PEP/PROJ-PERF 
Última Revisão  
Próxima Revisão  
 
Este manual de projeto é voltado aos empregados da Petrobras que são habilitados a desempenhar suas 
funções como especialistas em MPD. Este documento contém as informações necessárias para a execução 
do projeto de MPD e que são desdobradas a partir da diretriz técnica de MPD. Este manual de projeto possui 
teor estritamente técnico a respeito da especialidade em questão, não estabelecendo e nem definindo 
nenhum aspecto referente à processos de especificação técnica e de contratação. 
 
 
 

## Página 2

 
2 
 
 
HISTÓRICO DE REVISÕES 
Data Versão Alterações Realizadas 
 0 Emissão original 
18/01/2022 1 Revisada árvore de perdas. Revisadas recomendações para ajusta das PRVs e pressões 
máximas. 
24/11/2023 2 
Retirada a folha executiva. Inserido possibilidade de utilização de BHA padrão na simulação. 
Inseridas recomendações para redução da fricção no anular. Revisada a configuração de PRVs e 
limites do sistema. Revisadas as recomendações para PMCD e FMCD. Revisadas 
recomendações de Fingerprint. Clarificados pontos sobre pressões limites e indicação a outros 
padrões. 
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
 
 

## Página 3

 
3 
 
Conteúdo 
1. INTRODUÇÃO. ................................................................................................................. 4 
2. DEFINIÇÕES E ÍNDICE DE VARIÁVEIS. ......................................................................... 4 
3. DOCUMENTOS DE REFERÊNCIA ................................................................................... 7 
4. CONSIDERAÇÕES GERAIS. ........................................................................................... 8 
5. IDENTIFICAÇÃO DA DEMANDA MPD (SBP/MCD) ......................................................... 8 
6. INSUMOS .......................................................................................................................... 9 
7. DEFINIÇÃO DA ESTRATÉGIA DE APLICAÇÃO ............................................................ 10 
8. PROJETO DE FLUIDOS DE PERFURAÇÃO ................................................................. 12 
8.1. Circulação de influxo ................................................................................................. 16 
9. PROJETO DIRECIONAL / BHA ...................................................................................... 16 
10. ASSENTAMENTO PRELIMINAR DE SAPATAS ............................................................ 18 
11. PROJETO DE REVESTIMENTOS .................................................................................. 18 
12. RISER ANALYSIS E ESTRUTURA DE POÇO ............................................................... 19 
13. EQUIPAMENTOS............................................................................................................ 19 
14. ÁRVORE DE DECISÃO DE COMBATE A PERDAS E CONVERSÃO PARA MCD ........ 21 
15. TESTE DE PRESSÃO DOS EQUIPAMENTOS MPD ..................................................... 21 
16. SUBSTITUIÇÃO DE FLUIDO E CORTE DE CIMENTO .................................................. 22 
17. FINGERPRINT ................................................................................................................ 22 
18. PERFURAÇÃO DA FASE ............................................................................................... 22 
19. TESTEMUNHAGEM ........................................................................................................ 23 
20. PERFILAGEM A CABO ................................................................................................... 23 
21. REVESTIMENTO E CIMENTAÇÃO ................................................................................ 24 
22. COMPLETAÇÃO ............................................................................................................. 24 
23. MUD CAP DRILLING ...................................................................................................... 24 
23.1. Pressurized Mud Cap Drilling ................................................................................... 25 
23.2. Floating MudCap Drilling ........................................................................................... 25 
24. CONSIDERAÇÕES FINAIS ............................................................................................ 26 
25. ANEXOS ......................................................................................................................... 26 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

## Página 4

 
4 
 
1. INTRODUÇÃO. 
Este manual tem por objetivo orientar os projetistas na elaboração dos projetos de MPD quando 
este for requerido. 
Os projeto MPD, Managed Pressure Drilling, contém características e cuidados especiais. Antes 
da elaboração de um projeto em qualquer variante MPD (Perfuração com Gerenciamento de 
Pressão) devem ser relacionados os dados e informações mínimas necessárias para 
elaboração deste projeto de interveção , auxiliando na melhor estratégia de uso das técnicas 
de MPD. 
2. DEFINIÇÕES E ÍNDICE DE VARIÁVEIS. 
Anchor Point: A profundidade na qual a pressão no anular do poço deve ser mantida constante 
com emprego do sistema de MPD, para todos alinhamentos possíveis. 
Anomalia de fluxo: Invasão prevista ou planejada de fluido da formação para o poço. Ocorre 
devido às operações planejadas, como DPPT, amostragem de fluido ou outras. 
Ballooning / Breathing Formation: Fenômenos ocorridos no poço que se caracterizam pela 
aparente perda de fluido para a formação durante a perfuração (maior pressão devido ao ECD) 
e ganho de fluido durante a conexão (perda da pressão de fricção) sem, contudo, configurar 
um influxo. 
Buffer Manifold: Manifold de distribuição que permite direcionar o fluxo com diferentes 
alinhamentos necessários às operações MPD (SBP e MCD). É responsável por direcionar fluxo 
para outros sistemas de circulação da sonda, como choke manifold, standpide manifold, 
separador atmosférico de gás, tanque de manobra, entre outros. 
Coluna de trabalho: Coluna utilizada disponibilizada pela unidade de intervenção para trabalho 
no poço, podendo ser coluna de perfuração, assentamento, completação, condicionamento, 
entre outras. 
Conjunto de vedação do RCD: Conjunto composto pelos elementos de vedação e rolamento, 
quando presente. 
Dynamic Formation Integrity Test (DFIT): Teste de integridade da formação feito com 
circulação contínua pelo poço e Sistema de Gerenciamento de Pressão. A formação do poço 
aberto é submetida a uma pressão, através da combinação de pressão de superfície, pressões 
de fricção e pressão hidrostática da coluna de fluido para determinar a resistência da formação 
frente a uma pressão planejada. 
Dynamic Leak Off Test (DLOT): Teste de absorção feito com circulação contínua pelo poço e 
Sistema de Gerenciamento de Pressão. A formação do poço aberto é submetida a uma pressão 
através da combinação de pressão de superfície, pressões de fricção e pressão da coluna 
hidrostática de fluido para determinar a pressão na qual a formação absorve fluido. 
Dynamic Pore Pressure Test (DPPT): Teste realizado com circulação contínua pelo poço e 
Sistema de Gerenciamento de Pressão, que visa determinar a pressão de poros através da 
redução da pressão aplicada na superfície até a verificação de anomalia de fluxo. 
Elemento de vedação do RCD: Elemento da RCD que promove a vedação contra a coluna de 
trabalho. O elemento de vedação permite a aplicação de pressão no anular do poço. 
Equivalent Circulation Density: Densidade de circulação equivalente é a densidade efetiva 
do fluido circulante no poço, resultante da soma da pressão imposta pela coluna hidrostática de 
fluido, pressão de fricção e contrapressão aplicada na superfície. 
Fingerprinting: Etapa pré-operacional de ajuste e calibração do sistema de controle MPD. 

## Página 5

 
5 
 
Floating Mud Cap Drilling (FMCD): É uma técnica de MCD na qual o nível de fluido permanece 
abaixo da mesa rotativa. 
Fluido hidrostaticamente underbalance: Fluido utilizado na intervenção, cuja pressão 
exercida por sua coluna hidrostática é menor que a pressão de uma determinada formação 
comunicada com o poço aberto. 
Formações carstificadas / vugulares: Formações que sofreram dissolução de parte de sua 
matriz por águas subterrâneas,resultando em cavidades de diversas formas e tamanhos. 
Formation Integrity Test (FIT): Teste de integridade da formação (teste de competência de 
formação) com aplicação de pressão adicional na superficie em uma coluna de fluido (pressão 
hidrostática) para determinar a capacidade de uma zona subterrânea para suportar uma 
pressão planejada. 
Full Evacuation: Esvaziamento total do interior do revestimento. 
Influxo: Invasão imprevista e indesejada de fluido da formação para o poço. 
Janela operacional: Representa a menor diferença entre o gradiente de pressão de poros / 
colapso mais elevada e o gradiente de pressão de fratura / perda de fluido mais baixa do poço 
aberto. 
Leak Off Test (LOT): Teste que visa determinar a pressão a que a formação exposta absorve 
fluido do poço. A aplicação da pressão é feita através da coluna de fluido (pressão hidrostática) 
e uma pressão superficial até o indicativo de absorção. 
Mud Cap Drilling (MCD): É uma técnica de MPD que possibilita o prosseguimento da operação 
de forma segura durante a ocorrência de perda total de fluido para a formação. A perda para 
formação não é controlada e o cascalho produzido durante a perfuração é bombeado para a 
formação. 
Non Return Valve (NRV): é uma válvula do tipo flapper, instalada no interior da coluna de 
trabalho que impede o fluxo ascedente em caso de desbalanceio entre coluna e anular do poço. 
PP: Pressão de poros. 
Pressão de trabalho: Pressão planejada no choke MPD para as operações normais e 
programadas para a intervenção. 
Pressurized Mud Cap Drilling (PMCD): É uma técnica de MCD na qual a perda total é 
controlada pela aplicação de contrapressão na superfície. 
Rotating Control Device (RCD): equipamento que permite a passagem da coluna de trabalho 
(com ou sem rotação) pelo seu interior enquanto promove a vedação contra a coluna e, por 
consequência, mantem a pressão no anular do poço no patamar desejado. É parte integrante 
do Conjunto Solidário de Barreiras primário. 
Sistema de Contrapressão: Sistema que gera contrapressão pela restrição do fluxo por 
chokes, com objetivo de manter a pressão de superfície ou anular em patamar desejado. É 
composto por manifold MPD e por um sistema de controle. 
Sistema de Desvio de Fluxo: Sistema composto por equipamentos instalados na coluna de 
riser que desvia o fluxo do poço para o sistema de superfície. 
Sistema de Gerenciamento de Pressão: Todo o aparato necessário à aplicação das técnicas 
MPD e suas variantes. 
Surface Back Pressure (SBP): é uma técnica de MPD na qual é aplicada ativamente uma 
contrapressão na superfície durante a operação (perfuração, conexão, manobra, entre outras), 
com objetivo de manter a pressão no valor desejado no Anchor Point. 

## Página 6

 
6 
 
 
AP – Anchor Point 
BTR – Bellow Tensioner Ring 
DDV – Downhole Deployment Valve 
DFIT – Dynamic Formation Integrity Test 
DLOT – Dynamic Leak Off Test 
DP – Drill Pipe 
DPPT – Dynamic Pore Pressure Test 
EKD – Early Kick Detection 
ERW – Extended Reach Well 
FMCD – Floating Mud Cap Drilling 
HL – High Limit 
HPHT – High Pressure High Temperature 
LAM – Light Annular Mud 
LCM – Loss Control Material 
LWD – Logging while Drilling 
MCD – Mud Cap Drilling 
MGS – Mud Gas Separator (separador atmosférico) 
MPD – Managed Pressure Drilling 
MWD – Measuring while Drilling 
LDA – Lâmina d’água 
LWD – Logging while drilling 
NRV – Non-return Valve 
PCV – Pressure Control Valve 
P&ID – Piping and Instrumentation Diagram 
PMCD –Pressurized Mud Cap Drilling 
PP – Pressão de poros 
PRV –Pressure Relief Valve 
PWD – Pressure While Drilling 
RCD – Rotating Control Device (Cabeça Rotativa) 
RSS – Rotary Steerable System 
SAC – Fluido de sacrifício 
SBP – Surface Back Pressure 
SPL – Secondary Pressure Limiter 
WSOG – Well Specific Operating Guidelines 

## Página 7

 
7 
 
3. DOCUMENTOS DE REFERÊNCIA 
PE-2POC-01099 - [ MPD ] [ FMCD ] [ OPER ] PERFURAÇÃO NO MODO FMCD 
PE-2POC-01097 - [ MPD ] [ FMCD ] [ CONT ] PREPARAÇÃO PARA PERFURAÇÃO NO MODO 
FMCD  
PE-2POC-01106 - [ MPD ] [ PMCD ] [ OPER ] TRANSIÇÃO PARA PMCD 
PE-2POC-01107 - [ MPD ] [ PMCD ] [ OPER ] PERFURAÇÃO EM MODO PMCD 
PE-2POC-01098 - [ MPD ] [ FMCD ] [ CONT ] CONVERSÃO DO MODO MPD PARA FMCD 
PE-2POC-01113 - [ MPD ] [ SBP ] [ OPER ] DETECÇÃO E CIRCULAÇÃO DE ANOMALIA DE 
FLUXO 
PE-2POC-01115 - [ MPD ] [ GERAL ] TREINAMENTO 
PE-1PBR-00603-E DIRETRIZ DE SEGURAÇA E INTEGRIDADE DE POÇOS 
PE-2POC-01257 – COMPLETAÇÃO MPD 
PE-2POC-00453 - LIMPEZA DE POÇO E HIDRÁULICA - UTILIZAÇÃO DO SIMCARR E 
INTERPRETAÇÃO DO PWD 
PE-2DPT-00048 - DIRETRIZ DE PROJETO DE POÇO - FLUIDOS DE PERFURAÇÃO 
PE-1PBR-00049 - PERDAS DE FLUIDO SEVERAS E TOTAIS NA PERFURAÇÃO: 
DIRETRIZES OPERACIONAIS DE SEGURANÇA DE POÇO 
PE-1PBR-00733 - SIMULAÇÕES HIDRÁULICAS DE CONTROLE DE POÇO: CONCEITOS E 
ELABORAÇÃO 
PP-1PBR-00614 - SIMULAÇÕES HIDRÁULICAS DE CONTROLE DE POÇO: DIRETRIZES E 
FLUXO DE INFORMAÇÃO  
ANSI/NACE MR 0175/ISO 15156: 2015 – Petroleum and Natural Gas Industries – Materials for 
use in H2S-containing Environments in Oil and Gas Production. 
API SPEC 7NRV: 2012 – Specification for Dill String Non-return Valves. 
API RP 7K: 2015 (6th edition) – Drilling and Well Servicing Equipment. 
API SPEC 16RCD:– Specification for Rotating Control Devices. 
API RP 92M: 2017 (1st edition) – Managed Pressure Drilling Operations with Surface Back-
Pressure. 
API RP 92S Managed Pressure Drilling Operations-Surface Back-pressure with a Subsea 
Blowout Preventer - First Edition  
N-2752 – Segurança de Poço para Projetos de Perfuração em Poços Marítimos 

## Página 8

 
8 
 
PE-2POC-00422 - COMBATE À PERDA DE CIRCULAÇÃO NAS ATIVIDADES DE 
PERFURAÇÃO 
 
N-2768 - Segurança de poço nas Operações de Perfuração no Mar  
4. CONSIDERAÇÕES GERAIS. 
O projeto MPD deve ser elaborado de forma que avalie todos os possíveis cenários que serão 
encontrados ao longo da construção do poço, adequando o perfil de pressão no anular de forma 
que o poço seja mantido todo o tempo sob controle, ainda que apresente perda de fluido parcial 
ou total. A avaliação de cenários consiste de duas partes: o levantamento das operações que 
serão necessárias para a construção do poço (perfuração, perfilagem, descida de colunas de 
condicionamento, etc); e o levantamento dos cenários operacionas possíveis como janela 
estreita, perda parcial e perda total, considerando, inclusive, como contingência a utilização de 
técnicas de Mud Cap Drilling (MCD). 
Para isto é necessária a análise da janela operacional esperada do poço. Através de 
simulações, devem-se verificadas as pressões esperadas nas diferentes situações 
operacionais e adequadas de forma que estas não excedam os limites operacionais dos 
equipamentos e das formações. 
5. IDENTIFICAÇÃO DA DEMANDA MPD (SBP/MCD) 
A avaliação inicial de demanda do recurso MPD para um novo projeto deve ser feita com base 
no histórico dos poços de correlação, previsões geomecânicas, de pressão de poros e de perda 
de fluido. Essa avaliação pode indicar que seja mais vantajoso a opção por uma sonda 
convencional. 
Deve-se levar em consideração a duração das atividades inerentes à aplicação da técnica, além 
dos seus custos relativos aos equipamentos, e comparado com as operações sem utilização 
da técnica. Apesar de haver um incremento de tempo devido à essas operações inerentes 
(descida da junta integrada, fingerprint, etc), devido à utilização das técnicas MPD é esperada 
uma redução nos tempos, e custo, não produtivos, como operações de combates a perda, 
circulação de influxo, entre outros. Assim, deve-se avaliar o custo/benefício/segurança 
operacional da aplicação da técnica para o poço ou projeto em questão. 
Além dos pontos anteriores, a escassez dos recursos (sonda com equipamentos MPD) também 
pode levar à decisão de não utilização de técnicas MPD. 
A análise em conjunto com a equipe de reservatório para identificação de pontos críticos na 
trajetória do poço deve ser executada durante a elaboração do projeto do poço. Esta discussão 
prévia auxiliará na elaboração dos cenários operacionais mais prováveis e, assim, na definição 
da melhor estratégia de perfuração. Deve ser, também, considerado o histórico operacional dos 
poços de correlação. 
Os seguintes cenários operacionais são candidatos à utilização da técnica de MPD: 
 Janela operacional estreita - quando a diferença entre pressão de poros (ou colapso 
inferior) e a pressão de fratura (ou pressão de indução de perdas) é pequena, conforme 
a diretriz de segurança e integridade de poço, item 5, onde o peso de fluido necessário 
para controlar o poço e evitar influxo, considerando também a circulação, seja suficiente 
para fraturar a formação mais frágil ou induzir perdas. 
 Perdas severas - Ocorrem devido à presença de rochas vugulares e/ou fraturas nos 
reservatório. Em reservatórios carbonáticos depletados, devido ao maior 

## Página 9

 
9 
 
sobrebalanceio, existe um mecanismo adicional de perda. 
 Poços HPHT - Os efeitos térmicos e/ou altas pressões de reservatórios demandam um 
melhor monitoramento e controle mais acurado da barreira primária do poço. 
 Problemas de estabilidade de poço – Problemas como breakouts, colapso de poço ou 
fechamento de poço que ocorrem devido a diferença de pressão no poço entre as 
condições estática e dinâmica (com e sem circulação).  
 Poços exploratórios - Devido às incertezas associadas a esses poços, é necessária 
maior flexibilidade e maior velocidade na adequação do perfil de pressão do poço. Além 
disso, em alguns cenários em que não se poderia prosseguir a perfuração convencional, 
a utilização de técnicas MPD pode tornar possível a perfuração até a profunidade final 
projetada. 
6. INSUMOS 
O checklist completo de insumos de projeto MPD encontra-se no Anexo B deste padrão. Entre 
os insumos, alguns são essenciais para a elaboração do projeto MPD e deverão ser 
disponibilizados pelo projetista, enquanto outros são desejáveis, aumentando a qualidade do 
projeto e seu detalhamento. Outros podem ser buscados junto à sonda ou companhias 
contratadas. Verificar o cheklist para identificar os itens obrigatórios. 
Apesar de serem considerados insumos, algumas definições poderão ser rediscutidas durante 
a elaboração do projeto MPD, em comum acordo com a equipe de projeto. 
Para a definição dos insumos, observar os seguintes limites: 
RCD: Limite de projeto de 750 psi de contrapressão na superfície para operação normal e limite 
operacional da cabeça rotativa de acordo com envelope operacional da RCD (relaciona a 
rotação da coluna e a pressão de trabalho); 
Choke MPD: Vazão e pressão na superfície deverão estar dentro da faixa ótima de trabalho do 
choke MPD. Sonda: A definição da sonda permitirá realizar os cálculos da simulação hidráulica 
com maior precisão, por incluir as perdas de carga de superfície específicos da sonda. Além 
disso, impacta diretamente na definição das operações específicas para cada equipamento, 
tais como cabeça rotativa e sistema de contrapressão. A equipe da sonda deve estar com os 
treinamentos MPD atualizados. 
Perda de carga de superfície: Perda de carga para as vazões e fluido utilizados, linhas de 
superfície de retorno, comprimento, número de curvas e joelhos e ID dos tubos. Esse insumo é 
obtido pelo próprio projetista MPD. 
Drill Pipe: Data sheet dos Drill Pipes com informação sobre Tool Joints. Informar a composição 
da doluna, principalmente se a mesma será composta por mais de um tipo de DP (diâmetro, 
tool joint,etc). 
Bombas de Lama: Quantidade, diâmetro da camisa, presença de coriolis. 
Barramentos: Configuração dos barramentos, equipamentos em cada barramento; 
Estratégia proposta:. A definição do AP e peso de fluido será feita pelo projetista do poço com 
auxílio do projetista de fluidos e projetista MPD nessa análise. Para isso, deverá ser levado em 
consideração as pressões na superfície resultantes das simulações de hidráulica e seus limites. 
Também deve ser analisada a possibilidade de utilização das técnicas MCD no poço em 
questão. 
DFIT / DLOT e DPPT: Definir se será realizado DFIT, DLOT ou DPPT, bem como a 
profundidade, motivo e valores esperados;  

## Página 10

 
10 
 
Testemunhagem: A necessidade de testemunhagem deverá ser informada pelo projetista do 
poço. Definir a previsão da profundidade inicial, extensão testemunhada, número de barriletes, 
rotação e vazão esperados da operação. A equipe de projetos deverá analisar os cenários 
possíveis de realizar as operações previstas e os cuidados a serem tomados. 
Perfilagem a cabo: Deve ser informada a previsão de perfilagem e as condicionantes para 
realização da operação. Caso seja prevista perfilagem a cabo com MPD, o planejamento deverá 
ser realizado de forma antecipada, afim de verificar a disponibilidade de recursos. 
Fluido: As informações do fluido como tipo, reologia, estimativa preliminar de peso, entre 
outras, deverão ser disponibilizadas pelo projetista de fluido. Também devem ser informados 
os aditivos do fluido SAC para as operações MCD.  
Vazão: Informar a vazão prevista na coluna e na booster para todas as operações previstas 
(perfuração, conexão, testemunhagem, alargamento, etc) assim como a estimativa de variação 
mínima e máxima. 
Rotação: Deve ser considerada a rotação que se pretende utilizar na fase, evitando um range 
muito abrangente. A rotação impactará diretamente no limite de contrapressão na superfície. 
Geometria do BHA: Comprimento dos componentes, OD, ID, estabilizadores (tipo e número 
de aletas). Um melhor detalhamento permitirá uma melhor a simulação da fricção no anular e 
assim ajuste fino das simulações. Poderá ser utilizado BHA padrão para a simulação hidráulica 
de projeto. 
MWD/LWD: Devem ser considerados os possíveis ranges de vazão de trabalho das 
ferramentas MWD e LWD a serem utilizadas no poço, bem como restrições impostas pelo modo 
de comunicação (pulso positivo ou pulso negativo). 
Ferramenta direcional: Informar o range de vazões das ferramentas direcionais pois podem 
limitar a vazão e/ou pressão de bombeio da fase, como é o caso da turbina. Informar também 
a pressão (ou perda de carga) necessária para o funcionamento da ferramenta, como é o caso 
de alguns RSS existentes. 
TFA da broca / alargador: Além de permitir o cálculo mais preciso da pressão de bombeio, 
deve ser utilizado para garantir que a coluna estará cheia durante a operação de FMCD. 
Esquema do poço: LDA, Mesa Rotativa, Geometria e peso dos revestimentos do poço. 
7. DEFINIÇÃO DA ESTRATÉGIA DE APLICAÇÃO 
Além do SBP, é necessário considerar se o projeto irá contar com alguma técnica de MCD. 
Para isso, deve-se verificar a probabilidade e a previsão do nível de perda. Caso a operação 
MCD seja considerada, deverá ser verificado o impacto operacional desta técnica na operação 
da sonda conforme instalação e linhas de superfície disponíveis e nos BHA’s e colunas de 
trabalho previstas para serem utilizadas no poço. 
Entre as técnicas MCD, a Petrobras considera como técnica primária o PMCD. Caso as 
formações a serem atravessadas na fase estejam depletadas, deve-se fazer o uso da técnica 
de FMCD. As técnicas MCD são técnicas contingentes, utilizadas quando não é possível o 
prosseguimento da operação em SBP. A indução de perdas e/ou fraturas através do aumento 
da pressão do poço para a utilização de técnicas MCD não é recomendada devido ao risco de 
plugeamento das formações, pois este mecanismo não irá suportar a injeção do cascalho 
gerado da perfuração e não possui histórico de sucesso na perfuração em nossas operações. 
O AP deverá ser definido pelo projetista do poço, com auxílio da equipe SPO (equipe MPD e 
de fluidos). De acordo com as curvas de geopressões, deve-se definir se o fluido a ser utilizado 
será hidrostaticamente sobrebalanceado ou sub-balanceado.  

## Página 11

 
11 
 
A utilização de fluido sobrebalanceado resulta em operações com procedimentos mais simples 
e condições mais seguras na construção do poço, porém limita a redução de pressão no poço, 
não permitindo trabalhar com pequenos overbalances.  
O uso de fluido com pressão hidrostática inferior a pressão de poros (sub-balanceado) exige a 
manutenção de contrapressão e maior controle da pressão no poço, resultando em operações 
e procedimentos mais complexos, aumentando o risco da operação (risco de influxo caso a 
contrapressão não seja mantida). Porém, permite melhor controle da pressão no poço e 
possibilidade de redução da pressão, podendo mitigar perdas de fluido em poços com janelas 
operacionais estreitas. 
Um fluido hidrostaticamente sub-balanceado também permite a realização do DPPT.  
Nota: Em operações MPD, a pressão na formação exposta será sempre sobrebalanceada. 
Nota: Em fases cujo objetivo é apenas o treinamento da equipe e teste do sistema (ocorre 
quando é a primeira operação MPD da sonda com a Petrobras ou ela está há mais de 6 meses 
sem utilizar MPD, conforme padrão de treinamento MPD) não é necessário que se utilize a 
técnica durante toda a fase e não se recomenda o uso de fluido sub-balanceado. 
Ao escolher o AP para iniciar a fase deve-se observar como ocorrerá (ou ocorreu) o final da 
fase anterior com relação à entrada na formação de interesse e peso de fluido que será (foi) 
utilizado. Essas informações permitem balizar a estratégia de AP e peso de fluido a ser utilizado 
na fase objetivo. 
Nesta etapa deverá ser definido se será realizado DFIT (ou DLOT). O DFIT no início da fase 
poderá ser descartado caso a fase anterior tenha entrado na formação de interesse com peso 
de fluido superior ao necessário para perfuração da fase objetivo ou se existir previsão de 
perdas e falhas ao longo da fase, fazendo com que o DFIT no início dela seja inútil. 
Nota: em formações com heterogeneidade do reservatório, o DFIT realizado com uma parte da 
formação exposta não garante a manutenção do limite medido para o restante da fase, uma 
vez que podem aparecer vugs e cavernas ao longo da perfuração. 
Ao final da fase, deve ser avaliado com a equipe de projeto a realização um DFIT, levando-se 
em conta o histórico operacional dos poços de correlação, para conhecer o limite de pressão 
durante a operação de cimentação, ou mesmo para decidir o peso de fluido a ser utilizado para 
matar o poço antes das próximas operações. Não é recomendado DLOT nesse momento pelo 
risco de indução de fraturas e consequente diminuição da janela operacional. Em caso de 
constatação de perdas durante a perfuração esta operação deve ser revista. 
A realização do DPPT é importante nos cenários de perfuração MPD com janela estreita e 
perdas severas. Recomenda-se que seja realizado assim que for verificada uma formação com 
permeabilidade adequada (podendo ser verificada através do LWD), tal que permita a 
identificação do microinfluxo, sob risco de não ser possível realizá-lo caso seja constatada 
perda de fluido antes da realização do teste, conforme recomenda o padrão de DPPT. 
A não realização do DPPT nesse momento poderá impactar a estratégia de combate à perda 
de fluido, pois não se poderá reduzir a pressão no poço devido ao desconhecimento do limite 
inferior da pressão de poros, podendo ocasionar influxo ou fluxo cruzado no reservatório. 
A operação em MPD afeta de forma não convencional os equipamentos e recursos da sonda. 
Antes da entrega do projeto é necessária a verificação dos limites operacionais, capacidades 
da sonda e treinamento das equipes. A impossibilidade de certos alinhamentos, assim como 
limites de pressão reduzidos podem inviabilizar certas operações e devem estar previstos no 
projeto. 

## Página 12

 
12 
 
8. PROJETO DE FLUIDOS DE PERFURAÇÃO 
O projeto de fluidos influencia diretamente nas pressões do poço e de superfície, através da 
pressão hidrostática e das perdas de carga no anular do poço. Os fluidos utilizados nas 
operações MPD devem seguir os mesmos critérios que os fluidos utilizados em operações 
convencionais. Atenção deve ser dada aos efeitos que suas propriedades terão no 
gerenciamento de pressões como, por exemplo, efeitos da alteração da reologia nas pressões 
do poço, visto que estes têm impacto direto no cálculo da pressão de superfície necessária no 
choke MPD. As características e propriedades dos fluidos são insumos do projeto de MPD, e 
devem ser reavaliadas conforme evolução do projeto e planejamento da intervenção em MPD. 
Nota: Qualquer alteração ou variação nas propriedades dos fluídos deve ser comunicada ao 
projetista MPD do poço, visto que deverá ser efetuada nova avaliação dos parâmetros de 
perfuração. Atenção especial também deve ser dada nas alterações das propriedades durante 
a operação. 
Quando houver uso de fluido hidrostaticamente sub-balanceado, o projeto deve seguir os 
seguintes limites de contrapressão durante as operações programadas: 
A pressão de trabalho na superfície deverá ser limitada a 750 psi. Essa limitação deve ser 
considerada para as operações programadas (isto é, em projeto) para a perfuração. Eventos 
de controle de poço podem ser programados em até 80% da pressão configurada para abertura 
das PRVs. 
Caso a simulação hidráulica de projeto resulte em pressões superiores ao recomendado acima, 
deverão ser observadas alternativas que permitam a redução da contrapressão na superfície, 
entre elas: 
 Reduzir vazão pela coluna e utilização de ferramentas low flow no BHA 
 Utilizar fluido com baritina micronizada, de forma a reduzir a reologia 
 Utilizar BHA e DP de menor diâmetro externo 
 Modificar a configuração do poço, aumentando o diâmetro do anular 
Após a análise das possibilidades de redução da SBP planejada, caso ainda assim seja 
necessário utilizar pressões acima de 750 psi, observar se há margem suficiente para os 
mecanismos anti sobrepressurização (PRV, HL, SPL) e margem para o controle de poço. 
Nota: Poderá ser adotada a estratégia de entrar no reservatório com pressões na superfície de 
até 1000 psi durante um intervalo de perfuração de até 48h, a partir do corte da sapata. Tal 
estratégia é normalmente adotada em poços exploratórios, pois poderá reduzir a necessidade 
de sucessivas reduções no peso de fluido após a medição da pressão de poros. Caso as 48h 
sejam excedidas o elemento de vedação da cabeça rotativa deve ser trocado caso tenha 
operado acima de 750 psi, conforme padrão PERFURAÇÃO COM CONTRAPRESSÃO NA 
SUPERFÍCIE (MPD/SBP). 
Para as operações de completação e Workover o limite de pressão na superfície será de 1000 
psi, visto que os dados de pressão do reservatório são conhecidos. 
Os setpoints dos mecanismos de controle de sobrepressurização (PRVs, dispositivos de 
liberação de pressão dos chokes MPD, PCVs) e as pressões de teste devem ser ajustados 
conforme tabela 1, em psi: 
 
Tabela 1: 

## Página 13

 
13 
 
 
Pressão de teste: Pressão de teste dos equipamentos MPD. Definido de forma a permitir o 
teste sem ultrapassar o limite dos equipamentos (2000 psi). 
PRV: Valor considerado para a PRV do buffer manifold ou linhas de chegada. As demais PRVs 
poderão ser ajustadas para a pressão com uma margem 20% abaixo das pressões máximas 
das linhas de superfície. 
Proteção choke B: Pressão a ser considerada na proteção contra sobrepressurização 
utilizada pela prestadora de serviço MPD Nota: Caso seja utilizada Weatherford, a lógica 
deverá ser invertida com o HL conforme tabela.  
SBP estático máx: Pressão limite a ser considerada na operação MPD de forma estática. 
SBP din max:  Pressão limite a ser considerada na operação de forma dinâmica. 
A recomendação de limitar a pressão de trabalho em 750 psi considera três pontos principais: 
aumentar a vida útil dos elementos de vedação, que diminui com o aumento da pressão de 
trabalho; minimizar a intensidade de um influxo em caso de falha do sistema MPD; e aumentar 
a margem para a reação do sistema em caso de influxo, já que ao trabalhar com alta 
contrapressão perde-se margem no caso da PP estar acima do previsto em projeto, o que é 
potencializado em poços exploratórios. 
Nota: Poderá ser avaliado utilizar contrapressões maiores (até 1000 psi) nos casos onde a PP 
é bem conhecida ou a operação tem previsão de duração no projeto de até 48h (tempo entre a 
pressurização do riser e o momento de liberação de pressão do riser pelo isolamento da 
formação por outra barreira), desde que devidamente discutido e com contingências listadas 
para diminuição da pressão na superfície. Exemplos: Descida de cauda na completação inferior, 
início da fase até realização de DPPT ou medição da pressão. 
A seleção do peso de fluido deve considerar as incertezas tanto nos dados de geopressões, 
como nas estimativas das pressões de operação (pressões de bombeio, pressões de anular, 
pressões de superfície, etc). O projetista do poço, em conjunto com o projetista de fluido e de 
MPD, deverá determinar a pressão no Anchor Point, bem como o peso de fluido, considerando 
que em fases mais rasas ou muito extensas, é possível que a contrapressão utilizada seja muito 
alta e fique próxima ao limite de resistência da formação na sapata anterior. 
Para cada um dos fluidos do projeto devem ser feitas análises de hidráulica para as operações 
e vazões previstas no poço, incluindo considerações de carreamento de cascalho.  
Nota: Para as simulações hidráulicas de projeto poderão ser utilizados BHAs padrões, uma vez 
que a diferença nas perdas de carga no anular entre o BHA padrão e o BHA real é desprezível. 

## Página 14

 
14 
 
As pressões na superfície devem estar de acordo com os limites operacionais dos 
equipamentos de superfície e às melhores práticas de segurança. 
As bombas e camisas adequadas deverão ser escolhidas para vazão e pressão a que a 
perfuração estará submetida. Atentar que se forem utilizados jatos reduzidos na broca devido 
à possibilidade de conversão para FMCD e/ou turbina, a pressão de bombeio será maior para 
a perfuração em SBP. 
Quando perfurando em PMCD, a simulação da pressão de bombeio deve considerar o cenário 
de desbalanceio entre interior da coluna e anular, pelo impacto da pressão de poros e 
consequente diferencial entre SAC e LAM. 
A limpeza do poço em MCD pode ser dificultada pela utilização de AGMAR como fluido SAC. 
Deve-se realizar simulação de limpeza com análise de sensibilidade da vazão e ROP para este 
cenário, considerando a zona de perda logo abaixo da sapata. A perfuração não deve exceder 
o ROP limite para limpeza adequada do poço. 
Deve-se incluir recomendação de utilização de tampões viscosos, bem como acompanhamento 
dos indicativos de má limpeza (verificação do torque, drag e ECD, monitoramento por equipe 
PWDA). O projeto de perfuração deve considerar os cenários de limpeza como limitantes ao 
ROP e estratégias de repasse do poço. 
Caso esteja prevista a realização de DPPT, a escolha do peso do fluido deve levar em 
consideração:  
 A mínima pressão no poço aberto na curva de Pressão de Poros mais provável e margem 
para redução da pressão do poço além dessa estimativa; 
 Perdas de carga na superfície, com a vazão de perfuração (coluna de perfuração) e/ou 
vazão de conexão (bomba da booster). 
 Perdas de carga em poço aberto e revestido. 
Nota: em alguns cenários não é possível realizar o DPPT com a vazão normal de perfuração, 
não sendo possível baixar a pressão do poço abaixo da PP. Dessa forma, pode ser necessário 
reduzir a vazão para o mínimo possível que tenha leitura em tempo real do PWD. Para isso a 
vazão e as perdas de carga nessa condição de vazão reduzida devem ser conhecidas. 
Inicialmente, o ponto de ancoragem pode ser definido na sapata ou topo da formação 
permeável. Caso se verifiquem perdas durante a perfuração da fase, o AP pode ser fixado na 
região mais provável de ocorrência de problemas operacionais, tendo cuidado de manter a 
pressão no poço aberto sempre acima da pressão de poros. Diferentes fatores podem alterar a 
localização e a pressão do ponto de ancoragem, incluindo: peso do fluido, vazão, pressão 
estática de superfície aplicada, pressão dinâmica de superfície aplicada, reservatórios 
atravessados na fase, geopressões (poros, fratura, colapso inferior e superior), profundidade 
dos reservatórios, entre outros.  
Em caso de operação em PMCD, a definição do peso do LAM deve considerar a pressão de 
poros e a limitação dos equipamentos de superfície, incluindo as incertezas, conforme calculado 
na fórmula abaixo. Deve ser considerado também a perda de carga para injeção do fluido pelo 
anular e a pressão necessária para a injeção no reservatório, que pode se elevar ao longo da 
perfuração. 
𝑃௅஺ெ =  ∆𝑃ௌ஻௉௦௧௔௧௜௖+ ∆𝑃௕௢௠௕ + ∆𝑃௜௡௝௙௥௔௧+ ∆𝑃௠௜௚௚௔௦ 
- PLAM = pressão de injeção do fluido LAM pelo Flowspool; 
- ∆PSBPstatic = SBP com anular com fluido LAM e livre de gás/óleo; 

## Página 15

 
15 
 
- ∆𝑃௕௢௠௕  = Pressão de fricção do poço e das linhas de superfícies; 
- ∆𝑃௜௡௝௙௥௔௧ = Delta de pressão necessário para injeção do fluido na formação; 
- ∆Pmiggas = Delta de pressão adicional a SBP devido a diferença hidrostática do fluido invasor 
e do fluido LAM. 
A vazão mínima para injeção de LAM pelo anular nas operações PMCD deverá seguir a 
simulação hidráulica de bullheading ou vazão de controle pelo anular para evitar migração de 
fluido da formação 
Para poços com FMCD contingente, deverá ser realizada simulação hidráulica de bullheading 
ou vazão de controle pelo anular para evitar migração de fluido da formação. Devido ao fluido 
SAC não ter reologia suficiente para retardar a migração do fluido da formação pelo anular, sua 
velocidade no anular deverá impedir a migração do fluido da formação. Dessa forma, a injeção 
deverá ser contínua. O planejamento da operação deve prever a continuidade da injeção pelo 
anular do poço do início ao fim da operação FMCD e um plano de contingência em caso de 
problemas. 
Também devem ser produtos das simulações hidráulicas as pressões esperadas durante o 
bombeio no anular. Estas pressões devem ser comparadas com os limites operacionais dos 
equipamentos envolvidos. O cálculo da vazão pelo anular deverá ser realizado conforme uma 
das opções abaixo, em ordem de prioridade: 
 
1. Simulação de bullheading ou vazão de controle pelo área de segurança de poço , , 
conforme padrão PE-1PBR-00733 - SIMULAÇÕES HIDRÁULICAS DE CONTROLE DE 
POÇO: CONCEITOS E ELABORAÇÃO 
2. Na impossibilidade do método 1, utilizar o método do shut in para determinação das 
vazões mínimas de injeção. Utilizar fator de segurança 2 para fluido base aquosa. 
 
𝑉𝑔𝑚= 12 ∗𝑒(ି଴,ଷ଻∗௅஺ெ ) 
Vgm - Velocidade de migração do gás (pés/seg) 
LAM - Peso do fluido de anular (lb/gal) 
Nota: Deve ser feito o monitoramento e verificação da necessidade de aumentar a vazão de 
injeção. 
É recomendada a utilização do mesmo fluido de perfuração do modo SBP para o LAM do modo 
PMCD, de modo a evitar necessidade de troca de fluidos. 
Em PMCD, no mínimo, deverá ser injetado 50 bbl de fluido LAM pelo anular a cada 6h, de forma 
a quebrar o efeito gel e permitir a leitura nos sensores de pressão de superfície, de eventual 
influxo no poço. As injeções no anular de poços com PMCD, devem ocorrer sempre a pressão 
no anular ultrapassar o limite pré-estabelecido, devendo também ser de conhecimento dos 
envolvidos as vazões e volumes mínimos para injeção. 
Em ambiente offshore, o fluido de sacrifício (SAC) deve ser AGMAR, salvo em ocasiões nas 
quais o volume necessário e a logística permitam outro tipo de fluido. Deve ser feita uma análise 
sobre o uso de inibidores de incrutação e bacterícida no SAC, de forma a prevenir danos à 
formação devido a injeção contínua de SAC. Em operações PMCD, o SAC deve aumentar a 
pressão de bombeio devido ao desbalanceio hidrostático, enquanto em operações FMCD, deve 
ocorrer uma queda no nível de fluido no anular. Para a simulação de carreamento de cascalho 
com fluido SAC, considerar zona de perda logo abaixo da sapata e broca na profundidade final 
do poço. No caso de uma operação FMCD, prever a capacidade de injeção contínua no anular 

## Página 16

 
16 
 
e ajuste no fluido de sacrifício.  
Ao utilizar água do mar como SAC, deve-se deslocar fluido com bactericida ao final da 
perfuração para inibição das BRS nas bordas do poço. Para a interação rocha-fluido, os estudos 
realizados para o campo de Marlim Leste e Marlim sul evidenciaram o baixo impacto no 
reservatório relativo ao dano à formação pela injeção de água do mar, não sendo necessários 
estudos para os poços com MCD como contingência. 
A hidráulica do poço deve ser simulada em software adequado, podendo ser realizada pelo 
prestador do serviço de contrapressão, projetista MPD ou pelo projetista de fluidos. Deve ser 
realizada análise de sensibilidade para peso de fluido, taxa de perfuração e vazão, conforme 
insumos do projeto MPD. 
Devem ser simulados os cenários SBP (perfuração, conexão, alargamento, testemunhagem, 
entre outros) e o cenário contingente MCD com relação à hidráulica e limpeza do poço, já que 
esta última representa um dos limites inferiores da vazão pela coluna. 
O projeto deve incluir a contingência de ajuste de peso do fluido quando houver diferença da 
pressão de poros encontrada na fase. Nesses casos é preferível manter a circulação pela 
coluna até o ajuste do peso de fluido. 
Através de simulações em software adequado, deverão ser calculadas as pressões na 
superfície para as diversas etapas da perfuração (perfuração, conexão, manobra, 
testemunhagem). 
A pressão de bombeio deverá ser calculada nas simulações de hidráulica considerando os 
diferentes BHA’s e colunas de trabalho, assim como os diferentes fluidos que possam ser 
utilizados na intervenção com sistema MPD. 
Em ambiente offshore, o fluido de sacrifício (SAC) deve ser preferencialmente AGMAR, salvo 
em ocasiões nas quais o volume necessário e a logística permitam outro tipo de fluido 
8.1. Circulação de influxo 
A possibilidade de circulação de influxos pelo sistema MPD deverá atender às normas e 
padrões vigentes, considerando os volumes e pressões máximas definidas para esta operação. 
A análise na fase de projeto deverá considerar as pressões esperadas no poço, bem como 
analisar as possibilidades de circulação para o caso das pressões máximas esperadas 
utilizando simulações em software adequado ou limitando as pressões e volume de acordo com 
o descrito no padrão de circulação de influxo MPD e padrão de simulação de influxo do SIP. 
9. PROJETO DIRECIONAL / BHA 
Deverá ser realizada validação do BHA proposto pelo projetista direcional. Algumas 
recomendações a serem observadas para a validação seguem abaixo. 
É recomendado que a taxa de transmissão dos dados de PWD seja de 5 dados por minuto e, 
no mínimo, 1 dado a cada 20s. Para isto deverá ser avaliada a quantidade de perfis e 
ferramentas que compõe o BHA. 
Deve ser verificada a mínima vazão de operação das ferramentas de MWD/LWD e ferramenta 
direcional. Caso esses limites não estejam de acordo com as vazões necessárias para as 
operações, solicitar a troca das ferramentas (normalmente são necessárias ferramentas com 
baixa vazão de acionamento para atender aos cenários em que se utilizam técnicas MPD). 
Considerar a vazão pelo alargador, caso esteja presente no BHA. 
Deve ser avaliada a pressão (perda de carga abaixo da ferramenta) necessária para 
funcionamento das ferramentas do BHA, tais como alargador e ferramentas direcionais. 

## Página 17

 
17 
 
A utilização de turbina apresenta algumas desvantagens em relação a outras ferramentas 
direcionais, pois: gera uma perda de carga mais alta na coluna, podendo chegar próximo ao 
limite da pressão de bombeio (principalmente cenário de perfuração PMCD e pressão de poros 
mais elevada); possui recomendações específicas quanto ao controle de influxo, como pode 
ser verificado no padrão PE-2POC-01113; tem um range de vazão de trabalho pequeno, que 
pode atrapalhar na flexibilidade de adequação do perfil de pressões no anular. 
Caso seja previsto utilizar motor de fundo, deve-se estar atento à possibilidade de conversão 
para MCD, pois a borracha do estator é dependente das características do poço (principalmente 
temperatura) e do fluido utilizado (água do mar para operação em MCD).  
Outro ponto de cuidado em caso de utilização de motor de fundo na perfuração é com uma 
momentânea diminuição da vazão no anular do poço no caso de stall (travamento da broca) 
que não é compensada pelo choke MPD (os modelos hidráulicos utilizam a vazão de entrada), 
podendo ser crítica quando se está trabalhando com pequeno overbalance. Dessa forma, deve-
se utilizar um motor de alta potência, de forma a evitar a ocorrência de stall. Acompanhamento 
contínuo deverá ser recomendado para o acompanhamento direcional, pois o desgaste da 
broca poderá facilitar o stall do motor, variando as vazões no anular sem possibilidade de 
resposta do choke em tempo adequado. Além disso, é importante recomendar às equipes de 
direcionais e da sonda que, em caso de stall severo, não diminuam a vazão de forma abrupta, 
sob risco de não permitir que o choke compense a pressão no poço adequadamente podendo 
colocar o mesmo em situação underbalance. 
Caso seja alta a probabilidade de conversão para FMCD, evitar a utilização de ferramentas 
MWD de pulso negativo, pois é provável que não funcionem devido ao desbalanceio 
hidrostático entre coluna e anular. 
Verificar a real rotação de coluna que será utilizada na operação, pois a depender da cabeça 
rotativa utilizada, pode impactar no limite de pressão do conjunto de vedação. 
Em poços mais profundos, a depender das colunas de DP disponíveis na sonda, pode ser 
necessário utilizar coluna combinada devido as cargas axiais. Nesse caso, deverá ser verificado 
se existe conjunto de vedação disponível para o diâmetro de coluna que será utilizado. 
Recomendar treinamento prático (padrão PE-2POC-01115) de troca do conjunto com 
contrapressão durante o fingerprint. 
No cenário de perfuração MCD, todo o cascalho gerado deverá ser carreado por água do mar 
e injetado na formação, por isso, deve-se utilizar, preferencialmente, brocas que geram 
cascalhos de menores dimensões para facilitar este carreamento e injeção na formação. É 
importante também verificar a expectativa de durabilidade da broca, evitando que seja 
necessário manobrar antes do final da fase. 
A mínima quantidade de NRVs no BHA deve ser de 02 (duas), sendo que obrigatoriamente uma 
acima do sub de circulação (PBL). Avaliar possibilidade de posicionar uma terceira NRV na 
coluna, de forma que fique acima do BOP ao final da perfuração, tendo conhecimento que a 
terceira NRV pode impedir o uso de ferramentas como coliding tool ou string shot. 
Não é recomendado utilizar ferramentas com fonte radioativa (caso da maioria dos perfis de 
densidade e neutrão) no BHA quando for previsto MCD devido ao maior risco de prisão da 
coluna, especialmente poços direcionais de alto ângulo. Optar por ferramentas que não utilizam 
fonte, disponíveis com algumas companhias contratadas (a depender da ferramenta e diâmetro 
necessários). 
Nas operações de FMCD deve-se garantir a capacidade de comunicação das ferramentas do 
BHA. Como o nível de fluido no anular fica abaixo da MR, em alguns casos é necessário 
adicionar ao BHA um flow restrictor ou diminuir o TFA da broca para que o interior da coluna 
permaneça cheio e possibilite a comunicação, no mínimo enquanto houver circulação pela 

## Página 18

 
18 
 
coluna. Além disso, deve-se configurar as ferramentas para o envio dos dados on demand após 
a conexão, pois assim que for reestabelecida a circulação pela coluna, será necessário algum 
tempo até a coluna ser preenchida de fluido. Abaixo pode ser vista a fórmula para determinação 
do TFA da broca. 
𝑇𝐹𝐴=  ඨ 𝜌ௌ஺஼ ×  𝑄ଶ
12032 ×  (∆𝑃ௗ௘௦௕ − ∆𝑃௖௢௟− ∆𝑃஻ு஺ ) 
𝜌𝑆𝐴𝐶 = Massa específica do fluido SAC, Lb/gal; 
Q = Vazão pela coluna, gpm; 
∆𝑃𝑑𝑒𝑠𝑏 = Desbalanceio hidrostático entre interior da coluna e anular, psi; 
∆𝑃𝑐𝑜𝑙 = Perda de carga da coluna, psi; 
∆𝑃𝐵𝐻𝐴 = Perda de caga no BHA, psi; 
10. ASSENTAMENTO PRELIMINAR DE SAPATAS 
É necessário avaliar o impacto da utilização das técnicas MPD no assentamento das sapatas. 
Em casos críticos de poços com alta perda de carga (fases extensas, ERW, diâmetros 
reduzidos), a sapata anterior pode ter aumento significativo de pressão durante as conexões 
ao longo da perfuração no caso de utilização do achor point no fundo do poço, podendo trazer 
a necessidade de alteração no planejamento do assentamento das sapatas. Pode ocorrer 
também em poços com pequena LDA. 
Por outro lado, o MPD traz a possibilidade de flexibilidade operacional. É função do projetista, 
verificar o impacto do MPD no projeto de assentamento de sapatas e adequar o projeto  de 
forma a otimizar os recursos e garantir a segurança operacional. 
Caso a fase a ser perfurada seja carbonática, é improvável que seja necessário utilizar fase 
contingente, pois caso sejam encontradas perdas severas, o sistema permite a conversão da 
perfuração para MCD. Ressalva pode ser feita aos casos nos quais a perda de fluido é muito 
alta para se conviver e dar prosseguimento à perfuração e muito baixa para a conversão para 
MCD. 
No caso de perfuração utilizando sistema MPD, o volume do fluido invasor para cálculo da 
tolerância ao kick pode ser reduzido através de análise de risco específica, conforme item da 
norma N-2752 devido a capacidade do sistema de detectar influxos com volumes inferiores a 
perfuração em modo convencional.  
11. PROJETO DE REVESTIMENTOS 
O detalhamento do projeto de revestimentos deve seguir o padrão da área especialista, com as 
seguintes considerações:  
As operações de MPD irão implicar em carregamentos diferentes no interior do revestimento 
quando comparado a operações convencionais, e estes devem ser considerados no projeto de 
revestimento respeitando os fatores de segurança de acordo com os padrões e normas 
vigentes.  
Como critério de dimensionamento em relação a pressão interna no revestimento, o nível 
estático deve ser calculado com fluido de perfuração mais pesado utilizado na fase. A pressão 
externa continua sendo calculada normalmente.  
O perfil de pressão do MPD, assim como a redução do volume de influxo pode acarretar em 
um menor número de revestimentos na fase. Deve ser revisto pelo projetista a possibilidade de 

## Página 19

 
19 
 
otimização das fases do poço. 
As operações de FMCD irão implicar em um cenário semelhante ao de queda no nível de fluido. 
As pressões de reservatório e os pesos de fluido considerados deverão contemplar as 
condições previstas do projeto.  
As simulações termo-hidráulicas devem contemplar o carregamento gerado pela injeção de 
fluido pela coluna e/ou anular que ocorre durante as operações de MCD (principalmente em 
FMCD devido à injeção contínua pelo anular). Essas injeções podem gerar carregamentos 
superiores aos de outras operações como acidificação, operação de injeção, entre outros, 
devendo ser avaliada para garantia de manutenção da integridade do poço. 
A descida de revestimento com MPD em poço sub-balanceado é restrita a revestimentos com 
comprimento inferior à LDA. Para essa operação, deverá ser realizado planejamento específico, 
dada sua complexidade, contemplando uma análise de risco específica para esta operação, 
considerando, por exemplo, a necessidade de inclusão de NRVs na coluna de assentamento. 
Cuidados como garantia de compensação da pressão durante a descida pelo software de 
controle MPD, modelo hidráulico ajustado aos elementos que serão descidos e considerações 
sobre o efeito gel do fluido deverão ser observados. 
A cimentação de revestimentos ou liners deverá ser planejada rigorosamente e observados 
todos os cuidados para garantir a integridade do CSB primário durante a operação, bem como 
garantir a integridade do poço após a cimentação e eventuais contingências. Alguns softwares 
das companhias contratadas são capazes de utilizar diversos fluidos com reologias diferentes, 
inclusive simular o efeito de free fall. Contudo, devido à ausência de sensor no fundo, não se 
pode garantir a manutenção da pressão no patamar adequado. Portanto, criterioso 
planejamento e análise de risco são necessários caso se opte por realizar essa operação. 
12. RISER ANALYSIS E ESTRUTURA DE POÇO 
É necessário realizar um Riser Analisys específico considerando as condições de operação 
MPD (colapso, gráficos LDA x peso máximo de fluido) para cada poço, conforme norma API 
RP 92S Managed Pressure Drilling Operations-Surface Back-pressure with a Subsea Blowout 
Preventer - First Edition. É necessário efetuar estudo dos efeitos do MPD / MCD no riser, 
incluindo a análise de riser recoil. A variação no nível de fluido no interior do riser (quando 
perfurando em FMCD) gera alterações no comportamento do sistema podendo alterar os 
esforços na cabeça do poço. A operação de MPD / MCD provoca variações da pressão do 
interior do riser devendo o equipamento ser adequado. Além disso, é importante que o aumento 
da rigidez da flex joint seja refletido no WSOG, com redução do passeio da sonda. 
13. EQUIPAMENTOS 
Para uma operação MPD (SBP/MCD) é necessário fazer uma verificação prévia das 
características da sonda com as necessidades do projeto de MPD e MCD, incluindo layout de 
superfície e sub-superfície e alinhamentos disponíveis da sonda. A adequação da sonda às 
operações previstas pela Petrobras é verificada durante a negociação e recebimento. Contudo, 
algumas unidades possuem características ligeiramente diferentes que podem impactar no 
projeto: linha de injeção de SAC em PMCD por apenas um dos tramos do stand pipe manifold, 
linha conectando apenas um dos lados do choke manifold e o buffer manifold, presença de 
coriollis na entrada das bombas, junta de riser MPD (relativo à performance e tempo de descida) 
de nova geração, presença de 2 manifolds MPD, entre outras. 
Verificar se o buffer manifold possui todos os alinhamentos disponíveis para as operações 
previstas. Caso não seja o fato, deve-se verificar o impacto das limitações de alinhamentos com 
as operações esperadas.  

## Página 20

 
20 
 
Algumas unidades de perfuração são contratadas para projetos específicos e, apesar de 
atenderem o cenário objeto do contrato, não atendem necessariamente a todos os itens da ET 
Petrobras. Portanto, é necessário que sejam observadas as particularidades relativas aos 
limites operacionais dos equipamentos caso a unidade seja utilizada fora do projeto para a qual 
foi contratada. 
Faz-se necessário verificar se o BOP / riser são capazes de suportar o diferencial de pressão , 
de fora para dentro, esperado para o projeto de perfuração do poço, caso contrário deve ser 
discutido e registrado plano de contingência ou mudança do recurso selecionado para o projeto. 
Solicitar à sonda que sejam utilizados anéis de vedação adequados aos níveis de pressão 
esperados nesses equipamentos. 
Quando operando em FMCD, o cenário de fechamento do BOP (fechamento do poço ou 
desconexão) pode ser crítico para as gavetas e anulares, resultando em uma pressão superior 
na parte de cima destes elementos e, consequentemente, em uma força resultante no topo. 
Deve-se verificar a severidade desse cenário e definir um plano de ação para esse caso. 
Verificar a capacidade de bombeio de AGMAR, capacidade de bombeio simultâneo de 
diferentes tanques, disponibilidade de tanques para uso de diferentes fluidos necessários para 
a perfuração e contingência operacionais.  
Definir a configuração das bombas, isto é, quais estarão alinhadas para a coluna e quais estarão 
alinhadas para a booster. Para fases de 8 ½” a recomendação é manter 2 na coluna e 2 na 
booster. Para fases 12 ¼” a recomendação é manter 3 na coluna e 1 na booster, mudando para 
2 bombas na boster durante a manobra. Deve-se avaliar também a distribuição das bombas 
por barramento elétrico e o modo de operação da sonda, se é com barramento aberto ou 
fechado, para evitar a queda de todas as bombas durante a operação e consequente 
despressurização do poço em caso de blackout parcial. 
Verificar os equipamentos de segurança disponíveis para alívio de pressão na sonda e a sua 
lógica de atuação. Estes podem ser PRV (caso a não tenha rearme, uma avaliação de risco 
deve ser conduzida) ou PCV. 
O limite superior dos chokes do sistema MPD deve ser 80% da máxima pressão permitida na 
superfície, com a juste das demais contingências conforme item 8. A máxima pressão permitida 
na superfície é a menor entre: capacidade do Riser de perfuração, capacidade da RCD e 
capacidade dos equipamentos de superfície, devendo ser definido na etapa de projeto. A 
definição do projeto definirá a pressão do teste de pressão que servirá de referência para os 
demais limites de pressão. 
Nota: Na definição do limite superior, ele não deverá ser um impeditivo para aumento da 
pressão para controle de influxo. Sendo assim, caso haja expectativa de entrar em outra 
formação ou perfurando sal com possibilidade de lentes sobrepressurizadas, utilizar valores da 
PRV de acordo com o limite dos equipamentos. 
Além das válvulas de segurança da sonda (PRV ou PCV), os manifolds MPD também contam 
com mecanismos de segurança para evitar a sobrepressurização. 
WEATHERFORD: O limite é aplicado na função High Limit (HL) do Sistema MPD. Ao atingir 
90% do HL o sistema não permitirá aumentar a pressão e irá gerar um alarme. Caso seja 
ultrapassado o HL, o choke irá abrir totalmente, despressurizando o poço. Dessa forma, caso 
esteja utilizando esse sistema, é recomendado que a pressão da PRV (caso seja rearmável) ou 
PCV fiquem abaixo do limite do HL. 
HALLIBURTON: O limite é aplicado na função SPL (Secondary Pressure Limiter) do sistema 
MPD. Ao atingir a pressão limite, o choke C, quando disponível, irá abrir conforme definido pelo 
operador até a pressão ser drenada para o patamar pré-definido. 

## Página 21

 
21 
 
De acordo com a cabeça rotativa utilizada, deverá ser verificado se o material da borracha dos 
selos de vedação está adequado ao fluido do poço, limites de pressão, temperatura do fluido 
da formação e temperatura do fluido durante a operação. 
14. ÁRVORE DE DECISÃO DE COMBATE A PERDAS E CONVERSÃO PARA MCD 
Deverá ser elaborada uma árvore de decisão de perdas e conversão entre modos de operação 
(SBP para PMCD ou FMCD por exemplo) para guiar a decisão durante a operação. Deverão 
participar dessa elaboração o projetista de fluidos, o projetista da intervenção e o projetista 
MPD. Essa matriz deverá considerar os seguintes pontos para ser elaborada: 
 Mínima pressão de poros, obtida durante o DPPT. Caso não tenha sido realizado, utilizar 
a PP mais provável; 
 Capacidade de fabricação de fluido de perfuração; 
 Volume de fluido de perfuração disponível; 
 Mínima vazão dos equipamentos do BHA; 
 Mínima vazão para limpeza do poço com fluido de perfuração; 
 Mínima vazão para limpeza do poço com SAC; 
 Mínima vazão de injeção no anular para conter a migração do influxo; 
 LCM a ser utilizado em cada etapa da matriz; 
De posse desses dados, utilizar o modelo presente no Anexo C para elaboração da matriz. 
15. TESTE DE PRESSÃO DOS EQUIPAMENTOS MPD 
Deve ser recomendado o valor, o momento e a periodicidade dos testes de pressão dos 
equipamentos MPD de acordo com as normas e padrões vigentes. 
O teste de pressão dos equipamentos MPD deverá ser realizado antes da fase a ser perfurada 
com MPD. Após o primeiro teste, os demais testes periódicos ao longo da perfuração da fase 
poderão ser somente funcionais. 
O valor do teste de pressão será seguir a tabela 1. Caso sejam previstos valores maiores de 
pressão na superfície, ou a sonda esteja em recebimento, a pressão de teste deverá ser 2000 
psi. 
Os testes de pressão para as linhas de superfície, manifold MPD e equipamentos de riser, 
podem ser realizados em sua maior parte fora do caminho crítico, devendo ser programados 
durante descida do BHA ou ferramenta para teste do BOP. 
Os testes que necessitam ser realizados no caminho crítico podem ser realizados conforme 
uma das opções: contra a ferramenta de teste do BOP, contra a gaveta de teste, contra o 
revestimento após a descida do BHA. 
Em qualquer uma das opções acima, devido ao tamanho da câmara a ser pressurizada, é 
recomendado que se utilize o método de teste otimizado, no qual não há despressurização da 
câmara riser-poço. 
Caso o teste seja realizado com BHA de perfuração no fundo, recomenda-se que seja feito 
antes da substituição do fluido para não haver a necessidade de nova troca de fluido em caso 
de teste falho. 

## Página 22

 
22 
 
16. SUBSTITUIÇÃO DE FLUIDO E CORTE DE CIMENTO 
Caso seja previsto utilizar fluido hidrostaticamente underbalance, deverá ser previsto teste 
negativo antes de submeter o poço a condição de underbalance, uma vez que a contrapressão 
em superfície não é mantida durante todas as etapas do fingerprint. 
A substituição de fluido poderá ser realizada com auxílio do sistema MPD, de forma que seja 
possível realizar de forma mais rápida e com maior controle. Caso seja feita em paralelo com o 
corte de cimento, utilizar o alinhamento para o choke MPD e by-pass do Coriolis. 
Há a opção de realizar alguns testes do fingerprint durante a substituição de fluido e/ou corte 
de cimento a fim de ganhar tempo na operação. Verificar padrão de fingerprint MPD. 
A janela para a realização de DPPT no início da fase deverá ser observada para evitar que o 
cimento cortado esteja chegando à superfície, pois, apesar dessa operação não requerer poço 
limpo de cascalhos, ela não poderá ser iniciada enquanto o fluido retornado tiver excesso de 
cimento. 
17. FINGERPRINT 
Deverá ser realizado fingerprint para intervenção da fase conforme padrão de fingerprint MPD. 
O fingerprint deve ser realizado com o mesmo BHA e fluido com o qual a fase será perfurada. 
Caso não seja possível, discutir quais etapas deverão ser repetidas após troca de BHA ou do 
fluido, pois essas mudanças podem alterar a hidráulica e respostas do poço. 
É importante que os parâmetros sejam calibrados para todas as etapas da fase, sejam elas 
perfuração, alargamento, testemunhagem, completação ou workover. Adicionalmente, deve-se 
prever algumas calibrações para circuitos de superfície com vista a operações de perfilagem e 
completação, caso necessário. 
Deverá ser observado o direcionador abaixo de acordo com a estratégia traçada para a fase a 
ser perfurada. Consultar o padrão de FINGERPRINT MPD PE-1PBR-01326. 
18. PERFURAÇÃO DA FASE 
Deve ser avaliada e recomendada se o retorno de fluido dever ser realizado por uma ou duas 
mangueiras de acordo com a vazão e perdas de carga esperadas. 
Deverão ser verificados os limites de pressão para a contrapressão na superfície. O limite de 
pressão de superfície é 2000 psi. Contudo, quando há giro na coluna esse limite diminui de 
acordo com o envelope operacional da cabeça rotativa (que deverá estar anexado ao projeto). 
Deve-se considerar ainda a resistência da formação mais frágil da fase, bem como a resistência 
à pressão interna dos revestimentos. Deve ser de conhecimento da operação que o limite de 
pressão na superfície, conforme item 8 deste padrão, só devem ser excedidos em casos 
extraordinários e com avaliação de risco que inclua a equipe especializada MPD. 
Devem ser recomendados os modos de controle da pressão durante as operações a serem 
realizadas, como perfuração, conexão, manobra (modo hidráulico, SBP, etc). 
A cada nova descida de coluna o conjunto de vedação deverá ter todos seus elementos de 
vedação novos, sendo o reaproveitamento de elementos de vedação não recomendado. 
O projeto deverá descrever em linhas gerais as principais etapas da fase e seus alinhamentos, 
tais como perfuração, MCD, teste de BOP, além de determinar a necessidade de instalação de 
protective sleeve, caso seja necessária. 
É importante incluir no projeto os momentos de instalação dos conjuntos de vedação ou bucha 
de proteção, a fim de permitir o melhor planejamento das operações, bem como suas durações. 

## Página 23

 
23 
 
19. TESTEMUNHAGEM 
Deve ser solicitado no projeto a utilização de um Conjunto de Vedação novo para a operação 
de testemunhagem. Considerando que é uma operação demorada e que a sua interrupção para 
uma eventual troca de conjunto de vedação traz riscos adicionais a operação, é importante que 
a operação não seja interrompida por falha no conjunto de vedação. 
Durante o fingerprint da fase, todos os parâmetros deverão ter sido verificados para a operação 
de testemunhagem, principalmente o modelo hidráulico e calibração dos parâmetros do 
controlador do choke MPD. O arraste da coluna nos elementos de vedação da RCD deve ser 
verificado antes do início da testemunhagem. O valor do arraste e comportamento deve ser de 
conhecimento dos técnicos da testemunhagem. 
Além da velocidade de retirada do testemunho também deverá ser considerada a pressão no 
anular do poço no programa de testemunhagem. A taxa de despressurização do testemunho 
deve ser calculada de acordo com a pressão no anular e não somente relativo à profundidade, 
pois ao retirar o testemunho acima do BOP e fechar a gaveta cega, o riser deverá ser 
despressurizado de acordo com a taxa calculada. 
O histórico de recuperação da tesmunhagem em zonas com altas perdas é de baixa eficiência. 
Como o histórico de testemunhagem com altas perdas na Petrobras é escasso e o histórico de 
testemunhagem com PMCD é nulo, deve-se observar que os mecanismos de perda (vugs e 
cavernas) são os mesmo que podem reduzir a eficiência da recuperação do testemunho, 
resultando em uma operação não efetiva. 
20. PERFILAGEM A CABO 
Deve ser abordada a estratégia para perfilagem, seja ela de apoio (no meio da fase) ou final. 
Normalmente, coloca-se o poço em overbalance para realizar a operação. Em alguns casos, 
como perfilagem de apoio, pode ser mais interessante manter o poço com fluido underbalance 
para realização da perfilagem e neste caso, é necessário um criterioso planejamento da 
operação de perfilagem com MPD. 
Devem ser verificadas as limitações da operação quanto à segurança, capacidade de pescaria 
de ferramentas em operação de corte e costura, além de calcular o custo/benefício em termos 
de tempo e qualidade do perfil (LWD x perfil a cabo), comparando com as outras opções como: 
colocar fluido overbalance no poço, perfilar apenas com ferramentas em LWD, etc. 
A disponibilidade de materiais e equipamentos deve ser confirmada, pois a operação não é 
recorrente e depende de compatibilidade entre fornecedores. 
Ao final da perfilagem, caso tenha sido amostrado fluido da formação pode-se optar por realizar 
a circulação de condicionamento do fluido pelo sistema MPD conforme uma das alternativas 
abaixo: 
 Instalar o conjunto de vedação e circular o fluido da formação pelo riser e sistema MPD. 
Permite giro da coluna, evitando que esta fique parada em poço aberto. [Recomendado] 
 Fechar o anular de superfície para a circulação. Economiza-se o tempo de instalação do 
conjunto de vedação, porém, não permite o giro da coluna durante a operação. 
NOTA: Observar o volume máximo que poderá ser circulado pelo sistema MPD, conforme 
padrão de Detecção e circulação de influxo com sistema MPD, PE-2POC-01113, e simulações 
específicas para o poço perfilado 

## Página 24

 
24 
 
21. REVESTIMENTO E CIMENTAÇÃO 
Não é possível descer revestimentos maiores que a LDA com fluido hidrostaticamente 
underbalance, a não ser que esteja disponível válvula de isolamento de revestimento. 
A descida de revestimento/ liner com MPD é possível, porém não há ferramentas de fundo para 
medição da pressão em tempo real, dependendo exclusivamente da simulação hidráulica da 
companhia de serviço. 
Para isso é necessária discussão específica envolvendo todas as disciplinas necessárias para 
a operação. 
22. COMPLETAÇÃO 
A instalação de completação com fluido hidrostaticamente underbalance deve ser limitada a um 
comprimento inferior à LDA e ser descida com coluna compatível com RCD. Assim, em 
ambiente com janela operacional estreita, perdas ou MCD, a instalação da completação deve 
se limitar à cauda inferior. Dessa forma, o poço aberto poderá ser isolado e o restante das 
operações de completação poderá ser realizado de forma convencional. A completação pode 
ser realizada de duas formas a depender da condição do poço: em SBP com circulação de 
superfície ou em MCD. 
Para a descida das ferramentas de condicionamento deverão ser observados os diâmetros dos 
equipamentos MPD de riser. Medidas de prevenção deverão ser tomadas para evitar danos 
aos equipamentos como, por exemplo, uso de protective sleeve para diâmetros superiores a 14 
¾” o caso da RCD da Weatherford. 
Uma vez que haverá conversão de MCD para SBP quando o packer for assentado (devido à 
perda de comunicação com o poço aberto), deve estar previsto no fingerprint da perfuração a 
etapa de simulação de perda, na qual se testa a abertura do choke com a diminuição da perda 
de fluido para a formação. 
Deverão ser previstas duas barreiras na coluna, sendo pelo menos uma NRV. Atentar que, a 
depender do modo de instalação da cauda inferior (considerando o assentamento do packer, 
liberação da ferramenta de instalação da cauda ou assentamento das Barreiras Mecânicas de 
Anulares, etc), pode ficar pressão trapeada na coluna abaixo das NRVs. Portanto, não se 
recomenda lançamento de esfera para assentamento do packer. 
É importante notar que, mesmo com a perfuração finalizada sem perdas, pode haver perda de 
fluido após a troca para fluido de completação, uma vez que se utiliza fluido sem obturante e 
capacidade de formar reboco, sendo necessária a conversão para MCD durante a completação. 
A contrapressão utilizada na operação de completação deverá seguir a mesma premissa da 
perfuração de não exceder os 750 psi devido à vida útil dos elementos de vedação e segurança 
de poço. Contudo, dado que a pressão de poros já seja conhecida e considerando a duração 
prevista para a operação inferior a 48h, pode-se trabalhar com pressões de até 1000 psi, 
observando os limites dos equipamentos. 
Para maiores informações sobre completação MPD deve ser consultado o padrão PE-2POC-
01257 COMPLETAÇÃO COM MPD. 
23. MUD CAP DRILLING 
As perfurações em MCD poderão ser FMCD ou PMCD a depender da pressão de poros e fluido 
utilizado. Em ambos os casos é utilizado um fluido de sacrifício que será injetado na formação 
continuamente. Os fluidos utilizados deverão estar de acordo com o projeto conforme item 8. 

## Página 25

 
25 
 
Apesar da grande disponibilidade, o SAC tem um baixo poder de carreamento dos sólidos 
produzidos na perfuração, necessitando de vazões maiores para garantir a limpeza do poço. 
Deverá ser simulado em projeto a vazão mínima para carreamento do cascalho gerado com a 
taxa prevista na operação.  
Ainda que as simulações apontem a possibilidade de altas taxas de penetração, deve ser 
recomendado iniciar de forma mais lenta e acompanhar a evolução dos parâmetros drag, torque 
e ECD e que os mesmos estejam em níveis aceitáveis. 
23.1. Pressurized Mud Cap Drilling 
Devido à utilização de SAC por dentro da coluna e LAM no anular, o desbalanceio provocado 
pode aumentar consideravelmente a pressão de bombeio, necessitando adequar as camisas 
das bombas utilizadas ou até mesmo inviabilizando a operação. Para esses casos, não é 
recomendada a utilização de turbina ou motor, por aumentarem a perda de carga no BHA. Faz-
se necessário simulação hidráulica para avaliar pressões envolvidas. 
As NRVs deverão ser testadas previamente considerando essa pressão de desbalanceio. 
O fluido a ser utilizado no anular será o Light Anular Mud (LAM), cujo peso é insuficiente para 
matar o poço. Dessa forma, é recomendado que esse fluido seja o mesmo anteriormente 
utilizado na perfuração SBP, para evitar a necessidade de substituição do fluido. 
Em PMCD, como o fluido no anular permanecerá parado enquanto o SAC é injetado na 
formação junto com os cascalhos, e considerando que a pressão no poço está em equilíbrio 
com a pressão da formação, poderá haver troca de fluido entre poço e formação, acumulando 
algum fluido da formação no anular do poço. Caso isso ocorra, o fluido da formação poderá 
migrar no anular do poço, aumentando a pressão de superfície. Com isso, no mínimo, deverão 
ser injetados 50 bbl de fluido LAM pelo anular a cada 6h, de forma a quebrar o efeito gel e 
permitir a leitura nos sensores de pressão de superfície, de eventual influxo no poço. A vazão 
a ser utilizada deverá seguir a recomendação de projeto. 
Obs.: Devido à limitação de injetividade no reservatório, pode ser necessário diminuir vazão 
pela coluna ou mesmo interromper bombeio pela coluna durante bullheading pelo anular. 
Deverá ser observada a vazão de bullheading necessária para evitar a migração de fluido da 
formação pelo anular, conforme padrão PE-2POC-01106 - [ MPD ] [ PMCD ] [ OPER ] 
TRANSIÇÃO PARA PMCD. 
A simulação deverá ser solicitada pelo projetista generalista ao SIP, conforme padrão PE-
1PBR-00733 - SIMULAÇÕES HIDRÁULICAS DE CONTROLE DE POÇO: CONCEITOS E 
ELABORAÇÃO e incorporado ao projeto do poço. 
Poços nos quais será necessário utilizar um fluido overbalance ao final da perfuração ainda 
assim poderão utilizar a técnica PMCD, pois apesar de grande extensão de poço aberto para 
combate a perda com cimento ao final, o histórico operacional mostra ser possível tal operação, 
apesar dos riscos e cuidados que deverão ser observados. Referenciar a Nota Técnica GAT-
CIM-001-23_Rev0 para mais informações. 
23.2. Floating MudCap Drilling 
Em FMCD, o nível de fluido irá baixar tanto dentro da coluna quanto no anular. Para evitar que 
a coluna fique vazia e impossibilite o envio dos dados de MWD/LWD, deve-se prever a utilização 
de restritores de vazão na coluna ou jatos de broca mais fechados. A queda no nível estático é 
calculada segundo a fórmula abaixo: 
𝑄𝑢𝑒𝑑𝑎=  𝐷
𝜌௠
∗ (𝜌௠ −𝜌௣) 

## Página 26

 
26 
 
D = Profundidade da zona de perda, m; 
𝜌௠  = Peso específico equivalente do fluido no poço, lb/gal; 
𝜌௣= Peso específico equivalente de poros na zona de perda, lb/gal; 
Quando a queda é muito acentuada, ao retornar com bombas após a conexão, pode levar algum 
tempo para o enchimento da coluna. Por isso, é necessária configurar a ferramenta para enviar 
os dados on demand. A perda de carga no interior da coluna deve evitar o efeito de free fall 
devido ao desbalanceio. 
A migração de fluido da formação é controlada pela velocidade descendente do fluxo de SAC 
pelo anular, uma vez que este não tem reologia para impedir a rápida migração pelo anular. 
Dessa forma, deve-se efetuar previamente simulação de controle conforme padrão PP-1PBR-
00614 para os poços candidatos a FMCD. 
Como em FMCD a vazão pelo anular é constante, deve-se garantir que haja pelo menos duas 
bombas alinhadas para o anular do poço e que as bombas estejam em barramentos diferentes 
para o caso de blackout parcial. 
24. CONSIDERAÇÕES FINAIS 
A elaboração do projeto MPD é atribuição da gerência POCOS/SPO/PEP/PROJ-PERF, 
podendo ser elaborado pela contratada de serviços de contrapressão. Nesse caso, deverá ser 
realizada revisão do projeto MPD por um especialista MPD da Petrobras. 
É necessário incluir na APRI do poço as questões específicas para todas as fases do poço que 
irão demandar o uso do MPD (SBP / MCD). A equipe deverá ser obrigatoriamente constituída 
pelo projetista do poço, projetista de fluidos, representante técnico da área de Segurança de 
Poço, representante da sonda e representante técnico para as técnicas MPD (chave estrutural 
MPDSPO). 
25. ANEXOS 
Anexo A - Checklist Insumos MPD 
Anexo B - Checklist de Projeto MPD 
Anexo C - Buffer Manifold e P&ID genéricos 
Anexo D - Árvore de Decisão de perda 
Anexo E – Modelo de Projeto MPD 
