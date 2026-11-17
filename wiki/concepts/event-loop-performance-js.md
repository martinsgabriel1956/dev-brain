---
type: concept
title: "Event Loop e Performance JavaScript"
aliases: ["event loop js", "bloqueio event loop", "nodejs performance", "single thread js"]
date_created: 2026-06-02
date_updated: 2026-11-16
source_count: 8
tags: [javascript, nodejs, event-loop, performance, web-streams, async]
skill: lang-dynamic
status: stable
---

# Event Loop e Performance JavaScript

O event loop é o núcleo do modelo de concorrência de JavaScript: uma única thread processa eventos sequencialmente. Qualquer operação síncrona que demore bloqueia **todos** os outros eventos enquanto não terminar.

## O Problema Central

```
10 clientes → cliente 1 chama readFileSync
→ clientes 2–10 aguardam
→ aplicação parece travada
```

Toda função com sufixo `Sync` é potencialmente um ponto de bloqueio: `readFileSync`, `writeFileSync`, `execSync`, etc.

## Padrões que Travam o Event Loop

| Anti-padrão | Impacto | Fix |
|---|---|---|
| `readFileSync` em servidor | Paralisa todos os clientes | `fs.readFile` / `fsPromises.readFile` |
| `console.log` em produção | Síncrono — acumula I/O | **Pino** (assíncrono, multithreads) |
| Processar lista grande em memória | GC pressure + bloqueio | Web Streams / processamento sob demanda |
| Loop `for` sobre array de 1M itens | Bloqueia por tempo proporcional | Generator / Stream |

## Web Streams — Processamento sob Demanda

Parte da especificação JavaScript (sem instalação, funciona em Node.js, browser, Deno):

```js
// Anti-padrão: tudo em memória
const dados = await lerTudoDeUmaVez()  // 10 GB → memória
processar(dados)

// Padrão: sob demanda
const stream = criarReadableStream()
for await (const chunk of stream) {
  processar(chunk)  // 1 item, transformar, liberar memória
}
```

Processa 10 GB de dados no browser sem backend e sem travar a tela.

## I/O-bound vs. CPU-bound: por que o event loop escala

O event loop só dá conta de atender muita gente ao mesmo tempo porque a maior parte do trabalho de servidor é **I/O-bound** (disco, rede, banco): o Node inicia a operação, delega ao sistema operacional/thread, registra uma callback e volta a atender a fila — iniciar I/O é rápido, executá-lo é o que demora, e essa espera não ocupa a thread principal.

O problema é quando a operação é **CPU-bound**: criptografia, compactação, parse de JSON/CSV grande, ordenação/transformação de dados em memória, e — caso importante em aplicações web modernas — **renderização de página via SSR** (ver [[wiki/concepts/renderizacao-ssr-vs-csr]]). Esse tipo de operação segura a thread principal de verdade: enquanto ela roda, nenhum outro evento é processado, nem mesmo callbacks de I/O que já retornaram.

**`await` e `setTimeout`/microtasks não resolvem bloqueio de CPU.** `await` só libera a thread para operações de I/O — se a função é síncrona e pesada, `await` não tira nada da main thread. `setTimeout` e microtasks apenas adiam a execução; o código pesado ainda roda na mesma thread quando chega sua vez. As soluções reais seguem a mesma linha já documentada acima (chunking, Web Streams) mais [[wiki/concepts/thread|worker threads]] para tirar de fato o trabalho CPU-bound da thread principal.

## Arquitetura Assíncrona (além do código)

Não só evitar `Sync` — projetar o sistema para separar **recebimento** de **processamento**:

```
Cliente envia CSV
→ API salva arquivo (rápido)
→ API responde: "em processamento" (imediato)
→ Worker separado processa CSV em background
→ Notifica cliente quando pronto
```

Benefícios: custo de VM menor, responsabilidades isoladas, falhas contidas.

## Achar o código que segura a thread

Quando não se sabe qual função é cara, um [[wiki/concepts/cpu-profiling|CPU profile]] gravado durante um [[wiki/concepts/teste-de-carga]] mostra onde a thread passa o tempo. Em [[wiki/sources/cpu-profiling-nodejs-inspector-autocannon-erick-wendel]], o vilão era uma cópia profunda dos dados a cada requisição.

## O modelo didático: call stack, callback queue e event loop

Em [[wiki/sources/jstack-como-funciona-o-nodejs]], o event loop é "como se fosse um while true" entre a *callback queue* e a call stack: quando a operação assíncrona termina, o callback vai para a fila, e o loop o passa para a [[wiki/concepts/pilha|call stack]] assim que ela está vazia. O modelo é útil, com três ajustes:
- **Não há uma fila só.** O loop da [[wiki/entities/libuv|libuv]] passa por fases (timers, pending, poll, check, close); entre callbacks rodam as microtasks (`process.nextTick`, depois promises) `[skill: lang-dynamic]`.
- **Não fica perguntando "tem, não, tem".** Na fase poll ele dorme no epoll/kqueue/IOCP até chegar evento ou vencer um timer, e termina quando não há mais nada pendente.
- **I/O de rede não vai para o [[wiki/concepts/thread-pool]]**; só disco, DNS, crypto e zlib. Ver [[wiki/concepts/non-blocking-io]].

## Por que o servidor não termina (JStack, aula 04)

Em [[wiki/sources/jstack-criando-o-servidor-http]], `node src/index.js` fica rodando, ao contrário dos scripts da aula 03, porque o `listen` registra um handle ativo na [[wiki/entities/libuv|libuv]], e o loop só sai quando não há mais handles nem requisições pendentes. Cada requisição chega como evento e chama o handler do `createServer` na mesma thread.

Em [[wiki/sources/frontpush-arrays-e-loops-for-while-javascript]], o loop infinito acontece na gravação: um `while` sem `i++` trava o navegador ("isso consome muito processamento"). É a thread principal ocupada; nada mais roda até o loop terminar. Pela mesma razão, um `while` que espera um booleano mudar "em outra parte do seu código, ou então puxando de algum banco de dados" nunca o vê mudar.

Em [[wiki/sources/frontpush-javascript-assincrono-sincrono-vs-assincrono]], o assíncrono são "tasks [...] que rodam no fundo da aplicação" enquanto o JavaScript roda "o síncrono bonitinho", com "ideia de processamento paralelo". O que roda no fundo é o ambiente (Web APIs, libuv); o callback volta pela fila e o event loop o executa na mesma thread. Ver [[wiki/concepts/javascript-assincrono]].

Em [[wiki/sources/frontpush-promises-resolve-reject-then-catch]], o `resolve` "levanta uma bandeirinha verde" que "aciona o then". `[skill: lang-dynamic]` Na prática, o callback do `then` entra na fila de microtasks e roda quando a pilha esvazia, antes dos timers.

## Key Sources

- [[wiki/sources/5-dicas-performance-javascript]]
- [[wiki/sources/node-single-thread-ssr-bloqueio-event-loop]] — caso concreto de SSR pesado (CPU-bound) travando o event loop inteiro e causando tela em branco para todos os usuários; distinção explícita I/O-bound vs. CPU-bound e por que `await`/`setTimeout` não resolvem bloqueio de CPU
- [[wiki/sources/cpu-profiling-nodejs-inspector-autocannon-erick-wendel]]: CPU gasto por requisição (cópia profunda com `cloneDeep`) derruba a capacidade da rota de 11.000 para 2000 requisições; como achar o culpado com [[wiki/concepts/cpu-profiling]]
- [[wiki/sources/jstack-como-funciona-o-nodejs]]: modelo call stack + callback queue + event loop, com correções
- [[wiki/sources/jstack-criando-o-servidor-http]]: listen mantém o loop vivo; requisição = evento
- [[wiki/sources/frontpush-arrays-e-loops-for-while-javascript]]: FrontPUSH, JavaScript aula 06: loop infinito trava o browser
- [[wiki/sources/frontpush-javascript-assincrono-sincrono-vs-assincrono]]: FrontPUSH, JavaScript aula 12: "no fundo da aplicação" (é o ambiente, não outra thread JS)
- [[wiki/sources/frontpush-promises-resolve-reject-then-catch]]: FrontPUSH, JavaScript aula 15: then como microtask (a bandeirinha)
