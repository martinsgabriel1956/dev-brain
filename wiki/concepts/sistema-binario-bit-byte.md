---
type: concept
title: "Sistema Binário, Bit e Byte"
aliases: ["bit", "byte", "sistema binário", "binary digit", "representação binária"]
date_created: 2026-08-07
date_updated: 2026-08-25
source_count: 3
tags: [cs-fundamentals, sistema-binario, bit, byte, numero-binario, representacao, rgb, unicode]
skill: cs-fundamentals
status: draft
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

## Unário vs. Binário: Por Que Base 2

[[wiki/sources/cs50-2026-semana-0-representacao-dados-algoritmos-scratch]] contrasta o sistema **unário** (base 1 — contar com dígitos únicos, como dedos de uma mão, limitado a 5 ou 10) com o **binário** (base 2): usando os dedos de uma única mão como 5 posições com pesos 1, 2, 4, 8, 16 (em vez de contar quantos estão levantados), é possível contar até **31**. O mesmo princípio se aplica a lâmpadas físicas contando de 0 a 7 com 3 posições de peso 4/2/1 — a razão de fundo para computadores usarem base 2 (e não base 10) é que distinguir "eletricidade fluindo ou não" é mais simples e robusto de construir em hardware do que distinguir dez níveis de voltagem diferentes.

## Além de Texto: RGB, Vídeo e Som Também São Números

A mesma fonte generaliza o princípio "zeros e uns + convenção de interpretação" para além de caracteres:

- **Cor (RGB)** — misturar vermelho, verde e azul em proporções de 0–255 cada (1 byte por componente, 3 bytes = 24 bits por pixel) produz praticamente qualquer cor. RGB (0,0,0) = preto, RGB (255,255,255) = branco. Notação hexadecimal (`#FF0000`) é só outra forma de representar os mesmos valores 0–255.
- **Vídeo** — uma sequência de ~30 imagens por segundo, rápida o suficiente para o cérebro interpretar como movimento (o mesmo princípio de um flipbook).
- **Som/música** — cada nota pode ser descrita por três números: frequência/altura (pitch), duração e amplitude (volume).

O padrão se repete: representar qualquer tipo de mídia é uma questão de convenção de interpretação sobre a mesma sequência de bits, nunca uma limitação do binário em si.

## O bit físico: 1V/0V num transistor

[[wiki/sources/como-transistores-formam-portas-logicas-celulas-padrao-cmos]] abre a caixa-preta mencionada acima ("os dois estados são representados de forma confiável por componentes como transistores"): mostra exatamente como isso acontece — um transistor tipo N conduz eletricidade quando 1V é aplicado ao seu gate, e um tipo P conduz quando 0V é aplicado. É essa diferença de tensão física (1V vs. 0V), e não uma metáfora, que corresponde ao bit `1` ou `0`. Ver [[wiki/concepts/transistor]] e [[wiki/concepts/celula-padrao]] para o detalhamento completo de como bits combinados em portas físicas ([[wiki/concepts/cmos|CMOS]]) formam a hierarquia até um chip completo.

## Relação com outros conceitos

- [[wiki/concepts/logica-booleana]] — AND, OR, NOT como as operações que constroem qualquer circuito a partir de 0s e 1s
- [[wiki/concepts/bitwise-operations]] — AND/OR/shift manipulando bits diretamente para parsing e encoding
- [[wiki/concepts/maquina-de-turing]] — o modelo teórico opera sobre uma fita de símbolos de um alfabeto finito (tipicamente 0 e 1)
- [[wiki/concepts/criptografia]] — chaves e hashes são, no fundo, sequências de bits; o tamanho em bits define o espaço de possibilidades
- [[wiki/concepts/ascii]] — a mesma convenção "byte = 1 caractere" aplicada especificamente a texto
- [[wiki/concepts/unicode]] — extensão do princípio a alfabetos além do inglês e a emoji
- [[wiki/concepts/transistor]] — o componente físico que implementa o estado 0/1 via tensão no gate (0V/1V)
- [[wiki/concepts/celula-padrao]] — como bits (saídas de transistores) se combinam em portas lógicas físicas

## Key sources

- [[wiki/sources/conceitos-que-regem-a-computacao-bits-turing-complexidade]] — bit como binary digit (2 estados / transistores), byte como 8 bits representando um caractere, e a lógica binária como base do processamento
- [[wiki/sources/cs50-2026-semana-0-representacao-dados-algoritmos-scratch]] — unário vs. binário com demonstração física (dedos/lâmpadas); 2⁸=256 e 2³²/2⁶⁴ como tamanhos modernos de palavra; generalização do princípio para RGB, vídeo e som
- [[wiki/sources/como-transistores-formam-portas-logicas-celulas-padrao-cmos]] — como o transistor implementa fisicamente o estado 0V/1V que o bit representa
