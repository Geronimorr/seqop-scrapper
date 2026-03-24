# Anexo D - Ajuste dos mecanismos contra sobrepressurização.xlsx

## Aba: Tabela

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Sistema de contrapressão da Halliburton |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  | Dispositivos de segurança | Mecanismo | Proteção | Pressão de teste | Set Abertura | Set Fechamento | Observações |
|  | PRVs Choke Manifold / Standpipe Manifold para BFM | PRV eletrônica com set de fixo de abertura e fechamento. | Linhas de superfície. | 3000 psi | 2400 psi | 1900 psi | N/A |
|  | PRVs Mangueiras de Fluxo / BFM | PRV eletrônica com set fixo de abertura e fechamento. | Linhas de superfície. | 1900 psi | 1700 psi | Maior entre: a) 750 psi; b) SBP de shut-in (PP) + 50 psi. | N/A |
|  | SPL (Secondary Pressure Limiter) | Funciona como uma PRV eletrônica só que com 02 estágios (posição de abertura do choke SPL). Os estágios são fixos e configurados no software. | O que for mais restrito entre linhas de superfície e poço. | N/A | Menor entre: a) 1400 psi; b) SBP de perfuração (FIT) - 100 psi. | SBP = SBP setpoint - 100 psi. | Exemplo: 1º Estágio: Choke SPL vai a 50% de abertura e permance nessa posição por 30s. 2º Estágio: Choke SPL vai a 100% de abertura e permance nessa posição. Em qualquer momento que a SBP voltar a ficar abaixo do set de abertura o choke SPL se fecha. |
|  | MAX SBP (Max Surface Back Pressure) | Limitador de SBP setpoint calculado pelo modelo hidráulico que não considera as condições dinâmicas do poço (limitador fixo). | O que for mais restrito entre linhas de superfície e poço. | N/A | 50 psi abaixo do set de abertura do SPL. | N/A | Não limita SBP setpoint imputada manualmente pelo operador. |
|  | ASP (Allowable Surface Pressure) | Limitador de SBP setpoint calculado pelo modelo hidráulico, baseado no limite superior da janela operacional (FIT/LOT), que considera as condições dinâmicas do poço (limitador variável). | O que for mais restrito entre linhas de superfície e poço. | N/A | Limitador varíavel baseado no limite superior da janela operacional (FIT/LOT). | N/A | Não limita SBP setpoint imputada manualmente pelo operador. |
|  |  |  |  |  |  |  |  |
|  | Cenários possíveis: |  |  |  |  |  |  |
|  | a) Cenário de plugueamento do Choke: Será ativado o SPL. Os outros dispositivos não irão ter reação para esse cenário. b) Cenário de MH determinar um SBP setpoint alto: Será limitado pelo MAX SBP. É importante que esse valor seja inferior ao SPL para evitar seu acionamento. c) Cenário de MH determinar um SBP setpoint alto em Well Control (ActEv): Será limitado pelo MAX SBP. Em cenário de perfuração a MS será de 150 psi para o FIT. Avaliar aumentar os limites de SPL e MAX SBP caso seja decidido transferir o controle do poço para a sonda para permitir aumentar a SBP na saída de bomba da coluna. |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  | Sistema de contrapressão da SLB |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  | Dispositivos de segurança | Mecanismo | Proteção | Pressão de teste | Set Abertura | Set Fechamento | Observações |
|  | PRVs Choke Manifold / Standpipe Manifold para BFM | PRV eletrônica com set de fixo de abertura e fechamento. | Linhas de superfície. | 3000 psi | 2400 psi | 1900 psi | N/A |
|  | PRVs Mangueiras de Fluxo / BFM | PRV eletrônica com set fixo de abertura e fechamento. | Linhas de superfície. | 1900 psi | 1700 psi | Maior entre: a) 750 psi; b) SBP de shut-in (PP) + 50 psi. | N/A |
|  | BIAS | BIAS é a tolerância máxima de desvio superior da SBP medida em relação à SBP setpoint. Quando esse limite é atingido o choke backup é aberto controladamente. Usualmente usa-se BIAS entre 50 e 100 psi. | Poço. | N/A | SBP > SBP setpoint + BIAS | SBP < SBP setpoint + BIAS | Mitiga eventos de sobrepressurização do poço no caso de entupimento do choke. |
|  | MAX SP (Max Surface Pressure) | Limitador de SBP que não considera as condições dinâmicas do poço (limitador fixo). Juntamente com o BIAS, não permitirá que a SBP ultrapasse esse limite. | O que for mais restrito entre linhas de superfície e poço. | N/A | Menor entre: a) 1400 psi; b) SBP de perfuração (FIT) - 100 psi. | N/A | Limita SBP setpoint tanto pelo modelo hidráulico quanto pelo input manual do operador. |
|  | DMAASP (Dynamic Max Allowable Annular Surface Pressure) | Limitador de SBP setpoint calculado pelo modelo hidráulico quando em modo Well Control (EKD-AIR), baseado no limite superior da janela operacional (FIT/LOT), que considera as condições dinâmicas do poço (limitador variável). | O que for mais restrito entre linhas de superfície e poço. | N/A | Limitador varíavel baseado no limite superior da janela operacional (FIT/LOT). | N/A | Somente ativo quando em modo Well control (EKD-AIR). Quando ativado inibe o limitador fixo do MAX SP. |
|  |  |  |  |  |  |  |  |
|  | Cenários possíveis: |  |  |  |  |  |  |
|  | a) Cenário de plugueamento do Choke: Será ativado o BIAS. b) Cenário de MH determinar um SBP setpoint alto: Será limitado pelo MAX SP. c) Cenário de MH determinar um SBP setpoint alto em Well Control (EKD-AIR): Será limitado pelo DMAASP e o MAX SP será inibido permitindo que o sistema utilize toda a margem de SBP na saída de bomba da coluna. |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  | Sistema de contrapressão da Weatherford |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  | Dispositivos de segurança | Mecanismo | Proteção | Pressão de teste | Set Abertura | Set Fechamento | Observações |
|  | PRVs Choke Manifold / Standpipe Manifold para BFM | PRV eletrônica com set de fixo de abertura e fechamento. | Linhas de superfície. | 3000 psi | 2400 psi | 1900 psi | N/A |
|  | PRVs Mangueiras de Fluxo / BFM | PRV eletrônica com set fixo de abertura e fechamento. | O que for mais restrito entre linhas de superfície e poço. | 1900 psi | Menor entre: a) 1400 psi; b) SBP de perfuração (FIT) - 100 psi. | Maior entre: a) 750 psi; b) SBP de shut-in (PP) + 50 psi. | Deve ser setado para proteção primária, pois possui capacidade de fechar automaticamente mantendo alguma pressão no poço. |
|  | High Limit | Funciona como uma PRV eletrônica de estágio único levando os chokes MPD para a posição de 100% aberto, sem mecanismo automático de fechamento. | Linhas de superfície. | N/A | 1700 psi | N/A | Deve ser setado para proteção secundária, pois precisa de intervenção do operador para ser fechada e reestabelecer a condição de poço pressurizado. |
|  |  |  |  |  |  |  |  |
|  | Cenários possíveis: |  |  |  |  |  |  |
|  | a) Cenário de plugueamento do Choke: Serão ativadas as PRVs das mangueiras de fluxo. b) Cenário de MH determinar um SBP setpoint alto: Será limitado pelo MAX SP. c) Cenário de MH determinar um SBP setpoint alto em Well Control (EKD-AIR): Será limitado pelo DMAASP e o MAX SP será inibido permitindo que o sistema utilize toda a margem de SBP na saída de bomba da coluna. |  |  |  |  |  |  |

## Aba: Padrão

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |
|  | 1) Qual o tipo de intervenção? |  | 2) Se FMCD Simplificado: |  | 3) Se modo SBP: |  | 4) Se Halliburton, necessário ajustar os dispositivos: OPÇÃO A |  | 5) Se SLB, necessário ajustar os dispositivos: |  | 6) Se Weatherford, necessário ajustar os dispositivos: |
|  | a) Fase iniciada em modo SBP. |  | a) Testar Junta integrada no Moonpool. |  | a) Testar Junta integrada no Moonpool. |  | a) SPL. |  | a) BIAS. |  | a) High Limit. |
|  | b) Fase iniciada em FMCD Simplificado. |  | Testar com 300/2000 psi. |  | Testar com 300/2000 psi. |  | Abertura: Menor entre 1500 psi e SBP de perfuração (FIT) - 100 psi. |  | 50 a 100 psi. |  | Abrir com 1700 psi e fechar com 750 psi ou OB (shutin). |
|  |  |  | Mantém critério original de teste. |  | Teste normal. |  | Dispositivo funciona como uma PRV em 02 estágios. Deve proteger o que for mais restrito entre poço ou equipamentos de superfície. |  | Dispositivo que pilota o choke backup para manter a SBP abaixo do SBP setpoint + BIAS. |  | Funciona como uma PRV eletrônica de estágio único levando os chokes MPD para a posição de 100% aberto, sem mecanismo automático de fechamento. |
|  |  |  | b) Testar BFM. |  | b) Testar BFM. |  | b) MAX SBP MH. |  | b) MAX SP. |  | b) PRVs das mangueiras para BFM |
|  |  |  | Testar com 300 psi. |  | Testar com 300/3000 psi. |  | Setar 50 psi abaixo do set de abertura do SPL. |  | Menor entre 1500 psi e SBP de perfuração (FIT) - 100 psi. |  | Menor entre 1500 psi e SBP de perfuração (FIT) - 100 psi. |
|  |  |  | Somente teste de baixa. |  | Atenção com equipamentos limitados a 2000 psi. Após os testes retornar as PRVs para proteção dos equipamentos de superfície. Aproveitar para verificar calibração dos sensores. |  | Dispositivo funciona como um filtro estático de Setpoint de SBP orinundo do MH. Em qualquer momento que o MH sugerir um setpoint maior que o filtro, a sugestão será ignorada pelo software. Ativo somente em modo MH. |  | Dispositivo funciona como um limite estático da SBP. Independente se oriundo do MH ou inputado pelo operador. Juntamente com o BIAS, não permitirá que a SBP ultrapasse esse limite. |  | Quando operando com sistema Wetherford deve proteger o que for mais restrito entre poço ou equipamentos de superfície. |
|  |  |  | c) Ajustar PRVs. |  | c) Testar sistema de contrapressão. |  | c) ASP MH. |  | c) DMAASP. |  |  |
|  |  |  | Ajustar para 200 psi. Efetuar teste funcional e conferir calibração dos sensores. |  | Testar com 300/2000 psi. |  | Inserir o resultado do FIT no Software. |  | Inserir o resultado do FIT no Software. |  |  |
|  |  |  | 100 psi abaixo da pressão de teste. Evitar submeter os equipamentos à pressão de teste. |  | Necessário acompanhamento do operador. |  | Dispositivo limita a máxima SBP considerando os dados de FIT/LOT e as condições dinâmicas do poço. Ou seja, trata-se de um limite dinâmico que varia conforme as perdas de carga do momento. Ativo somente em modo MH. |  | Dispositivo limita a máxima SBP considerando os dados de FIT/LOT e as condições dinâmicas do poço. Ou seja, trata-se de um limite dinâmico que varia conforme as perdas de carga do momento. Ativo somente em modo Well Control (EKD-AIR). Quando ativado inibe o limite do MAX SP. |  |  |
|  |  |  | d) Testar NRVs (HP - Sim) |  | d) Ajustar PRVs. |  |  |  |  |  |  |
|  |  |  | Testar com 2000 psi. |  | PRVs CM e SPP para BFM: Abrir com 2400 psi e fechar com 1900 psi. PRVs das mangueiras para BFM: Abrir com 1700 psi e fechar com 750 psi ou OB (shutin). |  |  |  |  |  |  |
|  |  |  | Mantém critério original de teste. |  | Devem proteger os equipamentos de superfície. |  |  |  |  |  |  |
|  |  |  | e) Se converter FMCD, testar BA/SSA (HP - Não) |  | e) Testar NRVs HP. |  |  |  |  |  |  |
|  |  |  | Testar com 300 psi. |  | Teste de alta: Maior entre 2500 psi e (PPmax - 8,55) x 0,1704 x Prof_final. |  |  |  |  |  |  |
|  |  |  | Teste de operação, somente para verificar se BA está instalado corretamente e estanque. |  | Pressão de teste deve considerar contingência PMCD, se for o caso. |  |  |  |  |  |  |
|  |  |  |  |  | f) Testar sistema MPD HP. |  |  |  |  |  |  |
|  |  |  |  |  | Testar com 300/1900 psi. |  |  |  |  |  |  |
|  |  |  |  |  | Teste normal. |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  | 4) Se Halliburton, necessário ajustar os dispositivos: OPÇÃO B |  |  |  |  |
|  |  |  |  |  |  |  | a) SPL. |  |  |  |  |
|  |  |  |  |  |  |  | Abertura: Menor entre 1500 psi e SBP de perfuração (FITaj) - 100 psi. Fechamento: Maior entre 750 psi e SBP de shut-in (PP) + 50 psi. |  |  |  |  |
|  |  |  |  |  |  |  | Dispositivo funciona como uma PRV em 02 estágios. Deve proteger o que for mais restrito entre poço ou equipamentos de superfície. |  |  |  |  |
|  |  |  |  |  |  |  | b) MAX SBP MH. |  |  |  |  |
|  |  |  |  |  |  |  | Setado em 1600 psi (100 psi abaixo do Set das PRVs). |  |  |  |  |
|  |  |  |  |  |  |  | Dispositivo funciona como um filtro estático de Setpoint de SBP orinundo do MH. Em qualquer momento que o MH sugerir um setpoint maior que o filtro, a sugestão será ignorada pelo software. Ativo somente em modo MH. |  |  |  |  |
|  |  |  |  |  |  |  | c) ASP MH. |  |  |  |  |
|  |  |  |  |  |  |  | Inserir o resultado do FITaj no Software. Sendo FITaj = 97% do FIT ou 95% do LOT. SBP de perfuração (FITaj) deve ser pelo menos 50 psi abaixo da SBP de perfuração (FIT). |  |  |  |  |
|  |  |  |  |  |  |  | Dispositivo limita a máxima SBP considerando os dados de FIT/LOT e as condições dinâmicas do poço. Ou seja, trata-se de um limite dinâmico que varia conforme as perdas de carga do momento. Ativo somente em modo MH. |  |  |  |  |

## Aba: No padrão

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Sistema de contrapressão da Halliburton |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  | Dispositivos de segurança | Mecanismo | Proteção | Pressão de teste | Set Abertura | Set Fechamento | Observações |
|  | PRVs Choke Manifold / Standpipe Manifold para BFM | PRV eletrônica com set de fixo de abertura e fechamento. | Linhas de superfície. | 3000 psi | 2400 psi | 1900 psi | N/A |
|  | PRVs Mangueiras de Fluxo / BFM | PRV eletrônica com set fixo de abertura e fechamento. | Linhas de superfície. | 1900 psi | 1700 psi | Maior entre: a) 750 psi; b) SBP de shut-in (PP) + 50 psi. | N/A |
|  | SPL (Secondary Pressure Limiter) | Funciona como uma PRV eletrônica só que com 02 estágios (posição de abertura do choke SPL). Os estágios são fixos e configurados no software. | O que for mais restrito entre linhas de superfície e poço. | N/A | Menor entre: a) 1400 psi; b) SBP de perfuração (FIT) - 100 psi. | SBP = SBP setpoint - 100 psi. | Exemplo: 1º Estágio: Choke SPL vai a 50% de abertura e permance nessa posição por 30s. 2º Estágio: Choke SPL vai a 100% de abertura e permance nessa posição. Em qualquer momento que a SBP voltar a ficar abaixo do set de abertura o choke SPL se fecha. |
|  | MAX SBP (Max Surface Back Pressure) | Limitador de SBP setpoint calculado pelo modelo hidráulico que não considera as condições dinâmicas do poço (limitador fixo). | O que for mais restrito entre linhas de superfície e poço. | N/A | 50 psi abaixo do set de abertura do SPL. | N/A | Não limita SBP setpoint imputada manualmente pelo operador. |
|  | ASP (Allowable Surface Pressure) | Limitador de SBP setpoint calculado pelo modelo hidráulico, baseado no limite superior da janela operacional (FIT/LOT), que considera as condições dinâmicas do poço (limitador variável). | O que for mais restrito entre linhas de superfície e poço. | N/A | Limitador varíavel baseado no limite superior da janela operacional (FIT/LOT). | N/A | Não limita SBP setpoint imputada manualmente pelo operador. |
|  |  |  |  |  |  |  |  |
|  | Cenários possíveis: |  |  |  |  |  |  |
|  | a) Cenário de plugueamento do Choke: Será ativado o SPL. Os outros dispositivos não irão ter reação para esse cenário. b) Cenário de MH determinar um SBP setpoint alto: Será limitado pelo MAX SBP. É importante que esse valor seja inferior ao SPL para evitar seu acionamento. c) Cenário de MH determinar um SBP setpoint alto em Well Control (ActEv): Será limitado pelo MAX SBP. Em cenário de perfuração a MS será de 150 psi para o FIT. Avaliar aumentar os limites de SPL e MAX SBP caso seja decidido transferir o controle do poço para a sonda para permitir aumentar a SBP na saída de bomba da coluna. |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  | Sistema de contrapressão da SLB |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  | Dispositivos de segurança | Mecanismo | Proteção | Pressão de teste | Set Abertura | Set Fechamento | Observações |
|  | PRVs Choke Manifold / Standpipe Manifold para BFM | PRV eletrônica com set de fixo de abertura e fechamento. | Linhas de superfície. | 3000 psi | 2400 psi | 1900 psi | N/A |
|  | PRVs Mangueiras de Fluxo / BFM | PRV eletrônica com set fixo de abertura e fechamento. | Linhas de superfície. | 1900 psi | 1700 psi | Maior entre: a) 750 psi; b) SBP de shut-in (PP) + 50 psi. | N/A |
|  | BIAS | BIAS é a tolerância máxima de desvio superior da SBP medida em relação à SBP setpoint. Quando esse limite é atingido o choke backup é aberto controladamente. Usualmente usa-se BIAS entre 50 e 100 psi. | Poço. | N/A | SBP > SBP setpoint + BIAS | SBP < SBP setpoint + BIAS | Mitiga eventos de sobrepressurização do poço no caso de entupimento do choke. |
|  | MAX SP (Max Surface Pressure) | Limitador de SBP que não considera as condições dinâmicas do poço (limitador fixo). Juntamente com o BIAS, não permitirá que a SBP ultrapasse esse limite. | O que for mais restrito entre linhas de superfície e poço. | N/A | Menor entre: a) 1400 psi; b) SBP de perfuração (FIT) - 100 psi. | N/A | Limita SBP setpoint tanto pelo modelo hidráulico quanto pelo input manual do operador. |
|  | DMAASP (Dynamic Max Allowable Annular Surface Pressure) | Limitador de SBP setpoint calculado pelo modelo hidráulico quando em modo Well Control (EKD-AIR), baseado no limite superior da janela operacional (FIT/LOT), que considera as condições dinâmicas do poço (limitador variável). | O que for mais restrito entre linhas de superfície e poço. | N/A | Limitador varíavel baseado no limite superior da janela operacional (FIT/LOT). | N/A | Somente ativo quando em modo Well control (EKD-AIR). Quando ativado inibe o limitador fixo do MAX SP. |
|  |  |  |  |  |  |  |  |
|  | Cenários possíveis: |  |  |  |  |  |  |
|  | a) Cenário de plugueamento do Choke: Será ativado o BIAS. b) Cenário de MH determinar um SBP setpoint alto: Será limitado pelo MAX SP. c) Cenário de MH determinar um SBP setpoint alto em Well Control (EKD-AIR): Será limitado pelo DMAASP e o MAX SP será inibido permitindo que o sistema utilize toda a margem de SBP na saída de bomba da coluna. |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  | Sistema de contrapressão da Weatherford |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  | Dispositivos de segurança | Mecanismo | Proteção | Pressão de teste | Set Abertura | Set Fechamento | Observações |
|  | PRVs Choke Manifold / Standpipe Manifold para BFM | PRV eletrônica com set de fixo de abertura e fechamento. | Linhas de superfície. | 3000 psi | 2400 psi | 1900 psi | N/A |
|  | PRVs Mangueiras de Fluxo / BFM | PRV eletrônica com set fixo de abertura e fechamento. | O que for mais restrito entre linhas de superfície e poço. | 1900 psi | Menor entre: a) 1400 psi; b) SBP de perfuração (FIT) - 100 psi. | Maior entre: a) 750 psi; b) SBP de shut-in (PP) + 50 psi. | Deve ser setado para proteção primária, pois possui capacidade de fechar automaticamente mantendo alguma pressão no poço. |
|  | High Limit | Funciona como uma PRV eletrônica de estágio único levando os chokes MPD para a posição de 100% aberto, sem mecanismo automático de fechamento. | Linhas de superfície. | N/A | 1700 psi | N/A | Deve ser setado para proteção secundária, pois precisa de intervenção do operador para ser fechada e reestabelecer a condição de poço pressurizado. |
|  |  |  |  |  |  |  |  |
|  | Cenários possíveis: |  |  |  |  |  |  |
|  | a) Cenário de plugueamento do Choke: Serão ativadas as PRVs das mangueiras de fluxo. b) Cenário de MH determinar um SBP setpoint alto: Será limitado pelo MAX SP. c) Cenário de MH determinar um SBP setpoint alto em Well Control (EKD-AIR): Será limitado pelo DMAASP e o MAX SP será inibido permitindo que o sistema utilize toda a margem de SBP na saída de bomba da coluna. |  |  |  |  |  |  |
