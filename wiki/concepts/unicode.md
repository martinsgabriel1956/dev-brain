---
type: concept
title: "Unicode"
aliases: ["unicode", "codepoint", "unicode charset", "universal character set"]
date_created: 2026-06-10
date_updated: 2026-06-10
source_count: 1
tags: [unicode, charset, utf-8, strings, cs-fundamentals, internacionalização]
skill: cs-fundamentals
status: stable
---

# Unicode

Unicode é um **[[charset]]** universal: define um espaço de mais de 1,1 milhão de codepoints (U+0000 a U+10FFFF), cobrindo todos os idiomas escritos conhecidos, símbolos matemáticos, emojis e caracteres históricos.

**Unicode não é um encoding.** Ele apenas diz qual valor numérico corresponde a qual caractere — não como armazenar esse valor em bytes.

## Charset, Não Encoding

Essa distinção é crítica:

| | O que diz |
|---|---|
| **Unicode (charset)** | U+4E16 = 世, U+1F600 = 😀, U+0048 = H |
| **UTF-8 (encoding)** | Como armazenar U+4E16 em bytes (3 bytes: `E4 B8 96`) |
| **UTF-16 (encoding)** | Como armazenar U+4E16 em bytes (2 bytes: `4E 16`) |
| **UTF-32 (encoding)** | Como armazenar qualquer codepoint em 4 bytes fixos |

O mesmo charset Unicode pode ser serializado com encodings diferentes.

## Compatibilidade com ASCII

Os primeiros 128 codepoints do Unicode (U+0000–U+007F) são idênticos ao [[ascii]]. Isso não é coincidência — foi uma decisão de design para garantir retrocompatibilidade.

## Por Que Veio Depois do ASCII

O [[ascii]] suporta apenas 128 caracteres — suficiente para inglês, insuficiente para o resto do mundo. Unicode foi criado para ser o mapeamento único e definitivo de todos os caracteres de todos os idiomas, eliminando a proliferação de charsets regionais incompatíveis (ISO-8859-x, Shift-JIS, GB2312…).

## Relação com UTF-8

O encoding dominante para Unicode é o [[utf-8]], criado por Ken Thompson e Rob Pike. UTF-8 usa largura variável (1–4 bytes por codepoint), mantém compatibilidade total com ASCII e é o encoding padrão na web e na maioria das linguagens modernas.

## Relação com Outros Conceitos

- [[charset]] — Unicode é o maior e mais abrangente charset existente
- [[ascii]] — subconjunto de Unicode (U+0000–U+007F)
- [[utf-8]] — o encoding mais usado para Unicode
- [[string]] — toda string moderna é Unicode + UTF-8 por padrão

## Key Sources

- [[sources/como-strings-realmente-funcionam]]
