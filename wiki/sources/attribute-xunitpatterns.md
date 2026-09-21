---
type: source
title: "Attribute (xUnitPatterns.com — Gerard Meszaros)"
aliases: ["attribute", "atributo", "xunit patterns glossary attribute"]
date_created: 2026-09-21
date_updated: 2026-09-21
source_file: /home/nemomartins/Documentos/new/dev-study/raw/attribute-xunitpatterns.md
source_url: "http://xunitpatterns.com/attribute.html"
author: "Gerard Meszaros"
date_published: 2003-01-01
date_ingested: 2026-09-21
source_count: 0
tags: [testes, junit, nunit, xunit, fonte-primaria, terminologia, glossario]
skill: tech-mentor-testing
status: stable
---

# Attribute (xUnitPatterns.com — Gerard Meszaros)

## TL;DR

Verbete curtíssimo do Glossário do xUnitPatterns.com que define **attribute**: "uma característica de algo". No xUnit, o termo carrega dois sentidos distintos e não relacionados entre si: (1) sinônimo de [[wiki/sources/annotation-xunitpatterns|annotation]] — é literalmente o nome que o **NUnit** usa para o mesmo mecanismo que o **JUnit** chama de annotation, como já registrado em [[wiki/sources/annotation-xunitpatterns]]; ou (2) sinônimo de **instance variable** — a variável de estado de um objeto. O verbete não elabora qual sentido se aplica em qual contexto; distinguir os dois cabe a quem lê o código.

---

## Afirmações Centrais

| Afirmação | Evidência | Fonte | Confiança |
|---|---|---|---|
| Attribute é "uma característica de algo" | "A characteristic of something." | fonte primária (Meszaros) | alta |
| No xUnit, attribute é uma annotation de classe ou método | "In xUnit it is either an annotation of a class or method" | fonte primária | alta |
| No xUnit, attribute também é sinônimo de instance variable | "...or a synonym for instance variable." | fonte primária | alta |

---

## Key Claims

### 1. Confirma, de fonte primária isolada, a equivalência annotation (JUnit) ↔ attribute (NUnit)
[[wiki/sources/annotation-xunitpatterns]] já registrava que "NUnit uses attributes" onde JUnit usa annotations, mas esse dado aparecia só de passagem, dentro do verbete dedicado a "annotation". Este verbete faz o caminho inverso — parte de "attribute" — e confirma formalmente que o termo, nesse primeiro sentido, é sinônimo funcional de annotation, fechando o par simétrico de definições entre os dois termos.

### 2. Um segundo sentido, sem relação com o primeiro: sinônimo de instance variable
O verbete lista, sem hierarquia entre eles, um segundo significado completamente distinto: "attribute" como sinônimo de **instance variable**. Esse uso é o sentido genérico de OO (uma característica/propriedade de um objeto, tipicamente armazenada como estado) — não específico de teste. Nenhuma fonte anterior da wiki havia isolado esse segundo sentido, embora "instância" e "variável de instância" já aparecessem de passagem em [[wiki/concepts/shared-fixture]] e [[wiki/concepts/test-method]] (a propósito do comportamento do NUnit 2.x/TestNG de reutilizar instância entre Test Methods).

### 3. Ambiguidade deliberada, sem desambiguação no próprio verbete
Diferente de "test fixture" (onde [[wiki/sources/test-fixture-xunitpatterns]] distingue explicitamente os múltiplos sentidos do termo e nomeia qual se aplica onde), o verbete de "attribute" apresenta os dois sentidos lado a lado sem indicar como o leitor deve escolher entre eles — a desambiguação fica implícita no contexto (se o attribute está decorando uma classe/método, é annotation; se está guardando estado de um objeto, é instance variable).

---

## Entidades Mencionadas

- [[wiki/entities/junit]] — implicitamente referenciado como o framework que usa "annotation" em vez de "attribute" para o primeiro sentido
- [[wiki/entities/nunit]] — framework que usa literalmente o termo "attribute" para o mecanismo de marcação (primeiro sentido)
- [[wiki/entities/gerard-meszaros]] — autor do verbete; mesma fonte primária do catálogo já usada para dezenas de outros termos de glossário já ingeridos

## Conceitos Tocados

- [[wiki/concepts/tdd|Xunit]] — attribute como um dos dois nomes possíveis (com annotation) para o mecanismo de marcação de Testcase Classes e Test Methods

## Questões Abertas

- ~~O verbete não define **instance variable** separadamente~~ — resolvido: [[wiki/sources/instance-variable-xunitpatterns]] ingerida em 2026-09-21, dando fonte primária isolada ao termo.
- ~~O sentido "annotation de classe" não tinha fonte primária isolada nomeando o termo genérico~~ — resolvido: [[wiki/sources/class-attribute-xunitpatterns]] ingerida em 2026-09-21, restringindo o primeiro sentido ao nível de classe.
- ~~O sentido "annotation de método" não tinha fonte primária isolada nomeando o termo genérico~~ — resolvido: [[wiki/sources/method-attribute-xunitpatterns]] ingerida em 2026-09-21, restringindo o primeiro sentido ao nível de método. Com isso, os dois pares (class attribute / method attribute) estão fechados.
- Não há indicação no verbete de que frameworks existem além de JUnit/NUnit usando um ou outro termo — permanece assumido que a distinção é binária (JUnit=annotation, NUnit=attribute), sem verificação contra outros membros da família xUnit já ingeridos (RSpec, TestNG, SUnit).

---

## Citações Relevantes

> "A characteristic of something. In xUnit it is either an annotation of a class or method or a synonym for instance variable."

*(Tradução completa em `raw/attribute-xunitpatterns.md`.)*
