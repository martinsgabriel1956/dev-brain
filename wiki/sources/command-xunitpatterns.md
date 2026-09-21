---
type: source
title: "Command (xUnitPatterns.com — Gerard Meszaros)"
aliases: ["command xunitpatterns", "external patterns command", "GOF command citation xunitpatterns"]
date_created: 2026-09-21
date_updated: 2026-09-21
source_file: /home/nemomartins/Documentos/new/dev-study/raw/command-xunitpatterns.md
source_url: "http://xunitpatterns.com/Command.html"
author: "Gerard Meszaros (verbete de citação); Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides — GOF (definição original citada)"
date_published: 2011-02-09
date_ingested: 2026-09-21
source_count: 0
tags: [design-patterns, command, behavioral, gof, xunit, external-patterns, fonte-primaria]
skill: tech-mentor-testing
status: stable
---

# Command (xUnitPatterns.com — Gerard Meszaros)

## TL;DR

Verbete curtíssimo da categoria **External Patterns** do catálogo xUnitPatterns.com, segunda entrada dessa categoria ingerida na wiki depois de [[wiki/sources/decorator-xunitpatterns]] — mesmo formato: citação direta da definição canônica do **[[wiki/concepts/command-pattern|Command]]** do **[[wiki/entities/gang-of-four|GOF]]** (*Design Patterns*, 1994), sem elaboração própria de Meszaros. Fecha, com fonte primária isolada em inglês, a lacuna que [[wiki/sources/testcase-object-xunitpatterns]] já havia deixado em aberto: aquela fonte *aplicava* o Command Pattern ao [[wiki/concepts/testcase-object|Testcase Object]] (cada teste como objeto Command com método `run` padrão) sem citar a definição formal do padrão em si — esta fonte fornece exatamente essa definição, no texto original do GOF.

---

## Afirmações Centrais

| Afirmação | Evidência | Fonte | Confiança |
|---|---|---|---|
| Command objetifica uma solicitação para que ela possa ser executada via uma interface padrão | "Objectify a request so that it can be executed via a standard interface." | fonte primária (Meszaros) | alta |
| Encapsula uma solicitação como objeto, permitindo parametrizar clientes com diferentes solicitações, enfileirar/registrar solicitações, e suportar operações desfazíveis (undo) | "Encapsulate a request as an object, thereby letting you parameterize clients with different requests, queue or log requests, and support undoable operations." | fonte primária | alta |
| A definição citada não é formulação original de Meszaros — é atribuída diretamente ao GOF | "From [GOF]." | fonte primária (citação) | alta |

---

## Key Claims

### 1. Confirma, com fonte primária dedicada, a definição de Command já usada na wiki para explicar o Testcase Object
[[wiki/concepts/command-pattern]] já registrava, com base em [[wiki/sources/testcase-object-xunitpatterns]], que cada teste xUnit é "um objeto Command com método `run` padrão" — mas sem citar a definição formal do próprio padrão Command, apenas sua aplicação. Esta fonte fecha essa lacuna: fornece o texto canônico do GOF ("encapsulate a request as an object..."), permitindo comparar diretamente a definição geral do padrão com sua aplicação específica em testes (parametrizar/enfileirar/desfazer uma solicitação ↔ o Test Runner invocar um Testcase Object sem conhecer sua interface específica).

### 2. Undo/redo, a motivação mais citada do Command, não aparece na aplicação ao Testcase Object
A definição do GOF cita explicitamente "support undoable operations" como uma das motivações centrais do padrão — mas, como já registrado em [[wiki/concepts/command-pattern]] ("Aplicação concreta: cada teste xUnit é um Command"), a aplicação de Meszaros ao Testcase Object não usa essa capacidade: a motivação ali é uniformidade de invocação (o Test Runner chama `run` sem conhecer a interface do teste) e possibilidade de manter testes em coleções, não reversibilidade. Confirma, por contraste direto com a fonte primária do padrão, que a aplicação em teste é uma leitura parcial do Command — usa apenas a faceta de "objetificar uma chamada", descartando queue/log/undo.

### 3. Mesmo formato mínimo de citação da categoria External Patterns, mesma nota de obsolescência do site
Como em [[wiki/sources/decorator-xunitpatterns]], a página é um rascunho mínimo (resumo de uma frase + definição formal + "From [GOF]") com a mesma nota do site alertando que o conteúdo "provavelmente mudou substancialmente" desde a publicação do livro em 2007. Reforça o padrão já observado: as entradas de External Patterns são citações de vocabulário emprestado, não elaborações próprias de Meszaros como as entradas de Glossary ou XUnit Basics.

---

## Entidades Mencionadas

- [[wiki/entities/gerard-meszaros]] — autor do verbete de citação, mesma fonte primária usada para toda a série de glossário/ferramentas/referências/external patterns do xUnitPatterns.com
- [[wiki/entities/gang-of-four]] — autoria original da definição citada (*Design Patterns: Elements of Reusable Object-Oriented Software*, 1994)

## Conceitos Tocados

- [[wiki/concepts/command-pattern]] — recebe a definição formal do GOF como fonte primária adicional, em inglês, citada diretamente; contraste explícito entre a definição geral (com undo/redo) e a aplicação parcial ao Testcase Object (sem undo/redo)
- [[wiki/concepts/testcase-object]] — beneficiário indireto: a aplicação do Command já registrada ali agora tem a definição formal do padrão para comparação

## Questões Abertas

- Assim como em [[wiki/sources/decorator-xunitpatterns]], as demais entradas da categoria "External Patterns" (Adapter, Composite, Facade, Observer, Singleton, Strategy, Template Method, entre ~40 outras listadas na barra lateral) seguem majoritariamente não ingeridas — candidatas naturais para completar o panorama da categoria. **Atualização (2026-09-21):** [[wiki/sources/pluggable-behavior-xunitpatterns]] tornou-se a terceira entrada ingerida — única das três que cita Kent Beck (SBPP) em vez do GOF.
- A nota do site sobre o conteúdo ter "mudado substancialmente" não é datada nem detalhada — não há como confirmar se a definição final publicada no livro (2007) diverge da citação nesta página web (gerada em 2011).

---

## Citações Relevantes

> "Objectify a request so that it can be executed via a standard interface."

> "Encapsulate a request as an object, thereby letting you parameterize clients with different requests, queue or log requests, and support undoable operations."

> "From [GOF]."

*(Tradução completa em `raw/command-xunitpatterns.md`.)*
