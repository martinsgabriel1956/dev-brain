---
type: source
title: "Sete Padrões de Design de Software"
aliases: ["7 design patterns", "GoF patterns intro"]
date_created: 2026-05-05
date_updated: 2026-05-05
source_count: 0
tags: [design-patterns, gof, creational, structural, behavioral, singleton, builder, factory, facade, adapter, strategy, observer]
skill: tech-mentor-backend
status: stable
source_file: /home/nemomartins/Documentos/new/dev-study/raw/sete-padroes-de-design-de-software.md
source_url: ""
author: "Forest (YouTube)"
date_published: 2026-05-05
date_ingested: 2026-05-05
---

# Sete Padrões de Design de Software

Vídeo do canal Forest (YouTube) que apresenta 7 dos 23 padrões GoF com exemplos TypeScript práticos. Cobre os três grupos: criacionais, estruturais e comportamentais.

## TL;DR

Design patterns são soluções para problemas recorrentes de programação, independente de linguagem. Os 23 padrões [[gang-of-four]] se dividem em [[creational-patterns]], [[structural-patterns]] e [[behavioral-patterns]]. Este source cobre 7 dos mais usados na prática cotidiana.

## Padrões Cobertos

### Criacionais

**[[singleton-pattern]]** — garante uma única instância global. Analogia: logger centralizado. Trade-off principal: difícil de testar e é essencialmente uma variável global glorificada. Use apenas quando a unicidade é genuinamente necessária (pool de conexões, logger).

**[[builder-pattern]]** — constrói objetos complexos passo a passo via method chaining. Resolve o problema de construtores com muitos parâmetros opcionais. Código resultante lê como linguagem natural.

**[[factory-pattern]]** — centraliza a lógica de criação de objetos. Elimina `new` espalhado pelo código com condicionais repetidas. Toda lógica de criação fica em um lugar; adicionar um novo tipo exige mudar só a factory.

### Estruturais

**[[facade-pattern]]** — interface simplificada sobre subsistemas complexos. Analogia: botão "comprar agora" que esconde fraud check, inventário, pagamento e shipping. É basicamente encapsulamento bem aplicado. Risco: virar um [[god-object]] se não houver disciplina.

**[[adapter-pattern]]** — compatibiliza interfaces incompatíveis. Analogia: adaptador de tomada. Caso clássico: API de terceiros que retorna Celsius/km, app que espera Fahrenheit/mph. Isola lógica de conversão em um único lugar.

### Comportamentais

**[[strategy-pattern]]** — encapsula algoritmos intercambiáveis em classes separadas. Elimina `if/else` crescente para variações do mesmo comportamento. Segue o [[open-closed-principle]]: novas estratégias sem tocar código existente. Declarado pelo autor como "o melhor padrão de todos".

**[[observer-pattern]]** — objetos se inscrevem para serem notificados de eventos em outros objetos. Analogia: inscrição + sino no YouTube. Base de sistemas event-driven. Risco: event callback hell se abusado (evento A dispara B que dispara C...).

## Citações Relevantes

> "A Singleton is basically just a glorified global variable."

> "Always use a Strategy Pattern. If you take anything from this video, take that."

> "You're probably using facades all the time without realizing it — think of `fetch()`."

## Conexões

- [[gang-of-four]] — livro de 1994, 23 padrões, base de toda a discussão
- [[open-closed-principle]] — Strategy pattern como aplicação direta
- [[creational-patterns]] — Singleton, Builder, Factory
- [[structural-patterns]] — Facade, Adapter
- [[behavioral-patterns]] — Strategy, Observer
- [[god-object]] — anti-pattern que Facade pode virar se mal usado

## Questões em Aberto

- O vídeo não cobre Decorator, Proxy, Command, Template Method, Chain of Responsibility — todos igualmente relevantes segundo a referência `design-patterns.md` da skill.
- Singleton em ambientes multi-thread exige double-checked locking ou equivalente — não coberto no vídeo.
