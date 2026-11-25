---
type: source
title: "O operador módulo (JavaScript Ninja, semana 7, vídeo 01)"
aliases: ["JavaScript Ninja operador módulo", "JS Ninja %", "01 - O operador módulo", "operador de resto JavaScript Ninja"]
date_created: 2026-11-25
date_updated: 2026-11-25
source_count: 0
tags: [javascript, operadores, modulo, resto, par-impar, while, incremento, debugging]
skill: lang-dynamic
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/javascript-ninja-operador-modulo.md"
source_url: ""
author: "Fernando Daciuk"
date_published: ""
date_ingested: 2026-11-25
---

# O operador módulo (JavaScript Ninja, semana 7, vídeo 01)

## TL;DR

Primeiro vídeo depois da resolução do desafio da semana 6 do [[wiki/entities/javascript-ninja|JavaScript Ninja]] (cerca de 9 min), por isso citado como semana 7 (inferência, média-alta). Autoria de [[wiki/entities/fernando-daciuk|Fernando Daciuk]] ("Fernando da Silva" na legenda). Apresenta o `%`, que faltava na aula 02 de [[wiki/concepts/operadores-aritmeticos-javascript|operadores aritméticos]].

- **O que faz:** "retorna [...] o resto da divisão entre dois operandos", "representado pelo sinal de porcentagem", usado "no lugar da barra".
- **Analogias:** três bolas para três pessoas, não sobra nenhuma (`3 % 3` é 0); cinco carros para duas pessoas, "não posso cortar um carro no meio", dois para cada e sobra um (`5 % 2` é 1).
- **Par e ímpar:** um número é par quando "dividido por dois ele tem resto zero"; `13 % 2` tem sobra, então é ímpar; `4 % 2` é 0, então é par.
- **Pares de 0 a 20 com `while`:** primeiro imprime todos de 0 a 20 (corrigindo `< 20` para `<= 20`), depois filtra com `if (num % 2 === 0)` ([[wiki/concepts/estruturas-de-repeticao-javascript]]).
- **Erro ao vivo:** incrementar o número antes do teste fez o console mostrar os ímpares; movendo o incremento para depois do `if`, saem 0, 2, 4... 20 ([[wiki/concepts/incremento-e-decremento]]).
- **Errar faz parte:** "é isso que vai acontecer no seu dia a dia [...] você vai errar e você vai precisar analisar e entender aquilo que está sendo feito" ([[wiki/concepts/debugging]]).
- **Próximo vídeo:** arrays, porque "na verdade não existem arrays de verdade [...] são objetos disfarçados" ([[wiki/concepts/array]]).

## Key Claims

### O que é o módulo

- "Operador de módulo, representado pelo sinal de porcentagem. O que ele faz? Ele retorna para o resto da divisão entre dois operandos."
- É usado "no lugar do sinal de dividir, no lugar da barra" e devolve "o valor inteiro que é o resto dessa divisão".
- "É matemática básica de toda divisão com números inteiros."

### As analogias

- "Três bolas e vou dividir por três pessoas [...] dar uma bala para cada pessoa e não sobra nenhuma. Então o resto da divisão é zero."
- "Cinco carros [...] para duas pessoas [...] dois carros e meio. Opa. Mas eu não posso cortar um carro no meio." Dois para cada: "um total de quatro, e um carro vai sobrar."
- `4 / 2` é 2; `5 / 2` é 2,5; "se não houvesse [resto], por exemplo, 4 no módulo 2, ele vai retornar a zero."

### Par e ímpar

- "Eu sei que o número [...] é par quando esse número ele é dividido por dois ele tem resto zero."
- "13 módulo 2, ou seja, o 13 não é um número par, porque quando eu tento dividir por dois [...] minha sobra é diferente de zero." Em seguida diz "o 3 é um número ímpar" (a legenda mistura 13 e 3).

### Imprimindo os pares de 0 a 20

- Relembra o `while`: "enquanto a condição do while ela for verdadeira ele vai entrando ali [...] e quando aquela estrutura for falsa, ele simplesmente sai do while e continua o programa normal."
- Primeiro, `num = 0`, "enquanto for menor que 20"; corrige para "menor igual a 20" para imprimir "do zero até o vinte".
- Segundo, "se o número dividido por 2 [der] 0, vai fazer console ponto log, porque senão ele não vai imprimir nada."
- O erro: "eu acabei mostrando os ímpares [...] eu peguei o número já se somando, e já somando eu fiz a divisão pelo dois."
- A correção: "se num dividido por dois for igual a zero, console ponto log num, senão não mostra nada", com o incremento depois. Saída: "0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20."
- "Por isso eu precisava incrementar depois que eu fizesse o meu cálculo."

### Errar faz parte

- "Ando aqui mostrando como é que isso acontece, errando, porque é isso que vai acontecer no seu dia a dia."
- "Você vai errar e você vai precisar analisar e entender aquilo que está sendo feito [...] pra você saber se realmente aquilo que você está fazendo está certo."

### Próximo vídeo

- "A gente vai conversar um pouquinho mais sobre [...] array [...] na verdade não existem arrays de verdade [...] Na verdade são objetos disfarçados."

## Precisões e tensões com a wiki

`⚠️` A skill lang-dynamic não tem arquivo de referência para operadores básicos de JavaScript; as precisões vêm da MDN e da especificação, marcadas `[external]` (sem fetch, conhecimento base; confiança alta salvo indicação). https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Remainder

1. **`%` é resto, não módulo.** `[external]` O nome "módulo" é comum, mas o sinal do resultado segue o dividendo: `-13 % 2` dá `-1`, não `1`. Por isso `n % 2 === 1` falha para ímpares negativos; o teste seguro é `n % 2 !== 0`. O módulo matemático (sempre positivo) é `((n % m) + m) % m`. A página [[wiki/concepts/operadores-aritmeticos-javascript]] já registrava isso.
2. **Nem sempre inteiro.** `[external]` "O valor inteiro que é o resto" vale para operandos inteiros. Com fração, `5.5 % 2` dá `1.5`; `x % 0` dá `NaN`. A aula só usa inteiros, então a afirmação não erra no contexto.
3. **`5 / 2` é 2,5 mesmo.** `[external]` JavaScript não tem divisão inteira; o quociente das analogias ("dois carros para cada") é `Math.floor(5 / 2)` ou `Math.trunc`. Quociente e resto juntos reconstroem o número: `2 * 2 + 1 === 5`.
4. **O erro dos ímpares.** O código exato não aparece na legenda. A explicação ("peguei o número já se somando [...] eu fiz a divisão") bate com `if (num++ % 2 === 0) console.log(num)`: o pós-incremento testa o valor antigo (par) e o `console.log` mostra o novo (ímpar), de 1 a 21 (inferência, média). Outra hipótese é o `num++` antes do `if`, mas aí sairiam os pares de 2 a 20, e não os ímpares ([[wiki/concepts/incremento-e-decremento]]).
5. **Sem `%` também dá.** `[external]` Para pares de 0 a 20, `for (var n = 0; n <= 20; n += 2)` faz 11 voltas em vez de 21 e não precisa de `if`. O `%` serve quando o número vem de fora (testar um valor qualquer) ou para ciclos: alternar cor de linha (`i % 2`), índice circular (`i % length`), "a cada N" (`i % N === 0`) ([[wiki/concepts/estruturas-de-repeticao-javascript]]).
6. **`< 20` × `<= 20`.** A correção ao vivo é o off-by-one que a página de loops já descreve: "de 0 a 20" inclui o 20.
7. **"Arrays são objetos disfarçados".** `[external]` `typeof []` dá `'object'`; para distinguir, `Array.isArray`. Mas o array tem `length` automático e herda de `Array.prototype`, então "não existem arrays de verdade" exagera. A aula 01 já dizia o mesmo ([[wiki/concepts/array]], [[wiki/concepts/objetos-javascript]]).
8. **"No ano passado".** Ele diz "você lembra que no ano passado a gente falou [...] sobre [...] a estrutura de repetição while"; deve ser "no vídeo passado" (o `while` é a semana 6, vídeo 02). Mantido literal no raw.
9. **Legenda.** Trocas principais: "na índia"→Ninja; "da Silva"→Daciuk; "modo"/"modelo"/"Modula" (14×)→módulo; "Pay"/"pago"/"pais"→par/pares; "receio"→resto; "ai"/"áudio" (4×)→while; "Lupi"→loop; "alto incrementado"→auto incrementado; "com logo"→console log; "ouvinte"→vinte; "imperador"/"interesses"→ímpares; "contrato"→contrário; "eu não dividir [...] foi [...] sinal"→num dividido [...] for [...] senão; "acordando"→codando; "a rede"/"rei"→array/arrays. Lista completa no [[wiki/log]].

## Entities

- [[wiki/entities/fernando-daciuk]]: instrutor.
- [[wiki/entities/javascript-ninja]]: o curso.
- [[wiki/entities/javascript]]: assunto.

## Concepts

- [[wiki/concepts/operadores-aritmeticos-javascript]]
- [[wiki/concepts/estruturas-de-repeticao-javascript]]
- [[wiki/concepts/incremento-e-decremento]]
- [[wiki/concepts/estruturas-condicionais-javascript]]
- [[wiki/concepts/debugging]]
- [[wiki/concepts/array]]
- [[wiki/concepts/objetos-javascript]]

Vídeo anterior do curso na wiki: [[wiki/sources/javascript-ninja-estrutura-de-repeticao-while]].

Vídeo seguinte na wiki: [[wiki/sources/javascript-ninja-arrays-propriedade-length]] (semana 7, vídeo 02), o de arrays que este anuncia.

## Open Questions

- **Código do erro dos ímpares**: `num++` dentro da condição (média) ou outra forma; a legenda não mostra.
- **"Que o número 22" / "o solo contou logo mais e fechou o set"**: montagem do primeiro loop (talvez `console.log(num++)` e o eco final do REPL); baixa. Literal.
- **"No caso do 5 o módulo 2 é igual a meu ver na prática"**: provavelmente "é igual a 1. Vamos ver na prática" (média); literal.
- **"Menor é a 25"**: deve ser "menor ou igual a 20" (média); literal.
- **"Não recebi mais mas"**: provavelmente "num recebe mais mais" (`num++`) (média); literal.
- **"Pra sub20" / "vai levantar"**: fecho do vídeo, ilegível (baixa).

## Raw quotes

- "Mas eu não posso cortar um carro no meio, né?"
- "Você vai errar e você vai precisar analisar e entender aquilo que está sendo feito"
- "Na verdade são objetos disfarçados."
