---
type: source
title: "Test Doubles"
aliases: ["mock stub fake spy dummy", "dublê de teste"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_file: /home/nemomartins/Documentos/new/dev-study/raw/test-doubles.md
source_url: ""
author: "tech-mentor-testing skill"
date_published: 2026-03-27
date_ingested: 2026-04-22
source_count: 0
tags: [testes, test-doubles, mock, stub, fake, spy, dummy, msw]
skill: tech-mentor-testing
status: stable
---

# Test Doubles

## TL;DR

Taxonomia de Gerard Meszaros (xUnit Test Patterns, 2007): Dummy, Stub, Fake, Spy, Mock. Regra de ouro: prefira Fake sobre Mock. Mock acopla teste à implementação — renomear método quebra o teste sem o comportamento ter mudado. Mocks excessivos (5+) são code smell de acoplamento alto.

## Claims Principais

| Claim | Confiança |
|---|---|
| Fake é o melhor tipo para repositórios — reutilizável, sem acoplamento à implementação | Alta |
| Mock acopla teste ao nome do método — frágil a refactoring | Alta |
| Mocks excessivos indicam acoplamento alto — refatore antes de continuar | Alta |
| MSW substitui APIs externas no nível da rede — código não sabe que está sendo interceptado | Alta |

## Conceitos Abordados

- [[test-doubles]] · [[tdd]] · [[piramide-de-testes]] · [[contract-testing]]
