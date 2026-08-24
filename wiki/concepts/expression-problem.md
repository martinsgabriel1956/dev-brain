---
type: concept
title: "Expression Problem"
aliases: ["problema da expressão", "trade-off tipos vs operações"]
date_created: 2026-08-23
date_updated: 2026-08-23
source_count: 1
tags: [oop, expression-problem, polimorfismo, discriminated-union, extensibilidade, oop-vs-fp]
skill: tech-mentor-backend
status: stub
---

# Expression Problem

Nome dado na literatura de linguagens de programação ao trade-off de extensibilidade entre dois estilos de organizar um conjunto de tipos e operações sobre eles: **orientado a objetos/polimorfismo** vs. **union discriminada + switch** (o estilo típico de linguagens funcionais, também chamado de *pattern matching*).

## O trade-off

Dado um conjunto de tipos (`Square`, `Circle`) e um conjunto de operações sobre eles (`area`, `perimeter`):

| | Estilo objeto (polimorfismo) | Estilo estrutura de dados (union + switch) |
|---|---|---|
| **Adicionar um novo tipo** (`Triangle`) | Fácil — cria uma nova classe implementando a interface, nenhum código existente muda | Difícil — precisa editar o `switch`/`case` de **cada** função existente |
| **Adicionar uma nova operação** (`center`) | Difícil — precisa adicionar o método em **cada** classe existente | Fácil — cria uma nova função com um `switch` cobrindo os tipos já conhecidos, nenhum código existente muda |

Nenhum dos dois estilos resolve os dois eixos ao mesmo tempo sem custo — daí "problema": não existe uma solução isenta de trade-off usando só esses dois mecanismos (linguagens com typeclasses/protocols abertos, como Haskell ou Rust traits, atenuam o problema permitindo adicionar operações a tipos existentes sem editar a definição original do tipo nem um switch central).

## Onde isso aparece

[[wiki/sources/classes-vs-estruturas-de-dados-uncle-bob]] descreve exatamente esse trade-off (sem nomeá-lo formalmente) como uma das três formas em que **objetos** e **estruturas de dados** são opostos — ver [[wiki/concepts/objeto-vs-estrutura-de-dados]]. A recomendação prática de Uncle Bob: se você espera adicionar **novos tipos** com frequência, use classes/polimorfismo; se espera adicionar **novas operações** com frequência, use estruturas de dados + switch.

## Relação com outros conceitos

- [[wiki/concepts/objeto-vs-estrutura-de-dados]] — a distinção mais ampla da qual este trade-off é uma consequência direta
- [[wiki/concepts/polimorfismo]] — o mecanismo do lado "objeto" da comparação
- [[wiki/concepts/dependency-inversion-principle]] — o mesmo exemplo (Square/Circle/Triangle) também ilustra por que o estilo polimórfico inverte a direção da dependência de código-fonte

## Key Sources

- [[wiki/sources/classes-vs-estruturas-de-dados-uncle-bob]] — post original de Uncle Bob descrevendo o trade-off via exemplo de formas geométricas, sem usar o nome formal "Expression Problem"
