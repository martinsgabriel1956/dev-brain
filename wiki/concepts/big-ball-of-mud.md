---
type: concept
title: "Big Ball of Mud"
aliases: ["big ball of mud", "grande bola de lama", "BBoM", "bola de lama"]
date_created: 2026-08-14
date_updated: 2026-08-14
source_count: 1
tags: [big-ball-of-mud, anti-patterns, arquitetura, entropia-de-software, legado, code-rot]
skill: tech-mentor-backend
status: draft
---

# Big Ball of Mud

## Definição

Um sistema de software que **carece de uma arquitetura perceptível** — a escala macroarquitetural do [[wiki/concepts/code-espaguete|código espaguete]]. Termo popularizado por [[wiki/entities/brian-foote|Brian Foote]] e [[wiki/entities/joseph-yoder|Joseph Yoder]] no paper *Big Ball of Mud* (PLoP '97), que creditam [[wiki/entities/brian-marick|Brian Marick]] por tê-lo cunhado.

> "Uma *Big Ball of Mud* é uma selva de código espaguete estruturada de forma desordenada, esparramada, desleixada, montada com fita adesiva e arame. (...) A informação é compartilhada promiscuamente entre elementos distantes do sistema, muitas vezes ao ponto de quase toda informação importante se tornar global ou duplicada." — Foote & Yoder, via [[wiki/sources/codigo-espaguete-wikipedia]]

## Por que é o estado *default*, não a exceção

O ponto contraintuitivo do conceito: a bola de lama não é fruto de incompetência isolada, e sim o resultado natural de três forças que atuam em quase todo sistema de vida longa — **pressão de negócio**, **rotatividade de desenvolvedores** (perda de contexto entre equipes) e **[[wiki/concepts/entropia-de-software|entropia de software]]**. É a mesma dinâmica descrita em [[wiki/concepts/god-object|God Object]] (a classe limpa que vira monstro sprint a sprint): ninguém decide construir uma bola de lama; ela se acumula.

## Sinais

- Informação global/duplicada em vez de encapsulada (viola [[wiki/concepts/ocultamento-de-informacao|ocultamento de informação]]).
- Nenhuma fronteira de módulo respeitada; qualquer parte fala com qualquer parte (ausência de [[wiki/concepts/separacao-de-responsabilidades|separação de responsabilidades]]).
- Crescimento não regulado + reparos improvisados repetidos (hotfix sobre hotfix).
- A estrutura original "erodiu além do reconhecimento" — ou nunca existiu.

## Lama por negligência vs. lama por escolha

O verbete trata a BBoM como puramente indesejável, mas há uma tensão produtiva com [[wiki/concepts/arquitetura-de-sacrificio|arquitetura de sacrifício]]: [[wiki/sources/arquitetura-de-sacrificio|Fowler]] argumenta que aceitar código descartável pode ser **deliberado e racional** quando você ainda não conhece a escala do problema. A diferença não está na aparência do código, e sim na intenção e na **[[wiki/concepts/monolito-modular|modularidade]]** que permite sacrificar *módulos* em vez do sistema inteiro. Sem boas fronteiras, "sacrifício" vira "lama".

## Como sair

- [[wiki/concepts/refatoracao|Refatoração]] contínua (regra do escoteiro, [[wiki/concepts/boy-scout-rule]]) para conter a entropia antes que consolide.
- [[wiki/concepts/strangler-fig-pattern|Strangler Fig]] para estrangular a lama incrementalmente em vez de reescrever tudo.
- Reintroduzir fronteiras: [[wiki/concepts/monolito-modular|monolito modular]] / [[wiki/concepts/hexagonal-architecture|Ports & Adapters]].

## Relacionado

[[wiki/concepts/code-espaguete]] · [[wiki/concepts/lasagna-code]] · [[wiki/concepts/ravioli-code]] · [[wiki/concepts/entropia-de-software]] · [[wiki/concepts/anti-pattern]] · [[wiki/concepts/arquitetura-de-sacrificio]]

## Key Sources

- [[wiki/sources/codigo-espaguete-wikipedia]] — definição de Foote & Yoder (PLoP '97) e as três forças (negócio, turnover, entropia)
