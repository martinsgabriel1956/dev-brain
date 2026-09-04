---
type: source
title: "Customer Test (xUnitPatterns.com — Gerard Meszaros)"
aliases: ["customer test", "teste de cliente", "story test", "acceptance test", "xunit patterns glossary customer test"]
date_created: 2026-09-02
date_updated: 2026-09-02
source_file: /home/nemomartins/Documentos/new/dev-study/raw/customer-test-xunitpatterns.md
source_url: "http://xunitpatterns.com/customer%20test.html"
author: "Gerard Meszaros"
date_published: 2003-01-01
date_ingested: 2026-09-02
source_count: 0
tags: [testes, customer-test, sut, xunit, fonte-primaria, terminologia]
skill: tech-mentor-testing
status: stable
---

# Customer Test (xUnitPatterns.com — Gerard Meszaros)

## TL;DR

Verbete curto do Glossário do catálogo xUnitPatterns.com que fecha, de fonte primária isolada, o par de termos citado por contraste em [[wiki/sources/unit-test-xunitpatterns]] e [[wiki/sources/sut-xunitpatterns]] desde que foram ingeridos: **customer test**. Define-se por dois critérios, não um: (1) **escopo** — verifica uma fatia da funcionalidade *visível* do sistema geral, com o [[wiki/sources/sut-xunitpatterns|SUT]] sendo o sistema inteiro ou um módulo funcional de ponta a ponta; (2) **independência de design** — o mesmo conjunto de customer tests deveria ser exigido não importa como o SUT é construído por dentro, embora a *interação* com o SUT possa mudar conforme decisões de arquitetura de alto nível. É o segundo critério, não o primeiro, que é a contribuição mais nova desta fonte: nenhuma outra fonte da wiki havia formalizado "independência das decisões de design" como propriedade definidora de um tipo de teste.

---

## Afirmações Centrais

| Afirmação | Evidência | Fonte | Confiança |
|---|---|---|---|
| Customer test verifica o comportamento de uma fatia da funcionalidade visível do sistema geral | "A test that verifies the behavior of a slice of the visible functionality of the overall system" | fonte primária (Meszaros) | alta |
| O SUT de um customer test pode ser o sistema inteiro ou uma fatia/módulo totalmente funcional de ponta a ponta | "The system under test (SUT) may be the entire system or a fully-functional top-to-bottom slice (or 'module') of the system" | fonte primária | alta |
| Um customer test deve ser independente das decisões de design tomadas ao construir o SUT — o mesmo conjunto de testes deveria valer não importa como o SUT é construído | "A customer test should be independent of the design decisions made while building the SUT. That is, we should require the same set of customer tests regardless of how we choose to build the SUT" | fonte primária | alta |
| Decisões de arquitetura de software de alto nível podem afetar como os customer tests interagem com o SUT, mesmo sem mudar quais testes existem | "But how the customer tests interact with the SUT may be affected by high-level software architecture decisions" | fonte primária | alta |

---

## Key Claims

### 1. "Visível" é o critério de escopo, e ele é definido pelo oposto exato de unit test
[[wiki/sources/unit-test-xunitpatterns]] já registrava, por contraste interno ao próprio verbete de unit test, que customer test é "derivado quase inteiramente dos requisitos" e "deveria ser verificável pelo cliente". Esta fonte, isolada, reformula o mesmo contraste em termos de escopo do SUT: unit test mede o SUT em classe/objeto/método (possivelmente irreconhecível para quem não constrói o software); customer test mede o SUT em "sistema inteiro" ou "módulo funcional de ponta a ponta" — sempre algo que um humano de fora do time de construção reconheceria como funcionalidade. Os dois verbetes, lidos juntos, formam um par de definição mútua completo: nenhum dos dois é definido sozinho, sempre em oposição ao outro.

### 2. Independência de design é uma propriedade normativa, não apenas descritiva — e é a peça que faltava na wiki
Diferente de SUT, unit test, test, control point etc. — todos verbetes que descrevem *o que uma coisa é* — este verbete inclui uma prescrição: "deveríamos exigir o mesmo conjunto de customer tests independentemente de como escolhemos construir o SUT". Isso formaliza a ideia (já presente implicitamente em [[wiki/concepts/piramide-de-testes]] como "customer test no topo verifica o fluxo do usuário, não a implementação") de que customer tests são a especificação executável dos requisitos — um contrato que sobrevive a um reescrita completa do SUT por dentro. É consistente com a definição de [[wiki/sources/unit-test-xunitpatterns|unit test]] (o SUT real "é consequência de uma ou mais decisões de design"): unit tests *dependem* do design; customer tests devem ser *agnósticos* a ele.

### 3. A ressalva final evita uma leitura absoluta demais da independência de design
A fonte faz questão de qualificar a própria afirmação: a *arquitetura* de alto nível pode, sim, afetar *como* os testes interagem com o SUT (ex.: entrar via UI web vs. via API headless vs. via fila de mensagens), mesmo que o *conjunto* de testes continue o mesmo. Essa distinção entre "o quê" (constante) e "como interagir" (variável com a arquitetura) evita a leitura ingênua de que customer tests seriam totalmente cegos à arquitetura do sistema — só são cegos às decisões de design *internas* ao SUT, não à forma de acesso externo a ele.

---

## Entidades Mencionadas

- [[wiki/entities/gerard-meszaros]] — autor do verbete; mesma fonte primária do catálogo já usada para [[wiki/sources/sut-xunitpatterns]], [[wiki/sources/unit-test-xunitpatterns]] e demais verbetes do glossário

## Conceitos Tocados

- [[wiki/concepts/piramide-de-testes]] — customer test é a definição formal do topo da pirâmide (E2E/aceitação), agora com fonte primária isolada em vez de apenas inferida do contraste com unit test
- [[wiki/concepts/extreme-programming]] — em XP, customer tests são historicamente o teste que o cliente/domain expert ajuda a especificar (papel também citado em [[wiki/sources/test-automater-xunitpatterns|test automater/subject matter expert]])

## Questões Abertas

- **"acceptance test" e "story test"** seguem no índice de Glossário do site como termos irmãos ainda não ingeridos isoladamente — a fonte de customer test não afirma explicitamente que são sinônimos, apenas os menciona en passant em fontes cruzadas já ingeridas (ex.: aliases citados em unit-test); permanece em aberto se o glossário os trata como sinônimos estritos ou como variações com nuance própria.
- A fonte não dá exemplo concreto do que significa "decisão de arquitetura de alto nível" afetando a interação — deixa implícito (ex.: testar via GUI vs. via camada de serviço), mas não cita nenhum caso.

---

## Citações Relevantes

> "A test that verifies the behavior of a slice of the visible functionality of the overall system. The system under test (SUT) may be the entire system or a fully-functional top-to-bottom slice (or 'module') of the system."

> "A customer test should be independent of the design decisions made while building the SUT. That is, we should require the same set of customer tests regardless of how we choose to build the SUT. (But how the customer tests interact with the SUT may be affected by high-level software architecture decisions.)"

*(Tradução completa em `raw/customer-test-xunitpatterns.md`.)*
