---
type: concept
title: "Mensageria"
aliases: ["message broker", "queue", "stream", "eda", "event driven"]
date_created: 2026-04-23
date_updated: 2026-09-02
source_count: 9
tags: [mensageria, kafka, rabbitmq, sqs, queue, stream, eda, at-least-once, dlq]
skill: tech-mentor-backend
status: stub
---

# Mensageria

Comunicação assíncrona entre serviços via broker de mensagens. Resolve acoplamento síncrono, absorve picos de tráfego e isola falhas.

**A fila como [[wiki/concepts/buffer]]:** absorver picos é exatamente o papel de buffer — a fila desacopla a velocidade de produção da de consumo, permitindo que consumidores trabalhem em ritmo constante sem perder mensagens num pico (ex.: Black Friday). Ver [[wiki/concepts/cache-vs-buffer]] para por que isso é buffer (fluxo), não cache (reutilização).

**Queue vs Stream:**
- **Queue (fila):** cada mensagem consumida uma vez — workers competem. Para jobs únicos (email, pagamento). Ex: RabbitMQ, SQS.
- **Stream:** cada consumer lê com seu próprio offset — replay possível. Para eventos de negócio com múltiplos consumidores. Ex: Kafka, Kinesis.

**Os três grandes:**
- **Kafka:** throughput massivo, replay, durável — operação complexa.
- **SQS:** zero ops, gerenciado, HA automático — sem replay, FIFO limitado.
- **RabbitMQ:** roteamento flexível AMQP — mais infra para operar.

**DLQ (Dead Letter Queue):** obrigatória — mensagens que falham N vezes não ficam em retry infinito.

**Garantias:** at-least-once exige consumer idempotente. Exactly-once é raro e caro.

**Redis Pub/Sub como notificador leve:** não é fila nem stream — mensagens não persistem, sem replay, sem consumer groups. Se o assinante não estiver conectado no momento do `PUBLISH`, a mensagem se perde. Serve bem para notificar múltiplas instâncias de um serviço (ex: propagar evento para clientes [[wiki/concepts/server-sent-events|SSE]] conectados em pods diferentes), mas não substitui Kafka/SQS/RabbitMQ quando entrega garantida importa.

**BullMQ como implementação de queue em Node.js/Bun:** producer e worker são processos independentes que só se comunicam via Redis — nunca por chamada de função direta. Ver [[wiki/concepts/bullmq]] e [[wiki/concepts/filas-e-workers]].

**Ambulance Pattern — roteando tráfego prioritário sem starvation:** dar prioridade a mensagens marcando um campo de prioridade no header (baixo/médio/alto) parece a solução óbvia, mas causa starvation do fluxo normal — mensagens de alta prioridade sempre furam a fila e podem travar completamente o processamento normal, com risco de timeout em quem espera resposta síncrona. A alternativa recomendada é separar fisicamente o tráfego em duas filas (normal e alta prioridade), permitindo processamento paralelo real, opcionalmente com uma instância de serviço dedicada por fila. Ver [[wiki/concepts/ambulance-pattern]].

**Por que o Kafka não paraleliza sozinho ao subir mais consumers:** essa é a diferença estrutural mais confundida entre Kafka e filas tradicionais. Num consumer group Kafka, a próxima mensagem de uma partição só é entregue depois que o consumer atual comita o offset da anterior — enquanto isso, um segundo consumer do mesmo grupo fica ocioso, mesmo com trabalho disponível. RabbitMQ/SQS funcionam diferente: consumers adicionais competem livremente por mensagens da mesma fila, sem essa barreira de ordenação. Ver [[wiki/concepts/kafka]] para o mecanismo completo (partições, offset commit, rebalance).

## Key Sources

- [[sources/mensageria]]
- [[sources/design-pattern-observer]] — distinção Observer (in-process) vs Pub/Sub (broker distribuído)
- [[wiki/sources/server-sent-events-sse-tempo-real]] — Redis Pub/Sub como notificador entre microsserviços, sem persistência nem replay
- [[wiki/sources/updates-tempo-real-polling-sse-websocket]] — mitigação da perda de mensagem via tabela de pendentes, quando o assinante Redis Pub/Sub está offline
- [[wiki/sources/pub-sub-message-queue-bullmq-na-pratica]] — distinção prática Pub/Sub vs queue e quickstart de BullMQ sobre Redis
- [[wiki/sources/system-design-simulador-hotel-booking-replit]] — Kafka escolhido num exercício de hotel booking pelo critério "capacidade de lidar com grandes volumes de dados", com ressalva explícita de possível [[wiki/concepts/over-engineering]] para o caso de uso; a IA avaliadora do exercício aponta corretamente que Kafka foi introduzido no desenho sem nenhum consumidor definido — reforça que escolher a tecnologia certa não substitui desenhar quem consome a fila
- [[wiki/sources/vale-a-pena-estudar-microsservicos-mesmo-sem-usar]] — comunicação assíncrona (filas/eventos) citada como conceito que ensina quando desacoplar processos (e-mail, geração de relatório) do fluxo principal, mesmo fora de arquitetura distribuída
- [[wiki/sources/cache-vs-buffer-diferenca-conceitual]] — fila (Kafka/SQS/RabbitMQ/Redis Streams) apresentada como "grande buffer" que absorve picos e desacopla produtor de consumidor
- [[wiki/sources/system-design-copa-do-mundo-tempo-real-kafka-event-sourcing-renato-augusto]] — demonstração passo a passo de por que um segundo consumer Kafka fica ocioso sem partições adicionais; dois consumer groups independentes consumindo o mesmo tópico para propósitos distintos
- [[wiki/sources/ambulance-pattern-priorizacao-mensagens-mark-richards]] — por que prioridade embutida na mensagem causa starvation, e por que separar em duas filas físicas (opcionalmente com instância dedicada por fila) resolve sem esse efeito colateral
