---
type: concept
title: "Escolha de Linguagem para LeetCode"
aliases: ["linguagem para leetcode", "melhor linguagem leetcode", "python para leetcode"]
date_created: 2026-08-12
date_updated: 2026-08-12
source_count: 1
tags: [cs-fundamentals, leetcode, python, go, entrevistas, produtividade]
skill: cs-fundamentals
status: stub
---

# Escolha de Linguagem para LeetCode

Heurística: para treinar [[wiki/entities/leetcode|LeetCode]], escolha **uma** linguagem de **baixo boilerplate** e rápida de prototipar, e use só ela. LeetCode é essencialmente prototipar um algoritmo e testá-lo muitas vezes — a linguagem deve sair do caminho.

- **Python** (recomendação da fonte): tipagem fraca (`a = 0` sem declarar tipos), poucos imports, mínimo cerimonial. O menor atrito para escrever algo simples.
- **Go** e **JavaScript**: boas alternativas, também rápidas de escrever (JS tem comportamentos estranhos que raramente aparecem nesses problemas).
- **Evitar Rust/Haskell** — a menos que você já seja fluente. Aprender a linguagem e aprender os algoritmos são *skill sets* distintos; combiná-los faz você "brigar com a linguagem em vez do problema" e atrasa o aprendizado de LeetCode. Numa entrevista, isso também custa velocidade.

A escolha é sobre **velocidade de aprendizado/entrevista**, não sobre a qualidade da linguagem — para quem já domina Rust, a recomendação se inverte. Regra do dedão da fonte: use a que você já tem fluência (ex.: 10 anos de Java) se o custo de aprender Python do zero superar o ganho.

## Relação com outros conceitos

- [[wiki/concepts/reconhecimento-de-padroes]] — separar o aprendizado da linguagem do aprendizado de padrões é o mesmo princípio de "uma coisa de cada vez"
- [[wiki/concepts/pratica-deliberada]] — menos atrito de sintaxe = mais repetições úteis por sessão

## Key Sources

- [[wiki/sources/como-ficar-bom-em-leetcode]] — Python como recomendação principal; evitar Rust/Haskell salvo fluência prévia
