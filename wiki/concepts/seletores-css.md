---
type: concept
title: "Seletores CSS"
aliases: ["seletor CSS", "CSS selectors", "combinadores CSS", "seletor descendente", "seletor filho", "seletor adjacente", "seletor de atributo", "seletor universal"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 1
tags: [css, frontend, seletores-css, combinadores]
skill: tech-mentor-frontend
status: draft
---

# Seletores CSS

A parte da regra [[wiki/concepts/css|CSS]] que diz **a quais elementos** o estilo se aplica. Seletores andam pela árvore do [[wiki/concepts/dom]] (pai, filho, irmão), por isso bem usados evitam criar uma classe "só por causa de um elemento" ([[wiki/sources/seletores-e-pseudo-elements-css]]).

## Tipos vistos na aula

| Seletor | Exemplo | Pega |
|---|---|---|
| Tipo | `h1` | todos os `h1` |
| Classe | `.intro` | elementos com `class="intro"` |
| ID | `#Lastname` | o elemento com aquele `id` |
| Universal | `*` | todos os elementos |
| Elemento + classe | `p.intro` | só os `p` com a classe |
| Agrupamento (vírgula) | `h1, p` | cada um da lista, mesmo estilo |
| Descendente (espaço) | `div p` | `p` em qualquer nível dentro de `div` |
| Filho (`>`) | `div > p` | só `p` filho direto de `div` |
| Adjacente (`+`) | `ul + p` | o `p` logo depois de um `ul`, mesmo pai |
| Atributo | `[id=my-Address]`, `input[type="text"]` | pelo valor de um atributo; base para formulários |

Fonte: [[wiki/sources/seletores-e-pseudo-elements-css]], percorrendo o Try CSS Selector do [[wiki/entities/w3schools]]. `[external]` Falta na aula o irmão geral (`~`): `p ~ ul` pega todo `ul` que vem depois de um `p` no mesmo pai.

Estados e posições (`:hover`, `:nth-child`) ficam em [[wiki/concepts/pseudo-classe-css]]; partes do elemento (`::first-letter`) em [[wiki/concepts/pseudo-elemento-css]].

## Menos classes x classes explícitas

A aula defende seletores para ter "a menor quantidade de classes possíveis". `[skill: tech-mentor-frontend]` Em CSS global grande, BEM e ITCSS preferem classes explícitas e especificidade baixa e plana; `@layer` decide a precedência entre camadas, independente da especificidade do seletor. Seletores longos que copiam a estrutura do HTML quebram quando ela muda. Inferência do agente: combinadores e pseudo-classes rendem mais em padrões estruturais (zebra de tabela, estados de formulário) do que em componentes.

`[external]` Especificidade: ID > classe/atributo/pseudo-classe > tipo/pseudo-elemento; o universal e os combinadores não somam: https://developer.mozilla.org/en-US/docs/Web/CSS/Specificity.

## Key sources

- [[wiki/sources/seletores-e-pseudo-elements-css]] — tour pelo W3Schools: classe, ID, vírgula, descendente, filho, adjacente, universal, atributo
