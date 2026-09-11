---
type: source
title: "Substitutable Dependency (xUnitPatterns.com — Gerard Meszaros)"
aliases: ["substitutable dependency", "dependência substituível", "xunit patterns glossary substitutable dependency"]
date_created: 2026-09-11
date_updated: 2026-09-11
source_file: /home/nemomartins/Documentos/new/dev-study/raw/substitutable-dependency-xunitpatterns.md
source_url: "http://xunitpatterns.com/substitutable%20dependency.html"
author: "Gerard Meszaros"
date_published: 2003-01-01
date_ingested: 2026-09-11
source_count: 0
tags: [testes, test-doubles, dependency-injection, dependency-lookup, test-specific-subclass, xunit, fonte-primaria, terminologia]
skill: tech-mentor-testing
status: stable
---

# Substitutable Dependency (xUnitPatterns.com — Gerard Meszaros)

## TL;DR

Verbete curto do Glossário do catálogo xUnitPatterns.com que define formalmente **substitutable dependency** (dependência substituível): a propriedade de um [[wiki/concepts/test-doubles|DOC]] poder ser trocado por um [[wiki/concepts/test-doubles|Test Double]] quando se quer testar o componente que depende dele isoladamente. O termo já era citado de passagem em pelo menos três fontes já ingeridas — [[wiki/sources/test-double-xunitpatterns-meszaros]], [[wiki/sources/test-stub-xunitpatterns-meszaros]] e [[wiki/sources/replace-dependency-with-test-double-xunitpatterns]] — sem nunca ter fonte primária dedicada. Esta ingestão fecha essa lacuna e nomeia explicitamente os três mecanismos catalogados por Meszaros para tornar uma dependência substituível: [[wiki/concepts/dependency-injection|Dependency Injection]], [[wiki/concepts/dependency-lookup|Dependency Lookup]] e [[wiki/concepts/test-specific-subclass|Test-Specific Subclass]] — o terceiro mecanismo, até agora não nomeado em nenhuma fonte da wiki (as fontes anteriores só citavam DI vs. Dependency Lookup).

---

## Afirmações Centrais

| Afirmação | Evidência | Fonte | Confiança |
|---|---|---|---|
| Um componente pode depender de qualquer número de outros componentes; testá-lo isoladamente exige poder substituir essas dependências por um Test Double | "A software component may depended on any number of other components. If we are to test this component by itself, we need to be able to replace the other components with a Test Double" | fonte primária (Meszaros) | alta |
| Existem várias formas de tornar algo uma substitutable dependency, incluindo Dependency Injection, Dependency Lookup e Test-Specific Subclass | "There are several ways that we can make something into a substitutable dependency including Dependency Injection, Dependency Lookup and Test-Specific Subclass" | fonte primária | alta |

---

## Key Claims

### 1. "Substitutable dependency" é a propriedade, não a técnica
O termo não nomeia uma técnica específica — nomeia a **característica de design** que o SUT precisa ter para que qualquer uma das técnicas funcione. Isso alinha exatamente com o uso que a wiki já fazia do termo antes desta fonte: em [[wiki/sources/test-double-xunitpatterns-meszaros]], a instalação do double era descrita como "usar qualquer um dos padrões de dependência substituível", tratando o termo como uma categoria guarda-chuva, não como um padrão único — o que esta fonte confirma formalmente.

### 2. Terceiro mecanismo nomeado: Test-Specific Subclass, até agora sem menção própria
As fontes já ingeridas sobre o "como" instalar um Test Double ([[wiki/sources/replace-dependency-with-test-double-xunitpatterns]]) só documentavam dois mecanismos — Dependency Injection e Dependency Lookup — e registravam isso como possível lacuna. Este verbete revela que o catálogo de Meszaros considera um **terceiro** mecanismo formal: **Test-Specific Subclass**, técnica em que o próprio SUT (ou uma subclasse dele usada só em teste) sobrescreve o ponto onde a dependência real seria criada/obtida, tornando-a substituível sem depender de um mecanismo de injeção externo.

### 3. Fecha, com fonte primária isolada, um termo citado repetidamente sem definição própria
Diferente de "control point" ou "DOC" — que também eram citados de passagem antes de ganharem fonte dedicada —, "substitutable dependency" tinha um padrão de uso ainda mais recorrente: aparecia em pelo menos três key claims espalhados por fontes distintas, sempre como pressuposto (a necessidade de a dependência **já ser** substituível), nunca como o objeto sendo definido. Esta é a primeira fonte que o define diretamente, em vez de assumi-lo.

---

## Entidades Mencionadas

- [[wiki/entities/gerard-meszaros]] — autor do verbete; mesma fonte primária do catálogo já usada para [[wiki/sources/test-double-xunitpatterns-meszaros]], [[wiki/sources/control-point-xunitpatterns]] e [[wiki/sources/depended-on-component-doc-xunitpatterns]]

## Conceitos Tocados

- [[wiki/concepts/test-doubles]] — substitutable dependency é a pré-condição de design que viabiliza instalar qualquer Test Double
- [[wiki/concepts/dependency-injection]] — um dos três mecanismos nomeados nesta fonte
- [[wiki/concepts/dependency-lookup]] — um dos três mecanismos nomeados nesta fonte; primeira fonte a lhe dar menção formal própria (ainda sem página dedicada antes desta ingestão)
- [[wiki/concepts/test-specific-subclass]] — terceiro mecanismo, sem menção prévia em nenhuma fonte já ingerida na wiki

## Questões Abertas

- O verbete não detalha **como** o Test-Specific Subclass funciona mecanicamente (qual método é sobrescrito, se exige um construtor especial de teste, etc.) — só o nomeia. Uma fonte primária dedicada ao termo "Test-Specific Subclass" (se existir no catálogo) fecharia essa lacuna, assim como já existe para "Dependency Lookup" nesta mesma pendência.
- A fonte não explica por que DI é preferida para unit tests e Dependency Lookup para customer tests (já registrado como lacuna em [[wiki/sources/replace-dependency-with-test-double-xunitpatterns]]); tampouco situa onde Test-Specific Subclass se encaixa nessa preferência por nível de teste.

---

## Citações Relevantes

> "A software component may depended on any number of other components. If we are to test this component by itself, we need to be able to replace the other components with a Test Double."

> "There are several ways that we can make something into a substitutable dependency including Dependency Injection, Dependency Lookup and Test-Specific Subclass."

*(Tradução completa em `raw/substitutable-dependency-xunitpatterns.md`.)*
