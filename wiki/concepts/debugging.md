---
type: concept
title: "Debugging"
aliases: ["depuração", "encontrar bugs"]
date_created: 2026-07-09
date_updated: 2026-07-21
source_count: 2
tags: [debugging, resolucao-de-problemas, pensamento-estruturado]
skill: tech-mentor-leadership
status: stub
---

## Definição

Processo de investigar um comportamento incorreto de um sistema até encontrar e corrigir sua [[causa-raiz]]. Na prática do dia a dia, debugging é a aplicação direta do método de [[pensamento-estruturado]] a um problema técnico concreto: entender o problema antes de mexer no código, decompor via [[arvore-de-decomposicao]], testar hipóteses ([[hipotese-e-validacao]]) em vez de assumir, e só então intervir no ponto exato do gargalo.

## Relação com outros conceitos

- [[pensamento-estruturado]] — o método geral do qual debugging é uma aplicação
- [[arvore-de-decomposicao]] — como quebrar um bug vago ("sistema lento") em perguntas específicas
- [[causa-raiz]] — o alvo final da investigação
- [[hipotese-e-validacao]] — validar suposições com dados antes de agir
- [[pensamento-regressivo]] — mapear o fluxo de trás para frente a partir do estado esperado

## Setup prático: debugger conectado desde o primeiro commit

Em vez de depurar via `console.log` + reiniciar servidor manualmente, [[wiki/concepts/setup-live-reload-debug-testes]] descreve como conectar o debugger do editor (`--inspect` do Node.js + `launch.json` do VS Code) direto ao ciclo de live reload e testes automatizados — permitindo breakpoints e inspeção de variáveis (inclusive via um "Debug Console" tipo REPL) sem sair do editor a cada hipótese testada.

## Key Sources

- [[wiki/sources/pensamento-estruturado-resolucao-de-problemas]]
- [[wiki/sources/3-pilares-testes-automatizados-produtividade]] — setup de debugger integrado a live reload e testes via Node.js `--inspect` + VS Code `launch.json`
