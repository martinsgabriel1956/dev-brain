---
type: concept
title: "Indentação Como Aviso"
aliases: ["indentation as warning", "8 char tabs", "aninhamento excessivo"]
date_created: 2026-04-29
date_updated: 2026-04-29
source_count: 1
tags: [indentacao, clean-code, aninhamento, linux-kernel, estilo]
skill: tech-mentor-leadership
status: stub
---

## TL;DR

Indentação padrão é 8 caracteres (Linux Kernel Coding Style). Quando o código "sai da tela" com esse tamanho de indentação, o sinal é claro: há aninhamento demais. A solução é refatorar o aninhamento — não reduzir a indentação para esconder o problema.

## A Lógica

Reduzir tabs para 2 ou 4 permite aninhar mais antes de sentir a dor. Isso mascara um design ruim. Com 8 caracteres, a dor aparece mais cedo — e é intencional.

## Key Sources

- [[sources/estilo-de-codigo-convencoes]]
