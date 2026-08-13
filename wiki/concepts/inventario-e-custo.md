---
type: concept
title: "Inventário É Custo"
aliases: ["inventory is cost", "trabalho em progresso como custo", "WIP como custo"]
date_created: 2026-08-13
date_updated: 2026-08-13
source_count: 1
tags: [lean, toyotismo, fluxo, teoria-de-filas, pull-request, gestao-de-fluxo, reinertsen]
skill: tech-mentor-leadership
status: stub
---

# Inventário É Custo

Princípio de origem toyotista (lean manufacturing), aplicado a desenvolvimento de software por [[wiki/entities/principles-of-product-development-flow|Donald Reinertsen]]: qualquer trabalho iniciado mas não concluído — código escrito mas não mergeado, feature pronta mas não lançada, PR aberto — é **inventário parado**, e inventário parado é custo, não neutro. A alternativa a um estilo "fordista" (lotes grandes, processamento em massa) é manter o inventário pequeno e processar o fluxo de trabalho de forma rápida e contínua.

## Aplicação a Pull Requests

[[wiki/sources/pull-requests-por-que-falham-alternativas-sem-pr]] aplica o princípio diretamente a PRs abertos: um PR parado por uma semana é uma semana em que aquele código não está gerando valor para a empresa — o próprio propósito do código é gerar dinheiro, então código parado equivale a dinheiro parado. Exemplo numérico usado na fonte: um dev de R$ 10.000/mês custa ~R$ 2.500 por semana de trabalho; um PR dele parado por uma semana representa esse valor "congelado" sem retorno.

Consequência prática defendida pela fonte: revisar PRs abertos **todos os dias**, idealmente **duas vezes por dia** (início e fim do expediente) — reduzindo tanto o tempo de inventário parado quanto o custo de troca de contexto (*context switching*) imposto sobre quem abriu o PR a cada ciclo de ida e volta entre autor e revisor.

## Relacionado

- [[wiki/entities/principles-of-product-development-flow]] — a obra de onde vem o princípio, já registrada por outra fonte sobre folga de capacidade de time
- [[wiki/concepts/code-review]] — PR como unidade concreta de inventário no contexto de revisão de código
- [[wiki/concepts/trunk-based-development]] — reduz inventário ao eliminar a espera por aprovação de PR

## Key Sources

- [[wiki/sources/pull-requests-por-que-falham-alternativas-sem-pr]] — aplicação do princípio a PRs abertos; recomendação de cadência de revisão diária/2x-dia
