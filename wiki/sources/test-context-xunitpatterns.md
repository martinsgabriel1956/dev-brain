---
type: source
title: "Test Context (xUnitPatterns.com — Gerard Meszaros)"
aliases: ["test context", "contexto de teste", "xunit patterns glossary test context"]
date_created: 2026-09-04
date_updated: 2026-09-04
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/test-context-xunitpatterns.md
source_url: "http://xunitpatterns.com/test%20context.html"
author: "Gerard Meszaros"
date_published: 2003-01-01
date_ingested: 2026-09-04
source_count: 0
tags: [testes, test-fixture, test-context, rspec, xunit, fonte-primaria, terminologia]
skill: tech-mentor-testing
status: stable
---

# Test Context (xUnitPatterns.com — Gerard Meszaros)

## TL;DR

Verbete de glossário curto do catálogo xUnitPatterns.com dedicado ao termo **test context**, já citado como sinônimo de [[wiki/concepts/tdd|test fixture]] em [[wiki/sources/test-fixture-xunitpatterns]] e [[wiki/sources/fixture-setup-xunitpatterns]], mas agora com fonte primária própria e um dado novo: é o **RSpec** que usa "context" como nome literal para o que o xUnit chama de test fixture. A fonte também traz um exemplo de código inédito na wiki — um fixture de um conjunto `fruits`, ilustrando as três fases Fixture/Exercise/Verify — e uma observação de design que nenhuma fonte anterior da série havia registrado explicitamente: **como se escolhe construir o fixture tem ramificações de longo alcance** sobre toda a escrita e manutenção de testes.

---

## Afirmações Centrais

| Afirmação | Evidência | Fonte | Confiança |
|---|---|---|---|
| Test context é tudo que o SUT precisa ter em vigor para ser exercitado com o propósito de verificar seu comportamento | "everything a system under test (SUT) needs to have in place in order to exercise it for the purpose of verifying its behavior" | fonte primária (Meszaros) | alta |
| RSpec chama o test fixture (em xUnit) de "context" | "For this reason RSpec calls the test fixture (in xUnit) a 'context'" | fonte primária | alta |
| Como se escolhe construir o fixture tem ramificações de longo alcance sobre toda a escrita e manutenção de testes | "how we choose to construct the fixture has very far-reaching ramifications on all aspects of test writing and maintenance" | fonte primária | alta |

---

## Key Claims

### 1. RSpec é a primeira ferramenta fora da família xUnit citada nominalmente na série de glossário
Todas as fontes anteriores da série xUnitPatterns.com citam apenas frameworks da própria família xUnit (JUnit, SUnit) ou ferramentas de mock (JMock). Este verbete é o primeiro a nomear explicitamente uma ferramenta **fora** da linhagem xUnit — o [[wiki/entities/rspec|RSpec]], framework de BDD para Ruby — e a razão do nome "context" que ele usa: é literalmente a mesma ideia de test fixture, só com rótulo diferente. Não existia entidade própria para RSpec na wiki antes desta ingestão.

### 2. Exemplo de código concreto do Four-Phase Test com um fixture mínimo
A fonte ilustra a definição com um exemplo minimalista — fixture de um conjunto `fruits = {apple, orange, pear}`, exercise removendo `orange`, verify checando `{apple, pear}` — reforçando de forma concreta a estrutura Fixture → Exercise → Verify já citada em [[wiki/sources/test-fixture-xunitpatterns]] (Four-Phase Test). Nenhuma fonte anterior da série trouxe um exemplo de código; esta é a primeira.

### 3. A forma de construir o fixture como decisão de design com "ramificações de longo alcance"
O verbete fecha com uma observação que nenhuma fonte anterior da série havia tornado explícita: a **maneira** como o fixture é construído (inline no teste, via factory, via builder, etc.) não é um detalhe cosmético — tem consequências duradouras sobre a legibilidade e manutenção da suíte de testes. É uma ponte direta para os padrões de [[wiki/concepts/criterios-de-bom-teste]] sobre legibilidade/manutenibilidade de testes, mas o verbete não detalha quais técnicas de construção são preferíveis — só afirma que a escolha importa.

---

## Entidades Mencionadas

- [[wiki/entities/gerard-meszaros]] — autor do verbete; mesma fonte primária do catálogo já usada para [[wiki/sources/test-fixture-xunitpatterns]], [[wiki/sources/fixture-setup-xunitpatterns]] e demais verbetes do glossário
- **RSpec** — citado nominalmente como a ferramenta que nomeia o test fixture de "context"; sem página própria na wiki ainda (candidato a stub futuro se aparecer fonte com mais profundidade)

## Conceitos Tocados

- [[wiki/concepts/test-doubles]] — test context/fixture é o "palco" onde Test Doubles entram durante a fixture setup; esta fonte acrescenta o sinônimo usado pelo RSpec
- [[wiki/concepts/indirect-input-output]] — test fixture é o produto coletivo da fase de fixture setup, onde control points entram em cena
- [[wiki/concepts/piramide-de-testes]] — a estrutura Fixture/Exercise/Verify vale em qualquer camada da pirâmide, exemplificada aqui com um caso mínimo
- [[wiki/concepts/criterios-de-bom-teste]] — a observação de que a forma de construir o fixture tem ramificações de longo alcance conecta diretamente com os critérios de legibilidade/manutenibilidade já discutidos ali
- [[wiki/concepts/tdd]] — Four-Phase Test como estrutura formal por trás do ciclo RED-GREEN-REFACTOR

## Questões Abertas

- ~~**RSpec não tem página própria na wiki.**~~ Resolvida em 2026-09-04: [[wiki/sources/rspec-xunitpatterns]] é o verbete de glossário dedicado ao framework, agora com página própria em [[wiki/entities/rspec]].
- A fonte não detalha **quais** técnicas de construção do fixture são preferíveis (inline vs. factory vs. builder) — apenas afirma que a escolha "tem ramificações de longo alcance", sem elaborar. Fica em aberto para uma fonte futura sobre Test Data Builders ou Object Mother.
- Sem contradição com o resto da wiki — a fonte confirma e nomeia com precisão nova (RSpec) uma equivalência que já era tratada como fato em [[wiki/sources/test-fixture-xunitpatterns]] ("some people call this the test context").

---

## Citações Relevantes

> "A test context is everything a system under test (SUT) needs to have in place in order to exercise it for the purpose of verifying its behavior. For this reason RSpec calls the test fixture (in xUnit) a 'context'."

> "In this example, the fixture is comprised of a single set and it is created directly in the test. But how we choose to construct the fixture has very far-reaching ramifications on all aspects of test writing and maintenance."

*(Tradução completa em `raw/test-context-xunitpatterns.md`.)*
