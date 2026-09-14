---
type: concept
title: "Renderização SSR vs. CSR"
aliases: ["server-side rendering", "client-side rendering", "SSR", "CSR", "SSR vs CSR"]
date_created: 2026-09-14
date_updated: 2026-09-14
source_count: 1
tags: [frontend, ssr, csr, nodejs, event-loop, performance, nextjs]
skill: lang-dynamic
status: stable
---

# Renderização SSR vs. CSR

Duas formas de decidir **onde** o HTML de uma página é montado — e, por consequência, **quem paga o custo computacional** dessa montagem.

## Client-Side Rendering (CSR)

O navegador baixa JavaScript, HTML e CSS, e é o próprio navegador quem monta a página. O servidor só entrega arquivos estáticos e responde chamadas de API — ele não participa da renderização em si. Quem executa o trabalho de montar o DOM é o **cliente**.

## Server-Side Rendering (SSR)

O servidor roda o componente, monta o HTML completo e devolve a página já pronta para o navegador. É o modelo do Next.js, do Remix, e de server components. Aqui, quem paga o custo de CPU da renderização é o **servidor** — não o cliente.

## Por que essa escolha importa além de performance percebida

A escolha entre SSR e CSR não é só sobre First Contentful Paint ou SEO — ela decide **onde o custo de CPU da renderização recai**. Em Node.js, isso tem uma implicação estrutural: o runtime é [[wiki/concepts/thread|single thread]] no [[wiki/concepts/event-loop-performance-js|event loop]], e renderização SSR complexa é uma operação **CPU-bound** (ao lado de criptografia, compactação, parsing de payloads grandes), diferente da maioria do trabalho de servidor, que é **I/O-bound** (disco, rede, banco) e pode ser delegado sem travar a thread principal.

Uma renderização SSR pesada (componente gigante, transformação grande de dados antes de renderizar) segura a thread principal do Node.js inteira: nenhuma outra requisição é processada enquanto ela roda — nem mesmo callbacks de I/O que já retornaram. O efeito visível para o usuário é a página carregando e nunca renderizando (tela em branco), e o efeito agrava com mais tráfego simultâneo na mesma rota.

## Mitigações para o custo de CPU do SSR

- **Cache de renderização** — evitar regenerar o mesmo HTML para requisições repetidas da mesma página; ver [[wiki/concepts/cache]] e ISR (Incremental Static Regeneration) do Next.js como estratégia híbrida entre estático e dinâmico.
- **Streaming SSR / renderização incremental** — técnicas mais recentes (fora do escopo da fonte que originou esta página) que enviam HTML em pedaços conforme fica pronto, em vez de bloquear até o componente inteiro terminar.
- **Worker threads** — deslocar o trabalho CPU-bound da renderização para uma thread separada quando o volume justificar; ver [[wiki/concepts/thread]].
- **Filas** — em casos extremos (ex. geração de relatório/PDF via SSR sob demanda), tirar o trabalho pesado do caminho síncrono da requisição; ver [[wiki/concepts/filas-e-workers]].

## Depois do SSR: hydration

No CSR puro não há esse passo; no SSR, depois que o HTML chega pronto, o JavaScript do cliente ainda precisa "acordar" a página para torná-la interativa — ver [[wiki/concepts/hydration]].

## Ver também

- [[wiki/concepts/event-loop-performance-js]] — por que operações síncronas pesadas bloqueiam tudo em Node.js
- [[wiki/concepts/thread]] — worker threads como via de escape para trabalho CPU-bound
- [[wiki/concepts/cache]] — como evitar recomputar o mesmo HTML repetidamente
- [[wiki/concepts/hydration]] — o que acontece depois que o HTML do SSR chega ao navegador

## Key Sources

- [[wiki/sources/node-single-thread-ssr-bloqueio-event-loop]]
