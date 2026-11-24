---
type: concept
title: "Truthy e falsy em JavaScript"
aliases: ["truthy", "falsy", "valores falsos", "ToBoolean", "coerção para booleano", "!!"]
date_created: 2026-11-16
date_updated: 2026-11-24
source_count: 5
tags: [javascript, booleano, coercao, condicionais, tipos]
skill: lang-dynamic
status: draft
---

# Truthy e falsy em JavaScript

Toda condição (`if`, `while`, ternário, `!`, `&&`, `||`) converte o valor para booleano (`ToBoolean` na especificação). Os valores que viram `false` são os **falsy**; todo o resto é **truthy**. `[external]` https://developer.mozilla.org/en-US/docs/Glossary/Falsy

## Os oito falsy

`false`, `0`, `-0`, `0n` (bigint), `''` (string vazia), `null`, `undefined` e `NaN`. (Mais `document.all`, um resquício histórico dos navegadores.)

## Truthy que surpreendem

- `'0'`, `'false'`, `' '`: strings não vazias.
- `[]` e `{}`: todo objeto é truthy, inclusive vazio. Para lista vazia, `lista.length === 0`.
- `-1`, `Infinity`.

## Usos e armadilhas

- `!!valor` ou `Boolean(valor)` convertem explicitamente.
- `valor || padrão` troca qualquer falsy, inclusive `0` e `''`; `valor ?? padrão` troca só `null`/`undefined` ([[wiki/concepts/null-e-undefined]]).
- `cond && <Componente />` no React renderiza `0` se `cond` for `0` ([[wiki/concepts/renderizacao-condicional]]).
- Truthy ≠ `== true`: `'2' == true` é `false`, porque o `==` converte o `true` para `1` ([[wiki/concepts/igualdade-javascript]]).

Relacionado: [[wiki/concepts/logica-booleana]], [[wiki/concepts/tipos-primitivos-javascript]], [[wiki/concepts/estruturas-condicionais-javascript]].

## No FrontPUSH

Em [[wiki/sources/frontpush-estruturas-condicionais-booleanos-comparadores-javascript]], [[wiki/entities/nasser|Násser]] testa no `if`: string não vazia e número diferente de 0 entram; `''`, `0`, `false`, `undefined` e `NaN` não. "É mais fácil tratar o falso porque ele é mais específico." Faltam `-0`, `0n` e (por um trecho sem legenda) provavelmente `null`; "o único número [falso] é o 0" não é exato.

## No JavaScript Ninja, semana 2, vídeo 01 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-operadores-logicos]], os operadores lógicos aparecem "combinando ou invertendo valores booleanos", só com comparações. Com valores quaisquer, `&&` e `||` decidem por truthy/falsy e devolvem o próprio operando (`'' || 'padrão'` é `'padrão'`); só o `!` devolve booleano ([[wiki/concepts/operadores-logicos-javascript]]).

## No JavaScript Ninja, semana 2, vídeo 04 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-instrucoes-condicionais-if]], a condição do `if` "vai se tornar um valor booleano". A aula só usa comparações; a conversão vale para qualquer valor, e é aqui que truthy e falsy decidem se o bloco roda ([[wiki/concepts/estruturas-condicionais-javascript]]).

## No JavaScript Ninja, semana 4, vídeo 01 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-truthy-e-falsy]], a aula inteira é sobre o tema: truthy é o que, "booleanamente falando", é "representado por true"; falsy, o contrário. Lista `NaN`, `0`, `-0`, string vazia (aspas simples e duplas), `null` e `false`; `undefined` não aparece em trecho legível e `0n` é posterior. Mostra `'0'`, `'Fernando'`, `{}` e `[]` como truthy e ensina `!!valor` como forma de ver o booleano sem `if`. Testa só com `if` e `!!`, sem passar pelo `==` (`'0' == false` é `true`).

## No JavaScript Ninja, semana 4, vídeo 02 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-condicional-ternario]], a condição do ternário também passa por truthy/falsy: `'sim' ? 'porta' : 'janela'` dá `'porta'`; com `false`, `'janela'` ([[wiki/concepts/operador-ternario-javascript]]).

## Key sources

- [[wiki/sources/frontpush-estruturas-condicionais-booleanos-comparadores-javascript]]: FrontPUSH, JavaScript aula 03: string vazia, 0, undefined e NaN como falsos
- [[wiki/sources/javascript-ninja-operadores-logicos]]: JavaScript Ninja, semana 2, vídeo 01: &&, || e ! só com booleanos
- [[wiki/sources/javascript-ninja-instrucoes-condicionais-if]]: JavaScript Ninja, semana 2, vídeo 04: condição do if vira booleano
- [[wiki/sources/javascript-ninja-truthy-e-falsy]]: JavaScript Ninja, semana 4, vídeo 01: aula dedicada; seis falsy listados e `!!`
- [[wiki/sources/javascript-ninja-condicional-ternario]]: JavaScript Ninja, semana 4, vídeo 02: truthy/falsy na condição do ternário
