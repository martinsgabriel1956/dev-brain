---
type: source
title: "Unit Test (xUnitPatterns.com — Gerard Meszaros)"
aliases: ["unit test", "teste de unidade", "teste unitário", "developer test", "programmer test", "xunit patterns glossary unit test"]
date_created: 2026-08-31
date_updated: 2026-08-31
source_file: /home/nemomartins/Documentos/new/dev-study/raw/unit-test-xunitpatterns.md
source_url: "http://xunitpatterns.com/unit%20test.html"
author: "Gerard Meszaros"
date_published: 2003-01-01
date_ingested: 2026-08-31
source_count: 0
tags: [testes, unit-test, sut, customer-test, xp, xunit, fonte-primaria, terminologia]
skill: tech-mentor-testing
status: stable
---

# Unit Test (xUnitPatterns.com — Gerard Meszaros)

## TL;DR

Verbete curto do Glossário do catálogo xUnitPatterns.com que define formalmente **unit test**: o que classifica um teste como "de unidade" não é uma propriedade do teste em si, mas o tamanho do [[wiki/sources/sut-xunitpatterns|SUT]] que ele exercita — "um subconjunto muito pequeno do sistema geral", possivelmente irreconhecível para quem não constrói o software. A fonte formaliza o contraste com **customer test** (derivado dos requisitos, verificável pelo cliente) e fixa que, em **eXtreme Programming**, unit test também é chamado de **developer test** ou **programmer test**. Fecha, junto com [[wiki/sources/sut-xunitpatterns]], a definição do termo mais citado — mas até agora nunca formalmente ingerido — em toda a wiki de testes.

---

## Afirmações Centrais

| Afirmação | Evidência | Fonte | Confiança |
|---|---|---|---|
| Unit test verifica o comportamento de uma pequena parte do sistema geral | "A test that verifies the behavior of some small part of the overall system" | fonte primária (Meszaros) | alta |
| O que define "unidade" é o tamanho do SUT, não uma propriedade do teste — pode ser irreconhecível a quem não constrói o software | "What makes a test a unit test is that the system under test (SUT) is a very small subset of the overall system and may be unrecognizable to someone who is not involved in building the software" | fonte primária | alta |
| O SUT real pode ser um único objeto ou método, consequência de decisões de design, ainda que rastreável a requisitos funcionais | "The actual SUT may be as small as a single object or method that is a consequence of one or more design decisions although its behavior may also be traced back to some aspect of the functional requirements" | fonte primária | alta |
| Unit tests não precisam ser legíveis/verificáveis pelo cliente; customer test é o oposto — derivado dos requisitos e verificável pelo cliente | "There is no need for unit tests to be readable, recognizable or verifiable by the customer or business domain expert. Contrast this with a customer test which is derived almost entirely from the requirements and which should be verifiable by the customer" | fonte primária | alta |
| Em eXtreme Programming, unit tests também são chamados de developer tests ou programmer tests | "In eXtreme Programming, unit tests are also called developer tests or programmer tests" | fonte primária | alta |

---

## Key Claims

### 1. "Unidade" é definida pelo tamanho do SUT, não por uma técnica de teste
A fonte amarra a definição de unit test diretamente ao vocabulário já formalizado em [[wiki/sources/sut-xunitpatterns]]: o que torna um teste "de unidade" é exclusivamente o tamanho do SUT que ele exercita ser "muito pequeno" — não o uso de doubles, não a ausência de I/O, não a velocidade de execução. Isso é uma correção de precisão importante: a wiki já discutia [[wiki/concepts/unit-test-solitario-vs-sociavel|solitário vs. sociável]] como variação *dentro* de unit test, mas nunca tinha a definição-raiz que ambas as variações compartilham (SUT pequeno) citada de fonte primária.

### 2. Unit test pode ser irreconhecível para quem não constrói o software — critério de opacidade
Frase notável e nunca antes registrada na wiki: um bom unit test pode legitimamente testar algo tão granular (um método privado, uma decisão de design interna) que seria "irreconhecível" para alguém fora da construção do software. Isso é o oposto exato do critério de customer test (verificável pelo cliente) — os dois termos são definidos um em função do outro, por contraste direto.

### 3. Unit test em XP tem dois sinônimos historicamente atestados: developer test e programmer test
A fonte cita a nomenclatura de **eXtreme Programming**: "developer test" e "programmer test" são sinônimos históricos de unit test, não termos concorrentes com significado distinto. Nenhuma menção prévia a esses dois termos existia na wiki, mesmo em [[wiki/concepts/extreme-programming]], que já documenta TDD como prática central de XP sem citar esse detalhe de nomenclatura.

---

## Entidades Mencionadas

- [[wiki/entities/gerard-meszaros]] — autor do verbete; mesma fonte primária do catálogo já usada para [[wiki/sources/sut-xunitpatterns]], [[wiki/sources/test-double-xunitpatterns-meszaros]] e demais verbetes do glossário
- [[wiki/entities/kent-beck]] — criador da eXtreme Programming, contexto onde "developer test"/"programmer test" são usados como sinônimos de unit test

## Conceitos Tocados

- [[wiki/concepts/unit-test-solitario-vs-sociavel]] — ganha a definição-raiz (SUT pequeno) que precede a distinção solitário/sociável
- [[wiki/concepts/extreme-programming]] — ganha os sinônimos "developer test"/"programmer test", não documentados antes
- [[wiki/concepts/piramide-de-testes]] — a camada "Unitário" da pirâmide corresponde exatamente a este verbete

## Questões Abertas

- **"customer test" ainda não tem verbete de glossário isolado próprio** — conhecido até agora só por contraste dentro deste verbete e de [[wiki/sources/sut-xunitpatterns]]. Candidato natural para fechar o par de termos, junto com "acceptance test" e "user story", já listados no índice de Glossário do site mas não ingeridos.
- A fonte não distingue explicitamente as escolas London/Detroit (solitário/sociável) — esse refinamento continua vindo só de Fowler, via [[wiki/sources/integration-test-martin-fowler]], já registrado em [[wiki/concepts/unit-test-solitario-vs-sociavel]].

---

## Citações Relevantes

> "A test that verifies the behavior of some small part of the overall system. What makes a test a unit test is that the system under test (SUT) is a very small subset of the overall system and may be unrecognizable to someone who is not involved in building the software."

> "The actual SUT may be as small as a single object or method that is a consequence of one or more design decisions although its behavior may also be traced back to some aspect of the functional requirements."

> "There is no need for unit tests to be readable, recognizable or verifiable by the customer or business domain expert. Contrast this with a customer test which is derived almost entirely from the requirements and which should be verifiable by the customer."

> "In eXtreme Programming, unit tests are also called developer tests or programmer tests."

*(Tradução completa em `raw/unit-test-xunitpatterns.md`.)*
