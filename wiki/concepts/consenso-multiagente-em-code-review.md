---
type: concept
title: "Consenso Multiagente em Code Review"
aliases: ["review multiagente por consenso", "filtro social de agentes", "verificação de achados de review"]
date_created: 2026-10-26
date_updated: 2026-10-26
source_count: 1
tags: [code-review, agentes, multi-agente, falso-positivo, verificacao, anthropic]
skill: tech-mentor-ai
status: draft
---

# Consenso Multiagente em Code Review

Padrão da camada 3 do pipeline da [[wiki/entities/anthropic]] ([[wiki/sources/anthropic-code-review-por-agentes-sete-camadas]]):

1. **Vários agentes caçam bugs em paralelo** no mesmo PR, lendo o diff **contra o repositório inteiro e a intenção declarada** ("resolve o que diz resolver? encaixa no sistema? quebra outra coisa?").
2. Um **grupo separado verifica** cada achado.
3. **Só vira comentário o que é confirmado por consenso**; estilo, limpeza e achados não unânimes são descartados — "um filtro social dos agentes".
4. O que sobrevive é **ordenado por gravidade e rotulado** (importante / nitpick / pré-existente).

Os filtros foram validados por **A/B nos próprios PRs** antes de serem mantidos.

## Por que importa

Troca recall por precisão: reduz o ruído que, com autor-agente, vira loop de correções ([[wiki/concepts/ruido-e-loop-de-nitpick-em-revisao-por-agente]]). O comportamento é guiado por [[wiki/concepts/review-md]].

## Leitura [skill: tech-mentor-ai — inferência]

É um caso de *self-consistency* / votação aplicado à detecção de bugs, mais um estágio de verificação no estilo [[wiki/concepts/llm-as-judge]]. Risco: se os agentes compartilham o mesmo modelo e viés, o consenso pode confirmar o mesmo falso negativo — o custo é de tokens (várias execuções por PR), não medido na fonte.

## Key sources

- [[wiki/sources/anthropic-code-review-por-agentes-sete-camadas]]
