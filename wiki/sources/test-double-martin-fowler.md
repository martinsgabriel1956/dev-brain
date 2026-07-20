---
type: source
title: "Test Double (Martin Fowler)"
aliases: ["test double bliki", "dublê de teste fowler", "meszaros test double taxonomy"]
date_created: 2026-07-19
date_updated: 2026-07-19
source_file: /home/nemomartins/Documentos/new/dev-study/raw/test-double-martin-fowler.md
source_url: "https://martinfowler.com/bliki/TestDouble.html"
author: "Martin Fowler"
date_published: 2006-01-17
date_ingested: 2026-07-19
source_count: 0
tags: [testes, test-doubles, mock, stub, fake, spy, dummy, martin-fowler, gerard-meszaros]
skill: tech-mentor-testing
status: stable
---

# Test Double (Martin Fowler)

## TL;DR

Fonte primária do termo "Test Double" — bliki entry curto de 2006 em que Fowler relata o vocabulário que **Gerard Meszaros** estava criando para o livro *xUnit Test Patterns*: Dummy, Fake, Stub, Spy e Mock. Fowler cunha/divulga o termo guarda-chuva "Test Double" (analogia a dublê de cinema — "stunt double"), mas a taxonomia dos cinco tipos é atribuída explicitamente a Meszaros, não inventada por Fowler.

## Key Claims

- **"Test Double" é termo genérico para qualquer objeto que substitui um objeto de produção com propósito de teste** — analogia direta a dublê de cinema (stunt double). → [[wiki/concepts/test-doubles]]
- **Autoria da taxonomia de cinco tipos é de Gerard Meszaros**, não de Fowler — Fowler relata um vocabulário que Meszaros desenvolveu para o livro *xUnit Test Patterns* (2007), resolvendo a inconsistência de nomes que já existia na comunidade de testes. → [[wiki/entities/gerard-meszaros]]
- **Dummy**: passado adiante mas nunca usado — preenche listas de parâmetros.
- **Fake**: implementação funcional real mas com atalho que a torna inadequada para produção (ex.: `InMemoryTestDatabase`).
- **Stub**: respostas prontas ("canned answers") às chamadas do teste, sem responder a nada fora do programado.
- **Spy**: stub que também registra informação sobre como foi chamado (ex.: contar e-mails enviados).
- **Mock**: pré-programado com expectativas que especificam as chamadas esperadas; pode lançar exceção em chamada inesperada e é verificado na validação para confirmar que recebeu todas as chamadas esperadas.
- **Leitura complementar apontada pelo próprio Fowler**: o artigo "Mocks Aren't Stubs" expande a discussão sobre quando cada tipo de double é apropriado.

## Entities

[[wiki/entities/martin-fowler]] · [[wiki/entities/gerard-meszaros]]

## Concepts

[[wiki/concepts/test-doubles]] · [[wiki/concepts/tdd]] · [[wiki/concepts/piramide-de-testes]] · [[wiki/concepts/contract-testing]] · [[wiki/concepts/teste-de-integracao-estreito-vs-amplo]]

## Contradição corrigida na wiki

Antes desta ingestão, [[wiki/concepts/test-doubles]] atribuía a cunhagem do termo "TestDouble" diretamente a [[wiki/entities/martin-fowler]] sem distinguir o termo guarda-chuva (de fato divulgado por Fowler no bliki) da taxonomia interna dos cinco tipos (de autoria de [[wiki/entities/gerard-meszaros]], relatada por Fowler). Corrigido nesta ingestão — ver seção correspondente em `wiki/concepts/test-doubles.md`.

## Open Questions

- O livro *xUnit Test Patterns* (Meszaros, 2007) em si nunca foi ingerido como fonte primária — só é conhecido nesta wiki via referência de terceiros (este bliki e a skill `tech-mentor-testing`). Se surgir a chance de acessar o livro ou resumos mais extensos dele, vale revisitar a entity de Meszaros.
- O artigo "Mocks Aren't Stubs" (também de Fowler, referenciado como leitura complementar aqui) ainda não foi ingerido como fonte própria na wiki — candidato natural a próxima ingestão sobre o mesmo tema.

## Raw Quotes

> "Test Double is a generic term for any case where you replace a production object for testing purposes."

> "Mocks are pre-programmed with expectations which form a specification of the calls they are expected to receive. They can throw an exception if they receive a call they don't expect and are checked during verification to ensure they got all the calls they were expecting."

*(Tradução completa em `raw/test-double-martin-fowler.md`; para o texto exato em inglês, ver `source_url`.)*
