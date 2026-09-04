---
type: concept
title: "Polimorfismo"
aliases: ["polymorphism", "polimorfismo dinâmico", "dynamic dispatch"]
date_created: 2026-08-23
date_updated: 2026-09-02
source_count: 2
tags: [oop, polimorfismo, dynamic-dispatch, expression-problem]
skill: tech-mentor-backend
status: stub
---

# Polimorfismo

Mecanismo pelo qual chamar a mesma operação nomeada (ex.: `area()`) sobre objetos de tipos diferentes (`Square`, `Circle`) executa uma implementação diferente para cada tipo, decidida em tempo de execução pelo próprio objeto — **polimorfismo dinâmico** (dynamic dispatch). Quem chama não precisa saber qual implementação concreta vai rodar; só depende da interface comum.

## Contraste com union discriminada + switch

[[wiki/sources/classes-vs-estruturas-de-dados-uncle-bob]] usa o polimorfismo como o lado "objeto" de uma comparação com o estilo "estrutura de dados": em vez de várias implementações de `area` pertencendo cada uma à sua classe (polimorfismo), uma união discriminada guarda um código de tipo e uma única função com `switch` decide qual caminho seguir. Essa diferença é a raiz do trade-off descrito em [[wiki/concepts/expression-problem]] e da inversão de dependência descrita em [[wiki/concepts/dependency-inversion-principle]].

## Precursor histórico: procedure variable, antes de existir sintaxe de método virtual

[[wiki/sources/procedure-variable-xunitpatterns]] (Gerard Meszaros, glossário xUnitPatterns.com) situa o despacho dinâmico numa camada abaixo da linguagem: uma **procedure variable** (também chamada *function pointer*, ou *delegate* em .Net) é uma variável que referencia um procedimento em vez de um dado, permitindo que o código chamado seja decidido em tempo de execução (dynamic binding) em vez de tempo de compilação. A fonte afirma que *procedure variables* foram precursoras das OOPLs verdadeiras: C++ inicial as usava em tabelas (arrays) de estruturas de dados para montar manualmente as *dispatch tables* de objetos/classes — o mesmo efeito que hoje `area()` obtém automaticamente via polimorfismo, mas antes de existir sintaxe de classe/método virtual na linguagem.

## Key Sources

- [[wiki/sources/classes-vs-estruturas-de-dados-uncle-bob]] — exemplo Square/Circle/Triangle contrastando polimorfismo dinâmico com switch sobre união discriminada
- [[wiki/sources/procedure-variable-xunitpatterns]] — verbete de glossário do xUnitPatterns.com (Meszaros) isolando "procedure variable"/function pointer/delegate como precursor pré-OOP do despacho dinâmico, via tabelas manuais de dispatch em C++ inicial
