---
type: source
title: "Arrays e iterações em JavaScript: forEach e map (FrontPUSH)"
aliases: ["FrontPUSH forEach e map", "módulo de JavaScript ES6, aula 07", "Array & Interações"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [javascript, array, foreach, map, callback, arrow-function, iteracao, json, curso, frontend]
skill: lang-dynamic
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/frontpush-arrays-e-iteracoes-foreach-map-javascript.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-16
---

# Arrays e iterações: forEach e map (FrontPUSH)

## TL;DR

Aula 07 do módulo de JavaScript ES6+ do [[wiki/entities/frontpush|FrontPUSH]], com [[wiki/entities/nasser|Násser]]. Continua a aula 06: o front-end recebe do back-end dados "em forma de objeto, seja em XML, seja em JSON" e precisa manipular arrays de objetos.

- **Callback:** a função passada como argumento, como no `addEventListener('click', fn)`. Ver [[wiki/concepts/callback-javascript]].
- **forEach:** "for vem da estrutura de repetição e each vem para cada". Percorre o array "sem você ficar pensando em índice". O callback recebe item, índice e o próprio array; "o que importa é a ordem", os nomes são livres (`a, b, c`). Ver [[wiki/concepts/metodos-de-array-javascript]].
- **Arrow function:** `marcas.forEach(item => console.log(item))` numa linha ([[wiki/concepts/arrow-functions]]).
- **Transformar cada item:** `'marca: ' + item`, `item.toUpperCase()`.
- **forEach × map:** "o map devolve um array modificado, enquanto o forEach não devolve nada".
- **Demo do map:** com `marcas` e `carros` (Polo, Argo, Kwid, LaFerrari, A3), `const carrosMarcas = marcas.map((item, index) => item + ' ' + carros[index])` junta os dois arrays pela posição. Com `forEach`, a constante fica `undefined`, e o `carrosMarcas.forEach` seguinte dá erro ("Não foi possível ler").

## Key Claims

### Por que

- "Nós como dev front-end precisamos ter uma atenção especial a isso [...] estudar em si como manipular arrays de objetos, porque [...] quando a gente faz uma requisição para o back-end, a gente precisa processar essas informações e elas na maioria das vezes vão voltar em forma de objeto, seja em XML, seja em JSON."
- Com `for` é preciso "definir o índice, ver o tamanho do array e rodar em cada interação"; "existem funções próprias que já fazem todo esse procedimento".

### Callback

- "A propriedade addEventListener [...] você coloca no primeiro argumento, por exemplo, um argumento de clique e aqui você vai colocar no segundo argumento uma função, que é uma função de callback, que é uma função genérica que você simplesmente pode colocar o que você quiser aqui." O DOM terá "uma ênfase gigantesca" mais adiante.

### forEach

- "For vem da estrutura de repetição e each vem para cada, ou seja, ele já faz a estrutura de repetição já verificando o tamanho do array."
- "Essa função já detém de três argumentos [...] Primeiro é o item [...] o próprio valor [...] O segundo vai rodar o index [...] e por último, ele vai devolver o próprio array." "Na maioria das vezes você vai querer só o item."
- `index + ' - ' + item + ' - ' + array` mostra "0, tracinho o item [...] tracinho o próprio array".
- "Entenda que isso é uma variável muda. O que importa é a ordem, sempre vai ser item, index e array. Mas eu posso muito bem colocar a, b, c."
- Arrow: "eu posso suprimir o function [...] e aí, ao invés de abrir e fechar chaves assim, eu coloco uma setinha". Com o `console.log` "ocupando somente uma linha", tira as chaves. Nomes comuns: `item`, `i` ou `e`, "que é de evento".
- Resumo: "O forEach é um método que detém três argumentos, item, index e array. E ele devolve uma função de callback [...] e ela executa essa função para cada item do array."
- `'marca: ' + item` mostra "marca VW, marca Fiat": "eu só concatenei um string a cada item e mostrei ele na tela". `item.toUpperCase()` deixa "todas as letras maiúsculas".

### map

- "O map é muitíssimo parecido com o forEach, porém, o map devolve um array modificado, enquanto o forEach não devolve nada [...] ele não modifica esse carinha aqui, ele não devolve para você um novo array."
- "Vamos supor que você queira fazer um novo array a partir desse, você não consegue com o forEach, a não ser que você faça a modificação de um outro array aqui dentro dele."
- `carrosMarcas = marcas.map(...)`: "o resultado desse método aqui é um novo array que eu vou jogar dentro dessa variável, enquanto se eu fizesse isso aqui com o forEach, ele iria atribuir para essa variável aqui undefined."
- O callback devolve o item "concatenado com carros no index específico": VW Polo, Fiat Argo, Renault Kwid, Ferrari LaFerrari, Audi A3.
- Com `forEach` no lugar do `map`, o `carrosMarcas.forEach` seguinte quebra: "Não foi possível ler, por quê? Porque ele não volta o array, o forEach, ele volta undefined."

## Entities

- [[wiki/entities/nasser]]: instrutor (a fala do aluno o chama pelo nome).
- [[wiki/entities/frontpush]]: curso; módulo de JavaScript ES6+.
- [[wiki/entities/javascript]]: assunto da aula.

## Concepts

- [[wiki/concepts/metodos-de-array-javascript]] (criado neste ingest)
- [[wiki/concepts/array]]
- [[wiki/concepts/callback-javascript]]
- [[wiki/concepts/arrow-functions]]
- [[wiki/concepts/estruturas-de-repeticao-javascript]]
- [[wiki/concepts/event-listener-javascript]]
- [[wiki/concepts/json]]
- [[wiki/concepts/imutabilidade]]
- [[wiki/concepts/string]]
- [[wiki/concepts/template-literals]]

## Precisões e tensões com a wiki

`⚠️` Sem arquivo de referência na skill lang-dynamic para métodos de array; as precisões vêm do MDN (`[external]`).

- **O forEach recebe um callback; não "devolve" um.** `[external]` `forEach` devolve `undefined` (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach). O resumo da aula inverte a direção, e o "sem precisar se preocupar com [...] callbacks" queria dizer índices.
- **O forEach não modifica o array.** "Você pode fazer toda e qualquer modificação [...] dentro desse mesmo array" e "ele simplesmente modificou e colocou marca VW" descrevem só o que foi impresso: `marcas` continua igual. O `map` também não muda o original; devolve um array **novo**, não "um array modificado" ([[wiki/concepts/imutabilidade]]).
- **A seta substitui o `function`, não as chaves.** `function (item) { }` vira `(item) => { }`; as chaves só saem quando o corpo é uma expressão ([[wiki/concepts/arrow-functions]]).
- **No `map`, o `return` é obrigatório com chaves.** Sem ele, cada posição vira `undefined`. Com corpo de expressão, o retorno é implícito: `` marcas.map((m, i) => `${m} ${carros[i]}`) ``. A aula acerta em usar `return` dentro das chaves.
- **`e` como nome do item confunde.** Por convenção, `e` é o objeto de evento de um listener ([[wiki/concepts/event-listener-javascript]]). Para um array de marcas, `marca` diz o que a variável é. O "marca, marca, marca undefined" que aparece antes da troca para `item` (num trecho sem legenda) é provavelmente esse erro de nome.
- **Juntar dois arrays pela posição** funciona se eles tiverem o mesmo tamanho e a mesma ordem. Com tamanhos diferentes, `carros[index]` dá `undefined`. Um array de objetos (`[{ marca: 'VW', carro: 'Polo' }]`) evita depender da ordem, que é como os dados costumam vir do back-end.
- **XML e JSON chegam como texto**, não "em forma de objeto"; precisam de `JSON.parse`/`response.json()` (ou `DOMParser` para XML) ([[wiki/concepts/json]]).
- **forEach não para no meio.** `break` não funciona dentro dele, e `await` dentro do callback não espera (o `forEach` ignora a promise). Para parar, `for...of`, `some` ou `find`; para async em sequência, `for...of` com `await` ([[wiki/concepts/estruturas-de-repeticao-javascript]], [[wiki/concepts/async-await]]).
- **No React**, listas são renderizadas com `map`, porque ele devolve o array de elementos; o `forEach` não devolveria nada para o JSX ([[wiki/entities/react]]).
- **Concatenação com `+`** de novo, em vez de [[wiki/concepts/template-literals|template string]].
- **"Emergir"** no começo queria dizer "imergir" (aprofundar); ficou literal no raw.

## Open Questions

- Trechos sem legenda: 00:10:19–00:10:26, 00:10:47–00:11:00 (o que causou "marca undefined" e como foi corrigido) e 00:11:52–00:12:00.
- "Event aportuguesando, que é de evento": ele quis dizer que `e` vem de *event*? A frase está truncada.

## Raw quotes

- "for vem da estrutura de repetição e each vem para cada"
- "o que importa é a ordem, sempre vai ser item, index e array"
- "o map devolve um array modificado, enquanto o forEach não devolve nada"
