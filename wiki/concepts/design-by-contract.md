---
type: concept
title: "Design by Contract"
aliases: ["DbC", "projeto por contrato", "programação por contrato"]
date_created: 2026-09-23
date_updated: 2026-09-23
source_count: 1
tags: [design-by-contract, oop, corretude, bertrand-meyer, eiffel, contratos]
skill: tech-mentor-backend
status: draft
---

## TL;DR

Abordagem de projeto em que cada módulo/rotina declara explicitamente o que **exige** (pré-condições), o que **garante** (pós-condições) e o que **sempre se mantém** (invariantes). Programa correto = faz exatamente o que o contrato diz. Criado por [[wiki/entities/bertrand-meyer]] em [[wiki/entities/eiffel]]. [[wiki/sources/design-by-contract-video]]

## Ideia central

Analogia com contrato humano (ex.: contrato de trabalho): direitos e responsabilidades das duas partes; se ambas cumprem, ambas ganham. Em software, as partes são **chamador** e **rotina chamada**; ver [[wiki/concepts/precondicao-poscondicao-invariante]] para a divisão de responsabilidades. Violação aciona um "remédio" combinado (tipicamente exceção/asserção). [[wiki/sources/design-by-contract-video]]

## Suporte por linguagem

- **Nativo:** Eiffel (origem); Clojure com pré/pós-condições ([[wiki/entities/clojure]]). [[wiki/sources/design-by-contract-video]]
- **Parcial/nenhum:** simular com asserções, guard clauses e exceções; ou, no mínimo, **documentar o contrato em comentário** antes do método. [[wiki/sources/design-by-contract-video]]

## Distinções

- **≠ contrato de API (OpenAPI/HTTP):** este descreve a interface entre serviços; DbC descreve o comportamento correto de uma rotina. Ver [[wiki/concepts/contract-testing]]. [[wiki/sources/design-by-contract-video]]
- **Relação com testes:** o autor aponta [[wiki/concepts/property-based-testing]] como técnica próxima (invariantes viram propriedades).
- **Relação com [[wiki/concepts/fail-fast]]:** pré-condição violada = falhar cedo na fronteira, em vez de propagar dado inválido. [inferência da wiki, não afirmado na fonte]

## Conexões com SOLID (fora da fonte)

[external] Na teoria de Meyer, a substituição de subclasses (ver [[wiki/concepts/liskov-substitution-principle]]) é formulada em termos de contrato: subtipo não pode **fortalecer** pré-condições nem **enfraquecer** pós-condições. A fonte ingerida só menciona que Meyer criou o [[wiki/concepts/open-closed-principle]]; esta conexão com LSP vem de conhecimento geral (Meyer, *Object-Oriented Software Construction*) e não foi verificada em fonte primária nesta ingestão.

## Key Sources

- [[wiki/sources/design-by-contract-video]]
