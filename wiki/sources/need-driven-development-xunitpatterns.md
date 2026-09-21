---
type: source
title: "Need-Driven Development (xUnitPatterns.com — Gerard Meszaros)"
aliases: ["need-driven development", "NDD", "desenvolvimento guiado por necessidade"]
date_created: 2026-09-21
date_updated: 2026-09-21
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/need-driven-development-xunitpatterns.md
source_url: "http://xunitpatterns.com/need-driven%20development.html"
author: "Gerard Meszaros"
date_published: 2003-01-01
date_ingested: 2026-09-21
source_count: 0
tags: [testes, tdd, mock-object, outside-in, xunit, fonte-primaria, terminologia, glossario]
skill: tech-mentor-testing
status: stable
---

# Need-Driven Development (xUnitPatterns.com — Gerard Meszaros)

## TL;DR

Verbete de Glossário do xUnitPatterns.com que nomeia formalmente, pela primeira vez com fonte primária isolada na wiki, a variação **outside-in / London School** de [[wiki/concepts/tdd|TDD]] já descrita informalmente na seção "As duas escolas" de [[wiki/concepts/tdd]]: **need-driven development**. A definição amarra três peças que a wiki já tinha separadas — [[wiki/concepts/test-doubles|Mock Object]], [[wiki/concepts/indirect-input-output|indirect output]] e [[wiki/concepts/storytest-driven-development|storytest-driven development]] — num único fluxo de processo com uma justificativa explícita: cada unidade só é codificada depois que suas responsabilidades já são bem compreendidas, evidenciadas tanto por unit tests quanto por exemplos de uso real. A camada mais externa do sistema fecha esse fluxo usando storytest-driven development, com exemplos de uso por clientes reais (citando **Service Facade** [CJ2EEP] como exemplo concreto) somados aos [[wiki/sources/customer-test-xunitpatterns|customer tests]].

---

## Afirmações Centrais

| Afirmação | Evidência | Fonte | Confiança |
|---|---|---|---|
| Need-driven development é uma variação do test-driven development | "A variation on the test-driven development process" | fonte primária (Meszaros) | alta |
| O código é escrito de fora para dentro (outside in) | "code is written from the outside in" | fonte primária | alta |
| Todo código dependente é substituído por Mock Objects que verificam os indirect outputs esperados do código sendo escrito | "all depended-on code is replaced by Mock Objects that verify the expected indirect outputs of the code being written" | fonte primária | alta |
| Isso garante que as responsabilidades de cada unidade sejam bem compreendidas antes de serem codificadas, via unit tests e exemplos de uso real | "This ensures that the responsibilities of each software unit are well understood before they are coded by virtue of having both unit tests and examples of real usage" | fonte primária | alta |
| A camada mais externa do software é escrita usando storytest-driven development e deve ter exemplos de uso por clientes reais além dos customer tests | "The outermost layer of software is written using storytest-driven development and should also have examples of usage by real clients (...) in addition to the customer tests" | fonte primária | alta |

---

## Key Claims

### 1. Fecha, com fonte primária dedicada, um termo que a wiki só descrevia informalmente
[[wiki/concepts/tdd]] já documentava a distinção Detroit/London (Inside-Out vs. Outside-In) e citava, na seção "As duas escolas", que na escola London "o design emerge das interfaces que o teste exige" — mas sem nomear formalmente esse processo. Este verbete fornece exatamente esse nome, de fonte primária isolada de Meszaros: **need-driven development**. É o mesmo processo, agora com definição oficial do catálogo, em vez de apenas inferido por contraste com Detroit School.

### 2. Conecta explicitamente três conceitos que a wiki já tinha, mas nunca ligados num único fluxo nomeado
A definição amarra, numa única frase, mecanismos que já existiam isoladamente na wiki: [[wiki/concepts/test-doubles|Mock Object]] (já com taxonomia completa via [[wiki/sources/test-double-xunitpatterns-meszaros]]) e [[wiki/concepts/indirect-input-output|indirect output]] (já com fonte primária isolada) como o mecanismo técnico; [[wiki/concepts/storytest-driven-development]] como o processo complementar que cobre a camada mais externa. Nenhuma fonte anterior já ingerida havia declarado explicitamente que esses três elementos formam, juntos, um processo de desenvolvimento com nome próprio.

### 3. Introduz "Service Facade [CJ2EEP]" como novo exemplo de interface acionada por clientes reais, sem página própria na wiki
O verbete cita, como exemplo concreto de "uma interface de usuário acionando a Service Facade", o padrão **Service Facade** do livro *Core J2EE Patterns* (citado pela sigla **[CJ2EEP]**, seguindo a mesma convenção de citação por sigla já vista em [[wiki/sources/utwhcm-xunitpatterns|[UTwHCM]]]). Nem o padrão Service Facade nem o livro *Core J2EE Patterns* têm página própria na wiki até esta ingestão — candidato a lacuna futura, registrado como questão aberta abaixo.

### 4. Dupla verificação: unit tests + "exemplos de uso real" como evidência de compreensão de responsabilidade
O verbete afirma que a garantia de responsabilidades bem compreendidas vem de **duas** fontes, não uma: unit tests (verificação formal) e exemplos de uso real (evidência de aplicabilidade prática). Essa dualidade ecoa o próprio espírito de [[wiki/concepts/storytest-driven-development]] — que exige não apenas unidades corretas isoladamente, mas um "todo utilizável" do ponto de vista de quem usa o sistema — mas aqui aplicada explicitamente também ao nível de unidade interna, não só à camada mais externa.

---

## Entidades Mencionadas

- [[wiki/entities/gerard-meszaros]] — autor do verbete; mesma fonte primária do catálogo já usada para dezenas de outros termos de glossário já ingeridos

## Conceitos Tocados

- [[wiki/concepts/tdd]] — need-driven development nomeia formalmente a variação outside-in/London School já descrita informalmente na página
- [[wiki/concepts/test-doubles]] — Mock Object é o mecanismo técnico central do processo
- [[wiki/concepts/indirect-input-output]] — indirect output é o que os Mock Objects verificam
- [[wiki/concepts/storytest-driven-development]] — processo complementar que cobre a camada mais externa do software

## Questões Abertas

- **Service Facade [CJ2EEP] não tem página própria na wiki** — citado apenas como exemplo de passagem, sem elaboração do próprio verbete sobre o padrão em si. *Core J2EE Patterns* (Alur, Malks, Crupi) também não está catalogado como entidade/fonte.
- O verbete não esclarece se "need-driven development" é sinônimo estrito de "outside-in TDD"/"London School" ou um termo distinto com nuance própria — a wiki assume equivalência com base na descrição do processo, mas nenhuma fonte confirma essa equivalência terminológica diretamente.

---

## Citações Relevantes

> "A variation on the test-driven development process where code is written from the outside in and all depended-on code is replaced by Mock Objects that verify the expected indirect outputs of the code being written."

> "This ensures that the responsibilities of each software unit are well understood before they are coded by virtue of having both unit tests and examples of real usage. The outermost layer of software is written using storytest-driven development and should also have examples of usage by real clients (e.g. a user interface driving the Service Facade[CJ2EEP]) in addition to the customer tests."

*(Tradução completa em `raw/need-driven-development-xunitpatterns.md`.)*
