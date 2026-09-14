---
type: source
title: "Como uma Única Requisição Derruba o Servidor Node.js (Event Loop, SSR e CPU-bound)"
aliases: ["bug event loop SSR", "uma requisição derruba o servidor", "SSR bloqueia event loop"]
date_created: 2026-09-14
date_updated: 2026-09-14
source_count: 0
tags: [nodejs, event-loop, ssr, cpu-bound, io-bound, worker-threads, cache, lang-dynamic]
skill: lang-dynamic
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/node-single-thread-ssr-bloqueio-event-loop.md
source_url:
author: Júnior Alves (canal de vídeo)
date_published:
date_ingested: 2026-09-14
---

# Como uma Única Requisição Derruba o Servidor Node.js (Event Loop, SSR e CPU-bound)

## TL;DR

Transcrição de vídeo que explica um bug clássico e recorrente: uma página fica com tela em branco por muito tempo porque uma única requisição de SSR (server-side rendering) travou o event loop do Node.js inteiro. O argumento central: o event loop é single thread e só consegue atender múltiplas requisições simultaneamente porque delega operações de I/O (que não seguram CPU) — mas operações CPU-bound, como renderização SSR pesada, seguram a thread principal e bloqueiam literalmente tudo, inclusive respostas que já estavam prontas. `await`, `setTimeout` e microtasks não resolvem isso porque o trabalho síncrono continua rodando na mesma thread; as soluções reais são quebrar o trabalho em chunks, worker threads, filas assíncronas e cache de renderização (ex. ISR do Next.js).

## Key Claims

1. **Renderização client-side (CSR) vs. server-side (SSR)** — em CSR, o navegador baixa JS/HTML/CSS e monta a página; o servidor só serve arquivos estáticos e responde APIs. Em SSR (Next.js, Remix, server components), o servidor roda o componente e devolve o HTML pronto — quem paga o custo de CPU da renderização é o servidor, não o cliente.
2. **O Node.js é single thread no event loop** — existe um único processador de JavaScript por processo (a "main thread"); ele executa uma operação por vez.
3. **O event loop escala porque delega I/O, não porque paraleliza CPU** — ao encontrar uma operação de I/O (disco, rede, banco), o Node delega a operação ao sistema operacional/thread, registra uma callback, e volta imediatamente a atender a fila de eventos. Iniciar I/O é rápido; executá-lo é o que demora, e essa espera não ocupa a thread principal.
4. **Toda operação do servidor é I/O-bound ou CPU-bound** — I/O-bound: acesso a disco, rede, banco (CPU quase ociosa). CPU-bound: criptografia, compactação de imagem, parse de JSON/CSV grande, ordenação/transformação de dados em memória, e **renderização de página complexa via SSR**.
5. **O bug: SSR pesado é CPU-bound e trava o event loop inteiro** — enquanto uma renderização pesada roda, o event loop não processa nenhum novo evento; nem sequer callbacks de I/O que já retornaram conseguem ser atendidos. Novas requisições HTTP se acumulam na fila; o usuário vê tela em branco; quanto mais gente acessa ao mesmo tempo, mais a fila cresce (efeito bola de neve).
6. **`await` e `setTimeout`/microtasks não resolvem bloqueio de CPU** — `await` só libera a thread para operações de I/O; se a função em si é síncrona e pesada, `await` não tira nada da main thread. `setTimeout`/microtask apenas adiam a execução — o código pesado ainda roda na mesma thread quando chega a vez.
7. **Soluções reais: chunking, worker threads, filas, cache** — (a) quebrar o trabalho pesado em pedaços menores e "respirar" entre loops; (b) delegar trabalho CPU-bound a worker threads, mantendo a thread principal livre para atender; (c) processar de forma assíncrona via filas, fora do caminho síncrono da requisição; (d) cache de renderização — evitar recomputar o mesmo HTML para cada requisição idêntica, com estratégias híbridas de estático+dinâmico (ex. ISR do Next.js).

## Entidades Mencionadas

- Next.js — citado como exemplo de framework SSR
- Remix — citado como exemplo de framework SSR

## Conceitos Tocados

- [[wiki/concepts/event-loop-performance-js]]
- [[wiki/concepts/renderizacao-ssr-vs-csr]]
- [[wiki/concepts/thread]]
- [[wiki/concepts/filas-e-workers]]
- [[wiki/concepts/cache]]
- [[wiki/concepts/hydration]]

## Open Questions

- Fonte não cita métricas reais (ex. tempo de bloqueio observado, tamanho exato do payload que causou o incidente) — o exemplo do "JSON de 50MB" e do "componente gigante" são ilustrativos, não um caso documentado com números.
- Fonte não distingue explicitamente Worker Threads de Cluster/Child Process (todos chamados genericamente de "worker threads") — `references/nodejs-core.md` da skill `lang-dynamic` detalha a diferença entre os três mecanismos e quando usar cada um; adicionada como qualificação em [[wiki/concepts/thread]].
- Fonte não menciona `--frozen`/streaming SSR (React 18 `renderToPipeableStream`) nem outras técnicas modernas de renderização incremental que mitigam parcialmente o problema sem sair da thread principal — fora do escopo da fonte, mas relevante como contraponto técnico a explorar em fonte futura.

## Citações

> "O event loop ele só funciona porque a maioria das coisas do servidor não faz uma computação pesada."

> "Iniciar uma operação de I/O ela é rápida, o problema é executar ela de fato."

> "Utilizar await... se a função ela faz um trabalho pesado de forma síncrona, await não vai rodar, não vai tirar nada da trade principal — ele só vai funcionar com operações de I/O."
