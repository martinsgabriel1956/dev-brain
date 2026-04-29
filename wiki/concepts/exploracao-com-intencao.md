---
type: concept
title: "Exploração com Intenção"
aliases: ["intentional exploration", "explorar código com objetivo"]
date_created: 2026-04-29
date_updated: 2026-04-29
source_count: 1
tags: [codebase, aprendizado, debugging, fluxo-de-dados, onboarding]
skill: tech-mentor-leadership
status: stub
---

## TL;DR

Explorar um codebase com uma pergunta específica em mente é muito mais eficaz do que vagar aleatoriamente pelo código. A pergunta serve como fio condutor que conecta arquivos, funções e estados numa narrativa coerente.

## Exemplo

> "Quando desenho um retângulo, qual código roda no mouse down? Onde o shape vai para o estado? Quais componentes re-renderizam? Onde o undo é acionado?"

Rastrear essa pergunta no Excalidraw revela `onPointerDown` → `createGenericElement` → atualização de estado → re-render — um modelo mental completo do fluxo de dados para aquela ação.

## Key Sources

- [[sources/como-aprender-um-codebase-novo]]
