# Teste de Influxo / Teste BOP

5 SEQOPs | 2 comentários MPD

## Análise IA dos Comentários

```json
{
  "sub_tipos": [
    "Teste do BOP com ITT PUAO",
    "Teste do sistema MPD",
    "Corte do cimento",
    "Troca do fluido"
  ],
  "pontos_verificacao": [
    {
      "item": "Verificar e registrar a pressão setada no 'Latch Safety Rating' e garantir que o intertravamento está habilitado.",
      "frequencia": "alta",
      "exemplo_real": "item 6. d) Verificar e registrar a pressão setada no 'Latch Safety Rating' que corresponde ao intertravamento entre unlatch e pressão trapeada abaixo do BA. Garantir que o intertravamento está habilitado."
    },
    {
      "item": "Confirmar substituição de fluido e alinhamento para trip tank.",
      "frequencia": "alta",
      "exemplo_real": "Item 5. Bullet #1: retorno pela flowline até confirmar a substituição AGMAR por FPBA 8,7 ppg (mínimo de 10 bbl?). Fazer alinhamento para trip tank."
    },
    {
      "item": "Realizar testes de pressão em diferentes configurações de válvulas e componentes do sistema.",
      "frequencia": "alta",
      "exemplo_real": "item 10 em teste #1: Riser, RCD+BA, RCD-V1, FLS-V1, FLS-V3; teste #2: Riser, RCD+BA, RCD-V2, FLS-V2, FLS-V4; teste #3: Riser, RCD+BA, BFM-V1+BFM-V2+BFM-V9; Teste #4: Riser, DSIT, BFM-V3, BFM-V4, BFM-V10."
    },
    {
      "item": "Garantir que a pressão do riser + poço revestido esteja entre 1900 psi e 2000 psi.",
      "frequencia": "alta",
      "exemplo_real": "item 11. Elevar pressão do riser + poço revestido entre 1900 psi e 2000 psi."
    },
    {
      "item": "Avaliar o retorno do cimento antes de alinhar o sistema MPD para etapas do fingerprint.",
      "frequencia": "média",
      "exemplo_real": "item 20 - bullet #1: Após 1 BU, avaliar o retorno do cimento antes de alinhar o sistema MPD para antecipar as etapas do fingerprint."
    },
    {
      "item": "Verificar a possibilidade de drenagem pelo choke hidráulico caso o tanque da UC não tenha volume suficiente.",
      "frequencia": "média",
      "exemplo_real": "item 12. Se a UC não tiver tanque com volume suficiente para receber o retorno, drenar pelo choke hidráulico do choke manifold da sonda, ou conforme procedimento da sonda."
    },
    {
      "item": "Realizar teste da NRV de alta com 4500 psi, se aplicável.",
      "frequencia": "baixa",
      "exemplo_real": "Item 10. Avaliar realizar teste da NRV de alta com 4500 psi (cenário de PMCD previsto?)."
    }
  ],
  "erros_frequentes": [
    "Omissão de registro da pressão setada no 'Latch Safety Rating'.",
    "Falta de alinhamento adequado para o trip tank durante substituição de fluido.",
    "Configurações incorretas ou incompletas nos testes de pressão em válvulas e componentes.",
    "Pressão do riser + poço revestido fora da faixa recomendada (1900 psi a 2000 psi).",
    "Falta de avaliação do retorno do cimento antes de alinhar o sistema MPD.",
    "Ausência de planejamento para drenagem em caso de insuficiência de volume no tanque da UC."
  ],
  "padroes_aprovacao": [
    "Registro detalhado e correto das pressões e intertravamentos.",
    "Execução de testes de pressão em todas as configurações necessárias.",
    "Planejamento adequado para substituição de fluido e alinhamento para trip tank.",
    "Garantia de que a pressão do riser + poço revestido está dentro da faixa recomendada.",
    "Antecipação de problemas, como entupimento do choke MPD, com base em histórico recente."
  ],
  "normas_aplicaveis": [
    "PE-2POC-01113",
    "PE-1PBR-00037"
  ]
}
```

## Comentários MPD Completos

### 4-SPS-112 — Teste do BOP com ITT PUAO e ITT PUAO + RTLe
**Leonardo Mesquita Caetano há um ano** | v1

Pessoal, boa tarde.
Qual momento previsto para instalação do BA e teste da junta integrada?

OPERAÇÕES EM PARALELO E OFFLINE
Item 10. Avaliar realizar teste da NRV de alta com 4500 psi (cenário de PMCD previsto?)

> ↳ **Anderson Morosov há um ano:** Boa tarde.

1) Não tem previsão de PMCD em projeto.
2) Testes do BA e junta integrada serão durante a descida do BHA.

### 7-BUZ-94D-RJS — Teste do sistema MPD, corte do cimento e troca do fluido
**Ivani Tavares de Oliveira** | v1

Item 5. Bullet #1: retorno pela flowline até confirmar a substituição AGMAR por FPBA 8,7 ppg (mínimo de 10 bbl?). Fazer alinhamento para trip tank. 
*Analisar com o químico a possibilidade de efetuar a substituição do fluido para o TT com AGMAR e depois de confirmar fluido 8,7 ppg, substituir para o TT que estará com FPBA 8,7 ppg. Substituir em paralelo o TT contaminado (AGMAR + Fluido 8,7 ppg).

item 6. d) Verificar e registrar a pressão setada no "Latch Safety Rating" que corresponde ao intertravamento entre unlatch e pressão trapeada abaixo do BA. Garantir que o intertravamento está habilitado.

item 9. (Pfinal ≥ 1900 psi e < 2000 psi - Pnominal)

item 10 em teste #1: Riser, RCD+BA, RCD-V1, FLS-V1, FLS-V3
teste #2: Riser, RCD+BA, RCD-V2, FLS-V2, FLS-V4
teste #3: Riser, RCD+BA, BFM-V1+BFM-V2+BFM-V9
Teste #4: Riser, DSIT, BFM-V3, BFM-V4, BFM-V10

item 11. Elevar pressão do riser + poço revestido entre 1900 psi e 2000 psi

Item 12. Se a UC não tiver tanque com volume suficiente para receber o retorno, drenar pelo choke hidráulico do choke manifold da sonda, ou conforme procedimento da sonda.

item 18. Acrescentar o texto: usando a linha de by-pass (BFM V4 aberta e MV-010 fechada), alinhada para flowline.
Ainda o item 18, o padrão PE-1PBR-00037 não abrange operações em MPD/MCD.

item 20 - bullet #1: Após 1 BU, avaliar o retorno do cimento antes de alinhar o sistema MPD para antecipar as etapas do fingerprint. Histórico recente de entupimento do choke MPD, ainda em investigação.
