---
type: source
title: "Decorator (xUnitPatterns.com — Gerard Meszaros)"
aliases: ["decorator xunitpatterns", "external patterns decorator", "GOF decorator citation xunitpatterns"]
date_created: 2026-09-04
date_updated: 2026-09-04
source_file: /home/nemomartins/Documentos/new/dev-study/raw/decorator-xunitpatterns.md
source_url: "http://xunitpatterns.com/Decorator.html"
author: "Gerard Meszaros (verbete de citação); Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides — GOF (definição original citada)"
date_published: 2011-02-09
date_ingested: 2026-09-04
source_count: 0
tags: [design-patterns, decorator, structural, gof, xunit, external-patterns, fonte-primaria]
skill: tech-mentor-testing
status: stable
---

# Decorator (xUnitPatterns.com — Gerard Meszaros)

## TL;DR

Verbete curtíssimo da categoria **External Patterns** do catálogo xUnitPatterns.com — primeira entrada dessa categoria ingerida na wiki, distinta de Glossary ([[wiki/sources/doc-xunitpatterns|ex.: DOC]]), Tools ([[wiki/sources/jmock|ex.: JMock]]) e References ([[wiki/sources/utwhcm-xunitpatterns|ex.: UTwHCM]]) já cobertas — que cita, sem elaboração própria de Meszaros, a definição canônica do padrão **[[wiki/concepts/decorator-pattern|Decorator]]** do **[[wiki/entities/gang-of-four|GOF]]** (*Design Patterns*, 1994). Funciona como fonte primária independente (texto original em inglês, via citação direta) para a definição já registrada em [[wiki/concepts/decorator-pattern]] — até agora baseada apenas em fontes secundárias em vídeo, em português. Nota do próprio site: o livro *xUnit Test Patterns* já foi publicado e o conteúdo desta página provavelmente mudou substancialmente em relação ao capítulo final — sinal de que, ao contrário dos verbetes de Glossary já ingeridos, esta é uma página-rascunho mínima.

---

## Afirmações Centrais

| Afirmação | Evidência | Fonte | Confiança |
|---|---|---|---|
| Um Decorator é um objeto posicionado entre um cliente e outro objeto com o propósito de adicionar comportamento | "An object that is placed between a client and another object for the purpose of adding behavior." | fonte primária (Meszaros) | alta |
| Um Decorator implementa a mesma interface do objeto decorado e adiciona comportamento antes ou depois de chamar, no objeto decorado, o mesmo método que foi chamado nele mesmo | "A Decorator implements the same interface as the decorated object and adds behavior before or after it calls the same method (on the decorated object) as was called on itself." | fonte primária | alta |
| A definição citada não é formulação original de Meszaros — é atribuída diretamente ao GOF | "From [GOF]." | fonte primária (citação) | alta |

---

## Key Claims

### 1. Primeira entrada da categoria "External Patterns" ingerida — quarta categoria do site coberta pela wiki
As três categorias do xUnitPatterns.com já ingeridas eram todas de autoria conceitual de Meszaros ou citação de artigo externo relacionado a testes: **Glossary** (definição de termo do próprio vocabulário xUnit Patterns), **Tools** ([[wiki/sources/jmock|JMock]], ferramenta real) e **References** ([[wiki/sources/utwhcm-xunitpatterns|UTwHCM]], artigo externo sobre mocks). **External Patterns** é uma quarta categoria distinta: padrões de design **gerais**, não específicos de teste, que o site referencia como vocabulário emprestado de outros catálogos (aqui, o GOF) — a barra lateral da página lista dezenas de outros padrões nessa mesma categoria (Adapter, Command, Composite, Facade, Observer, Singleton, Strategy, Template Method, entre outros), a maioria ainda não ingerida.

### 2. Conteúdo é citação pura, sem elaboração própria de Meszaros
Diferente dos verbetes de Glossary (ex.: [[wiki/sources/doc-xunitpatterns]], [[wiki/sources/sut-xunitpatterns]]) que trazem definição formal detalhada e contextualizada dentro da taxonomia de testes, este verbete de External Pattern é apenas a citação textual da definição do GOF, com uma frase de resumo do próprio Meszaros e a nota "From [GOF]." — não há discussão de como (ou se) o Decorator é usado na construção de Test Doubles dentro do restante do catálogo. Essa ligação não pôde ser confirmada por esta fonte isolada (ver Questões Abertas).

### 3. Reforça, com fonte primária independente e em inglês, a definição já presente em decorator-pattern.md
[[wiki/concepts/decorator-pattern]] já continha uma definição de Decorator construída a partir de duas fontes secundárias em vídeo, em português ([[wiki/sources/seis-design-patterns-mais-usados-na-pratica]] e [[wiki/sources/design-pattern-decorator-renato-augusto]]). Esta fonte acrescenta o texto formal original do GOF, citado por Meszaros: "Attach additional responsibilities to an object dynamically. Decorators provide a flexible alternative to subclassing for extending functionality." — a formulação canônica que as fontes em vídeo parafraseavam sem citar diretamente.

---

## Entidades Mencionadas

- [[wiki/entities/gerard-meszaros]] — autor do verbete de citação, mesma fonte primária usada para toda a série de glossário/ferramentas/referências do xUnitPatterns.com
- [[wiki/entities/gang-of-four]] — autoria original da definição citada (*Design Patterns: Elements of Reusable Object-Oriented Software*, 1994)

## Conceitos Tocados

- [[wiki/concepts/decorator-pattern]] — recebe a definição formal do GOF como fonte primária adicional, em inglês, citada diretamente (não parafraseada)
- [[wiki/concepts/test-doubles]] — tangencial: não há, nesta fonte isolada, confirmação de que o Decorator é usado como técnica de construção de Test Doubles em outras páginas do site; registrado como questão aberta, não como claim

## Questões Abertas

- O verbete não explica **por que** o Decorator está catalogado dentro do xUnitPatterns.com — se é usado como técnica de implementação em outras páginas do catálogo (ex.: Test Spy ou Mock Object descritos como um Decorator em torno de um [[wiki/concepts/test-doubles|DOC]] real) ou se é referenciado apenas como vocabulário geral citado ao longo do livro. Candidato a esclarecer ingerindo as páginas "Test Spy" ou "Mock Object" do mesmo site, ainda não cobertas.
- As demais entradas da categoria "External Patterns" (Adapter, Command, Composite, Facade, Observer, Singleton, Strategy, Template Method, entre ~40 outras listadas na barra lateral) não foram ingeridas — candidatas naturais para completar o panorama desta categoria específica do site.
- A nota do site ("o conteúdo deste capítulo provavelmente mudou substancialmente") não é datada nem detalhada — não há como confirmar se a definição final publicada no livro (2007) diverge da citação nesta página web (gerada em 2011).

---

## Citações Relevantes

> "An object that is placed between a client and another object for the purpose of adding behavior."

> "Attach additional responsibilities to an object dynamically. Decorators provide a flexible alternative to subclassing for extending functionality."

> "A Decorator implements the same interface as the decorated object and adds behavior before or after it calls the same method (on the decorated object) as was called on itself. From [GOF]."

*(Tradução completa em `raw/decorator-xunitpatterns.md`.)*
