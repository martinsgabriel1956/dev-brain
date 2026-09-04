---
type: source
title: "Emergent Design (xUnitPatterns.com — Gerard Meszaros)"
aliases: ["emergent design xunitpatterns", "design emergente xunitpatterns"]
date_created: 2026-09-04
date_updated: 2026-09-04
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/emergent-design-xunitpatterns.md
source_url: "http://xunitpatterns.com/emergent%20design.html"
author: "Gerard Meszaros"
date_published: 2003-01-01
date_ingested: 2026-09-04
source_count: 0
tags: [testes, tdd, xunit, fonte-primaria, terminologia, emergent-design, bduf]
skill: tech-mentor-testing
status: stable
---

# Emergent Design (xUnitPatterns.com — Gerard Meszaros)

## TL;DR

Verbete de glossário do xUnitPatterns.com que define, com fonte primária dedicada, o próprio termo **emergent design**: o oposto de **BDUF** (Big Design, Up Front). Consiste em deixar o design certo ser descoberto à medida que o software evolui lentamente para passar em **um teste de cada vez** durante o [[wiki/concepts/tdd|test-driven development]]. Fecha a lacuna deixada por [[wiki/sources/test-driven-development-xunitpatterns]], que já citava o termo, mas sem definição própria — e introduz **BDUF** como conceito novo, formalmente contrastante.

---

## Afirmações Centrais

| Afirmação | Evidência | Fonte | Confiança |
|---|---|---|---|
| Emergent design é o oposto de BDUF (Big Design, Up Front) | "The opposite of BDUF (Big Design, Up Front), emergent design involves..." | fonte primária (Meszaros) | alta |
| Consiste em deixar o design certo ser descoberto à medida que o software evolui | "...letting the right design be discovered as the software is slowly evolved..." | fonte primária | alta |
| O mecanismo é passar em um teste de cada vez durante TDD | "...to pass one test at a time during test-driven development" | fonte primária | alta |

---

## Key Claims

### 1. BDUF é o antônimo formal, agora com fonte primária própria
A wiki já usava o termo "emergent design" (via [[wiki/sources/test-driven-development-xunitpatterns]]) sem nunca ter isolado sua fonte primária dedicada nem o conceito com que ele contrasta. Esta fonte fecha as duas lacunas: define emergent design diretamente e nomeia formalmente o oposto — **BDUF**, Big Design Up Front — que não tinha página própria na wiki até esta ingestão.

### 2. Confirma, sem adicionar, a definição já inferida em [[wiki/concepts/emergent-design]]
O stub de conceito já existente (criado a partir da leitura do verbete de test-driven-development) já continha essencialmente esta definição. Esta fonte é a **confirmação primária direta** — antes a wiki citava o termo por segunda mão (definido dentro do verbete de outro termo), agora há uma página isolada e dedicada exclusivamente a "emergent design" no próprio glossário.

---

## Entidades Mencionadas

- [[wiki/entities/gerard-meszaros]] — autor do verbete; mesma fonte primária do catálogo já usada para [[wiki/sources/test-driven-development-xunitpatterns]], [[wiki/sources/test-first-development-xunitpatterns]] e outras entradas do glossário xUnitPatterns.com

## Conceitos Tocados

- [[wiki/concepts/emergent-design]] — promovido de stub para stable: agora tem fonte primária dedicada, não apenas citação por dentro do verbete de TDD
- [[wiki/concepts/bduf]] — novo stub criado a partir desta fonte; termo citado como oposto formal de emergent design
- [[wiki/concepts/tdd]] — mecanismo pelo qual o emergent design acontece ("passar um teste de cada vez")

## Questões Abertas

- BDUF (Big Design, Up Front) não tem verbete de glossário próprio ingerido ainda (`http://xunitpatterns.com/BDUF.html`) — candidato natural a uma próxima ingestão da mesma série para expandir o stub criado aqui.
- Sem contradição com o resto da wiki — esta fonte apenas formaliza, com página dedicada, o que já estava implícito em [[wiki/sources/test-driven-development-xunitpatterns]].

---

## Citações Relevantes

> "The opposite of BDUF (Big Design, Up Front), emergent design involves letting the right design be discovered as the software is slowly evolved to pass one test at a time during test-driven development."

*(Tradução completa em `raw/emergent-design-xunitpatterns.md`.)*
