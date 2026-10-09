---
type: concept
title: "Algoritmo"
aliases: ["algorithm", "propriedades do algoritmo"]
date_created: 2026-10-09
date_updated: 2026-10-09
source_count: 1
tags: [algoritmo, fundamentos, cs-fundamentals]
skill: cs-fundamentals
status: draft
---

# Algoritmo

Sequência **finita** e **precisa** de passos que transforma uma entrada em uma saída para resolver um problema. A linguagem de programação é só a ferramenta que traduz essa lógica para a máquina ([[wiki/sources/o-que-e-um-algoritmo-propriedades-pseudocodigo-sistemas-de-recomendacao]]).

## Quatro propriedades (segundo a fonte)

1. **Entrada** — dados recebidos para processar.
2. **Clareza e precisão** — cada instrução unívoca; o computador não deduz, executa.
3. **Finitude** — precisa terminar; loop infinito sem resultado é falha.
4. **Saída** — resultado esperado ao fim.

[external] Knuth (*TAOCP* vol. 1) acrescenta **efetividade** (cada passo é básico o bastante para ser executado de fato) e agrupa clareza como "definição precisa". Ressalva: serviços de longa duração (servidores) não terminam por desenho — a finitude vale por *requisição/tarefa*, não pelo processo inteiro.

## Analogia

Receita de bolo: ingredientes (entrada) → passos (misturar, bater, 180 °C por 40 min) → bolo (saída). "Um pouco de farinha até ficar bom" é vago demais para ser algoritmo.

## Relações

- Rascunhado como [[wiki/concepts/pseudocodigo]] ou [[wiki/concepts/fluxo-logico]] antes do código; ver [[wiki/concepts/traducao-logica-para-codigo]].
- Usa decisões e repetições: [[wiki/concepts/fluxo-de-controle]].
- Custo medido por [[wiki/concepts/big-o]]; catálogo em [[wiki/concepts/algoritmos-e-estruturas-de-dados]].
- Uso popular ("o algoritmo do TikTok") = [[wiki/concepts/sistema-de-recomendacao]].

## Key sources

- [[wiki/sources/o-que-e-um-algoritmo-propriedades-pseudocodigo-sistemas-de-recomendacao]] — definição, quatro propriedades, receita de bolo
