---
type: source
title: "xUnit (xUnitPatterns.com — Gerard Meszaros)"
aliases: ["xunit", "xUnit framework family", "test automation framework family", "xunit patterns glossary xunit"]
date_created: 2026-08-31
date_updated: 2026-08-31
source_file: /home/nemomartins/Documentos/new/dev-study/raw/xunit-xunitpatterns.md
source_url: "http://xunitpatterns.com/xUnit.html"
author: "Gerard Meszaros"
date_published: 2003-01-01
date_ingested: 2026-08-31
source_count: 0
tags: [testes, xunit, junit, sunit, test-automation-framework, doc, fonte-primaria, terminologia]
skill: tech-mentor-testing
status: stable
---

# xUnit (xUnitPatterns.com — Gerard Meszaros)

## TL;DR

Verbete de glossário mais curto do catálogo xUnitPatterns.com ingerido até agora: define formalmente o próprio termo **xUnit** como "o nome genérico para qualquer Framework de Automação de Testes de teste de unidade baseado no padrão do **JUnit** ou **SUnit**". O valor real desta fonte não está na definição em si — já coberta em maior profundidade por [[wiki/sources/xunit-martin-fowler]] — mas em nomear explicitamente **SUnit** como o segundo ancestral formal da família, ao lado do JUnit. A wiki já documentava (via [[wiki/entities/kent-beck]] e [[wiki/entities/c3-project]]) que Beck construía "frameworks de teste caseiros em Smalltalk" antes do JUnit, mas nunca havia atribuído a esse framework caseiro o nome próprio pelo qual é historicamente conhecido: **SUnit**. Esta fonte fecha essa lacuna de nomenclatura.

---

## Afirmações Centrais

| Afirmação | Evidência | Fonte | Confiança |
|---|---|---|---|
| xUnit é o nome genérico para qualquer Test Automation Framework de unit testing baseado no padrão do JUnit ou SUnit | "The generic name for any Test Automation Framework for unit testing that is patterned on JUnit or SUnit" | fonte primária (Meszaros) | alta |
| Frameworks xUnit para a maioria das linguagens podem ser encontrados em xprogramming.com ou na Wikipedia | "The xUnit test framework for most languages can be found at http://xprogramming.com or http://en.wikipedia.org/wiki/XUnit" | fonte primária | alta |
| opensourcetesting.org é indicado como catálogo tanto de ferramentas de unit test quanto de customer test | "Another place to look for both unit test and customer test tools is http://www.opensourcetesting.org" | fonte primária | alta |

---

## Key Claims

### 1. SUnit, não só JUnit, é citado como ancestral formal do nome "xUnit"
Esta é a contribuição nova em relação ao que a wiki já sabia: o verbete nomeia **dois** frameworks-padrão de referência (JUnit **ou** SUnit), não só um. [[wiki/sources/xunit-martin-fowler]] já contava a origem histórica — Kent Beck construía "frameworks de teste caseiros em Smalltalk" antes do JUnit, usados no [[wiki/entities/c3-project|C3]] — mas nenhuma fonte ingerida até agora havia dado nome próprio a esse framework caseiro em Smalltalk. **SUnit** é esse nome, e esta fonte é a primeira a citá-lo explicitamente. Cria-se aqui o stub [[wiki/entities/sunit]] para fechar essa lacuna.

### 2. "xUnit" é definido por convenção de nomenclatura (o "x" é literal, um placeholder), não por uma especificação técnica formal
O verbete não define xUnit por uma lista de requisitos de API ou arquitetura — define por **linhagem**: qualquer framework que segue o *padrão* estabelecido por JUnit ou SUnit herda o nome (PyUnit, NUnit, CppUnit, etc., já listados na barra lateral do próprio site como "xUnit Members"). Isso é consistente com o relato de Fowler em [[wiki/sources/xunit-martin-fowler]] de que os ports variam "de traduções literais até adaptações sofisticadas" — a família se define por herança de padrão, não por conformidade estrita a uma interface.

### 3. O site distingue explicitamente "unit test tools" de "customer test tools" como duas categorias de catálogo separadas
Reforça, de fonte primária, a mesma distinção já formalizada em [[wiki/sources/unit-test-xunitpatterns]] (unit test vs. customer test pelo tamanho do SUT) — aqui aplicada não à definição de teste, mas à categorização de ferramentas: xUnit cobre a categoria de unit testing; customer test tools são uma família de ferramentas distinta, catalogada à parte.

---

## Entidades Mencionadas

- [[wiki/entities/gerard-meszaros]] — autor do verbete; mesma fonte primária do catálogo já usada para [[wiki/sources/sut-xunitpatterns]], [[wiki/sources/unit-test-xunitpatterns]] e demais verbetes do glossário
- [[wiki/entities/junit]] — citado nominalmente como um dos dois frameworks-padrão de referência da família
- [[wiki/entities/sunit]] — citado nominalmente como o segundo framework-padrão de referência; stub criado nesta ingestão
- [[wiki/entities/kent-beck]] — criador do SUnit (framework caseiro em Smalltalk que antecedeu o JUnit)

## Conceitos Tocados

- [[wiki/concepts/test-doubles]] — a taxonomia inteira de Meszaros é descrita no site como parte do catálogo "xUnit Test Patterns"; este verbete formaliza o nome da própria família de frameworks ao redor da qual a taxonomia foi escrita
- [[wiki/concepts/unit-test-solitario-vs-sociavel]] — via [[wiki/sources/unit-test-xunitpatterns]], a distinção unit test/customer test reaparece aqui aplicada à categorização de ferramentas

## Questões Abertas

- **SUnit não tem, até esta ingestão, nenhuma fonte primária própria isolada** — sua existência é inferida por citação cruzada (este verbete + o relato não-nomeado de Fowler em [[wiki/sources/xunit-martin-fowler]]). Candidato a ingestão futura se o site xUnitPatterns.com tiver um verbete de glossário próprio para "SUnit" (não confirmado — não visto na barra lateral "xUnit Members" da página coletada).
- O verbete não distingue "xUnit" (o padrão/família) de "XUnit" (a página da Wikipedia citada usa capitalização diferente) — tratado aqui como o mesmo termo, variação apenas de estilo de capitalização.

---

## Citações Relevantes

> "The generic name for any Test Automation Framework for unit testing that is patterned on JUnit or SUnit."

> "The xUnit test framework for most languages can be found at http://xprogramming.com or http://en.wikipedia.org/wiki/XUnit."

> "Another place to look for both unit test and customer test tools is http://www.opensourcetesting.org."

*(Tradução completa em `raw/xunit-xunitpatterns.md`.)*
