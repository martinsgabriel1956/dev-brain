---
type: concept
title: "State Pattern"
aliases: ["state", "padrão estado"]
date_created: 2026-05-05
date_updated: 2026-09-21
source_count: 2
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

## Exemplo de domínio: IA de jogos

O caso mais citado de State Pattern na prática é justamente a implementação de uma [[wiki/concepts/finite-state-machine|Finite State Machine (FSM)]] de comportamento de inimigo/NPC: cada estado (`patrulhar`, `perseguir`, `atacar`, `fugir`) vira uma classe própria, e o objeto de contexto (o inimigo) delega para o estado atual, que pode iniciar sua própria transição quando uma regra de design é satisfeita (distância do jogador, HP, evento de som). Ver [[wiki/sources/o-que-e-uma-finite-state-machine]].

## Key Sources

- [[sources/design-pattern-strategy]] — mencionado nas relações como padrão estruturalmente similar
- [[wiki/sources/o-que-e-uma-finite-state-machine]] — exemplo de FSM de Game Design (Pac-Man, turret) implementável via State Pattern
