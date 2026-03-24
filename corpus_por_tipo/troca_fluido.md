# Troca de Fluido / Condicionamento

29 SEQOPs | 44 comentários MPD

## Análise IA dos Comentários

```json
{
  "sub_tipos": [
    "Troca de fluido em modo MPD",
    "Condicionamento após perfilagem",
    "Retirada de coluna com troca de fluido",
    "Amortecimento e troca de fluido",
    "Condicionamento para descida de calha",
    "Teste de sistemas MPD durante troca de fluido"
  ],
  "pontos_verificacao": [
    {
      "item": "Equalizar pressão na linha antes de abrir válvulas submarinas",
      "frequencia": "alta",
      "exemplo_real": "No ponto de atenção da UC como contingência de cavitação, atentar para equalizar pressão na linha antes de abrir a válvula submarina (LIK)."
    },
    {
      "item": "Alinhar retorno para o MGS durante circulação de gás residual",
      "frequencia": "alta",
      "exemplo_real": "Alinhar retorno para o MGS e circular o volume de riser entre DSIT e mesa rotativa (~50 bbl) com diverter fechado."
    },
    {
      "item": "Realizar testes de pressão (DSIT, BOP, etc.) antes de operações críticas",
      "frequencia": "alta",
      "exemplo_real": "Sugiro acrescentar um teste de pressão do DSIT antes do condicionamento para garantir estanqueidade durante a circulação."
    },
    {
      "item": "Manter controle da profundidade da interface durante troca de fluido",
      "frequencia": "alta",
      "exemplo_real": "Equipe SLB MPD deve manter controle da profundidade da interface durante a retirada considerando volume de 9,2 bbl bombeado, volume de aço retirado e perdas para a formação."
    },
    {
      "item": "Compensar swab com contrapressão durante manobras",
      "frequencia": "média",
      "exemplo_real": "Sugiro usar contrapressão para compensar efeito swab e maximizar velocidade de manobra."
    },
    {
      "item": "Ventilar linhas antes de iniciar circulação",
      "frequencia": "média",
      "exemplo_real": "Ventilar linha do flowspool para flowline. Avaliar se é melhor ventilar a linha 2\" para o choke manifold da sonda."
    },
    {
      "item": "Simular operações críticas antes de execução",
      "frequencia": "média",
      "exemplo_real": "Solicitado à Halliburton que seja feita a simulação de manobra com fluido visco."
    },
    {
      "item": "Acompanhar e corrigir posição da interface do fluido pesado durante troca de fluido",
      "frequencia": "alta",
      "exemplo_real": "MPD deve preparar uma tabela com a SBP de perfuração e de conexão previstas durante a troca de fluido considerando os cenários de perda."
    }
  ],
  "erros_frequentes": [
    "Falta de alinhamento correto de tanques e bombas",
    "Omissão de testes de pressão antes de operações críticas",
    "Desconsiderar cenários de perda durante troca de fluido",
    "Não detalhar critérios de aceitação para testes",
    "Falta de comunicação prévia ao CSD MPD antes de operações críticas",
    "Troca de fluido sem considerar impacto na profundidade da interface"
  ],
  "padroes_aprovacao": [
    "Realizar testes de pressão antes de operações críticas",
    "Manter comunicação prévia com o CSD MPD antes de operações importantes",
    "Simular operações críticas para prever cenários e ajustar parâmetros",
    "Garantir alinhamento correto de tanques, bombas e linhas",
    "Compensar swab com contrapressão para evitar problemas durante manobras",
    "Ventilar linhas antes de iniciar circulação para evitar contaminação"
  ],
  "normas_aplicaveis": [
    "PE-2POC-01113",
    "Especificação técnica 6.4.2.11",
    "Padrão de perfuração SBP"
  ]
}
```

## Comentários MPD Completos

### 1-RJS-763D — 25 - Substituição por fluido OB e retirada de coluna
**Gustavo Costa Magalhaes Pena** | v1

De acordo. 

Uma recomendação em caso de nova revisão:

Em alertas para operação com MPD, item 15: No ponto de atenção da UC como contingência de cavitação, atentar para equalizar pressão na linha antes de abrir a válvula submarina (LIK).

### 1-RJS-763D — 32 - Condicionamento após perfilagem
**Ramon Moreira Fernandes** | v1

Ao final da circulação, abrir o DSIT e circular pela eventual gás residual pela linha de 2" antes de desmobilizar o BA.

### 1-RJS-763D — 32 - Condicionamento após perfilagem
**Ramon Moreira Fernandes** | v1

Prezados

Desconsiderar o terceiro ponto do comentário anterior. Para a circulação de HC com sistema MPD é necessário instalar o BA, fechar o DSIT e alinhar o retorno para o MGS. Prever Holdpoint MPD para teste do BA contra o DSIT após a instalação do BA.

### 1-RJS-763D — 32 - Condicionamento após perfilagem
**Ramon Moreira Fernandes** | v1

Passo 17:
Confirmar que há equipe MPD de contrapressão (SLB) embarcada para  possibilitar alinhamento de retorno pelo choke MPD.
Alinhar retorno para o MGS
Como não teremos BA instalado, para drenar eventual gás trapeado abaixo do DSIT, antes de abrí-lo é necessário fechar o diverter com retorno alinhado para o MGS e circular o volume de riser entre DSIT e mesa rotativa (~50 bbl) com diverter fechado.

### 3-RJS-762 — 21 - Troca de fluido e perfuração 12 1/4" x 13 1/2"
**Gustavo Costa Magalhaes Pena** | v2

De acordo. Peço somente para ajustar uma coisa.

Os itens 31 e 32 estão invertidos. O tampão de manobra deve ser bombeado somente após a retirada do BA.
Lembrar do evento que tivemos quando descemos o ported sub dentro do riser com a coluna vazia.

### 3-RJS-762 — 21 - Troca de fluido e perfuração 12 1/4" x 13 1/2"
**Gustavo Costa Magalhaes Pena** | v1

Seguem comentários:

Item 5: A partir do item e, liberar Halliburton para iniciar etapas do fingerprint com FPBNA 8,2 ppg, iniciando pela verificação do PID.

Item 6: Necessário concluir a verificação do FP para o FPBNA 8,2 ppg nesta etapa, antes de seguir para o item 8.
Serão verificados: PID, eficiência, perda de carga e MH. Todas etapas serão realizadas com a premissa de manter a pressão no fundo igual a 9,2 ppg.

Item 19: Importante assim que possível (a partir de 60 m dentro do reservatório) a geologia indicar um ponto de tomada de pré-teste para determinarmos o limite inferior da janela operacional. Assim em caso de perdas, saberemos se podemos reduzir o AP.

Item 25: Em caso de perdas durante a fase, avaliar troca do fluido em 02 etapas (poço aberto/revestido e riser).

Item 28: Sistema MPD pode auxiliar a compensar o SWAB.

Item 29: Não bombear tampão de manobra enquanto o BA não for retirado da RCD (planejado para item 32).

### 3-SPS-111D — 29 BHA 8,5 x 9,5 pol, teste do MPD e troca de fluido
**Gustavo Costa Magalhaes Pena há um ano** | v2

De acordo. 

No aguardo do anexo contendo as etapas do Fingerprint e treinamento prático.

### 3-SPS-111D — 29 BHA 8,5 x 9,5 pol, teste do MPD e troca de fluido
**Gustavo Costa Magalhaes Pena há um ano** | v1

Prezados, seguem comentários.

Em operações paralelas fora das MRs:
Item 4:
a) Para a 1ª corrida da fase são necessárias somente 02 NRVs. As outras 02 podem ser testadas em momento oportuno.
b) Registrar SN das NRVs e Float Sub.
c) Priorizar o teste pela UC e RTOlive (teste rápido e offline).
Item 5: Ajustar numeração.

Em operações paralelas na MR auxiliar:
a) Confirmar pelo menos 02 seções estaleiradas com SSART+ SSA (elementos novos).

Em instalação SSA e teste MPD:
Item 14cii: Desconheço restrição de velocidade de manobra a depender da SBP. Favor pedir a sonda que nos encaminhe a justificativa e orientação do fabricante.
Item 14e: Avaliar instalar SSA em momento oportuno (mais raso) para treinar equipe pendente de treinamento.
Itens 17 e 18: Sugiro trocar os 10 bbl, por até confirmar correto alinhamento (retira a necessidade de bombear 20 bbl com vazão baixa = mais tempo).
Item 22: Comunicar CSD MPD cerca de 30 min antes de iniciar os testes.
Item 22bi: A equalização nas linhas de superfície é realizada com a bomba da sonda, já que a UC estará monitorando a pressão do riser. Garantir que sempre o trecho a jusante das válvulas sendo testadas estarão sempre ventilados (abrir choke hidráulico do CM).

Em troca de fluido:
Item 31: Avaliar despressurizar packers da ACD e trocar fluido acima do SSA até o diverter a baixa vazão.

> ↳ **Ramon Sena Barretto há um ano:** Pena, segue recomendação sobre restrição de velocidade:
Conforme conversamos, sobre os conjuntos estaleirados, vamos manter um conjunto de instalação (SSART + SSRT) + SSA (elementos novos) e um conjunto de recuperação (SSART).

Demais comentários alterados.

### 3-SPS-111D — 36 Condicionamento do poço aberto para perfilagem
**Gustavo Costa Magalhaes Pena** | v3

Faltou mencionar momento de fechar o DSIT no item 21.
Também faltou a circulação para remover possível gás abaixo do DSIT (e abrir o mesmo). Para depois seguir com item 23.

### 3-SPS-111D — 36 Condicionamento do poço aberto para perfilagem
**Gustavo Costa Magalhaes Pena** | v2

Seguem comentários:

Item 4: Durante montagem do BHA, evitar deixar o float sub com NRV non ported no topo da seção, recentemente tivemos um evento no qual após retirar o lift sub a NRV pulou para fora do sub inadvertidamente. Alerta técnico em elaboração.

Item 16: Não faz sentido fechar o DSIT nesta etapa pois vamos descer repassando no item seguinte. E não se rotaciona coluna com o DSIT fechado. É mais simples fechar o DSIT no item 21.

### 3-SPS-111D — 38 Condicionamento do poço aberto e tampão de cimento #1
**Ramon Moreira Fernandes** | v3

Conforme discutido no grupo do teams, sugiro acrescentar um teste de pressão do DSIT antes do condicionamento para garantir estanqueidade durante a circulação. Para isso teríamos que fechar o BOP mantendo monitoramento do poço com unidade de cimentação por uma linha submarina, estabelecer vazão no riser pela booster e colocar uma contrapressão via choke MPD para monitorar estanqueidade do DSIT via trip tank. Caso a sugestão seja aprovada esse teste poderá ser considerado como Holdpoint MPD, com critério de ganho máximo de 0,1 bbl/5min no trip tank.

### 3-SPS-111D — 38 Condicionamento do poço aberto e tampão de cimento #1
**Ramon Moreira Fernandes** | v1

Passo 17 / item c e l: retirar menção ao PWD uma vez que não será usado PWD nessa manobra.

### 3-SPS-113 — 33 - Troca de fluido 11,3 x 12,3 ppg em modo MPD e retirada 
**Leonardo Mesquita Caetano** | v2

Sugestão do peso de fluido ser 12,4 ppg para refletir a condição final da fase, que estabilizou o poço.

### 3-SPS-113 — 33 - Troca de fluido 11,3 x 12,3 ppg em modo MPD e retirada 
**Ramon Moreira Fernandes** | v1

Passo 5, item e: Retirar circulação na coluna mantendo circulação no circuito de superfície (linha de PMCD).

Passo 6: MPD deve preparar um tabela com a SBP de perfuração e de conexão previstas durante a troca de fluido (mud rollover) considerando os cenários:
1 - sem perda
2 - com perda de 30 bbl/h
3 - com perda de 50 bbl/h
O objetivo é acompanhar e corrigir a posição da interface do fluido pesado e corrigir o setpoint SBP em função do cenário de perda.

Passo 7: fechar BOP anular, despressurizar o riser lentamente monitorando o sensor do BOP stack e interromper a circulação no circuito de superfície.

> ↳ **Denes Marcel Chaves Lopes:** Passo 5, item e: Retirar circulação na coluna mantendo circulação no circuito de superfície (linha de PMCD).
Será corrigido na V2

Passo 6: MPD deve preparar um tabela com a SBP de perfuração e de conexão previstas durante a troca de fluido (mud rollover) considerando os cenários:
1 - sem perda
2 - com perda de 30 bbl/h
3 - com perda de 50 bbl/h
Será inserido no passo 1 também com o valor medido de perda de fluido.
O objetivo é acompanhar e corrigir a posição da interface do fluido pesado e corrigir o setpoint SBP em função do cenário de perda.
Podemos colocar na tabela mas não está previsto realização de conexão durante troca de fluido.

Passo 7: fechar BOP anular, despressurizar o riser lentamente monitorando o sensor do BOP stack e interromper a circulação no circuito de superfície.
Passo será alterado na V2.

### 3-SPS-114 — 28 - Condicionamento do poço aberto após perfilagem
**Ivani Tavares de Oliveira** | v2

Item 13. Ventilar linha do flowspool para flowline.
Avaliar se é melhor ventilar a linha 2" para o choke manifold da sonda deixando o CH aberto.

item 14. Avisar ao CSD MPD 30 min de antecedência.
Critério de aceitação é queda de 10 psi por 5 min de observação.
O monitoramento do TT é durante todo o teste.

### 7-BUZ-100D-RJS — Condicionamento do poço, troca de fluido e retirada do BHA 8
**Ramon Moreira Fernandes** | v1

Passo 4: sugiro fazer uma despressurização progressiva do poço mantendo circulação apenas pela booster, reduzindo AP de 9,1 ppg até abrir totalmente o choke, fazer um flowcheck dinâmico com choke todo aberto e só então fazer um flowcheck estático.

> ↳ **Thiago Rodrigo de Souza:** Olá, Ramon. Obrigado pela sugestão. Estou de acordo. Será contemplado na V2. Abraço!

### 7-BUZ-90D-RJS — Condicionamento com broca tricônica
**Ramon Moreira Fernandes há um ano** | v1

Prezados

Considerar setting da PRV 5 em 1700 psi quando estiver mantendo poço pressurizado via circuito de superfície de modo a proteger os equipamentos de contrapressão que são limitados a 2000 psi.

Passos 14 a 18: Como estaremos sem PWD nesse BHA, sugiro usar o modo AP com equivalente a 9,5 ppg na sapata enquanto estiver circulando pela coluna, de forma a compensar eventual erro no modelo hidráulico.

### 7-BUZ-90D-RJS — Retirada BHA 8 1/2", condicionamento e troca de fluido
**Geronimo de Freitas Rolandi há um ano** | v7

Sequencia aprovada, flowcheck estático do passo 23 deverá ser feito com slug e bombas da sonda a 3 gpm, conforme FAM.

### 7-BUZ-90D-RJS — Retirada BHA 8 1/2", condicionamento e troca de fluido
**Gustavo Costa Magalhaes Pena há um ano** | v6

Prezados, seguem comentários.

No item 3 faltou mencionar a vazão da booster.

Sugiro inverter os itens 8 e 9. Primeiro flow check e depois circulação BU para limpeza. Desta forma teremos como confirmar o diagnóstico do flow check.

Os itens condicionais para perda estão como 8, mas são 11.

No item 13 considerar avaliar a velocidade de manobra e a SBP necessária a depender se foi utilizado o glicerinado viscosificado.

No item 23 não vejo necessidade de flow check dinâmico, somente estático com BA instalado (de olho no sensor do BOP para confirmar que o alinhamento está adequado).

### 7-BUZ-90D-RJS — Retirada BHA 8 1/2", condicionamento e troca de fluido
**Ramon Moreira Fernandes há um ano** | v1

Prezados

Passo 7: sugiro detalhar o alinhamento de tanques, bombas standpipe/booster para bombear simultaneamente Camai de sacrifício pela coluna e FPBA 8,7 ppg na booster.

Passo 7: Usar modo AP nessa etapa.

Passo 8 / 1º bullet: sugiro reformular a frase para: "ajustar AP para promover overbalance de 150 psi simulando condição do poço após a troca de fluido".

Passo 11: Usar modo AP nessa etapa.
Passo 11: Para evitar contaminação do CAMAI com FPBA ao final do bombeio é melhor não bombear pela booster e passar a bombear o FPBA 8,7 ppg pela linha de PMCD. Para isso faz-se a transição de bombeio da booster para linha de PMCD utilizando outro standpipe (isolado do standpipe que está com CAMAI). Detalhar o alinhamento de tanques, bombas e standpipe para o Camai e para o FPBA.

Passo 12 / bullet 2: [...] mantendo circulação via linha de PMCD com 400-600 gpm.

Passo 13: antes de ciclar as gavetas abrir as FSVs abaixo e acima para manter comunicação da pressão do riser com o poço (mesmo já tendo alinhado a UC).

Passo 15: Nessa etapa não precisará mais de contrapressão. Portanto o flowcheck dinâmico será com choke todo aberto. Em seguida flowcheck estático com o devido alinhamento.

### 7-BUZ-95-RJS — Condicionamento do poço, troca de fluido e retirada do BHA 8
**Gustavo Costa Magalhaes Pena** | v2

De acordo.

Itens 5, 8, 10 e 12: Atentar que as manobras de coluna (sem circulação) são realizadas em modo SBP com EMW 9,2 ppg no topo do reservatório, e não AP 9,2 ppg. Mas é um detalhe da equipe MPD, acredito que sem necessidade de nova revisão.

### 7-BUZ-95-RJS — Condicionamento do poço, troca de fluido e retirada do BHA 8
**Gustavo Costa Magalhaes Pena** | v1

Em dados básicos: Esquema mecânico do poço atualizado.

Em considerações operações MPD: Retirar informações sobre operações em MCD e retornar com contingência de circulação e controle de poço com MPD (fluxograma).

Em condicionamento, item 4: Efetuar flow check dinâmico (após remoção do reboco) e decidir por necessidade de combate a perda.

Em substituição do fluido:
Itens 6 e 7: Ao decidir por uma vazão baixa, estamos abrindo mão do PWD. A SBP será determinada pelo cálculo do MH de perda de carga (vazão intermediária não verificada em FP) e estimativa de altura da interface de fluido novo (função do calibre do poço, volume bombeado para o anular, perdas e volume de aço retirado).
Itens 8 e 10: 
A retirada costumamos fazer em modo SBP, com EMW de 9,2 ppg a 5471 m. Pode ser necessário aplicar um EMW maior para compensar pistoneio. 
Para a manobra alinhar 02 bombas de lama, de barramentos distintos, para a booster.
Equipe SLB MPD deve manter controle da profundidade da interface durante a retirada considerando volume de 9,2 bbl bombeado, volume de aço retirado e perdas para a formação.
Itens 11, 14, 15 e 16: Nestas etapas serão bombeados volumes de FCBA 9,2 ppg para o anular, que deverão interferir na profundidade da interface.
Item 24: 
Trocar fluido do trip tank.
Alinhar trip tank para BFM para flow check estático com BA instalado.

### 7-JUB-78D-ESS — (Contingência) Condicionamento Para Descida De Calha
**Ramon Moreira Fernandes** | v2

Prezados

Não é necessário usar PS na RCD. Na ET temos a seguinte especificação:
"6.4.2.11 Não será aceita solução de Cabeça Rotativa com necessidade de instalação/ desinstalação de bucha protetora no bore da Cabeça Rotativa para sua proteção. Caso seja utilizada, será de inteira responsabilidade da CONTRATADA, não fazendo jus ao pagamento de taxa relativa a essa operação. Além disso, seu drift deverá ser de, no mínimo, 17 3/4"."

No nosso padrão de perfuração SBP temos também uma orientação similar:
"Não deverá ser utilizada bucha de proteção na cabeça rotativa, ainda que o conjunto de vedação não esteja instalado. Para isso devem ser observadas as recomendações do fabricante sobre a limpeza da área antes do assentamento do conjunto de vedação, bem como o monitoramento da inclinação da coluna de riser e diâmetro das ferramentas que passam pela área de vedação (considerar ferramentas com estrutura cortante de ataque lateral)."

> ↳ **Raphael Depes Bruzzi Emery:** Ramon, a instalação da PS foi definida ainda na etapa de planejamento da intervenção, desta forma entendo que devemos seguir o planejamento.

### 7-JUB-78D-ESS — (Contingência) Condicionamento Para Descida De Calha
**Ivani Tavares de Oliveira** | v1

De acordo, só uma observação:
Verificar o melhor momento de retirar a PS. Se houver outras corridas, lembrar de retirar antes de descer o BA.

### 7-JUB-78DA-ESS — Amortecimento, condicionamento e retirada do BHA 8,5pol
**Ramon Moreira Fernandes** | v1

Observações MPD / passo 20: atualizar simulação de retirada com novo cenário de Pp.

Sequência operacional:
Passos 3, 4 e 5: alternativa para amortecimento: ao invés de manter circulação pela booster no início do amortecimento, manter circulação em circuito de superfície via linha de PMCD + contrapressão. Com circuito de superfície + contrapressão, substitui linhas submarinas (kill, choke e booster) e em seguida troca fluido do poço aberto + revestido.
Alinhamentos:
Tq X (FPBA 8,8 ppg) -> SPP2 -> linha de PMCD -> Choke MPD
Tq Y (FPBA 9,0 ppg) -> SPP1 -> troca de fluido linhas subamrinas e poço aberto/revestido.
Vantagem: evitar ficar com circulação somente pela coluna no intervalo de 500 bbl a 1100 bbl.

Passos 14, 15 e 16: Sugiro usar contrapressão para compensar efeito swab e maximizar velocidade de manobra.

### 7-JUB-78DA-ESS — Fechamento da VIF, substituição fluido e retirada da COT
**Gustavo Costa Magalhaes Pena** | v2

De acordo. Em caso de nova revisão sugiro ajuste no trecho que fala sobre gás de riser:

Com BA instalado, alinhar retorno do MPD para MGS e avaliar fechamento do DSIT/AID (para fechamento do DSIT/AID precisa interromper rotação). Mais detalhes padrão PE-2POC-01113, item 3.8.4.

Sem BA instalado, fechar diverter e circular alinhado para o MGS. Seguindo as instruções da tabela.

### 7-JUB-78DA-ESS — Fechamento da VIF, substituição fluido e retirada da COT
**Leonardo Mesquita Caetano** | v1

Caros,
em "GÁS DE RISE" considerar cenário de gás de riser com BA instalado (até o passo 11) o retorno deve ser alinhado para o MGS.

### 7-MRO-37-RJS — Amortecimento e retirada da coluna
**Leonardo Mesquita Caetano há um ano** | v3

Caros, 
de acordo com a sequência.

Comentários extras para revisão:
Item 5 - Para mim está claro, mas acho prudente especificar sem vazão na coluna:
"Descer coluna até o fundo sem rotação e sem vazão *na coluna* a 3 min/sç."


Item 28. Sugestão de realizar uma despressurização gradual para que seja observado qualquer indicio de vazamento precocemente.

Item 31. Sugestão de avaliar chegada da interface através das propriedades do fluido com o coriolis.

> ↳ **Renan Luiz Costa de Carvalho há um ano:** Alterado na v.4.

### 7-MRO-37-RJS — Amortecimento e retirada da coluna
**Ramon Moreira Fernandes há um ano** | v2

Passo 9 / b: MP4 e MP5: Mantém circulação a 600 gpm pela booster e MPD em modo SBP...

Passos 13 a 16: O posicionamento do glicerinado com baixa vazão e retirada de coluna simultânea é uma operação complexa do ponto de vista da modelagem MPD. Sugiro adotar outra estratégia para posicionar o glicerinado no poço aberto. Exemplo do BUZ93: 1) posicionar glicerinado em poço aberto + 200 bbl de excesso no poço revestido, 2) retirar coluna até topo do glicerinado sem circulação pela coluna compensando swab com contrapressão, 3) continuar troca do revestimento. Importante usar uma reologia adequada no logging pill, suficiente para segurar as perdas mas não tão alta para permitir uma manobra sem pistoneio elevado.

### 7-MRO-37-RJS — Amortecimento e retirada da coluna
**Leonardo Mesquita Caetano há um ano** | v1

Caros, bom dia.

- Sugestão de usar compensação de swab no modelo MPD.
- No item 35, pode se fechar válvula de croosover, para forçar fluxo passando por uma mangueira e retornando por outra.

> ↳ **Lucas Loures Sa há um ano:** Bom dia Leo, obrigado pelos comentários. A compensação do swab seria sim uma opção. Entretanto, devido aos atrasos inerentes da compensação do swab, estamos achando mais seguro trabalhar no modo SBP. Estamos trabalhando em uma tabela de valores de SBP necessário de acordo com a posição do fluido FCBA 9,35 ppg no poço e o swab. Daí nossa vida ficará mais fácil.

### 7-MRO-37-RJS — Rebaixamento do cimento, condicionamento e teste do revestim
**Gustavo Costa Magalhaes Pena há um ano** | v1

De acordo. Aproveitar e testar funcionalidade das PRVs junto com o teste do BFM.

Existem outros testes MPD para serem feitos, mas eles podem ser inseridos em sequencias mais pra frente:
1) Teste do sistema de contrapressão Halliburton (precisa de equipe MPD Halliburton a bordo).
2) Teste HP das NRVs (deve ser feito mais próximo da descida do BHA).

> ↳ **Osvaldo Chaves do Nascimento Neto há um ano:** Boa tarde, Pena!

Serão feitos em sequências posteriores após embarque da equipe Halliburton. Os testes das NRVs vamos deixar para fazer mais próximo da descida do BHA 8 1/2".

### 8-BUZ-89D-RJS — Condicionamento do poço, troca do fluido e retirada do BHA 8
**Leonardo Mesquita Caetano** | v2

Caros,
solicitado a Halliburton que seja feita a simulação de manobra com fluido visco. Assim que disponível, incluir a tabela nova e as referências de reologias.

### 8-BUZ-89D-RJS — Condicionamento do poço, troca do fluido e retirada do BHA 8
**Leonardo Mesquita Caetano** | v1

Caros,
de acordo com os comentários do CSD-BUZ.

No item 10 - usar modo de compensação de swab.

### 8-BUZ-96D-RJS — [Contingência] Perfuração 8 1/2”, manobra em F/PMCD dinâmico
**Gustavo Costa Magalhaes Pena** | v7

Seguem comentários:

Recomendo retirar informações do BHA#1 com Nitroforce e ajustar nos parâmetros de perfuração.

Recomendo revisar a sequencia operacional considerando a recomendação do padrão de utilizar o dobro das vazões simuladas de controle e bullheading, quando utilizando SAC no anular.

### 8-BUZ-96D-RJS — [Contingência] Perfuração 8 1/2”, manobra em F/PMCD dinâmico
**Ramon Moreira Fernandes** | v6

Controle de migração sempre via anular

### 8-BUZ-96D-RJS — [Contingência] Perfuração 8 1/2”, manobra em F/PMCD dinâmico
**Ramon Moreira Fernandes** | v4

Passos 38 e 39: repetir a observação de abastecimento contínuo do anular a 4 bpm (preferencialmente via booster).

> ↳ **Matheus Marins Gonzaga:** Obrigado pelos comentários, Ramon.

Serão aplicados na versão 5.

### 8-BUZ-96D-RJS — [Contingência] Perfuração 8 1/2”, manobra em F/PMCD dinâmico
**Ramon Moreira Fernandes** | v4

Passo 12/b: Como nesse cenário estamos com fluido overbalance, a depender da vazão que estiver sendo injetada pode ficar com a SBP zerada. Portanto o abastecimento do poço precisa ser contínuo via anular (preferencialmente via booster).

### 8-BUZ-96D-RJS — [Contingência] Perfuração 8 1/2”, manobra em F/PMCD dinâmico
**Ramon Moreira Fernandes** | v3

Passo 13/b: a informação do volume do poço revestido (560 bbl) não tem relevância nesse passo.

### 8-BUZ-96D-RJS — [Contingência] Perfuração 8 1/2”, manobra em F/PMCD dinâmico
**Ramon Moreira Fernandes** | v3

Passo 12/b: uma vez todo anular preenchido com SAC, manter abastecimento contínuo com SAC via linha de booster a 2-3 bpm.

### 8-BUZ-96D-RJS — [Contingência] Perfuração 8 1/2”, manobra em F/PMCD dinâmico
**Ramon Moreira Fernandes** | v1

Passo 3: para o teste de injetividade com FPBA 8,7 ppg não há necessidade de efetuar mudança de alinhamento: pode manter 2 bombas na coluna e 2 bombas na booster. Só precisa alinhar 2 bombas para linha de PMCD depois de concluir o teste de injetividade (passo 5 em diante).

### 8-MRO-36-RJS — Retirada do BHA 8,5 pol, condicionamento, amortecimento
**Geronimo de Freitas Rolandi** | v1

Item 9:
Ótima iniciativa de manter a pressão do poço através do circuito de superfície para evitar contaminação durante a troca pela booster, mas  o circuito de superfície poderia ficar  alinhado para o poço pelas mangueiras -> flowspool mesmo, na sequencia manda alinhar pelo choke Manifold (GV2) mas não especifica por qual linha vai atacar o poço (kill ou choke).
Sugestão: 
MP3 e MP4 – Mantém circulação a 600 gpm e MPD em modo SBP para manter 9,3 ppg na sapata 10 3/4” pela booster
MP1 e MP2 – Alinhar para STP#2 -> STP-AUX -> PMCD -> Buffer manifold (B3 Fechada)
Pressurizar com MP1 contra B3, até SBP para equalizar pressão
Abrir B3, aumentar vazão da MP1 e MP2 e diminuir MP4 e MP4,

### 9-BUZ-103D-RJS — 18 - Preparar para perfurar fase 4 com MPD - parte 1
**Ramon Moreira Fernandes** | v1

Após discussão com os CSDs AGUP, BUZ e SF, segue nova estratégia para troca de fluido evitando problemas de contaminação:

Não instala SSA inicialmente
Corta cimento até 10 m da sapata com FPBNA
Troca fluido de todo sistema FPBNA por FPBA
Instala SSA e testa sistema MPD com FPBA
Efetua fingerprint MPD...

### 9-BUZ-103D-RJS — 18 - Preparar para perfurar fase 4 com MPD - parte 1
**Ramon Moreira Fernandes** | v1

Passo 3, item f: Sugiro colocar da seguinte forma:
Alinhamento para pressurizar o riser: UC->Choke Manifold->Linha submarina
Alinhamento para pressurizar o buffer: Bomba da sonda->linha de PMCD->BM
Alinhamento para despressurizar o buffer: BM->Choke Manifold->Choke hidráulico da sonda->Stripping tank

Passo 3: Acrescentar critério de aceitação dos testes:
Baixa pressão: queda máxima 10 psi / 5 min (PINICIAL ≤ 350 psi). 
No teste de baixa, se a pressão ficar entre 350 psi e 500 psi na pressurização, drenar até < 350 psi. Se ultrapassar 500 psi, drenar até zero e reiniciar.
Alta pressão: queda máxima 40 psi / 5 min (1900 psi ≤ Pfinal ≤ 2000 psi – pressão nominal).

Passo 4: O primeiro teste de baixa com FPBNA costuma demorar para estabilizar a pressão. Para otimizar o tempo de estabilização sugiro pressurizar até 475 psi e aguardar 15 min de "acomodação" para em seguida drenar até o range do teste (250-350psi).

Passos 13 e 14: Manter LACD relaxado e linha de 2" ventilada.

Para trocar o fluido acima do SSA e do trip tank, sugiro fazê-lo antes de iniciar a troca do poço, entre passos 34 e 35, da seguinte forma: esvaziar trip tank, alinhar bomba da sonda para linha de 2", manter LACD fechado, abrir UACD e trocar FPBNA por FPBA acima do ACD retornando para trip tank. Interromper bombeio quando começar a retornar FPBA no trip tank e esvaziar novamente trip tank para preenchê-lo com FPBA.

### 9-BUZ-103D-RJS — 19 - Preparar para perfurar fase 4 com MPD - parte 2
**Leonardo Mesquita Caetano** | v1

Caros, 

Incluir uma verificação do sistema de monitoramento da ACD, conforme comentário do CSD BUZ.

Item 3. Dispensar: já é realizado junto com MPD drill
Item 9. Dispensar item 4
Item 12. Realizar apenas o simulado da operação que vai acontecer: DFIT (Dispensar simulado de DPPT)
