---
type: concept
title: "Cifra de Vigenère"
aliases: ["vigenere", "cifra de vigenere", "vigenere cipher", "cifra indecifravel"]
date_created: 2026-07-28
date_updated: 2026-07-28
source_count: 1
tags: [criptografia, historia, cifra, vigenere, criptografia-simetrica]
skill: tech-mentor-security
status: stub
---

## Definição

Cifra de substituição **polialfabética** (c. 1500) — evolução direta da limitação da [[wiki/concepts/caesar-cipher]]. Em vez de cada letra ser sempre substituída pela mesma letra (A sempre vira E), a letra da mensagem pode virar letras diferentes na cifra dependendo da posição, guiada por uma chave secreta repetida ao longo do texto.

## Como funciona

1. Mensagem e chave (repetida até cobrir o tamanho da mensagem) são alinhadas letra a letra.
2. Uma matriz (tabula recta) de A a Z nas linhas e colunas é usada: a linha da letra da mensagem cruza com a coluna da letra da chave, e a interseção é a letra cifrada.
3. Para descriptografar: localiza-se a linha da letra da chave, procura-se nela a letra cifrada, e a coluna correspondente dá a letra original.

## Criptografia simétrica

A mesma chave usada para cifrar é usada para decifrar — Vigenère é o primeiro exemplo histórico citado na wiki do princípio de **criptografia simétrica**, o mesmo modelo usado hoje pelo [[wiki/concepts/aes]].

## "A cifra indecifrável"

Foi considerada inquebrável por mais de 300 anos, até ataques estatísticos (método de Kasiski, depois Friedman) explorarem o fato de a chave se repetir em intervalos fixos — quebrando a cifra de volta em múltiplas instâncias de César deslocado. Esse método de quebra não é detalhado na fonte que introduziu este conceito (ver open question na fonte).

## Relação com outros conceitos

- [[wiki/concepts/caesar-cipher]] — Vigenère resolve a fraqueza de substituição monoalfabética fixa do César
- [[wiki/concepts/criptografia]] — primeiro exemplo histórico de criptografia simétrica citado na wiki
- [[wiki/concepts/aes]] — herdeiro moderno do princípio de chave simétrica compartilhada

## Key Sources

- [[wiki/sources/criptografia-cesar-vigenere-rsa-aes-hashing-quantica]]
