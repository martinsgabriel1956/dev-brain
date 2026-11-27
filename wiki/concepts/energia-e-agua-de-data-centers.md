---
type: concept
title: "Energia e Água de Data Centers de IA"
aliases: ["consumo de energia de data centers", "consumo de água da IA", "data centers e rede elétrica", "custo energético da IA"]
date_created: 2026-11-27
date_updated: 2026-11-27
source_count: 2
tags: [data-center, energia, agua, infraestrutura, mercado-de-ia, sustentabilidade]
skill: tech-mentor-ai
status: stub
---

## Definição

O custo físico da IA que não aparece no preço do token: a eletricidade para treinar e servir os modelos e a água para resfriar os data centers e gerar a energia. Com a demanda de IA, isso virou restrição de infraestrutura (rede elétrica, licenças, água local), e não só item de custo.

## Números de referência

- **EUA:** data centers consumiram ~176 TWh em 2023, ~4,4% da eletricidade do país. A projeção é de 6,7–12% em 2028. [external] LBNL, https://eta.lbl.gov/publications/2024-lbnl-data-center-energy-usage-report
- **Mundo:** cerca de 1,5% da eletricidade em 2024, com a IA puxando o crescimento. [external] IEA, Energy and AI (2025), https://www.iea.org/reports/energy-and-ai
- **Rede:** a PJM Interconnection, o maior operador dos EUA (~65 milhões de pessoas), projeta déficit de ~6 GW de confiabilidade em 2027 por causa da demanda de data centers. [[wiki/sources/frontpush-ia-o-futuro-da-ia-parte-2]]
- **Água:** "meio litro a cada 20–30 perguntas" vem de Li et al. (2023) para o GPT-3, contando a água da geração de energia. É ordem de grandeza, não medida atual. [external] https://arxiv.org/abs/2304.03271

## No FrontPUSH

Na [[wiki/sources/frontpush-ia-o-futuro-da-ia-parte-1|parte 1]], "não existe água no mundo" para resfriar computadores infinitos. A [[wiki/sources/frontpush-ia-o-futuro-da-ia-parte-2|parte 2]] traz as manchetes (contas de luz em alta perto de data centers, data centers da Microsoft em SP, a Alphabet pedindo mais energia, painéis solares chineses) para concluir que "tudo vai ficar mais caro". Atenção a um erro de leitura da aula: "aumenta 12%" é a fatia da eletricidade chegando a até 12%, não um aumento de 12%.

## Relações

- [[wiki/concepts/terras-raras-e-minerais-criticos]] e [[wiki/concepts/gpu]]: o outro lado da restrição física.
- [[wiki/concepts/scaling-laws]]: mais escala, mais energia por ganho marginal.
- [[wiki/concepts/corrida-preco-qualidade-llm]] e [[wiki/concepts/enshittification]]: por que o preço pode subir mesmo com tokens mais eficientes.

## Key Sources

- [[wiki/sources/frontpush-ia-o-futuro-da-ia-parte-2]]: FrontPUSH, módulo de IA, aula 6: gráficos de TWh, 6 GW na PJM, água e contas de luz
- [[wiki/sources/frontpush-ia-o-futuro-da-ia-parte-1]]: FrontPUSH, módulo de IA, aula 5: energia e água como limite físico da escala
