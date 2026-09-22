---
type: source
title: "Test-Driven Bug Fixing (xUnitPatterns.com — Gerard Meszaros)"
aliases: ["test-driven bug fixing", "TDD bug fixing", "test-driven bug fixing xunitpatterns"]
date_created: 2026-09-22
date_updated: 2026-09-22
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/test-driven-bug-fixing-xunitpatterns.md
source_url: "http://xunitpatterns.com/test-driven%20bug%20fixing.html"
author: "Gerard Meszaros"
date_published: 2003-01-01
date_ingested: 2026-09-22
source_count: 0
tags: [testes, tdd, xunit, fonte-primaria, terminologia, debugging]
skill: tech-mentor-testing
status: stable
---

# Test-Driven Bug Fixing (xUnitPatterns.com — Gerard Meszaros)

## TL;DR

Verbete curtíssimo do Glossário do catálogo xUnitPatterns.com que nomeia formalmente a prática já citada de passagem em [[wiki/concepts/frequent-debugging]] e em [[wiki/concepts/production-bugs]]: **test-driven bug fixing** é escrever e automatizar um [[wiki/sources/unit-test-xunitpatterns|unit test]] que reproduz o bug **antes** de depurar o código e aplicar a correção. A fonte a define explicitamente como a extensão do [[wiki/concepts/tdd|test-driven development]] aplicada à correção de defeitos, não como uma prática independente.

---

## Afirmações Centrais

| Afirmação | Evidência | Fonte | Confiança |
|---|---|---|---|
| É uma forma de corrigir bugs que envolve escrever/automatizar um unit test que reproduz o bug antes de depurar e corrigir | "A way of fixing bugs that entails writing and automating unit tests that reproduce each bug before debugging the code and fixing the bug" | fonte primária (Meszaros) | alta |
| É a extensão do test-driven development para correção de bugs, não uma prática separada | "It is the bug fixing extension of test-driven development" | fonte primária | alta |

---

## Key Claims

### 1. Fecha a referência que [[wiki/concepts/frequent-debugging]] já fazia sem fonte própria
[[wiki/sources/frequent-debugging-xunitpatterns]] recomendava, para o cenário de **Untested Requirement**, "escrever o teste automatizado que exporia o problema e então aplicar **test-driven bug fixing**" — citando o termo sem definição própria na wiki até esta ingestão. Este verbete fecha essa lacuna com a fonte primária dedicada.

### 2. O teste vem antes da depuração, não depois da correção
A ordem importa: primeiro se escreve o teste que **reproduz** o bug (ele deve falhar, replicando o defeito), só então se depura e corrige o código de produção. Isso difere de escrever um teste de regressão *depois* de já ter corrigido o problema manualmente — nesse segundo caso não há garantia de que o teste de fato capturaria a causa raiz, porque a correção já foi validada por outro método (observação manual, print, debugger).

### 3. Sem escopo formal de nível de teste
O verbete usa "unit tests" no singular genérico, sem distinguir explicitamente se a prática se aplica também a customer tests/component tests. Fica implícito que o nível do teste de reprodução deve corresponder ao nível em que o bug se manifesta — mesma lógica de granularidade que [[wiki/concepts/frequent-debugging]] já discutia para Defect Localization.

---

## Entidades Mencionadas

- [[wiki/entities/gerard-meszaros]] — autor do verbete; mesma fonte primária do catálogo já usada para [[wiki/sources/test-driven-development-xunitpatterns]] e outras entradas do glossário xUnitPatterns.com

## Conceitos Tocados

- [[wiki/concepts/tdd]] — a fonte define bug fixing como extensão direta da prática central já documentada
- [[wiki/concepts/frequent-debugging]] — referência ao termo agora resolvida com fonte primária dedicada
- [[wiki/concepts/production-bugs]] — cenário Untested Requirement, onde a prática é a resposta recomendada
- [[wiki/sources/unit-test-xunitpatterns]] — o tipo de teste usado para reproduzir o bug

## Questões Abertas

- Sem contradição com o resto da wiki — o verbete apenas nomeia e formaliza uma prática já referenciada informalmente por outras fontes.
- Não há verbete próprio distinguindo se a prática se aplica igualmente a component/customer tests, ou só a unit tests — inferido por analogia com [[wiki/concepts/frequent-debugging]].

---

## Citações Relevantes

> "A way of fixing bugs that entails writing and automating unit tests that reproduce each bug before debugging the code and fixing the bug. It is the bug fixing extension of test-driven development."

*(Tradução completa em `raw/test-driven-bug-fixing-xunitpatterns.md`.)*
