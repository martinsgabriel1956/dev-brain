---
type: entity
title: "Clojure"
aliases: ["clj", "clojurescript", "cljs"]
date_created: 2026-05-31
date_updated: 2026-05-31
source_count: 1
tags: [clojure, lisp, jvm, programacao-funcional, imutabilidade]
skill: tech-mentor-backend
status: draft
---

# Clojure

## TL;DR

Dialeto Lisp funcional rodando na JVM, criado por [[rich-hickey]] em 2007. [[Imutabilidade]] por default em todas as estruturas de dados. Acesso ao ecossistema Java completo. Linguagem principal do [[nubank]].

## Características

- **Imutabilidade nativa** — todas as estruturas de dados são persistentes (imutáveis)
- **JVM** — acesso ao ecossistema Java maduro sem reinventar a roda
- **REPL-driven development** — desenvolvimento interativo
- **Homoiconicidade** — código é dado (Lisp)
- **Concorrência** — atoms, refs, agents para gerenciar estado mutável quando necessário

## Por que o Nubank Escolheu

1. [[Programacao-funcional|Programação funcional]] nativa — elimina [[complexidade-acidental]]
2. **Ecossistema JVM** — bibliotecas Java maduras disponíveis imediatamente
3. **[[Imutabilidade]]** por default — alinha com princípios do [[event-sourcing]]
4. Criado pelo mesmo autor do [[datomic]] ([[rich-hickey]]) — integração natural

## Ecossistema JVM como Vantagem

> *"Having to roll all of your own libraries to do basic things would have been an unbelievable detour from our core mission."* — Nubank Engineer

A JVM oferece bibliotecas para criptografia, networking, serialização, logging e muito mais — tudo battle-tested e maduro.

## Key Sources

- [[wiki/sources/nubank-clojure-datomic-event-sourcing]]
