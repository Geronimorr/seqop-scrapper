# Fingerprint / Treinamento MPD

40 SEQOPs | 70 comentários MPD

## Análise IA dos Comentários

```json
{
  "sub_tipos": [
    "Fingerprint offline",
    "Fingerprint online",
    "Treinamento prático MPD",
    "MPD Drill",
    "Choke Drill",
    "DLOT",
    "Corte de cimento",
    "Troca de fluido",
    "Simulado de Hang-off",
    "Calibração do modelo hidráulico",
    "Teste de influxo (DPPT/DFIT)"
  ],
  "pontos_verificacao": [
    {
      "item": "Configuração e teste das PRVs (válvulas de alívio de pressão)",
      "frequencia": "alta",
      "exemplo_real": "Confirmar válvulas de bloqueio das PRVs abertas e travadas com cadeado."
    },
    {
      "item": "Calibração do PID e eficiência das bombas",
      "frequencia": "alta",
      "exemplo_real": "Sugiro efetuar uma calibração preliminar do PID e ajuste da eficiência de bombas com o FPBNA 9,1 ppg antes de iniciar a troca de fluido."
    },
    {
      "item": "Verificação de alinhamentos do sistema MPD",
      "frequencia": "alta",
      "exemplo_real": "Alinhar sistema MPD: JC, Coriolis e Choke MPD."
    },
    {
      "item": "Monitoramento de parâmetros de segurança (SBP, ECD, PRC)",
      "frequencia": "alta",
      "exemplo_real": "Atentar para setpoint das PRVs acordado com a Transocean."
    },
    {
      "item": "Execução de fluxogramas atualizados",
      "frequencia": "alta",
      "exemplo_real": "Atualizar o fluxograma de controle de influxo com sistema MPD."
    },
    {
      "item": "Simulação de cenários críticos (ex.: influxo, DLOT, DPPT)",
      "frequencia": "alta",
      "exemplo_real": "Simulado de Hang-off e Choke Drill vem logo após do simulado de MPD Drill."
    },
    {
      "item": "Preenchimento e envio de checklists",
      "frequencia": "média",
      "exemplo_real": "Preencher checklist do MPD Drill que será anexado ao SIP a título de checkpoint."
    },
    {
      "item": "Troca de fluido e limpeza do sistema",
      "frequencia": "média",
      "exemplo_real": "Efetuar primeiro flush das mangueiras de MPD 6\" e 2\" para ambiente controlado."
    },
    {
      "item": "Ajuste de vazões e pressões durante operações críticas",
      "frequencia": "alta",
      "exemplo_real": "Considerar maior vazão possível na coluna para efetuar o DLOT de modo a minimizar a máxima SBP."
    }
  ],
  "erros_frequentes": [
    "Fluxogramas desatualizados ou duplicados",
    "Falta de calibração adequada do PID e eficiência das bombas",
    "Alinhamento incorreto ou incompleto do sistema MPD",
    "Configuração inadequada das PRVs",
    "Falta de registro ou preenchimento incompleto de checklists",
    "Execução de etapas fora de sequência ou desnecessárias",
    "Ausência de alertas para riscos específicos (ex.: indexação do alargador)",
    "Subutilização de vazões adequadas para operações críticas"
  ],
  "padroes_aprovacao": [
    "Utilização de fluxogramas atualizados e claros",
    "Execução de simulações práticas e treinamentos complementares",
    "Configuração correta e teste prévio de todos os equipamentos",
    "Manutenção de alinhamentos consistentes e seguros",
    "Preenchimento completo e envio de checklists para registro",
    "Ajustes de parâmetros operacionais conforme padrões técnicos",
    "Execução de operações críticas com atenção aos limites de segurança"
  ],
  "normas_aplicaveis": [
    "PE-2POC-01113",
    "PE-1PBR-00047",
    "PE-1PBR-01326",
    "NS-33 – 1-ESS-229"
  ]
}
```

## Comentários MPD Completos

### 1-RJS-763D — 23 - Troca de Fluido, Fingerprint, Corte do Cimento e DLOT
**Ivani Tavares de Oliveira** | v3

Em MPD DRILL:
Sugiro remover os 4 "fluxogramas detalhados" do item 8 - e). O fluxograma completo é suficiente, é o mesmo do padrão.

### 1-RJS-763D — 23 - Troca de Fluido, Fingerprint, Corte do Cimento e DLOT
**Gustavo Costa Magalhaes Pena** | v2

Prezados, seguem comentários e sugestões:

Em troca de fluido, item 6:
c) Linha de PMCD alinhada para linha de 2" pela MPDV17, com retorno para as mangueiras de 6" e linha by-pass do BFM.
e/f) Não vejo necessidade de fazer essas etapas neste momento. Sugiro aguardar a troca do fluido do poço e então fazer (pequeno volume).

Em Simulado de hang-off e Choke drill, item 16: Esse item é o ultimo passo do MPD Drill (acredito que esteja contemplado na SeqOp de FP e TP MPD).

Em corte do cimento, item 30: Atenção para o risco de plugueamento do choke com cimento. Se necessário alternar chokes para a limpeza, avaliar junto ao CSD MPD a necessidade de reduzir/interromper o corte/vazão para evitar plugueamento de ambos os chokes ao mesmo tempo (risco de atuação do dispositivo de segurança e despressurização do poço).

### 1-RJS-763D — 23 - Troca de Fluido, Fingerprint, Corte do Cimento e DLOT
**Ramon Moreira Fernandes** | v1

Passo 9: atenção nesta etapa pois o PID ainda não terá sido calibrado e a eficiência de bombas também. Sugiro efetuar uma calibração preliminar do PID e ajuste da eficiência de bombas com o FPBNA 9,1 ppg antes de iniciar a troca de fluido (antes do passo 4). Posteriormente conclui-se a etapa de calibração de PID e ajuste de eficiência de bombas durante o fingerprint com fluido leve.

Passo 17: O simulado de hangoff e choke drill vem logo após do simulado de MPD Drill (seqop do fingerprint). No final do MPD Drill estaremos com anchor point acima da Pp simulada. Portanto para dar continuidade ao Choke Drill, é interessante continuar no cenário mantendo contrapressão no poço. Portanto após fechar o BOP anular, será necessário pressurizar a linha submarina de kill com SBP de shutin antes de abrir as válvulas submarinas e continuar o choke drill com este cenário que reflete melhor a transição do controle de poço do MPD para sonda numa situação real.

DLOT: considerar usar a maior vazão possível na coluna para o DLOT de modo a reduzir a máxima SBP esperada. Atentar para setpoint das PRVs acordado com a Transocean.

### 1-RJS-763D — 23a - Fingerprint de MPD
**Gustavo Costa Magalhaes Pena** | v2

Prezados, seguem comentários e sugestões:

Em CSBs: Vamos ter feito no item 13 da SeqOp de troca de fluido um flowcheck estático de 30 min para atestar que o fluido FPBNA 8,8 ppg (em estática) + tampão de cimento são barreira. Esta confirmação vai permitir que durante o FP e TP o sistema MPD não seja necessário para manutenção do CSB primário.

Em calibração do modelo hidráulico, item 20: A vazão da booster na tabela está 300 gpm quando deveria ser 350 gpm. Conferir se a perfuração será com AP 9,9 ppg, na SeqOp de perfuração para DLOT está com AP 9,1-9,4 ppg.

Em simulado DLOT, item 22/23: Verificar se existe necessidade de ajuste de eficiência a cada 5 steps (variação de 250 psi). Se sim, registrar nova eficiência.

### 1-RJS-763D — 23a - Fingerprint de MPD
**Ramon Moreira Fernandes** | v1

Passos 17 e 18: Considerar maior vazão possível na coluna para efetuar o DLOT de modo a minimizar a máxima SBP.

Passo 17: Explicação sobre item 7 da tabela: o procedimento para circular o gás residual trapeado abaixo do BA consiste em promover um alinhamento via linha de 2" para o choke da sonda sem se comunicar com o alinhamento do flowspool. Em seguida abre-se progressivamente o choke da sonda observando redução do do flowout em relação ao flowin (parcela de fluxo que vai para linha de 2" não passa pelo coriolis). É desejável que abrindo o choke hidráulico da sonda consiga ter um fluxo de pelo menos 150 gpm pela linha de 2" (será observado pela diferença entre flowin e flowout).

Passo 17: Sugiro unificar item 5 e 6 da tabela com alinhamento para ambas mangueiras: corresponde à condição de manobra. Adicionar um item para medição de perda de carga passando apenas por 1 mangueira.

Passo 20/a: Completar ou aliminar a frase "NOTA: como o peso de fluido (8,8 ppg) está muito próximo do ECD desejado (9,9 ppg), ".

Passo 20/b: Eliminar Nota sobre aferição alternativa via sensor do BOP, pois esta aferição é muito imprecisa.

DLOT: Considerar uso de maior vazão para minimizar a máxima SBP durante o DLOT.

Treinamento Prático MPD: pelo nosso registro foram treinadas as equipes A e E em 11/08 (fase debug intermediária). Prever treinamento prático complementar após o fingerpint para as equipes a bordo.

### 1-RJS-763D — 23b - Treinamento Prático de MPD
**Ivani Tavares de Oliveira** | v2

Em TREINAMENTO PRÁTICO item 4 - c) Todas as bombas estão no barramento B.

### 1-RJS-763D — 23b - Treinamento Prático de MPD
**Gustavo Costa Magalhaes Pena** | v1

Seguem comentários e sugestões:

Em CSBs: Vamos ter feito no item 13 da SeqOp de troca de fluido um flowcheck estático de 30 min para atestar que o fluido FPBNA 8,8 ppg (em estática) + tampão de cimento são barreira. Esta confirmação vai permitir que durante o FP e TP o sistema MPD não seja necessário para manutenção do CSB primário.

Em MPD Drill:
Item 23: Corrigir gráfico do sub-item 6.
Páginas 11 e 12: Retirar fluxogramas.

### 1-RJS-763D — Fingerprint e Treinamento Pratico MPD
**Geronimo de Freitas Rolandi** | v3

Ao término do MPD drill:

 Sonda fecha o BOP anular e alinha linhas submarinas para monitoramento do poço. A partir desta etapa inicia-se o simulado de Hang-off conforme PE-1PBR-00047 SIMULADO DE HANGOFF E CONTROLE DE POÇO (CHOKE DRILL).
 Sonda e MPD Despressuriza o riser e monitorando pressão do BOP e monitora riser via trip tank (alinhamento de flow check estático).
Em caso de suspeita de gás de riser, mantém riser pressurizado e circula 1 volume de riser com DSIT fechado alinhando retorno para MGS monitorando sensor de gás no flow divider (apenas conversar e explicar os alinhamentos). Uma vez concluída circulação, seguir para despressurização e monitoramento do riser.
Fiscalização e sonda fazem o planejamento e a simulação de circulação do influxo pelo método do sondador. A partir desta etapa inicia-se o simulado de Choke Drill conforme PE-1PBR-00047 SIMULADO DE HANG-OFF E CONTROLE DE POÇO (CHOKE DRILL).

### 1-RJS-763D — Fingerprint e Treinamento Pratico MPD
**Geronimo de Freitas Rolandi** | v3

Ao término do MPD drill:

 Sonda fecha o BOP anular e alinha linhas submarinas para monitoramento do poço. A partir desta etapa inicia-se o simulado de Hang-off conforme PE-1PBR-00047 SIMULADO DE HANGOFF E CONTROLE DE POÇO (CHOKE DRILL).
 Sonda e MPD Despressuriza o riser e monitorando pressão do BOP e monitora riser via trip tank (alinhamento de flow check estático).
Em caso de suspeita de gás de riser, mantém riser pressurizado e circula 1 volume de riser com DSIT fechado alinhando retorno para MGS monitorando sensor de gás no flow divider. Uma vez concluída circulação, seguir para despressurização e monitoramento do riser.
Fiscalização e sonda fazem o planejamento e a simulação de circulação do influxo pelo método do sondador. A partir desta etapa inicia-se o simulado de Choke Drill conforme PE-1PBR-00047 SIMULADO DE HANG-OFF E CONTROLE DE POÇO (CHOKE DRILL).

### 1-RJS-763D — Fingerprint e Treinamento Pratico MPD
**Ramon Moreira Fernandes** | v2

Para o MPD Drill sugiro usar o modelo de seqop do NS-28, 3-RJS-762:

### 1-RJS-763D — Fingerprint e Treinamento Pratico MPD
**Ramon Moreira Fernandes** | v2

Prezados

No passo 38, ficou algum bug na visualização do fluxograma.
Esse passo corresponde ao MPD Drill cujo padrão ainda não foi publicado, porém já temos uma edição quase finalizada com um passo a passo mais bem detalhado. Enviamos pelo teams o padrão com o passo a passo para facilitar a atualização da seqop.

### 1-RJS-763D — Fingerprint e Treinamento Pratico MPD
**Ramon Moreira Fernandes** | v1

Passo 2: sugiro revisar ou remover os gráficos de circuito de superfície para teste das PRVs. Nos gráficos as válvulas a montante do junk catcher estão fechadas... o teste é feito com circulação pelo sistema de contrapressão (by-passando apenas o coriolis).

Passo 3: no item b fala em usar o modo posição; no item c fala em usar o modo SBP. O correto nessa etapa é usar o modo posição. Portanto alterar item C para "modo posição".

Passo 5: O gráfico do P&ID não condiz com o alinhamento para a calibração dp PID de superfície. Sugiro revisar ou remover. Nessa etapa as mangueiras do flowspool ficam isoladas do buffer.

Passo 11: Atualizar o fluxograma de controle de influxo com sistema MPD:
(imagem tbm disponível no padrão PE-2POC-01113 - [ MPD ] [ SBP ] [ OPER ] DETECÇÃO E CIRCULAÇÃO DE INFLUXO COM SISTEMA MPD)

Passos 15 e 17: verificar qual será a vazão de perfuração da fase (normalmente próxima do maior valor do range das ferramentas) e utilizar essa vazão para calibração do PID e aferição de perda de carga.

Passo 17: Está previsto DPPT nessa fase? Caso não esteja, não precisa medir a perda de carga com vazão de 650 gpm (linha #3 da tabela).
Obs: O objetivo da linha #7 da tabela é verificar a parcela de vazão que irá circular pela linha de 2" ao abrir o choke da sonda (sangria dinâmica). Para isso precisa estar com o coriolis alinhado e verificar a redução do flowout pelo coriolis. É desejável que parcela de vazão pela linha de 2" seja superior a 100 gpm de modo a garantir o carreamento de fluxo multifásico durante eventual remoção de gás trapeado abaixo do BA.

Passo 18: Na segunda tabela, linha #1 consierar vazão de 400 gpm na booster para conexão. Na linha #3 considerar vazão de 600 gpm na booster para manobra. Na linha #4 considerar a mesma vazão usada na calibração de perda de carga de superfície no DLOT: 800 gpm.

Passo 19: o PWD Baker normalmente fornece o ESD moda que pode ser usado para calibrar o modelo hidráulico no lugar do ESD med. O ESDmin e ESDmax não devem ser usado como referência para essa calibração.

Passo 20: ajustar terminologia do "PWDCF" (próprio da Halliburton) para o sistema de contrapressão da SLB. Verificar informação com supervisor SLB. Segue sugestão de tabela para calibração do Pumps-On:

Passo 23: Registrar eventuais alterações do parâmetro de eficiência de bombas na tabela de modo deixar a informação mapeada para a execução posterior do DLOT.

Passo 34: Sugiro executar o item b (não apenas verbalmente) por se tratar de etapa crítica de transição de ataque ao poço que demanda experiência prática nas mudanças de alinhamentos e comunicação.

Passo 35: Sugiro executar itens a, b, c, j, K e L (não apenas verbalmente) por se tratar de etapa crítica de transição de ataque ao poço que demanda experiência prática nas mudanças de alinhamentos e comunicação.

Passo 38: Idem comentário do passo 11 (fluxograma atualizado). Preencher checklist do MPD Drill que será anexado ao SIP a título de checkpoint.

### 1-RJS-763D — S10 - Troca de Fluido _Corte do Cimento_ Fingerprint e DLOT
**Gustavo Costa Magalhaes Pena** | v4

De acordo.

Em caso de nova revisão, se possível, justificar a necessidade de utilizar passos de 25 psi ao invés de 50 psi no DLOT, conforme estabelece o padrão.

> ↳ **Denes Marcel Chaves Lopes:** Devido pressão de fratura baixa e já próxima ao ECD, foi reduzida o step de pressão do DLOT.

### 1-RJS-763D — S10 - Troca de Fluido _Corte do Cimento_ Fingerprint e DLOT
**Ramon Moreira Fernandes** | v2

Ótima sequência!

### 1-RJS-763D — S10 - Troca de Fluido _Corte do Cimento_ Fingerprint e DLOT
**Geronimo de Freitas Rolandi** | v1

39 c) - Muito bom o lembrete sobre a força ascendente na coluna devido ao DLOT, acho que para complementar à informação poderia mencionar que o sondador deve despressurizar o compensador de x psi a cada y psi do DLOT. Alternativamente avaliar a possibilidade de fechar o DSIT logo acima de um tool joint para segurar a coluna.

> ↳ **Eduardo Duarte Nascimento:** Boa noite. Em função do peso da coluna ser suficiente para conter movimento ascendente, achamos que esse stress no DSIT pode ser desnecessário e gerar consequências como seu desgaste prematuro.

### 3-RJS-762 — 10 Troca de fluido, corte de cimento, fingerprint MPD e FIT
**Leonardo Mesquita Caetano há um ano** | v3

Caros, acredito que a V3 que foi carregada no sistema foi trocada com outro arquivo.

> ↳ **Andre Santos Doria há um ano:** Correto. Vou postar novamente.

### 3-RJS-762 — 10 Troca de fluido, corte de cimento, fingerprint MPD e FIT
**Gustavo Costa Magalhaes Pena há um ano** | v2

De acordo. 

Porém tenho uma sugestão. No item 19, avaliar a real necessidade de utilizar o sistema MPD para cortar o restante do cimento, condicionar rat hole e perfurar 5 m de formação nova (Fluido 8,7 ppg e AP 9,2 ppg). Como não estamos em zona com potencial de fluxo, recomendaria manter o alinhamento do item 2 (by-pass MPD) até a conclusão do FIT para evitar passar cimento, sapata e acessórios pelo sistema MPD.
Somente após a conclusão do FIT (item 39), com o poço já limpo, ai sim faríamos o alinhamento do sistema MPD para seguir com perfuração MPD (Debug).

Caso a minha sugestão não seja acatada, recomendo postar o alinhamento que será utilizado no item 19, assim como relembrar o setting dos dispositivos de segurança do MPD (durante a execução do Fingeprint e treinamento prático esses settings podem ter sido alterados).

> ↳ **Andre Santos Doria há um ano:** Acertado com CGEP e PROJ para fazer o by-pass do manifold MPD durante o corte de cimento e sapata, circular 1 BU para limpeza e perfurar os 5 m de formação nova alinhado para o MPD (choke e coriollis) mantendo AP 9,2 ppg (poço limpo).

V3 será postada com essa alteração, atendendo ao proposto pelo CSD MPD e mantendo o planejamento do debug a partir do início da fase (1º metro perfurado).

### 3-RJS-762 — 10 Troca de fluido, corte de cimento, fingerprint MPD e FIT
**Geronimo de Freitas Rolandi há um ano** | v1

Prezados, boa noite,
Como o BA terá sido instalado na sequência anterior, não será possível efetuar a troca do fluido acima do BA conforme está descrito nessa sequência. Teremos duas opções, conviver com AGMAR no Trip Tank e acima do BA ou efetuar essa troca utilizando o ported sub da Junta Integrada. No caso de mantermos AGMAR no Trip Tank, se observado vazamento do BA, deveremos monitorar a chegada da interface do fluido FPBNA no Diverter (~40 bbl) para evitar contaminação do tanque com AGMAR com FPBNA.

> ↳ **Renato da Costa Aparecido há um ano:** Bom dia!

Podemos conviver com AGMAR acima do BA, confirmado com químicos de bordo. Não haverá problema se acabar incorporando ao FPBNA.

### 3-RJS-762 — 10 Troca de fluido, corte de cimento, fingerprint MPD e FIT
**Ramon Moreira Fernandes há um ano** | v1

Prezados

Em "Preparativos" / [Sonda/MPD] / b / bullet 4: não ficou muito claro se será feito sistematicamente o alinhamento de uma segunda bomba para linha de booster nas conexões ou se será feito somente em caso de falha da booster na conexão... O ideal é que nas conexões tenhamos sempre 2 bombas na booster (de barramentos distintos), para se prevenir de uma despressurização por falha de bomba durante a desconexão. Como para perfuração será necessário 3 bombas na coluna, isso implica em ficar sempre realinhando as bombas para a conexão...

Em "Operações Offline" / 1: mencionar testes das NRVs.

> ↳ **Renato da Costa Aparecido há um ano:** Boa tarde!

Conversado com preposto MPD BR de base e achado melhor alterar planejamento para 2 bombas na coluna e 1 bomba na booster (+ 1 bomba spare, alinhada para booster).

Mencionado teste das NRVs.

### 3-RJS-762 — 10a Fingerprint e Treinamento Pratico MPD
**Geronimo de Freitas Rolandi há um ano** | v2

15 e 16: Como teremos um fingerprint adicional posteriormente com fluido 7,8 ppg, incluir mais steps de pressão x-100, x-50, x, x+100, x+200, x+ 300, x +400. 
18. Calibrar a eficiencia das bombas com os valores simulados para o fluido 7,8 ppg também (consultar pessoal Halliburton a bordo para simulações)

### 3-RJS-762 — 10a Fingerprint e Treinamento Pratico MPD
**Geronimo de Freitas Rolandi há um ano** | v1

Prezados, 
A SPL deve ser configurada para pressão do FIT - 100 psi, na sequencia inteira está com a pressão do FIT.

> ↳ **Renato da Costa Aparecido há um ano:** Bom dia!

Alteração contemplada na V2 (com SPL configurado para 80% do FIT, conforme combinado).

### 3-RJS-762 — 19 MPD Drill, Choke Drill e Corte do cimento
**Fábio Koiti Dairiki** | v3

Caros, boa tarde
Item A3, letra d:  Sugerido adicionar: PRV #3 (PMCD) e PRV #4 (Choke Manifold) deverão estar protegendo o sistema MPD (menor classe de pressão) de sobrepressurização acidental durante o teste (NS-33 – 1-ESS-229 – 26/03/2024). Alternativamente, o sistema MPD pode estar ventilado durante o teste.

### 3-RJS-762 — 19 MPD Drill, Choke Drill e Corte do cimento
**Gustavo Costa Magalhaes Pena** | v2

Seguem comentários:

Uma recomendação visando redução de complexidade e de escopo, sem abrir mão da segurança:
Após conferir o TOC, partir para a etapa de Fingerprint, simulado Hang-off, Choke drill e MPD drill ainda com FPBNA 8,7 ppg.
Em seguida, efetuar o corte do cimento, sapata e perfuração de 5 m de formação nova ainda com FPBNA 8,7 ppg e com sistema MPD by-passado no BFM. Então executar o microfrac ainda com FPBNA 8,7 ppg.
Após o microfrac, descer o BHA até o fundo e efetuar a troca de fluido de FPBNA 8,7 ppg para FPBNA 8,2 ppg com AP 9,0 ppg no fundo (se o retorno estiver sem excesso de cimento, já poderemos contar com coriolis, caso contrário, vamos manter o coriolis by-passado até a conclusão da troca de fluido). 
Com FPBNA 8,2 ppg e AP 9,0 ppg no fundo, faremos uma verificação ajustes do Fingerprint, com a premissa de sempre manter o AP 9,0 ppg no fundo. Toma-se nova PCR e perda de carga nas linhas.
E com tudo ajustado e calibrado, damos sequencia na perfuração da fase.

Essa estratégia visa retirar complicações de utilização do choke MPD com retorno de cimento (risco de entupimento), necessidade de efetuar teste de influxo (redução de escopo) e realização de microfrac com necessidade de manutenção do poço pressurizado o tempo todo (risco de despressurização do poço).
O prejuízo é a necessidade de verificação/ajuste do FP com o poço aberto, que vai exigir mais atenção da equipe do sistema de contrapressão, mas que é previsto no padrão PE-1PBR-01326 -FINGERPRINT MPD.

Após o item 16, inserir o MPD Drill, que deve ser realizado após verificação da PRC e antes do simulado hang-off e choke drill.

### 3-RJS-762 — 19a Fingerprint (Anexo)
**Fábio Koiti Dairiki** | v3

Boa tarde,

Cabeçalhos de Fingerprint parte 2: Trocar fluido para FPBNA 8,7 ppg.

Obs: Com a informação de que não há restrição para efetuar o FP de testemunhagem (200 gpm) no poço revestido por conta do alargador, vamos realizar o FP completo com FPBNA 8,7 ppg e etapas parciais para confirmação após troca para FPBNA 8,2 ppg para minimizar as etapas em poço aberto.

### 3-RJS-762 — 19a Fingerprint (Anexo)
**Gustavo Costa Magalhaes Pena** | v2

Seguem comentários:

Itens 2 e 14: No ajuste do SPL considerar FPBNA 8,7 ppg.

Em Fingerprint parte 2 - Operação principal: Atentar que faremos um FP primeiro com FPBNA 8,7 ppg para permitir execução do MPD Drill e troca do fluido, ainda antes de cortar a sapata. E depois do microfrac, teremos a troca de fluido mantendo AP 9,2 ppg no fundo, e em seguida iremos repetir algumas etapas do FP para confirmar, e se necessário ajustar, o FP para o FPBNA 8,2 ppg. Estas etapas com FPBNA 8,2 ppg deverão seguir a premissa de manter a pressão no fundo superior a 8,7 ppg.

Após o item 14, a figura que ilustra o alinhamento para fingerprint no caminho crítico não está certa (linha vinho). O alinhamento é o convencional de perfuração.

Item 16, 18 e 19: Considerando a instrução do item 3, não será realizado o FP para a condição de testemunhagem nesta SeqOp. A etapa dedicada para FP na condição de testemunhagem será realizada em poço aberto, ao término da corrida com esse BHA, antes de iniciar a manobra.

O Fluxograma de combate a perda, anexado no final não faz parte do escopo de Fingerprint. Recomendo retirar (uma página a menos).

### 3-RJS-762 — 19a Fingerprint (Anexo)
**Gustavo Costa Magalhaes Pena** | v1

Seguem comentários e recomendações:

Pendente definição quanto à estratégia da SeqOp de Troca de fluido e corte de cimento. Se aceita a recomendação, o FP será realizado com FPBNA 8,7 ppg em poço revestido, e depois confirmado/ajustado com FPBNA 8,2 ppg com poço aberto.


No entanto, já nesta sequencia é possível:

Item 12: Somente confirmar se alarme está funcional. Sem necessidade  de controle, pois será realizado MPD Drill após o FP.

Itens 16, 18, 19, 20, 22, 23: Booster 350 gpm é o suficiente para o choke de 3".

Item 17: Booster 600 gpm.

Item 19 e 20: Incluir verificação para cenário de testemunhagem.

Item 20: Considerar somente uma bomba da booster para conexão e perfuração. A outra fica de spare.

Item 21: Retira subitem a.

Item 23: Faz parte do escopo de treinamento prático, como as equipes a bordo já foram treinadas, esse item pode ser removido.

Item 25: MPD Drill está fora do contexto do FP. Ele deve ser realizado após o FP e registro das PRCs e perdas de carga nas linhas submarinas. Vou enviar um padrão MPD drill, ainda em fase preliminar para ajustar (se necessário) o passo a passo do MPD Drill.

### 3-SPS-111D — 10.1 Fingerprint e Treinamento Prático MPD
**Leonardo Mesquita Caetano há um ano** | v1

Item 16; perda de carga (primeiros registros da sonda).
-Realizar uma linha (digamos #0) de pressão com com vazão de 15 gpm (só para garantir linhas cheias)
-Não realizar alinhamento 12

Item 17. 
No item #2, repetir a eficiência da booster do item #1 (mudar a cor da MP4 para amarelo)

Item 22. 
Itens como "Repetir procedimento para PRV #2" e SPL podem ser conceituais e não precisam ser repetidos

Item 34 e 35. Simulado de kick (MPD Drill - esse simulado é recorrente é recorrente em fases MPD)
O registro deve ser feito no ficha que segue e pode ser adicionada como anexo a SeqOP:
https://petrobrasbr.sharepoint.com/:w:/t/bdoc_POCOS-SPO-SP-FLUI/Eag_uee3_6RNhcZX2uK1NxEBbXkvuV2fhWKlc23dLW4rMA?e=idN8c6

### 3-SPS-111D — 29.1 Fingerpirnt e treinamento prático MPD
**Gustavo Costa Magalhaes Pena há um ano** | v1

Prezados, seguem comentários.

Em teste de alarme de influxo (offline): Ajustar a numeração e incluir o fluxograma atualizado para controle de poço com MPD.

No caminho critico:

Existem etapas que mencionam a vazão de conexão com 300 gpm e outras com 400 gpm. Importante definir qual a vazão de conexão que será praticada, e ajustar na SeqOp.

Existem etapas que mencionam vazão na coluna de 200 gpm, porém durante todo o FP e TP (com o BHA dentro do revestimento) precisamos ter a preocupação de não estabelecer vazão intermediária entre (100-300 gpm) para evitar abrir o alargador. Portanto recomendo retirar as etapas com vazões intermediárias, e além disso incluir alerta para que todas as equipes tenham conhecimento deste risco.
E etapa de fingerprint (perda de carga, modelo hidráulico e eficiência de bomba) com vazão de testemunhagem, poderá ser realizado após a abertura do alargador, preferencialmente ao término da corrida e com o PWD funcional.

Item 20: Não vejo necessidade de realizar a etapa durante o FP (será realizado FIT). Somente incluir no TP para um escopo mais reduzido.

Sobre o treinamento prático:
Apesar das turmas B e C não terem sido treinadas previamente à fase Debug, eles tiveram vivencia de perfuração, conexão e manobra e outros durante a fase, não sendo necessário repetir etapas (o instrutor MPD vai adaptar o escopo do TP para cada turma).

Item 27: O sistema de desvio de fluxo da NOV (ACD/SSA) permite que seja realizado um flow check estático somente despressurizando os packers da ACD.

Item 34: Conhecido como MPD Drill. Atentar para o preenchimento do Checklist para efeito de Check Point no SIP. Atualizado o fluxograma.

> ↳ **Ramon Sena Barretto há um ano:** Boa tarde pessoal!

Sobre o DFIT (comentário "item 20"): mantivemos essa etapa no fingerprinting pois há previsão de eventual DFIT no final da fase, para avaliar o peso de fluido que será posicionado no poço antes da retirada do BHA, por isso mantivemos, em acordo com o CGEP.

Sobre o comentário "item 27": Esse comentário já consta na sequencia, por isso mantivemos.

Obrigado pelo restante dos comentários, serão alterados na próxima versão.

### 3-SPS-111D — Troca de fluido, corte do cimento, fingerprint e DLOT
**Leonardo Mesquita Caetano há um ano** | v2

Caros, 
De acordo com V2, aprovada.

Segue comentários para serem considerados na operação ou para caso haja revisão.


OBSERVAÇÕES DE SEGURANÇA DE POÇO
Item 3. Os selos trabalham com pequenos vazamentos controlados através da pressão de acionamento da SSA. Os parâmetros de desgastes devem ser acompanhado pela sonda conforme as recomendações do fabricante (NOV/AFG).


OPERAÇÃO PRINCIPA
No item 19. Confirmar configuração dos dispositivos de segurança
No item 20. Poderá ser feito ajuste de pressão dos selos da SSA para permitir a troca dali para cima.

### 3-SPS-111D — Troca de fluido, corte do cimento, fingerprint e DLOT
**Geronimo de Freitas Rolandi há um ano** | v1

Bom dia, na figura do item 18, utilizar 530 psi (valor a ser corrigido com DLOT) como limite, conforme está na sequencia. Excluir bullet com "Limite da janela operacional = 560 psi (100 psi abaixo da pressão estática para DLOT previsto de 10,70 ppg @ 3238 m com PF = 9,5 ppg);"

passo 38) DLOT, sugestão, montar uma tabela para compensar o empuxo na coluna conforme a pressão é aumentada.

### 3-SPS-113 — 23A Fingerprint MPD e MPD Drill_3SPS113
**Gustavo Costa Magalhaes Pena** | v6

De acordo, apesar de não ver sentido em fazer o simulado de DPPT (assinatura de descompressão do poço), já que esta operação não está prevista para ser realizada com o FPBNA 12,3 ppg.

### 3-SPS-113 — 23A Fingerprint MPD e MPD Drill_3SPS113
**Ramon Moreira Fernandes** | v3

Verificar ser está previsto realizar DPPT no reservatório (não encontrei essa informação no cronograma). Caso não esteja previsto DPPT, excluir etapa do simulado de DPPT.

> ↳ **Marcelo Goncalves Lira:** O DPPT não é firme, mas preferimos deixar no fingerprinting para termos a possibilidade de fazer quando constatarmos o reservatório. Temos o TesTrak no BHA, mas, em caso de falha, um DPPT pode ser útil.

### 3-SPS-113 — 23A Fingerprint MPD e MPD Drill_3SPS113
**Geronimo de Freitas Rolandi** | v1

Bom dia, ótima sequencia.

### 3-SPS-114 — 23.1 - Fingerprint MPD fase V (8 1/2")
**Ramon Moreira Fernandes** | v2

Estou de acordo com a sequência, porém não corresponde à sequência de "Fingerprint". Sugiro renomeá-la para "Descida do BHA 8 1/2" e teste d MPD".

### 4-RJS-764 — 10 Troca de fluido, fingerprint e choke drill
**Leonardo Mesquita Caetano** | v1

Caros, de acordo com a sequência.
Alguns comentários apenas para ficar na memória.

Preparativos.

3) Recomenda-se que a pressão de teste do buffer seja 3000 psi; caso contrário, ajustar as PRVs de acordo com a pressão do teste executado.

9) Ajustar conforme testes. Está tudo certo se a pressão de teste do buffer foi 3000 psi.

OBSERVAÇÕES DE MPD

1) Recomenda-se 3000 psi para buffer. 

Fingerprint

32) Definir os valores de vazão da operação

Item 37) geralmente vem antes do modelo hidráulico.

SIMULADO DE DFIT

39)  Sem booster

41) d) Registrar em tabela valores do PWD, SBP, volumes dos tanques e TT

54) iii Desligar bombas da coluna (manter booster)

### 4-RJS-764 — 10a Fingerprint offline - 4rjs764
**Leonardo Mesquita Caetano** | v1

OBSERVAÇÕES GERAIS

3) Tester do buffer com 3000 psi, como foi feito.

55) Usar como limite 100% do FIT

### 4-RJS-764 — 18 - troca de fluido, fingerprint e choke drill
**Gustavo Costa Magalhaes Pena** | v3

Suguem comentários:

Em troca de fluido:
 Item 20: Não é possível utilizar o sistema MPD para controlar o poço nesta etapa. Para controlar o influxo com o MPD, é necessário realizar Fingerprint para detecção e controle.
 Em fingerprint:
 Item 30: É importante alternar os barramentos da bombas alinhadas na coluna.
 Item 32: Neste momento não teremos um MH calibrado. Será ajustado o sistema MPD para que seja aplicado um ECD equivalente a 9,45 ppg (ou seja, AP na broca).
 Item 33: Não vejo necessidade de perfurar com 02 bombas na booster com camisa de 6". Prefiro deixar uma MP de backup como mencionei no item 30.
 Atentar que sempre que estabelecer vazão de 200 gpm na coluna (registro de eficiência, PID, perda de carga e MH), pode haver indexação do alargador. 
 Item 38 e 39: O ajuste do MH não é realizado desta forma. Estabelece parâmetros de perfuração e ajusta o MH. Faz-se uma simulação de conexão e verifica pelos dados de ESD se o MH está adequado. Repito esse processo até que o meu MH seja adequado para os cenários de perfuração e conexão.

Ficou faltando verificar o MH para testemunhagem. Lembrando do risco de indexação do alargador. Acredito que tenha sido "esquecido" de proposito. Para ser realizado com o BHA em poço aberto.
 Em MPD Drill, item 46: Além do alinhamento, recomendo que seja realizada uma reunião pré-tarefa para discutir o MPD com as equipes, além de lembrar da necessidade de preenchimento do Check list durante a execução do simulado.

### 4-RJS-764 — 18 - troca de fluido, fingerprint e choke drill
**Ivani Tavares de Oliveira** | v1

Em preparativos,
  - item 4: Atenção com a limitação de teste do Coriolis de 2000 psi.
 - item 6: adicionar nota: Confirmar válvulas de bloqueio das PRVs abertas e travadas com cadeado.

A troca de fluido será feita com os Packers Assy e BA instalados?
 Se SIM: incluir instalação e testes dos packers assy e BA (Lembrar que após a instalação e teste do packer assy, substiuir o fluido acima do packer assy antes de assentar o BA. É importante termos o fingrprint realizado para troca do fluido para poder utilizar o AP com modelo hidráulico calibrado.
 Se NÃO: retirar o subitem "a)" do item 20. Adicionar no item 26 a instalação e testes dos packers Assy e BA para poder circular e substituir o fluido do sistema MPD.

Em FINGERPRINT:
item 32, acrescentar: c) ajustar vazão pela coluna...
              d) se necessário, ajustar vazão de conexão na booster de acordo com a controlabilidade do choke, recomendado entre 300 e 400 gpm.

Itens 34, 35: incluir na tabela os valores de SBP decrescente, ou seja, SBP inicial = X+300 e SBP final = X+200; SBP inicial = X+200 e SBP final = X+100 e SBP inicial = X+100 e SBP final = Perfuração (X).

item 36. substituir no primeiro item da tabela a palavra Perfuração (Y) para Conexão (Y). Acrescentar a ordem decrescente: SBP inicial = X+200 e SBP final = X+100 e SBP inicial = X+100 e SBP final = Conexão (Y).

item 38, b): Faltou a letra "C" em: ...travamento do CMC...
e) Observar o comportamento do retorno do fluido nos tanques.

item 40. acrescentar: b) Avaliar condição ideal de compensação. O heave pode dar interferência nas leituras de flow out devido à coluna entrando e saindo do BA.
NOTA: Posicionar coluna de modo a não ter tool joint próximo ao selo do BA.
NOTA: Interromper atividades de movimentação de carga e não efetuar mudança de aproamento ou transferências entre tanques de lastro ou fluido e nem alterar alinhamentos no circuito de fluidos (degasser, centrífuga, sandtrap), durante o simulado.

item 41. a) Monitorar constantemente o Trip Tank para identificar possível vazamento do BA.

item 43. acrescentar no item c) Verificar a compressibilidade do fluido, que deve ser linear com a pressão.

item 65. a) Após preenchimento do formulário MPD drill e assinatura dos participantes, "scanear" e enviá-lo para a chave CSD MPD.

> ↳ **Adriano Henrique Silva Ferreira de Araujo:** O o BA e PA foram instalados na seqop anterior.

### 4-RJS-764 — 18A - Fingerprint offline
**Gustavo Costa Magalhaes Pena** | v1

Seguem comentários:

Em preparativos, item 1: Atenção com a limitação de teste do Coriolis de 2000 psi.

Em teste das PRVs e SPL:
Item 10: Aumentar SBP a partir do ajuste do choke em modo posição.
Item 11: Ao atingir a SBP de ativação do SPL o mesmo irá abrir até que a SBP caia 100 psi limitado a posição de 50% de abertura. Se ele não conseguir reduzir a SBP em 100 psi por 30 s na posição 50% ele vai para a abertura plena.

Em teste de alarme de perda e de influxo, 
Itens 41 e 48: Alinhar choke manifold da sonda para o BFM para permitir os testes.
Item 45: Muito cuidado no ato de fechar o choke hidráulico da sonda (velocidade) da sonda para permitir o adequado funcionamento do choke MPD (risco de sobrepressurização).

### 4-SPS-112 — Fingerprint e Treinamento Prático
**Gustavo Costa Magalhaes Pena há um ano** | v2

De acordo.

Item 10: Fluxograma do controle de poço com MPD saiu dobrado.

### 4-SPS-112 — Fingerprint e Treinamento Prático
**Gustavo Costa Magalhaes Pena há um ano** | v1

Seguem comentários:

Em Operações paralela:

Itens 2 a 7: Confirmar a vazão de manobra se 600 gpm ou 700 gpm. Por ser um choke de 3" entendo que 600 gpm será suficiente.

Item 8: Inserir etapa para verificação da perda de carga da linha de by-pass sistema de contrapressão no BFM (B14).

Item 10: Atualizar fluxograma de Controle de poço com MPD.

Em Operações no caminho crítico:

Item 15: Confirmar a necessidade de vazão tão alta e necessidade de 02 bombas na booster em todas conexões. Por ser um choke de 3" entendo que 350 ou 400 gpm na booster (somente uma MP) será suficiente. Caso seja decidido ajustar a vazão da booster no FP, corrigir itens: 16, 17 e 18 (na etapa do MH está com 350 gpm).

Item 16: 
#4 - Não vejo necessidade de realizar essa etapa no FP como registro de perda de carga. Fica mais interessante inserir no treinamento prático.

Item 17: 
#2 - MP1 + MP2 na booster para manobra.
#3 - Recomendo planejar a fase com uma MP spare (MP2), sendo assim, recomendo MP1 na booster e MP3 + MP4 na coluna.
#5 - MP1 + MP2 na booster e MP3 na coluna, com MP4 spare para a testemunhagem.
#6 - MP3 e MP4 na coluna para DPPT / DFIT.

Item 19: 
- Sobre critério de calibração de MH (conexão e testemunhagem), o padrão recomenda considerar somente ESDmédio ou ESDmoda como critério. Os valores de ESD máximo e mínimo são mais influenciados por PID, velocidade de entrada e saída de bomba, gel do fluido, heave, hold for standpipe, etc.
- Na tabela da testemunhagem mencionar a vazão da coluna de 200 gpm.

Item 20: Por se tratar de uma contingência não se faz necessária etapa dedicada no FP. Minha sugestão seria encaixar essa etapa no TP para pegar as informações mais importantes (variação VTT , ativo e assinatura) em uns 4 a 5 steps.

Em treinamento prático:
Tratar sobre DPPT e DFIT.
Incluir bate papo sobre as contingência de perfuração sem retorno PMCD e FMCD, alinhamentos, conversão e cuidados.
Incluir como monitorar condição do Junk Catcher e como proceder em caso de entupimento.

Em MPD drill:
a) Preencher formulário MPD drill durante execução e depois enviar para CSD MPD cadastrar no Checkpoint no SIP (em fase piloto).
b) Atualizar fluxograma de controle de poço com MPD.

### 7-BR-86DB-RJS — Fingerprinting do sistema MPD e MPD Drill
**Ramon Moreira Fernandes** | v3

Prezados

No projeto está previsto realizar DPPT após perfurar "5 m no horizonte de perda do BR-86DA", portanto faz-se necessário fazer um simulado de DPPT durante o fingerprint em poço revestido para registrar a curva de referência.

### 7-BR-86DB-RJS — Fingerprinting do sistema MPD e MPD Drill
**Fábio Koiti Dairiki** | v2

Prezados, de acordo

Caso haja outra revisão, mudar em informações gerais, item 4, bullet 4: de FMCD simplificado para FMCD.
Obs: Para FMCD simplificado seria usada a linha de by-pass do manifold MPD. Não passaríamos pelo choke de MPD.

### 7-BR-86DB-RJS — Fingerprinting do sistema MPD e MPD Drill
**Gustavo Costa Magalhaes Pena** | v1

Prezados, seguem comentários.

Em informações gerais, item 4:
Sobre as operações MCD:
PMCD convencional: LAM no anular. Nível na superfície. Choke MPD fechado com SBP. Anular parado. Monitoramento de pressões, e recalques preventivos e reativos. Pressão de poros maior que peso de fluido (LAM). LAM maior que 8,7 ppg.
FMCD: SAC no anular. Nível no riser. Choke MPD aberto sem SBP. Anular continuamente na vazão de controle. Monitoramento de pressões, e recalques reativos. Pressão de poros menor que 8,5 ppg.
PMCD dinâmico: LAM = SAC no anular. Nível na superfície. Choke MPD fechado com SBP. Anular continuamente na vazão de controle. Monitoramento de pressões, e recalques reativos. Pressão de poros entre 8,4 e 8,7 ppg.

Em preparativos para atividades paralelas, item 1: BFM é testado com 300/3000 psi. Cuidado com Coriolis (limite 2000 psi). 

Em perdas de carga, item 17:
c) Não precisa fazer em todas intervenções. Tem mais o efeito de treinamento das equipes.
Tabela: Fazer itens 1, 2, 3 e 5.

Em MPD Drill:
Planejar na seguinte ordem: Fingerprint, PRC, MPD Drill, Sim. Hang-off e Choke Drill.
Item 24: Mantendo AP 9,9 ppg na broca.
Fluxogramas: Manter somente o completo, sem necessidade de manter os outros (parciais) das páginas 12 e 13.

### 7-BR-86DB-RJS — Troca de fluido, choke drill e corte do cimento
**Ivani Tavares de Oliveira** | v1

Em OBSERVAÇÕES PARA OPERAÇÃO COM MPD (FINGERPRINT):
 item 3 - adicionar b) Em caso de substituição do BA, é necessário testá-lo pela metodologia Hold Point com aprovação do CSD-MPD.

Em FINGERPRINT E TREINAMENTO PRÁTICO MPD:
Inicia na numeração 23? Se necessário corrigir a numeração. Acredito que este item se refira apenas ao Fingerprint.
Treinamento prático do sistema MPD ocorreu na intervenção anterior. Verificar os nomes dos participantes. É obrigatório pelo menos 1 da equipe da sonda treinado (Toolpusher/sondador/Assist. sondador) por turno:
                     Turma A e E: 10/08/2025
                     Turma C e D: 23/09/2025
Verificar se a sequência 04a que será anexada, descrita no item 23, consta o MPD Drill, caso contrário adicionar o MPD Drill antes do item 24).

Em CORTE DO CIMENTO – PERFURAÇÃO DE SACO P/ SIDETRACK:
item 36 bullet #5) Após peneiras limpas, alinhamento para o sistema MPD no BM. Retirar a palavra "by-pass".
item 37 flowcheck estático, precisa circular com a bomba do TT, conforme figura do item 5.

> ↳ **Cesar Ferreira dos Reis:** Obg, ajustado na vs2.

### 7-BUZ-100D-RJS — Fingerprint do sistema MPD, MPD drill e choke drill
**Gustavo Costa Magalhaes Pena** | v2

De acordo.


Somente 02 pontos de atenção: 

No item 23, em caso de insucesso com 1 bpm, repetir com 3 bpm.

No item 33, o monitoramento do riser pode ocorrer de 02 formas:
Suspeita de gás de riser: Riser pressurizado e com circulação pela booster.
Sem suspeita de gás de riser: Riser despressurizado com trip tank alinhado.

Para efeito de simulado, considerar sem suspeita de gás de riser: abrir o choke MPD, desligar a booster e alinhar o trip tank para o riser através do BFM.

### 7-BUZ-100D-RJS — Fingerprint do sistema MPD, MPD drill e choke drill
**Gustavo Costa Magalhaes Pena** | v1

Seguem comentários:

Em dados do poço, no momento do Fingerprint no caminho crítico o fluido será FPBA 8,7 ppg.

Sobre as PRVs #2 e #4: Apesar de não ter sido gerada GM/FAM, entendo ser importante que as recomendações operacionais da MOC, elaborada pela Seadrill e aprovada pela Petrobras, sejam mencionadas na SeqOp: 
Manter PRV3 alinhada e substituindo PRV2, sempre que possível. Desta forma teremos 02 PRVs alinhadas durantes as operações de perfuração e manobra.
Quando a UC for alinhada para acessar o BFM, garantir que exista PRV alinhada e ajustada para proteção do sistema de superfície. Cuidado especial com o set da pop-off da UC.

Em fingerprint offline, no item 4: Avaliar condição de atuação as PRVs com alta pressão, alta vazão e pequeno volume (1000 psi e 900 gpm, em circuito de superfície + linhas submarinas). Caso necessário, o teste funcional pode ser realizado com parâmetros mais brandos (pressão e vazão) para evitar estresse do equipamento.

Em fingerprint no caminho crítico:

Considero importante um alerta para a SLB a respeito do contexto desse FP. Trata-se de um FP simplificado, pois estaremos com fluido estaticamente OB, com o sistema MPD mantendo a pressão constante na sapata (provavelmente perfuração com choke aberto e controle de pressão nas conexões), com a contingência de conversão para MCD (FMCD ou PMCD Dinâmico).  

No item 10: É mencionada a necessidade de manter no mínimo 9,04 ppg na sapata, porém estamos com FPBA 8,7 ppg e a PP P90 é 8,57 ppg. Portanto, recomendo retirar esse alerta. Podendo o sistema MPD ser completamente despressurizado e mesmo assim mantendo a condição OB.

Em MPD Drill:

Retirar menção à necessidade de manter 9,04 ppg.
Atualizar etapas conforme esboço de padrão de MPD Drill. A ser enviado para a fiscalização.
Para o contexto do NS48, considerando a degradação das PRVs, recomendo que seja realizada a modalidade de volume excedido.
Atualizar formulário de MPD Drill.
Atualizar fluxograma de controle de poço com MPD.

### 7-BUZ-90D-RJS — Corte de cimento, troca de fluido, fingerprint e DLOT
**Ramon Moreira Fernandes há um ano** | v1

Passo 21: O DLOT poderá ser conduzido até máxima pressão de 1500 psi (limite superior do envelope operacional do BAxRCD). Portanto o máximo EMW esperado no DLOT será de ~14,0 ppg (a confirmar durante o fingerprint na etapa do simulado de DLOT). Caso não se atinja absorção com EMW de 14,0 ppg avaliar se será suficiente se limitar ao DFIT ou se será necessário conduzir um LOT convencional (sem MPD).

> ↳ **Diogo de Barros Correia há um ano:** Conforme definido na reunião de GEP caso não atinja a absorção e seja atingido o limite de 1500 psi na superfície podemos prosseguir a operação com DFIT desde que atinja os critério dos valores mínimos para prosseguir sem GM.

### 7-BUZ-90D-RJS — Corte de cimento, troca de fluido, fingerprint e DLOT
**Geronimo de Freitas Rolandi há um ano** | v1

Prezados, bom dia,

Durante a execução do DLOT, tomar a mesma precaução do LOT e compensar a força ascendente na coluna drenando pressão do compensador enquanto pressuriza o poço:

Em considerações Adicionais de Segurança Operacional
Casos de influxo que requerem fechamento do BOP:
Colar a figura já utilizada no passo 14:

### 7-BUZ-90D-RJS — Fingerprint do sistema MPD e MPD drill
**Gustavo Costa Magalhaes Pena há um ano** | v2

De acordo.

Só um ajuste para o caso de nova revisão: No item 4, calibração do MH, a vazão da booster ficou com 500 gpm.

### 7-BUZ-90D-RJS — Fingerprint do sistema MPD e MPD drill
**Gustavo Costa Magalhaes Pena há um ano** | v1

Inserir alerta de que a pressão de poros P90 é de 9,1 ppg e estamos utilizando FPBA 8,7 ppg, portanto durante as etapas de FP, MPD Drill e Choke Drill o sistema MPD deverá manter um EMW mínimo de 9,2 ppg na sapata. 

O diagrama apresentado na página 3 está com alinhamento de teste e não de FP. Sugiro pegar o diagrama utilizada na seqop do BUZ85.

Item 1 - Em calibração do PID: Não vejo necessidade de usar 500 gpm na booster nas conexões. É possível fazer as conexões mantendo os 400 gpm já que o choke da SLB é de 3". Corrigir o restante da SeqOp para 400 gpm.

Item 1 - Em comportamento de retorno do fluido dos tanques na conexão: Não é necessário dedicar tempo no FP para essa etapa que poderá ser verificada em paralelo às conexões.

Item 2 - Calibração de eficiência: 
Na perfuração 02 bombas na coluna e 01 na booster.
Na conexão 01 bomba na booster a 400 gpm.

No BUZ85 foi utilizada a MP2/MP3 na coluna, MP1 na booster e MP4 back-up.

Item 3 - Perdas de carga:
Os itens importantes são os de perfuração e conexão (400 gpm) que podem ser registrados durante a eficiência das bombas. Indisponibilidade de mangueira e circulação pelo MGS são contingências e já temos registros de outros intervenções que podemos utilizar como referência, se necessário.

Item 5 - Arraste do DP/TJ pelas borrachas do BA: Essa etapa só é realizada no caminho crítico quando em treinamento prático. No NS48 os sondadores já conhecem o arraste e podem conferir a qualquer momento, se acharem necessário.

Tomada de PRC: Corrigir número sequencial do item. Esta etapa faz parte do MPD Drill e não do Fingerprint. Trata-se da preparação para o simulado.

Item 6 - MPD Drill: Estamos em fase piloto de inserir o MPD Drill como check point no SIP. Sendo assim, iremos enviar para a fiscalização um formulário que deverá ser utilizado/preenchido durante o MPD Drill, e depois enviado para o CSD MPD como evidência.

### 7-BUZ-90D-RJS — Fingerprint online do sistema MPD
**Ramon Moreira Fernandes há um ano** | v4

De acordo com a seqop. Única alteração foi a otimização do simulado de DLOT, reduzindo o número de steps de pressurização.

### 7-BUZ-90D-RJS — Fingerprint online do sistema MPD
**Geronimo de Freitas Rolandi há um ano** | v1

Prezados, boa noite:
O fingerprint offline já foi feito, porém o valor do BIAS é 50 psi (um delta em relação ao setpoint)
De acordo com o PERF, utilizar a vazão máxima de 680 gpm. eventuais ajustes de eficiência podem ser feitos após abertura do alargador duarnte a perfuração.

### 7-BUZ-95-RJS — Corte de cimento, troca de fluido, fingerprint, MPD drill e 
**Geronimo de Freitas Rolandi** | v3

No Item 17, colocar:  Alerta: Caso o teste de influxo anterior tenha falhado, não submeter o poço intencionalmente à condição de underbalance. Isso inclui não efetuar desligamento de bombas e não realizar simulado de DPPT.

### 7-BUZ-95-RJS — Corte de cimento, troca de fluido, fingerprint, MPD drill e 
**Ramon Moreira Fernandes** | v2

Verificar com CGEP a possibilidade de efetuar um teste de influxo método 4 ao final da troca de fluido para permitir uma melhor calibração do modelo hidráulico durante o fingerprint MPD. Caso contrário é necessário acrescentar uma observação na etapa de fingerprint que durante todo o fingerprint é necessário manter o poço overbalance com peso equivalente de no mínimo 9,1 ppg na sapata.

### 7-BUZ-95-RJS — Corte de cimento, troca de fluido, fingerprint, MPD drill e 
**Ramon Moreira Fernandes** | v2

Passo 14: Alinhar para by-passar o sistema MPD no buffer manifold.  -> by-passar coriolis.

Passo 15: Manter alinhamento by-pass do sistema MPD no buffer manifold.  -> by-passar coriolis enquanto estiver retornando cimento nas peneiras.

### 7-BUZ-95-RJS — Corte de cimento, troca de fluido, fingerprint, MPD drill e 
**Geronimo de Freitas Rolandi** | v1

Prezados, boa tarde,

Passo 4 do fingerprint offline, primeiro bullet:
• Interligar circuito ao choke manifold, mantendo as válvulas submarinas das linhas de kill e choke e as válvulas externas da Junta Integrada fechadas e as válvulas abertas na superfície (maximizando volume da câmara de teste para melhor verificação do rearme das PRVs).

Passo 17 Fingeprint, Esse procedimento aparentemente é da Halliburton, confirmar com equipe a bordo procedimento SLB,

Passo 24. MPD Drill
Preencher checklist MPD Drill durante a execução e recolher assinaturas, entrar em contato com CSD MPD para obter uma cópia do documento.

### 7-JUB-78D-ESS — Fingerprint do sistema MPD
**Ramon Moreira Fernandes** | v2

Colocar etapa do MPD Drill nesta sequência ou na sequência da perfuração

> ↳ **Eduardo Duarte Nascimento:** Boa tarde. Treinamento está incluído, na SO do treinamento prático.

### 7-JUB-78D-ESS — Fingerprint do sistema MPD
**Ramon Moreira Fernandes** | v2

Prezados

Geralmente não temos feito o passo 18 do fingerprint (comportamento do fluxo de retorno com bombas desligadas) pois as sondas já possuem experiência suficiente no comportamento transiente dos volumes dos tanques. Caso julguem necessário fazer essa etapa, a tabela correta para registro dos resultados encontra-se no padrão de fingerprint e transcrevo abaixo:

### 7-MRO-37-RJS — Fingerprint MPD da fase de 8 1/2"
**Leonardo Mesquita Caetano há um ano** | v1

Caros, de acordo.

Solicito apenas que mude a vazão de "influxo" simulado do MPD drill para 5 bpm, para simularmos e avaliarmos uma possível falha do software da Halliburton.

Adicionalmente, estamos num piloto de implementar um check point do MPD drill. Dessa forma, solicito que anexe Nesse documento o check list relacionado.

Check List - MPD drill.pdf
Versão word: MODELO_NS48_7BUZ93D_Check List MPD Drill_25-12-2024.docx

> ↳ **Leonardo Mesquita Caetano há um ano:** Aproveitando, excluir itens de dppt, já que não estão está previsto (em eficiência de bomba e perda de carga de linhas de superfície)

### 8-ATP-8D-RJS — Corte de cimento, troca de fluido, fingerprint do MPD e trei
**Gustavo Costa Magalhaes Pena há um ano** | v2

De acordo. 

Somente atentar que do item 11 até o item 25 não há necessidade de manter o Choke MPD alinhado já que não teremos necessidade de gestão de pressão. Por isso a recomendação de by-passar o sistema MPD todo no BFM e não somente o coriolis.

### 8-ATP-8D-RJS — Corte de cimento, troca de fluido, fingerprint do MPD e trei
**Gustavo Costa Magalhaes Pena há um ano** | v1

Comentários sobre os Anexos:

Importante que as PRVs do sistema MPD estejam sempre alinhadas e setadas adequadamente para proteção das linhas de superfície. Após os testes funcionais, atentar para retornar com o set.

Caminho crítico:

Calibração do controlador PID: A simulação da Hall de projeto foi realizada com perfuração 600+400 gpm e conexão com 0 + 400 gpm.

Perdas de carga do sistema de superfície:
a) Os alinhamentos utilizando a linha de PMCD: Fazer na etapa do fingerprint paralelo. Faltou o item 12 com 1200 gpm by-passando JC E MPD.
b) Faltaram os alinhamentos com retorno do poço pelas mangueiras de 6" nas vazões de perfuração e conexão.

Perdas de carga 

Calibração de eficiência de bombas: Na configuração prevista diz que a booster será a MP1, mas na tabela está MP2.
1) Booster (1 MP) de conexão.
2) Coluna (2 MP) e booster (1 MP) de perfuração.
3) Booster de manobra (2 MP).

Comportamento do fluxo de retorno com bombas ligadas e desligadas: Etapa faz parte do escopo do treinamento prático das equipes.

PRC com MPD: Etapa faz parte do escopo do treinamento prático das equipes. 

Altura do bloco com TJ no BA: Etapa faz parte do escopo do treinamento prático das equipes. 

Simulados DFIT e DPPT: Etapa faz parte do escopo do treinamento prático das equipes. 

Restante das etapas do treinamento prático: No anexo 3 são mencionados diversas etapas do treinamento prático que ainda não foram detalhadas nesta sequencia/anexos. Pendente incluir também o MPD Drill. Atentar para a necessidade de preencher formulário especifico para registro de checkpoint no SIP.


Em paralelo:

PID de superfície: Geralmente utilizamos vazão de 600 gpm. Confirmar se será necessário 800 gpm.

Ativação de PRV: Mencionar o setting das PRVs e SPL antes, durante e depois da etapa.

### 8-ATP-8D-RJS — Corte de cimento, troca de fluido, fingerprint do MPD e trei
**Gustavo Costa Magalhaes Pena há um ano** | v1

Comentários sobre a SeqOp:

Item 4, 11º bullet: Durante o corte de cimento by-passar todo o sistema MPD e não somente o coriolis, conforme ilustrado na figura 2.

Item 6, 4º bullet: Procurar fazer as etapas do FP paralelo durante a montagem e descida do BHA. No momento da troca de fluido, as equipes da sonda e os equipamentos estarão dedicados na operação principal.

Item 9: Conferir se não há excesso de retorno de cimento e alinhar sistema MPD: JC, Coriolis e Choke MPD.

Item 10: Recomendo que as etapas de treinamento prático e fingerprint fiquem num documento dedicado para revisão (mesmo que com o nome de anexo).

Item 11: Novamente by-passar todo sistema MPD no BFM.

Item 24: Antes de retomar a perfuração, conferir se não há excesso de retorno de cimento e alinhar sistema MPD: JC, Coriolis e Choke MPD.

### 8-ATP-8D-RJS — S09ANEXO - Fingerprinting e treinamento prático de MPD
**Ivani Tavares de Oliveira há um ano** | v2

Sugiro incluir antes da figura:
INFORMAÇÕES GERAIS / LEMBRETES: 
DURANTE TODAS AS ETAPAS, SEMPRE VERIFICAR O SETTING DE PRESSÃO DAS PRVS PARA PRESERVAR A INTEGRIDADE DOS EQUIPAMENTOS E DO POÇO.

SETUP Inicial das PRVs: 
PRV1 (Linha 6”) em 1700 psi - rearme 750 psi;
PRV2 (Linha 6”) em 1700 psi - rearme 750 psi.
PRV3 (Linha 2”) em 1700 psi - rearme 750 psi. o PRV4 (Choke Manifold) em 2400 psi - rearme 1900 psi;
PRV5 (PMCD) em 2400 psi - rearme 1900 psi;
SPL em 1500 psi (obs: na perfuração esse valor provavelmente será reduzido pelos parâmetros operacionais).

 PREPARATIVOS:
Sincronizar horário dos sistemas da envolvidos na operação (sonda, MPD, Mudlogging e LWD) para que estejam no mesmo horário.
Confirmar comunicação com demais sistemas via WITS e transmissão dos dados para RTO live.
Confirmar Buffer manifold testado com 300 / 3000 psi. Todos com indicação correta de posição.
Confirmar equipamentos testados com pressão (conforme abaixo) e funcionais. Todos com indicação correta de posição.
(1) Teste do Coriolis com 2000 psi.
(2) Teste das mangueiras com 2000 psi.
(3) Teste do riser com 1900 psi.
(4) Teste das NRVs com 2000 psi

Critério de aceitação:
 ➢ Baixa pressão: queda máxima 10 psi / 5 min (PINICIAL ≤ 350 psi).
No teste de baixa, se a pressão ficar entre 350 psi e 500 psi na pressurização, drenar até < 350 psi. Se ultrapassar 500 psi, drenar até zero e reiniciar.
 ➢ Alta pressão: queda máxima 40 psi / 5 min (PFINAL ≥ PNOMINAL TESTE)

### 8-ATP-8D-RJS — S09ANEXO - Fingerprinting e treinamento prático de MPD
**Geronimo de Freitas Rolandi há um ano** | v1

Boa note, além das observações do Leandro, proceder com alterações do item 32 conforme arquivo enviado pelo Teams

### 8-BUZ-89D-RJS — Corte de cimento, troca de fluido, fingerprint, MPD Drill e 
**Geronimo de Freitas Rolandi** | v1

item 10c. Atenção para efetuar primeiro flush das mangueiras de MPD 6" e 2" para ambiente controlado (possibilidade de ocorrer H2S por fluido muito tempo parado).

### 8-BUZ-96D-RJS — Corte de cimento, troca de fluido, fingerprint, MPD Drill e 
**Gustavo Costa Magalhaes Pena** | v2

De acordo.

Em caso de nova revisão, no item 27: Retirar o tachado da parte que menciona que o operador MPD deve pausar o controle automático e notificar sondador.

### 8-BUZ-96D-RJS — Corte de cimento, troca de fluido, fingerprint, MPD Drill e 
**Gustavo Costa Magalhaes Pena** | v1

Seguem comentários:

Em dados básicos:
Margem de segurança de riser: Está sendo considerada a PP do COA. Se usar a PP do topo do reservatório de 8,55 ppg, devemos passar para outra condição.
CSB após o corte do shoetrak: O FPBA 8,7 ppg é considerado OB na sequencia vigente, sem necessidade do MPD para compor CSB.

Em segurança, 1º bullet: O trip tank vai estar monitorando a estanqueidade do BA. Para monitorar o poço é necessário realizar alinhamento específico no BFM.

Item 6: Confirmar se a vazão de manobra será 700 ou 600 gpm. No item  20 a vazão de manobra esta 600 gpm.

Item 16, 1º bullet: Assim que o primeiro BU for concluído, já é possível alinhar o JC, by-pass coriolis e Choke MPD. Desta forma a equipe MPD já pode iniciar algumas etapas em paralelo à homogeneização.

Item 20: Considerando que sempre acabamos tendo uma bomba de lama em reparo, sugiro incluir a verificação de eficiência com somente uma bomba na booster (MP2 ou MP3).

Item 24: Etapa pode ser suprimida já que a sonda já esta acostumada com operações MPD.

Em MPD Drill: Estou trabalhando num padrão para o MPD Drill que está bem avançado. Vou compartilhar com vocês para ajustarmos a SeqOp.

### 8-MRO-36-RJS — Anexo - Fingerprint e treinamento prático
**Ramon Moreira Fernandes** | v2

Passo 11: o fluxograma está desatualizado. Considerar o seguinte fluxograma:

Passo 37/c: ficou com referência "NS-62". Corrigir para NS-59.

### 8-MRO-36-RJS — Anexo - Fingerprint e treinamento prático
**Ramon Moreira Fernandes** | v1

Enviei uma versão revisada pelo teams.
