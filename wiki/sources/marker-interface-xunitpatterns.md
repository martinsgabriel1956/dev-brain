---
type: source
title: "Marker Interface (xUnitPatterns.com — Gerard Meszaros)"
aliases: ["marker interface xunitpatterns", "external patterns marker interface", "interface marcadora"]
date_created: 2026-09-21
date_updated: 2026-09-21
source_file: "raw/marker-interface-xunitpatterns.md"
source_url: "http://xunitpatterns.com/Marker%20Interface.html"
author: "Gerard Meszaros"
date_published: 2011-02-09
date_ingested: 2026-09-21
source_count: 0
tags: [design-patterns, marker-interface, oo, xunit, external-patterns, fonte-primaria]
skill: tech-mentor-testing
status: stable
---

# Marker Interface (xUnitPatterns.com — Gerard Meszaros)

## TL;DR

Verbete curto da categoria **External Patterns** do catálogo xUnitPatterns.com, mesmo formato mínimo já visto em [[wiki/sources/command-xunitpatterns]] e [[wiki/sources/decorator-xunitpatterns]]: resumo de uma frase seguido de uma definição formal — aqui, ao contrário das duas fontes citadas, **sem** atribuição a uma referência externa como [GOF]; é definição própria de Meszaros. Fecha a lacuna de fonte primária isolada para **Marker Interface** já sinalizada em [[wiki/concepts/marker-interface]], que até esta ingestão só conhecia o termo por menção de passagem em [[wiki/sources/test-discovery-xunitpatterns]] (uma das quatro soluções de **Testcase Class Discovery**).

---

## Afirmações Centrais

| Afirmação | Evidência | Fonte | Confiança |
|---|---|---|---|
| Marker Interface indica um atributo booleano semântico de uma classe através do simples fato de ela implementar a interface | "The Marker Interface pattern uses the fact that a class implements an interface to indicate semantic boolean attribute of the class" | fonte primária (Meszaros) | alta |
| Funciona particularmente bem com classes utilitárias que precisam determinar algo sobre objetos sem assumir que são instância de uma classe específica | "It works particularly well with utility classes that must determine something about objects without assuming they are an instance of any particular class" | fonte primária | alta |
| O resumo do padrão é "indicar algo sobre uma classe implementando uma interface vazia" | "Indicate something about a class by implementing an empty interface" | fonte primária | alta |

---

## Key Claims

### 1. A interface é vazia por definição — o valor está inteiramente no type-check, não em nenhum método
O resumo da fonte ("empty interface") e a definição ("o fato de uma classe implementar uma interface") deixam claro que o mecanismo não depende de nenhum comportamento herdado: o "sinal" é puramente estrutural — `obj instanceof MarkerInterface` (ou equivalente por linguagem) é toda a informação que a interface carrega. Isso explica por que [[wiki/sources/test-discovery-xunitpatterns]] a cita como alternativa "acoplada via sistema de tipos, sem herança forçada de comportamento" à subclassificação de uma Testcase Superclass: ambas identificam a classe via seu tipo, mas Marker Interface não impõe nenhuma implementação herdada, só a marca.

### 2. É a única entrada de External Patterns já ingerida na wiki sem atribuição a uma fonte de design patterns canônica
[[wiki/sources/command-xunitpatterns]] cita o GOF explicitamente ("From [GOF]"); [[wiki/sources/decorator-xunitpatterns]] segue o mesmo padrão. Este verbete não atribui a ninguém — é a formulação do próprio Meszaros do padrão, um vocabulário mais informal e específico da comunidade Java (a técnica de marker interfaces, como `Serializable` ou `Cloneable` no próprio JDK, é folclore da linguagem mais do que um padrão do GOF). Isso é consistente com o fato de o termo não aparecer no catálogo original de *Design Patterns* (1994).

### 3. Aplicação já documentada na wiki antes desta fonte: Testcase Class Discovery
[[wiki/concepts/marker-interface]] já registrava a aplicação prática do padrão ao vocabulário de xUnit, via [[wiki/sources/test-discovery-xunitpatterns]]: o framework pode reconhecer uma **Testcase Class** verificando se ela implementa a Marker Interface, em vez de exigir subclassificação de uma Testcase Superclass. Esta fonte não acrescenta esse exemplo — fica limitada à definição geral do padrão — mas confirma que a leitura já registrada (marcação por tipo, sem comportamento herdado) está correta e é exatamente o que o padrão formalmente propõe.

---

## Entidades Mencionadas

- [[wiki/entities/gerard-meszaros]] — autor do verbete; mesma fonte primária do catálogo já usada para dezenas de outros verbetes

## Conceitos Tocados

- [[wiki/concepts/marker-interface]] — recebe fonte primária dedicada, fechando a lacuna sinalizada desde sua criação como stub a partir de menção de passagem
- [[wiki/concepts/test-discovery]] — a aplicação prática do padrão (Testcase Class Discovery) já documentada ali é confirmada, não expandida, por esta fonte

## Questões Abertas

- A fonte não cita exemplos concretos de código (ao contrário de outras entradas de External Patterns com exemplos multi-linguagem) nem menciona interfaces marcadoras reais da própria linguagem Java (`Serializable`, `Cloneable`) — fica em nível puramente conceitual.
- Não há discussão do trade-off conhecido do padrão na comunidade mais ampla (marker interfaces vs. annotations como mecanismo de marcação, debate que ganhou força após Java 5) — a fonte não entra nesse contraste, deixado implícito pela comparação já existente em [[wiki/sources/test-discovery-xunitpatterns]] entre Marker Interface e class attribute/annotation como soluções irmãs de Testcase Class Discovery.

---

## Citações Relevantes

> "Indicate something about a class by implementing an empty interface."

> "The Marker Interface pattern uses the fact that a class implements an interface to indicate semantic boolean attribute of the class. It works particularly well with utility classes that must determine something about objects without assuming they are an instance of any particular class."

*(Tradução completa em `raw/marker-interface-xunitpatterns.md`.)*
