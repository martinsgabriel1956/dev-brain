---
type: source
title: "[UTwHCM] — Unit Testing With Hand Crafted Mocks (xUnitPatterns.com — Gerard Meszaros, citando Sven Gorts)"
aliases: ["UTwHCM", "unit testing with hand crafted mocks", "hand-built test double reference", "sven gorts mocks"]
date_created: 2026-09-04
date_updated: 2026-09-04
source_file: /home/nemomartins/Documentos/new/dev-study/raw/utwhcm.md
source_url: "http://xunitpatterns.com/UTwHCM.html"
author: "Gerard Meszaros (verbete de referência); Sven Gorts (autor do artigo original citado)"
date_published: 2011-02-09
date_ingested: 2026-09-04
source_count: 0
tags: [testes, test-doubles, mock, hand-built, referencia-bibliografica, xunit, fonte-primaria]
skill: tech-mentor-testing
status: stable
---

# [UTwHCM] — Unit Testing With Hand Crafted Mocks (xUnitPatterns.com — Gerard Meszaros, citando Sven Gorts)

## TL;DR

Verbete da categoria **References** (bibliografia) do catálogo xUnitPatterns.com — diferente de "Glossary" ([[wiki/sources/doc-xunitpatterns|ex.: DOC]]) e "Tools" ([[wiki/sources/jmock|ex.: JMock]]), já ingeridas — que cita e resume um artigo externo de **Sven Gorts** sobre construir mocks **à mão** (hand-crafted), sem framework de mocking. O valor principal desta fonte não é o conteúdo do artigo em si (não está disponível para leitura completa — link secundário aponta para refactoring.be, fora do escopo desta ingestão), mas a **estrutura de citação**: o verbete referencia a subseção "**Hand-Built Test Double**" dentro da página (ainda não ingerida) *Configurable Test Double*, especificamente para **Test Stub** e **Mock Object**. Isso revela que a dicotomia "Hard-Coded vs. Configurable" já registrada em [[wiki/concepts/test-doubles]] tem uma subdivisão adicional dentro do lado Configurable: **Hand-Built** (classe escrita à mão, mas configurável em runtime) vs. o que o exemplo de [[wiki/entities/jmock|JMock]] representa — geração **dinâmica** via reflexão/proxy. Ver nota de correção em [[wiki/concepts/test-doubles]].

---

## Afirmações Centrais

| Afirmação | Evidência | Fonte | Confiança |
|---|---|---|---|
| O artigo de Gorts resume e nomeia idiomas relacionados a Hand-Built Test Doubles, especificamente Test Stubs e Mock Objects | "This paper summarizes and names a number of idioms related to Hand-Built Test Doubles [...], specfically Test Stubs [...] and Mock Objects" | fonte primária (Meszaros, citando Gorts) | alta |
| "Hand-Built Test Double" é uma subseção/técnica dentro da página Configurable Test Double, não um padrão independente | Link HTML original aponta para `Configurable Test Double.html#Hand-Built Test Double` (âncora dentro da página, não página própria) | fonte primária (estrutura de link) | alta — mas a definição completa de "Hand-Built Test Double" não está nesta fonte, apenas a referência a ela |
| Gorts escreveu todos os mocks à mão apesar da disponibilidade de frameworks de mocking na época | "despite the availability of various mocking frameworks, each of the mock classes I've used has been hand written" | citação direta de Gorts | alta |

---

## Key Claims

### 1. Nova categoria de fonte: References/bibliografia, distinta de Glossary e Tools
Todas as fontes do xUnitPatterns.com ingeridas até agora eram "Glossary" (definição de termo) ou "Tools" ([[wiki/sources/jmock]]). Esta é a primeira da categoria **References**: um verbete que resume e cita um artigo **externo** ao site (por Sven Gorts, hospedado em refactoring.be), com sigla própria de citação **[UTwHCM]** usada em outros verbetes do catálogo para remeter a ele. O texto do artigo original não foi lido nesta ingestão — apenas o resumo/citação de Meszaros.

### 2. "Hand-Built" revela uma subdivisão não capturada antes na wiki
[[wiki/concepts/test-doubles]] já registrava a dualidade **Hard-Coded vs. Configurable Test Double** como a "técnica de construção" ortogonal ao "papel" do double (Stub/Mock/Fake). O link estrutural desta fonte (`Configurable Test Double.html#Hand-Built Test Double`) mostra que "Hand-Built" é uma técnica **dentro** do lado Configurable — ou seja, um Hand-Built Test Double é escrito à mão pelo desenvolvedor, mas ainda assim **configurável** em runtime (ex.: via setters ou construtor que define o valor de retorno), em contraste com um Configurable Test Double **gerado dinamicamente** por um framework de mocking (o caso do [[wiki/entities/jmock|JMock]], via reflexão/proxy). A nota anterior em [[wiki/concepts/test-doubles]] que tratava "escrito à mão" como sinônimo direto de "Hard-Coded" está imprecisa — corrigida nesta ingestão.

### 3. Motivação de Gorts: consolidar idiomas observados na própria prática, não propor um framework
A citação direta de Gorts é uma retrospectiva pessoal ("in this article I do some retrospection") sobre os idiomas de mocking que ele achou mais úteis ao longo de anos escrevendo mocks manualmente — não uma proposta normativa nem uma crítica a frameworks de mocking. O artigo é contemporâneo ao período em que frameworks dinâmicos (como JMock) já existiam mas ainda não eram universalmente adotados.

---

## Entidades Mencionadas

- [[wiki/entities/gerard-meszaros]] — autor do verbete de citação/referência
- [[wiki/entities/sven-gorts]] — autor do artigo original citado (nova entidade criada nesta ingestão)
- [[wiki/entities/jmock]] — contraste implícito: JMock representa o lado "gerado dinamicamente" da dualidade que este verbete revela dentro de Configurable Test Double

## Conceitos Tocados

- [[wiki/concepts/test-doubles]] — revela subdivisão Hand-Built vs. Dinamicamente Gerado dentro de Configurable Test Double; correção aplicada à nota anterior sobre JMock

## Questões Abertas

- A página primária **"Configurable Test Double"** do xUnitPatterns.com (que contém a subseção "Hand-Built Test Double" referenciada aqui) ainda não foi ingerida — é a fonte que resolveria com certeza a definição completa de Hand-Built vs. Dynamically Generated. Candidata natural para uma próxima ingestão.
- O artigo original de Sven Gorts (refactoring.be/articles/mocks/mocks.html) está fora do escopo desta ingestão (site externo, não xUnitPatterns.com) — não foi lido; os "idiomas" que ele nomeia continuam desconhecidos para a wiki.
- Não há indicação de data de publicação do artigo original de Gorts nem de sua profissão/afiliação — a fonte primária não fornece esses dados.

---

## Citações Relevantes

> "This paper summarizes and names a number of idioms related to Hand-Built Test Doubles (see Configurable Test Double on page X), specfically Test Stubs (page X) and Mock Objects (page X)."

> "Many of the unit tests I wrote over the last couple of years use mock objects in order to test the behavior of a component in isolation of the rest of the system. So far, despite the availability of various mocking frameworks, each of the mock classes I've used has been hand written. In this article I do some retrospection and try to wrap up the mocking idioms I've found most usefull." — Sven Gorts

*(Tradução completa em `raw/utwhcm.md`.)*
