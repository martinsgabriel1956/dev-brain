---
type: concept
title: "ASCII"
aliases: ["ascii", "american standard code for information interchange", "tabela ascii"]
date_created: 2026-06-10
date_updated: 2026-07-22
source_count: 2
tags: [ascii, charset, encoding, strings, cs-fundamentals, representacao, decode]
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

Essa limitação gerou demanda pelo [[unicode]] e pelo [[utf-8]].

## Compatibilidade com UTF-8

O [[utf-8]] foi projetado para ser 100% retrocompatível com ASCII: qualquer byte com valor 0–127 em UTF-8 representa exatamente o mesmo caractere que em ASCII. Código ASCII válido é automaticamente UTF-8 válido.

## O Fast Path do ASCII num Decoder UTF-8

Como todo byte ASCII tem o bit mais significativo em `0` (`b0 < 0x80`), um decoder [[utf-8]] pode identificar caracteres ASCII com uma única comparação, sem precisar de nenhuma operação bitwise — o byte já É a runa completa. [[wiki/sources/algoritmo-decode-utf8-com-tdd]] usa exatamente esse atalho como primeiro `case` do algoritmo, antes de entrar na lógica mais complexa de [[bitwise-operations|AND/OR/shift]] para caracteres multi-byte.

## Key Sources

- [[sources/como-strings-realmente-funcionam]]
- [[wiki/sources/algoritmo-decode-utf8-com-tdd]] — ASCII como caso trivial (fast path) no decoder
