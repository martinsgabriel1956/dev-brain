---
type: concept
title: "Finite State Machine (FSM)"
aliases: ["FSM", "máquina de estado finita", "máquina de estados finitos", "autômato finito"]
date_created: 2026-09-21
date_updated: 2026-09-21
source_count: 1
tags: [cs-fundamentals, teoria-da-computacao, fsm, automatos, game-design, game-ai]
skill: cs-fundamentals
status: draft
---

# Finite State Machine (FSM)

Modelo matemático com um número finito de estados, um estado inicial, e uma função de transição que leva de um estado a outro quando um evento/input ocorre. Apenas um estado pode estar ativo por vez — dois estados mutuamente exclusivos nunca coexistem. `[skill: cs-fundamentals — references/computation-theory.md]`

## Componentes

- **Estados**: um conjunto finito de comportamentos possíveis (ex.: `perseguir`, `fugir`, `patrulhar`, `atacar`).
- **Transições**: mudanças de um estado para outro, disparadas por um evento ou por uma regra definida arbitrariamente (distância do jogador, ruído, item consumido, HP zerado).
- **Estado inicial** (e, em automação formal, estados finais/de aceitação — nem sempre relevante em FSMs de jogo, que costumam rodar em loop contínuo).

```typescript
type State = 'patrulhar' | 'atacar' | 'eliminado'
type Event = 'JOGADOR_NO_ALCANCE' | 'JOGADOR_SEM_VIDA' | 'REVIVE_USADO'

const transitions: Record<State, Partial<Record<Event, State>>> = {
  patrulhar: { JOGADOR_NO_ALCANCE: 'atacar' },
  atacar:    { JOGADOR_SEM_VIDA: 'eliminado' },
  eliminado: { REVIVE_USADO: 'patrulhar' },
}
```

## Exemplo de Game Design: fantasmas de Pac-Man

Os fantasmas de _Pac-Man_ têm dois estados mutuamente exclusivos: **perseguir** e **fugir**. Por padrão, perseguem o jogador; ao comer uma pílula, a transição inverte e os fantasmas passam a fugir. É um exemplo didático porque o gatilho da transição (comer a pílula) é visualmente óbvio — mas transições de FSM em jogos nem sempre são assim. Um inimigo pode transitar de "patrulhar" para "atacar" apenas quando o jogador chega a uma distância exata definida pelo Game Designer, ou ao ouvir um ruído que chama sua atenção — a função de transição é, na prática, um contrato de design arbitrário sobre o estado do mundo, não uma limitação técnica do modelo. Ver [[wiki/sources/o-que-e-uma-finite-state-machine]].

## Papel histórico em IA de jogos

FSM foi uma das primeiras técnicas usadas para modelar IA de inimigos/NPCs, e ainda é usada hoje, mas perdeu espaço como abordagem dominante diante de técnicas mais expressivas como Behavior Trees, GOAP (Goal-Oriented Action Planning) e Utility AI — que evitam a explosão combinatória de transições que uma FSM plana sofre à medida que o número de estados cresce `[external]`.

## Relação com outros conceitos

- [[wiki/concepts/maquina-de-turing]] — FSM é um autômato mais fraco na hierarquia de Chomsky: tem memória finita (apenas o estado atual) e nenhuma fita/pilha, ao contrário da máquina de Turing (irrestrita) ou do pushdown automaton (livre de contexto). FSM só reconhece linguagens regulares.
- [[wiki/concepts/state-pattern]] — é a implementação orientada a objetos mais comum de uma FSM: cada estado vira uma classe, e o contexto delega comportamento e transições para o estado atual.
- [[wiki/concepts/maquina-de-estados-ui]] — aplicação de FSM a componentes de interface (loading/erro/sucesso), com a mesma regra de exclusividade mútua de estados.
- [[wiki/concepts/hierarchical-finite-state-machine]] — extensão hierárquica da FSM: cada estado pode conter subestados com seu próprio conjunto de transições, evitando que a FSM plana cresça descontroladamente.

## Key sources

- [[wiki/sources/o-que-e-uma-finite-state-machine]] — definição via exemplos de Game Design (Pac-Man, turret), incluindo transições disparadas por regras definidas pelo Game Designer e o papel histórico da FSM como IA de jogos
