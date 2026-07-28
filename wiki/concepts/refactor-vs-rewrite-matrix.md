---
type: concept
title: "Matriz Refatorar vs. Reescrever"
aliases: ["refactor vs rewrite", "matriz de decisão refatoracao reescrita"]
date_created: 2026-07-28
date_updated: 2026-07-28
source_count: 1
tags: [tech-debt, refactoring, rewrite, decisao, arquitetura]
skill: tech-mentor-leadership
status: stub
---

# Matriz Refatorar vs. Reescrever

## TL;DR

Matriz 2×2 de valor de negócio × risco técnico para decidir, depois de já ter priorizado um item de dívida técnica (via [[wiki/concepts/paid-framework]] ou [[wiki/concepts/hotspot-analysis]]), se o caminho certo é refatorar, reescrever, conviver ou depreciar.

## A Matriz

| | Baixo Risco Técnico | Alto Risco Técnico |
|---|---|---|
| **Alto Valor de Negócio** | Refatorar | Reescrever |
| **Baixo Valor de Negócio** | Conviver com isso | Depreciar |

- **Alto valor + baixo risco → Refatorar.** Vale investir, e o risco de quebrar algo mexendo é baixo.
- **Alto valor + alto risco → Reescrever.** O componente é importante o suficiente para justificar o esforço maior, mas o estado atual é arriscado demais para refatorar incrementalmente.
- **Baixo valor + baixo risco → Conviver com isso.** Não vale o esforço de tocar.
- **Baixo valor + alto risco → Depreciar.** Não vale manter nem investir — planejar a saída.

## O Risco do "Vamos Reescrever Tudo"

Reescrita tem custo de oportunidade alto: um caso citado na fonte descreve uma empresa que escolheu reescrever um sistema inteiro em vez de refatoração direcionada e ficou **18 meses sem entregar nenhuma feature nova**. Zerar a dívida técnica não vale o custo se o preço é estagnar o roadmap por um ano e meio — a matriz existe justamente para evitar escolher "reescrever" por padrão quando "refatorar" já resolveria.

Esse risco é o mesmo documentado como anti-padrão de "rewrite fantasma" na gestão de dívida técnica: reescrever sem produto funcionando ao lado é risco altíssimo.

## Relacionado

[[wiki/concepts/tech-debt-como-ferramenta]] · [[wiki/concepts/refatoracao]] · [[wiki/sources/strangler-fig]] — alternativa a uma reescrita "big bang": migrar gradualmente em vez de reescrever tudo de uma vez.

## Key Sources

- [[wiki/sources/tech-debt-guia-completo-gestao-metricas]]
