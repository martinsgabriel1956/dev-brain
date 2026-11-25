---
type: concept
title: "Comprimento de Função"
aliases: ["function length", "tamanho de função", "função curta"]
date_created: 2026-04-29
date_updated: 2026-11-25
source_count: 2
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

## Contra a regra de N linhas (Ousterhout)

[[wiki/sources/filosofia-do-design-de-software-cap-04-modulos-devem-ser-profundos]] (4.6) ataca o conselho "qualquer método com mais de N linhas deve ser dividido" (N pode ser 10). Para [[wiki/entities/john-ousterhout]], a regra gera muitos métodos rasos e aumenta a complexidade do sistema; o critério certo é a profundidade, não o tamanho ([[wiki/concepts/modulo-profundo]], [[wiki/concepts/classite]]). Esta página também recusa o limite fixo, mas por outro critério (aninhamento). As duas convergem em "função simples pode ser longa".

## Key Sources

- [[wiki/sources/estilo-de-codigo-convencoes]]
- [[wiki/sources/filosofia-do-design-de-software-cap-04-modulos-devem-ser-profundos]] — crítica à regra de N linhas por método (4.6)
