---
type: source
title: "Pub/Sub, Message Queue e BullMQ na Prática"
aliases: ["pub sub vs message queue", "BullMQ quickstart", "diferença pub sub e fila"]
date_created: 2026-07-09
date_updated: 2026-07-09
source_count: 0
tags: [tech-mentor-backend, pub-sub, mensageria, message-queue, bullmq, redis, workers, background-jobs]
skill: tech-mentor-backend
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/pub-sub-message-queue-bullmq-na-pratica.md
source_url:
author: desconhecido (canal de vídeo)
date_published:
date_ingested: 2026-07-09
---

# Pub/Sub, Message Queue e BullMQ na Prática

## TL;DR

Transcrição de vídeo que separa dois conceitos frequentemente confundidos — Pub/Sub e message queue — pelo modelo mental de dependência (quem depende de quem) e mostra, na prática, um producer/worker mínimo com BullMQ + Redis rodando localmente via Docker.

## Key Claims

1. **Pub/Sub publica um fato; message queue publica um trabalho a ser feito.** No Pub/Sub, "pagamento foi feito com sucesso" é publicado sem se importar se alguém está ouvindo — é um evento, não um comando. Na queue, o job (ex.: `compress_image`) existe para ser pego e executado por exatamente um worker.
2. **A distinção central é uma inversão de dependência.** Numa message queue, quem depende é o publisher — o serviço principal precisa que o job seja executado (ex.: comprimir a imagem). No Pub/Sub, quem depende é o subscriber — o sistema de pagamentos não liga se o sistema de estoque está ouvindo ou não; quem depende da mensagem é o estoque.
3. **Múltiplos workers numa queue devem competir, não duplicar.** 20, 50, 1000 workers podem ouvir a mesma fila, mas a ideia é que um job seja processado uma única vez — nunca a mesma imagem comprimida em paralelo por workers diferentes. Isso contrasta com Pub/Sub, onde cada subscriber recebe sua própria cópia do evento (fan-out).
4. **Pub/Sub e message queue são frequentemente combinados no mesmo fluxo.** Exemplo: pagamento bem-sucedido dispara um evento Pub/Sub que o serviço de e-mail ouve; o serviço de e-mail então enfileira o envio numa message queue, que garante entrega at-least-once (ou exactly-once) via um worker dedicado.
5. **Garantias de entrega variam por modelo (at-least-once, at-most-once, exactly-once)** e a escolha depende de como o sistema é desenhado — não é uma propriedade fixa do Pub/Sub nem da queue.
6. **Em produção, os três componentes (producer, broker, worker) costumam viver em infraestruturas separadas** (servidor/VPS, um broker gerenciado como AWS SQS, e workers em lambdas ou outras VPS) — mas para fins didáticos, os três rodam na mesma máquina.
7. **Demonstração prática com BullMQ**: producer e worker são dois processos Bun independentes que só se comunicam através de uma fila Redis (via Docker) — nunca por chamada de função direta. O producer usa `setInterval` para enfileirar um job por segundo; o worker consome a cada 500ms e loga o processamento. Parar o producer não trava o worker (ele drena a fila e espera); parar o worker não perde jobs (ele retoma de onde parou ao reconectar).

## Entidades Mencionadas

- **BullMQ** — biblioteca de filas para Node.js/Bun construída sobre Redis.
- **Redis** — broker/armazenamento subjacente ao BullMQ, rodando via Docker no exemplo.
- **AWS SQS (Simple Queue Service)** — citado como exemplo de message queue gerenciada em produção real.
- **Bun** — runtime usado para rodar producer e worker como processos separados.

## Conceitos Tocados

- [[wiki/concepts/pub-sub]]
- [[wiki/concepts/mensageria]]
- [[wiki/concepts/filas-e-workers]]
- [[wiki/concepts/fila]]
- [[wiki/concepts/bullmq]]
- [[wiki/concepts/escalabilidade-horizontal]]

## Open Questions

- Fonte não cita autor, canal ou referências formais — didática mas sem rigor acadêmico, mesmo padrão observado em outras fontes deste wiki (ex.: [[wiki/sources/10-conceitos-fundamentais-backend]]).
- O vídeo não aprofunda idempotência, retry/backoff nem DLQ no exemplo de código — aponta apenas o comportamento observado (worker retoma de onde parou). Detalhamento técnico desses tópicos já está coberto em [[wiki/concepts/filas-e-workers]] via `references/background-jobs.md` (tech-mentor-backend).
