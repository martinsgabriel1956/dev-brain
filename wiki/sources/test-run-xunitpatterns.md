---
type: source
title: "Test Run (xUnitPatterns.com — Gerard Meszaros)"
aliases: ["test run", "execução de teste", "xunit patterns glossary test run"]
date_created: 2026-09-21
date_updated: 2026-09-22
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/test-run-xunitpatterns.md
source_url: "http://xunitpatterns.com/test%20run.html"
author: "Gerard Meszaros"
date_published: 2003-01-01
date_ingested: 2026-09-21
source_count: 0
tags: [testes, test-run, test-result, xunit, fonte-primaria, terminologia]
skill: tech-mentor-testing
status: stable
---

# Test Run (xUnitPatterns.com — Gerard Meszaros)

## TL;DR

Verbete de glossário do catálogo xUnitPatterns.com dedicado ao termo **test run**. Particularidade desta fonte: o texto do verbete é **idêntico, palavra por palavra**, ao de [[wiki/sources/test-result-xunitpatterns]] — "um test ou test suite pode ser executado muitas vezes, cada uma com um test result diferente" — com a única diferença sendo qual dos três termos (test result vs. test run) recebe o link `GlossaryRef` de destaque na própria frase. O catálogo trata "test run" e "test result" como **a mesma entrada conceitual vista por dois ângulos**: "test run" é o evento/ato de executar; "test result" é o produto desse evento. Nenhum dos dois verbetes tenta diferenciar os termos explicitamente — a diferenciação é inferida pela wiki, não afirmada pela fonte.

---

## Afirmações Centrais

| Afirmação | Evidência | Fonte | Confiança |
|---|---|---|---|
| Um test ou test suite pode ser executado muitas vezes | "A test or test suite can be run many times" | fonte primária (Meszaros) | alta |
| Cada execução ("test run") produz um test result próprio | "each with a different test result" | fonte primária | alta |

---

## Key Claims

### 1. "Test run" é o evento; "test result" é o produto — mas a fonte não faz essa distinção explicitamente
O texto idêntico entre os dois verbetes é, em si, o dado mais informativo desta ingestão: o catálogo não trata "test run" e "test result" como conceitos com definições independentes, mas como **duas faces do mesmo fenômeno** — executar (test run) e o que se obtém ao executar (test result). A distinção evento/produto é uma inferência da wiki a partir do padrão de uso do termo (ex.: "test run" tipicamente usado como substantivo de uma execução específica: "o test run de ontem à noite falhou"), não uma afirmação textual do verbete.

### 2. Reuso literal de texto entre verbetes de Glossário é uma prática do catálogo, não uma anomalia isolada
Esta é a primeira vez, na wiki, que dois verbetes do Glossário xUnitPatterns.com têm corpo de texto **100% idêntico**. Não invalida a definição — apenas confirma que o site trata alguns pares de termos como sinônimos funcionais suficientemente próximos para não merecerem prosa própria, delegando a diferenciação ao contexto de uso.

---

## Entidades Mencionadas

- [[wiki/entities/gerard-meszaros]] — autor do verbete; mesma fonte primária do catálogo já usada para os demais verbetes de Glossário ingeridos

## Conceitos Tocados

- [[wiki/concepts/test-suite-object]] — "test run" nomeia formalmente o evento de execução do Test Suite Object pelo [[wiki/concepts/test-runner|Test Runner]], do qual o test result é o produto

## Questões Abertas

- Resolve a lacuna sinalizada em [[wiki/sources/test-result-xunitpatterns]] ("test success", "test failure", "test error" e "test run" como termos irmãos sem fonte isolada) — "test run" agora está coberto; ~~**test success**, **test failure** e **test error** seguem sem verbete próprio ingerido.~~ **atualização 2026-09-22**: [[wiki/sources/test-failure-xunitpatterns]] fechou "test failure", [[wiki/sources/test-success-xunitpatterns]] fechou "test success" e [[wiki/sources/test-error-xunitpatterns]] fechou "test error", o último do quarteto. Lacuna completamente resolvida.
- A fonte não esclarece se "test run" pode se referir tanto à execução de um `test` individual quanto de uma `test suite` inteira (o texto usa "a test or test suite" indistintamente) — fica implícito que sim, sem termo separado para cada granularidade.

---

## Citações Relevantes

> "A test or test suite can be run many times, each with a different test result."

*(Tradução completa em `raw/test-run-xunitpatterns.md`. Texto idêntico ao de `raw/test-result-xunitpatterns.md`.)*
