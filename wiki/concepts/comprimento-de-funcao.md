---
type: concept
title: "Comprimento de Função"
aliases: ["function length", "tamanho de função", "função curta"]
date_created: 2026-04-29
date_updated: 2026-04-29
source_count: 1
tags: [clean-code, funcoes, complexidade, aninhamento, linux-kernel]
skill: tech-mentor-leadership
status: stub
---

## TL;DR

O tamanho máximo de uma função é inversamente proporcional à sua complexidade e nível de aninhamento. Funções complexas e aninhadas devem ser curtas. Funções simples podem ser longas.

## A Regra

```
complexidade ↑  →  tamanho máximo permitido ↓
complexidade ↓  →  tamanho máximo permitido ↑
```

Complexidade e aninhamento andam juntos: mais níveis de indentação geralmente significam mais complexidade, e vice-versa.

## Exceção Válida

Um `switch/case` longo com muitos casos diretos e simples pode ser extenso — porque a complexidade por caso é baixa mesmo que o número de casos seja alto.

## Relacionado

- [[indentacao-como-aviso]] — aninhamento como proxy de complexidade
- [[comentarios-o-que-nao-o-como]] — funções complexas geram necessidade de comentários de "como"

## Key Sources

- [[sources/estilo-de-codigo-convencoes]]
