---
type: source
title: "Arrays e estruturas de repetição (for e while) em JavaScript (FrontPUSH)"
aliases: ["FrontPUSH arrays e loops", "módulo de JavaScript ES6, aula 06", "Array & Loops"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [javascript, array, indice, pop, push, length, for, while, loop-infinito, off-by-one, json, curso, frontend]
skill: lang-dynamic
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/frontpush-arrays-e-loops-for-while-javascript.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-16
---

# Arrays e estruturas de repetição em JavaScript (FrontPUSH)

## TL;DR

Aula 06 do módulo de JavaScript ES6 do [[wiki/entities/frontpush|FrontPUSH]], com [[wiki/entities/nasser|Násser]] (diz o nome). Aula "um pouquinho mais introdutória" que "prepara o terreno": o back-end devolve [[wiki/concepts/json|JSON]], que "basicamente são arrays, objetos", e o front-end precisa percorrê-los.

- **Array:** "uma variável com vários compartimentos", em colchetes, que aceita valores, funções e outros arrays (uni, bi, tridimensional). Ver [[wiki/concepts/array]].
- **Índice:** o armário com gavetas que "sempre começa com 0"; `frutas[0]` é maçã, e `frutas[4]` num array de quatro dá `undefined`.
- **Aninhado:** `['maçã', 'uva', 'mamão', 'laranja', ['nanica', 'prata']]` tem tamanho 5; `frutas[4][1]` é prata.
- **Métodos:** `typeof` dá `object`, "mas é um objeto do tipo array", que herda `indexOf`, `join`, `map`, `pop`, `push`. `pop` "remove o último item e retorna ele"; `push` adiciona no fim; `length` dá o tamanho.
- **Estruturas de repetição:** "blocos de código para poder repetir de forma inteligente". Três partes: "como começa", "como termina", "como modifica". Ver [[wiki/concepts/estruturas-de-repeticao-javascript]].
- **for:** `for (let i = 0; i <= 12; i++)` roda 13 vezes, não 12 (corrigido ao vivo). `i++` é `i = i + 1`.
- **Loop infinito:** sem o "como modifica", "vai ficar rodando infinitamente" e trava o navegador. Acontece de verdade na gravação: ele esquece o `i++` no `while` e o browser trava.
- **while:** "mais aberto"; dá para incrementar só dentro de um `if`, controlado por um booleano.
- **Percorrer o array:** `i <= 5` com cinco itens imprime `undefined` no fim; a forma certa é `i < frutas.length`, no `while` e no `for`.

## Key Claims

### Por que arrays

- "O front-end faz muito isso. Quando a gente comunica com o back-end, a gente sempre faz uma requisição e esse arquivo vem em JSON. E o JSON basicamente são arrays, objetos que eles dois têm um conceito parecido."
- As próximas aulas vão "continuar explorando os arrays e iterações [...] descobrir mais métodos".

### Array e índices

- "É uma variável com vários compartimentos [...] você pode colocar tanto valores como funções como outros arrays [...] unidimensionais ou bidimensionais, tridimensionais."
- "Quando eu for definir um objeto é por meio de chaves, quando é um array é por meio de colchetes."
- "Eu vou colocar entre chaves o número do índice" (são colchetes, como ele mesmo usa no código).
- "Pensa que isso aqui é uma gaveta e esse aqui é um armário [...] a gaveta em arrays sempre começa com 0." `frutas[0]` → maçã, 1 → uva, 2 → banana, 3 → laranja, 4 → `undefined`, "porque eu não defini a posição".
- Aninhado: banana troca por mamão e entra `['nanica', 'prata']` no fim; `frutas[4]` devolve "um arrayzinho", `frutas[4][1]` é prata e `frutas[4][0]` é nanica.
- "Índices que começam de 0 até a quantidade do tamanho do seu array."

### Métodos herdados

- "Segundo a última aula, eu disse que tudo em JavaScript é um objeto [...] Ele está identificando como um objeto, mas é um objeto do tipo array. Então ele já herdou muitas funções e propriedades de forma nativa."
- `pop`: "remove o último item e retorna ele". Útil para "mostrar de trás para frente o item e ele vai acabando". `frutas.pop()` devolve `['nanica', 'prata']`, e o array cai de 5 para 4.
- `push`: "adiciona um item [...] o que você vai passar no argumento, no final do array". Com kiwi, o tamanho volta a 5.
- `length` "vai voltar o tamanho do array".

### Estruturas de repetição

- "São blocos de código para poder repetir de forma inteligente alguma coisa [...] é bem programação raiz aqui, é o for e o while."
- "Ela é composta de três parâmetros, não necessariamente você precisa [...] informar todos eles": "como começa a iteração", "como termina" e "como modifica".
- `for (let i = 0; i <= 12; i++)`: "esse loop vai rodar 12 vezes porque ele está começando no zero [...] na verdade ele está rodando 13 vezes". Começando de 1, roda 12.
- "i++ é exatamente igual eu escrever isso aqui, só que de maneira mais contraída, então é o i recebendo o valor antigo do i mais um."
- "É sempre uma boa prática você estabelecer essas três cláusulas, porque você pode acabar criando um loop infinito e travar o seu browser ou a sua máquina sem querer."

### while

- "O for é mais voltado para interações de números [...] o while é mais voltado para algo mais aberto [...] ele abraça mais possibilidades."
- "No for sempre no começo da interação ele vai incrementar [...] o i é menor ou igual a 12? Sim [...] ele executa e soma 1 [...] e fica nessa até essa condição se tornar falsa."
- "No while eu consigo [...] colocar cláusulas if aqui dentro e fazer com que o i só seja incrementado se encaixar nessa cláusula if." Um `boolean = true` decide o incremento, e "essa variável aqui pode estar em outra parte do seu código sendo também modificada, ou então puxando de algum banco de dados".

### Percorrendo o array

- `console.log('fruta ' + frutas[i])` dentro do `while`. Com o `i++` esquecido: "eu criei um loop infinito, está vendo? O meu browser já travou [...] isso consome muito processamento, então muito cuidado."
- `i <= 5` com cinco itens: "ele rodou até o 5 e está undefined [...] como tem 5 itens é de 0 até 4."
- "Eu posso colocar frutas.length [...] só que você tem que colocar menor para poder justamente ele não contar a última posição já que começa no 0." O mesmo no `for`.

## Entities

- [[wiki/entities/nasser]]: instrutor (diz o nome).
- [[wiki/entities/frontpush]]: curso; módulo de JavaScript ES6.
- [[wiki/entities/javascript]]: assunto da aula.

## Concepts

- [[wiki/concepts/array]]
- [[wiki/concepts/estruturas-de-repeticao-javascript]] (criado neste ingest)
- [[wiki/concepts/json]]
- [[wiki/concepts/objetos-javascript]]
- [[wiki/concepts/tipos-primitivos-javascript]]
- [[wiki/concepts/event-loop-performance-js]]
- [[wiki/concepts/estruturas-condicionais-javascript]]
- [[wiki/concepts/operadores-aritmeticos-javascript]]
- [[wiki/concepts/template-literals]]
- [[wiki/concepts/loops-sass]]
- [[wiki/concepts/logica-de-programacao]]

## Precisões e tensões com a wiki

`⚠️` Sem arquivo de referência na skill lang-dynamic para arrays e loops; as precisões vêm do MDN (`[external]`).

- **O `while` não vê mudanças "em outra parte do seu código" durante o loop.** `[external]` JavaScript roda o seu código numa thread só: um `while` síncrono ocupa a thread inteira, e nenhum clique, timer ou resposta de banco é processado até ele acabar ([[wiki/concepts/event-loop-performance-js]]). Se o booleano que libera o `i++` for `false`, o loop nunca termina. É o mesmo travamento que a gravação mostra com o `i++` esquecido. Esperar algo externo se faz com eventos, promises e `await`, não com `while`.
- **O incremento do `for` roda no fim de cada volta, não "no começo".** `[external]` A ordem é: inicialização uma vez; condição; corpo; incremento; condição de novo (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for). A descrição seguinte da aula ("executa e soma 1") está certa.
- **"Três parâmetros" é a anatomia do `for`, não de toda repetição.** O `while` só tem a condição; inicialização e incremento ficam por conta de quem escreve, e por isso ele se esquece com mais facilidade. Um `if` dentro do corpo também cabe no `for` (com `continue`); a escolha prática é `for` quando se sabe quantas voltas e `while` quando o fim depende de uma condição.
- **Para percorrer array, o JS moderno raramente usa índice.** `for...of` (ES2015), `forEach`, `map` e `filter` eliminam o *off-by-one* do `i <= 5` e o risco de esquecer o `i++` ([[wiki/concepts/estruturas-de-repeticao-javascript]]). A aula promete esses métodos para depois.
- **`typeof []` é `'object'`.** `[external]` Para saber se é array, `Array.isArray(x)` ([[wiki/concepts/tipos-primitivos-javascript]]). Aqui o "tudo é objeto" acerta: array é objeto de verdade, com protótipo `Array.prototype` ([[wiki/concepts/objetos-javascript]]).
- **JSON não "são" arrays e objetos.** É um formato de texto com a sintaxe dos literais de objeto e array do JavaScript (aspas duplas obrigatórias, sem funções nem `undefined`). Vira objeto com `JSON.parse` ou `response.json()` ([[wiki/concepts/json]]).
- **Índices vão de 0 até `length - 1`**, não "até a quantidade do tamanho"; a própria aula corrige isso com `<`.
- **"Entre chaves o número do índice"** são colchetes; chaves são do objeto, como ele disse um minuto antes.
- **"Essas duas estruturas condicionais"** são de repetição; a aula troca os nomes duas vezes no fim.
- **`push` devolve o novo tamanho, e `pop` e `push` mudam o array original.** Em React, mudar o array do estado não re-renderiza; usa-se cópia (`[...frutas, 'kiwi']`), como a wiki registra em [[wiki/concepts/imutabilidade]].
- **`i++` × `i = i + 1`:** iguais como instrução; como expressão, `i++` devolve o valor antigo (`let a = i++`) ([[wiki/concepts/operadores-aritmeticos-javascript]]).
- **"Iteração" × "interação":** a aula alterna as duas; o termo é iteração (cada volta do loop).

## Open Questions

- "Mamão papaia e não lembro o nome do outro": o outro é o formosa.
- O vídeo foi editado depois do travamento ("voltei dando aula"); não dá para saber quanto foi cortado.

## Raw quotes

- "a gaveta em arrays sempre começa com 0"
- "o meu browser já travou"
- "é sempre uma boa prática você estabelecer essas três cláusulas"
