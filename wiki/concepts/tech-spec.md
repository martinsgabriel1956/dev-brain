---
type: concept
title: "Tech Spec (Especificação Técnica)"
aliases: ["tech spec", "especificação técnica", "technical specification sdd"]
date_created: 2026-06-02
date_updated: 2026-07-09
source_count: 3
tags: [spec-driven, tech-spec, planejamento, documentacao, harness]
skill: tech-mentor-ai
status: stable
---

# Tech Spec (Especificação Técnica)

## TL;DR

Segundo artefato do fluxo [[wiki/concepts/spec-driven-development|Spec Driven Development]]. Converte o PRD (o quê e o porquê) em decisões tecnológicas concretas (o como). É o contexto que cada agente de execução recebe junto com a tarefa a ser implementada.

## Posição no Fluxo SDD

```
Ideia → [PRD] → [Tech Spec] → [Tarefas] → Execução
          ↑           ↑             ↑
       negócio    tecnologia     execução
       (o quê)    (o como)
```

## O que Contém

- Decisões de arquitetura específicas do problema
- Contratos de API (endpoints, schemas, tipos)
- Estratégia de persistência e modelagem de dados
- Restrições técnicas e dependências externas
- Critérios de aceite técnicos (performance, segurança, compatibilidade)
- Questões técnicas abertas

## O que NÃO Contém

- Padrões de arquitetura globais do projeto → ficam nas [[wiki/concepts/rules-agente|rules]]
- Requisitos de negócio → ficam no [[wiki/concepts/prd-product-requirements-document|PRD]]
- Tech Spec referencia rules, não as repete

## Contexto que Consome

O agente que gera a Tech Spec recebe como input:
1. O PRD aprovado
2. As rules do projeto (patterns, stack, convenções)
3. As skills disponíveis
4. Análise do código fonte relevante

## Granularidade de Tarefas

Cada tarefa derivada da Tech Spec deve ser pequena o suficiente para:
- Caber em um único contexto de execução
- Ser reexecutável isoladamente se interrompida
- Ser verificável com um critério de aceite claro

## Especificar Mudanças de Módulo e Interface, Não Só Endpoints

[[wiki/sources/fundamentos-de-software-importam-mais-que-nunca-na-era-da-ia]] acrescenta um item concreto ao "O que Contém": a tech spec deve ser específica sobre **quais [[wiki/concepts/modulo-profundo|módulos]] mudam e como suas interfaces são modificadas** — não só contratos de API externos, mas as fronteiras internas entre módulos profundos da aplicação. Citando Kent Beck ("invista no design do sistema todos os dias"), o argumento é que ignorar essas fronteiras na spec é o que faz o "specs to code" desinvestir do design em vez de investir nele a cada mudança.

## Key Sources

- [[wiki/sources/formacao-ia-devs-aula-04-agentes-planejamento]]
- [[wiki/sources/formacao-ia-devs-aula-05-qa]]
- [[wiki/sources/fundamentos-de-software-importam-mais-que-nunca-na-era-da-ia]]
