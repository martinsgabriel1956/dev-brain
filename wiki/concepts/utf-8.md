---
type: concept
title: "UTF-8"
aliases: ["utf-8", "utf8", "unicode transformation format 8", "text encoding"]
date_created: 2026-06-10
date_updated: 2026-06-10
source_count: 1
tags: [utf-8, encoding, unicode, strings, cs-fundamentals, charset]
skill: cs-fundamentals
status: stable
---

# UTF-8

UTF-8 (Unicode Transformation Format – 8-bit) é o **encoding** dominante para o [[charset]] [[unicode]]. Define como armazenar codepoints Unicode em bytes usando largura variável: 1 a 4 bytes por caractere, dependendo do codepoint.

Criado por **Ken Thompson** e **Rob Pike** (também criadores do Go).

## Encoding vs. Charset

UTF-8 não é um charset — é o algoritmo que responde: *"dada esta sequência de bytes, qual codepoint Unicode ela representa?"*.

O charset [[unicode]] define que U+4E16 = 世. O UTF-8 define que U+4E16 se armazena como os 3 bytes `E4 B8 96`.

## Regra de Largura Variável

| Faixa de codepoint | Bytes necessários | Padrão de bits |
|---|---|---|
| U+0000–U+007F | 1 byte | `0xxxxxxx` |
| U+0080–U+07FF | 2 bytes | `110xxxxx 10xxxxxx` |
| U+0800–U+FFFF | 3 bytes | `1110xxxx 10xxxxxx 10xxxxxx` |
| U+10000–U+10FFFF | 4 bytes | `11110xxx 10xxxxxx 10xxxxxx 10xxxxxx` |

O bit de prefixo indica quantos bytes formam o caractere atual. Isso permite ao decodificador saber onde começa e termina cada caractere sem precisar de delimitador.

## Compatibilidade com ASCII

Qualquer byte com valor 0–127 em UTF-8 representa o mesmo caractere que em [[ascii]]. Código ASCII é automaticamente UTF-8 válido — a retrocompatibilidade foi um requisito de design.

## Por Que Strings São Imutáveis

Alterar um byte arbitrário numa string UTF-8 pode fragmentar um caractere multi-byte. Exemplo: substituir 1 dos 3 bytes de `世` (U+4E16) por outro valor arbitrário produz uma sequência de bytes que não corresponde a nenhum codepoint válido — o encoding fica corrompido silenciosamente. Ver [[string]] e [[imutabilidade]].

## Diferença de `encoding.md`

O verbete [[encoding]] nesta wiki cobre *transport encoding* (Base64, URL encoding, Hex) — transformações para transmissão de dados. UTF-8 é *text encoding*: define como caracteres são armazenados em memória. São camadas distintas; podem coexistir (ex.: uma string UTF-8 transmitida via Base64).

## Relação com Outros Conceitos

- [[unicode]] — o charset que UTF-8 implementa
- [[ascii]] — subconjunto de UTF-8; codepoints 0–127 são idênticos
- [[charset]] — UTF-8 é o encoding, não o charset
- [[string]] — string é um slice de bytes; UTF-8 é o algoritmo que transforma esses bytes em caracteres
- [[encoding]] — encoding de transporte (Base64, URL) vs. encoding de texto (UTF-8): conceitos distintos

## Key Sources

- [[sources/como-strings-realmente-funcionam]]
