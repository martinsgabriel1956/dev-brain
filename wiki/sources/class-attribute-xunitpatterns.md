---
type: source
title: "Class Attribute (xUnitPatterns.com — Gerard Meszaros)"
aliases: ["class attribute", "atributo de classe", "xunit patterns glossary class attribute"]
date_created: 2026-09-21
date_updated: 2026-09-21
source_file: "raw/class-attribute-xunitpatterns.md"
source_url: "http://xunitpatterns.com/class%20attribute.html"
author: "Gerard Meszaros"
date_published: 2003-01-01
date_ingested: 2026-09-21
source_count: 1
tags: [testes, xunit, fonte-primaria, terminologia, glossario]
skill: tech-mentor-testing
status: stable
---

# Class Attribute (xUnitPatterns.com — Gerard Meszaros)

## TL;DR

Verbete curtíssimo do Glossário do xUnitPatterns.com que isola o primeiro dos dois sentidos de **[[wiki/sources/attribute-xunitpatterns|attribute]]** já registrado na wiki — o sentido "annotation de classe" — e o nomeia explicitamente como **class attribute**: um attribute colocado numa classe no código-fonte para dizer ao compilador ou ao runtime que essa classe é "especial". A aplicação citada é exatamente a já documentada em [[wiki/entities/nunit]] e [[wiki/concepts/test-discovery]]: em algumas variantes de xUnit, class attributes indicam que uma classe é uma [[wiki/sources/testcase-class-xunitpatterns|Testcase Class]] — o exemplo concreto (`[TestFixture]` do NUnit) já estava na wiki, mas sem fonte primária isolada nomeando o mecanismo genérico "class attribute" em si.

---

## Afirmações Centrais

| Afirmação | Evidência | Fonte | Confiança |
|---|---|---|---|
| Class attribute é um attribute colocado numa classe no código-fonte, dizendo ao compilador/runtime que essa classe é "especial" | "An attribute that is placed on a class in the source code to tell the compiler or runtime system that this class is 'special'" | fonte primária (Meszaros) | alta |
| Em algumas variantes de xUnit, class attributes indicam que uma classe é uma Testcase Class | "In some variants of xUnit, class attributes are used to indicate that a class is a Testcase Class" | fonte primária | alta |

---

## Key Claims

### 1. Nomeia o mecanismo genérico por trás de um exemplo já documentado
[[wiki/sources/test-discovery-xunitpatterns]] já mostrava o exemplo concreto `[TestFixture]` do NUnit como mecanismo de **Testcase Class Discovery** via class attribute, e [[wiki/entities/nunit]] já documentava esse mesmo atributo. Nenhuma das duas fontes, porém, nomeava e definia formalmente o termo genérico "class attribute" em si — apenas o citavam de passagem ou davam o exemplo específico. Este verbete fecha essa lacuna terminológica isolada, definindo a categoria da qual `[TestFixture]` é instância.

### 2. Fecha o par terminológico "genérico → específico" já aberto por [[wiki/sources/attribute-xunitpatterns]]
A fonte de "attribute" já registrava dois sentidos possíveis do termo genérico: annotation de classe/método, ou sinônimo de instance variable. Este verbete se aprofunda especificamente no primeiro sentido, mas restrito ao nível de **classe** (não de método) — complementar ao par ainda não ingerido isoladamente, "method attribute", citado no Glossário do mesmo site como termo irmão.

### 3. Definição de propósito ("dizer que a classe é especial") é mais ampla que apenas Testcase Class Discovery
A fonte generaliza o propósito de um class attribute para qualquer sinalização "esta classe é especial" ao compilador/runtime — a aplicação a Testcase Class Discovery é dada como exemplo ("in some variants of xUnit"), não como a única finalidade do mecanismo. Isso é consistente com o uso mais amplo de attributes/annotations de classe em .NET/Java fora do contexto de testes (ex.: `[Serializable]`, `@Entity`), embora a fonte não cite esses exemplos.

---

## Entidades Mencionadas

- [[wiki/entities/gerard-meszaros]] — autor do verbete; mesma fonte primária do catálogo já usada para dezenas de outros termos de glossário já ingeridos
- [[wiki/entities/nunit]] — framework já citado com o exemplo concreto `[TestFixture]` (class attribute) em outras fontes da wiki

## Conceitos Tocados

- [[wiki/concepts/test-discovery]] — nomeia formalmente o mecanismo genérico (class attribute) por trás do exemplo `[TestFixture]` já documentado como uma das soluções de Testcase Class Discovery

## Questões Abertas

- ~~**"method attribute"** segue como termo irmão no índice de Glossário do site, ainda não ingerido isoladamente~~ — resolvido: [[wiki/sources/method-attribute-xunitpatterns]] ingerida em 2026-09-21, completando o par genérico/específico ao lado de class attribute, análogo ao já fechado entre annotation/attribute.
- A fonte não cita exemplos de class attribute fora do contexto de teste (ex.: `[Serializable]` em .NET) — a generalização "esta classe é especial" fica sem ilustração concreta além do caso de Testcase Class.

---

## Citações Relevantes

> "An attribute that is placed on a class in the source code to tell the compiler or runtime system that this class is 'special'. In some variants of xUnit, class attributes are used to indicate that a class is a Testcase Class."

*(Tradução completa em `raw/class-attribute-xunitpatterns.md`.)*
