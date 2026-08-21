---
type: concept
title: "Ravioli Code"
aliases: ["ravioli code", "codigo ravioli", "código ravióli"]
date_created: 2026-08-14
date_updated: 2026-08-14
source_count: 1
tags: [ravioli-code, anti-patterns, arquitetura, over-engineering, coesao]
skill: tech-mentor-backend
status: stub
---

# Ravioli Code

Anti-padrão da família das "massas": **classes bem estruturadas, fáceis de entender isoladamente, mas que em conjunto produzem um design de sistema pouco claro**. Se o [[wiki/concepts/code-espaguete|espaguete]] é *pouca* estrutura, o ravióli é o excesso de fragmentação — muitas peças pequenas e corretas, sem uma visão coerente do todo.

## A ambivalência do termo

O próprio verbete usa "ravioli code" em dois sentidos opostos:
- **Irônico/elogioso:** código complexo, porém *bem escrito* e encapsulado em unidades limpas.
- **Pejorativo:** fragmentação excessiva que dispersa a lógica em tantas classes que ninguém consegue mais enxergar o fluxo — um primo do [[wiki/concepts/over-engineering|over-engineering]].

Ambos partem da mesma imagem: cada ravióli é um "pacote" fechado. A pergunta é se os pacotes *compõem* um prato coerente ou apenas escondem a complexidade em caixas pequenas demais.

## Relacionado

[[wiki/concepts/code-espaguete]] · [[wiki/concepts/lasagna-code]] · [[wiki/concepts/big-ball-of-mud]] · [[wiki/concepts/over-engineering]] · [[wiki/concepts/coesao]]

## Key Sources

- [[wiki/sources/codigo-espaguete-wikipedia]] — definição e uso ambivalente (elogioso vs. pejorativo) do termo
