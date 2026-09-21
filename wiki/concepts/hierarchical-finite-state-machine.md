---
type: concept
title: "Hierarchical Finite State Machine (HFSM)"
aliases: ["HFSM", "máquina de estados hierárquica", "statechart"]
date_created: 2026-09-21
date_updated: 2026-09-21
source_count: 1
tags: [cs-fundamentals, teoria-da-computacao, fsm, automatos, game-design, game-ai]
skill: cs-fundamentals
status: stub
---

# Hierarchical Finite State Machine (HFSM)

Extensão de [[wiki/concepts/finite-state-machine]] em que cada estado pode conter **subestados**, cada um com seu próprio conjunto de transições. Em vez de uma FSM plana com todas as transições declaradas entre todos os estados de topo, um comportamento pode ser aninhado dentro de outro maior — reduzindo a explosão combinatória de transições diretas conforme o número de comportamentos cresce.

## Exemplo

No modelo de FSM dos fantasmas de _Pac-Man_ ([[wiki/sources/o-que-e-uma-finite-state-machine]]), os estados de topo continuam sendo `perseguir` e `fugir`, mas cada um pode ser subdividido: o estado `perseguir` pode ter subestados como `atravessar paredes` ou `ficar invisível`, sem precisar declarar essas variações como estados de primeiro nível concorrendo diretamente com `fugir`.

## Relação com Statecharts (Harel)

O que a fonte chama de HFSM é conceitualmente equivalente ao que a literatura formal de teoria da computação chama de **Statechart** (David Harel, 1987): FSMs com hierarquia, estados concorrentes (paralelos) e ações associadas a transições. Ferramentas como **XState** (citada em [[wiki/concepts/maquina-de-estados-ui]]) implementam statecharts para uso em frontend/backend. `[skill: cs-fundamentals — references/computation-theory.md, seção "FSM vs Statechart (Harel)"]` — a fonte original não usa o termo "statechart" nem cita Harel; essa equivalência é uma adição da skill, não um claim do artigo.

## Relação com outros conceitos

- [[wiki/concepts/finite-state-machine]] — HFSM é uma extensão direta da FSM; toda FSM plana é um caso degenerado de HFSM sem subestados.
- [[wiki/concepts/maquina-de-estados-ui]] — statecharts (a forma "formal" de HFSM) são usados via XState para modelar componentes de UI complexos.

## Key sources

- [[wiki/sources/o-que-e-uma-finite-state-machine]] — introduz HFSM como "easter egg" ao final do artigo, com exemplo de subestados aplicado aos fantasmas de Pac-Man
