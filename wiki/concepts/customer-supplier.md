---
type: concept
title: "Customer/Supplier"
aliases: ["customer supplier", "cliente-fornecedor"]
date_created: 2026-09-30
date_updated: 2026-09-30
source_count: 1
tags: [ddd, context-map, integracao]
skill: tech-mentor-backend
status: stub
---

# Customer/Supplier

## TL;DR

Padrão de integração entre bounded contexts com **dependência hierárquica**: o contexto *supplier* (upstream) fornece o modelo e o *customer* (downstream) o consome ([[wiki/sources/bounded-context-contextos-delimitados-bernardo-lobato]]). Ver [[wiki/concepts/context-map]]. Na skill [skill: tech-mentor-backend], o poder está no Supplier; o Customer adapta-se ou negocia mudanças. Contraste com [[wiki/concepts/conformist]].

## Key Sources

- [[wiki/sources/bounded-context-contextos-delimitados-bernardo-lobato]] — citado como dependência hierárquica entre contextos (uma linha)
