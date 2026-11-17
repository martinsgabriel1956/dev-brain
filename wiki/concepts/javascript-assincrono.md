---
type: concept
title: "JavaScript assíncrono"
aliases: ["JS assíncrono", "assincronia em JavaScript", "síncrono vs assíncrono", "código não bloqueante"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 3
tags: [javascript, assincrono, sincrono, event-loop, callback, promise, async-await, nao-bloqueante, lang-dynamic]
skill: lang-dynamic
status: stub
---

# JavaScript assíncrono

Código **síncrono** roda linha a linha, e cada linha espera a anterior terminar. Código **assíncrono** começa uma operação demorada (rede, timer, disco, evento) e segue em frente; o resultado chega depois, por um callback, uma Promise ou um `await`.

## Como funciona (uma thread, várias filas)

`[skill: lang-dynamic]` (`nodejs-core.md`) e `[external]` (MDN):

- O motor executa o código JavaScript numa **única thread**, com uma pilha de chamadas.
- As operações demoradas ficam com o **ambiente**: Web APIs no navegador (`fetch`, `setTimeout`, eventos do DOM) e libuv no Node (I/O, timers).
- Quando terminam, o callback vai para uma fila. O [[wiki/concepts/event-loop-performance-js|event loop]] o executa quando a pilha esvazia.
- **Microtasks** (Promises, `queueMicrotask`) rodam antes das **macrotasks** (`setTimeout`, I/O). No Node: `nextTick → promise → timeout → immediate`.
- É [[wiki/concepts/concorrencia|concorrência]], não [[wiki/concepts/paralelismo|paralelismo]]: duas funções JS não rodam ao mesmo tempo na mesma thread. Trabalho pesado de CPU (um `JSON.parse` enorme) bloqueia tudo; para paralelo real há Web Workers e `worker_threads`.

## Evolução das ferramentas

1. [[wiki/concepts/callback-javascript|Callback]]: a função passada para rodar depois (`addEventListener`, `setTimeout`, o error-first do Node). Encadeados, viram o *callback hell*.
2. [[wiki/concepts/ajax|AJAX]] / `XMLHttpRequest`: requisição sem recarregar a página, com callbacks de evento.
3. [[wiki/concepts/promise-javascript|Promise]] (ES2015): um objeto que representa o resultado futuro; `then`/`catch` encadeados, `Promise.all` para tarefas independentes.
4. [[wiki/concepts/fetch-api|Fetch]]: API nativa de requisição que devolve Promise. [[wiki/entities/axios|Axios]] é a biblioteca equivalente, também com Promises.
5. [[wiki/concepts/async-await|async/await]] (ES2017): sintaxe que deixa a cadeia de Promises com cara de código síncrono.

## Por que importa no front-end

- A interface não trava enquanto a rede responde.
- Dá para atualizar só uma parte da página (base das [[wiki/concepts/single-page-application|SPAs]]).
- Tarefas que dependem umas das outras ficam em sequência (`await` encadeado); as independentes vão em paralelo de espera (`Promise.all`).

## No FrontPUSH, JavaScript aula 12

Em [[wiki/sources/frontpush-javascript-assincrono-sincrono-vs-assincrono]], [[wiki/entities/nasser|Násser]] define síncrono como "ideia de ordem" e assíncrono como tarefas que "rodam no fundo da aplicação", com "ideia de processamento paralelo". Exemplo: requisição HTTP → JSON → objeto → cadastro. Lista AJAX, Axios, Promises, Fetch e async/await como as próximas aulas. A precisão: o que corre "no fundo" é o ambiente, e o código JS continua numa thread só.

Em [[wiki/sources/frontpush-ajax-xmlhttprequest-open-send-readystate]], a aula 14 mostra o assíncrono na aba Network: a requisição "demora um pouquinho [...] ela executa a página e em seguida faz a requisição". O `onreadystatechange` registrado depois do `send` ainda funciona porque a resposta só chega numa volta seguinte do event loop ([[wiki/concepts/xmlhttprequest]]).

Em [[wiki/sources/frontpush-promises-resolve-reject-then-catch]], o `Promise {<pending>}` no console demonstra o assíncrono: o log roda "imediatamente depois" da chamada, antes de a requisição voltar. O `then` roda quando a Promise assenta, como microtask.

## Key sources

- [[wiki/sources/frontpush-javascript-assincrono-sincrono-vs-assincrono]]: FrontPUSH, JavaScript aula 12: síncrono × assíncrono e as ferramentas que vêm
- [[wiki/sources/frontpush-ajax-xmlhttprequest-open-send-readystate]]: FrontPUSH, JavaScript aula 14: XHR assíncrono na aba Network
- [[wiki/sources/frontpush-promises-resolve-reject-then-catch]]: FrontPUSH, JavaScript aula 15: pending como prova do assíncrono
