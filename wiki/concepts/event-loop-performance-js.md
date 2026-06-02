---
type: concept
title: "Event Loop e Performance JavaScript"
aliases: ["event loop js", "bloqueio event loop", "nodejs performance", "single thread js"]
date_created: 2026-06-02
date_updated: 2026-06-02
source_count: 1
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
