---
type: concept
title: "Pseudocódigo"
aliases: ["pseudocode", "fluxograma"]
date_created: 2026-10-09
date_updated: 2026-10-09
source_count: 2
tags: [pseudocodigo, fluxograma, algoritmo, fundamentos, cs-fundamentals]
skill: cs-fundamentals
status: draft
---

# Pseudocódigo

Descrição passo a passo de um [[wiki/concepts/algoritmo]] em linguagem próxima da natural, **sem sintaxe rígida**. Junto com fluxogramas, é como desenvolvedores estruturam o raciocínio antes de escolher Python, JavaScript ou C.

## Exemplo (saque em caixa eletrônico)

1. Ler cartão e senha.
2. Senha confere? Não → encerra e emite alerta.
3. Perguntar o valor.
4. Saldo ≥ valor? Sim → dispensar cédulas e atualizar saldo; não → informar saldo insuficiente.

Contém os dois ingredientes de algoritmos não triviais: **desvios condicionais** e (em versões com tentativas de senha) **repetições** — ver [[wiki/concepts/fluxo-de-controle]] e o refinamento em [[wiki/concepts/fluxo-logico]].

## Relações

- Terminologia (funções, condicionais, booleanos, loops) em [[wiki/sources/cs50-2026-semana-0-representacao-dados-algoritmos-scratch]].
- Próximo passo: [[wiki/concepts/traducao-logica-para-codigo]]. Casos de borda: [[wiki/concepts/edge-case]].

## Key sources

- [[wiki/sources/o-que-e-um-algoritmo-propriedades-pseudocodigo-sistemas-de-recomendacao]] — pseudocódigo/fluxograma como etapa antes da linguagem; exemplo do caixa eletrônico
- [[wiki/sources/cs50-2026-semana-0-representacao-dados-algoritmos-scratch]] — pseudocódigo da busca binária no catálogo telefônico
