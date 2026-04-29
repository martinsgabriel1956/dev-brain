---
type: source
title: "Clean Architecture na Era da IA — O Custo Real das Abstrações"
aliases: ["clean architecture ia", "custo abstrações ia", "arquitetura agentes"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_count: 0
tags: [arquitetura, clean-architecture, ia, agentes, yagni, ddd, tokens, custo, abstraction-bloat]
skill: tech-mentor-backend
status: stable
source_file: /home/nemomartins/Documentos/new/dev-study/raw/clean-architecture-ia-custo-real.md
source_url: ""
author: "transcrição-video"
date_published: 2026-04-23
date_ingested: 2026-04-23
---

# Clean Architecture na Era da IA — O Custo Real das Abstrações

## TL;DR

Um time SaaS B2B de 10 devs com domínio complexo (billing, contratos, fiscais) seguiu Clean Architecture à risca. Ao adotar Claude Code, features simples passaram a tocar 18 arquivos — consumindo contexto demais, inventando relações, repetindo lógica. O custo por feature subiu em tokens, revisão e bugs. A pergunta central: quanto da arquitetura que defendemos por décadas era sobre código — e quanto era sobre nossos próprios limites cognitivos?

## Key Claims

**Claim:** Feature simples em Clean Architecture ritualística pode tocar 18 arquivos, tornando o trabalho com agentes de IA mais caro e propenso a erros.
**Evidence:** Caso real: time SaaS B2B, adoção de Claude Code, produtividade caiu em alguns módulos.
**Source:** raw/clean-architecture-ia-custo-real.md
**Confidence:** Alta (caso observado diretamente)

**Claim:** A indústria já vinha simplificando arquitetura antes da IA — Go é a prova.
**Evidence:** Kubernetes, Docker e Cloudflare implementam princípios de Clean Architecture sem cerimônia: sem classes, herança ou anotações.
**Source:** raw/clean-architecture-ia-custo-real.md
**Confidence:** Alta

**Claim:** DDD Estratégico ficou mais importante com IA, não menos; DDD Tático é o que vale questionar.
**Evidence:** Bounded Context limita o escopo de arquivos que o agente precisa ler — otimização de token, não só clareza de modelo.
**Source:** raw/clean-architecture-ia-custo-real.md
**Confidence:** Alta

**Claim:** Encapsulamento e Inversão de Dependência são conceitos distintos que a maioria dos devs confunde.
**Evidence:** Encapsulamento = esconder detalhe (sem interface necessária). DIP = alto nível não depende de baixo nível diretamente — ambos dependem de abstração.
**Source:** raw/clean-architecture-ia-custo-real.md
**Confidence:** Alta

**Claim:** A regra prática é "Estratégico → Flat → Abstrai por Dor" — não desenhar para o futuro imaginado.
**Evidence:** Três perguntas: trocou essa dependência nos últimos 2 anos? tem segundo caso de uso real? tem medo de poluição de contrato externo?
**Source:** raw/clean-architecture-ia-custo-real.md
**Confidence:** Alta

## Entities

- [[entities/uncle-bob]] — Robert C. Martin, autor de Clean Architecture
- [[entities/eric-evans]] — autor de Domain-Driven Design
- [[entities/kent-beck]] — autor de Extreme Programming, cunhou YAGNI em 1999

## Concepts

- [[concepts/yagni]] — You Ain't Gonna Need It, princípio de não antecipar abstração
- [[concepts/abstraction-bloat]] — agentes geram complexidade desnecessária por viés de treinamento
- [[concepts/abstraction-illusion]] — IA torna padrões acessíveis sem torná-los apropriados
- [[concepts/navigation-paradox]] — mais arquivos = mais falhas de navegação do agente
- [[concepts/comprehension-debt]] — dívida de compreensão do código gerado por IA
- [[concepts/vertical-slice-architecture]] — organização por feature, não por camada
- [[concepts/dependency-injection]] — injeção de dependência — backlink adicionado

## Open Questions

- Existe um número de arquivos por feature que serve como threshold objetivo para questionar a arquitetura?
- Como medir o custo real em tokens de diferentes estilos arquiteturais no mesmo codebase?

## Raw Quotes

> "Quanto da arquitetura que a gente defendeu por décadas era sobre código — e quanto era sobre os nossos próprios limites?"

> "Cada arquivo a mais no teu projeto é token a mais no contexto do agente."

> "Contexto delimitado bem definido virou otimização de contexto — não só clareza de modelo."

> "Tu não precisa de algo até precisar. E quando precisar, refatora — porque código simples é mais fácil de refatorar do que a abstração que tu tentou adivinhar ao futuro."
