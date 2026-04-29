---
date: 2026-04-16
tags: [tech-mentor, backend, mensageria, background-jobs, bullmq, skip-locked, queues]
skill: tech-mentor-backend/references/mensageria
level: intermediário
---

# Background Jobs — BullMQ, SKIP LOCKED e Estratégias de Queue

## Contexto

Background jobs processam trabalho fora do ciclo request-response: envio de email, geração de relatório, processamento de imagem, sincronização com APIs externas. A escolha da implementação afeta diretamente confiabilidade (perda de jobs?), escalabilidade (múltiplos workers?) e operacionalidade (onde ver jobs falhando?).

Três abordagens principais:
- **BullMQ** (Node.js): Redis como backend, rico em features, ideal para TypeScript
- **SKIP LOCKED** (PostgreSQL): jobs direto no banco, sem Redis, transacional por natureza
- **Celery** (Python): equivalente ao BullMQ para Python, suporta Redis e RabbitMQ

---

## BullMQ — Redis-backed Jobs para Node.js

### Setup e Tipos

```typescript
import { Queue, Worker, Job, QueueEvents } from "bullmq";
import { Redis } from "ioredis";

const connection = new Redis(process.env.REDIS_URL!, {
  maxRetriesPerRequest: null  // requerido pelo BullMQ
});

// Definição de tipos de jobs
type EmailJobData = {
  to: string;
  subject: string;
  templateId: string;
  variables: Record<string, string>;
};

type ReportJobData = {
  userId: string;
  startDate: string;
  endDate: string;
  format: "pdf" | "csv";
};

// Criar filas
const emailQueue = new Queue<EmailJobData>("emails", { connection });
const reportQueue = new Queue<ReportJobData>("reports", { connection });
```

### Publicando Jobs

```typescript
// Job simples
await emailQueue.add("welcome-email", {
  to: user.email,
  subject: "Bem-vindo!",
  templateId: "welcome",
  variables: { name: user.name }
});

// Job com delay (enviar após 1 hora)
await emailQueue.add("follow-up", jobData, {
  delay: 60 * 60 * 1000  // ms
});

// Job recorrente (cron)
await reportQueue.add("daily-report", jobData, {
  repeat: { cron: "0 8 * * *" }  // todo dia às 8h
});

// Job com prioridade (menor número = maior prioridade)
await emailQueue.add("password-reset", jobData, {
  priority: 1  // urgente — processa antes dos outros
});

// Job com deduplicação (evita duplicatas)
await emailQueue.add("weekly-digest", jobData, {
  jobId: `digest-${userId}-${weekNumber}`,  // ID único → ignora se já existe
  removeOnComplete: true
});
```

### Worker — Processamento

```typescript
const emailWorker = new Worker<EmailJobData>(
  "emails",
  async (job: Job<EmailJobData>) => {
    const { to, subject, templateId, variables } = job.data;

    // Atualizar progresso (visível no BullMQ dashboard)
    await job.updateProgress(10);

    const html = await renderTemplate(templateId, variables);
    await job.updateProgress(50);

    await resend.emails.send({ from: "noreply@empresa.com", to, subject, html });
    await job.updateProgress(100);

    return { sentAt: new Date().toISOString() };
  },
  {
    connection,
    concurrency: 5,  // até 5 jobs em paralelo neste worker
    limiter: {
      max: 100,       // no máximo 100 jobs
      duration: 60000 // por minuto (rate limiting)
    }
  }
);

// Tratamento de erros e retry
emailWorker.on("failed", (job, error) => {
  console.log({ message: "Job failed", jobId: job?.id, error: error.message, attempts: job?.attemptsMade });
});

emailWorker.on("completed", (job, result) => {
  console.log({ message: "Job completed", jobId: job.id, result });
});
```

### Retry e Dead Letter

```typescript
// Configurar retry na fila (aplica a todos os jobs por padrão)
const emailQueue = new Queue<EmailJobData>("emails", {
  connection,
  defaultJobOptions: {
    attempts: 3,
    backoff: {
      type: "exponential",
      delay: 2000  // 2s, 4s, 8s
    },
    removeOnComplete: { count: 100 },  // manter últimos 100 completados
    removeOnFail: false  // manter falhos para inspeção
  }
});

// Jobs falhos ficam em estado "failed" — visíveis no dashboard
// Para reprocessar manualmente:
const failedJobs = await emailQueue.getFailed();
for (const job of failedJobs) {
  await job.retry();
}
```

### BullMQ Board — Observabilidade

```typescript
import { createBullBoard } from "@bull-board/api";
import { BullMQAdapter } from "@bull-board/api/bullMQAdapter";
import { ExpressAdapter } from "@bull-board/express";
import express from "express";

const serverAdapter = new ExpressAdapter();
serverAdapter.setBasePath("/admin/queues");

createBullBoard({
  queues: [
    new BullMQAdapter(emailQueue),
    new BullMQAdapter(reportQueue)
  ],
  serverAdapter
});

const app = express();
app.use("/admin/queues", serverAdapter.getRouter());
```

---

## SKIP LOCKED — Job Queue no PostgreSQL

Para sistemas que já têm PostgreSQL e querem evitar a complexidade operacional do Redis:

```sql
-- Tabela de jobs
CREATE TABLE jobs (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  queue VARCHAR(100) NOT NULL,
  payload JSONB NOT NULL,
  status VARCHAR(20) NOT NULL DEFAULT 'pending',  -- pending, processing, done, failed
  attempts INT NOT NULL DEFAULT 0,
  max_attempts INT NOT NULL DEFAULT 3,
  scheduled_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  locked_until TIMESTAMPTZ,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  error TEXT
);

CREATE INDEX idx_jobs_queue_status_scheduled ON jobs (queue, status, scheduled_at)
  WHERE status = 'pending';
```

```typescript
// Worker com SKIP LOCKED — múltiplos workers sem conflito
async function processNextJob(queue: string): Promise<boolean> {
  return prisma.$transaction(async tx => {
    // SKIP LOCKED: pula rows bloqueadas por outros workers → sem espera, sem deadlock
    const job = await tx.$queryRaw<JobRow[]>`
      SELECT id, payload, attempts
      FROM jobs
      WHERE queue = ${queue}
        AND status = 'pending'
        AND scheduled_at <= NOW()
      ORDER BY scheduled_at ASC
      LIMIT 1
      FOR UPDATE SKIP LOCKED
    `;

    if (job.length === 0) return false;

    const { id, payload, attempts } = job[0];

    // Marcar como processing e definir lock timeout
    await tx.$executeRaw`
      UPDATE jobs
      SET status = 'processing',
          locked_until = NOW() + INTERVAL '5 minutes',
          attempts = attempts + 1
      WHERE id = ${id}
    `;

    try {
      await executeJob(payload);

      await tx.$executeRaw`
        UPDATE jobs SET status = 'done' WHERE id = ${id}
      `;
    } catch (error) {
      const failed = attempts + 1 >= 3;
      await tx.$executeRaw`
        UPDATE jobs
        SET status = ${failed ? "failed" : "pending"},
            error = ${(error as Error).message},
            scheduled_at = NOW() + INTERVAL '${failed ? 0 : (attempts + 1) * 30} seconds'
        WHERE id = ${id}
      `;
    }

    return true;
  });
}

// Poll loop
async function startWorker(queue: string) {
  while (true) {
    const processed = await processNextJob(queue);
    if (!processed) {
      await new Promise(resolve => setTimeout(resolve, 1000)); // sleep 1s se fila vazia
    }
  }
}
```

### Vantagens e Desvantagens de SKIP LOCKED

| Aspecto | SKIP LOCKED (PostgreSQL) | BullMQ (Redis) |
|---|---|---|
| **Infraestrutura** | Já tem o banco | Requer Redis |
| **Transacional** | Sim — job + operação numa transação | Não — separados |
| **Performance** | Bom até ~1000 jobs/min | Excelente, 10k+ jobs/min |
| **Observabilidade** | SQL queries + sua ferramenta | Bull Board, UI nativa |
| **Cron/delay** | Manual | Nativo |
| **Maturidade** | Padrão robusto | Muito maduro |

**Usar SKIP LOCKED quando:** transacionalidade importa (job deve ser criado junto à operação de negócio) e volume é moderado.

**Usar BullMQ quando:** volume alto, precisa de UI de observabilidade, delay/cron, rate limiting por job type.

---

## Padrões Comuns

### Fan-out: Um Job → Múltiplos Jobs Filhos

```typescript
// Job pai que gera filhos
const reportWorker = new Worker<ReportJobData>("reports", async job => {
  const users = await getUsersForReport(job.data);

  // Criar job filho para cada usuário
  const childrenJobs = users.map(user => ({
    name: "user-report",
    data: { userId: user.id, ...job.data },
    opts: { attempts: 3 }
  }));

  // Flow — parent completa quando todos os filhos completam
  await emailQueue.addBulk(childrenJobs);
});
```

### Idempotência em Jobs

```typescript
// Usar jobId determinístico para deduplicação
async function scheduleWelcomeEmail(userId: string) {
  await emailQueue.add(
    "welcome-email",
    { userId },
    {
      jobId: `welcome-${userId}`,  // se chamar duas vezes → mesmo job, não duplica
      attempts: 3
    }
  );
}
```

## Conceitos Relacionados

[[kafka]] · [[rabbitmq]] · [[temporal]] · [[idempotencia]] · [[dlq-event-patterns]] · [[outbox-pattern]]

---
*Fonte: tech-mentor skill · tech-mentor-backend · 2026-04-16*
