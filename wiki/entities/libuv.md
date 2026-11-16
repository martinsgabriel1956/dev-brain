---
type: entity
title: "libuv"
aliases: ["libUV", "LibUV"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 2
tags: [nodejs, c, event-loop, thread-pool, io, biblioteca]
skill: lang-dynamic
status: stub
---

# libuv

Biblioteca em C, multiplataforma, de I/O assíncrono. Feita para o [[wiki/entities/nodejs|Node.js]] (substituiu libev/libeio por volta de 2011, com o porte para Windows), hoje usada por outros projetos também `[external]` https://docs.libuv.org/en/v1.x/design.html.

Fornece:
- o [[wiki/concepts/event-loop-performance-js|event loop]], com fases (timers, pending, poll, check, close);
- I/O de rede não bloqueante sobre epoll, kqueue, event ports e IOCP ([[wiki/concepts/non-blocking-io]]);
- o [[wiki/concepts/thread-pool]] para file system, DNS e trabalho do usuário;
- timers, processos filhos, sinais, pipes.

## No JStack (aula 01)

Em [[wiki/sources/jstack-como-funciona-o-nodejs]]: "uma biblioteca escrita em C chamada libuv" que implementa o thread pool e o event loop e "também [...] toda a parte de file system do Node, de DNS". O slide usa o logo do dinossauro com chifre de unicórnio.

## Key sources

- [[wiki/sources/jstack-como-funciona-o-nodejs]]: libuv como base do assíncrono no Node
- [[wiki/sources/jstack-criando-o-servidor-http]]: o handle do `listen` mantém o loop (e o processo) vivo
