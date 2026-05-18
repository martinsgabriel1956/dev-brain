---
type: source
title: "Low Level Design (LLD)"
aliases: ["LLD"]
date_created: 2026-05-17
date_updated: 2026-05-17
source_file: /home/nemomartins/Documentos/new/dev-study/raw/low-level-design.md
source_url: ""
author: "tech-mentor-system-design"
date_published: 2026-05-17
date_ingested: 2026-05-17
tags: [system-design, arquitetura, lld, documentacao]
skill: tech-mentor-system-design
status: stable
---

# Low Level Design (LLD)

## TL;DR

LLD é o zoom dentro de um componente definido no HLD — responde "como esse bloco é implementado". Cobre schemas de banco, contratos de API, estrutura de classes, algoritmos críticos e tratamento de erro. É o artefato que o time usa como referência direta antes e durante a implementação.

## Key Claims

- **Remove ambiguidade antes de codificar:** schema de banco, assinaturas de endpoint, sequência de chamadas internas. [[wiki/concepts/low-level-design]]
- **Habilita desenvolvimento paralelo:** frontend pode iniciar antes do backend se o contrato de API estiver no LLD
- **Problemas de modelagem emergem cedo:** schema no LLD detecta problemas de normalização antes de migration existir
- **Custo de manutenção alto:** diverge do código com o tempo — requer disciplina para manter atualizado
- **Diagrama de sequência** torna fluxos complexos navegáveis, mas fica obsoleto rapidamente se o código muda
- **Evitar em CRUD simples:** o código é mais claro que o diagrama nesses casos

## Concepts

- [[wiki/concepts/low-level-design]]
- [[wiki/concepts/high-level-design]]
- [[wiki/concepts/adr-architecture-decision-record]]
- [[wiki/concepts/trd-technical-requirements-document]]

## Open Questions

- Qual é o nível de detalhe mínimo que justifica um LLD vs. simplesmente escrever o código?

## Raw Quotes

> "LLD é onde decisões de HLD se tornam contratos concretos: schemas de banco, assinaturas de API, estrutura de classes, algoritmos críticos e tratamento de erro."
