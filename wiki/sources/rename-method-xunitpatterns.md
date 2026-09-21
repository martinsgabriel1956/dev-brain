---
type: source
title: "Rename Method (xUnitPatterns.com — catálogo de Gerard Meszaros, conteúdo atribuído a Martin Fowler)"
aliases: ["rename method", "renomear método", "xunit patterns code refactoring rename method"]
date_created: 2026-09-21
date_updated: 2026-09-21
source_file: "raw/rename-method-xunitpatterns.md"
source_url: "http://xunitpatterns.com/Rename%20Method.html"
author: "Gerard Meszaros (catálogo); conteúdo atribuído a Martin Fowler"
date_published: 2007-01-01
date_ingested: 2026-09-21
source_count: 0
tags: [testes, refactoring, test-discovery, xunit, fonte-primaria]
skill: tech-mentor-testing
status: stable
---

# Rename Method (xUnitPatterns.com — catálogo de Gerard Meszaros, conteúdo atribuído a Martin Fowler)

## TL;DR

Verbete curtíssimo da categoria **Code Refactorings** do catálogo xUnitPatterns.com, dedicado à refatoração **Rename Method** — mesma proveniência "host ≠ autor" já registrada para [[wiki/sources/extract-method-xunitpatterns|Extract Method]] e [[wiki/sources/extract-interface-xunitpatterns|Extract Interface]]: Meszaros hospeda o verbete, mas credita o conteúdo a **[[wiki/entities/martin-fowler|Fowler]]** (*Refactoring: Improving the Design of Existing Software*). Fecha uma lacuna citada explicitamente em três lugares — [[wiki/concepts/rename-method]] (stub), [[wiki/concepts/test-discovery]] e [[wiki/sources/test-discovery-xunitpatterns]] — onde Rename Method já era mencionada como a técnica recomendada para migrar Test Methods a um framework que descobre testes por convenção de nomenclatura, mas sem fonte primária dedicada. Igual às duas refatorações-irmãs, o verbete é minimalista (problema, resumo de uma frase, remissão bibliográfica) e carrega a mesma nota do site alertando que o capítulo correspondente do livro publicado "provavelmente mudou substancialmente" — mas aqui acrescenta uma citação direta de Fowler ausente nas duas outras: um comentário sobre o risco de métodos pequenos demais tornarem o código difícil de seguir ("merry dance").

---

## Afirmações Centrais

| Afirmação | Evidência | Fonte | Confiança |
|---|---|---|---|
| O problema motivador é: o nome de um método não revela seu propósito | "The name of a method does not reveal its purpose" | fonte primária (catálogo, atribuída a Fowler) | alta |
| A solução é mudar o nome do método | "Change the name of the method" | fonte primária | alta |
| Fowler alerta que métodos pequenos demais, mal nomeados, dificultam entender o que o código faz | "Done badly, this can lead you on a merry dance to find out what all the little methods do" | fonte primária (citação direta) | alta |
| O conteúdo desta página é atribuído a Fowler, não a Meszaros — remissão bibliográfica explícita | "From [Ref]" → *Refactoring: Improving the Design of Existing Software* | fonte primária | alta |
| A própria página se declara desatualizada em relação ao livro publicado | "The book has now been published and the content of this chapter has likely changed substanstially" | nota do site | alta (é o próprio site que avisa) |

---

## Key Claims

### 1. Terceiro exemplo confirmado do padrão "host ≠ autor" na categoria Code Refactorings
Com Extract Method e Extract Interface já ingeridas, este é o terceiro verbete consecutivo da categoria **Code Refactorings** do catálogo de Meszaros atribuído integralmente a Fowler. O padrão está agora bem estabelecido: essa categoria inteira funciona como índice/pointer para a literatura clássica de refatoração, distinta das categorias onde Meszaros é a própria fonte primária (Glossary, XUnit Basics, Test Smells etc.).

### 2. Único dos três verbetes de refatoração ingeridos com citação direta de Fowler além do par problema/solução
Diferente de Extract Method e Extract Interface — que se limitam à fórmula "problema em uma frase, solução em uma frase, remissão bibliográfica" — este verbete acrescenta uma citação literal de Fowler sobre o *risco* da técnica-irmã (métodos pequenos), não apenas sobre Rename Method em si. É a primeira vez, entre os três, que o catálogo preserva a voz de Fowler além da fórmula problema/solução — ainda que o trecho citado fale mais sobre a filosofia de métodos pequenos do que sobre a mecânica de renomear.

### 3. Fecha a lacuna citada em três pontos distintos da wiki, todos no mesmo contexto: Test Method Discovery
[[wiki/concepts/rename-method]] já existia como stub, criado a partir da única menção disponível até agora — [[wiki/sources/test-discovery-xunitpatterns]], que cita Rename Method [Fowler] como a técnica de migração quando um Test Method precisa passar a seguir a convenção de nomenclatura de um novo framework. Esta ingestão não altera esse contexto de aplicação (a fonte não menciona teste em nenhum momento — é um verbete genérico de refatoração), mas dá a ele, pela primeira vez, uma fonte primária própria e independente da citação indireta.

---

## Entidades Mencionadas

- [[wiki/entities/martin-fowler]] — creditado como autor original da refatoração Rename Method, via seu livro *Refactoring: Improving the Design of Existing Software*; citação direta preservada nesta fonte
- [[wiki/entities/gerard-meszaros]] — autor do catálogo/site que hospeda este verbete, mas não do conteúdo em si; terceiro exemplo do padrão "host ≠ autor" já registrado para Extract Interface e Extract Method

## Conceitos Tocados

- [[wiki/concepts/rename-method]] — página existente (stub), agora com fonte primária dedicada além da citação indireta em test-discovery
- [[wiki/concepts/extract-method]] — refatoração-irmã de mesma proveniência host≠autor, já ingerida
- [[wiki/concepts/test-discovery]] — contexto de aplicação prático já documentado: migração de Test Methods para descoberta por convenção de nomenclatura

## Questões Abertas

- **A fonte é genérica, não específica de teste** — assim como Extract Method e Extract Interface, o verbete não menciona xUnit, Test Method ou Test Discovery em nenhum momento; toda a aplicação ao contexto de teste vem de [[wiki/sources/test-discovery-xunitpatterns]], uma fonte separada. Rename Method, em si, é uma refatoração de propósito geral.
- **A citação sobre "merry dance"** fala do risco de métodos pequenos demais em geral (contexto de Extract Method), não especificamente da mecânica de Rename Method — presença um pouco desalinhada com o resto do verbete, mas preservada por ser a única voz direta de Fowler capturada nos três verbetes de refatoração ingeridos até agora.
- Com Extract Method, Extract Interface e Rename Method agora ingeridas, restam ainda sem fonte primária dedicada as demais refatorações citadas de passagem no rodapé da categoria: Extract Class, Extract Superclass, Inline Method, Inline Temp, Introduce Explaining Variable, Move Field, Move Method, Preserve Whole Object, Pull Up Field, Pull Up Method, Replace Conditional With Guard Clause, Replace Magic Number with Symbolic Constant, Replace Nested Conditional with Guard Clauses, Sprout Class — nenhuma delas citada até agora em outra fonte já ingerida na wiki, portanto sem urgência de ingestão.

---

## Citações Relevantes

> "The name of a method does not reveal its purpose."

> "Change the name of the method."

> "An important part of the code style I am advocating is small methods to factor complex processes. Done badly, this can lead you on a merry dance to find out what all the little methods do."

*(Tradução completa em `raw/rename-method-xunitpatterns.md`.)*
