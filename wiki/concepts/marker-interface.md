---
type: concept
title: "Marker Interface"
aliases: ["interface marcadora"]
date_created: 2026-09-21
date_updated: 2026-09-21
source_count: 2
tags: [testes, oo, xunit, terminologia, padrao-externo]
skill: tech-mentor-testing
status: stable
---

# Marker Interface

Interface **vazia** (sem métodos), implementada por uma classe apenas para indicar um atributo booleano semântico dela em tempo de execução, verificável por type-check (`instanceof` ou equivalente) — sem exigir nenhum comportamento herdado. Segundo [[wiki/sources/marker-interface-xunitpatterns]], fonte primária dedicada de [[wiki/entities/gerard-meszaros]], funciona particularmente bem com classes utilitárias que precisam determinar algo sobre objetos sem assumir que são instância de uma classe específica. Diferente de outras entradas da categoria "External Patterns" do catálogo ([[wiki/sources/command-xunitpatterns|Command]], [[wiki/sources/decorator-xunitpatterns|Decorator]]), esta não é atribuída ao [[wiki/entities/gang-of-four|GOF]] — é formulação própria de Meszaros, vocabulário mais informal e específico da comunidade Java (ex.: `Serializable`, `Cloneable` no próprio JDK).

## Aplicação em xUnit: Testcase Class Discovery

[[wiki/sources/test-discovery-xunitpatterns]] cita Marker Interface como uma das soluções de **[[wiki/concepts/test-discovery|Testcase Class Discovery]]**: o framework pode identificar quais classes são [[wiki/sources/testcase-class-xunitpatterns|Testcase Classes]] verificando se implementam a Marker Interface, em vez de exigir subclassificação de uma Testcase Superclass. Essa fonte referencia a sigla externa **[PJV1]** (não expandida na wiki) como origem do termo — a fonte dedicada ao padrão em si não cita essa referência, sugerindo que [PJV1] é a origem do exemplo de aplicação a testes, não do padrão geral.

## Alternativa a subclassificação

Ao lado de subclassificar uma **Testcase Superclass**, é uma das duas formas de "tagging" citadas por [[wiki/sources/test-discovery-xunitpatterns]] para Testcase Class Discovery — ambas acoplam via sistema de tipos, em contraste com as outras duas soluções (class attribute/annotation, ou convenção de localização/nomenclatura de arquivo) que não exigem alteração na hierarquia de tipos da classe. Como a interface é vazia por definição, o custo de acoplamento é menor que o de subclassificar uma superclasse: não força herança de nenhuma implementação, só a marca.

## Status: stable

Fonte primária dedicada ao padrão ([[wiki/sources/marker-interface-xunitpatterns]]) fecha a lacuna sinalizada desde a criação deste stub a partir de menção de passagem em [[wiki/sources/test-discovery-xunitpatterns]]. Segue em aberto o contraste entre Marker Interface e annotations como mecanismo de marcação (debate que ganhou força na comunidade Java pós-Java 5) — nenhuma das duas fontes ingeridas entra nesse trade-off diretamente.

## Key Sources

- [[wiki/sources/marker-interface-xunitpatterns]] — **fonte primária dedicada**: definição formal do padrão, sem atribuição externa (diferente de Command/Decorator, que citam o GOF)
- [[wiki/sources/test-discovery-xunitpatterns]] — aplicação prática do padrão a Testcase Class Discovery, com a sigla externa [PJV1]
