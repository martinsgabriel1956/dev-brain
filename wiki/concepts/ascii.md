---
type: concept
title: "ASCII"
aliases: ["ascii", "american standard code for information interchange", "tabela ascii"]
date_created: 2026-06-10
date_updated: 2026-08-18
source_count: 4
tags: [ascii, charset, encoding, strings, cs-fundamentals, representacao, decode, iso-8859-1]
skill: cs-fundamentals
status: stable
---

# ASCII

ASCII (American Standard Code for Information Interchange) é o [[charset]] mais antigo e mais difundido. Define 128 caracteres (valores 0–127) usando 7 bits — e é simultaneamente charset e encoding porque 1 byte é suficiente para representar qualquer caractere.

## Estrutura

| Faixa | Conteúdo |
|---|---|
| 0–31 | Caracteres de controle (newline, tab, null…) |
| 32–126 | Caracteres imprimíveis (letras, dígitos, pontuação) |
| 127 | DEL (delete) |

Exemplos de mapeamento:

| Decimal | Binário | Caractere |
|---|---|---|
| 72 | 01001000 | H |
| 101 | 01100101 | e |
| 65 | 01000001 | A |
| 48 | 00110000 | 0 |

## Por Que ASCII é Charset e Encoding ao Mesmo Tempo

Nos computadores modernos a menor unidade endereçável de memória é 1 byte (8 bits). Como ASCII usa no máximo 7 bits (128 valores), 1 byte é sempre suficiente — sem ambiguidade de leitura. Basta pegar o byte e consultar a tabela.

## Limitação: 128 Caracteres Não São Suficientes

ASCII não suporta:
- Acentos (á, é, ç, ñ…)
- Emojis
- Qualquer idioma não baseado no alfabeto latino inglês (árabe, chinês, japonês, grego…)

Essa limitação gerou demanda por codificações mais abrangentes — primeiro extensões regionais de 8 bits como [[iso-8859-1-latin-1]] (dobra o espaço para 0–255, já com acentos), e depois pelo [[unicode]] e pelo [[utf-8]] como solução universal.

## Contraste com Huffman Coding: Largura Fixa vs. Variável

[[wiki/sources/gzip-deflate-huffman-lz77]] usa o ASCII de 7 bits fixos como contraste didático para explicar por que o Huffman coding — algoritmo por trás do deflate/gzip, ver [[wiki/concepts/compactacao-de-texto]] — comprime texto: em ASCII, **todo** caractere gasta exatamente 7 bits, independente de quão frequente ou raro ele seja. Na árvore de Huffman, cada caractere tem um comprimento de código **variável**, proporcional à sua frequência no texto (caracteres comuns ficam mais rasos na árvore = menos bits; caracteres raros ficam mais fundos = mais bits). É essa troca de largura fixa por largura variável — não qualquer mágica sobre os bytes em si — que gera a compressão.

## O "Bit de Verificação" do 8º Bit

[[wiki/sources/codificacao-de-caracteres-ascii-iso-8859-1-unicode]] descreve o ASCII como usando 1 byte (8 bits) por símbolo, mas apenas 7 bits de dado — o 8º bit tratado como bit de verificação. Isso é reflexo da origem histórica do ASCII em transmissão serial (paridade); em contextos modernos como um decoder [[utf-8]], esse mesmo bit tem outro papel: sempre `0` num byte ASCII válido, ele é o que permite ao decoder distinguir ASCII de bytes de continuação multi-byte (ver seção abaixo). Framings complementares, não contraditórios.

## Compatibilidade com UTF-8

O [[utf-8]] foi projetado para ser 100% retrocompatível com ASCII: qualquer byte com valor 0–127 em UTF-8 representa exatamente o mesmo caractere que em ASCII. Código ASCII válido é automaticamente UTF-8 válido.

## O Fast Path do ASCII num Decoder UTF-8

Como todo byte ASCII tem o bit mais significativo em `0` (`b0 < 0x80`), um decoder [[utf-8]] pode identificar caracteres ASCII com uma única comparação, sem precisar de nenhuma operação bitwise — o byte já É a runa completa. [[wiki/sources/algoritmo-decode-utf8-com-tdd]] usa exatamente esse atalho como primeiro `case` do algoritmo, antes de entrar na lógica mais complexa de [[bitwise-operations|AND/OR/shift]] para caracteres multi-byte.

## Key Sources

- [[sources/como-strings-realmente-funcionam]]
- [[wiki/sources/algoritmo-decode-utf8-com-tdd]] — ASCII como caso trivial (fast path) no decoder
- [[wiki/sources/codificacao-de-caracteres-ascii-iso-8859-1-unicode]] — estrutura de bits (7 dados + verificação), tabela de contiguidade alfabética, exercício de decode
- [[wiki/sources/gzip-deflate-huffman-lz77]] — ASCII (largura fixa) como contraste didático para explicar o Huffman coding (largura variável)
