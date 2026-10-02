---
type: concept
title: "Comunicação Assíncrona"
aliases: ["asynchronous communication", "comunicação assincrona", "async communication"]
date_created: 2026-09-30
date_updated: 2026-10-02
source_count: 2
tags: [comunicacao-assincrona, mensageria, polling, webhook, acoplamento, resiliencia, consistencia-eventual, arquiteturas-distribuidas]
skill: tech-mentor-backend
status: draft
---

# Comunicação Assíncrona

O emissor envia uma mensagem (ou chama um serviço) e **não espera a resposta imediatamente**; o receptor processa em background e o resultado chega depois — por notificação ou por consulta periódica de status. Analogia do vídeo: áudio no grupo de WhatsApp.

## Síncrona vs. assíncrona

| | [[wiki/concepts/comunicacao-sincrona\|Síncrona]] | Assíncrona |
|---|---|---|
| Resposta | Imediata | Não imediata |
| Acoplamento | Forte (codependência) | Fraco (API lenta não derruba o resto) |
| Exemplo | REST entre microsserviços | Mensageria via broker (Kafka, RabbitMQ) |

O "acoplamento fraco" vale no eixo temporal ([[wiki/concepts/temporal-coupling]]); o contrato da mensagem continua acoplando produtor e consumidor [skill: tech-mentor-backend].

## Três formas de implementar

1. **Polling por ID de operação** — [[wiki/concepts/async-request-reply]].
2. **Webhook / callback** — [[wiki/concepts/webhook]].
3. **Mensageria** por broker de tópicos/eventos — [[wiki/concepts/mensageria]] ([[wiki/concepts/kafka]], [[wiki/entities/rabbitmq]]).

Polling e webhook são comuns quando não se controla todos os sistemas (ex.: API externa já em produção).

## Benefícios

- **Autonomia e escalabilidade:** no exemplo de pedidos, o evento "pedido criado" é consumido por Estoque e Faturamento sem que um dependa da resposta do outro; times pequenos trabalham num serviço só.
- **Tolerância a falhas:** serviço que cai relê as mensagens perdidas ao voltar ([[wiki/concepts/tolerancia-a-falha]]).
- **Picos de carga (Black Friday):** escala-se só o serviço sob pressão; a fila age como [[wiki/concepts/buffer]].

## Desafios

1. **Debug** sem fluxo linear → [[wiki/concepts/observabilidade]], [[wiki/concepts/distributed-tracing]].
2. **Garantia de entrega** → [[wiki/concepts/garantia-de-entrega]].
3. **Consistência eventual** → [[wiki/concepts/eventual-consistency]]; é preciso alinhar com liderança/cliente que os dados não estarão consistentes o tempo todo.
4. **Complexidade e capacitação** do time; não emular síncrono sobre assíncrono nem adotar "por usar".

## Base para

[[wiki/concepts/cqrs]], [[wiki/concepts/event-sourcing]], [[wiki/concepts/event-driven-architecture]], [[wiki/concepts/microsservicos]]. Ver também [[wiki/concepts/processamento-assincrono]] (workers + fila para tarefas pesadas).

## Key sources

- [[wiki/sources/comunicacao-assincrona-arquiteturas-distribuidas-bernardo-lobato]] — definição, formas, exemplo de pedidos e três desafios
- [[wiki/sources/arquitetura-distribuida-introducao-historico-desafios-bernardo-lobato]] — retomada no vídeo de abertura da série: escolha impacta escalabilidade, disponibilidade e complexidade
