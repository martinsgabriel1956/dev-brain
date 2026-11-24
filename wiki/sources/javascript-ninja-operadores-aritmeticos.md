---
type: source
title: "Operadores aritméticos (JavaScript Ninja, aula 02)"
aliases: ["JavaScript Ninja aula 02", "JS Ninja operadores aritméticos", "02 - Operadores aritméticos"]
date_created: 2026-11-24
date_updated: 2026-11-24
source_count: 0
tags: [javascript, expressoes, operadores, operadores-aritmeticos, incremento, decremento, pos-incremento, pre-incremento, atribuicao-composta, espaco-em-branco, legibilidade, nodejs, repl]
skill: lang-dynamic
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/javascript-ninja-operadores-aritmeticos.md"
source_url: ""
author: "Fernando Daciuk (inferido do curso)"
date_published: ""
date_ingested: 2026-11-24
---

# Operadores aritméticos (JavaScript Ninja, aula 02)

## TL;DR

Vídeo seguinte ao de [[wiki/sources/javascript-ninja-variaveis-e-tipos-de-dados|variáveis e tipos de dados]] no [[wiki/entities/javascript-ninja|JavaScript Ninja]] (cerca de 9 min), de novo no REPL do [[wiki/entities/nodejs|Node]]. O instrutor não diz o nome; a autoria de [[wiki/entities/fernando-daciuk|Fernando Daciuk]] vem do curso.

- **Expressão** é "uma frase em JavaScript que pode ser avaliada para produzir um certo valor", e "uma das maneiras mais comuns de criar expressões" é com operadores ([[wiki/concepts/expressao-javascript]]).
- **Quatro aritméticos:** `+`, `-`, `*` e `/`: `1 + 2` dá 3, `10 - 3` dá 7, `3 * 3` dá 9, `10 / 2` dá 5 ([[wiki/concepts/operadores-aritmeticos-javascript]]).
- **Espaços em branco** em volta do operador "não tem diferença nenhuma"; servem "para que o nosso código fique mais legível".
- **`++` e `--`**, os "operadores aritméticos abreviados". Pós (`soma++`) devolve o valor e depois soma; pré (`++soma`) "já vai adicionou mais um e depois ele vai interpretar o valor" ([[wiki/concepts/incremento-e-decremento]]).
- **Atribuição composta:** `+=`, `-=`, `*=`, `/=`. `soma += 20` "é basicamente igual a `soma = soma + 20`" ([[wiki/concepts/atribuicao-composta]]).
- Próximo vídeo: operadores de igualdade e relacionais ([[wiki/concepts/igualdade-javascript]]).

Continua em [[wiki/sources/javascript-ninja-operadores-de-igualdade-e-relacionais]].

## Key Claims

### Expressões

- "Nós fizemos aquilo tudo, o que nós fizemos foram expressões [...] uma expressão, ela nada mais é do que uma frase em JavaScript que pode ser avaliada para produzir um certo valor."
- Exemplo: "a gente criou a variável x [...] var x é igual a zero [...] quando nós chamamos a variável x, ela é avaliada e produz o valor que foi colocado sobre ela."
- "Uma das maneiras mais comuns de criar expressões JavaScript [é] usando operadores."

### Os quatro operadores

- "Quatro tipos de operadores aritméticos em JavaScript, que são os operadores básicos da matemática": adição pelo "sinal de mais", subtração "pelo traço ou pelo sinal de menos", multiplicação "pelo asterisco" e divisão "pela barra".
- `1 + 2` "retornou o valor três"; "isso é uma expressão no JavaScript, que é uma frase que eu estou dizendo que o código JavaScript deve fazer". Depois, `10 - 3` = 7, `3 * 3` = 9, `10 / 2` = 5, `50 / 5`.

### Espaços em branco

- "Espaços em branco que eu estou usando para separar essas expressões não tem diferença nenhuma em JavaScript": "10 e um espaço gigantesco [...] barra 2" e sem espaço nenhum dão o mesmo.
- Mesmo assim, use "o espaço para separar [...] o sinal do nosso operador [...] para que o nosso código fique mais legível", "para que fique fácil a visualização" e "você saiba exatamente onde está ocorrendo a operação".

### Incremento e decremento

- "Nós temos também o uso dos operadores aritméticos abreviados [...] mais mais ou menos menos."
- `var soma = 10 + 10` dá 20; `soma = soma + 1`, 21. "Se eu fizer soma mais mais, vai ser basicamente [...] soma igual soma mais 1, que no caso daria 22."
- "Isso aqui, na verdade, ele vai fazer o pós-incremento": o eco do REPL ainda mostra o valor antigo, e chamar `soma` depois mostra 22.
- "Agora, se eu fizer mais e mais soma [...] ele já vai, adicionou mais um, e depois ele vai interpretar o valor de soma": 23.
- "Menos menos funciona exatamente do mesmo jeito": `soma = soma - 1` dá 22; `soma--` mostra 22 e deixa 21; "pré-decremento, que [é] o menos menos soma", "já o valor de 20 impresso aqui".

### Atribuição composta

- "Outro formato de utilizar os operadores aritméticos abreviados [...] mais igual, menos igual, vezes igual, dividido igual."
- Para somar 20 e não 1: `soma += 20` leva 21 a 41; "isso aqui é basicamente igual a soma igual soma mais 20". "Eu estou pegando [...] o valor de soma, então colocando mais o valor."
- `soma -= 20` volta a 21; um `soma--` final, a 20.

## Precisões e tensões com a wiki

`⚠️` A skill lang-dynamic não tem arquivo de referência para operadores de JavaScript; as precisões vêm do MDN e da especificação, marcadas `[external]` (sem fetch, conhecimento base; confiança alta salvo indicação). Referência geral: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators

1. **`var x = 0` não é expressão, é instrução.** `[external]` Declaração é *statement* e não produz valor: por isso o REPL ecoa `undefined` depois dela (ver a aula anterior, precisão 1). `x = 0` sem `var` é expressão de atribuição e vale `0`; `x` sozinho também é expressão. A definição da aula está certa, o exemplo não ([[wiki/concepts/expressao-javascript]]).
2. **Não são quatro.** A wiki já lista `%` (resto) e `**` (potência, ES2016, posterior à aula), além do `+` e `-` unários (`+'5'` dá 5) ([[wiki/concepts/operadores-aritmeticos-javascript]]). A aula também não toca na coerção: `'10' + 2` dá `'102'`, `'10' - 2` dá 8.
3. **`++` e `--` não são "aritméticos abreviados" de `+=`.** São incremento e decremento: só valem para uma referência (`5++` é `SyntaxError`) e convertem para número. Com `let s = '5'`, `s++` deixa `s` com 6, mas `s += 1` dá `'51'` ([[wiki/concepts/incremento-e-decremento]]).
4. **Pré × pós só importa quando o valor é usado.** Como instrução solta, `soma++` e `++soma` fazem o mesmo. A diferença aparece em `y = soma++` (y recebe o antigo) e `y = ++soma` (y recebe o novo). A aula mostra isso pelo eco do REPL, sem nomear a regra. Por causa dessa armadilha, o estilo de Douglas Crockford e a regra `no-plusplus` do ESLint preferem `+= 1` (média-alta) ([[wiki/concepts/pitfalls-de-linguagem]]).
5. **Espaço "não tem diferença nenhuma" tem exceções.** Vale entre tokens, não dentro deles (`1 0` é erro). E os sinais podem colar: `a - -b` é subtrair o negativo, `a --b` é erro de sintaxe, e `a+++b` vira `a++ + b`. Quebra de linha também importa por causa da inserção automática de ponto e vírgula (`return` seguido de quebra devolve `undefined`). Um formatador (Prettier) resolve a legibilidade sem decisão manual.
6. **Faltam atribuições compostas.** Além das quatro, existem `%=`, `**=` e as lógicas `&&=`, `||=`, `??=` (ES2021) ([[wiki/concepts/atribuicao-composta]]).
7. **"Não posso usar somente o menos menos"** no fim é provavelmente "eu posso usar": a demonstração seguinte usa `soma--` (média).
8. **Legenda.** O ASR manteve bem os números e trocou menos que na aula anterior: "Os jovens ninja"→JavaScript Ninja, "arreios"→arrays, "vai"→var, "lamentou"→retornou, "semânticos"→aritméticos, "requerimento"→decremento, "some"/"soube"→soma, "varanda ou"→variável. Trechos sem sentido ficaram literais (lista no [[wiki/log]]).

## Entities

- [[wiki/entities/fernando-daciuk]]: instrutor (inferido do curso; não se apresenta).
- [[wiki/entities/javascript-ninja]]: o curso.
- [[wiki/entities/javascript]]: assunto.
- [[wiki/entities/nodejs]]: REPL das demonstrações.

## Concepts

- [[wiki/concepts/expressao-javascript]] (criado neste ingest)
- [[wiki/concepts/operadores-aritmeticos-javascript]]
- [[wiki/concepts/incremento-e-decremento]] (criado neste ingest)
- [[wiki/concepts/atribuicao-composta]] (criado neste ingest)
- [[wiki/concepts/var-let-const]]
- [[wiki/concepts/pitfalls-de-linguagem]]
- [[wiki/concepts/estruturas-de-repeticao-javascript]]
- [[wiki/concepts/igualdade-javascript]]

## Open Questions

- "Vindos de fora do Brasil, que nós estamos dando um giro pela língua": saudação a alunos estrangeiros? Ficou literal.
- "A divisão, ela é representada pela barra invariante na prática": "invariante" talvez seja "e vamos ver".
- O trecho entre o `soma = soma + 1` e o `soma++` ("eu sou Mei todo o valor, eu que sou uma gatinha cara 20") é ininteligível na legenda.
- "Mais, mais 26, 21, quero que fique 41": o 26 é provavelmente 20, pela conta.

## Raw quotes

- "uma frase em JavaScript que pode ser avaliada para produzir um certo valor"
- "ele já vai, adicionou mais um, e depois ele vai interpretar o valor de soma"
- "para que o nosso código fique mais legível"
