---
type: source
title: "Test (xUnitPatterns.com — Gerard Meszaros)"
aliases: ["test", "teste", "test case", "caso de teste", "xunit patterns glossary test"]
date_created: 2026-08-31
date_updated: 2026-09-02
source_file: /home/nemomartins/Documentos/new/dev-study/raw/test-xunitpatterns.md
source_url: "http://xunitpatterns.com/test.html"
author: "Gerard Meszaros"
date_published: 2003-01-01
date_ingested: 2026-08-31
source_count: 1
tags: [testes, sut, test-case, xunit, fonte-primaria, terminologia]
skill: tech-mentor-testing
status: stable
---

# Test (xUnitPatterns.com — Gerard Meszaros)

## TL;DR

Verbete mais curto e mais básico do Glossário do catálogo xUnitPatterns.com: define o próprio termo **test**. Um procedimento — manual ou automatizado — usado para verificar que o [[wiki/sources/sut-xunitpatterns|SUT]] está se comportando como esperado; frequentemente chamado de **test case**. Fecha a base da hierarquia de termos já ingerida (SUT → unit test → test) com a definição mais elementar de todas: o que é, afinal, um teste.

---

## Afirmações Centrais

| Afirmação | Evidência | Fonte | Confiança |
|---|---|---|---|
| Um teste é um procedimento, manual ou automatizado, usado para verificar que o SUT se comporta como esperado | "A procedure, whether manually executed or automated, that can be used to verify that the system under test (SUT) is behaving as expected" | fonte primária (Meszaros) | alta |
| Um teste é frequentemente chamado de "test case" | "Often called a test case" | fonte primária | alta |

---

## Key Claims

### 1. Teste manual e automatizado são a mesma categoria conceitual
A definição não distingue teste manual de teste automatizado como coisas diferentes — ambos são "um procedimento... que verifica o SUT". A automação (o próprio foco do catálogo xUnitPatterns.com e dos frameworks xUnit) é uma característica de **execução**, não uma categoria à parte do conceito de teste. Isso é consistente com [[wiki/concepts/piramide-de-testes]], onde as camadas descritas já pressupõem testes automatizados sem precisar reafirmar essa distinção.

### 2. "Test" e "test case" são sinônimos na fonte, não termos hierárquicos
Muitas convenções de mercado tratam "test case" como um documento/especificação e "test" (ou "test method") como sua implementação em código — uma hierarquia de um-para-um ou um-para-muitos. Meszaros não faz essa distinção aqui: trata os dois termos como equivalentes ("often called a test case"), reforçando que o vocabulário do catálogo é pragmático e não introduz uma camada extra de terminologia entre "teste" e sua implementação.

---

## Entidades Mencionadas

- [[wiki/entities/gerard-meszaros]] — autor do verbete; mesma fonte primária do catálogo já usada para [[wiki/sources/sut-xunitpatterns]], [[wiki/sources/unit-test-xunitpatterns]] e demais verbetes do glossário

## Conceitos Tocados

- [[wiki/concepts/criterios-de-bom-teste]] — a definição-raiz de "o que é um teste" precede os cinco critérios de qualidade já documentados ali
- [[wiki/concepts/piramide-de-testes]] — todas as camadas da pirâmide são, na base, instâncias deste conceito genérico

## Questões Abertas

- ~~"test case" não recebe verbete próprio no índice de Glossário do site~~ — **corrigido**: recebe, sim, verbete próprio. Ver [[wiki/sources/test-case-xunitpatterns]], que confirma o sinônimo genérico e acrescenta um segundo sentido técnico do XUnit (Testcase Class como Test Suite Factory).
- **"test suite" e "test run"**, termos irmãos que agregam testes individuais, seguem sem fonte primária isolada ingerida — candidatos naturais para fechar a base do vocabulário. ~~"customer test" e "acceptance test" também seguiam sem fonte isolada~~ — **parcialmente corrigido**: ver [[wiki/sources/customer-test-xunitpatterns]]; "acceptance test" permanece sem fonte isolada.
- ~~Quem constrói o teste não tem papel formalizado no glossário~~ — **corrigido**: ver [[wiki/sources/test-automater-xunitpatterns]], que isola o papel de "test automater" (quem constrói/automatiza os testes definidos aqui) e o distingue do "subject matter expert" (quem decide o que testar). Restam ainda "test maintainer", "test reader" e "test stripper" como papéis irmãos não ingeridos.

---

## Citações Relevantes

> "A procedure, whether manually executed or automated, that can be used to verify that the system under test (SUT) is behaving as expected. Often called a test case."

*(Tradução completa em `raw/test-xunitpatterns.md`.)*
