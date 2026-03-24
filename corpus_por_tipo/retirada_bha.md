# Retirada de BHA / Manobra

1 SEQOPs | 1 comentários MPD

## Análise IA dos Comentários

```json
{
  "sub_tipos": [
    "Troca de broca",
    "Teste de pressão Hold Point",
    "Controle do poço via circuito de superfície"
  ],
  "pontos_verificacao": [
    {
      "item": "Realização obrigatória do teste de pressão Hold Point para instalação de BA",
      "frequencia": "alta",
      "exemplo_real": "Adicionar um item 'c)' Para toda instalação de BA, é obrigatório realizar o teste de pressão Hold Point, com aprovação do CSD-MPD conforme o cenário."
    },
    {
      "item": "Confirmação de estanqueidade da LBSR ou CSR",
      "frequencia": "alta",
      "exemplo_real": "Passo #15 a) confirmar estanqueidade da LBSR ou CSR?"
    },
    {
      "item": "Teste de estanqueidade do BA contra LBSR ou CSR",
      "frequencia": "alta",
      "exemplo_real": "Passo #25) teste de estanqueidade do BA contra LBSR ou CSR?"
    },
    {
      "item": "Equalização de pressão acima da LBSR ou CSR",
      "frequencia": "média",
      "exemplo_real": "Passo #25 e) equalizar pressão acima da LBSR ou CSR?"
    },
    {
      "item": "Velocidade máxima permitida no BA no RCD",
      "frequencia": "média",
      "exemplo_real": "Passo #26 b) Velocidade máxima (limite BA no RCD): 2 min/seção."
    },
    {
      "item": "Garantia de vazão mínima pela booster durante operações específicas",
      "frequencia": "média",
      "exemplo_real": "Não é possível bombear isoladamente o tampão pela coluna mantendo vazão na booster. Logo, para garantir uma vazão mínima pela booster, nós da OP topamos 'perder' uma fração do tampão para a booster/riser com 50 gpm."
    }
  ],
  "erros_frequentes": [
    "Omissão do teste de pressão Hold Point para instalação de BA",
    "Falta de clareza sobre a abertura ou fechamento da CSR em momentos específicos",
    "Ausência de confirmação de estanqueidade da LBSR ou CSR",
    "Falta de equalização de pressão acima da LBSR ou CSR"
  ],
  "padroes_aprovacao": [
    "Clareza nas etapas de operação, incluindo abertura e fechamento de válvulas",
    "Garantia de testes de estanqueidade em pontos críticos",
    "Definição de critérios claros para vazão mínima e velocidade máxima em operações com BA"
  ],
  "normas_aplicaveis": [
    "PE-2POC-01113"
  ]
}
```

## Comentários MPD Completos

### 1-RJS-763D — 26 - Manobra com MPD para troca de broca
**Ivani Tavares de Oliveira** | v1

Em ALERTAS PARA OPERAÇÃO COM MPD:
Passo #3: mover o item b) do passo #14 e remover este passo.
Ainda no passo #3, adicionar um item "c)" Para toda instalação de BA, é obrigatório realizar o teste de pressão Hold Point, com aprovação do CSD-MPD conforme o cenário. Seguem os critérios:

Passo #16: Eu desconheço essas recomendações. Mas se for procedimento da sonda, tudo bem.

Passo #18 b) a partir deste item, avaliar a possibilidade de manter o controle do poço com MPD via circuito de superfície.

passo #15 a) confirmar estanqueidade da LBSR ou CSR?

Passo #25) teste de estanqueidade do BA contra LBSR ou CSR?
e) equalizar pressão acima da LBSR ou CSR?
Em que momento vai abrir CSR? No passo #14 f) está: "Fechar LBSR e CSR."
600 gpm na booster (2 bombas de barramentos diferentes).

Passo #26 b) Velocidade máxima (limite BA no RCD): 2 min/seção.

> ↳ **Ramon Sena Barretto:** Ivani, o passo #16 existe por uma dificuldade do lay-out da sonda. Não é possível bombear isoladamente o tampão pela coluna mantendo vazão na booster. Logo, para garantir uma vazão mínima pela booster, nós da OP topamos "perder" uma fração do tampão para a booster/riser com 50 gpm.

> ↳ **Ramon Sena Barretto:** Os passos que mencionam a gaveta fechada, é sempre LBSR mesmo, pois a CSR não veda; ela é fechada apenas para proteção mecânica acima da LBSR. MAs ficou faltando de fato abrir a CSR, corrigido no passo 25.
