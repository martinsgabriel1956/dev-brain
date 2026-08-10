---
type: concept
title: "Máquina de Turing"
aliases: ["Turing machine", "máquina de turing", "modelo de Turing", "tabela de transição"]
date_created: 2026-08-07
date_updated: 2026-08-07
source_count: 1
tags: [cs-fundamentals, teoria-da-computacao, maquina-de-turing, computabilidade, automatos]
skill: cs-fundamentals
status: stub
---

# Máquina de Turing

Modelo teórico de computação proposto por **[[wiki/entities/alan-turing|Alan Turing]] em 1936**. É um dos modelos fundamentais da teoria da computação e serve para definir **o que pode ser computado** e como.

## Os componentes

- **Fita infinita** dividida em células. Cada célula armazena um símbolo de um conjunto finito (por exemplo, `0` ou `1`).
- **Cabeça de leitura/escrita** que passa sobre a fita: pode ler o símbolo da célula atual, escrever um novo símbolo, e se mover para a célula adjacente à esquerda ou à direita.
- **Tabela de transição** — conjunto finito de regras que rege o funcionamento. A regra é escolhida a partir de dois inputs: o **símbolo lido** e o **estado atual** da máquina. Ela determina três saídas: o novo símbolo a escrever, a direção do movimento e o novo estado.

Exemplo de regras:

```
se (estado=A, lê 0) → escreve 1, move direita, vai para estado B
se (estado=A, lê 1) → não altera,  move esquerda, permanece em A
```

## Por que importa

A força do modelo está na combinação de **simplicidade** e **poder**. Apesar de trivialmente simples, a máquina de Turing consegue representar **qualquer algoritmo computável**: tudo que um computador moderno computa também pode ser computado por uma máquina de Turing (à custa de uma tabela de transição enorme e uma fita gigantesca, mas é possível). Não há definição de computador mais completa, e ela permanece válida até hoje — é a referência para se raciocinar sobre os **limites da computação**.

Na hierarquia de Chomsky, a máquina de Turing corresponde às gramáticas irrestritas — reconhece qualquer linguagem computável, o topo do poder expressivo. `[skill: cs-fundamentals — references/computation-theory.md]`

## Relação com outros conceitos

- [[wiki/concepts/determinismo-vs-nao-determinismo]] — a máquina de Turing tem variantes determinística (uma ação por estado/símbolo) e não-determinística (várias ações)
- [[wiki/concepts/complexidade-computacional]] — as classes de complexidade são definidas em termos do que máquinas de Turing (determinísticas e não) resolvem e em quanto tempo/espaço
- [[wiki/concepts/sistema-binario-bit-byte]] — a fita opera sobre símbolos de um alfabeto finito, tipicamente 0 e 1
- [[wiki/concepts/maquina-de-estados-ui]] — FSM é um modelo de autômato mais fraco (memória finita, sem fita) do mesmo campo da teoria da computação

## Key sources

- [[wiki/sources/conceitos-que-regem-a-computacao-bits-turing-complexidade]] — definição via fita infinita, cabeça de leitura/escrita e tabela de transição; argumento de que representa tudo que é computável
