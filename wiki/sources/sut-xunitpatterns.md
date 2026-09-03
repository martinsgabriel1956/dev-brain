---
type: source
title: "SUT — System Under Test (xUnitPatterns.com — Gerard Meszaros)"
aliases: ["SUT", "system under test", "sistema sob teste", "AUT", "MUT", "CUT", "xunit patterns glossary SUT"]
date_created: 2026-08-31
date_updated: 2026-08-31
source_file: /home/nemomartins/Documentos/new/dev-study/raw/sut-xunitpatterns.md
source_url: "http://xunitpatterns.com/SUT.html"
author: "Gerard Meszaros"
date_published: 2003-01-01
date_ingested: 2026-08-31
source_count: 0
tags: [testes, test-doubles, sut, doc, xunit, fonte-primaria, terminologia]
skill: tech-mentor-testing
status: stable
---

# SUT — System Under Test (xUnitPatterns.com — Gerard Meszaros)

## TL;DR

Verbete curto do Glossário do catálogo xUnitPatterns.com que define formalmente **SUT (system under test)**: o termo já usado o tempo todo em [[wiki/concepts/test-doubles]] e [[wiki/concepts/indirect-input-output]], mas até agora sem uma citação primária isolada dedicada só a ele. A fonte fixa dois pontos que a wiki ainda não tinha formalizado: (1) SUT é **sempre definido a partir da perspectiva do teste** — não é uma propriedade fixa do código, e sim um papel relativo a qual teste está rodando; (2) o **escopo do SUT muda com a granularidade do teste** — em um teste de unidade é uma classe (**CUT**), objeto (**OUT**) ou método(s) (**MUT**); em um teste de cliente/aceitação é a aplicação inteira (**AUT**) ou um subsistema grande. Fecha, junto com [[wiki/sources/doc-xunitpatterns]], o par de termos que organiza toda a taxonomia de [[wiki/concepts/test-doubles|Test Double]].

---

## Afirmações Centrais

| Afirmação | Evidência | Fonte | Confiança |
|---|---|---|---|
| SUT é "seja lá o que for que estamos testando", sempre definido a partir da perspectiva do teste | "It is short for 'whatever thing we are testing' and is always defined from the perspective of the test" | fonte primária (Meszaros) | alta |
| Em unit tests, o SUT é a classe (CUT), objeto (OUT) ou método(s) (MUT) sendo testado | "the system under test (SUT) is whatever class (a.k.a. CUT), object (a.k.a. OUT) or method(s) (a.k.a. MUT) we are testing" | fonte primária | alta |
| Em customer tests, o SUT é provavelmente a aplicação inteira (AUT) ou um subsistema importante | "the SUT is probably the entire application (a.k.a. AUT) or at least a major subsystem of it" | fonte primária | alta |
| Partes da aplicação não verificadas no teste em questão ainda podem estar envolvidas como DOC | "The parts of the application that we are not verifying in this particular test may still be involved as a depended-on component (DOC)" | fonte primária | alta |

---

## Key Claims

### 1. SUT é um papel relativo ao teste, não uma propriedade fixa do código
A definição "sempre definido a partir da perspectiva do teste" é o ponto mais importante do verbete e o que faltava formalizar na wiki: a mesma classe pode ser SUT em um teste e DOC em outro teste que exercita uma classe vizinha. SUT/DOC não são categorias do design, são papéis atribuídos pelo teste que está rodando — reforça a definição de DOC já isolada em [[wiki/sources/doc-xunitpatterns]] ("classe da qual o SUT depende": a relação é sempre relativa a um teste específico).

### 2. O escopo do SUT escala com a granularidade do teste (unit → customer)
A fonte amarra explicitamente o tamanho do SUT ao tipo de teste: unit test → classe/objeto/método; customer test → aplicação inteira ou subsistema grande. Isso formaliza algo que a wiki já tratava implicitamente em [[wiki/concepts/piramide-de-testes]] (camadas com granularidades diferentes), mas nunca havia amarrado ao próprio vocabulário SUT/DOC — o mesmo par de termos vale em qualquer nível da pirâmide, só muda o tamanho do que cada lado do par representa.

### 3. Três siglas irmãs nunca antes documentadas na wiki: CUT, MUT, AUT
Nenhuma menção prévia a **AUT** (*application under test*), **MUT** (*method(s) under test*) ou **CUT** (*class under test*) existia na wiki antes desta fonte — só "SUT" e "DOC" apareciam nas fontes já ingeridas. São variações de granularidade do mesmo conceito, não termos concorrentes: útil para reconhecer essas siglas em código/discussões que preferem o nome mais específico ao genérico "SUT".

---

## Entidades Mencionadas

- [[wiki/entities/gerard-meszaros]] — autor do verbete; mesma fonte primária do catálogo já usada para [[wiki/sources/test-double-xunitpatterns-meszaros]], [[wiki/sources/test-stub-xunitpatterns-meszaros]], [[wiki/sources/doc-xunitpatterns]], [[wiki/sources/control-point-xunitpatterns]], [[wiki/sources/fixture-setup-xunitpatterns]] e [[wiki/sources/indirect-input-xunitpatterns]]

## Conceitos Tocados

- [[wiki/concepts/test-doubles]] — SUT é a metade do par SUT/DOC que organiza toda a taxonomia; ganha aqui a definição formal isolada e as siglas irmãs (AUT/MUT/CUT)
- [[wiki/concepts/indirect-input-output]] — o eixo entrada/saída indireta é sempre relativo ao SUT deste verbete; ganha a nota de que o escopo do SUT varia com a granularidade do teste
- [[wiki/concepts/piramide-de-testes]] — a escala unit → customer test citada na fonte é a mesma que organiza as camadas da pirâmide

## Questões Abertas

- **OUT** (*object under test*) é citado no texto mas não recebe entrada própria no índice de Glossário do site (só aparece dentro do verbete de SUT) — tratado aqui como sigla irmã de mesmo peso que CUT/MUT, sem fonte primária isolada própria.
- Os verbetes irmãos "observation point", "indirect output", "direct input" e "fixture teardown" do mesmo glossário seguem sem fonte primária isolada ingerida (lacuna já registrada em ingests anteriores — ver [[wiki/concepts/indirect-input-output]]).

---

## Citações Relevantes

> "The 'system under test'. It is short for 'whatever thing we are testing' and is always defined from the perspective of the test."

> "When we are writing unit tests the system under test (SUT) is whatever class (a.k.a. CUT), object (a.k.a. OUT) or method(s) (a.k.a. MUT) we are testing; when we are writing customer tests, the SUT is probably the entire application (a.k.a. AUT) or at least a major subsystem of it."

> "The parts of the application that we are not verifying in this particular test may still be involved as a depended-on component (DOC)."

*(Tradução completa em `raw/sut-xunitpatterns.md`.)*
