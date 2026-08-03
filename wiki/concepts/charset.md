---
type: concept
title: "Charset"
aliases: ["character set", "conjunto de caracteres", "mapeamento de caracteres"]
date_created: 2026-06-10
date_updated: 2026-07-31
source_count: 3
tags: [charset, encoding, strings, unicode, ascii, cs-fundamentals, iso-8859-1]
skill: cs-fundamentals
status: stable
---

# Charset

Um charset (character set) é um **mapeamento** entre valores numéricos e caracteres: "o valor `X` representa o caractere `Y`". É apenas uma tabela de correspondência — não define como armazenar esses valores em bytes.

## Distinção: Charset vs. Encoding

| | Charset | Encoding |
|---|---|---|
| **O que é** | Mapeamento valor → caractere | Algoritmo bytes → valor |
| **Exemplo** | Unicode diz: U+4E16 = 世 | UTF-8 diz: como armazenar U+4E16 em bytes |
| **Depende de** | Nada — é uma tabela | Depende do charset |

Um charset responde "o que significa o valor 72?" O encoding responde "como ler uma sequência de bytes para extrair um valor?".

## ASCII: Charset que é Também Encoding

O [[ascii]] é um caso especial: como todos os seus 128 caracteres cabem em 1 byte, não existe ambiguidade de leitura. O charset e o encoding colapsam num só — pega o byte, consulta a tabela, fim.

## Unicode: Charset Sem Encoding Próprio

O [[unicode]] define um espaço de mais de 1 milhão de codepoints. Alguns codepoints exigem mais de 1 byte para ser representados. Isso significa que o Unicode precisa de um encoding separado para definir *como* armazenar esses valores — sendo o [[utf-8]] o mais utilizado.

## ISO-8859-1: Charset Regional Intermediário Entre ASCII e Unicode

[[iso-8859-1-latin-1]] é outro exemplo de charset que também funciona como seu próprio encoding (como o ASCII): 8 bits completos, 256 valores, 1 byte por caractere sem ambiguidade. Ele ilustra a fase intermediária entre ASCII (insuficiente) e Unicode (universal) — extensões regionais de 8 bits que resolviam acentuação para um grupo de idiomas, mas não para todos.

## Relação com Outros Conceitos

- [[ascii]] — charset com 128 entradas, funciona também como encoding
- [[iso-8859-1-latin-1]] — charset regional de 256 entradas, superconjunto direto de ASCII, também funciona como encoding
- [[unicode]] — charset universal, não é encoding
- [[utf-8]] — encoding para o charset Unicode
- [[string]] — toda string é definida por um charset + encoding + tamanho

## Key Sources

- [[sources/como-strings-realmente-funcionam]]
- [[wiki/sources/algoritmo-decode-utf8-com-tdd]] — implementação prática do encoding UTF-8 sobre o charset Unicode
- [[wiki/sources/codificacao-de-caracteres-ascii-iso-8859-1-unicode]] — ISO-8859-1 como exemplo de charset regional que também é encoding
