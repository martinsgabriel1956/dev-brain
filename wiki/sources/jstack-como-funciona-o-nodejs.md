---
type: source
title: "JStack, aula 01: como funciona o Node.js"
aliases: ["JStack aula 01", "como funciona o Node.js", "JStack Node.js call stack event loop"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [nodejs, javascript, runtime, v8, libuv, call-stack, pilha, single-thread, non-blocking-io, thread-pool, event-loop, callback-queue, callback, assincrono, jstack, iniciante, cs-fundamentals]
skill: lang-dynamic
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/jstack-como-funciona-o-nodejs.md"
source_url: ""
author: "Mateus Silva (inferido)"
date_published: ""
date_ingested: 2026-11-16
---

# JStack, aula 01: como funciona o Node.js

## TL;DR

Aula de abertura (cerca de 10 min) do curso [[wiki/entities/jstack]], com [[wiki/entities/mateus-silva]] (autoria inferida pelo "como assim Mateus?" da fala). Antes do código, uma visão macro de como o [[wiki/entities/nodejs|Node.js]] executa JavaScript, em quatro partes:

1. **O que é o Node.** Não é linguagem, é "uma plataforma, ou [...] runtime". O [[wiki/entities/v8|V8]] chegou com o Chrome em 2008, é open source, e em 2009 [[wiki/entities/ryan-dahl|Ryan Dahl]] o levou para o servidor. O V8 é apresentado como "interpretador", com a analogia do tradutor entre um brasileiro e um japonês.
2. **Call Stack.** `printDouble(2)` → `double` → `multiply` empilham e desempilham; "a primeira função que entra é a última a sair" ([[wiki/concepts/pilha|LIFO]]).
3. **Single thread × non-blocking I/O.** Uma call stack só, então "apenas uma coisa por vez". Mesmo assim o Node executa I/O em paralelo porque roda sobre a [[wiki/entities/libuv|libuv]], que implementa [[wiki/concepts/thread-pool]] e [[wiki/concepts/event-loop-performance-js|event loop]] (e também file system e DNS).
4. **O fluxo de um `db.query`.** `console.log('Antes')` → `db.query(query, callback)` sai da stack e vai para o thread pool → `console.log('Depois')` → a query termina, o [[wiki/concepts/callback-javascript|callback]] vai para a *callback queue* → o event loop, "como se fosse um while true", o leva à stack quando ela está vazia.

O modelo é bom para começar, mas tem três simplificações que a wiki corrige em "Tensões e precisões": I/O de rede (como uma query de banco) **não** passa pelo thread pool; o V8 é um motor com compilador JIT, não só um interpretador; e a "callback queue" única esconde as fases do event loop e as microtasks.

## Key Claims

### O que é o Node.js

- **Runtime, não linguagem.** "O Node não é uma linguagem de programação. O Node é uma plataforma, ou você pode chamar também de runtime, que permite que a gente execute código JavaScript [...] do lado do servidor." Slide: "Plataforma que permite rodar JavaScript no servidor." Correto.
- **JavaScript nasceu no navegador.** Foi "criado para executar apenas nos nossos browsers".
- **V8 em 2008.** "Lá em 2008, uma versão do Chrome foi lançada e junto com essa versão, veio um carinha chamado V8", que "é open source". `[external]` O Chrome e o V8 foram lançados em 2 de setembro de 2008: https://v8.dev/ e https://en.wikipedia.org/wiki/V8_(JavaScript_engine) (sem fetch nesta sessão, confiança alta).
- **V8 como "interpretador".** A máquina "não consegue entender o código JavaScript"; é preciso algo "no meio do caminho" que "traduz para [...] um idioma, entre aspas, que a máquina vai conseguir compreender", como um intérprete entre um brasileiro e um japonês ou o Google Tradutor. Ver as tensões e [[wiki/concepts/compilador]].
- **Node em 2009.** "Um carinha chamado Ryan Dahl, pegou esse V8 e executou ele no servidor [...] e aí nasceu o que a gente conhece hoje como Node.js." Correto: apresentado na JSConf EU de novembro de 2009 `[external]` https://en.wikipedia.org/wiki/Node.js.

### Call Stack

- **Definição.** "A pilha de processamento do nosso código, ou seja, todas as funções que a gente executa vão para essa pilha."
- **Exemplo do slide:**

```js
function multiply(a, b) { return a * b; }
function double(number) { return multiply(number, 2); }
function printDouble(number) {
  const result = double(number);
  console.log(result);
}
printDouble(2);
```

- **Passo a passo.** O JavaScript lê de cima para baixo e declara as três funções; nada entra na stack até `printDouble(2)`. Entram `printDouble`, `double`, `multiply` (o slide mostra as três empilhadas). `multiply` retorna e sai, "o papel dela já foi concluído"; `double` sai em seguida; `console.log` entra e sai; por fim `printDouble` sai.
- **LIFO.** "A primeira função que entra é a última a sair": `multiply` foi a última a entrar e a primeira a sair, e `printDouble`, o "ponto de entrada", ficou até o fim. Ver [[wiki/concepts/pilha]].
- **Importância.** "Não é nenhum [bicho de sete cabeças]", mas "tem um peso muito grande no nosso código".

### Single thread e non-blocking I/O

- **Single thread.** Slide: "Single Thread / Apenas uma Call Stack / Apenas uma coisa por vez." "Enquanto ela está ocupada a gente não consegue executar outra coisa."
- **A aparente contradição.** O Node é "non-blocking I/O", "o que a gente conhece também como execução de código assíncrono": deixar "uma query executando no banco de dados enquanto processa um outro tipo de conteúdo". As duas coisas são verdade. Ver [[wiki/concepts/non-blocking-io]] e [[wiki/concepts/concorrencia]].
- **libuv.** "Debaixo dos panos ali ele roda com uma biblioteca escrita em C chamada libuv", que implementa o thread pool e o event loop, "quem possibilita que a gente execute esses códigos assíncronos entre aspas em background". Também implementa "toda a parte de file system do Node, de DNS". Ver [[wiki/entities/libuv]].

### Thread pool, callback queue e event loop

- **Exemplo do slide:**

```js
console.log('Antes');
db.query(query, function callback(err, data) {
  console.log(data);
});
console.log('Depois');
```

- **"Função bloqueante".** `db.query` "leva um certo tempo para ser executada": conectar, executar a query, esperar a resposta. Se o Node "não tomasse nenhuma ação", ela "ficaria travada ali na minha Call Stack", e a linha de baixo não rodaria.
- **Delegação.** O Node "entende que essa função aqui vai bloquear a minha Call Stack" e "joga para dentro da libuv, dentro do nosso thread pool"; `db.query` sai da stack e `console.log('Depois')` roda. Ver [[wiki/concepts/thread-pool]].
- **Callback queue.** Quando a query termina, a função de callback (o segundo argumento, `(err, data)`) vai para a *callback queue* "com os dados já retornados do banco de dados". "Callback [...] numa tradução literal, seria ligue de volta": "depois que isso aqui terminar de executar, você me liga de volta". Ver [[wiki/concepts/callback-javascript]].
- **Event loop.** Fica entre a callback queue e a call stack, "como se fosse um while true" que pergunta "tem, não, tem, não". Quando há uma função e a call stack "está liberada", ele a move para a stack; o `console.log(data)` roda e a stack esvazia. "É assim que o Node consegue executar código assíncrono." Ver [[wiki/concepts/event-loop-performance-js]].
- **Ordem de saída** (inferida do modelo, não dita): `Antes`, `Depois`, depois os dados.

## Tensões e precisões

- **Query de banco não vai para o thread pool.** A libuv usa o thread pool para file system, DNS (`getaddrinfo`/`getnameinfo`) e trabalho enviado por `uv_queue_work`; "network I/O is always performed in a single thread, each loop's thread", com sockets não bloqueantes sobre epoll (Linux), kqueue (macOS/BSD) e IOCP (Windows) `[external]` https://docs.libuv.org/en/v1.x/design.html. Drivers como `pg` e `mysql2` falam TCP com o banco, então a espera fica no kernel, não numa thread do pool. No Node, o pool também atende `crypto` assíncrono (`pbkdf2`, `scrypt`) e `zlib` `[external]` https://nodejs.org/en/learn/asynchronous-work/dont-block-the-event-loop (sem fetch nesta sessão, confiança alta). O exemplo funcionaria igual com `fs.readFile`, que de fato usa o pool.
- **"Função bloqueante" com o sentido trocado.** Na documentação do Node, bloqueante é a operação síncrona que segura a thread (`readFileSync`, loop pesado, JSON grande). `db.query` com callback é uma API **não bloqueante** que demora. O Node também não "entende" que uma função vai bloquear: a API é assíncrona por desenho. Uma função síncrona pesada bloqueia a stack, e o Node não faz nada a respeito ([[wiki/sources/node-single-thread-ssr-bloqueio-event-loop]]).
- **V8 não é só interpretador.** É um motor com interpretador de bytecode (Ignition) e compiladores JIT (Sparkplug, Maglev, TurboFan) que geram código de máquina para funções "quentes" `[skill: lang-dynamic]` (`references/nodejs-core.md`). A analogia do tradutor serve para "o processador não entende JavaScript"; "interpretador" é o termo errado. Ver [[wiki/concepts/compilador]].
- **Uma "callback queue" só é simplificação.** O event loop da libuv passa por fases (timers, pending callbacks, poll, check, close), e o callback de I/O roda na fase poll. Entre callbacks rodam as microtasks: `process.nextTick` antes, depois promises. Por isso um `.then` resolvido roda antes de um `setTimeout(fn, 0)` `[skill: lang-dynamic]`.
- **"while true" que pergunta sem parar.** O loop não fica girando: na fase poll ele **bloqueia** em `epoll_wait` (ou equivalente) até chegar evento ou vencer um timer, e não gasta CPU. E não é infinito: quando não há mais handles ou requisições ativos, o loop termina e o processo sai `[external]` https://docs.libuv.org/en/v1.x/design.html.
- **"Single thread" é sobre o seu JavaScript.** O processo Node tem várias threads (as 4 do pool por padrão, ajustável por `UV_THREADPOOL_SIZE`, e threads do V8 para GC e compilação). E `worker_threads` permite rodar JavaScript em paralelo ([[wiki/concepts/thread]]). O que é único é a call stack que roda o seu código por event loop.
- **Node em 2009 não usava libuv.** A primeira versão usava libev e libeio; a libuv surgiu em 2011, com o porte para Windows `[external]` https://en.wikipedia.org/wiki/Libuv (sem fetch nesta sessão, confiança média). A aula descreve o Node de hoje, então isso não muda o argumento.
- **Concorrência, não paralelismo.** "Ele consegue executar mais de uma coisa ao mesmo tempo" vale para esperas de I/O sobrepostas. O seu código continua rodando uma coisa por vez. Ver [[wiki/concepts/concorrencia]].

## Entities

- [[wiki/entities/jstack]]: o curso
- [[wiki/entities/mateus-silva]]: instrutor (inferido)
- [[wiki/entities/nodejs]]: o runtime
- [[wiki/entities/v8]]: motor JavaScript do Chrome
- [[wiki/entities/libuv]]: thread pool, event loop, file system, DNS
- [[wiki/entities/ryan-dahl]]: criador do Node
- [[wiki/entities/google]]: Chrome e V8

## Concepts

- [[wiki/concepts/pilha]]: call stack, LIFO
- [[wiki/concepts/thread-pool]]
- [[wiki/concepts/non-blocking-io]]
- [[wiki/concepts/event-loop-performance-js]]: event loop, callback queue
- [[wiki/concepts/callback-javascript]]: "ligue de volta"
- [[wiki/concepts/thread]]: single thread, worker threads
- [[wiki/concepts/concorrencia]]
- [[wiki/concepts/compilador]]: V8 "interpretador" × JIT

## Open Questions

- O curso vai mostrar promises e `async/await` como a mesma ideia do callback, e explicar a fila de microtasks?
- O resto do curso usa um driver de banco real? Se sim, vale conferir que a query sai pelo socket no event loop, não pelo thread pool.

## Raw quotes

> "O Node não é uma linguagem de programação. O Node é uma plataforma, ou você pode chamar também de runtime."

> "A primeira função que entra é a última a sair."

> "Callback [...] numa tradução literal, seria ligue de volta."
