---
type: source
title: "Procedure Variable (xUnitPatterns.com — Gerard Meszaros)"
aliases: ["procedure variable", "variável de procedimento", "function pointer", "delegate .net", "xunit patterns glossary procedure variable"]
date_created: 2026-09-02
date_updated: 2026-09-02
source_file: /home/nemomartins/Documentos/new/dev-study/raw/procedure-variable-xunitpatterns.md
source_url: "http://xunitpatterns.com/procedure%20variable.html"
author: "Gerard Meszaros"
date_published: 2003-01-01
date_ingested: 2026-09-02
source_count: 0
tags: [testes, test-doubles, xunit, fonte-primaria, terminologia, oop, dynamic-binding]
skill: tech-mentor-testing
status: stable
---

# Procedure Variable (xUnitPatterns.com — Gerard Meszaros)

## TL;DR

Verbete curtíssimo (três frases) do Glossário do catálogo xUnitPatterns.com que define **procedure variable** (também conhecida como *function pointer* ou *delegate* em .Net): uma variável que referencia um procedimento/função em vez de um dado, permitindo que o código chamado seja decidido em tempo de execução (*dynamic binding*) em vez de tempo de compilação. Diferente da maioria dos outros verbetes já ingeridos desta fonte — que fixam vocabulário específico de teste (SUT, DOC, control point) — este é um termo de **mecânica de linguagem de programação**, citado no glossário porque é a técnica de implementação por trás do **Configurable Test Double** já registrado em [[wiki/concepts/test-doubles]]. Meszaros também o posiciona historicamente: *procedure variables* foram o precursor das OOPLs (linguagens verdadeiramente orientadas a objetos) — C++ inicial usava tabelas de *procedure variables* para montar as *dispatch tables* de objetos/classes, o mecanismo que hoje chamamos de [[wiki/concepts/polimorfismo|polimorfismo]] dinâmico.

---

## Afirmações Centrais

| Afirmação | Evidência | Fonte | Confiança |
|---|---|---|---|
| Procedure variable é uma variável que referencia um procedimento/função, não um dado | "A variable that refers to a procedure or function rather than a piece of data" | fonte primária (Meszaros) | alta |
| Permite dynamic binding — o código chamado é decidido em tempo de execução, não de compilação | "This allows the called code to be determined at run time (dynamic binding) rather than at compile time" | fonte primária | alta |
| Procedure variables foram precursoras das OOPLs verdadeiras; C++ inicial as usava em tabelas para montar dispatch tables de objetos/classes | "Early OOPLs such as C++ were built by using tables (arrays) of data structures containing procedure variables to implement the dispatch tables for objects/classes" | fonte primária | alta |

---

## Key Claims

### 1. "Procedure variable" é o nome de mecanismo, não de padrão de teste — mas o glossário o inclui porque sustenta o Configurable Test Double
Todos os outros verbetes já ingeridos desta fonte (SUT, DOC, control point, fixture setup) fixam vocabulário específico de teste. Este é diferente: é um conceito puro de linguagem de programação (também chamado *function pointer* em C/C++, *delegate* em .Net). A razão de estar no Glossário do xUnitPatterns.com é prática — [[wiki/sources/replace-dependency-with-test-double-xunitpatterns]] já registra a distinção **Hard-Coded vs. Configurable Test Double** como uma das três decisões ortogonais ao introduzir um double; um Configurable Test Double tipicamente é construído atribuindo comportamento a uma *procedure variable* (ou ao equivalente em runtime, como um lambda/callback) em vez de fixá-lo no código do double. O verbete isola essa peça mecânica que a fonte anterior menciona só de passagem.

### 2. Dynamic binding via procedure variable é o mesmo mecanismo, antes de existir uma palavra para "polimorfismo"
A definição situa *procedure variables* como precursoras históricas das OOPLs: antes de existir despacho polimórfico embutido na linguagem, o mesmo efeito — decidir em runtime qual código roda — era obtido manualmente, guardando ponteiros de função em tabelas (arrays) que imitavam o que hoje é a *vtable*/*dispatch table* de uma classe. [[wiki/concepts/polimorfismo]] já registra o despacho dinâmico (chamar `area()` sobre tipos diferentes) como decidido em tempo de execução pelo próprio objeto; esta fonte mostra a camada de implementação por baixo desse comportamento em linguagens como C++ inicial — antes de existir sintaxe de classe/método virtual, o programador montava essas tabelas de despacho manualmente com *procedure variables*.

---

## Entidades Mencionadas

- [[wiki/entities/gerard-meszaros]] — autor do verbete; mesma fonte primária do catálogo já usada para [[wiki/sources/test-double-xunitpatterns-meszaros]], [[wiki/sources/test-automater-xunitpatterns]] e demais verbetes do glossário

## Conceitos Tocados

- [[wiki/concepts/test-doubles]] — procedure variable é o mecanismo típico de implementação do Configurable Test Double (Hard-Coded vs. Configurable, já registrado via [[wiki/sources/replace-dependency-with-test-double-xunitpatterns]])
- [[wiki/concepts/polimorfismo]] — dynamic binding via procedure variable é o precursor histórico, pré-OOP, do despacho dinâmico hoje embutido na linguagem

## Questões Abertas

- A fonte não dá um exemplo concreto de código (nem em C, nem em .Net) mostrando uma *procedure variable* sendo usada para montar um Configurable Test Double — a conexão com Test Doubles é inferência da wiki a partir de [[wiki/sources/replace-dependency-with-test-double-xunitpatterns]], não afirmação explícita deste verbete.
- O mesmo glossário do xUnitPatterns.com lista termos irmãos de mecânica de linguagem ainda não ingeridos — ex.: **dynamic binding** e **static binding** têm verbetes próprios linkados no Glossário (vistos na barra lateral desta página) e ainda não foram ingeridos isoladamente; candidatos naturais para fechar esta pequena série de vocabulário de linguagem, análoga à série de papéis de projeto (test automater/maintainer/reader/stripper).

---

## Citações Relevantes

> "A variable that refers to a procedure or function rather than a piece of data. This allows the called code to be determined at run time (dynamic binding) rather than at compile time. The actual procedure to be invoked is assigned to the variable either during program initialization or during execution. Procedure variables were a precursor to true object-oriented programming languages (OOPLs). Early OOPLs such as C++ were built by using tables (arrays) of data structures containing procedure variables to implement the dispatch tables for objects/classes."

*(Tradução completa em `raw/procedure-variable-xunitpatterns.md`.)*
