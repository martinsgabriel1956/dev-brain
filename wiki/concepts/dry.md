---
type: concept
title: "DRY (Don't Repeat Yourself)"
aliases: ["dry principle", "não se repita", "duplicação de código"]
date_created: 2026-08-18
date_updated: 2026-08-18
source_count: 1
tags: [dry, code-smells, duplicacao, abstracao, under-engineering, yagni]
skill: tech-mentor-backend
status: stub
---

# DRY (Don't Repeat Yourself)

Princípio que recomenda evitar duplicação de conhecimento/lógica no código. Registrado aqui não como regra absoluta, mas com a mesma cautela já presente em [[wiki/concepts/yagni]]: repetição nem sempre é o problema — abstração prematura sobre uma repetição ainda instável costuma ser pior.

## Posição do vídeo de origem (deliberadamente contrária ao dogma)

[[wiki/sources/9-code-smells-como-identificar-codigo-ruim]] declara explicitamente não ser fã de DRY como regra rígida: às vezes vale mais repetir um trecho de código do que abstraí-lo cedo demais. A decisão depende de **quanto** e **o quê** está sendo repetido, não da simples existência de duplicação.

Exemplo usado: chamadas a uma API espalhadas pelo código, cada uma validando status HTTP e extraindo o corpo da resposta de forma quase idêntica.

- **2 pontos de duplicação** → tolerável, não considerado problema real.
- **3 ou mais pontos** → problemático, porque o custo de manutenção passa a superar o custo de uma abstração.

O limiar numérico (2 vs. 3+) é uma heurística pessoal do autor, não uma métrica validada externamente — registrado aqui como opinião, não fato.

## Por que a duplicação incontrolada é um problema de manutenção (não de compreensão)

O código duplicado costuma continuar compreensível e testável isoladamente — o problema real é que uma mudança (ex.: endpoint alterado, novo código de status HTTP esperado) precisa ser replicada manualmente em todos os pontos duplicados, arriscando corrigir alguns e esquecer outros.

## Correção recomendada: abstrair só o que é de fato repetido

Extrair uma função auxiliar central (ex.: um helper de request HTTP que valida status e faz parsing) e reutilizá-la nos pontos que hoje duplicam a lógica — sem tentar abstrair preventivamente tudo que *poderia* se repetir no futuro. Mesmo depois de abstrair, evitar detalhes "mágicos" hard-coded (ex.: URL de API direto no código) — preferir variável de ambiente ou, no mínimo, uma constante nomeada (ver [[wiki/concepts/naming]]).

## Relacionado

[[wiki/concepts/code-smells]] · [[wiki/concepts/yagni]] · [[wiki/concepts/naming]] · [[wiki/concepts/refatoracao]]

## Key Sources

- [[wiki/sources/9-code-smells-como-identificar-codigo-ruim]]
