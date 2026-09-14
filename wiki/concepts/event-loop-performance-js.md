---
type: concept
title: "Event Loop e Performance JavaScript"
aliases: ["event loop js", "bloqueio event loop", "nodejs performance", "single thread js"]
date_created: 2026-06-02
date_updated: 2026-09-14
source_count: 2
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

## Key Sources

- [[wiki/sources/5-dicas-performance-javascript]]
- [[wiki/sources/node-single-thread-ssr-bloqueio-event-loop]] — caso concreto de SSR pesado (CPU-bound) travando o event loop inteiro e causando tela em branco para todos os usuários; distinção explícita I/O-bound vs. CPU-bound e por que `await`/`setTimeout` não resolvem bloqueio de CPU
