---
type: concept
title: "Árvore de Decomposição"
aliases: ["decomposition tree", "problem breakdown tree", "breakdown hierárquico"]
date_created: 2026-05-01
date_updated: 2026-05-01
source_count: 1
tags: [resolucao-de-problemas, debugging, pensamento-estruturado]
skill: tech-mentor-leadership
status: stable
---

## Definição

Técnica de [[pensamento-estruturado]] que pega um problema vago e o quebra hierarquicamente em perguntas cada vez mais específicas até chegar em algo testável e acionável.

```
Problema vago
├── Dimensão 1 (ex: onde?)
│   ├── Opção A
│   ├── Opção B
│   └── Opção C
├── Dimensão 2 (ex: quando?)
│   ├── ...
└── Dimensão 3 (ex: para quem?)
    ├── ...
```

## Por que funciona

Perguntas específicas geram respostas específicas. Respostas específicas geram soluções específicas. O problema "sistema lento" tem soluções completamente diferentes dependendo de *onde*, *quando* e *para quem* — sem a decomposição, você pode resolver a coisa errada.

## Exemplo — Sistema Lento

```
Sistema lento
├── Onde? → tela inicial / busca / relatório / tudo
├── Quando? → 10 usuários / 1000 usuários / sempre / noite
└── Para quem? → premium / gratuito / todos / mobile
```

Resultado: "sistema lento com 1000 usuários na tela inicial" → problema de escala → solução é paginação ou paralelização, não refatoração de código.

## Regra de Ouro

> Em nenhum momento você precisa mexer no código para chegar à causa raiz. A decomposição acontece antes de qualquer linha de código.

## Key Sources

- [[wiki/sources/pensamento-estruturado-resolucao-de-problemas]]
