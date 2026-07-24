---
type: concept
title: "UTF-8"
aliases: ["utf-8", "utf8", "unicode transformation format 8", "text encoding"]
date_created: 2026-06-10
date_updated: 2026-07-22
source_count: 2
tags: [utf-8, encoding, unicode, strings, cs-fundamentals, charset, decode, bitwise, overlong-encoding]
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

## Algoritmo de Decode (Bytes → Runa)

[[wiki/sources/algoritmo-decode-utf8-com-tdd]] implementa em Go, via TDD, uma função `DecodeRune(b []byte) (rune, int, error)` que reconstrói esse processo na prática, usando apenas [[bitwise-operations|AND, OR e left shift]]:

1. **Detectar o tamanho pelo primeiro byte**: AND com uma máscara (`0xE0`, `0xF0`, `0xF8`) isola o prefixo e compara com o valor esperado (`0xC0`, `0xE0`, `0xF0`) para 2, 3 e 4 bytes respectivamente.
2. **Extrair os bits de dados de cada byte**: AND remove o prefixo de tamanho/continuação, deixando só os bits `x` da tabela.
3. **Montar a runa de 32 bits**: left shift abre espaço para o próximo grupo de bits; OR mescla os grupos extraídos num único valor.

### Validações Obrigatórias (a parte difícil)

Decodificar bytes válidos é simples — a maior parte da complexidade está em **rejeitar** input inválido:

- **Byte de continuação malformado**: todo byte de continuação começa com `10xxxxxx` (`byte & 0xC0 == 0x80`); nenhum outro tipo de byte usa esse prefixo.
- **[[overlong-encoding]]**: um caractere codificado com mais bytes do que o mínimo necessário é proibido, mesmo que a sequência decodifique "corretamente".
- **Surrogate pairs proibidos**: codepoints na faixa `U+D800`–`U+DFFF` (reservada para UTF-16) nunca são um resultado válido de decode UTF-8.
- **Codepoint máximo**: qualquer runa acima de `U+10FFFF` é inválida — o Unicode não define nada além desse limite.

## Diferença de `encoding.md`

O verbete [[encoding]] nesta wiki cobre *transport encoding* (Base64, URL encoding, Hex) — transformações para transmissão de dados. UTF-8 é *text encoding*: define como caracteres são armazenados em memória. São camadas distintas; podem coexistir (ex.: uma string UTF-8 transmitida via Base64).

## Relação com Outros Conceitos

- [[unicode]] — o charset que UTF-8 implementa
- [[ascii]] — subconjunto de UTF-8; codepoints 0–127 são idênticos
- [[charset]] — UTF-8 é o encoding, não o charset
- [[string]] — string é um slice de bytes; UTF-8 é o algoritmo que transforma esses bytes em caracteres
- [[encoding]] — encoding de transporte (Base64, URL) vs. encoding de texto (UTF-8): conceitos distintos
- [[bitwise-operations]] — AND, OR e left shift usados para montar/desmontar runas
- [[overlong-encoding]] — regra de largura mínima que um decoder precisa validar

## Key Sources

- [[sources/como-strings-realmente-funcionam]]
- [[wiki/sources/algoritmo-decode-utf8-com-tdd]] — implementação prática do algoritmo de decode em Go, via TDD
