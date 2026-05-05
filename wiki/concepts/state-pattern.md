---
type: concept
title: "State Pattern"
aliases: ["state", "padrão estado"]
date_created: 2026-05-05
date_updated: 2026-05-05
source_count: 1
tags: [design-patterns, behavioral, state, gof]
skill: tech-mentor-backend
status: stub
---

# State Pattern

Padrão [[behavioral-patterns|comportamental]] que permite que um objeto altere seu comportamento quando seu **estado interno muda**. O objeto parecerá ter mudado de classe.

## Mecanismo

Encapsula cada estado em uma classe separada. O contexto mantém referência ao estado atual e delega para ele. Os estados podem iniciar transições para outros estados automaticamente.

## Distinção do Strategy

Estruturalmente muito similar ao [[strategy-pattern]], mas com intenção diferente:

| | State | [[strategy-pattern]] |
|---|---|---|
| Quem troca? | O próprio estado (automático) | O cliente (explícito) |
| Estados se conhecem? | Sim — podem acionar transições | Não — estratégias são independentes |
| Propósito | Modelar máquina de estados | Trocar algoritmos intercambiáveis |

## Quando usar

- Objetos que se comportam diferente dependendo do estado atual
- Muitas condicionais baseadas em estado espalhadas pelo código
- Máquinas de estados finitos: pedido (pendente → pago → enviado → entregue)

## Key Sources

- [[sources/design-pattern-strategy]] — mencionado nas relações como padrão estruturalmente similar
