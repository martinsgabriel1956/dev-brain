---
type: concept
title: "Filas e Workers"
aliases: ["job queue", "background processing", "async workers", "processamento assíncrono"]
date_created: 2026-07-09
date_updated: 2026-08-24
source_count: 7
tags: [filas, workers, background-jobs, mensageria, backend, retry, idempotencia]
skill: tech-mentor-backend
status: stub
---

# Filas e Workers

Nem todo trabalho precisa acontecer enquanto o usuário espera. No checkout, o sistema precisa responder rápido — mas enviar e-mail, gerar nota fiscal, etc. são jobs que não precisam travar a resposta principal.

Uma fila desacopla o pedido do processamento pesado: a API coloca uma mensagem na fila, um **worker** consome essa mensagem depois. Se o volume de jobs cresce, a fila acumula; se é preciso processar mais rápido, sobem-se mais workers.

> Nota: esta página trata do padrão arquitetural de processamento assíncrono. Para a estrutura de dados FIFO subjacente, ver [[wiki/concepts/fila]].

## Riscos que a fila introduz

| Risco | Pergunta a responder |
|---|---|
| Job falha | Existe retry? Com que backoff? |
| Job processa duas vezes | A operação é idempotente? |
| Fila cresce mais rápido que o consumo | Autoscaling de workers? Backpressure? |
| Ordem importa | A fila garante ordem de entrega ou apenas at-least-once? |

## Distinção de Pub/Sub: quem depende de quem

Fila e worker não são o mesmo modelo mental de [[wiki/concepts/pub-sub|Pub/Sub]]. Numa message queue, o serviço que enfileira o job **depende** de alguém executá-lo (ex.: comprimir uma imagem) — é uma inversão de dependência em relação ao Pub/Sub, onde o publicador não depende de ninguém estar ouvindo. Também por isso múltiplos workers numa mesma fila devem **competir** pelos jobs (cada job processado uma única vez), nunca duplicar o processamento — diferente do fan-out de Pub/Sub, onde cada assinante recebe sua própria cópia do evento.

## Exemplo mínimo com BullMQ

Producer e worker como dois processos independentes (ex.: Bun), comunicando-se apenas via Redis — nunca por chamada de função direta. Parar o producer não trava o worker (ele drena a fila); parar o worker não perde jobs (retoma de onde parou ao reconectar). Ver [[wiki/concepts/bullmq]] para a anatomia da lib.

## Relação com outros conceitos

- [[wiki/concepts/fila]] — a estrutura de dados FIFO que fundamenta o padrão
- [[wiki/concepts/escalabilidade-horizontal]] — workers escalam horizontalmente de forma independente da API
- [[wiki/concepts/stateless]] — jobs em andamento não podem depender de estado local do worker, sob risco de perda se a instância cair
- [[wiki/concepts/pub-sub]] — modelo mental oposto: publica um trabalho a ser feito, não um fato
- [[wiki/concepts/bullmq]] — implementação concreta em Node.js/Bun sobre Redis
- Ver detalhamento de BullMQ, SKIP LOCKED, DLQ e fan-out em [[wiki/sources/background-jobs]] e `references/background-jobs.md` (tech-mentor-backend)

## Key sources

- [[wiki/sources/10-conceitos-fundamentais-backend]]
- [[wiki/sources/pub-sub-message-queue-bullmq-na-pratica]]
- [[wiki/sources/system-design-por-nivel-junior-pleno-senior]] — workers aparecem como conhecimento esperado a partir de pleno; em nível sênior, o uso de background jobs/workers para aliviar carga do sistema é tratado como ferramenta central de escala
- [[wiki/sources/escalar-para-um-milhao-de-usuarios]] — computações pesadas (processar vídeo/imagem, gerar PDF) publicadas como jobs numa fila; worker (thread em outra máquina, lambda) puxa e processa, aliviando os servidores web para responderem rápido. A fonte chama isso de "publisher/subscriber" — na prática, uma job queue / competing consumers
- [[wiki/sources/cache-vs-buffer-diferenca-conceitual]] — a fila entre produtor e consumidor como [[wiki/concepts/buffer]] que absorve picos (ex.: Black Friday) e permite processamento em ritmo constante
- [[wiki/sources/back-pressure-producer-consumer-filas-bounded-admission-control]] — o que fazer quando o worker não acompanha o ritmo do produtor: identificar o gargalo, podar stale jobs, processar em batches, e controlar a admissão de novos jobs (ver [[wiki/concepts/admission-control]])
- [[wiki/sources/escalando-aplicacao-zero-a-um-milhao-usuarios-renato-augusto]] — mesmo padrão (job pesado → mensagem na fila → resposta imediata → worker processa em background), com nomes concretos de ferramentas (RabbitMQ, Kafka, AWS SQS) e a analogia de checkout de e-commerce: "pagar" não trava a tela até o gateway confirmar, exatamente como o padrão de resposta imediata + confirmação assíncrona
