---
type: entity
title: "Spring Boot"
aliases: ["Spring", "Spring Framework"]
date_created: 2026-08-24
date_updated: 2026-08-24
source_count: 1
tags: [java, spring-boot, framework, backend]
skill: tech-mentor-leadership
status: stub
---

# Spring Boot

Framework Java para construção de aplicações backend, usado como estudo de caso em [[wiki/sources/como-ler-documentacao-de-uma-linguagem-de-programacao]] para demonstrar o [[wiki/concepts/padrao-de-secoes-de-documentacao-tecnica|padrão universal de seções de documentação]] (getting started, tutorials, guides, API reference).

## Estrutura da documentação oficial

- **Getting Started** — "building an app", com código de exemplo de um Hello Controller e uso de command line runner
- **Learning → Quickstart** — guia de início de projeto
- **Learning → Guides** — guias de estudo por tópico (ex.: "Building a RESTful Web Services"), com passo a passo completo
- **Projects** — sub-projetos com tutoriais próprios: Spring Integration, Spring AI, Spring Cloud, Spring Data (Spring Data JPA)

## Spring Data JPA — nomenclatura de método como query

Convenção de nomenclatura de métodos de repositório que gera a query automaticamente a partir do nome — ex.: `findDistinctByLastnameAndFirstname` gera um `SELECT DISTINCT` filtrando por sobrenome e nome, sem escrever SQL/JPQL manualmente.

## Key Sources

- [[wiki/sources/como-ler-documentacao-de-uma-linguagem-de-programacao]]
