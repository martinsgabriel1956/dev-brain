---
type: concept
title: "Low Level Design (LLD)"
aliases: ["LLD", "Low-Level Design"]
date_created: 2026-05-17
date_updated: 2026-05-17
source_count: 1
tags: [system-design, arquitetura, lld, documentacao]
skill: tech-mentor-system-design
status: stable
---

# Low Level Design (LLD)

**TL;DR:** LLD é o zoom dentro de um componente definido no HLD. Responde "como esse bloco é implementado" — schemas de banco, contratos de API, estrutura de classes, algoritmos críticos e tratamento de erro.

## O Que É

Artefato que remove ambiguidade antes de codificar. Usado como referência direta antes e durante a implementação.

## O Que um LLD Cobre

- Estrutura interna do componente (camadas, módulos, responsabilidades)
- Contratos de API (endpoints, request/response, status codes, erros)
- Schema do banco (tabelas, colunas, índices, constraints, FK)
- Fluxo de dados interno (sequência de chamadas entre classes/funções)
- Casos de borda e tratamento de erro
- Estratégias de retry, idempotência e consistência

## Quando Usar / Evitar

**Usar:** implementando serviço/módulo novo de porte médio+, dependência entre times (frontend precisa do contrato antes), lógica de negócio complexa, design review formal.

**Evitar:** CRUD simples sem regra de negócio (o código é mais claro), time pequeno com contexto compartilhado, protótipo (o LLD vira dívida se o design mudar).

## Custo de Manutenção

Alto — diverge do código com o tempo. Requer disciplina para manter atualizado após mudanças de requisito.

## Key Sources

- [[wiki/sources/low-level-design]]

## Conceitos Relacionados

[[high-level-design]] · [[adr-architecture-decision-record]] · [[trd-technical-requirements-document]]
