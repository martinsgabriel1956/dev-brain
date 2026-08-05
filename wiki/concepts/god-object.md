---
type: concept
title: "God Object"
aliases: ["god class", "objeto deus", "god object anti-pattern"]
date_created: 2026-05-05
date_updated: 2026-08-04
source_count: 4
tags: [anti-patterns, god-object, design-patterns, solid, coesao]
skill: tech-mentor-backend
status: stable
---

# God Object (Anti-pattern)

Classe ou objeto que sabe demais e faz demais. Concentra responsabilidades que deveriam estar distribuídas por múltiplas classes, violando o [[single-responsibility-principle]] e tornando o sistema difícil de testar, manter e estender.

## Sintomas

- Classe com centenas de métodos não relacionados entre si
- Toda alteração no sistema exige tocar nessa classe
- Nenhuma outra classe pode funcionar sem ela
- Difícil de testar isoladamente

## Relação com Facade

O [[facade-pattern]] tem risco explícito de virar um God Object se não houver disciplina:

> "Uma fachada pode se tornar um objeto deus acoplado a todas as classes de uma aplicação." — [[sources/design-pattern-facade]]

A diferença: uma Facade *bem feita* delega para o subsistema e não contém lógica própria. Quando começa a acumular lógica de negócio, vira God Object.

## Como uma God Class nasce sprint a sprint

[[wiki/sources/o-que-e-refatoracao-quando-usar]] narra a origem mais comum: não é um design ruim desde o início, é degradação incremental sob prazo. Uma classe `OrderProcessor` limpa (recebe pedido, cobra, salva) recebe um `if` "rapidinho" de frete internacional numa sprint de prazo apertado; algumas sprints e trocas de equipe depois, virou uma classe que valida cupom, calcula imposto, checa fraude e dispara evento — sem que nenhum desenvolvedor individual tenha tomado a decisão consciente de criar uma God Class. Isso é o argumento central para tratar [[wiki/concepts/refatoracao]] como hábito contínuo (ver também [[wiki/concepts/boy-scout-rule]]), não como projeto isolado a ser aprovado depois que o dano já está feito.

## Limite de Tamanho de Arquivo Como Gate Automático

[[wiki/sources/quatro-tecnicas-ci-cd-gate-qualidade-codigo-ia-uncle-bob]] propõe um gate de CI direto contra "god files" (a fonte cita arquivos de 3.000 a 5.000 linhas): um limite bloqueante de linhas por arquivo — o exemplo dado é 300 linhas —, reprovando o PR automaticamente se ultrapassado. É um proxy estrutural mais grosseiro do que [[wiki/concepts/complexidade-ciclomatica|complexidade ciclomática]] (que mede caminhos dentro de uma função) e do que [[wiki/concepts/single-responsibility-principle|SRP]] (que é qualitativo), mas barato de automatizar e, segundo a fonte, complementar a esses dois: um arquivo pode estar sob o limite de complexidade função a função e ainda assim ter virado um God Object pelo acúmulo de responsabilidades não relacionadas.

## Como resolver

- Aplicar [[single-responsibility-principle]]: cada classe com uma razão para mudar
- Extrair responsabilidades para classes especializadas
- Usar [[facade-pattern]] (com disciplina) ou [[mediator-pattern]] para coordenação

## Key Sources

- [[sources/design-pattern-facade]]
- [[sources/sete-padroes-de-design-de-software]]
- [[wiki/sources/o-que-e-refatoracao-quando-usar]] — exemplo narrativo de God Class nascendo por degradação incremental sob prazo, sprint a sprint
- [[wiki/sources/quatro-tecnicas-ci-cd-gate-qualidade-codigo-ia-uncle-bob]] — limite de tamanho de arquivo (exemplo: 300 linhas) como gate automático de CI contra god files
