---
type: entity
title: "Gerard Meszaros"
aliases: ["Meszaros", "xUnit Test Patterns author"]
date_created: 2026-07-19
date_updated: 2026-08-21
source_count: 5
tags: [testes, autor, test-doubles, xunit, taxonomia]
skill: tech-mentor-testing
status: draft
---

# Gerard Meszaros

Autor de *xUnit Test Patterns: Refactoring Test Code* (2007), livro de padrões para os frameworks da família [[wiki/concepts/tdd|Xunit]]. Criou a taxonomia dos cinco tipos de [[wiki/concepts/test-doubles|Test Double]] — Dummy, Fake, Stub, Spy, Mock — relatada e divulgada por [[wiki/entities/martin-fowler]] em seu bliki em 2006, antes mesmo do livro ser publicado.

## Autoria da taxonomia de Test Doubles

A distinção entre os cinco tipos de dublê de teste é frequentemente associada a Fowler por ser a fonte mais citada, mas o próprio Fowler credita a autoria a Meszaros explicitamente: ele estava "escrevendo um livro para capturar padrões de uso dos vários frameworks Xunit" e criou o vocabulário para resolver a inconsistência de nomes (stub, mock, fake, dummy) que já existia informalmente na comunidade. Ver [[wiki/sources/test-double-martin-fowler]].

A **fonte primária** dessa taxonomia — a própria página `Test Double` do catálogo xUnitPatterns.com, escrita por Meszaros como versão preliminar do capítulo do livro (p. 522) — está ingerida em [[wiki/sources/test-double-xunitpatterns-meszaros]]. Além dos cinco tipos, ela fixa o vocabulário que os sustenta: **SUT** (sistema sob teste, nunca substituído), **DOC** (componente-dependência, o que se substitui), **entrada/saída indireta** e **pontos de controle/observação**. Duas definições normativas dele que valem citar: um **Mock não é "Stub + asserção"** (a ênfase na *verificação* das saídas indiretas o torna um uso fundamentalmente diferente), e um **Test Spy é "apenas um" Stub com gravação**.

## Contribuidor recorrente do bliki de Fowler sobre test doubles

Além de ser a fonte da taxonomia relatada por Fowler, Meszaros é creditado como um dos contribuidores de ideias no bliki [[wiki/sources/self-initializing-fake-martin-fowler]] (2009), ao lado de Josh Price e Darren Cotterill — indício de que a relação entre os dois não se limitou à divulgação da taxonomia em 2006, mas incluiu troca continuada sobre padrões de teste.

## Ver também

- [[wiki/concepts/test-doubles]]
- [[wiki/entities/martin-fowler]] — divulgou a taxonomia de Meszaros no bliki antes do livro sair

## Key Sources

- [[wiki/sources/test-double-xunitpatterns-meszaros]] — **fonte primária**: a página canônica `Test Double` do próprio Meszaros (xUnitPatterns.com), com o vocabulário completo e as cinco variações
- [[wiki/sources/indirect-input-xunitpatterns]] — verbete de glossário do mesmo site, isolando a definição de "indirect input"
- [[wiki/sources/doc-xunitpatterns]] — verbete de glossário do mesmo site, isolando a definição formal de DOC (depended-on component)
- [[wiki/sources/test-double-martin-fowler]] — fonte secundária que popularizou e atribuiu a taxonomia a ele
- [[wiki/sources/self-initializing-fake-martin-fowler]] — creditado como contribuidor de ideias, junto com Josh Price e Darren Cotterill
