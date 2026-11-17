---
type: source
title: "JavaScript assíncrono: síncrono × assíncrono, exemplos e vantagens (FrontPUSH)"
aliases: ["FrontPUSH JS assíncrono", "módulo de JavaScript ES6, aula 12", "JS Assíncrono"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [javascript, assincrono, sincrono, event-loop, ajax, axios, promise, fetch, async-await, requisicao-http, curso, frontend]
skill: lang-dynamic
status: draft
source_file: "/home/nemomartins/Documentos/dev-brain/raw/frontpush-javascript-assincrono-sincrono-vs-assincrono.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-16
---

# JavaScript assíncrono (FrontPUSH)

## TL;DR

Aula 12 do módulo de JavaScript ES6 do [[wiki/entities/frontpush|FrontPUSH]], com [[wiki/entities/nasser|Násser]] (pela sequência; não diz o nome). Aula curta e só conceitual (cerca de 4 min, sem código), que abre a parte de requisições depois da [[wiki/sources/frontpush-json-parse-stringify-comunicacao-front-back|aula de JSON]]. Ver [[wiki/concepts/javascript-assincrono]].

- **Síncrono** "vem de sincronia, que denota a ideia de ordem": termina a primeira tarefa, executa a segunda, depois a terceira.
- **Assíncrono:** "quando acontece algum evento", outra tarefa roda fora dessa ordem, em "tasks [...] que rodam no fundo da aplicação", o que dá "essa ideia de processamento paralelo".
- **Exemplo:** requisição HTTP que devolve um JSON, transformar em objeto, pegar uma característica e cadastrar no banco.
- **Ferramentas que vêm a seguir:** [[wiki/concepts/ajax|AJAX]], [[wiki/entities/axios|Axios]], [[wiki/concepts/promise-javascript|Promises]], [[wiki/concepts/fetch-api|Fetch]], [[wiki/concepts/async-await|async/await]].
- **Vantagem:** "carregar seção [...] sem precisar recarregar a página inteira", como o miolo do produto num e-commerce. "Economiza recursos" e dá "maior controle de quando iniciar alguma função".

## Key Claims

### Síncrono

- "A palavra síncrono vem de sincronia, que denota a ideia de ordem, então é literalmente quando você executa uma tarefa e depois outra tarefa e depois outra tarefa."
- "Quando termina a primeira [...] eu executo a segunda, quando termina a segunda, eu executo a terceira, então tem uma certa ordem."

### Assíncrono

- "Quando acontece algum evento, eu faço ele rodar uma outra tarefa de maneira assíncrona dessa ordem, então ela independe dessa ordem para poder acontecer."
- Exemplo: "faço uma requisição via URL por meio do protocolo HTTP [...] e ele me devolve um JSON. Dentro desse JSON, eu posso fazer uma outra tarefa para poder transformar ele em um objeto [...] e, por exemplo, cadastro no banco de dados." Ver [[wiki/concepts/requisicao-http]] e [[wiki/concepts/json]].
- "Uma série de tarefas que acontecem de maneira assíncrona [...] que não necessariamente está dentro de uma ordem estabelecida dentro do nosso código."
- "Depende das tasks de tarefas que rodam no fundo da aplicação, que o seu JavaScript vai estar rodando o síncrono bonitinho e você pode fazer o assíncrono no fundo, então meio que vai dar essa ideia de processamento paralelo." Ver [[wiki/concepts/event-loop-performance-js]].

### Exemplos e vantagens

- "O AJAX, Axios, Promises, o que são promessas, o Fetch, Async, Await, então nós vamos conhecer esses métodos que ilustram o JavaScript assíncrono."
- "Carregar seção, por exemplo, sem precisar recarregar a página inteira." E-commerce: "você clica simplesmente para carregar o miolo daquela página, só um produto, para que eu vou clicar e fazer de maneira síncrona para poder carregar todos os itens mais uma vez". Ver [[wiki/concepts/single-page-application]].
- "Isso economiza recursos [...] e ainda consegue fazer ele de maneira paralela, então eu consigo otimizar a minha aplicação."
- "Eu tenho maior controle de quando iniciar alguma função mediante essas particularidades do JavaScript assíncrono."

## Entities

- [[wiki/entities/nasser]]: instrutor (pela sequência do módulo).
- [[wiki/entities/frontpush]]: curso; módulo de JavaScript ES6, aula 12.
- [[wiki/entities/javascript]]: assunto da aula.
- [[wiki/entities/axios]]: citado entre os exemplos.

## Concepts

- [[wiki/concepts/javascript-assincrono]] (criado neste ingest)
- [[wiki/concepts/event-loop-performance-js]]
- [[wiki/concepts/ajax]]
- [[wiki/concepts/promise-javascript]]
- [[wiki/concepts/async-await]]
- [[wiki/concepts/fetch-api]]
- [[wiki/concepts/callback-javascript]]
- [[wiki/concepts/concorrencia]]
- [[wiki/concepts/paralelismo]]
- [[wiki/concepts/single-page-application]]
- [[wiki/concepts/json]]
- [[wiki/concepts/requisicao-http]]

## Precisões e tensões com a wiki

`[skill: lang-dynamic]` Referência: `nodejs-core.md` (event loop, microtasks, bloqueio). Resto do MDN como `[external]`, sem fetch nesta sessão (confiança alta).

- **Não é paralelo, é concorrente.** O JavaScript roda o seu código numa thread só. O que corre "no fundo" é do ambiente (navegador ou libuv no Node): rede, timers, disco. Quando terminam, um callback entra na fila e o [[wiki/concepts/event-loop-performance-js|event loop]] o executa quando a pilha esvazia. Duas funções JS nunca rodam ao mesmo tempo na mesma thread; paralelismo real pede Web Workers ou `worker_threads`. Ver [[wiki/concepts/concorrencia]] × [[wiki/concepts/paralelismo]].
- **O exemplo mistura assíncrono e síncrono.** Esperar a resposta HTTP é assíncrono; o `JSON.parse` e o "pegar uma característica" são síncronos e rodam na ordem. A sequência requisição → objeto → banco é uma cadeia de dependências, e por isso se escreve com `then` ou `await` em ordem. `[skill: lang-dynamic]` Um `JSON.parse` grande até bloqueia a thread.
- **"Cadastrar no banco" a partir do front.** No navegador, o cadastro é outra requisição ao back-end, não acesso direto ao banco ([[wiki/sources/frontpush-json-parse-stringify-comunicacao-front-back|aula 11]]). No Node, a frase vale literalmente.
- **"Síncrono = ordem" está pela metade.** Assíncrono também tem ordem; a diferença é se a próxima linha espera o resultado ou não (bloqueante × não bloqueante). `[external]` E as microtasks (Promises) rodam antes das macrotasks (`setTimeout`): `nodejs-core.md` mostra a saída `nextTick → promise → timeout → immediate`.
- **A lista mistura camadas.** AJAX é a técnica (de `XMLHttpRequest`); Fetch é a API nativa moderna; Axios é biblioteca sobre XHR (no navegador) ou `http` (no Node); Promise é o tipo que representa o resultado futuro; `async/await` é sintaxe sobre Promises. Falta o primeiro mecanismo de todos, o [[wiki/concepts/callback-javascript|callback]], que o curso já usou com `addEventListener` e `forEach`.
- **"Carregar só uma seção" é o argumento do AJAX e das SPAs**, e é real: menos dados trafegados, sem piscar a página. Mas o ganho principal é não travar a interface enquanto a rede responde; um XHR síncrono (`async: false`, obsoleto) congelaria a página.
- **Eventos já eram assíncronos.** Os listeners das [[wiki/sources/frontpush-dom-parte-3-eventos-addeventlistener-target-keydown|aula 10]] rodam quando o evento acontece, fora da ordem do código; a aula liga "evento" a assíncrono sem lembrar disso.

## Open Questions

- "Por isso que eu escrevi aqui": há um texto ou slide na tela que a legenda não mostra.
- A ordem anunciada (AJAX, Axios, Promises, Fetch, async/await) é a ordem das próximas aulas? Axios antes de Promise seria estranho, porque o Axios devolve Promises.

## Raw quotes

- "síncrono vem de sincronia, que denota a ideia de ordem"
- "você pode fazer o assíncrono no fundo"
- "sem precisar recarregar a página inteira"
