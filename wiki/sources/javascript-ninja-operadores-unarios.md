---
type: source
title: "Operadores unários (JavaScript Ninja, semana 2, vídeo 02)"
aliases: ["JavaScript Ninja operadores unários", "JS Ninja + e - unários", "02 - Operadores Unários"]
date_created: 2026-11-24
date_updated: 2026-11-24
source_count: 0
tags: [javascript, operadores, operadores-unarios, coercao, nan, concatenacao, incremento, efeito-colateral, tipagem-fraca]
skill: lang-dynamic
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/javascript-ninja-operadores-unarios.md"
source_url: ""
author: "Fernando Daciuk"
date_published: ""
date_ingested: 2026-11-24
---

# Operadores unários (JavaScript Ninja, semana 2, vídeo 02)

## TL;DR

Segundo vídeo da segunda leva do [[wiki/entities/javascript-ninja|JavaScript Ninja]] (cerca de 6 min), depois de [[wiki/sources/javascript-ninja-operadores-logicos|operadores lógicos]]. O instrutor se apresenta ("Fernando da Silva" na legenda, a mesma deformação das aulas 03 e 04), então a autoria de [[wiki/entities/fernando-daciuk|Fernando Daciuk]] é de confiança alta. Anunciado como o fim do "giro pela linguagem".

- **Mais unário:** `+valor` "vai tentar converter o valor que está vendo depois dele em número", ou dá `NaN`; se já for número, "não vai fazer absolutamente nada". `+'3'` dá `3` ([[wiki/concepts/operadores-unarios-javascript]]).
- **`NaN`** "é avaliado como o tipo número", "mas ele significa que esse valor não é um número" ([[wiki/concepts/tipos-primitivos-javascript]]).
- **Mais binário também concatena:** string com número "não soma, ele concatena": "sempre [...] o JavaScript sempre vai entender que eu quero fazer uma concatenação" ([[wiki/concepts/operadores-aritmeticos-javascript]]).
- **Menos unário:** converte para número "e ele inverte o sinal". `-x` com `x = 3` dá `-3`, e "isso não causa efeito colateral": `x` continua 3. `-'3'` dá `-3`.
- **`++` e `--`** também são unários e, ao contrário de `+`/`-`, "causam o efeito colateral": "ele atribui o novo valor a essa variável" ([[wiki/concepts/incremento-e-decremento]], [[wiki/concepts/efeito-colateral]]).
- Próximo vídeo: estrutura léxica do JavaScript.

Continua em [[wiki/sources/javascript-ninja-estrutura-lexica]].

## Key Claims

### Mais unário

- Antes: o mais e o menos "servia[m] para somar dois valores", com dois operandos (`3 + 3`).
- "Quando você usa ele como um operador unário [...] quando você usa somente ele, [e] um outro valor [...] ele vai tentar converter o valor que está vendo depois dele em número. Ou NaN."
- "E se por acaso esse valor já for um número, ele não vai fazer absolutamente nada": `+3` dá `3`.
- `'3'` sozinho volta "com as aspas [...] ou com os apóstrofos"; "quando eu uso o sinal de mais antes [...] ele converte para mim [...] em números".
- Com "uma frase": `NaN`. "Ele é avaliado como o tipo número [...] mas ele significa que esse valor não é um número. Então ele tentou converter esse valor aqui, ele retornou dizendo que não é um número."

### Concatenação

- "O operador mais, ele serve também para concatenar." Dois números somam; duas strings juntam.
- String com número: "ele não soma, ele concatena". Nem na ordem inversa (`3 + '3'`) ele converte a string para somar: "ele vai concatenar os valores".
- "Sempre que eu [somo uma string] com um número, o JavaScript sempre vai entender que eu quero fazer uma concatenação. Nunca que eu vou fazer uma soma [...] de um valor que não é número com o outro." (Trecho entre colchetes reconstruído; a legenda diz "sou mais ninguém".)

### Menos unário

- "Ele tenta converter o valor para números e ele inverte o sinal daquele número."
- `var x = 3; -x` dá `-3`. "Isso não causa efeito colateral. Se eu chamar o valor de x aqui, vai continuar sendo 3."
- Com a string `'3'`: "vai [converter] 3 para o número e vai inverter o sinal dele".

### `++` e `--`

- "Os operadores unários de incremento, de decremento, que nós já vimos": `x = 3`, `x++` deixa 4, `++x` ("pré-incremento") deixa 5.
- "Esse operador aqui, mais mais ou menos menos, eles causam o efeito colateral. Ele atribui o novo valor a essa variável."
- Já `+` e `-` unários: "simplesmente [...] inverte o valor, mas a variável continua valendo [...] o valor que ela já tinha".

## Precisões e tensões com a wiki

`⚠️` A skill lang-dynamic não tem arquivo de referência para operadores de JavaScript; as precisões vêm do MDN e da especificação, marcadas `[external]` (sem fetch, conhecimento base; confiança alta salvo indicação).

1. **`+x` é `Number(x)`.** `[external]` Aplica *ToNumber*: `+''` e `+' '` dão `0`, `+true` dá `1`, `+null` dá `0`, `+undefined` dá `NaN`, `+[]` dá `0`, `+'0x10'` dá `16`, `+'1e3'` dá `1000`. Com BigInt, `+1n` lança `TypeError` (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Unary_plus). Diferente de `parseInt`: `+'12px'` é `NaN`, `parseInt('12px', 10)` é `12` ([[wiki/concepts/operadores-unarios-javascript]]).
2. **"Sempre concatena" vale só para o `+`.** `[external]` Se um dos lados, depois de virar primitivo, for string, o `+` concatena; `-`, `*` e `/` convertem para número: `'3' - 1` dá `2`, `'3' * '2'` dá `6`. A ordem importa: `1 + 2 + '3'` dá `'33'`, `'1' + 2 + 3` dá `'123'`. Para somar, converter antes: `+'3' + 3` dá `6`. Bate com o `'200' + 200` do FrontPUSH em [[wiki/concepts/igualdade-javascript]] e com a tipagem fraca de [[wiki/concepts/sistema-de-tipos]].
3. **Objetos também entram.** `[external]` `[] + 1` dá `'1'` e `{} + []` depende de onde aparece; o `+` chama *ToPrimitive* primeiro ([[wiki/concepts/pitfalls-de-linguagem]]).
4. **"Operador binário" onde se esperava "unário".** "O operador unário menos [...] faz a mesma coisa que o operador binário mais", "é o operador binário, mas não um operador unário mais" e "sobre operadores binários, era isso" pedem "unário" pelo contexto. Pode ser legenda ou lapso de fala; ficou literal.
5. **`NaN` é number, e é contagioso.** Qualquer conta com `NaN` dá `NaN`, e `NaN !== NaN`; testar com `Number.isNaN` ([[wiki/concepts/tipos-primitivos-javascript]]).
6. **Efeito colateral bem colocado.** `-x` e `+x` são expressões puras; `x++` e `++x` escrevem na variável. É o mesmo critério de [[wiki/concepts/efeito-colateral]] e de [[wiki/concepts/expressao-javascript]].
7. **Lista incompleta de unários.** `[external]` Também são unários `!` (o vídeo anterior, [[wiki/concepts/operadores-logicos-javascript]]), `typeof`, `void`, `delete`, `~` e `await`. Sintaxe: `a + +b` soma `b` convertido; `a+++b` é `(a++) + b`.
8. **Legenda.** Trocas principais: "Fernando da Silva"→Fernando Daciuk, "sugiro a"→o giro pela (média-alta), "unitários"/"cenários"→unários, "anárquico"/"Mario"/"humano" (2×)/"área"/"nariz"/"não é"→unário, "Note"/"nota e não"→NaN (média), "eleito no 13"→ele retornou três (média), "apóstolos"→apóstrofos, "estigma"/"estilingue"/"tinha"→string, "Mano"→menos, "inventar"→inverter, "Eu comentei"→Ele converteu (média), "convencer"→converter, "léxico"→léxica. Lista dos trechos literais no [[wiki/log]].

## Entities

- [[wiki/entities/fernando-daciuk]]: instrutor (se apresenta).
- [[wiki/entities/javascript-ninja]]: o curso.
- [[wiki/entities/javascript]]: assunto.

## Concepts

- [[wiki/concepts/operadores-unarios-javascript]] (criado neste ingest)
- [[wiki/concepts/operadores-aritmeticos-javascript]]
- [[wiki/concepts/incremento-e-decremento]]
- [[wiki/concepts/tipos-primitivos-javascript]]
- [[wiki/concepts/sistema-de-tipos]]
- [[wiki/concepts/efeito-colateral]]
- [[wiki/concepts/expressao-javascript]]
- [[wiki/concepts/operadores-logicos-javascript]]
- [[wiki/concepts/pitfalls-de-linguagem]]

## Open Questions

- "Se eu fizer menos 3 usando mais mais": provavelmente "usando aspas" (`-'3'`), pelo que vem depois ("é uma historinha", isto é, string); ficou literal.
- "Ele vai ser disse eu", "mas existem 3", "A 1": a demo de `3 + '3'` perdeu as expressões; o resultado (concatena) é claro.
- "Essa historinha" aparece duas vezes onde caberia "string"; como na aula 03, ficou literal.
- O vídeo diz "pra finalizar agora o giro pela linguagem", mas anuncia estrutura léxica para o próximo; o giro talvez termine depois.

## Raw quotes

- "ele vai tentar converter o valor que está vendo depois dele em número"
- "Isso não causa efeito colateral. Se eu chamar o valor de x aqui, vai continuar sendo 3."
- "mais mais ou menos menos, eles causam o efeito colateral"
