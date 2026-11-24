---
type: source
title: "Operadores lógicos (JavaScript Ninja, semana 2, vídeo 01)"
aliases: ["JavaScript Ninja operadores lógicos", "JS Ninja &&, || e !", "01 - Operadores Lógicos"]
date_created: 2026-11-24
date_updated: 2026-11-24
source_count: 0
tags: [javascript, operadores, operadores-logicos, and, or, not, boolean, igualdade-estrita, coercao, tipagem-fraca]
skill: lang-dynamic
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/javascript-ninja-operadores-logicos.md"
source_url: ""
author: "Fernando Daciuk"
date_published: ""
date_ingested: 2026-11-24
---

# Operadores lógicos (JavaScript Ninja, semana 2, vídeo 01)

## TL;DR

Primeiro vídeo da segunda leva do [[wiki/entities/javascript-ninja|JavaScript Ninja]] (cerca de 9 min), "depois de [corrigir] o exercício" do desafio da semana que fechou [[wiki/sources/javascript-ninja-funcoes|a aula de funções]]. O instrutor não diz o nome; a autoria de [[wiki/entities/fernando-daciuk|Fernando Daciuk]] vem do curso e do "Como assim, Fernando?" que ele mesmo faz.

- **O que fazem:** "eles combinam ou eles invertem valores booleanos" ([[wiki/concepts/operadores-logicos-javascript]]).
- **E (`&&`), "dois 'e' comercial":** com `x = 3` e `y = 7`, `x === 3 && y === 7` dá true; com `y === 4`, falso. "Ele só retorna true quando os dois valores são verdadeiros."
- **OU (`||`):** "pelo menos um deles é verdadeiro". `x === 3 || y === 3` dá true porque o X é 3.
- **Not (`!`):** "vai inverter um valor". `x === 3` dá true; "not X é igual a 3" dá falso. "Esse formato [...] não é utilizado": para negar uma comparação, usa-se o diferente.
- **Diferente estrito × não estrito:** volta ao `!=` × `!==` com `x = 3` e `'3'`. A legenda perdeu boa parte da demo; a conclusão é a da aula de igualdade: sem testar o tipo, "isso é bastante problemático", fique com o operador estrito ([[wiki/concepts/igualdade-javascript]]).
- Dúvidas: no desafio, por email ou "abrir uma issue no GitHub". Próximo vídeo: operadores unários.

Continua em [[wiki/sources/javascript-ninja-operadores-unarios]].

## Key Claims

### O que são

- "Operadores lógicos, basicamente o que eles fazem: eles combinam ou eles invertem valores booleanos."

### E (`&&`)

- "O operador lógico E, que são dois 'e' comercial [...] ele vai combinar [...] dois valores, e ele vai retornar se a combinação desses valores é true ou falso."
- Preparação: `var x = 3`, `var y = 7`. `y === 5` é falso, "porque eu defini que o Y é sete"; `y === '7'` "também é falso, porque eu testei pelo tipo"; `y === 7` é true, "o tipo dele é o número".
- Combinação: "X é igual a 3 [e] Y é sete: ele vai retornar true". Com `y === 4`, "vai me retornar falso".
- Regra: "Ele só retorna true quando os dois valores são verdadeiros. Então, se o X é verdadeiro, mas o Y é falso", o resultado é falso.

### OU (`||`)

- "Para testar se dois valores, qualquer um deles é verdadeiro, ou pelo menos um deles é verdadeiro [...] eu vou testar usando o operador or."
- `x === 3 || y === 3` "retornou true", "mas o X é igual a 3": basta um lado.

### Not (`!`)

- "O not, ou o sinal de exclamação [...] ele vai inverter um valor."
- "Os operadores lógicos, ele sempre retornar [true] ou falso."
- `x === 3` retorna true; "se eu disser not X é igual a 3, ele vai retornar falso".
- "Esse formato novamente não é utilizado, então não tem utilização do formato com o not direto aqui": em vez de negar a comparação, `x != 3`/`x !== 3`.

### `!=` × `!==`

- `x != 3` é falso, "porque o X é igual a 3"; `x !== 3` também.
- Com a string `'3'`, o resultado muda conforme se testa o tipo ou não: sem tipo, `x != '3'` "vai dizer que é falso"; com tipo, `x !== '3'` dá true, "porque o X não é igual a três [string], e sim o X é igual a três números". (Reconstrução pelo que se entende; a legenda dessa parte é muito ruim.)
- "Você pode até ter um resultado bastante diferente, se você usar o operador e não testar pelo tipo dele [...] Então isso é bastante problemático."
- "Ficou claro? Ficou muito complicado? Bom, sim, ficou complicado." O assunto volta depois.

## Precisões e tensões com a wiki

`⚠️` A skill lang-dynamic não tem arquivo de referência para operadores de JavaScript; as precisões vêm do MDN e da especificação, marcadas `[external]` (sem fetch, conhecimento base; confiança alta salvo indicação).

1. **`&&` e `||` não devolvem booleano, devolvem um dos operandos.** `[external]` "Ele sempre [retorna true] ou falso" só vale quando os dois lados já são booleanos, como nos exemplos da aula. `'a' && 0` dá `0`, `null || 'padrão'` dá `'padrão'`, `'' && x` dá `''`. Só o `!` sempre devolve booleano (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_AND, https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_OR). Ver [[wiki/concepts/operadores-logicos-javascript]].
2. **Não são só "valores booleanos".** Qualquer valor entra; a decisão é por [[wiki/concepts/truthy-e-falsy|truthy e falsy]].
3. **Curto-circuito, que a aula não menciona.** `&&` não avalia o lado direito se o esquerdo for falsy; `||` não avalia se o esquerdo for truthy. É a base de `obj && obj.prop`, `valor || padrao` e do `cond && <Componente />` do React ([[wiki/concepts/renderizacao-condicional]]).
4. **"Not X é igual a 3" depende de como se escreve.** `[external]` `!` tem precedência maior que `===`: `!x === 3` é `(!x) === 3`, isto é, `false === 3`, que dá false. O resultado bate com o da aula por coincidência; negar a comparação exige `!(x === 3)`, ou melhor, `x !== 3`. Com `==`, `!x == 0` dá true (`false` vira `0`) ([[wiki/concepts/pitfalls-de-linguagem]]).
5. **Precedência entre `&&` e `||`.** `[external]` `&&` vem antes: `a || b && c` é `a || (b && c)`. Comparações vêm antes das duas, por isso `x === 3 && y === 7` dispensa parênteses.
6. **O `!` é muito usado, só não para negar comparação.** `!lista.length`, `if (!usuario)` e `!!valor` (conversão explícita para booleano) são comuns; o "não é utilizado" vale para `!(a === b)` no lugar de `a !== b`.
7. **`!==` e a recomendação.** A segunda metade repete a aula de igualdade e bate com [[wiki/concepts/igualdade-javascript]]: `===`/`!==` por padrão.
8. **Era ES5.** Faltam o `??` (ES2020), que só troca `null`/`undefined` e não pode se misturar com `&&`/`||` sem parênteses, e as atribuições lógicas `&&=`, `||=`, `??=` (ES2021, [[wiki/concepts/atribuicao-composta]]).
9. **Legenda.** Trocas principais: "na índia"→Ninja, "Ou"→E e "e é comercial"→"e" comercial, "ético"→é true, "preço"→três, "CET"/"Gasset"→sete/é sete, "Ibson"/"iPhone"→Y/Y é, "tornar" (8×)→retornar, "título"/"tudo"/"TRU"→true, "monitorar tudo"→retornar true, "não torna"→retorna, "off"/"olha"→or, "Note"/"Moto"→not, "ver tem"→inverter, "13"→três, "chip"→X, "tinha"/"Swing"/"estilingue"→string, "street"→strict, "escrito"/"restrito"→estrito, "político"/"positivo"→pelo tipo, "no script"→no JavaScript, "isca no videogame"→issue no GitHub, "olhares"→unários. Lista dos trechos literais no [[wiki/log]].

## Entities

- [[wiki/entities/fernando-daciuk]]: instrutor (autoria pelo curso).
- [[wiki/entities/javascript-ninja]]: o curso.
- [[wiki/entities/javascript]]: assunto.

## Concepts

- [[wiki/concepts/operadores-logicos-javascript]] (criado neste ingest)
- [[wiki/concepts/logica-booleana]]
- [[wiki/concepts/truthy-e-falsy]]
- [[wiki/concepts/igualdade-javascript]]
- [[wiki/concepts/estruturas-condicionais-javascript]]
- [[wiki/concepts/renderizacao-condicional]]
- [[wiki/concepts/atribuicao-composta]]
- [[wiki/concepts/tipos-primitivos-javascript]]
- [[wiki/concepts/pitfalls-de-linguagem]]

## Open Questions

- "Quando eu faço essa verificação, ele vai me retornar um valor falso": `x === 3` com `x = 3` dá true, e o próprio instrutor diz logo depois que "isso é verdadeiro". Erro de legenda ou de fala; não dá para saber.
- "Me explica esse negócio de multiplicar": provavelmente "combinar"; ficou literal.
- "Ora são dois prestar um ao lado do outro": quase certamente "OR são dois pipes um ao lado do outro" (`||`), mas a legenda não permite afirmar.
- A demo do `!=` × `!==` com `'3'` está muito deformada ("alinhamento ou neutro", "ele retornou o fato", "diferente de triste", "se ele defende três números"); a reconstrução em Key Claims é inferência (média).
- O vídeo de correção do desafio da semana, citado na abertura, não está na wiki.

## Raw quotes

- "eles combinam ou eles invertem valores booleanos"
- "Ele só retorna true quando os dois valores são verdadeiros."
- "Ficou claro? Ficou muito complicado? Bom, sim, ficou complicado."
