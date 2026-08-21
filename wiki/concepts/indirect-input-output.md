---
type: concept
title: "Entrada e Saída Indireta (Indirect Input / Indirect Output)"
aliases: ["indirect input", "indirect output", "entrada indireta", "saída indireta", "control point", "observation point", "ponto de controle", "ponto de observação", "direct input", "entrada direta"]
date_created: 2026-08-21
date_updated: 2026-08-21
source_count: 1
tags: [testes, test-doubles, sut, doc, terminologia, xunit]
skill: tech-mentor-testing
status: stub
---

# Entrada e Saída Indireta (Indirect Input / Indirect Output)

Par de termos do vocabulário formal de [[wiki/entities/gerard-meszaros]] ([[wiki/sources/test-double-xunitpatterns-meszaros]]) que explica **por que** existem os cinco tipos de [[wiki/concepts/test-doubles|Test Double]] — o eixo é a direção do dado entre o **SUT** (*system under test*) e o **DOC** (*depended-on component*, a dependência real que o double substitui).

## As duas direções

- **Entrada indireta** (*indirect input*) — valor que o SUT **recebe** de um DOC e que afeta seu comportamento. Fonte primária: [[wiki/sources/indirect-input-xunitpatterns]]. Formas concretas: retorno de função, parâmetro de saída (out) atualizado, ou erro/exceção levantado pelo DOC.
- **Saída indireta** (*indirect output*) — chamada ou efeito que o SUT **dispara** sobre um DOC, observável de fora.

A contraparte de entrada indireta é a **entrada direta** (*direct input*): um valor passado explicitamente ao SUT pelo próprio teste (ex.: argumento de método), sem passar por nenhum DOC.

## Pontos de controle e de observação

Testar cada direção exige um ponto de acesso diferente "na parte de trás" do SUT:

| Direção | Ponto de acesso | Double típico |
|---|---|---|
| Entrada indireta | **control point** (ponto de controle) | [[wiki/concepts/test-doubles\|Stub]] — injeta o valor controlado |
| Saída indireta | **observation point** (ponto de observação) | [[wiki/concepts/test-doubles\|Spy ou Mock]] — registra ou verifica a chamada |

Esse eixo controle × observação é o mesmo já sintetizado em [[wiki/concepts/test-doubles]] a partir da fonte primária de Test Double — este conceito isola especificamente o vocabulário de entrada/saída, já que agora há uma fonte primária dedicada só a "indirect input" ([[wiki/sources/indirect-input-xunitpatterns]]).

## Por que a distinção importa

Sem esse vocabulário, é fácil descrever "mock" como "stub com asserção" — uma simplificação que a própria fonte primária rejeita (ver [[wiki/sources/test-double-xunitpatterns-meszaros]]). A distinção correta é: Stub controla **entrada** indireta; Mock/Spy observam **saída** indireta. É esse eixo que também organiza a distinção entre [[wiki/concepts/unit-test-solitario-vs-sociavel|estilo de teste London (mocka saída) e Detroit (usa objetos reais, stuba só entrada de I/O externo)]].

## Ver também

- [[wiki/concepts/test-doubles]] — taxonomia completa dos cinco tipos organizados por esse eixo
- [[wiki/concepts/unit-test-solitario-vs-sociavel]] — escolas de TDD mapeadas no mesmo eixo controle/observação
- [[wiki/concepts/teste-de-integracao-estreito-vs-amplo]] — narrow integration test depende de um double fiel o suficiente para as entradas indiretas que fornece

## Questões Abertas

- Os verbetes irmãos "indirect output", "control point", "observation point" e "direct input" do mesmo glossário xUnitPatterns.com ainda não têm fonte primária própria ingerida — só são conhecidos aqui por inferência a partir de [[wiki/sources/indirect-input-xunitpatterns]] e [[wiki/sources/test-double-xunitpatterns-meszaros]]. Candidatos a ingestão futura para fechar o vocabulário.

## Key Sources

- [[wiki/sources/indirect-input-xunitpatterns]] — fonte primária de "indirect input"
- [[wiki/sources/test-double-xunitpatterns-meszaros]] — vocabulário completo SUT/DOC/entrada-saída indireta/pontos de controle-observação
