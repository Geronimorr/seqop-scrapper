# Instalação / Descida do BOP

59 SEQOPs | 82 comentários MPD

## Análise IA dos Comentários

```json
{
  "sub_tipos": [
    "Descida do BOP com junta integrada",
    "Descida de BHA e testes do BOP",
    "Teste de pressão de linhas e válvulas",
    "Troca de fluido e equalização de pressão",
    "Teste funcional de sistemas MPD",
    "Montagem e descida de BHA liso",
    "Instalação de junta integrada e testes subsequentes"
  ],
  "pontos_verificacao": [
    {
      "item": "Manter PRVs ajustadas para proteger o sistema MPD ou ventilado para evitar sobrepressurização.",
      "frequencia": "alta",
      "exemplo_real": "Manter PRVs ajustadas para proteger o sistema MPD ou manter sistema MPD ventilado para evitar sobrepressurização acidental do sistema com classe de pressão menor (LA-11628)."
    },
    {
      "item": "Conferir alinhamento antes de pressurizações e testes de pressão.",
      "frequencia": "alta",
      "exemplo_real": "Atenção para sempre manter as PRVs do sistema MPD alinhadas e setadas, e claro confirmar alinhamento antes das pressurizações."
    },
    {
      "item": "Testar funcionalidade e estanqueidade de válvulas e sistemas antes da operação.",
      "frequencia": "alta",
      "exemplo_real": "Efetuar testes de pressão das linhas e válvulas de superfície do sistema MPD."
    },
    {
      "item": "Verificar checklist de instalação da junta integrada antes da descida.",
      "frequencia": "alta",
      "exemplo_real": "Conferir checklist para descida da junta integrada MPD preenchido previamente à descida, conforme Anexo B do padrão PE-2POC-01247."
    },
    {
      "item": "Registrar dados de testes funcionais, como galonagem e pressão.",
      "frequencia": "média",
      "exemplo_real": "Registrar galonagem e amperagem dos testes funcionais do travamento, destravamento e destravamento secundário do latch do RCD."
    },
    {
      "item": "Planejar tally de riser para evitar tooljoints em posições críticas.",
      "frequencia": "média",
      "exemplo_real": "Planejar tally de riser considerando space out do RCD da junta integrada de modo a garantir que durante às conexões da coluna de trabalho não haverá tooljoint em frente ao RCD."
    },
    {
      "item": "Monitorar e ajustar parâmetros de pressão durante testes.",
      "frequencia": "alta",
      "exemplo_real": "Confirmar alinhamento e configuração para pressão de teste das PRVs."
    }
  ],
  "erros_frequentes": [
    "Falta de alinhamento correto das PRVs antes de pressurizações.",
    "Omissão de testes funcionais ou de estanqueidade de válvulas.",
    "Planejamento inadequado do tally de riser, resultando em tooljoints em posições críticas.",
    "Falta de registro detalhado de parâmetros durante testes.",
    "Execução de testes desnecessários ou em sequência incorreta.",
    "Inversão na conexão de mangueiras do sistema MPD."
  ],
  "padroes_aprovacao": [
    "Manter PRVs ajustadas para evitar sobrepressurização.",
    "Realizar testes de pressão e funcionalidade com alinhamentos claros e previamente definidos.",
    "Registrar todos os dados relevantes de testes e operações.",
    "Planejar adequadamente o tally de riser para evitar problemas durante conexões.",
    "Utilizar checklists padronizados para garantir conformidade com procedimentos."
  ],
  "normas_aplicaveis": [
    "PE-2POC-01247",
    "ET-2000.00-1100-000-PPQ-001",
    "PE-2POC-01113"
  ]
}
```

## Comentários MPD Completos

### 1-RJS-763D — 30 - Substituição do fluido, retirada do BHA e teste do BOP
**Ramon Moreira Fernandes** | v3

Prezados

É boa prática manter circulação pelo circuito de superfície durante a troca de fluido do poço aberto até a interface passar do BOP para se precaver de uma eventual queda de bomba na coluna já que a booster estará desligada. Para isso no passo 6, após item c) (interromper a vazão ma booster), estabelece circulação via stp2->linha de PMCD->buffer->choke MPD com fluido 8,8 ppg.

Dessa forma fica livre para trocar o fluido das linhas submarinas de kill, choke e booster, sempre mantendo circulação e contrapressão no circuito de superfície.

Passo 6: especificar em quais tanques está o fluido pesado e em quais tanques o fluido leve (não ficou claro pra mim).

### 1-RJS-763D — 30 - Substituição do fluido, retirada do BHA e teste do BOP
**Leonardo Mesquita Caetano** | v1

Caros, 
De acordo com a SeqOp.

No item 8, pode-se fechar a MPDV06 (a crossover do buffer), para forçar fluxo pelas mangueiras, passando pelo riser.

### 1-RJS-763D — Descida de BHA 16 pol, testes de BOP e MPD
**Ivani Tavares de Oliveira** | v3

De acordo com a sequência. Se houver uma próxima versão:
    - Atualizar a figura do item 22 porque está desatualizada em relação a versão do P&ID (não aparece a válvula MPDV50). As demais figuras estão corretas.
    - item 24, o procedimento da sonda MPD-DAQ-RSP-OP-01-02 orienta usar a UC para equalização da pressão nas válvulas do buffer para fazer o alinhamento do próximo teste (item 27). Perguntar a sonda se seria mais fácil usar bomba da sonda ao invés da UC, pois esta estará pressurizando o riser.

### 1-RJS-763D — Descida de BHA 16 pol, testes de BOP e MPD
**Gustavo Costa Magalhaes Pena** | v2

Sugestões de alinhamentos para os testes de pressão do sistema MPD foram enviados para a fiscalização.

### 1-RJS-763D — Descida de BHA 16 pol, testes de BOP e MPD
**Gustavo Costa Magalhaes Pena** | v1

Prezados, seguem comentários:

Em operações em paralelo:
Planejar o teste de giro da unidade, com até 175º para cada lado, monitorando moonpool e subsuperfície, a fim de identificar se existe alguma interferência gerada pelas mangueiras do MPD (considerando também possíveis limitações das mangueiras do sistema riser). Para mais detalhes, consultar o CSD MPD.
Mencionar o teste das NRVs non-ported (já realizado).


Em montagem e descida do BHA 16":

Item 6: Mencionar que a sonda e a SLB devem se planejar para a realização do Fingerprint offline. Em caso de indisponibilidade de alguma das partes, a fiscalização deverá ser informada.


Em descida do BHA e teste do sistema MPD:

Item 19 em diante: Recomendo conferir os alinhamentos propostos na SeqOp do NS57, item 15 em diante (seqop revisada em 02/02/2025):

NS-57 - 8-ATP-8D-RJS
S08 - Descida do BHA, testes do BOP e sistema MPD contra gaveta de testes.

### 1-RJS-763D — Descida do BOP com junta integrada
**Gustavo Costa Magalhaes Pena** | v2

Somente um comentário:

Item 16: O teste de giro é comumente realizado em paralelo com as intervenções, após a conexão do BOP com o suporte do ROV. Da forma que está escrito, me parece que o teste vai entrar no caminho crítico.

> ↳ **Fernando Roberto Benitez Nobrega:** De acordo e vamos explicitar na V3

### 1-RJS-763D — Descida do BOP com junta integrada
**Fábio Koiti Dairiki** | v1

Boa noite,
Segue comentário

Inserir no item 4, letra b:
 v. Nos testes de alta pressão que envolvam Standpipe Manifold ou Choke Manifold, manter PRVs ajustadas para proteger o sistema MPD ou manter sistema MPD ventilado para evitar sobrepressurização acidental do sistema com classe de pressão menor (LA-11628 ocorrido em NS-33).

> ↳ **Fernando Roberto Benitez Nobrega:** De acordo

### 1-RJS-763D — Descida do BOP com junta integrada
**Leonardo Mesquita Caetano** | v1

Caros, 
segue comentários.

Item 11 - O teste funcional do DSIT pode ser feito junto com o teste do diverter.

Item 12 - O teste de estanqueidade das linhas de 6" podem ser feito juntos com os testes da linha de 2". 

Realizar teste de giro com 175 graus para os dois lados, caso a sonda ainda não tenha feito. Registrar posições das mangueiras nos dois extremos com ROV.

> ↳ **Fernando Roberto Benitez Nobrega:** Bom dia, como será a primeira instalação da sonda, proponho manter os testes segregados para melhor identificar algum possível problema, e a otimização seria obtida a partir da segunda instalação. Estamos inserindo uma linha para o teste de giro

> ↳ **Leonardo Mesquita Caetano:** De acordo. 
Em relação a primeira instalação, muitos comentários não foram feitos pois já estão no check list que a gente passa para sonda. Só reforçando que é importante que eles usem:

https://rjln202.petrobras.com.br/SINPEP/REST/DP&T/SINP_MODP_R_P_DPT.NSF/0/eead534c8194523b0325879e004065c7/$FILE/Anexo%20B%20-%20Check-list%20instala%C3%A7%C3%A3o%20da%20junta%20integrada.xlsx

### 1-RJS-763D — Reconexão do LMRP com junta integrada
**Ramon Moreira Fernandes** | v1

Passo 12: efetuar teste funcional do sistema de travamento do packer assy e do BA, registrando indicativos de galonagem e sensor de posição.

Passo 16: Atenção para não comunicar esta pressão com o buffer manifold (conferir isolamento do buffer).

Passo 46 / Nota: "Por solicitação da sonda [...] fazer os testes de 1 a 4 [...]"

> ↳ **Ramon Moreira Fernandes:** Correção passo 12: desconsiderar "packer assy"

> ↳ **João Paulo Luz Alves:** Ramon, bom dia.

Em relação ao comentário da nota do passo 45, nós queríamos fazer só o teste 2 e 3 (válvulas externas) para testar o riser com AGMAR contra DSIT. A sonda quis antecipar o teste das válvulas internas do flow spool. Então seria 1 e 4 mesmo, e não 1 a 4.

### 3-RJS-762 — 08 Descida e instalação do BOP com Junta Integrada
**Ramon Moreira Fernandes há um ano** | v1

Prezados boa noite

Em preparativos:
Entre passo 16 e 17: Preparar tally de riser considerando space out do RCD da junta integrada de modo a garantir que durante às conexões da coluna de trabalho não haverá tooljoint em frente ao RCD.
Entre passo 18 e 19: Verificar que todas as funções eletro hidráulicas da junta integrada e do umbilical de controle estão previamente conectadas a dispositivos do tipo placa de stabs (stabbing plate).

Em operações em paralelo (offline fora das mesas rotativas):
Passo 3 / item c: informar CSD MPD (ao invés de CSD FLUI).

Em operações em paralelo (offline na mesa auxiliar):
Passo 3: registrar N/S, tipo de borracha. Usar borrachas novas. Verificar nível de óleo do BA e horas de uso acumuladas do BA.

Em Descida do BOP:
Passo 5 / item c: não costuma-se fazer o teste de pressão antes da instalação da junta integrada. Somente após a junta integrada. Como trata-se de um recebimento cabe considerar uma exceção.

Em Junta integrada de MPD:
Passo 14: testar mangueiras e válvulas do flowspool com 300 / 3000 psi (apenas a título de recebimento). Em paralelo, verificar funcionalidade dos sistemas de travamento do Packer Assy e do RCD. Efetuar teste funcional das válvulas de equalização EQA e EQB. Verificar funcionamento dos sensores de pressão da junta integrada.
Sugestão: melhorar a qualidade do diagrama MPD (melhorar resolução e incluir válvulas EQA e EQB). Segue um print melhorado:

### 3-RJS-762 — 09 Descida de BHA 16”, teste do BOP e sistema MPD
**Leonardo Mesquita Caetano há um ano** | v1

Caros, boa tarde.
Segue.

Em "OPERAÇÕES EM PARALELO"

Item 2, "Buffer Manifold: 300 / 3.000 psi. Atenção aos equipamentos limitados a 2.000 psi" unico trecho para 2000 psi no das mangueiras até o choke MPD deve ser o coriolis, conferir se há outra restrição do lado da sonda. 
Item 5. Incluir PRV 3 e 4. Verificar na comunicação profbus da sonda para Halliburton se todos os dados estão disponíveis.

Em "MESA AUXILIA"

Montar 2 conjuntos com BA+BART e 1 Packer Assy


Em "MESA PRINCIPA"

item 26. Atentar na passagem pela slip joint, passar com compensador aberto, para evitar atuação do mecanismo J slot


Item 28. Revisar os teste com foco em:
- avaliar o posicionamento do ported sub 
- focar apenas nas válvulas que não são possíveis fazer em paralelo (retirar válvulas que podem ser testadas offline)
- incluir vávlulas EQ A e EQ B, do sistema de equalização da junta 
- Reduzir para 3 testes (conforme sugerido no Teams)

> ↳ **Andre Santos Doria há um ano:** Ótimo! Será discutido com a Seadrill e ajustado na v2.

### 3-RJS-762 — 25 - Retirada de coluna após combate a perda, montagem de BH
**Ivani Tavares de Oliveira** | v5

Estou de acordo com a sequencia.
Se sair uma nova versão, corrigir o item 11, pois o critério de aprovação é em teste dinâmico, com booster para riser e sistema MPD:
Pressão de teste: SBP = (Pressão unidade de cimentação + 300 psi) / 15 min.
Critério: Variação inferior a 1bph ou ganho máximo de 0,25 bbl/15 min
item 20. Fazer flowcheck antes de desassentar BA e PackerAssy

### 3-RJS-762 — 25 - Retirada de coluna após combate a perda, montagem de BH
**Geronimo de Freitas Rolandi** | v3

Prezado, corrigir o alinhamento do circuito de superfície enquanto broca acima do BOP (itens 2, 3, 5 , 7 e 8):
Manter AP 9 ppg em 3950 m com 450 gpm no circuito de superfície. Alinhamento Standpipe manifold => Linha de PMCD=> Buffer manifold => Choke MPD, com Buffer manifold => Choke manifold => linha de choke (ou linha de kill) // deixar uma válvula fechada isolando choke manifold e Buffer manifold.
Item 10. Testar packer assy com SBP de conexão (300 psi) por 5 min. HOLD POINT CSD MPD. 
a) Fechar Packer inferior e pressurizar o riser com unidade de cimentação, via linha de choke, com 300 psi
b) Critério para avaliação do teste: queda de pressão de até 10 psi / 5 min.
c) Fechar o packer assy superior e abrir o inferior, testanto do packer superior.
d) drenar o riser até 0 psi pela UC.

item 11: acredito que tem que ter um TIW fechada abaixo do ported sub, confirmar

### 3-RJS-762 — 25 - Retirada de coluna após combate a perda, montagem de BH
**Ivani Tavares de Oliveira** | v1

Os testes do packer Assy e BA são Hold Point.

### 3-RJS-762 — 25 - Retirada de coluna após combate a perda, montagem de BH
**Ivani Tavares de Oliveira** | v1

Adicionar bullet:
 item 2 e 4: manter parâmetros constantes e avaliar tendência do volume dos tanques e trip tank virtual.
 item 8: Enviar informação e registro fotográfico (se tiver) do BA e Packers Assy para a chave CSDMPD.

Como está em edição a versão 2, considerar o teste do packer assy antes do assentamento do BA, são 2 corridas certo?
item 12. Para o instalação e teste do BA, tomar cuidado com o posicionamento do ported sub.

### 3-SPS-111D — Descida BHA 16 pol, teste do BOP e riser + MPD
**Gustavo Costa Magalhaes Pena há um ano** | v2

De acordo, apesar de não ter sido incorporada a recomendação de redução de escopo para teste do sistema MPD.

Da forma que está, entendo que são Hold Point MPD (compõe CSB primário) os alinhamentos:

#4 - DSIT e mangueiras de 6".
#5 - ACD+SSA e Riser.

### 3-SPS-111D — Descida BHA 16 pol, teste do BOP e riser + MPD
**Gustavo Costa Magalhaes Pena há um ano** | v1

Em operações paralelas: Garantir pelo menos 02 NRVs testadas com 300/5000 psi (HP CSD MPD), conforme mencionado na sequencia de descida do BOP e instalação da junta integrada.

Sobre os alinhamentos de teste do sistema MPD.
A ACD tem funcionamento diferente da RCD, assim como a linha de 2" em cada sistema.

Na RCD quem promove a vedação do anular são as borrachas do BA e o acesso à linha de 2" fica localizado entre BA e DSIT, ou seja, válvulas e linha de 2" ficam submetidas à pressão do poço e compõe CSB.

Na ACD quem promove a vedação do anular é a câmara pressurizada entre os packers, e o acesso à linha de 2" fica no interior dessa câmara, portanto as válvulas e linha de 2" não têm exposição à pressão do poço, e não compõe CSB.

Partindo dessa premissa é possível eliminar alguns alinhamentos de teste, conforme sugestão abaixo:

Alinhamento #1: ACD+SSA e válvulas internas do FS (DBV1 e DBV3).
Alinhamento #2: ACD+SSA e válvulas externas do FS (DBV2 e DVB4). HP CSD MPD.
Alinhamento #3: DSIT e válvulas de entrada do BFM (BV1 e BV2). HP CSD MPD.


Os outros elementos podem ser testados via unidade do Lub skid offline, como por exemplo:

Upper ACD é testado com a pressão da câmara e monitorado no TT.
DBV5 e DBV6 permanecem abertas o tempo todo para permitir pressurização da câmara entre os packers. O teste no sentido superfície x poço pode ser feito com UC ou Lubskid, em paralelo.
Mesma coisa se aplica para a BV525, só que no sentido poço x superfície.
A BV5 pode ser testada no no sentido poço x superfície utilizando o Lub skid.
A BV6 somente é testada no sentido superfície x poço, mas trata-se de uma contingência da contingência, sem função CSB.

> ↳ **Ricardo Bruno Martins Teixeira há um ano:** Bom dia, Pena

Em relação aos testes de pressão, já discutido previamente junto a sonda e CSD MPD em troca de emails e não seria possível fazer o teste via Lub Skid (limite de 1500 psi).

Quanto às demais possíveis otimizações, também discutidas na mesma troca de emails e sugerido pelo CSD MPD anteriormente para manter o plano de testes como original da unidade.

> ↳ **Gustavo Costa Magalhaes Pena há um ano:** Se a máxima pressão do lub skid é 1500 psi, então essas válvulas serão submetidas, no máximo, a 1500 psi durante as operações.

### 3-SPS-111D — Descida do BOP e Junta Integrada de MPD
**Leonardo Mesquita Caetano há um ano** | v4

Caros, bom dia.
Segue comentários para verificação/confirmação.

PREPARATIVO
"16. [Sonda / AFG] Conferir checklist para descida da junta integrada MPD preenchido previamente à descida", *conforme Anexo B do padrão PE-2POC-01247.

OPERAÇÕES EM PARALELO (OFFLINE NA MESA AUXILIAR)

b) "SSAs para perfuração com DP 6 5/8”" - Caros, apenas para confirmar se será usado DP de 6 5/8 na fase 3; confere?

JUNTA INTEGRADA DE MPD (MESA PRINCIPAL)

Antes do item "12. Conectar slip joint"; verificar Tally de Riser para evitar tool joint na frente dos selos durante conexões; caso necessários, realizar ajuste no tally para inserir sub de Riser gabaritado. 

EFETUAR TESTE DE GIRO (RECEBIMENTO) (MESA PRINCIPAL)

Avaliar interferências e registrar fotos com ROV das mangueiras na posição neutra e nos dois sentidos de giro e enviar para Chave MPDSPO e CSD MPD como evidência de atendidomento do critério contratual para fins de recebimento.

> ↳ **Leonardo Mesquita Caetano há um ano:** No item 17, ao conectar as mangueiras, analisar disposição da mangueiras no moonpool e transição da posição de espera até a conexão na coluna de riser . Mangueiras com diferentes comprimentos associado a condições ambientais podem estar sujeitas a entrelaçamento. [evento da 3-RJS-706 na NS-57]

> ↳ **Ramon Sena Barretto há um ano:** Boa noite! 

Confirmando, será usado DP 6 5/8" na fase 3. 

Colocamos a recomendação de planejar o tally para que não haja tooljoints em frente aos selos nas conexões, pois essa condição tem que ser buscada com o comprimento da coluna de riser abaixo da Junta Integrada. Toda alteração acima dela será absorvida pela slip joint. não sendo efetiva.

Não necessariamente o ROV conseguirá efetuar os registros, pois sua profundidade mínima de atuação é 50 m de profundidade. Mas colocamos a possibilidade para que seja avaliada no momento da operação.

### 3-SPS-111D — Descida do BOP e Junta Integrada de MPD
**Ramon Moreira Fernandes há um ano** | v2

Prezados

Não há necessidade de testar as linhas submarinas e conduites antes e depois da conexão da junta integrada (passo 9.d e passo 11). Costumamos testar apenas após a conexão da junta integrada.

Passo 18: o teste das linhas submarinas e conduites é através das mangueiras conectadas à slip joint (não através de capa de teste).

Passo 14 pode ser feito em paralelo ao passo 15.

> ↳ **Ramon Sena Barretto há um ano:** Boa tarde Ramon! Nós planejamos apenas um teste depois da junta integrada (passo 11) e um teste depois da junta telescópica (passo 18). Não previmos teste antes da conexão da junta integrada. O item 9.d é uma verificação apenas.

Passo 18: Será revisado na próxima versão!

Nós planejamos inicialmente fazer os passos 14 e 15 em paralelo, entretanto não está no procedimento da sonda. Avaliamos fazer mesmo assim, porém, como é a primeira vez que essas tarefas serão executadas por esta equipe, a sonda preferiu manter o foco separadamente nas duas operações.

### 3-SPS-113 — 08 Descida do BOP com Junta Integrada
**Fábio Koiti Dairiki** | v3

Caros, boa tarde
Observações para itens 17, 28, 30 e 31 (testes do BOP e linhas submarinas com UC): Manter PRVs ajustadas para proteger o sistema MPD ou manter sistema MPD ventilado para evitar sobrepressurização acidental do sistema com classe de pressão menor (LA-11628).

> ↳ **Victor Cardoso Thiers Vieira:** Bom dia, Dairik.
Observação adicionada na V4.

### 3-SPS-113 — 08 Descida do BOP com Junta Integrada
**Gustavo Costa Magalhaes Pena** | v2

De acordo com a SeqOp, no entanto seguem comentários para o caso de uma nova revisão.

Tivemos diversas anomalias do sistema MPD da Valaris durante a execução do Tortuga Leste, conforme e-mail enviado para a sonda em  26/05 às 09:48. Recomendo reforçar com a Valaris esses problemas para evitar recorrência, e se necessário incluir em SeqOp.

Em operações offline: 
Apesar da fase MPD estar mais para frente, se possível efetuar um teste de estanqueidade do BFM com a finalidade de identificar se o sistema está estanque antes da realização dos testes previstos no item 14.
Recomenda-se que a sonda confira o check-list de instalação de junta integrada do anexo B do padrão PE-2POC-01247 - PERFURAÇÃO COM CONTRAPRESSÃO NA SUPERFÍCIE (MPD/SBP).

### 3-SPS-113 — 08 Descida do BOP com Junta Integrada
**Ramon Moreira Fernandes** | v1

Passo 6: testar função de travamento, destravamento e destravamento secundário do RCD, verificando galonagem e leitura do sensor de posição.

> ↳ **Andre Luiz Tomelin:** Boa noite. Comentário será incorporado na V2.

### 3-SPS-114 — 8 - Descida do BOP com Junta Integrada
**Leonardo Mesquita Caetano** | v2

Caros, bom dia. 
Segue comentários.

Item 14 - confirmar PRVs alinhadas e ajustadas, compatíveis com a pressão do teste e necessários a proteção do sistema.

Item 15 - teste funcional do DSIT pode ser dispensado (conexão com stabbing plate com baixo histórico de falhas) ou feito junto com teste do diverter (item 34).

### 4-RJS-764 — 08 - Descida do BOP com JI de MPD
**Gustavo Costa Magalhaes Pena** | v1

Seguem comentários:

Em preparativos, item P18: As mangueiras do sistema MPD e suas respectivas polias devem estar instaladas no moonpool. 

Item de atenção:
Durante a descida do BOP, instalação da junta integrada e testes das linhas de superfície são realizados diversos testes de pressão de intensidades distintas, e um erro pode levar à uma sobrepressurização dos equipamentos MPD. Atenção para sempre manter as PRVs do sistema MPD alinhadas e setadas, e claro confirmar alinhamento antes das pressurizações.

Em operações em paralelo:
Item 2: A pressão de teste do BFM é de 3000 psi.
Item 3: Para evitar submeter as NRVs à altas pressões, é possível planejar o alinhamento de pressurização pelo anular e pelo interior da coluna, simultaneamente.

Em junta integrada, item 11: Este teste de pressão não está previsto no item 5.

### 4-RJS-764 — 09 Descida BHA 16 pol, teste do BOP e riser + MPD
**Leonardo Mesquita Caetano** | v3

No item 75) d) Confirmar alinhamento e configuração para pressão de teste das PRVs.

> ↳ **Andre Santos Doria:** Ajustado na v4

### 4-RJS-764 — 09 Descida BHA 16 pol, teste do BOP e riser + MPD
**Ramon Moreira Fernandes** | v1

Operações em paralelo na mesa auxiliar / passo 1: confirmar se realmente será usada borrachas naturais nos BAs. Geralmente a preferência é por borrachas de polyuretano.

### 4-SPS-112 — 08 Descida e instalação do BOP com Junta Integrada
**Geronimo de Freitas Rolandi há um ano** | v1

Bom dia,
Pequeno detalhe apenas..
Item 8 Teste#1 e Teste #2 acho que ficou invertido o texto:
Teste #1 – Teste de estanqueidade das válvulas internas da RCD e flowspool (BLD1, R1 e R3)
Teste #2 – Teste de estanqueidade das válvulas externas da RCD e flowspool (BLD2, R2 e R4)

### 4-SPS-112 — Instalação do CVU e Teste do BOP com SART
**Geronimo de Freitas Rolandi há um ano** | v1

Efetuar testes de pressão as linhas e válvulas de superfície do sistema MPD.
a) Conferir se as PRVs do sistema MPD estão alinhadas e ajustadas para proteção do equipamento de superfície. 
b) Em paralelo aos testes, conferir calibração dos manômetros. 
c) Pressões de testes: 
(1) Buffer Manifold: 300 / 3.000 psi. Atenção aos equipamentos limitados a 2.000 psi. 
(2) Sistema de contrapressão (manifold do choke e coriolis): 300 / 2.000 psi. Chamar MPD HALL

### 7-BR-86DB-RJS — DESCIDA DO BHA 12 1/4", TESTE DO BOP E MPD, CORTE DO CIMENTO
**Gustavo Costa Magalhaes Pena** | v2

De acordo.

Comentários:

Item 17.q: Não vejo necessidade de testar com fluxo, pois logo em seguida o sistema será testado com pressão.

Itens 26 a 32: Costumamos fazer de dentro para fora ou de fora para dentro... Na SeqOp, o primeiro alinhamento é o do queixo duro, o próximo deveria ser as válvulas externas da junta integrada, mas está com as válvulas internas. É um detalhe. Nos prints dos alinhamentos, sugiro ocultar a parte com numeração de alinhamentos para não confundir.

Item 39: Não entendi a figura com alinhamento de flow check estático.

> ↳ **Cesar Ferreira dos Reis:** itens 26 a 32: Mantive a sequência de testes do procedimento TOI. Mas ajustei a sequência pra fazer de fora pra dentro. Apaguei o numero dos alinhamentos nos diagramas.

Item 39- coloquei o diagrama do flowcheck por causa da contingência h.a

### 7-BR-86DB-RJS — DESCIDA DO BHA 12 1/4", TESTE DO BOP E MPD, CORTE DO CIMENTO
**Ramon Moreira Fernandes** | v1

Pode antecipar o bypass do sistema MPD a partir do passo 37 (ao invés do passo 38).

### 7-BR-86DB-RJS — DESCIDA DO BHA 12 1/4", TESTE DO BOP E MPD, CORTE DO CIMENTO
**Ramon Moreira Fernandes** | v1

Passo 18:
Alinhamento para pressurização: IC-> Choke Manifold -> Linha de kill
Alinhamento para equalização das válvulas do buffer: Bomba da sonda -> STP-> Linha de PMCD->Buffer
Alinhamento para drenagem a jusante das válvulas após alterações de alinhamento: Buffer->Choke->Choke hidráulico (lado choke)->Stripping Tank.
Obs: Trip tank monitora integridade do BA e Stripping Tank monitora integridade das válvulas sendo testadas.

Passos 20 e 21: Considerar flush tanto para trip tank quanto para stripping tank separadamente.

> ↳ **Cesar Ferreira dos Reis:** De acordo com o P&D, a linha de teste da UC chega em um junta de expansão do choke manifold e não seria possível fazer o alinhamento dessa forma, para usar a bomba da sonda para equalizar o buffer manifold. Mas já alinhado com o supervisor aqui, vamos isolar a linha de kill no choke manifold, fazer as drenagens pela UC e usar a UC para equalizar a pressão do buffer manifold para refazer os alinhamentos (daí monitora a pressão do riser pelo manômetro da RCD). Após os alinhamentos do buffer manifold para o teste seguinte, volta com o alinhameto da UC para a linha de kill , para monitorar a pressão do riser. Foi assim que foi feito no ultimo teste (apesar de na seqop aprovada estar para fazer da forma como você falou).

> ↳ **Cesar Ferreira dos Reis:** Linha de PMCD/ drenagem - Vermelha.
UC> linha de kill - Azul

### 7-BR-86DB-RJS — DESCIDA DO BHA 12 1/4", TESTE DO BOP E MPD, CORTE DO CIMENTO
**Daniel Bastos Chalita** | v1

Teste do riser + junta integrada + buffer manifold

Excluir item 17r
Treinamento prático das turmas A e E concluído em 11/08, turmas C e D em 23/09.

Item 38:
Incluir: "Confirmar válvulas da junta integrada de riser e buffer manifold alinhadas para modo corte de cimento, com by-pass do junk catcher, coriolis e choke MPD"
Incluir P&ID com alinhamentos, referenciar fechamento e abertura de respectivas válvulas para by-pass.

### 7-BR-86DB-RJS — Instalação do BOP com junta integrada MPD
**Ramon Moreira Fernandes** | v1

Item 13 / c: Registrar galonagem e amperagem dos testes funcionais do travamento, destravamento e destravamento secundário do latch do RCD.

### 7-BUZ-100DA-RJS — Descida do BHA 8,5 pol e testes do BOP e MPD simplificado
**Fábio Koiti Dairiki** | v1

Caros, boa tarde
Sugestão: Adicionar a seção INFORMAÇÕES GERAIS E PREPARATIVOS: Durante teste do BOP e linhas auxiliares com alta pressão, manter PRVs ajustadas para proteger o sistema MPD ou manter sistema MPD ventilado para evitar sobrepressurização acidental do sistema com classe de pressão menor (LA-11628).

### 7-BUZ-100DA-RJS — Teste de influxo (método 5), desconexão operacional do BOP e
**Fábio Koiti Dairiki** | v2

Caros, boa tarde
De acordo.
Se houver outra revisão, adicionar aos testes de  alta pressão das linhas e revestimento recomendação de manter PRVs ajustadas para proteger o sistema MPD ou manter sistema MPD ventilado para evitar sobrepressurização acidental do sistema com classe de pressão menor (LA-11628).

### 7-BUZ-90D-RJS — Descida do BHA 12,25 x 13,5 pol e Teste BOP e MPD
**Geronimo de Freitas Rolandi há um ano** | v2

Nos passos 18 e 19, para evitar o máximo de contaminação por fluido sintético, recomendo efetuar a troca  (passo18) quando o BA estiver próximo de ser assentado, no passo 19.., Exemplo:
19) Instalar bearing assembly na RCD de acordo com orientações do supervisor MPD. 
• Conectar e descer seção com BART+BA. 
• Confirmar linha de 2” ventilada. 
• Substituir fluido acima da RCD por FPBA 11,5 ppg com retorno para flowline
• Assentar BA na RCD e descarregar peso, conforme procedimento. 
• Travar BA na RCD e testar travamento com overpull. 
• Alinhar trip tank para monitoramento acima do BA. 
• Desassentar BART e manter 5 m acima da RCD. 
Em paralelo: 
• Calibrar e testar PRVs utilizando unidade de cimentação via linha de bleed e de PMCD, caso ainda não tenha sido feito

### 7-BUZ-90D-RJS — Descida do BHA 12,25 x 13,5 pol e Teste BOP e MPD
**Ivani Tavares de Oliveira há um ano** | v1

item 23. Teste #4, verificar o fechamento da BFM-V3.

### 7-BUZ-90D-RJS — Descida do BHA 8,5, troca de fluido, teste do BOP e teste de
**Leonardo Mesquita Caetano há um ano** | v4

- Item 17. Lembrando que teremos que conviver com fluido pesado acima do BA após a troca.

- Item 27. 
  -- Em paralelo, confirmar se os 2 filtros do junk catcher estão limpos.
  -- Manter a máxima vazão possível na booster a fim de garantir a limpeza do cimento grosseiro proveniente do anel de cimento.
  -- Avaliar a utilização de um tampão viscoso para uma limpeza criteriosa no final.

- Item 28. 
  -- Ao alinhar para o MPD, avaliar o comportamento do choke: (i) alinhar inicialmente com a gut line aberta, (ii) alinhar o choke totalmente aberto, (iii) fechar lentamente a gut line, (iv) aplicar contrapressão lentamente. Caso ocorra um comportamento inadequado da pressão durante o processo, abortar e reavaliar a limpeza.
  -- Realizar a calibração dos parâmetros do PID ates do início da troca.
  -- Realizar uma calibração do modelo em paralelo à troca, buscando ajustar o sistema para os valores de leitura do PWD de 9,2 ppg.

- Item 29. Retirar o trecho "Manter alinhamento para by-pass do sistema MPD no buffer manifold."

- Item 31. 
  -- Avaliar a retirada da broca acima do topo do cimento para evitar a queda de novas lascas do anel. (Antecipar o início do passo 32).
 -- Realizar em paralelo as etapas do fingerprint do MPD: ajuste do modelo variando a vazão na coluna em steps de 100 gpm, tanto para mais quanto para menos; eficiência da bomba (quando o coriolis estiver alinhado); etc.
  -- Monitorar o retorno e alinhar o coriolis assim que possível. 
  -- Trocar para outra perna do junk catcher com filtro limpo.

- Item 32. Sugestão de realizar o MPD drill antes do simulado de hang off. Em seguida, anexar à SeqOp (pode ser na SeqOp do fingerprint) o formulário disponível em https://petrobrasbr.sharepoint.com/:w:/r/teams/bdoc_POCOS-SPO-SP-FLUI/Documentos%20Compartilhados/MPD/11.%20CSD/12.%20Check%20Point/MODELO_NS48_7BUZ93D_Check%20List%20MPD%20Drill_25-12-2024.docx?d=we7b93fa8ffb74da485c657dae2b53711&csf=1&web=1&e=RC5EH8

> ↳ **Leonardo Mesquita Caetano há um ano:** No item 33, lembrar que o sistema MPD está no circuito e portanto- deve-se manter vazão na booster

No item 34, ao fechar o LA, a pressão no BOP deve ser registrada e não deve ser drenada abaixo desse valor

### 7-BUZ-90D-RJS — Descida do BHA 8,5, troca de fluido, teste do BOP e teste de
**Leonardo Mesquita Caetano há um ano** | v1

Caros, 
de acordo com a sequência como um todo.

Salvo o comentário já feito pelo Bruno, CSD FLUI. 
Atentar também que  no teste 4 do MPD deve-se ajustar a cor da bvm v4 no ANEXO (está aberta no desenho)

> ↳ **Walleska Monyele Lopes de Almeida há um ano:** Leonardo, seria a válvula BFM V10 que deve estar fechada, ao invés de aberta no teste 4. Correto?

> ↳ **Walleska Monyele Lopes de Almeida há um ano:** Leonardo, seria a válvula BFM V10 que deve estar fechada, ao invés de aberta no teste 4. Correto?

> ↳ **Walleska Monyele Lopes de Almeida há um ano:** Leonardo, seria a válvula BFM V10 que deve estar fechada, ao invés de aberta no teste 4. Correto?

### 7-BUZ-90D-RJS — Descida e instalação do BOP
**Ivani Tavares de Oliveira há um ano** | v1

Item 4:
Bullet t#1: Prever abertura de PT com antecedência.

Novo bullet: Durante manobras verificar inclinação da slip joint e trim da embarcação buscando o zero (para evitar contato do DP com RCD). Sempre que possível, durante as manobras, promover o giro da embarcação.

Novo bullet: Prever no tally de riser a instalação da BAP, de forma que não seja necessário quebrar a junta integrada para instalar a BAP. A altura da BAP deve ser absorvida pela junta telescópica.

Novo bullet: Ao longo das manobras e passagens das ferramentas e BHAs, se a Protective Sleeve não estiver instalada, não girar a coluna, de forma a evitar dano na RCD! 

Novo Bullet: Atenção: As fases de MPD têm previsão de utilização de fluido base água. Verificar adequação das borrachas do RCD e BA ao mesmo.

> ↳ **Enio Lustosa de Resende há um ano:** Ivani, os comentários referente a manobra de coluna vou incluir na próxima sequência (montagem e descida do BHA). Os demais comentários vou incluir na V2. Obrigado.

### 7-BUZ-94D-RJS — Descida do BHA 8 1/2" e teste do BOP
**Fábio Koiti Dairiki** | v1

Adicionar à seção Preparativos ou a todos os testes de alta pressão que envolvam Standpipe Manifold ou Choke Manifold a seguinte nota:
Manter PRVs ajustadas para proteger o sistema MPD ou manter sistema MPD ventilado para evitar sobrepressurização acidental do sistema com classe de pressão menor (LA-11628).

### 7-BUZ-95-RJS — Descida de LMRP e reconexão com junta integrada de MPD
**Fábio Koiti Dairiki** | v1

Bom dia,
Sugestão:
Adicionar aos preparativos ou a todos os testes de alta pressão que envolvam Standpipe Manifold ou Choke Manifold a seguinte nota:
Manter PRVs ajustadas para proteger o sistema MPD ou manter sistema MPD ventilado para evitar sobrepressurização acidental do sistema com classe de pressão menor (LA-11628).

### 7-ITP-7-RJS — Montagem e descida de BHA 8 ½”, Teste de BOP com coluna flut
**Gustavo Costa Magalhaes Pena** | v2

Em atividades offline, incluir teste do BFM com 300 psi por 5 min, e setagem das PRVs para abertura com 200 psi.

### 7-ITP-7-RJS — Navegação, teste de DP e descida do BOP
**Geronimo de Freitas Rolandi há um ano** | v1

PREPARATIVOS:
Planejar tally de descida do riser com antecedência de modo que não fiquem tooljoints na frente dos selos do SSA (seal sleeve assembly) e ACDs da junta integrada durante as conexões (coluna acunhada na mesa rotativa).

Atualizar esquemático da junta integrada de MPD com distâncias / profundidades, sensores de pressão e pressão de acionamento e stripping do DSIT, manter informações com fácil acesso pelo sondador.

Pintar tubo inferior de uma seção de DP 5 7/8” para teste funcional do DSIT.

Conferir checklist para descida da junta integrada MPD preenchido previamente à descida, conforme Anexo B do padrão PE-2POC-01247

A última junta de riser abaixo da junta integrada deve possuir flutuadores para evitar danos nas mangueiras de MPD.

Efetuar testes de pressão das linhas e válvulas de superfície do sistema MPD.
a) Conferir se as PRVs do sistema MPD estão alinhadas e ajustadas para proteção do equipamento de superfície.
b) Em paralelo aos testes, conferir calibração dos manômetros.
c) Pressões de testes:
(1) Buffer Manifold: 300 / 3.000 psi. Atenção aos equipamentos limitados a 2.000 psi.
(2) Sistema de contrapressão (manifold do choke e coriolis): 300 / 2.000 psi. Chamar MPD HALL.
3. [Sonda / DD] [Caso ainda não tenha sido concluído] [HP CSD MPD] Testar 4x NRVs 9 ½” SLB com 300 psi / 5 min e 
5.000 psi / 5 min.
a) Registrar o N/S das NRVs testadas e não as desmontar dos seus respectivos subs.
b) Teste a ser realizado com 5.000 psi para o teste de pressão do BOP com coluna flutuada com até 4300 psi.
Caso teste venha a ser feito com bomba do subsea, gerar carta para envio ao CSD. Caso seja pela UC, informar 
CSD MPD previamente (30 min) para acompanhamento pelo RTO

Montar conjuntos com SSA + SSART + SSRT:
a) Mover 2x SSA, 2x SSART e 2x SSRT para o drill floor. Mover eventuais PJs necessários.
b) Montar 2 (dois) conjuntos de instalação (baixo para cima) com PJ + SSART + SSRT + DPs.
c) Realizar o stab do conjunto no SSA, instalar colar se segurança abaixo do SSA e estaleirar o conjunto.
a) Montar e estaleirar dois conjuntos com SSAs.
b) SSAs para perfuração com DP 6 5/8”.


JUNTA INTEGRADA:

Garantir pré-carga dos acumuladores do DSIT e ACD

### 7-ITP-7-RJS — Teste de influxo método 5, desconexão operacional do BOP, in
**Leonardo Mesquita Caetano** | v3

Caros, de acordo.

Segue sugestão de ganho de tempo:

O teste 19 (teste funcional do DSIT) é dispensável, principalmente se houver necessidade de troca dos elevadores (Também pode ser feito junto com o teste do diverter)

### 7-ITP-7-RJS — Teste de influxo método 5, desconexão operacional do BOP, in
**Fábio Koiti Dairiki** | v1

Caros, bom dia
Sugestão:
Adicionar às operações paralelas ou a todos os testes de alta pressão que envolvam Standpipe Manifold ou Choke Manifold a seguinte nota:
Manter PRVs ajustadas para proteger o sistema MPD ou manter sistema MPD ventilado para evitar sobrepressurização acidental do sistema com classe de pressão menor (LA-11628).

Item 13: não se aplica. Desconexão operacional para instalação de junta integrada.

### 7-JUB-78D-ESS — Descida do BHA 9,5 pol, teste de BOP, troca de fluido e test
**Gustavo Costa Magalhaes Pena** | v2

Prezados, seguem comentários e sugestões.

Em segurança operacional, MPD: 
Testar BFM com 300/3000 psi. Atentar para verificar manômetros e sensores de pressão das PRVs. 
Teste funcional das PRVs (principalmente #3 e #4). Em seguida , ajustar para proteção dos equipamentos.
Testar sistema de contrapressão (Hall), com atenção ao limite do coriolis (2000 psi).
Montar e estaleirar as 02 seções de BART+BA.

Em sequencia operacional, item 3: Conferir nesta etapa se as pressões de anular lidas pelo CoPilot e Ontrak estão condizentes.

Em teste do riser e sistema MPD:
Item 22: Notificar CSD MPD sobre a proximidade da etapa de testes. Inserir que os testes são Hold Point e que serão acompanhados pelo CSD MPD.
Item 28: Faltou fechar as RCDs V1 e V2.
Item 32: Abrir RCD V1.
Item 37: Abrir DSIT.
Item 41: Vazão máxima 2 bpm, reduzindo a partir de 1500 psi para diminuir perda de carga.
Item 43: Cuidado para evitar despressurização do riser por erro de alinhamento.

### 7-JUB-78DA-ESS — DMM, descida do BOP e assentamento no AAP
**Gustavo Costa Magalhaes Pena** | v1

Seguem comentários:

Em preparativos e premissas operacionais: 

a) Durante a descida do BOP e instalação da junta integrada são realizados testes de pressão do sistema BOP (5000-5800 psi) e do sistema MPD (2000 psi). Conferir atentamente o alinhamento antes dos testes, e sempre manter as PRVs do sistema MPD alinhadas e configuradas para proteção das linhas e equipamentos de superfície.

b) Sonda deverá preencher e entregar para a fiscalização o checklist de instalação da junta integrada do padrão PE-2POC-01247, anexo B:

https://sinpep.petrobras.com.br/SINPEP_Padrao_Web/PadraoEditar?PadraoId=4103#


Em instalação da junta integrada:

Item 12: Atenção na identificação das mangueiras para evitar inversão na conexão dos FS. Além de cuidados para não entrelaçar mangueiras MPD e do BOP.

Item 14: Teste com 300/2000 psi.

### 7-MRO-37-RJS — Desconexão do BOP e Reinstalação do BOP
**Gustavo Costa Magalhaes Pena há um ano** | v2

De acordo. 

Somente uma recomendação em providencias preliminares: Conferir checklist para descida da junta integrada MPD preenchido previamente à descida", *conforme Anexo B do padrão PE-2POC-01247.

### 7-STUP-10DA-RJS — Descida BHA 8,5 pol, teste do BOP, corte de cimento e troca 
**Gustavo Costa Magalhaes Pena há um ano** | v1

Seguem comentários:

Em preparativos MPD, 4º bullet: Retirar SPLs.

Item 1: Confirmar hidráulica e se TFA da broca é adequado para a perfuração FMCD. Perda de carga no inferior da coluna na vazão de perfuração deve ser suficiente para manter a coluna cheia para não prejudicar a transmissão de dados L/MWD.

Item 6: Sugestão. Durante os testes do BOP, se for possível obter a atenção de sondador, toolpusher e assistentes sondadores, realizar o treinamento "prático" adaptado para FMCD em paralelo.

Item 9b: Na intervenção FMCD considera-se que o topo do reservatório poderá estar em condição underbalance. A barreira para evitar a migração do HC até a superfície é a manutenção da vazão de SAC (vazão de controle da simulação SIP) no anular o tempo todo.

Item 9d: 
Esse teste é Hold Point CSD-MPD.
Antes de iniciar o teste entendo que seria melhor abrir o DSIT. 
Monitorar trip tank.
Existe uma contingência para sistema ACD/SSA. Em caso de falha do teste de pressão estático com a UC, partir para o teste dinâmico utilizando o lub skid (mais detalhes ver S02A - Montagem e descida da cauda PACI (em FMCD) do TUP132DA).

Item 9e: Antes de retomar a perfuração efetuar o top-down do anular com SAC e manter vazão de controle. Em seguida, efetuar a substituição do volume de coluna por SAC na vazão de perfuração. Registrar pressões de referência e então seguir com perfuração.

Item 10, 6º bullet: O alinhamento de by-pass MPD da contratada é utilizado para manter o anular ventilado para o MGS ou perfurar com retorno (embuchamento) após instalação do SSA. 

Item 11, 2º bullet: Monitorar sensor do BOP, caso seja observado um aumento da pressão no BOP isoladamente (sem aumentar SPP ou PWD), indicando que pode haver HC migrando no anular. Proceder com vazão e volume de bulheading no anular.

### 7-STUP-10DA-RJS — Descida do BOP com junta MPD
**Leonardo Mesquita Caetano há um ano** | v2

Caros, bom dia.

Recomendo em "PREPARATIVOS"
"Sonda: Conferir checklist para descida da junta integrada MPD preenchido previamente à descida." (checklist diponível no Anexo B do padrão PE-2POC-01247")

> ↳ **Denes Marcel Chaves Lopes há um ano:** Será comunicado à sonda o checklist.

### 7-STUP-10DA-RJS — Descida do BOP com junta MPD
**Geronimo de Freitas Rolandi há um ano** | v1

Prezados, boa noite,
Não ficou claro pra mim em quais os momentos serão feitos os testes das linhas de KCB durante a descida do BOP, mas normalmente a sonda faz um teste imediatamente antes da instalação da JI e outro teste depois. Se for esse o caso por favos solicitar que façam somente o ultimo teste após a instalação da JI, antes da conexão de qualquer mangueira, pois a mobilização da JI geralmente não leva tanto tempo assim.
Passo 14. Esses testes não são hold point mpd, será hold point o teste caso seja instalado o BA.

> ↳ **Denes Marcel Chaves Lopes há um ano:** Estão programados 3 testes das linhas durante descida do BOP
1° teste - BOP na água (inicio descida)
2° teste - Após conectar junta MPD (fim descida)
3° teste - Após montar goose necks da slip joint

Retirado HP do passo 14 na revisão 2

### 7-TUP-129D-RJS — Descida BHA 8,5 pol e teste do BOP com coluna flutuada
**Fábio Koiti Dairiki** | v1

Caros, segue comentário:
Adicionar aos preparativos ou a todos os testes de alta pressão que envolvam Standpipe Manifold ou Choke Manifold a seguinte nota:
Manter PRVs ajustadas para proteger o sistema MPD ou manter sistema MPD ventilado para evitar sobrepressurização acidental do sistema com classe de pressão menor (LA-11628).

### 7-TUP-133-RJS — Descida BHA 8,5, teste BOP, fingerprint MPD, MPD drill, chok
**Ramon Moreira Fernandes** | v3

Passo 28 / bullet 2: para evitar erro de interpretação sobre o modo de controle MPD (modo SBP, modo AP ou modo manual), sugiro eliminar esse item. Mas já estou aprovando a sequência desta forma e avisando a equipe MPD a bordo sobre o modo de operação desejado (modo AP).

### 7-TUP-133-RJS — Descida BHA 8,5, teste BOP, fingerprint MPD, MPD drill, chok
**Ramon Moreira Fernandes** | v2

Passo 28 do fingerprint:

usar menor vazão de coluna possível desde que haja leitura de PWD.
iniciar com target 9,2 ppg na sapata e despressurizar progressivamente em steps de 25 psi até abrir totalmente o choke.

### 7-TUP-133-RJS — Descida BHA 8,5, teste BOP, fingerprint MPD, MPD drill, chok
**Ramon Moreira Fernandes** | v2

Prezados

Conversei com CSD AGUP e achamos mais robusto fazer as etapas de troca de fluido e fingerprint da seguinte forma:

Passo 28:
manter modo AP 9,2 ppg na sapata durante a troca. Em caso de interrupção de bombeio pela coluna o sistema MPD vai reagir automaticamente para manter 9,2 ppg na sapata. Em caso de queda de todas as bombas (shut-in) o sistema MPD vai tentar manter o AP 9,2 ppg mas é comum despressurizar um pouco.
O sistema MPD ainda não estará calibrado nesse momento pois o fingerprint online só será feito após a troca de fluido.

Passos 29, 30 e 31: manter AP 9,2 ppg na sapata. Somente no final do fingerprint, durante o simulado de DPPT que será feita a despressurização controlada do poço. Ao final do simulado de DPPT será adotado AP 9,1 ppg na sapata.

### 7-TUP-133-RJS — Navegação, descida e instalação do BOP com junta MPD e teste
**Geronimo de Freitas Rolandi** | v2

item 21 não é Hold Point MPD, normalmente esse teste é somente das mangueiras contra as válvulas internas da JI, de resto, de acordo.

### 7-TUP-133-RJS — Navegação, descida e instalação do BOP com junta MPD e teste
**Ivani Tavares de Oliveira** | v1

Em OPERAÇÕES EM PARALELO À NAVEGAÇÃO, DESCIDA E INSTALAÇÃO DO BOP:
item f) conforme padrão PE-2POC-01247, Teste funcional e de pressão antes do início da perfuração da fase MPD (8 1/2"). A próxima fase não será com MPD. Pode ser feito neste momento, mas deverá refeito na fase reservatório. Além disso os testes de alta do buffer manifold são 3000 psi/5min.

Itens 11, 13 e 14. em relação ao planejamento do tally/stack up da junta integrada, considerar que os elementos de vedação do ACD/SSA, DSIT e BOP respeitem o range de DP utilizado na sonda, ou seja, em conexão todos os elementos da junta de Riser MPD e BOP devem estar em posição livre de tooljoint.

> ↳ **Tiago Britto Liberato:** Boa tarde,

Para o ACD/SSA eu concordo. Para o DSIT e BOP, que estarão abertos durante operação normal, entendo que é desejável porém não obrigatório, pois pode acabar limitando o tally de risers.

Vamos tentar atender.

Obrigado!

### 8-ATP-8D-RJS — S07 - DMM e descida do BOP
**Leonardo Mesquita Caetano há um ano** | v2

Caros, bom dia
Alguns comentários apenas por redundância. 

- Em "PREPARATIVOS E PREMISSAS OPERACIONAI"
"Sonda: Conferir checklist para descida da junta integrada MPD preenchido previamente à descida." (checklist diponível no Anexo B do padrão PE-2POC-01247"

Segue link do documento:

https://rjln202.petrobras.com.br/SINPEP/REST/DP&T/SINP_MODP_R_P_DPT.NSF/0/eead534c8194523b0325879e004065c7/$FILE/Anexo%20B%20-%20Check-list%20instala%C3%A7%C3%A3o%20da%20junta%20integrada.xlsx

- Em "OPERAÇÕES PARALELA", ajustar teste do buffer em alta para 3000 psi

- Item 38. Se for possível com apenas uma seção, realizar teste funcional do DSIT junto com do Diverter

> ↳ **Diogo Jose Rossetto há um ano:** Não é possível efetuar o teste funcional do DSIT com apenas 1 seção de DP.

### 8-ATP-8D-RJS — S08 - Descida do BHA, testes do BOP e sistema MPD contra gav
**Gustavo Costa Magalhaes Pena há um ano** | v2

De acordo.

Formalidade: São Hold Point MPD (registro no SIP) somente os alinhamentos #3 e #4, mas acompanhamos todos os alinhamentos.

Esclarecimento: A sugestão do Léo quanto ao item 15 é de instalar o BA e retirar a BART 5 m acima do BA. realizar os testes nesta posição (verificar posição dos tool joints em relação a BA, DSIT e BOP).
Num cenário de vazamento do BA, a BART já está pronta para recuperar.

### 8-ATP-8D-RJS — S08 - Descida do BHA, testes do BOP e sistema MPD contra gav
**Leonardo Mesquita Caetano há um ano** | v1

Caros, bom dia.
Segue comentários.

Item 15) 
- sugestão de aguardar primeiro o teste de pressão com a BART 5 metros acima da RCD para confirmar vedação. 
- Usar BA com elementos de vedação novos; 
- Registrar no boletim do sondador horas de uso e nível de óleo do BA.

Item 17) Confirmar ajuste da popoff da bomba do teste para 2100 psi. 

Itens 23)...35)

- Ajustar Holdpoints: teste 3 e teste 4 (alta e baixa)
- Recomenda-se utilizar pressões de teste de alta em 1900 psi 

Item 36) Retirar BART

> ↳ **Diogo Jose Rossetto há um ano:** Como o teste será efetuado contra a gaveta de testes, se formos retirar a BART após executar o teste, precisaremos despressurizar o riser para abrir o BOP e retirar a BART.

> ↳ **Diogo Jose Rossetto há um ano:** Com relação ao teste de pressão, como tivemos vazamento no riser na primeira instalação da junta de MPD, o teste de recebimento ainda está pendente. Naquela época solicitaram que o teste fosse executado com 2000 psi mesmo. Favor, confirmar a possibilidade de reduzir a pressão do teste para 1900 psi.

> ↳ **Leonardo Mesquita Caetano há um ano:** Obrigado pelo histórico. Mantém os 2000 psi.

### 8-BUZ-89D-RJS — Descida do BHA 8,5 pol e testes do BOP e MPD
**Ivani Tavares de Oliveira** | v2

De acordo com a sequência, se sair uma nova versão, favor corrigir:
item 30. Testes de Alta pressão #1 e #2 são Hold Point.

### 8-BUZ-89D-RJS — Descida do BHA 8,5 pol e testes do BOP e MPD
**Geronimo de Freitas Rolandi** | v1

Garantir NRV's testadas com 2000 psi aprovadas Hold Ppoint CSD MPD. De resto, sequencia aprovada.

### 8-BUZ-89D-RJS — Descida, montagem de junta integrada de MPD e instalação do 
**Geronimo de Freitas Rolandi** | v1

De acordo.

### 8-BUZ-96D-RJS — Descida BHA 8 1/2" e testes do BOP e MPD
**Gustavo Costa Magalhaes Pena** | v1

De acordo.

Em caso de nova revisão:

Item 11: Entendo que o TOC já foi confirmado com a SS70, mas atentar que para descer a BART e instalar o BA é necessário descer 2 seções de DP (1,5 na verdade). Por precaução, deixaria umas 3 seções (ou até mais) acima do TOC.

Itens 28 e 29: Considerar todos os 4 alinhamentos como HP CSD MPD.

### 8-BUZ-96D-RJS — Instalação da cauda PACI 2z em FMCD e teste do BOP
**Gustavo Costa Magalhaes Pena** | v3

De acordo com a seqOp.

Somente alguns pontos de atenção.

Em considerações para operação FMCD:
Preferencialmente utilizar uma linha submarina (lower) para abastecimento do poço. A ideia é o abastecimento do poço será continuo mesmo em caso de necessidade do fechamento do BOP.
Para avaliar a vazão total no anular (limite dos equipamentos), considerar a vazão utilizada no fill-up diverter.

### 8-ITP-9D-RJS — S01 - Navegação, teste do DP e descida do BOP
**Leonardo Mesquita Caetano há um ano** | v3

Caros, boa noite.
Segue comentários.

Item 8. Avaliar compatibilidade da running tool de Riser com a junta.
Item 12. Todos os cabos dos atuadores e sensores até a stabbing plate deverão ser previamente conectados no deck.
Item 14, ajustar PRV para pressão de teste; concluído o teste, configura-las para 1700 psi de abertura.
Item 16. Tempo de fechamento do DSIT deverá ser inferior a 1 min. Ajustar para pressão de stripping e testar ajuste fino da pressão com step de 50 psi através do painel remoto.

Caso ainda não se tenha sido feito, prever teste de giro da unidade 175 graus para os dois lados.

> ↳ **Allan Frederico Castilho Esteves Godinho há um ano:** Leonardo, o teste de giro está previsto na sequencia seguinte.

### 8-ITP-9D-RJS — S01 - Navegação, teste do DP e descida do BOP
**Geronimo de Freitas Rolandi há um ano** | v1

De acordo com comentário do Leandro, pois se trata da primeira descida de JI dessa sonda.

### 8-ITP-9D-RJS — S03 - Montagem e descida do BHA liso e teste do bop com colu
**Leonardo Mesquita Caetano há um ano** | v4

Caros,
No item 20:
Certificar-se que o buffer manifold esteja ventilado durante a realização dos testes MPD 
Ajustar pop-off da unidade de cimentação antes da realização dos testes para proteger o riser. (ciclos de pressurização serão feitos sem PRV alinhada).

### 8-ITP-9D-RJS — S03 - Montagem e descida do BHA liso e teste do bop com colu
**Ramon Moreira Fernandes há um ano** | v3

De fato, como não será possível pressurizar o buffer manifold, não será possível fazer uma única pressurização do riser visto para mudar de um alinhamento para outro é necessário pressurizar o buffer para equalização dos elementos que foram testados. Nesse caso os 4 testes previstos no passo 19 serão feitos através de 4 pressurizações, teste de baixa seguido de teste de alta em cada pressurização. De acordo com o ajuste proposto para a próxima sequência.

### 8-ITP-9D-RJS — S03 - Montagem e descida do BHA liso e teste do bop com colu
**Ramon Moreira Fernandes há um ano** | v2

Boa noite

Passo 19: Não havendo prontidão do buffer manifold, os testes MPD sentido poço->superfície deverão ser modificados eliminando as pressurizações contra as válvulas do buffer manifold. Na prática isso implica em eliminar o teste #21 e efetuar os testes #22 (LACD) e #23 (DSIT) contra as válvulas do FlowSpool. Se precisar pode enviar o arquivo editável do diagrama MPD para que a gente atualize os testes #22 e #23. Posteriormente, quando o buffer estiver pronto, os testes #21, #22 e #23 deverão ser refeitos com os alinhamentos originais.

### 8-ITP-9D-RJS — S03 - Montagem e descida do BHA liso e teste do bop com colu
**Gustavo Costa Magalhaes Pena há um ano** | v1

Seguem comentários:

Em operações paralelas, é mencionado que o BFM foi testado, porém o mesmo ainda está em etapa de recebimento.

Itens 15 e 17: Aproveitar as operações com BA e treinar equipes para a estratégia de FMCD simplificado (escopo da intervenção).

Item 16: Possui um escopo maior de teste por se tratar de um teste de recebimento do sistema MPD. Quando em operação, é possível reduzir o escopo para 3 ou 4 alinhamentos.

### 8-ITP-9D-RJS — S03 - Montagem e descida do BHA liso e teste do bop com colu
**Ramon Moreira Fernandes há um ano** | v1

Item 16: Atentar para o fato de não estarmos com NRVs non ported nessa coluna (fase sem MPD). Portanto durante o teste haverá comunicação de pressão para o interior da coluna. Se necessário fechar IBOP para evitar interferência no momento em que for pressurizar o BM nas etapas de equalização e mudanças de alinhamentos.

### 8-ITP-9D-RJS — S03 - Montagem e descida do BHA liso e teste do bop com colu
**Ramon Moreira Fernandes há um ano** | v1

Item 16: mesmo não sendo HoldPoint nessa intervenção, por se tratar de um teste de recebimento, envolver CSD MPD para acompanhamento dos teste via RTO-Live.

### 8-ITP-9D-RJS — S03 - Montagem e descida do BHA liso e teste do bop com colu
**Ramon Moreira Fernandes há um ano** | v1

Passo 16 / bullet 1: Verificar perda de carga nas linhas de superfície entre flowspool e manifold MPD circulando AGMAR com 1500 gpm vias 2 mangueiras do FS e passando pelo junk catcher. A perda de carga deve ser no máximo de 150 psi, descontada a perda de carga no Coriolis e a diferença de hidrostática entre flowspool e choke MPD (cf item 6.1.6 da ET-2000.00-1100-000-PPQ-001).

### 8-MRO-36-RJS — Descida BHA 8,5, Teste BOP, troca de fluido e corte do cimen
**Gustavo Costa Magalhaes Pena** | v2

De acordo.

A principio será necessário treinar somente uma turma (Turma B). Sendo assim, existe a possibilidade da operação cair bem no horário da outra turma.
Caso isso ocorra, precisaremos avaliar se iremos aguardar, ou se iremos deixar o TP para ser realizado com o FP. Neste cenário, seria necessário incluir a execução de um teste de influxo pelo método 4 antes do passo 30.

### 8-MRO-36-RJS — Descida BHA 8,5, Teste BOP, troca de fluido e corte do cimen
**Gustavo Costa Magalhaes Pena** | v1

Seguem comentários:

Em gestões de mudança, temos a MOC da sonda devido indisponibilidade dos sensores de pressão do flowspool.

Em operações paralelas, o teste do sistema de superfície é 300/3000 psi. Manter coriolis by-passado e ventilado quando testando com 3000 psi.

Em descida do BHA, item 2: Em paralelo à montagem e descida do BHA efetuar etapas do Fingerprint offline.

Em teste do sistema MPD:

Item 10, 6º bullet: Será necessário retirar 2 seções para cumprir esse item.

Item 16: Bombear FPBA 11,5 ppg para evitar tubo U.

Item 18, 4º bullet: #1 a #4.
Item 18, 7º bullet: A vazão pode ser maior até no máximo 2 bpm.
Item 18, 8º bullet: Precisamos confirmar como iremos monitorar a estanqueidade do SSA se TT ou Riser Fluid.

Após o item 24: Inserir etapa de testes do sistema de desvio de fluxo operando em circuito fechado no lub skid.

Em troca de fluido, item 28: A parte que menciona que a troca deve ser realizada com MPD acho que precisa de mais destaque. Primeiro alinhar JC e choke MPD. Atentar que o sistema MPD precisará ser calibrado antes de iniciar a troca. Durante a homogeneização do fluido, já será possível iniciar etapas do FP que não precisam do coriolis. O coriolis será alinhado após confirmar peneiras sem excesso de cimento (geralmente após 1,5 BU).

Todos os itens 29 até 38 deverão ser realizados com a premissa de sempre manter a pressão no fundo superior a 9,4 ppg.

Item 33: SIDPP deverá levar em consideração o comentário anterior.

> ↳ **Gustavo Costa Magalhaes Pena:** Item 28 retirar o trecho que trata sobre retomar corte de cimento.

### 8-MRO-36-RJS — S01 – Navegação com BOP no fundo Descida do BOP com junta MP
**Ivani Tavares de Oliveira** | v1

item 10. Os testes hold point são no sentido poço x superfície, após instalção do BA. Durante a instalação da junta no moonpool os testes são feitos no sentido superfície x poço conforme critério de aceitação descrito, mas não são hold point. 
PRVs com 2100 psi para o teste.
Sistema MPD (coriolis) by pass para não correr risco de pressão superior a 2000 psi.

### 9-BUZ-103D-RJS — Descida e instalação do BOP e junta integrada de MPD
**Gustavo Costa Magalhaes Pena** | v1

Seguem comentários:

Itens de atenção: 

1) Durante a descida do BOP e instalação da junta integrada são realizados testes de pressão com níveis bem distintos, e um erro pode levar à uma sobrepressurização das linhas de superfície do MPD. Atenção para sempre manter as PRVs do sistema MPD alinhadas e setadas, e claro confirmar alinhamento antes da pressurização.

2) Atenção na identificação das mangueiras para evitar inversão na conexão dos FS. Além de cuidados para não entrelaçar mangueiras MPD e do BOP.

3) Sonda deverá preencher e entregar para a fiscalização o checklist  de instalação da junta integrada do padrão PE-2POC-01247, anexo B:

https://rjln202.petrobras.com.br/SINPEP/REST/DP&T/SINP_MODP_R_P_DPT.NSF/0/eead534c8194523b0325879e004065c7/$FILE/Anexo%20B%20-%20Check-list%20instala%C3%A7%C3%A3o%20da%20junta%20integrada.xlsx

### 9-MLL-95A-RJS — Montagem, descida de BHA 8 ½” e teste do BOP
**Gustavo Costa Magalhaes Pena** | v2

Prezados, 

Recentemente tivemos um evento no qual uma das NRVs pulou para fora do sub após a retirada do lift sub (Float sub era o elemento no topo da seção).
Quando o pino do lift sub parou de escorar a NRV a mesma pulou e caiu no piso da plataforma.
Sendo assim, temos recomendado que não sejam colocadas float sub no topo das seções, assim sempre haverá um pino travando ela na posição independente da pressão atuando abaixo dela.

Favor verificar se a posição dos float subs atendem essa nova recomendação.

> ↳ **Fernando Fonseca Kogik:** Bom dia!

confirmado a bordo que não teremos este risco

### 9-MLL-95A-RJS — Montagem, descida de BHA 8 ½” e teste do BOP
**Fábio Koiti Dairiki** | v2

Caros, bom dia
Sugestão: Adicionar ao item INFORMAÇÕES PRELIMINARES: Durante os testes do BOP e linhas submarinas, manter PRVs ajustadas para proteger o sistema MPD ou manter sistema MPD ventilado para evitar sobrepressurização acidental do sistema com classe de pressão menor (LA-11628).

### 9-MLL-95A-RJS — Montagem, descida de BHA 8 ½” e teste do BOP
**Gustavo Costa Magalhaes Pena** | v1

Segue comentário:

Em paralelo, P4: O teste do BFM para intervenção na estratégia FMCD simplificado não precisa de teste de alta. E é importante efetuar os testes de estanqueidade (300 psi) e funcional (200 psi) das PRVs.
