---
date: 2026-04-13
tags: [tech-mentor, arquitetura, principios, twelve-factor, cloud-native]
skill: tech-mentor-infra/references/cloud-native
level: fundamento
---

# Twelve-Factor App

## Contexto

Metodologia criada pelo Heroku (Adam Wiggins, 2011) para construir aplicações SaaS que sejam portáveis, escaláveis e operacionalmente sadias. Cada fator é uma prática que endereça um problema específico de aplicações em cloud.

Não é um framework — é um contrato de boas práticas. Aplicações cloud-native modernas (Kubernetes, serverless, PaaS) pressupõem que você segue esses fatores.

## Os 12 Fatores

### I. Codebase — Uma base de código, múltiplos deploys

```
✅ Um repositório → múltiplos ambientes (dev, staging, prod)
❌ Repositório por ambiente ("código de prod", "código de staging")
❌ Um repo com múltiplas apps (monorepo com projetos não relacionados)
```

### II. Dependencies — Declare e isole dependências

```typescript
// ✅ package.json declara tudo explicitamente
{
  "dependencies": { "express": "^4.18.0" },
  "devDependencies": { "vitest": "^1.0.0" }
}

// ❌ npm install -g some-tool  (depende do ambiente)
// ❌ assume que curl/jq estão instalados no servidor
```

### III. Config — Configuração em variáveis de ambiente

Tudo que varia entre ambientes (dev, staging, prod) deve estar em env vars, nunca hardcoded:

```typescript
// ✅ Zod para validar env vars no startup
import { z } from "zod";

const envSchema = z.object({
  DATABASE_URL: z.string().url(),
  REDIS_URL: z.string().url(),
  STRIPE_SECRET_KEY: z.string().min(1),
  PORT: z.coerce.number().default(3000),
  NODE_ENV: z.enum(["development", "test", "production"])
});

export const env = envSchema.parse(process.env);

// ❌ config.ts com valores hardcoded por ambiente
const config = {
  db: process.env.NODE_ENV === "production"
    ? "postgres://prod-server/app"
    : "postgres://localhost/app"
};
```

### IV. Backing Services — Serviços de apoio como recursos anexáveis

Banco de dados, fila, cache, e-mail: todos são **recursos externos** acessados via URL. Trocar de banco local por RDS = trocar a env var `DATABASE_URL`, sem mudar código.

```typescript
// ✅ Acessa backing services via configuração
const db = new Pool({ connectionString: env.DATABASE_URL });
const redis = new Redis(env.REDIS_URL);
const emailClient = new Resend(env.RESEND_API_KEY);
```

### V. Build, Release, Run — Separar estágios rigorosamente

```
Build:   código-fonte → artefato (Docker image, bundle)
Release: artefato + config → release (artefato + env vars)
Run:     executa o release no ambiente de destino

❌ "vou dar um ssh no servidor e editar o arquivo"
❌ build diferente para prod e dev
```

### VI. Processes — Execute como processos stateless

```typescript
// ✅ Estado compartilhado vai para backing service
app.post("/session", async (req, res) => {
  const sessionId = randomUUID();
  await redis.setex(`session:${sessionId}`, 3600, JSON.stringify(req.body.user));
  res.json({ sessionId });
});

// ❌ Estado em memória — quebra com múltiplas instâncias
const sessions = new Map<string, User>();  // não sobrevive restart, não compartilha entre pods
```

### VII. Port Binding — Exporte serviços via binding de porta

A aplicação é auto-contida e escuta em uma porta:

```typescript
// ✅ App escuta na porta configurada
const port = env.PORT;
app.listen(port, () => {
  console.log({ message: "Server started", port });
});

// ❌ depende de Apache/Nginx para funcionar (coupling com webserver)
```

### VIII. Concurrency — Escale via model de processos

Escale horizontalmente adicionando processos/containers, não verticalmente com threads:

```
Web process:    3 instâncias (tráfego HTTP)
Worker process: 5 instâncias (processamento de jobs)
Scheduler:      1 instância (cron jobs)
```

No Kubernetes: múltiplos Pods, não um Pod com muito CPU.

### IX. Disposability — Maximize robustez com startup rápido e shutdown gracioso

```typescript
// ✅ Graceful shutdown — finaliza conexões antes de sair
process.on("SIGTERM", async () => {
  console.log({ message: "SIGTERM received, shutting down gracefully" });
  server.close(async () => {
    await db.end();
    await redis.quit();
    process.exit(0);
  });
});
```

Startup deve ser rápido (< 5s) — Kubernetes mata pods lentos para escalar.

### X. Dev/Prod Parity — Mantenha dev, staging e prod o mais similares possível

```yaml
# ✅ Docker Compose para dev replica o ambiente de produção
services:
  app:
    image: node:20-alpine
  postgres:
    image: postgres:16  # mesma versão da prod
  redis:
    image: redis:7      # mesma versão da prod

# ❌ SQLite em dev, PostgreSQL em prod — comportamentos diferentes
```

### XI. Logs — Trate logs como streams de eventos

```typescript
// ✅ Log para stdout — agregador (CloudWatch, Datadog) coleta
console.log({ message: "Order placed", orderId, userId, total });

// ❌ Escrever em arquivo, gerenciar rotação de log dentro da app
import fs from "fs";
fs.appendFileSync("/var/log/app.log", message);
```

### XII. Admin Processes — Execute tarefas administrativas como processos únicos

```bash
# ✅ Migrations rodam como processo separado, mesmo ambiente
docker run --rm app npm run migrate

# ❌ Endpoint HTTP para rodar migration
# ❌ SSH no servidor para rodar script manual
```

## Trade-offs

| Fator | Benefício concreto | Custo |
|---|---|---|
| III (Config) | Mesmo artefato em todos os ambientes | Gestão de secrets (Vault, AWS Secrets Manager) |
| VI (Stateless) | Escala horizontal trivial | Redis ou DB para qualquer estado compartilhado |
| IX (Disposability) | Zero-downtime deploy | Graceful shutdown adiciona complexidade |
| X (Dev/Prod Parity) | Menos surpresas em deploy | Docker Compose mais pesado em dev |

## Conceitos Relacionados

[[clean-architecture]] · [[kubernetes]] · [[docker]] · [[observabilidade]] · [[secrets-management]]

---
*Fonte: tech-mentor skill · tech-mentor-infra · 2026-04-13*
