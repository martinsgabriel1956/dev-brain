---
type: source
title: "Extract Interface (xUnitPatterns.com — catálogo de Gerard Meszaros, conteúdo atribuído a Martin Fowler)"
aliases: ["extract interface", "extrair interface", "xunit patterns code refactoring extract interface"]
date_created: 2026-09-11
date_updated: 2026-09-11
source_file: /home/nemomartins/Documentos/new/dev-study/raw/extract-interface-xunitpatterns.md
source_url: "http://xunitpatterns.com/Extract%20Interface.html"
author: "Gerard Meszaros (catálogo); conteúdo atribuído a Martin Fowler"
date_published: 2007-01-01
date_ingested: 2026-09-11
source_count: 0
tags: [testes, test-doubles, refactoring, dependency-injection, interface, xunit, fonte-primaria]
skill: tech-mentor-testing
status: stable
---

# Extract Interface (xUnitPatterns.com — catálogo de Gerard Meszaros, conteúdo atribuído a Martin Fowler)

## TL;DR

Verbete curtíssimo da categoria **Code Refactorings** do catálogo xUnitPatterns.com, dedicado à refatoração **Extract Interface** — mas, diferente da maioria das páginas já ingeridas deste site (Glossary, Test Refactorings), o próprio Meszaros credita o conteúdo a **[[wiki/entities/martin-fowler|Fowler]]** (*Refactoring: Improving the Design of Existing Software*), não a si mesmo. Fecha uma lacuna citada de passagem em pelo menos duas fontes já ingeridas — [[wiki/sources/replace-dependency-with-test-double-xunitpatterns]] e [[wiki/concepts/test-doubles]] — como o pré-requisito técnico, em linguagens estaticamente tipadas, para instalar um [[wiki/concepts/test-doubles|Test Double]] no lugar de uma dependência real via [[wiki/concepts/dependency-injection|Dependency Injection]]. O verbete em si é minimalista: problema, resumo de uma frase, e uma remissão bibliográfica — sem mecânica passo a passo, sem exemplo de código. A própria página carrega uma nota do site alertando que o capítulo correspondente do livro publicado "provavelmente mudou substancialmente" em relação a esta versão preliminar.

---

## Afirmações Centrais

| Afirmação | Evidência | Fonte | Confiança |
|---|---|---|---|
| O problema motivador é: vários clientes usam o mesmo subconjunto da interface de uma classe, ou duas classes têm parte de suas interfaces em comum | "Several clients use the same subset of a class's interface, or two classes have part of their interfaces in common" | fonte primária (catálogo, atribuída a Fowler) | alta |
| A solução é extrair esse subconjunto compartilhado para uma interface própria | "Extract the subset into an interface" | fonte primária | alta |
| O conteúdo desta página é atribuído a Fowler, não a Meszaros — remissão bibliográfica explícita | "From [Ref] Refactoring: Improving the Design of Existing Software" | fonte primária | alta |
| A própria página se declara desatualizada em relação ao livro publicado | "The book has now been published and the content of this chapter has likely changed substanstially" | nota do site | alta (é o próprio site que avisa) |

---

## Key Claims

### 1. Extract Interface resolve duplicação de *contrato*, não duplicação de código
O problema descrito não é sobre lógica duplicada (o alvo usual de refatoração) — é sobre **múltiplos consumidores dependendo apenas de uma fatia de uma classe**, ou duas classes distintas compartilhando parte do seu contrato público sem uma abstração comum que capture essa fatia. A solução — extrair essa fatia para uma interface — é uma refatoração *estrutural de tipos*, não de comportamento: nada no comportamento do sistema muda, só o vocabulário de tipos que os clientes enxergam.

### 2. É a peça que faltava para "substitutable dependency" em linguagens estaticamente tipadas
Duas fontes já na wiki citavam Extract Interface apenas de passagem, como pré-requisito técnico: [[wiki/sources/replace-dependency-with-test-double-xunitpatterns]] ("em linguagens estaticamente tipadas, podemos ter que fazer uma refatoração Extract Interface antes de introduzir a implementação fake") e [[wiki/concepts/test-doubles]] (mesma citação, herdada). O mecanismo concreto: se uma variável está tipada pela **classe concreta** da dependência real, o compilador rejeita atribuir um [[wiki/concepts/test-doubles|Test Double]] no lugar dela — mesmo que o double implemente toda a API relevante — porque o double não *é* aquela classe. Extraindo uma interface que cobre a API usada pelo SUT, e retipando a variável para essa interface, tanto a implementação real quanto o double passam a satisfazer o mesmo tipo declarado, e a substituição se torna possível sem alterar o SUT além da declaração de tipo. Esse é o mecanismo que viabiliza, na prática, a propriedade nomeada em [[wiki/sources/substitutable-dependency-xunitpatterns|substitutable dependency]] para instalação via [[wiki/concepts/dependency-injection|Dependency Injection]].

### 3. Atribuição cruzada dentro do próprio catálogo de Meszaros
Diferente de "control point", "DOC" ou "substitutable dependency" — verbetes onde Meszaros é a própria fonte primária —, aqui o catálogo funciona como **índice/pointer** para um crédito externo: o verbete não elabora a técnica, apenas remete ao livro de Fowler. Isso é consistente com a categoria do site em que a página está classificada ("Code Refactorings", que também lista Extract Class, Extract Method, Extract Superclass, Inline Method, Rename Method, Pull Up Method/Field, etc.) — uma seção do site dedicada a catalogar refatorações **de código-fonte geral** (não específicas de teste), atribuídas à literatura de refatoração clássica, e não à taxonomia de teste que é a autoria original de Meszaros.

---

## Entidades Mencionadas

- [[wiki/entities/martin-fowler]] — creditado como autor original da refatoração Extract Interface, via seu livro *Refactoring: Improving the Design of Existing Software*
- [[wiki/entities/gerard-meszaros]] — autor do catálogo/site que hospeda este verbete, mas não do conteúdo em si; mesmo padrão "host ≠ autor" já registrado para outras páginas de Fowler (ex.: Consumer-Driven Contracts, hospedado mas não escrito por ele)

## Conceitos Tocados

- [[wiki/concepts/extract-interface]] — página nova; conceito central desta fonte
- [[wiki/concepts/test-doubles]] — Extract Interface como pré-requisito técnico em linguagens estaticamente tipadas para instalar um Test Double sem alterar o tipo declarado da dependência
- [[wiki/concepts/dependency-injection]] — mesmo pré-requisito, do ponto de vista do mecanismo de instalação (a variável injetada precisa ser tipada pela interface, não pela classe concreta)
- [[wiki/concepts/refatoracao]] — Extract Interface como uma das refatorações catalogadas na tradição de Fowler; ao contrário das refatorações de comportamento discutidas na página guarda-chuva, esta é puramente estrutural de tipos

## Questões Abertas

- **Resolve uma lacuna citada duas vezes**: tanto [[wiki/sources/replace-dependency-with-test-double-xunitpatterns]] quanto [[wiki/concepts/test-doubles]] citavam "Extract Interface [Fowler]" sem página própria — esta ingestão fecha essa lacuna, mas só até o nível de detalhe que o próprio verbete oferece (uma frase de problema, uma de solução). A mecânica passo a passo (como o IDE/desenvolvedor decide quais métodos vão para a interface, como lidar com métodos que só alguns clientes usam) não está nesta fonte — precisaria do capítulo real do livro *Refactoring*, não desta versão preliminar do site.
- **A própria fonte se declara desatualizada** ("o conteúdo deste capítulo provavelmente mudou substancialmente" na edição publicada do livro) — tratado aqui como a versão disponível mais primária que se pôde ingerir, não como o texto definitivo de Fowler.
- **Diferença de proveniência não documentada explicitamente pelo site**: nenhuma nota no verbete explica por que esta página (e as demais da categoria "Code Refactorings") são atribuídas a Fowler enquanto o restante do catálogo (Glossary, Test Refactorings, Test Doubles) é autoria própria de Meszaros — inferência feita a partir do padrão observado entre as páginas já ingeridas, não afirmação explícita da fonte.

---

## Citações Relevantes

> "Several clients use the same subset of a class's interface, or two classes have part of their interfaces in common."

> "Extract the subset into an interface."

> "From [Ref] Refactoring: Improving the Design of Existing Software."

*(Tradução completa em `raw/extract-interface-xunitpatterns.md`.)*
