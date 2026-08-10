---
type: concept
title: "Sistema Binário, Bit e Byte"
aliases: ["bit", "byte", "sistema binário", "binary digit", "representação binária"]
date_created: 2026-08-07
date_updated: 2026-08-07
source_count: 1
tags: [cs-fundamentals, sistema-binario, bit, byte, numero-binario, representacao]
skill: cs-fundamentals
status: stub
---

# Sistema Binário, Bit e Byte

O sistema binário é o sistema usado para representar **todas** as informações dentro da computação. Toda a stack — texto, imagem, som, instruções — se resume a sequências de bits.

## Bit

O **bit** é a menor unidade de informação. Tem dois estados possíveis: `0` ou `1` (desligado ou ligado). O termo é abreviação de *binary digit* (dígito binário).

Usar apenas dois estados **simplifica o design dos circuitos eletrônicos**: no hardware, os dois estados são representados de forma confiável por componentes como transistores — ligado para o `1`, desligado para o `0`. Confiabilidade é a razão de fundo: distinguir dois níveis de tensão é muito mais robusto do que distinguir dez.

## Byte

O **byte** é a unidade composta por **8 bits**. Enquanto o bit sozinho carrega pouca informação, o byte já representa uma informação completa ou parte dela — por exemplo, um caractere. A letra "A" corresponde a um byte específico (`01000001` em ASCII).

A hierarquia de composição:

```
bit → byte (8 bits) → caractere → palavra → frase → documento
```

Um documento de texto é armazenado em binário, onde cada byte representa uma letra, um conjunto de bytes representa uma palavra, e conjuntos desses conjuntos representam as frases.

## Processamento via lógica

O binário não serve só para armazenar — é eficiente para **processar**. Usando operadores lógicos (**AND**, **OR**, **XOR**) sobre os bytes, o computador constrói operações complexas a partir de lógica simples e rápida. Uma soma, por exemplo, pode ser expressa somente com essas operações lógicas. Ver [[wiki/concepts/logica-booleana]] e [[wiki/concepts/bitwise-operations]].

## Relação com outros conceitos

- [[wiki/concepts/logica-booleana]] — AND, OR, NOT como as operações que constroem qualquer circuito a partir de 0s e 1s
- [[wiki/concepts/bitwise-operations]] — AND/OR/shift manipulando bits diretamente para parsing e encoding
- [[wiki/concepts/maquina-de-turing]] — o modelo teórico opera sobre uma fita de símbolos de um alfabeto finito (tipicamente 0 e 1)
- [[wiki/concepts/criptografia]] — chaves e hashes são, no fundo, sequências de bits; o tamanho em bits define o espaço de possibilidades

## Key sources

- [[wiki/sources/conceitos-que-regem-a-computacao-bits-turing-complexidade]] — bit como binary digit (2 estados / transistores), byte como 8 bits representando um caractere, e a lógica binária como base do processamento
