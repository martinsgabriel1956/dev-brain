---
type: concept
title: "ISO-8859-1 (Latin-1)"
aliases: ["iso-8859-1", "latin-1", "latin1", "iso 8859-1"]
date_created: 2026-07-31
date_updated: 2026-07-31
source_count: 1
tags: [iso-8859-1, latin-1, charset, encoding, ascii, cs-fundamentals]
skill: cs-fundamentals
status: stub
---

# ISO-8859-1 (Latin-1)

ISO-8859-1, também conhecida como Latin-1, é um [[charset]] de 8 bits que estende o [[ascii]] para representar 256 valores (0–255) em vez de 128 (0–127).

## Retrocompatibilidade com ASCII

Os primeiros 128 valores (0–127) de ISO-8859-1 são idênticos aos da tabela [[ascii]] — mesmo mapeamento binário, mesmo caractere. Os 128 valores adicionais (128–255) cobrem caracteres que o ASCII não representa, incluindo caracteres acentuados (á, é, ç, ñ…), o que a torna adequada para português, espanhol, francês e a maioria das línguas da Europa Ocidental.

## Por que Existiu Antes do Unicode Dominar

Antes da adoção ampla do [[unicode]]/[[utf-8]], ISO-8859-1 era uma das codificações regionais mais usadas no Brasil e em outros países que precisavam de acentuação, mas sem a complexidade (e overhead de bytes) do Unicode multi-byte. Fazia parte de uma família maior de charsets regionais incompatíveis entre si (ISO-8859-x, Shift-JIS, GB2312…) que o Unicode foi criado para substituir — ver [[wiki/concepts/unicode]] ("Por Que Veio Depois do ASCII").

## Diferença Estrutural para ASCII

| | ASCII | ISO-8859-1 |
|---|---|---|
| Bits usados | 7 (dado) + 1 (verificação) | 8 (dado completo) |
| Valores representáveis | 0–127 | 0–255 |
| Caracteres acentuados | Não | Sim (128–255) |

## Relação com Outros Conceitos

- [[ascii]] — ISO-8859-1 é um superconjunto direto: 0–127 idênticos, 128–255 são a extensão
- [[charset]] — ISO-8859-1 é, como o ASCII, charset e encoding ao mesmo tempo (1 byte por caractere, sem ambiguidade)
- [[unicode]] — resolve a limitação de ISO-8859-1 (ainda regional, não universal) com um charset único para todos os idiomas

## Key Sources

- [[wiki/sources/codificacao-de-caracteres-ascii-iso-8859-1-unicode]]
