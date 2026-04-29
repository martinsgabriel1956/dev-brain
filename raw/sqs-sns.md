---
date: 2026-04-17
tags: [tech-mentor, mensageria, aws, sqs, sns, cloud]
skill: tech-mentor-backend/references/messaging
level: intermediário
---

# SQS e SNS (AWS)

## Contexto
**SQS** (Simple Queue Service) e **SNS** (Simple Notification Service) são os serviços gerenciados de mensageria da AWS. Enquanto Kafka e RabbitMQ requerem operação própria, SQS/SNS são totalmente serverless — sem cluster para gerenciar, billing por mensagem.

Juntos formam o padrão **Fanout**: SNS distribui para múltiplas filas SQS. Cada consumidor processa de forma independente.

## SQS — Tipos de Fila

| Aspecto | Standard Queue | FIFO Queue |
|---|---|---|
| Ordering | Best-effort (pode desordenar) | Garantido (First-In-First-Out) |
| Throughput | Praticamente ilimitado | 300 msg/s (3000 com batching) |
| Deduplicação | Não | Sim — por `MessageDeduplicationId` |
| Custo | Mais barato | ~10% mais caro |
| Uso | Jobs independentes, notificações | Pedidos financeiros, comandos sequenciais |

## Conceitos-Chave do SQS

**Visibility Timeout:** quando um consumer pega uma mensagem, ela fica invisível para outros consumers por N segundos. Se o consumer não a deletar nesse período (crash, timeout), ela fica visível novamente.

```typescript
import { SQSClient, ReceiveMessageCommand, DeleteMessageCommand, ChangeMessageVisibilityCommand } from "@aws-sdk/client-sqs";

const sqs = new SQSClient({ region: "us-east-1" });

async function processMessages() {
  const { Messages } = await sqs.send(new ReceiveMessageCommand({
    QueueUrl: process.env.QUEUE_URL,
    MaxNumberOfMessages: 10,
    WaitTimeSeconds: 20,         // Long polling — reduz custo e latência
    VisibilityTimeout: 60        // 60s para processar
  }));

  for (const message of Messages ?? []) {
    try {
      const body = JSON.parse(message.Body!);

      // Se o processamento for demorar mais que 60s, extender o timeout
      if (shouldExtendTimeout(body)) {
        await sqs.send(new ChangeMessageVisibilityCommand({
          QueueUrl: process.env.QUEUE_URL!,
          ReceiptHandle: message.ReceiptHandle!,
          VisibilityTimeout: 120
        }));
      }

      await processJob(body);

      // Deletar somente após processar com sucesso
      await sqs.send(new DeleteMessageCommand({
        QueueUrl: process.env.QUEUE_URL!,
        ReceiptHandle: message.ReceiptHandle!
      }));
    } catch (err) {
      // Não deletar — mensagem volta após visibility timeout
      // Após maxReceiveCount tentativas → vai para DLQ
      console.log({ message: "Processing failed, will retry", error: err });
    }
  }
}
```

**Dead Letter Queue (DLQ):** após `maxReceiveCount` falhas, a mensagem vai para a DLQ. Configure sempre.

```json
{
  "deadLetterTargetArn": "arn:aws:sqs:us-east-1:123456789:MyQueue-DLQ",
  "maxReceiveCount": 3
}
```

## SNS — Fanout Pattern

SNS distribui uma publicação para múltiplos subscribers (SQS, Lambda, HTTP, email, SMS).

```typescript
import { SNSClient, PublishCommand } from "@aws-sdk/client-sns";

const sns = new SNSClient({ region: "us-east-1" });

// Publisher publica no tópico SNS — não sabe quem vai consumir
await sns.send(new PublishCommand({
  TopicArn: process.env.ORDER_CREATED_TOPIC_ARN,
  Message: JSON.stringify({ orderId: "123", customerId: "456", total: 99.90 }),
  MessageAttributes: {
    eventType: { DataType: "String", StringValue: "order.created" }
  }
}));
```

```
SNS Topic: order-created
    │
    ├──► SQS: email-notifications    → envia email de confirmação
    ├──► SQS: inventory-updates      → atualiza estoque
    ├──► SQS: analytics-pipeline     → registra para analytics
    └──► Lambda: fraud-check         → verificação síncrona de fraude
```

**SNS Filter Policies:** cada subscriber pode filtrar quais mensagens recebe, por atributo.

```json
{
  "eventType": ["order.created", "order.updated"]
}
```

## SQS FIFO — Exactly-Once com Deduplicação

```typescript
await sqs.send(new SendMessageCommand({
  QueueUrl: "https://sqs.us-east-1.amazonaws.com/123/orders.fifo",
  MessageBody: JSON.stringify(order),
  MessageGroupId: order.customerId,          // ordering por grupo
  MessageDeduplicationId: `order-${order.id}-${order.version}` // exactly-once
}));
```

## Comparativo SQS vs. Kafka vs. RabbitMQ

| Aspecto | SQS | Kafka | RabbitMQ |
|---|---|---|---|
| Operação | Zero | Alto | Médio |
| Replay | Não (mensagem é deletada) | Sim (retention configurável) | Não (por default) |
| Throughput | Alto (Standard) / Limitado (FIFO) | Muito alto | Médio |
| Ordering | Melhor esforço / FIFO por grupo | Por partição | Por fila |
| Custo | Pay-per-message | Infraestrutura fixa | Infraestrutura fixa |
| Casos de uso | Cloud-native AWS, serverless | Event log, streaming | Routing complexo |

## Quando Usar / Quando Evitar

**Usar quando:**
- Stack AWS e sem time de infra para operar Kafka/RabbitMQ
- Workloads serverless (Lambda como consumer)
- Fanout simples sem necessidade de replay

**Evitar quando:**
- Precisa de replay de eventos históricos → Kafka
- Consome eventos de fora da AWS (Kafka é cloud-agnostic)
- Volume altíssimo onde custo por mensagem supera o custo de operar Kafka

## Conceitos Relacionados
[[kafka]] · [[rabbitmq]] · [[nats-jetstream]] · [[dlq-event-patterns]] · [[background-jobs]]

---
*Fonte: tech-mentor skill · tech-mentor-backend · 2026-04-17*
