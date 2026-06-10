---
type: source
title: "Como Strings Realmente Funcionam (por Baixo dos Panos)"
aliases: ["como strings funcionam", "strings internals", "utf-8 strings"]
date_created: 2026-06-10
date_updated: 2026-06-10
source_count: 0
tags: [strings, encoding, unicode, utf-8, ascii, charset, go, imutabilidade, cs-fundamentals]
skill: cs-fundamentals
status: stable
source_file: /home/nemomartins/Documentos/new/dev-study/raw/como-strings-realmente-funcionam.md
source_url: ""
author: "Não identificado (vídeo YouTube)"
date_published: ""
date_ingested: 2026-06-10
---

# Como Strings Realmente Funcionam (por Baixo dos Panos)

## TL;DR

Uma string não é um tipo primitivo opaco — é um slice de bytes com charset e encoding associados. O motivo da imutabilidade em quase todas as linguagens é técnico: alterar bytes individualmente numa string multi-byte quebra o encoding. UTF-8 é o encoding universal para Unicode; ASCII é seu subconjunto mais antigo.

---

## Key Claims

**1. Para uma string existir, são necessários três elementos.**
Tamanho (intervalo de endereços de memória), charset (mapeamento valor → caractere) e encoding (algoritmo que interpreta a sequência de bytes).
→ [[concepts/charset]], [[concepts/utf-8]]

**2. ASCII é simultaneamente charset e encoding.**
Funciona em 7 bits (128 caracteres, 0–127). Como 1 byte é suficiente para qualquer caractere ASCII, não existe ambiguidade na interpretação — não é preciso um algoritmo extra.
→ [[concepts/ascii]]

**3. Unicode é apenas charset; UTF-8 é seu encoding.**
Unicode define o mapeamento de codepoints para caracteres (cobrindo todos os idiomas, emojis, símbolos). UTF-8 define *como* armazenar esses codepoints em bytes — usando largura variável (1 a 4 bytes por caractere). UTF-8 é 100% compatível com ASCII.
→ [[concepts/unicode]], [[concepts/utf-8]]

**4. String é um slice de bytes — não de caracteres.**
Em Go (e na maioria das linguagens), `len(s)` retorna o número de bytes, não de caracteres visíveis. `"Hello, 世界"` tem 9 runas mas 13 bytes, porque os dois caracteres chineses ocupam 3 bytes cada em UTF-8.

**5. Indexar diretamente quebra o encoding com caracteres multi-byte.**
`s[7]` numa string UTF-8 retorna apenas o *primeiro byte* do caractere na posição 7 — não o caractere completo. O resultado é um valor inválido que, ao ser interpretado como string, produz um caractere diferente do esperado.

**6. Strings são imutáveis para proteger o encoding.**
Permitir `s[i] = x` tornaria trivial sobrescrever 1 byte de um caractere que ocupa 3 bytes, corrompendo silenciosamente o encoding. A imutabilidade é a proteção arquitetural contra esse bug.
→ [[concepts/imutabilidade]]

**7. Runa em Go = codepoint Unicode de 32 bits.**
`rune` é um alias para `int32` e representa um codepoint Unicode inteiro — incluindo os multi-byte. Para iterar caracteres reais usa-se `range` (que itera runas) ou `utf8.RuneCountInString()`.

---

## Curiosidade

O UTF-8 foi criado por **Ken Thompson** e **Rob Pike** — os mesmos criadores da linguagem Go.

---

## Conceitos Centrais

- [[concepts/string]]
- [[concepts/charset]]
- [[concepts/ascii]]
- [[concepts/unicode]]
- [[concepts/utf-8]]
- [[concepts/imutabilidade]]
- [[concepts/encoding]]

---

## Questões Abertas

- Como o algoritmo UTF-8 determina quantos bytes usa para cada codepoint? (Regra dos bits de prefixo: `0xxxxxxx` = 1 byte, `110xxxxx` = 2 bytes, `1110xxxx` = 3 bytes, `11110xxx` = 4 bytes.) Vale um vídeo separado segundo o autor.
- Como PHP permite strings mutáveis sem quebrar encoding? (PHP trabalha com bytes crus; a responsabilidade de manter o encoding válido é do desenvolvedor — daí "não recomendado".)

---

## Contradições com o Wiki Existente

`encoding.md` trata encoding como transformação para transporte (URL encoding, Base64) — ângulo de segurança. Esta fonte introduz *text encoding* (charset encoding) como conceito distinto. Não há contradição, mas a distinção precisa ser explicitada no verbete.
