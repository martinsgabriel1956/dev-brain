---
type: concept
title: "Flyweight Pattern"
aliases: ["flyweight", "peso mosca"]
date_created: 2026-05-05
date_updated: 2026-05-05
source_count: 1
tags: [design-patterns, structural, flyweight, gof, performance, memoria]
skill: tech-mentor-backend
status: stub
---

# Flyweight Pattern

Padrão [[structural-patterns|estrutural]] que permite acomodar mais objetos na quantidade disponível de RAM ao compartilhar partes comuns do estado entre múltiplos objetos, em vez de manter todos os dados em cada objeto.

## Distinção do Facade

- **Flyweight** — muitos objetos pequenos compartilhando estado intrínseco
- **[[facade-pattern]]** — um único objeto que representa um subsistema inteiro

## Quando usar

- Quando a aplicação precisa suportar um número enorme de objetos similares
- Quando isso causa problemas de memória
- Exemplos: caracteres em um editor de texto, partículas em um jogo, tiles em um mapa

## Estado intrínseco vs extrínseco

- **Intrínseco** — compartilhado, imutável, armazenado no flyweight
- **Extrínseco** — único por contexto, passado pelo cliente na chamada

## Key Sources

- [[sources/design-pattern-facade]] — mencionado nas relações com outros padrões
