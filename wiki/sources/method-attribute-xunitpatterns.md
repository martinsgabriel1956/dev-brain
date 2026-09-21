---
type: source
title: "Method Attribute (xUnitPatterns.com — Gerard Meszaros)"
aliases: ["method attribute", "atributo de método", "xunit patterns glossary method attribute"]
date_created: 2026-09-21
date_updated: 2026-09-21
source_file: "raw/method-attribute-xunitpatterns.md"
source_url: "http://xunitpatterns.com/method%20attribute.html"
author: "Gerard Meszaros"
date_published: 2003-01-01
date_ingested: 2026-09-21
source_count: 0
tags: [testes, xunit, fonte-primaria, terminologia, glossario]
skill: tech-mentor-testing
status: stable
---

# Method Attribute (xUnitPatterns.com — Gerard Meszaros)

## TL;DR

Verbete curtíssimo do Glossário do xUnitPatterns.com que fecha o par terminológico deixado em aberto por [[wiki/sources/class-attribute-xunitpatterns|class attribute]] e [[wiki/sources/attribute-xunitpatterns|attribute]]: nomeia formalmente o sentido "annotation de método" já usado de passagem em [[wiki/sources/test-discovery-xunitpatterns]] e no concept [[wiki/concepts/test-method]]. Define **method attribute** como um [[wiki/sources/attribute-xunitpatterns|attribute]] colocado num método no código-fonte para dizer ao compilador ou ao runtime que esse método é "especial" — e cita a mesma aplicação já documentada alhures: em algumas variantes de xUnit, method attributes indicam que um método é um [[wiki/concepts/test-method|Test Method]] (o exemplo concreto `[Test]` do NUnit já estava na wiki via [[wiki/sources/test-discovery-xunitpatterns]], mas sem fonte primária isolada nomeando o mecanismo genérico).

---

## Afirmações Centrais

| Afirmação | Evidência | Fonte | Confiança |
|---|---|---|---|
| Method attribute é um attribute colocado num método no código-fonte, dizendo ao compilador/runtime que esse método é "especial" | "An attribute that is placed on a method in the source code to tell the compiler or runtime system that this method is 'special'" | fonte primária (Meszaros) | alta |
| Em algumas variantes de xUnit, method attributes indicam que um método é um Test Method | "In some variants of xUnit, method attributes are used to indicate that a method is a Test Method" | fonte primária | alta |

---

## Key Claims

### 1. Nomeia o mecanismo genérico por trás de um exemplo já documentado
[[wiki/sources/test-discovery-xunitpatterns]] já mostrava o exemplo concreto `[Test]` do NUnit (e sua combinação com `[ExpectedException(...)]`) como mecanismo de **Test Method Discovery** via method attribute, e [[wiki/concepts/test-method]] já citava "method attribute/annotation" de passagem na seção sobre reconhecimento de Test Methods. Nenhuma das duas fontes, porém, nomeava e definia formalmente o termo genérico "method attribute" em si — apenas o citavam como exemplo ou de passagem. Este verbete fecha essa lacuna terminológica isolada, definindo a categoria da qual `[Test]` é instância — espelhando exatamente o que [[wiki/sources/class-attribute-xunitpatterns]] já havia feito para `[TestFixture]` no nível de classe.

### 2. Fecha o par simétrico "class attribute ↔ method attribute" nomeado desde o início como termo irmão
[[wiki/sources/class-attribute-xunitpatterns]] já flagava, na sua seção de Questões Abertas, que "method attribute" seguia como termo irmão no índice de Glossário do site, ainda não ingerido isoladamente. Esta ingestão resolve exatamente essa pendência: os dois verbetes são definidos com a mesma estrutura de frase, variando apenas o alvo (classe vs. método) e a aplicação citada (Testcase Class vs. Test Method) — confirmando que o site trata os dois como o mesmo mecanismo genérico (attribute/annotation) aplicado em dois níveis distintos do código.

### 3. Definição de propósito ("dizer que o método é especial") é mais ampla que apenas Test Method Discovery
Assim como em [[wiki/sources/class-attribute-xunitpatterns]], a fonte generaliza o propósito de um method attribute para qualquer sinalização "este método é especial" ao compilador/runtime — a aplicação a Test Method Discovery é dada como exemplo ("in some variants of xUnit"), não como a única finalidade do mecanismo. É consistente com o uso mais amplo de attributes/annotations de método em .NET/Java fora do contexto de testes (ex.: `[HttpGet]`, `@Override`), embora a fonte não cite esses exemplos.

---

## Entidades Mencionadas

- [[wiki/entities/gerard-meszaros]] — autor do verbete; mesma fonte primária do catálogo já usada para dezenas de outros termos de glossário já ingeridos
- [[wiki/entities/nunit]] — framework já citado com o exemplo concreto `[Test]` (method attribute) em outras fontes da wiki

## Conceitos Tocados

- [[wiki/concepts/test-method]] — nomeia formalmente o mecanismo genérico (method attribute) por trás do exemplo `[Test]` já citado na seção de reconhecimento de Test Methods
- [[wiki/concepts/test-discovery]] — fecha o par simétrico com class attribute na seção de Test Method Discovery, nomeando o termo genérico do qual `[Test]` é instância

## Questões Abertas

- A fonte não cita exemplos de method attribute fora do contexto de teste (ex.: `[HttpGet]` em ASP.NET, `@Override` em Java) — a generalização "este método é especial" fica sem ilustração concreta além do caso de Test Method, espelhando a mesma lacuna já registrada em [[wiki/sources/class-attribute-xunitpatterns]].
- Com este verbete, o par annotation/attribute e o par class attribute/method attribute estão ambos fechados na wiki com fonte primária isolada; resta como pendência aberta apenas a comparação explícita entre os dois pares (attribute genérico vs. attribute com escopo — a fonte nunca declara essa relação hierárquica de forma explícita, apenas por justaposição de verbetes).

---

## Citações Relevantes

> "An attribute that is placed on a method in the source code to tell the compiler or runtime system that this method is 'special'. In some variants of xUnit, method attributes are used to indicate that a method is a Test Method."

*(Tradução completa em `raw/method-attribute-xunitpatterns.md`.)*
