---
type: concept
title: "Determinismo vs. Não-Determinismo (Teoria da Computação)"
aliases: ["máquina de turing determinística", "máquina de turing não-determinística", "não-determinismo", "determinismo computacional"]
date_created: 2026-08-07
date_updated: 2026-08-07
source_count: 1
tags: [cs-fundamentals, teoria-da-computacao, determinismo, nao-determinismo, complexidade, maquina-de-turing]
skill: cs-fundamentals
status: stub
---

# Determinismo vs. Não-Determinismo (Teoria da Computação)

Distinção fundamental entre dois modelos da [[wiki/concepts/maquina-de-turing]], que sustenta boa parte da teoria da [[wiki/concepts/complexidade-computacional]].

## Máquina determinística

Para cada combinação de **(estado atual, símbolo lido)** existe **no máximo uma** ação possível. A tabela de transição tem uma única regra por combinação. Consequência: o comportamento é **totalmente previsível** — a mesma entrada sempre produz a mesma saída. É o modelo dos computadores que temos hoje.

## Máquina não-determinística

Generalização do modelo anterior: para cada **(estado, símbolo)** pode haver **várias** ações possíveis — a tabela de transição admite múltiplas regras para a mesma combinação. A máquina pode "escolher" entre as transições disponíveis e explorar caminhos diferentes; ela **aceita** a entrada se **pelo menos um** desses caminhos levar a um estado de aceitação.

Não é um modelo físico dos nossos computadores — é uma ferramenta teórica. Seu valor está em explorar os limites da computação e classificar problemas: existe uma classe de problemas que só seria solucionável em tempo razoável por uma máquina não-determinística, o que motiva a teoria da complexidade a distinguir classes como P e NP. `[skill: cs-fundamentals — references/computation-theory.md]`

## Nota de precisão — não-determinismo ≠ computação quântica

A fonte de vídeo associa o poder do não-determinismo aos **computadores quânticos**. Isso é uma **simplificação didática, não uma equivalência formal**: computação quântica (classe **BQP**) e não-determinismo (classe **NP**) são coisas distintas — não se sabe que um resolva o outro. Um computador quântico **não** é uma máquina de Turing não-determinística realizada em hardware. Tratar a associação como intuição de "explorar múltiplos caminhos", não como fato técnico. `[skill: cs-fundamentals]`

## Relação com outros conceitos

- [[wiki/concepts/maquina-de-turing]] — o modelo-base do qual as duas variantes derivam
- [[wiki/concepts/complexidade-computacional]] — as classes P (determinístico polinomial) e NP (não-determinístico polinomial) nascem dessa distinção
- [[wiki/concepts/big-o]] — a linguagem para medir "tempo razoável" em cada modelo
- [[wiki/concepts/determinismo-vs-probabilismo-em-ia]] — determinismo em outro contexto (saída reproduzível de modelos), útil para não confundir os dois usos do termo

## Key sources

- [[wiki/sources/conceitos-que-regem-a-computacao-bits-turing-complexidade]] — definição das duas variantes via unicidade (ou não) da regra de transição; associação (imprecisa) com computação quântica sinalizada aqui
