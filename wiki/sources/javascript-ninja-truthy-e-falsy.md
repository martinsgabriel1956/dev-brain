---
type: source
title: "Truthy e falsy (JavaScript Ninja, semana 4, vídeo 01)"
aliases: ["JavaScript Ninja truthy e falsy", "JS Ninja falsy", "01 - Truthy e Falsy"]
date_created: 2026-11-24
date_updated: 2026-11-24
source_count: 0
tags: [javascript, truthy-falsy, coercao, boolean, if-else, dupla-negacao, operadores-unarios]
skill: lang-dynamic
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/javascript-ninja-truthy-e-falsy.md"
source_url: ""
author: "Fernando Daciuk"
date_published: ""
date_ingested: 2026-11-24
---

# Truthy e falsy (JavaScript Ninja, semana 4, vídeo 01)

## TL;DR

Primeiro vídeo da "quarta aula" do [[wiki/entities/javascript-ninja|JavaScript Ninja]] (cerca de 10 min), depois de [[wiki/sources/javascript-ninja-metodos-de-objeto-continuacao|métodos de objeto (continuação)]]. Sem autoapresentação; autoria de [[wiki/entities/fernando-daciuk|Fernando Daciuk]] inferida da série (ele digita "Fernando" como string de exemplo). A legenda é muito deformada: boa parte das demonstrações só se reconstrói pelo contexto.

- **Definição:** valor truthy é o que, "booleanamente falando", é "representado por true"; falsy é "o contrário", o que vira `false` "quando se converte para booleano" ([[wiki/concepts/truthy-e-falsy]]).
- **Teste com `if`:** `var teste; if (valor) { teste = true } else { teste = false }`. `1` dá `true`; `0` dá `false` ([[wiki/concepts/estruturas-condicionais-javascript]]).
- **Falsy na aula:** `NaN` ("um tipo de número"), `0`, `-0`, string vazia "tanto com aspas simples como com aspas duplas", `null` e `false` ("esqueci de colocar aqui"). `undefined` provavelmente está nos trechos ilegíveis (ver Open Questions).
- **Truthy que surpreendem:** `'0'` ("o zero dentro da string [...] não é a mesma coisa que um número zero"), qualquer string preenchida (`'Fernando'`), objeto vazio e array vazio. "Todos os outros valores são [truthy]."
- **`!!valor`:** um `!` "converte para booleano, inverte"; dois invertem de novo e dão o booleano do valor sem precisar do `if` ([[wiki/concepts/operadores-unarios-javascript]]).
- "Dificilmente você vai precisar", porque o JavaScript "faz essa conversão automaticamente". Conversão de tipos e o uso real de `!!` ficam para depois.
- Próximo vídeo: o condicional ternário.

Continua em [[wiki/sources/javascript-ninja-condicional-ternario]] (semana 4, vídeo 02: condicional ternário).

## Key Claims

### Definição

- "Quando você precisa testar alguma coisa, como if, por exemplo, [...] ele precisa de um valor booleano para verificar se ele entrou [...] naquela condição."
- "Valor truthy é todo aquele valor que, booleanamente falando, digamos assim, [...] ele é representado por true. E o falsy é o contrário: é todo um valor que, quando se converte para booleano, [...] ele é representado por false."

### Demonstração com `if`

- Primeiro uma comparação: "testar se um aqui é igual a letra B. Um número, na verdade, não é igual a letra B. Então ele vai retornar [...] um valor falso." Depois o valor sozinho: "ele vai me retornar um", e a pergunta é como saber se ele é "verdadeiro ou falso": "testa com o if".
- `if (1)` põe `teste` em `true`: "ele é um valor verdadeiro". Com zero, "o teste, na verdade, é falso".

### Os falsy

- `NaN`: "ele é um tipo de número", mas é falsy (trecho muito deformado; ver Open Questions).
- `0` e `-0`: "eu posso usar o menos com o zero para dizer o que é um zero negativo".
- String vazia, "tanto com aspas simples como com aspas duplas": `if ('')` dá falso.
- `null`: "O null também é a mesma coisa. O null é um valor falso."
- `false`: "esqueci de colocar aqui o valor false [...] Obviamente ele é falso."
- Fechamento: "qualquer outro valor que seja diferente de [NaN], [...] de 0, menos 0 e string vazia, tanto com aspas simples ou com aspas duplas, é o false [...] Fora isso, todos os outros valores são [truthy]."

### Os truthy

- String preenchida, "ainda que seja com zero mesmo": `'0'` é truthy. "O tal número zero [...] vai representar um valor falso", a string não.
- "Pode ser Fernando aqui": `'Fernando'` também. "Porque uma string com valor" é truthy.
- `{}` e `[]` entram no `if` ("o objeto vazio", "o array também. A mesma coisa").
- `2` é truthy.

### Dupla negação

- "Tem uma forma de [a] gente descobrir [...] a representação booleana de um valor sem utilizar o if: [...] utilizar duas vezes o sinal [...] de exclamação."
- "Um único sinal de exclamação, ele converte para booleano, inverte valores"; o segundo inverte "o valor de novo".
- Demonstração: `!!true` é `true`, `!!2` e `!!'Fernando'` são `true`, `!!''` e `!!""` são `false`, `!!false` é `false`, `!!'0'` é `true`.
- "Essa é a forma mais fácil, mais prática de você descobrir [se] um valor é truthy ou falsy." Mas "dificilmente você vai precisar": o `if` já converte sozinho. "A gente vai verificar [...] mais pra frente" se vale a pena usar.

## Precisões e tensões com a wiki

`⚠️` A skill lang-dynamic não tem arquivo de referência para coerção e truthy/falsy no JavaScript básico; as precisões vêm da MDN e da especificação, marcadas `[external]` (sem fetch, conhecimento base; confiança alta salvo indicação).

1. **A lista da aula tem seis ou sete dos oito falsy.** `[external]` São `false`, `0`, `-0`, `0n`, `''`, `null`, `undefined` e `NaN` (https://developer.mozilla.org/en-US/docs/Glossary/Falsy). `0n` (BigInt) é do ES2020, depois da gravação. `undefined` não aparece em nenhum trecho legível; "A ONU também é falsa" e "na Arena também é falso" são os candidatos (média-baixa). `document.all` é a exceção histórica ([[wiki/concepts/truthy-e-falsy]]).
2. **String vazia com crase também é falsy.** `[external]` A aula cita aspas simples e duplas, da era ES5; desde o ES2015 a template literal vazia (`` `` ``) é a mesma string `''` ([[wiki/concepts/template-literals]]).
3. **`NaN` é do tipo number, como já dito na série.** `typeof NaN` é `'number'` ([[wiki/sources/javascript-ninja-operadores-unarios]]). "Ele não é nulo" provavelmente é "ele não é número" (inferência, média).
4. **`-0` é falsy, mas não é distinguível por `===`.** `[external]` `-0 === 0` é `true`; só `Object.is(-0, 0)` dá `false`. "Negativo igual a zero" está certo para `===`.
5. **Truthy ≠ `== true`.** `[external]` `'0'` é truthy, mas `'0' == false` é `true`, porque o `==` converte os dois para número; `[] == false` também é `true`. A aula testa com `if` e `!!`, que usam *ToBoolean*, e por isso não cai nessa armadilha ([[wiki/concepts/igualdade-javascript]]).
6. **`!!x` é o mesmo que `Boolean(x)`.** `[external]` As duas formas chamam *ToBoolean*; `Boolean(x)` é mais legível, `!!x` é o idioma comum. Não confundir com `new Boolean(false)`, que é objeto e portanto truthy ([[wiki/concepts/operadores-unarios-javascript]]).
7. **"Dificilmente você vai precisar" vale para o `if`, não para o resto.** `[external]` A conversão explícita aparece em `array.filter(Boolean)`, em flags serializadas e em retorno de função que deve ser booleano. E `valor || padrao` troca qualquer falsy (`0`, `''`), enquanto `??` troca só `null`/`undefined` ([[wiki/concepts/null-e-undefined]], [[wiki/concepts/operadores-logicos-javascript]]).
8. **Contra o vídeo 04 da semana 2.** Lá, "a condição vai se tornar um valor booleano" ficou só com comparações; esta aula mostra o caso geral, que a source anterior antecipou como precisão `[external]` ([[wiki/sources/javascript-ninja-instrucoes-condicionais-if]]).
9. **Legenda.** Trocas principais: "na índia"→Ninja, "estrofe"→truthy, "bullyng/bullying na mente"→booleanamente, "tu"/"TRU"/"tio"/"tudo"→true, "esfinge"/"estilingue"/"cidade"/"Cicinho"/"extinguir"→string, "as pacientes"/"os passivos"→aspas simples, "nu"→null, "rei"→array, "menos era"→menos zero, "hífen"/"wi fi"/"FI"/"e Phil"→if, "chips"→tipos, "Hellyétt F. Ou falso"→é truthy ou falsy, "chance e fazer"→truthy e falsy, "torná lo"→ternário. Lista completa no [[wiki/log]].

## Entities

- [[wiki/entities/fernando-daciuk]]: instrutor (inferido).
- [[wiki/entities/javascript-ninja]]: o curso.
- [[wiki/entities/javascript]]: assunto.

## Concepts

- [[wiki/concepts/truthy-e-falsy]]
- [[wiki/concepts/estruturas-condicionais-javascript]]
- [[wiki/concepts/operadores-unarios-javascript]]
- [[wiki/concepts/operadores-logicos-javascript]]
- [[wiki/concepts/tipos-primitivos-javascript]]
- [[wiki/concepts/null-e-undefined]]
- [[wiki/concepts/igualdade-javascript]]
- [[wiki/concepts/objetos-javascript]]
- [[wiki/concepts/logica-booleana]]
- [[wiki/concepts/template-literals]]

## Open Questions

- **`undefined` e `NaN`.** "A ONU também é falsa", "na Arena também é falso" e "testou a falha de novo, na Arena" vêm logo depois de `null` e da recapitulação; um deles deve ser `undefined` e outro `NaN` (média-baixa). Ficaram literais.
- **"Os valores apresentados por Fausto Silva":** provavelmente "representados por falsy"; "definidos no nome, ou seja, não é número, [...] ele ama" deve ser "NaN, ou seja, *not a number*, [...] o NaN". Ficou literal, salvo o `[NaN]` da citação do fechamento.
- **"Uma 2.0 [...] 5.0, o rendimento do teste vai ser ótimo":** é o `if (0)`; os números da legenda não fazem sentido e ficaram literais.
- **"Se o banco deixe esse símbolo" e "o banco usa":** provavelmente "exclamação" ou o `!`; literal.
- **"Avaliar um valor novamente" e "testar novamente o JavaScript":** "novamente" pode ser "booleanamente" nesses trechos (média-baixa); só a forma explícita "bullyng na mente" foi corrigida.

## Raw quotes

- "valor truthy é todo aquele valor que, booleanamente falando, [...] ele é representado por true"
- "o zero, na verdade, dentro da string, ele não é a mesma coisa que um número zero"
- "um único sinal de exclamação, ele converte para booleano, inverte valores"
