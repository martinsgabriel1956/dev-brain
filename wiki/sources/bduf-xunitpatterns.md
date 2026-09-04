---
type: source
title: "BDUF (xUnitPatterns.com — Gerard Meszaros)"
aliases: ["bduf xunitpatterns", "big design up front xunitpatterns"]
date_created: 2026-09-04
date_updated: 2026-09-04
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/bduf-xunitpatterns.md
source_url: "http://xunitpatterns.com/BDUF.html"
author: "Gerard Meszaros"
date_published: 2003-01-01
date_ingested: 2026-09-04
source_count: 0
tags: [testes, tdd, xunit, fonte-primaria, terminologia, bduf, emergent-design]
skill: tech-mentor-testing
status: stable
---

# BDUF (xUnitPatterns.com — Gerard Meszaros)

## TL;DR

Verbete de glossário do xUnitPatterns.com que define, com fonte primária dedicada, o próprio termo **BDUF** (Big Design, Up Front): a abordagem clássica "waterfall", onde todos os requisitos devem ser entendidos no início do projeto e o software é projetado para suportar todos eles numa única "fase" de design. Fecha a última lacuna aberta por [[wiki/sources/emergent-design-xunitpatterns]], que já citava BDUF como o oposto formal, mas sem definição própria — e permite promover [[wiki/concepts/bduf]] de stub (inferido por contraste) para stable (fonte primária).

---

## Afirmações Centrais

| Afirmação | Evidência | Fonte | Confiança |
|---|---|---|---|
| BDUF é a abordagem clássica "waterfall" (cascata) para design de software | "'Big Design, Up Front' is the classic 'waterfall' approach to software design..." | fonte primária (Meszaros) | alta |
| Exige que todos os requisitos sejam entendidos no início do projeto | "...where all the requirements must be understood early in the project..." | fonte primária | alta |
| O software é projetado para suportar todos os requisitos numa única fase de design | "...the software is designed to support all those requirements in a single design 'phase'" | fonte primária | alta |
| Contrastado explicitamente com emergent design, favorecido por projetos ágeis | "Contrast this with the emergent design favored by agile projects." | fonte primária | alta |

---

## Key Claims

### 1. BDUF finalmente tem fonte primária própria na wiki
Desde a ingestão de [[wiki/sources/test-driven-development-xunitpatterns]], BDUF era citado apenas por contraste (dentro do verbete de outro termo), e o stub em [[wiki/concepts/bduf]] tinha sua definição **inferida**, não confirmada por fonte direta. Este verbete fecha essa lacuna, nomeada explicitamente como open question em [[wiki/sources/emergent-design-xunitpatterns]].

### 2. Confirma, sem adicionar, a definição já inferida em [[wiki/concepts/bduf]]
O texto do glossário é curtíssimo e não introduz nuance nova além do que já estava inferido: BDUF = waterfall = todos os requisitos entendidos antecipadamente = design completo numa fase única. O ganho é epistemológico (fonte primária vs. inferência por contraste), não de conteúdo novo.

---

## Entidades Mencionadas

- [[wiki/entities/gerard-meszaros]] — autor do verbete; mesma fonte primária do catálogo já usada para [[wiki/sources/emergent-design-xunitpatterns]], [[wiki/sources/test-driven-development-xunitpatterns]] e demais entradas do glossário xUnitPatterns.com

## Conceitos Tocados

- [[wiki/concepts/bduf]] — promovido de stub (inferido por contraste) para stable: agora tem fonte primária dedicada
- [[wiki/concepts/emergent-design]] — oposto formal, já com fonte primária própria; este verbete fecha o par completo
- [[wiki/concepts/tdd]] — mecanismo pelo qual emergent design (o oposto de BDUF) acontece

## Questões Abertas

- Nenhuma nova. Fecha a última lacuna explicitamente registrada na série de ingestões TDD → test-first development → emergent design → BDUF. O único verbete-irmão ainda pendente da série mais ampla é `storytest-driven development.html`, registrado como open question desde a primeira ingestão da série.

---

## Citações Relevantes

> "'Big Design, Up Front' is the classic 'waterfall' approach to software design where all the requirements must be understood early in the project and the software is designed to support all those requirements in a single design 'phase'. Contrast this with the emergent design favored by agile projects."

*(Tradução completa em `raw/bduf-xunitpatterns.md`.)*
