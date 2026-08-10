---
type: concept
title: "Lógica Booleana"
aliases: ["lógica binária", "portas lógicas", "boolean logic", "AND OR NOT"]
date_created: 2026-06-26
date_updated: 2026-08-07
source_count: 2
tags: [cs-fundamentals, binario, logica-booleana, hardware, circuitos]
skill: cs-fundamentals
status: draft
---

# Lógica Booleana

A camada mais baixa da computação. Tudo que o computador processa — texto, imagem, som, vídeo — é, no fundo, uma sequência de **0s e 1s** manipulada por três operações:

| Operação | Símbolo | Comportamento |
|---|---|---|
| **AND** | `&&` / `&` | Verdadeiro somente se ambas as entradas são 1 |
| **OR** | `\|\|` / `\|` | Verdadeiro se pelo menos uma entrada é 1 |
| **NOT** | `!` / `~` | Inverte o valor — 0 vira 1, 1 vira 0 |

## Por que só três operações?

Porque **AND, OR e NOT são funcionalmente completas** — qualquer função lógica imaginável pode ser expressa como combinação dessas três. Na prática, NAND e NOR sozinhas também são suficientes (processadores reais usam NAND intensamente por eficiência de fabricação).

## Conexão com hardware

Cada uma dessas operações corresponde a uma **porta lógica** física — um circuito eletrônico que recebe tensões (0V ≈ 0, 5V ≈ 1) e produz uma saída. Combinando portas lógicas em série e paralelo você constrói:

- Somadores (adição binária)
- Registradores (memória de 1 bit)
- Multiplexadores (seleção de sinal)
- Processadores inteiros

## Representação de dados em binário

- Letra "A" = `01000001` (ASCII 65)
- Uma foto 4K = ~25 milhões de pixels × 3 bytes RGB = ~75 MB de zeros e uns
- Um número inteiro de 32 bits cobre de −2.147.483.648 a 2.147.483.647

## Relação com outros conceitos

- [[abstracao]] — toda a pilha de hardware→software é construída sobre essa fundação oculta
- [[big-o]] — operações binárias são O(1); algoritmos de busca e ordenação trabalham sobre representações binárias
- [[compilador]] — o código que você escreve é traduzido eventualmente para instruções que manipulam bits
- [[wiki/concepts/sistema-binario-bit-byte]] — os bits e bytes sobre os quais AND/OR/XOR operam; a fonte usa a soma como exemplo de operação construída só com lógica
- [[wiki/concepts/bitwise-operations]] — as mesmas operações aplicadas diretamente a bits em código (parsing, encoding, bitmask)

## Key sources

- [[wiki/sources/10-conceitos-fundamentais-computacao]]
- [[wiki/sources/conceitos-que-regem-a-computacao-bits-turing-complexidade]] — AND, OR e XOR sobre bytes como base do processamento binário (ex: representar uma soma só com operações lógicas)
