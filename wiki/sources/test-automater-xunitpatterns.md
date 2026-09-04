---
type: source
title: "Test Automater (xUnitPatterns.com — Gerard Meszaros)"
aliases: ["test automater", "automatizador de testes", "xunit patterns glossary test automater"]
date_created: 2026-09-02
date_updated: 2026-09-02
source_file: /home/nemomartins/Documentos/new/dev-study/raw/test-automater-xunitpatterns.md
source_url: "http://xunitpatterns.com/test%20automater.html"
author: "Gerard Meszaros"
date_published: 2003-01-01
date_ingested: 2026-09-02
source_count: 0
tags: [testes, papeis-de-projeto, xunit, fonte-primaria, terminologia]
skill: tech-mentor-testing
status: stable
---

# Test Automater (xUnitPatterns.com — Gerard Meszaros)

## TL;DR

Verbete curtíssimo (duas frases) do Glossário do catálogo xUnitPatterns.com que define o único termo de **papel de pessoa/projeto** ingerido até agora desta fonte: **test automater**, quem constrói os [[wiki/sources/test-xunitpatterns|testes]] (os automatiza). A definição separa explicitamente duas responsabilidades que o vocabulário técnico da wiki (SUT, DOC, control point, etc.) nunca precisou distinguir: **decidir quais testes existem** (papel do "subject matter expert", especialista no domínio) vs. **construir esses testes em código** (papel do test automater). É a primeira fonte da wiki que trata teste como divisão de trabalho entre papéis, não apenas como artefato técnico.

---

## Afirmações Centrais

| Afirmação | Evidência | Fonte | Confiança |
|---|---|---|---|
| Test automater é a pessoa ou papel do projeto responsável por construir os testes | "The person or project role responsible for building the tests" | fonte primária (Meszaros) | alta |
| Pode haver um "subject matter expert" separado, responsável por definir os testes a serem automatizados pelo test automater | "There may be a 'subject matter expert' who is responsible for coming up with the tests to be automated by the test automater" | fonte primária | alta |

---

## Key Claims

### 1. "Definir o teste" e "construir o teste" são papéis distintos, não a mesma tarefa
Nenhuma outra fonte da wiki sobre o catálogo xUnitPatterns.com (SUT, DOC, control point, test doubles) trata teste como trabalho dividido entre pessoas — todas descrevem vocabulário técnico do teste em si. Este verbete introduz a dimensão de **processo/papel**: um especialista de domínio pode saber *o quê* testar sem saber *como* automatizar, e o test automater entra para fechar essa lacuna de implementação. É consistente com o par **customer test** (verificável pelo cliente/domain expert) vs. **unit test** (construído e compreendido só por quem programa), já formalizado em [[wiki/sources/unit-test-xunitpatterns]] — o subject matter expert deste verbete é o mesmo tipo de ator que verificaria um customer test.

### 2. O termo não pressupõe automação por uma ferramenta específica — é definição de responsabilidade, não de técnica
A definição fala em "building the tests" de forma agnóstica a framework ou linguagem. Isso mantém o verbete coerente com o restante do glossário do site (definições sempre em termos de papel/relação, nunca de ferramenta) — o mesmo padrão já visto em [[wiki/sources/sut-xunitpatterns]], onde SUT é definido pela perspectiva do teste, não por uma propriedade fixa do código.

---

## Entidades Mencionadas

- [[wiki/entities/gerard-meszaros]] — autor do verbete; mesma fonte primária do catálogo já usada para [[wiki/sources/test-xunitpatterns]], [[wiki/sources/unit-test-xunitpatterns]] e demais verbetes do glossário

## Conceitos Tocados

- [[wiki/concepts/tdd]] — quem escreve o teste antes do código de produção, na prática, ocupa o papel de test automater
- [[wiki/concepts/piramide-de-testes]] — a divisão "quem decide o quê testar" vs. "quem automatiza" atravessa todas as camadas da pirâmide

## Questões Abertas

- O mesmo glossário do xUnitPatterns.com lista outros papéis de projeto irmãos ainda não ingeridos: **test maintainer**, **test reader** e **test stripper** — candidatos naturais para fechar a série de "papéis" do catálogo, análoga à série de vocabulário técnico (SUT/DOC/control point) já fechada.
- A fonte não detalha se "subject matter expert" e "test automater" podem ser a mesma pessoa na prática (times pequenos) ou se a distinção pressupõe times especializados (ex.: QA analyst vs. dev) — verbete deliberadamente enxuto, sem esse detalhe.

---

## Citações Relevantes

> "The person or project role responsible for building the tests. There may be a 'subject matter expert' who is responsible for coming up with the tests to be automated by the test automater."

*(Tradução completa em `raw/test-automater-xunitpatterns.md`.)*
