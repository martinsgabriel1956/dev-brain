---
type: source
title: "SUnit (xUnitPatterns.com — Gerard Meszaros)"
aliases: ["sunit", "sunit xunitpatterns", "xunit members sunit"]
date_created: 2026-09-11
date_updated: 2026-09-11
source_file: /home/nemomartins/Documentos/new/dev-study/raw/sunit-xunitpatterns.md
source_url: "http://xunitpatterns.com/SUnit.html"
author: "Gerard Meszaros"
date_published: 2003-01-01
date_ingested: 2026-09-11
source_count: 0
tags: [testes, sunit, smalltalk, xunit, kent-beck, fonte-primaria, xunit-members]
skill: tech-mentor-testing
status: stable
---

# SUnit (xUnitPatterns.com — Gerard Meszaros)

## TL;DR

Verbete curtíssimo da categoria **xUnit Members** (não Glossary) do xUnitPatterns.com, dedicado ao próprio **SUnit**: descrito como autodenominado "a mãe de todos os frameworks de teste unitário" (*"The mother of all unit testing frameworks"*), membro da família [[wiki/concepts/tdd|Xunit]] para **Smalltalk**, disponível para download em http://sunit.sourceforge.net. É a primeira fonte primária isolada da wiki dedicada ao SUnit em si — até agora ele só era conhecido por citação cruzada em [[wiki/sources/xunit-xunitpatterns]] (que o nomeia como ancestral, mas sem verbete próprio) e por relato indireto em [[wiki/sources/xunit-martin-fowler]] (que descreve o "framework de teste caseiro em Smalltalk" de Kent Beck sem nomeá-lo). Fecha exatamente a lacuna sinalizada como questão aberta em [[wiki/sources/xunit-xunitpatterns]].

---

## Afirmações Centrais

| Afirmação | Evidência | Fonte | Confiança |
|---|---|---|---|
| SUnit se autodenomina "a mãe de todos os frameworks de teste unitário" | "SUnit, the self-proclaimed \"The mother of all unit testing frameworks\"" | fonte primária (Meszaros) | alta |
| SUnit é o membro da família xUnit para a linguagem Smalltalk | "is the member of the xUnit family for the Smalltalk programming language" | fonte primária | alta |
| SUnit está disponível para download em sunit.sourceforge.net | "It is available for download at http://sunit.sourceforge.net" | fonte primária | alta |

---

## Key Claims

### 1. "Self-proclaimed" é uma ressalva editorial deliberada do próprio Meszaros
O site não endossa a afirmação "mãe de todos os frameworks de teste unitário" como fato objetivo — usa a palavra "self-proclaimed" (autodenominado) para marcar que é uma reivindicação do próprio projeto SUnit, não uma avaliação do catálogo. É consistente com a cronologia já registrada em [[wiki/entities/kent-beck]] e [[wiki/entities/sunit]]: SUnit antecede o JUnit e é o framework caseiro em Smalltalk que Beck usou antes de portá-lo para Java — a reivindicação de "mãe" tem lastro histórico, mesmo que o verbete não a afirme como certeza.

### 2. Categoria "xUnit Members", não "Glossary" — mesmo padrão de RSpec e diferente de "annotation"/"xUnit"
Assim como [[wiki/sources/rspec-xunitpatterns]], este verbete pertence à categoria **xUnit Members** do site (framework específico, com link de download), não à categoria **Glossary** (definição de termo abstrato) usada por [[wiki/sources/xunit-xunitpatterns]] e [[wiki/sources/annotation-xunitpatterns]]. O tratamento editorial é o mesmo dado a outros membros nomeados da família (JUnit, NUnit, CppUnit, PyUnit, RSpec, etc., listados na barra lateral "All xUnit Members" da própria página).

### 3. Fecha a lacuna de nomenclatura isolada, mas não acrescenta detalhe mecânico
Diferente de [[wiki/sources/rspec-xunitpatterns]] (que descreve como o RSpec troca vocabulário de teste por vocabulário de especificação), este verbete não descreve nenhuma característica de API ou sintaxe do SUnit — é deliberadamente mínimo, um parágrafo com tagline, família e link. Todo o detalhe mecânico e histórico sobre o SUnit continua vindo de fontes indiretas já ingeridas: [[wiki/sources/xunit-martin-fowler]] (uso no C3, reconstrução por time) e [[wiki/sources/xunit-xunitpatterns]] (nomeação como ancestral formal do padrão xUnit).

---

## Entidades Mencionadas

- [[wiki/entities/sunit]] — assunto central do verbete; primeira fonte primária isolada dedicada a ele
- [[wiki/entities/gerard-meszaros]] — autor do verbete; mesma fonte primária do catálogo já usada para dezenas de outros termos já ingeridos
- [[wiki/entities/kent-beck]] — criador do SUnit (não citado nominalmente neste verbete específico, mas confirmado por [[wiki/entities/sunit]] via fontes cruzadas)

## Conceitos Tocados

- [[wiki/concepts/tdd|Xunit]] — SUnit como membro nomeado da família, ao lado de JUnit, NUnit, RSpec e demais ports já catalogados na wiki

## Questões Abertas

- O verbete não menciona datas (ano de criação do SUnit, versão atual) nem detalhes de API — puramente descritivo/promocional (tagline + link de download). Sem novidade cronológica em relação ao que [[wiki/entities/sunit]] já registrava.
- Não fica claro se sunit.sourceforge.net ainda é o repositório ativo/canônico do projeto em 2026 — o link é o mesmo citado na página original de 2011, sem verificação de atualidade nesta ingestão.

---

## Citações Relevantes

> "SUnit, the self-proclaimed \"The mother of all unit testing frameworks\" is the member of the xUnit family for the Smalltalk programming language. It is available for download at http://sunit.sourceforge.net."

*(Tradução completa em `raw/sunit-xunitpatterns.md`.)*
