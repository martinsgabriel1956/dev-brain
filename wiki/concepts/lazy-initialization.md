---
type: concept
title: "Lazy Initialization"
aliases: ["inicialização lazy", "lazy loading", "virtual proxy"]
date_created: 2026-05-01
date_updated: 2026-06-05
source_count: 2
tags: [performance, design-patterns, proxy]
skill: tech-mentor-backend
status: stub
---

## Definição

Técnica que adia a criação ou inicialização de um objeto até o momento em que ele é realmente necessário. Evita custo de inicialização quando o objeto pode nunca ser usado.

## Relação com Proxy

O **Virtual Proxy** é uma variação do [[proxy-pattern]] que implementa lazy initialization: o proxy age como se fosse o objeto real, mas só cria a instância custosa quando o primeiro método é chamado.

## Key Sources

- [[wiki/sources/design-pattern-proxy]]
