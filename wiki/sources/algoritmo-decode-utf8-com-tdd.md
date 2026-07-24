---
type: source
title: "Como Transformar um Slice de Bytes em uma String Utilizando o Encode UTF-8"
aliases: ["decode utf8 go", "utf8 decoder tdd", "implementar utf8 do zero", "DecodeRune"]
date_created: 2026-07-22
date_updated: 2026-07-22
source_count: 0
tags: [utf-8, unicode, ascii, bitwise, tdd, go, decode, overlong-encoding, cs-fundamentals]
skill: cs-fundamentals
status: stable
source_file: /home/nemomartins/Documentos/new/dev-study/raw/algoritmo-decode-utf8-com-tdd.md
source_url: ""
author: "Não identificado (vídeo YouTube) — mesmo canal de [[wiki/sources/como-strings-realmente-funcionam]]"
date_published: ""
date_ingested: 2026-07-22
---

# Como Transformar um Slice de Bytes em uma String Utilizando o Encode UTF-8

## TL;DR

Continuação direta de [[wiki/sources/como-strings-realmente-funcionam]] (respondendo a um pedido do próprio autor no fim daquele vídeo). Implementa, em Go e via TDD, uma função `DecodeRune(b []byte) (rune, int, error)` que decodifica o primeiro caractere UTF-8 de um slice de bytes — usando apenas AND, OR e left shift. Os testes são importados da suite oficial do pacote `unicode/utf8` da standard library de Go, usada como oráculo de corretude. Apesar do título dizer "encode", a função construída é um **decoder** (bytes → runa).

---

## Key Claims

**1. TDD funciona melhor quando interface, input e output já são conhecidos.**
A especificação UTF-8 (RFC) já define exatamente isso, tornando este um caso de uso ideal para TDD.
→ [[tdd]]

**2. Importar a suite de testes de uma implementação de referência é uma técnica válida de TDD.**
Em vez de escrever testes do zero (arriscando esquecer edge cases), o autor copiou os testes do pacote `unicode/utf8` da stdlib de Go. Passar em todos eles é evidência forte de corretude — inclusive contra sequências de bytes inválidas que seriam difíceis de antecipar sozinho.
→ [[tdd]], [[go-stdlib]]

**3. Decodificar é mais simples que validar.**
Montar a runa a partir de bytes válidos é direto; a maior parte da complexidade do algoritmo está em rejeitar corretamente todo input inválido (comprimento, bytes de continuação, overlong encoding, surrogate pairs, codepoint máximo).

**4. O primeiro byte determina o comprimento do caractere via prefixo de bits.**
`0xxxxxxx` = 1 byte, `110xxxxx` = 2 bytes, `1110xxxx` = 3 bytes, `11110xxx` = 4 bytes — verificado com AND e uma máscara (`0xE0`, `0xF0`, `0xF8` respectivamente) comparada ao valor esperado (`0xC0`, `0xE0`, `0xF0`).
→ [[utf-8]], [[bitwise-operations]]

**5. Montar a runa exige três operações bitwise combinadas: AND, left shift e OR.**
AND com uma máscara descarta os bits de prefixo (que só indicam o tamanho, não fazem parte do caractere) e extrai os bits de dados de cada byte. Left shift abre espaço à direita para os bits do próximo byte. OR mescla os grupos de bits extraídos num único valor de 32 bits (`rune`).
→ [[bitwise-operations]]

**6. Todo byte de continuação começa obrigatoriamente com `10xxxxxx`.**
Nenhum outro tipo de byte usa esse prefixo — por isso ele identifica de forma inequívoca um byte de continuação. Checagem: `byte & 0xC0 == 0x80`. Um caractere ASCII (1 byte) seguido de um byte com esse prefixo é UTF-8 inválido (byte de continuação "solto").
→ [[utf-8]]

**7. Overlong encoding é proibido: todo caractere deve usar o menor número de bytes possível.**
É possível, mecanicamente, codificar um caractere ASCII (ex.: `A` = 65) usando 2 bytes em vez de 1 — o decode até funcionaria, mas o encoding é inválido pelo padrão. Para 3 bytes, a checagem específica é `b0 == 0xE0 && b1 < 0xA0` (o menor codepoint que exige 3 bytes é `U+0800`, codificado como `E0 A0 80`); lógica análoga para 4 bytes.
→ [[overlong-encoding]], [[utf-8]]

**8. Surrogate pairs (`U+D800`–`U+DFFF`) são proibidos como resultado de decode UTF-8.**
Essa faixa é reservada para representar pares substitutos em UTF-16 — nunca deve aparecer como codepoint decodificado de UTF-8 válido.
→ [[unicode]]

**9. O Unicode tem um codepoint máximo: `U+10FFFF`.**
Qualquer runa decodificada acima desse valor é inválida. Esse foi o bug mais difícil de diagnosticar no vídeo — os dois últimos testes falhando não eram erro na suite importada, eram um caso real não coberto pelo algoritmo.
→ [[unicode]]

**10. O algoritmo final não busca ser o mais rápido — busca ser legível e correto.**
O autor menciona explicitamente que existem implementações mais eficientes (inclusive *branchless*), mas o objetivo do vídeo era um algoritmo que qualquer pessoa consiga ler e entender o padrão UTF-8 através dele.

---

## Nota sobre Terminologia: "RFC" Tem Dois Sentidos Nesta Wiki

Este vídeo usa "RFC" no sentido de **especificação técnica publicada pela IETF** (o documento que define o padrão UTF-8, RFC 3629) — bem diferente do sentido já documentado em [[wiki/concepts/rfc-request-for-comments]], que é o processo organizacional de propor mudanças arquiteturais internas e coletar objeções antes de decidir. São dois usos legítimos e comuns do mesmo termo, sem relação direta entre si além do nome. Sinalizado no verbete de RFC para evitar confusão futura.

---

## Conceitos Centrais

- [[utf-8]]
- [[unicode]]
- [[ascii]]
- [[charset]]
- [[string]]
- [[tdd]]
- [[go-fundamentos]]
- [[go-stdlib]]
- [[bitwise-operations]]
- [[overlong-encoding]]
- [[rfc-request-for-comments]]

---

## Questões Abertas

- A fonte anterior ([[wiki/sources/como-strings-realmente-funcionam]]) tinha como questão aberta exatamente "como o algoritmo UTF-8 determina quantos bytes usa para cada codepoint" — esta fonte responde isso por completo. Questão fechada.
- O vídeo não implementa o lado *encode* (runa → bytes) apesar do título — fica como lacuna não coberta por nenhuma fonte da wiki até o momento.
- Quais são as implementações *branchless* de decode UTF-8 mencionadas de passagem pelo autor? Não detalhadas na fonte.

---

## Contradições com o Wiki Existente

Nenhuma contradição de conteúdo — esta fonte é consistente e complementar a [[wiki/concepts/utf-8]], [[wiki/concepts/unicode]] e [[wiki/concepts/ascii]]. A única colisão é terminológica (ver seção "RFC" acima), não uma contradição factual.
