---
type: concept
title: "Overlong Encoding (UTF-8)"
aliases: ["overlong utf8", "codificação longa demais", "non-shortest form"]
date_created: 2026-07-22
date_updated: 2026-07-22
source_count: 1
tags: [utf-8, unicode, encoding, validacao, cs-fundamentals]
skill: cs-fundamentals
status: draft
---

# Overlong Encoding (UTF-8)

Regra do padrão [[utf-8]]: todo caractere **deve** ser codificado usando o **menor número de bytes possível**. Codificar um caractere usando mais bytes do que o mínimo necessário — mesmo que a sequência de bits "pareça" um UTF-8 sintaticamente válido — é chamado de *overlong encoding* e é proibido pela especificação.

## Exemplo

O caractere `A` (codepoint 65, decimal) cabe em 1 byte ASCII. Nada impede, mecanicamente, de codificá-lo como uma sequência de 2 bytes (`110xxxxx 10xxxxxx`) preenchendo os bits de dados com o mesmo valor 65 — um decoder ingênuo decodificaria essa sequência de volta para `A` corretamente. Mas essa forma de dois bytes é *overlong*: 65 já cabe em 1 byte, então usar 2 é inválido pelo padrão.

## Como Detectar

Não basta checar apenas o valor final decodificado — é preciso checar o **primeiro byte de continuação** contra um valor mínimo, condicionado ao primeiro byte líder:

```go
// 3 bytes: o menor codepoint que realmente precisa de 3 bytes é U+0800,
// codificado como E0 A0 80. Se o primeiro byte é 0xE0 e o segundo é
// menor que 0xA0, o caractere caberia em 2 bytes — overlong.
if b0 == 0xE0 && b1 < 0xA0 {
    return 0, 0, errors.New("overlong encoding")
}
```

Para 2 bytes, basta comparar o valor final decodificado: se `r < 0x80`, é overlong (caberia em ASCII). A lógica de "checar o segundo byte contra um mínimo" só é necessária a partir de 3 bytes, porque o primeiro byte líder sozinho não distingue o intervalo válido do inválido.

## Por Que a Regra Existe

Permitir múltiplas representações válidas para o mesmo codepoint quebra uma propriedade central de encodings bem definidos: **um valor, uma única representação canônica**. Historicamente, overlong encoding foi explorado como vetor de bypass de filtros de segurança (ex.: sanitizadores que checam a forma ASCII de `/` ou `.` falhavam ao não rejeitar uma versão overlong desses mesmos bytes codificada em UTF-8) — por isso decoders robustos precisam rejeitar essas sequências explicitamente, não apenas "aceitar o que decodifica sem erro".

## Relação com Outros Conceitos

- [[utf-8]] — a regra de largura mínima faz parte da especificação do encoding
- [[bitwise-operations]] — a detecção usa comparação direta de bytes, não apenas AND/OR
- [[unicode]] — cada codepoint tem exatamente uma representação UTF-8 canônica

## Key Sources

- [[wiki/sources/algoritmo-decode-utf8-com-tdd]]
