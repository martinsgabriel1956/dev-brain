---
type: source
title: "TDD — Test-Driven Development"
aliases: ["test driven development", "red green refactor"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_file: /home/nemomartins/Documentos/new/dev-study/raw/tdd.md
source_url: ""
author: "tech-mentor-testing skill"
date_published: 2026-03-27
date_ingested: 2026-04-22
source_count: 0
tags: [testes, tdd, design, red-green-refactor, detroit, london]
skill: tech-mentor-testing
status: stable
---

# TDD — Test-Driven Development

## TL;DR

TDD é escrever o teste antes do código. O benefício central não é cobertura — é sentir o acoplamento antes de criá-lo. Ciclo: RED → GREEN → REFACTOR. Duas escolas: Detroit (inside-out, objetos reais) e London (outside-in, mocks como design tool).

## Claims Principais

| Claim | Confiança |
|---|---|
| TDD não garante boa arquitetura, mas garante que o código é testável | Alta |
| Sem o Refactor, TDD acumula débito técnico junto com os testes | Alta |
| Testar implementação (nome do método) em vez de comportamento = teste frágil | Alta |
| Mocks London podem mascarar integração quebrada | Alta |

## Conceitos Abordados

- [[tdd]] · [[test-doubles]] · [[bdd]] · [[piramide-de-testes]]
