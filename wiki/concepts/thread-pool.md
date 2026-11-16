---
type: concept
title: "Thread pool"
aliases: ["thread pool", "worker pool", "pool de threads", "UV_THREADPOOL_SIZE"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 2
tags: [nodejs, libuv, thread, concorrencia, assincrono, lang-dynamic]
skill: lang-dynamic
status: stub
---

# Thread pool

Conjunto fixo de [[wiki/concepts/thread|threads]] criadas de antemão que pegam tarefas de uma fila, executam e devolvem o resultado. Evita criar uma thread por tarefa.

## No Node.js (libuv)

A [[wiki/entities/libuv]] mantém um pool global, com 4 threads por padrão (`UV_THREADPOOL_SIZE` muda o número). Ele recebe o que não tem API assíncrona no sistema operacional `[external]` https://docs.libuv.org/en/v1.x/design.html:
- file system (`fs.readFile`, `fs.stat`...);
- DNS via `getaddrinfo`/`getnameinfo` (`dns.lookup`, que o `http` usa para resolver nomes);
- no Node, também `crypto` assíncrono (`pbkdf2`, `scrypt`, `randomBytes`) e `zlib` `[external]` https://nodejs.org/en/learn/asynchronous-work/dont-block-the-event-loop.

**I/O de rede não usa o pool.** Sockets TCP/UDP (HTTP, drivers de banco) ficam na thread do [[wiki/concepts/event-loop-performance-js|event loop]], não bloqueantes, sobre epoll/kqueue/IOCP. Ver [[wiki/concepts/non-blocking-io]].

**Gargalo:** com 4 threads, cinco `pbkdf2` simultâneos fazem o quinto esperar, e um `fs.readFile` também fica na fila. Sintoma comum: DNS lento travando requisições HTTP em servidores com muito `crypto`.

## No JStack (aula 01)

Em [[wiki/sources/jstack-como-funciona-o-nodejs]], [[wiki/entities/mateus-silva]] apresenta o thread pool como para onde o Node "joga" a `db.query` enquanto o código segue. O papel geral está certo, mas o exemplo não: uma query de banco é I/O de rede e não passa pelo pool. `fs.readFile` seria o exemplo correto.

## Na NLW #2, dia 2 (Diego Fernandes)

O exemplo de "criptografar a senha [...] ao mesmo tempo" só não bloqueia porque o `bcrypt` assíncrono roda no pool da libuv; não é efeito do non-blocking I/O. Ver [[wiki/sources/nlw-2-diego-fernandes-dia-2-api-rest-node-express-knex-proffy]].

## Key sources

- [[wiki/sources/jstack-como-funciona-o-nodejs]]: thread pool da libuv no fluxo de um `db.query` (com correção)
- [[wiki/sources/nlw-2-diego-fernandes-dia-2-api-rest-node-express-knex-proffy]]: NLW #2, Diego, dia 2: hash de senha no pool
