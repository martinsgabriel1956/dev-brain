---
type: source
title: "eXtreme Programming (xUnitPatterns.com — Gerard Meszaros)"
aliases: ["extreme programming", "xp", "xunit patterns glossary xp"]
date_created: 2026-09-02
date_updated: 2026-09-02
source_file: /home/nemomartins/Documentos/new/dev-study/raw/extreme-programming-xunitpatterns.md
source_url: "http://xunitpatterns.com/XP.html"
author: "Gerard Meszaros"
date_published: 2003-01-01
date_ingested: 2026-09-02
source_count: 0
tags: [testes, agile, xp, xunit, fonte-primaria, terminologia]
skill: tech-mentor-testing
status: stable
---

# eXtreme Programming (xUnitPatterns.com — Gerard Meszaros)

## TL;DR

Verbete de glossário mais curto e mais genérico de toda a série xUnitPatterns.com ingerida até agora (uma única frase): define **eXtreme Programming** apenas como "uma metodologia ágil de desenvolvimento de software que destaca pair programming, testes unitários automatizados e iterações curtas". É deliberadamente uma definição de dicionário — três práticas citadas de passagem, sem TDD nomeado como ciclo, sem planning game, sem refatoração contínua, sem YAGNI. Serve como fonte primária isolada do próprio termo "XP" para a série de vocabulário do glossário, mas contrasta fortemente com a riqueza já registrada em [[wiki/concepts/extreme-programming]] (que documenta Kent Beck, o [[wiki/entities/c3-project|projeto C3]], TDD, dois chapéus e YAGNI) — evidência de que o glossário do xUnitPatterns.com usa XP apenas como termo de referência cruzada (ex.: em [[wiki/sources/unit-test-xunitpatterns]], para os sinônimos "developer test"/"programmer test"), não como assunto central do catálogo.

---

## Afirmações Centrais

| Afirmação | Evidência | Fonte | Confiança |
|---|---|---|---|
| XP é classificada como metodologia ágil de desenvolvimento de software | "An agile software development methodology" | fonte primária (Meszaros) | alta |
| A definição do glossário resume XP a três práticas: pair programming, testes unitários automatizados e iterações curtas | "that showcases pair programming, automated unit testing and short iterations" | fonte primária | alta |

---

## Key Claims

### 1. O glossário reduz XP a três práticas visíveis, sem citar TDD como ciclo, planning game, refatoração contínua ou YAGNI
A definição usa o verbo "showcases" (destaca/exibe) — enquadra as três práticas citadas como as mais visíveis externamente, não necessariamente as mais estruturais. Isso contrasta com [[wiki/concepts/extreme-programming]], que já documenta o ciclo RED-GREEN-REFACTOR ([[wiki/concepts/tdd]]), a metáfora dos [[wiki/concepts/dois-chapeus-kent-beck|dois chapéus]] e o princípio [[wiki/concepts/yagni]] como partes centrais da metodologia. A fonte confirma que "testes unitários automatizados" (não "TDD" explicitamente) é o termo usado — reforça a distinção terminológica já registrada em [[wiki/sources/unit-test-xunitpatterns]], onde "unit test" em XP também é chamado de developer test/programmer test.

### 2. Verbete existe no glossário apenas como ponto de referência cruzada para outros termos, não como assunto aprofundado
Diferente de verbetes técnicos da mesma série (SUT, DOC, control point), que fixam vocabulário usado ativamente no restante do catálogo de padrões, "eXtreme Programming" aparece no glossário citado por outros verbetes (ex.: [[wiki/sources/unit-test-xunitpatterns]] o cita para justificar os sinônimos "developer test"/"programmer test") mas não tem, ele mesmo, nenhum padrão (pattern) do catálogo dedicado ao tema — XP é contexto histórico/organizacional, não uma técnica de teste em si.

---

## Entidades Mencionadas

- [[wiki/entities/gerard-meszaros]] — autor do verbete; mesma fonte primária do catálogo já usada para [[wiki/sources/test-xunitpatterns]], [[wiki/sources/unit-test-xunitpatterns]] e demais verbetes do glossário
- [[wiki/entities/kent-beck]] — criador da eXtreme Programming; não citado nominalmente neste verbete (a definição é genérica, sem atribuição de autoria), mas central em [[wiki/concepts/extreme-programming]]

## Conceitos Tocados

- [[wiki/concepts/extreme-programming]] — recebe a definição mais enxuta e genérica de todas as fontes já ingeridas para o conceito, útil como contraponto de "definição de dicionário" vs. as fontes mais ricas (Fowler) já registradas
- [[wiki/concepts/pair-programming]] — citada como uma das três práticas "que destacam" XP nesta definição
- [[wiki/concepts/tdd]] — "testes unitários automatizados" é a formulação do glossário para o que a página de TDD documenta como ciclo completo

## Questões Abertas

- O verbete não define "iterações curtas" em termos concretos (dias? semanas? o conceito de "sprint" nem é mencionado) — nenhuma outra fonte da wiki fecha essa lacuna especificamente para XP; [[wiki/concepts/story-points]] e [[wiki/concepts/planning-poker]] tratam de estimativa em Scrum, não do tamanho de iteração em XP.
- Diferente de outros verbetes da série (que sempre remetem a padrões do catálogo), este não lista nenhum "Related Patterns" — reforça a leitura de que XP é vocabulário de contexto, não uma entrada ativa no vocabulário técnico de teste do site.

---

## Citações Relevantes

> "An agile software development methodology that showcases pair programming, automated unit testing and short iterations."

*(Tradução completa em `raw/extreme-programming-xunitpatterns.md`.)*
