---
date: 2026-03-27
tags: [tech-mentor, system-design, deploy, zero-downtime, blue-green, canary, rolling-update, migrations]
skill: tech-mentor-system-design/references/zero-downtime-deployments.md
level: intermediário
---

# Zero-Downtime Deploy

## Contexto

Deploy com downtime é a forma mais comum de causar incidente. A solução não é trabalhar mais rápido — é projetar o deploy para que nunca seja necessário parar o sistema. Regra fundamental: **nunca migre schema e código no mesmo deploy**.

## Como Funciona

### Rolling Update — O Padrão do Kubernetes

```
Antes:  [v1] [v1] [v1] [v1]

Deploy (um pod por vez):
Step 1: [v2] [v1] [v1] [v1]  ← aguarda readiness antes de continuar
Step 4: [v2] [v2] [v2] [v2]  ← completo

v1 e v2 convivem durante o processo → API deve ser backward compatible
```

```yaml
spec:
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 25%        # pods extras durante update
      maxUnavailable: 0    # nunca reduz capacidade → zero-downtime garantido
  minReadySeconds: 30      # aguarda pod estável antes de continuar o rollout
```

### Blue/Green — Rollback Instantâneo

```
DNS/LB → Blue (v1) ← 100% tráfego
          Green (v2) ← smoke tests

Switch: muda seletor do Service para Green
Rollback: 1 comando → aponta de volta para Blue
Custo: 2× infra durante o período de switch
```

```yaml
# Switch para green
# kubectl patch service api -p '{"spec":{"selector":{"version":"green"}}}'

# Rollback para blue
# kubectl patch service api -p '{"spec":{"selector":{"version":"blue"}}}'
```

### Canary — Gradual e Seguro

```
v1: 95% │ v2: 5%   → monitorar error rate, latência
v1: 80% │ v2: 20%  → OK, continua
v1: 0%  │ v2: 100% → promoção completa

Se error rate > threshold → rollback automático para 0%
```

## Código de Referência

### Expand-Contract — Migrations Sem Downtime

```
Renomear coluna "email" para "email_address":

Deploy 1 — Expand:
  ADD COLUMN email_address
  Código: escreve em ambas, lê da nova se disponível

Deploy 2 — Migrate:
  Backfill: UPDATE users SET email_address = email

Deploy 3 — Contract:
  Código só usa email_address
  DROP COLUMN email
```

```sql
-- Deploy 1: adiciona coluna nova (nullable — não bloqueia)
ALTER TABLE users ADD COLUMN email_address VARCHAR(255);

-- Deploy 2: backfill em lotes (não trava a tabela)
DO $$
BEGIN
  LOOP
    UPDATE users SET email_address = email
    WHERE email_address IS NULL LIMIT 1000;
    EXIT WHEN NOT FOUND;
    PERFORM pg_sleep(0.1);
  END LOOP;
END$$;

-- Deploy 3: remove coluna antiga
ALTER TABLE users DROP COLUMN email;

-- Index sem lock de tabela
CREATE INDEX CONCURRENTLY idx_users_email ON users(email);

-- FK sem validação imediata
ALTER TABLE orders ADD CONSTRAINT fk_user
  FOREIGN KEY (user_id) REFERENCES users(id) NOT VALID;
ALTER TABLE orders VALIDATE CONSTRAINT fk_user;
```

### Graceful Shutdown

```typescript
const server = app.listen(3000);
let isShuttingDown = false;

process.on("SIGTERM", async () => {
  console.log({ message: "SIGTERM received — starting graceful shutdown" });
  isShuttingDown = true;

  server.close();
  await waitForActiveRequests(30_000);
  await db.$disconnect();
  await redis.quit();
  process.exit(0);
});

app.get("/health/ready", (req, res) => {
  if (isShuttingDown) return res.status(503).json({ status: "shutting down" });
  res.json({ status: "ready" });
});
```

```yaml
spec:
  terminationGracePeriodSeconds: 60
  containers:
    - lifecycle:
        preStop:
          exec:
            command: ["/bin/sh", "-c", "sleep 5"]
# preStop sleep: absorve lag entre Kubernetes remover o endpoint
# e o LB parar de enviar tráfego para o pod em shutdown
```

## Trade-offs

| Estratégia | Rollback | Complexidade | Custo Infra | Risco DB |
|---|---|---|---|---|
| **Rolling Update** | Lento | Baixa | Normal | API compat obrigatória |
| **Blue/Green** | Instantâneo | Média | 2× durante switch | DB deve suportar 2 versões |
| **Canary** | Gradual/automático | Alta | Normal + roteamento | API compat obrigatória |

## Quando Usar / Quando Evitar

| Operação DB | Segura? | Como fazer |
|---|---|---|
| `ADD COLUMN NULL` | ✅ | Direto |
| `DROP COLUMN` | ❌ imediato | Código para de usar → deploy → drop |
| `RENAME COLUMN` | ❌ imediato | Add nova + dual-write → migrate → drop |
| `CREATE INDEX` | ⚠️ | `CREATE INDEX CONCURRENTLY` |
| `ADD FOREIGN KEY` | ⚠️ | `NOT VALID` → `VALIDATE CONSTRAINT` separado |

**Checklist Zero-Downtime:**
```
[ ] /health/ready falha quando dependências críticas estão down
[ ] terminationGracePeriodSeconds configurado
[ ] preStop hook com sleep para lag do LB
[ ] Migrations via expand-contract
[ ] API backward compatible durante rolling update
[ ] Rollback testado antes do deploy
```

## Conceitos Relacionados

[[fase-4-deploy-operacoes]] · [[load-balancer]] · [[banco-de-dados]] · [[feature-flags]] · [[circuit-breaker]]

---
*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-03-27*
