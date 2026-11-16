---
type: concept
title: "Non-blocking I/O"
aliases: ["I/O não bloqueante", "non-blocking I/O", "IO assíncrono", "blocking vs non-blocking"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 2
tags: [nodejs, io, assincrono, event-loop, epoll, concorrencia, lang-dynamic]
skill: lang-dynamic
status: stub
---

# Non-blocking I/O

Modelo em que pedir uma operação de entrada e saída (rede, disco) **não** prende a thread que pediu: a chamada volta na hora, e o resultado chega depois por um evento ou [[wiki/concepts/callback-javascript|callback]]. Assim uma thread só atende milhares de conexões, desde que o trabalho seja I/O-bound.

## Como o Node faz

- **Rede:** sockets em modo não bloqueante, vigiados pelo mecanismo do sistema (epoll no Linux, kqueue no macOS/BSD, IOCP no Windows). O [[wiki/concepts/event-loop-performance-js|event loop]] espera eventos de todos de uma vez `[external]` https://docs.libuv.org/en/v1.x/design.html.
- **Disco e DNS:** não há API portável não bloqueante, então a [[wiki/entities/libuv]] simula com o [[wiki/concepts/thread-pool]].

## Bloqueante × não bloqueante (terminologia do Node)

A documentação chama de **bloqueante** a chamada síncrona que segura a thread do JavaScript (`readFileSync`, `execSync`, loop pesado, `JSON.parse` grande) e de **não bloqueante** a versão com callback ou promise `[external]` https://nodejs.org/en/learn/asynchronous-work/overview-of-blocking-vs-non-blocking. Uma API não bloqueante pode demorar muito: o que importa é se ela segura a call stack.

Non-blocking I/O não salva trabalho de CPU: ver [[wiki/sources/node-single-thread-ssr-bloqueio-event-loop]] e [[wiki/concepts/thread]] (worker threads).

## No JStack (aula 01)

Em [[wiki/sources/jstack-como-funciona-o-nodejs]], "non-blocking I/O" é "execução de código assíncrono": deixar uma query no banco enquanto processa outra coisa. Mas a aula chama `db.query` de "função bloqueante" no sentido de "demorada", o contrário do uso da documentação.

## Na NLW #2, dia 2 (Diego Fernandes)

Explicado como "salvar o usuário, enviar um e-mail e criptografar a senha tudo ao mesmo tempo". Vale para banco e e-mail (I/O); hash de senha é CPU e só não trava o loop se for assíncrono no thread pool. Ver [[wiki/sources/nlw-2-diego-fernandes-dia-2-api-rest-node-express-knex-proffy]].

## Key sources

- [[wiki/sources/jstack-como-funciona-o-nodejs]]: single thread × non-blocking I/O; termo "bloqueante" com sentido trocado
- [[wiki/sources/nlw-2-diego-fernandes-dia-2-api-rest-node-express-knex-proffy]]: NLW #2, Diego, dia 2: I/O × CPU no exemplo do cadastro
