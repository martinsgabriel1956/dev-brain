---
type: source
title: "Test Case (xUnitPatterns.com — Gerard Meszaros)"
aliases: ["test case", "caso de teste", "testcase class", "xunit patterns glossary test case"]
date_created: 2026-08-31
date_updated: 2026-08-31
source_file: /home/nemomartins/Documentos/new/dev-study/raw/test-case-xunitpatterns.md
source_url: "http://xunitpatterns.com/test%20case.html"
author: "Gerard Meszaros"
date_published: 2003-01-01
date_ingested: 2026-08-31
source_count: 1
tags: [testes, test-case, xunit, fonte-primaria, terminologia]
skill: tech-mentor-testing
status: stable
---

# Test Case (xUnitPatterns.com — Gerard Meszaros)

## TL;DR

Verbete de glossário do catálogo xUnitPatterns.com dedicado ao termo **test case**. Confirma o que já havia sido inferido em [[wiki/sources/test-xunitpatterns]]: "test case" é geralmente um sinônimo de **test**. Mas acrescenta um segundo sentido específico do XUnit: pode se referir a uma **Testcase Class**, que é na verdade uma **Test Suite Factory** e também o lugar onde ficam agrupados **Test Methods** relacionados — introduzindo três termos novos ainda sem verbete próprio ingerido na wiki.

---

## Afirmações Centrais

| Afirmação | Evidência | Fonte | Confiança |
|---|---|---|---|
| "Test case" é geralmente sinônimo de "test" | "Usually a synonym for test" | fonte primária (Meszaros) | alta |
| No XUnit, "test case" também pode se referir a uma Testcase Class | "In XUnit, it may also refer to a Testcase Class" | fonte primária | alta |
| Uma Testcase Class é, na verdade, uma Test Suite Factory | "which is actually a Test Suite Factory" | fonte primária | alta |
| Uma Testcase Class também é o lugar onde se agrupam Test Methods relacionados | "as well as a place to put a set of related Test Methods" | fonte primária | alta |

---

## Key Claims

### 1. "Test case" tem dois sentidos distintos no vocabulário XUnit, não um só
A definição em [[wiki/sources/test-xunitpatterns]] tratava "test" e "test case" como puros sinônimos. Este verbete refina isso: o sentido genérico (sinônimo de teste) coexiste com um sentido técnico específico do XUnit — a **Testcase Class**, uma unidade estrutural de código (a classe que agrupa métodos de teste), não o teste individual em si. Isso resolve a lacuna que o verbete de "test" havia deixado aberta.

### 2. Testcase Class é uma Test Suite Factory disfarçada
O verbete afirma que a Testcase Class "é na verdade" (*is actually*) uma Test Suite Factory — ou seja, sua responsabilidade real, por trás do nome, é produzir uma suíte de testes executáveis a partir dos Test Methods nela contidos. Isso é uma reclassificação funcional: o nome da classe (Testcase) sugere um teste individual, mas seu papel estrutural é o de fábrica de suíte.

---

## Entidades Mencionadas

- [[wiki/entities/gerard-meszaros]] — autor do verbete; mesma fonte primária do catálogo já usada para [[wiki/sources/test-xunitpatterns]], [[wiki/sources/sut-xunitpatterns]], [[wiki/sources/unit-test-xunitpatterns]] e demais verbetes do glossário

## Conceitos Tocados

- [[wiki/concepts/criterios-de-bom-teste]] — o par test/test case é a unidade elementar sobre a qual os critérios de qualidade se aplicam
- [[wiki/concepts/piramide-de-testes]] — a Testcase Class como unidade de agrupamento estrutural é a forma concreta como as camadas da pirâmide são organizadas em código

## Nota — a Testcase Class como fábrica do test fixture, não seu dono

[[wiki/sources/test-fixture-xunitpatterns]], o verbete dedicado ao termo **test fixture**/**test context**, acrescenta uma precisão a essa reclassificação: em JUnit e seus ports diretos, o test fixture é mantido conceitualmente separado da Testcase Class que o cria — coerente com a leitura de que a Testcase Class é uma **Test Suite Factory**: ela produz o fixture a cada execução, não o guarda como estado fixo e permanente da própria classe.

## Questões Abertas

- **Resolve parcialmente** a questão aberta em [[wiki/sources/test-xunitpatterns]] ("'test case' não recebe verbete próprio no índice de Glossário do site") — na verdade recebe verbete próprio; a observação anterior deve ser corrigida.
- **Testcase Class, Test Suite Factory e Test Method** são citados aqui pela primeira vez na wiki, mas nenhum dos três tem verbete de glossário isolado ingerido ainda — candidatos naturais para a próxima ingestão do mesmo cluster xUnitPatterns.com.
- **"Test Suite Factory"** como reclassificação funcional da Testcase Class levanta a pergunta: existe uma "Test Enumeration" mais ampla no catálogo (o link original aponta para `Test Enumeration.html#Test Suite Factory`) que caracteriza esse padrão com mais profundidade — candidata a fonte primária futura.

---

## Citações Relevantes

> "Usually a synonym for test. In XUnit, it may also refer to a Testcase Class which is actually a Test Suite Factory as well as a place to put a set of related Test Methods."

*(Tradução completa em `raw/test-case-xunitpatterns.md`.)*
