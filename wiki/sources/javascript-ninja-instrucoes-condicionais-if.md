---
type: source
title: "Instruções condicionais: if (JavaScript Ninja, semana 2, vídeo 04)"
aliases: ["JavaScript Ninja if", "JS Ninja if, else e else if", "04 - Instruções condicionais - IF"]
date_created: 2026-11-24
date_updated: 2026-11-24
source_count: 0
tags: [javascript, condicionais, if-else, else-if, controle-de-fluxo, operadores-logicos, boolean]
skill: lang-dynamic
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/javascript-ninja-instrucoes-condicionais-if.md"
source_url: ""
author: "Fernando Daciuk"
date_published: ""
date_ingested: 2026-11-24
---

# Instruções condicionais: if (JavaScript Ninja, semana 2, vídeo 04)

## TL;DR

Quarto vídeo da "segunda aula" do [[wiki/entities/javascript-ninja|JavaScript Ninja]] (cerca de 10 min), depois de [[wiki/sources/javascript-ninja-estrutura-lexica|estrutura léxica]]. O desafio da semana 2, prometido no vídeo anterior, fica para o próximo: "nós temos um assunto antes disso". Autoria de [[wiki/entities/fernando-daciuk|Fernando Daciuk]] ("falando da Silva" na legenda, a deformação de sempre).

- **`if`** dá "um controle pra gente [...] tomar algumas decisões": executa uma instrução "fundamentada em alguma validação". A condição entre parênteses "vai se tornar um valor booleano" ([[wiki/concepts/estruturas-condicionais-javascript]]).
- Com `x = 3`, `y = 7`: `if (x === 3) { y = 3 }` muda o `y`, "porque ele entrou nessa condição".
- **Com operadores lógicos:** `&&`, `||` e `!` "retornam também valores booleanos" e cabem no `if` ([[wiki/concepts/operadores-logicos-javascript]]). Com a condição falsa, o bloco é ignorado e as variáveis ficam como estavam.
- **`else`** "vai servir como senão": `if (x === 2) { y = 2 } else { y = 10 }` dá `y = 10`.
- **`else if`** testa "mais de duas coisas": "como se fosse mais um if", encadeado; se tudo for falso, cai no `else` final.
- Próximo vídeo: o desafio da semana 2.

## Key Claims

### O que é

- "Uma instrução condicional chamada if [...] ela vai dar um controle pra gente, para que [a] gente possa definir ou tomar algumas decisões do que a gente quer fazer, ou [...] se a gente quer executar alguma instrução fundamentada em alguma [...] validação."
- Sintaxe: "eu vou usar o if, abre e fecha parênteses", a condição dentro, e o bloco entre chaves com o que fazer "se isso [...] for verdadeira".
- "Essa instrução dentro do if, ela vai se tornar um valor booleano."

### Demonstração do `if`

- `var x = 3; var y = 7; if (x === 3) { y = 3; }`. "Ele vai entrar no if e vai fazer o y vale 3 [...] Porque ele entrou nessa condição: essa condição aqui foi verdadeira."

### Com `&&` e `||`

- "Lembro dos operadores [...] AND, OR, NOT? Então a gente vai poder usar eles também com if, porque [...] eles retornam também valores booleanos."
- Com `x = 3` e `y = 3`: `if (x === y && x === 3) { x = 5; y = 2; }` entra, "porque [...] X valia 3, ele era igual ao Y".
- "Eu posso fazer a mesma coisa também utilizando o operador" or: `x === 5 || ...`; "se qualquer uma dessas condições for verdadeira, ele vai [retornar] que essa instrução aqui é verdadeira". O bloco põe `x` e `y` em 1.
- Condição falsa: `if (x === 2) { x = 5; y = 5; }` com `x = 1`. "Como X não é igual a 2, ele simplesmente ignorou isto aqui."

### `else`

- "Ela funciona junto com o if [...] se [...] for verdadeira, ele vai entrar aqui dentro; senão, ele vai entrar no else."
- `if (x === 2) { y = 2; } else { y = 10; }` com `x = 1`: "como o X não é igual a 2, ele caiu aqui no Y é igual a 10".

### `else if`

- "Para testar mais de duas coisas." Com `if`/`else`, "eu só posso fazer dois testes".
- "Else, espaço, if": `if (x === 2) {...} else if (y === 3) {...} else if (x === y) {...} else { x = 0; y = 0; }`, com `x = 1` e `y = 10`.
- O `else if` é "como se fosse mais um if como esse primeiro aqui, só que sempre dentro dessa avaliação". Nada bateu, então "ele vai cair no else": `x` e `y` viram 0.

## Precisões e tensões com a wiki

`⚠️` A skill lang-dynamic não tem arquivo de referência para controle de fluxo em JavaScript; as precisões vêm da MDN e da especificação, marcadas `[external]` (sem fetch, conhecimento base; confiança alta salvo indicação).

1. **A condição não precisa ser booleana.** `[external]` O `if` converte o valor por *ToBoolean*: `if ('texto')`, `if (1)` e `if ([])` entram; `if ('')`, `if (0)`, `if (null)` não. "Vai se tornar um valor booleano" é certo nesse sentido, mas `&&` e `||` não "retornam valores booleanos", devolvem um operando que o `if` depois converte ([[wiki/concepts/truthy-e-falsy]], [[wiki/concepts/operadores-logicos-javascript]]).
2. **"Como se fosse mais um if" está certo.** `[external]` `else if` não é palavra-chave: é um `else` cujo corpo é outro `if`. Por isso não existe `elseif` nem `elif` em JavaScript. A cadeia para na primeira condição verdadeira ([[wiki/concepts/estruturas-condicionais-javascript]]).
3. **`if` é instrução, não expressão.** Não devolve valor, então não cabe numa atribuição; para isso há o ternário (`y = x === 2 ? 2 : 10`) ([[wiki/concepts/expressao-javascript]]).
4. **`else` não é outra "instrução condicional".** É a cláusula opcional do `if`, sem condição própria.
5. **Chaves são opcionais para uma instrução, mas a aula as usa sempre, e faz bem.** `[external]` Sem chaves, só a primeira instrução fica no `if`; o bug *goto fail* da Apple (2014) veio de uma linha duplicada fora das chaves (https://www.imperialviolet.org/2014/02/22/applebug.html) ([[wiki/concepts/pitfalls-de-linguagem]]).
6. **Atribuição na condição.** `if (x = 2)` atribui e entra (2 é truthy). A aula usa `===`, o que evita a confusão e a coerção ([[wiki/concepts/igualdade-javascript]]).
7. **As contas fecham.** 3/7 → `y = 3`; 3/3 → 5/2 pelo `&&`; → 1/1 pelo `||`; `x === 2` falso mantém 1/1; o `else` dá `y = 10`; na cadeia com 1/10, nenhuma condição vale e o `else` zera os dois.
8. **Legenda.** Trocas principais: "falando da Silva"→Fernando Daciuk (média-alta), "wi fi"/"Wi-Fi"/"WiFi"/"iPhone"/"FI"/"fi"→if (cerca de 20×), "13"→três, "Set"→sete, "monitorar"→retornar, "e"→else (2×), "Valium"→vale um, "FX foi"/"e esse fim"→else if (média), "Welsh"→else (média-alta), "texto"→teste, "Deus"/"esse"/"s"→else (média), "e fi"→if, "Ibson"→Y, "sinal"→senão (média), "iPhone"→o Y é (média). Lista dos trechos literais no [[wiki/log]].

## Entities

- [[wiki/entities/fernando-daciuk]]: instrutor.
- [[wiki/entities/javascript-ninja]]: o curso.
- [[wiki/entities/javascript]]: assunto.

## Concepts

- [[wiki/concepts/estruturas-condicionais-javascript]]
- [[wiki/concepts/operadores-logicos-javascript]]
- [[wiki/concepts/truthy-e-falsy]]
- [[wiki/concepts/igualdade-javascript]]
- [[wiki/concepts/expressao-javascript]]
- [[wiki/concepts/fluxo-de-controle]]
- [[wiki/concepts/pitfalls-de-linguagem]]

## Open Questions

- "Vou colocar X e treino seja": provavelmente "X é três, ou seja"; ficou literal.
- O segundo operando do `||` ("ou o valor de y é igual... o estou igual muitos 2") se perdeu; pelo contexto, `y === 2` (média).
- "Antes de dar tiro vou digitar o citado": provavelmente o `else`; ficou literal.
- No `else if (x === y)`, o bloco dá "o X vai receber 10 e o Y vai receber 100": não afeta o resultado, porque a condição é falsa.

## Raw quotes

- "ela vai dar um controle pra gente, para que [a] gente possa [...] tomar algumas decisões"
- "o seu uso vai servir como senão pra gente"
- "como se fosse mais um if como esse primeiro aqui, só que sempre dentro dessa avaliação"
