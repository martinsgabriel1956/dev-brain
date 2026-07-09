---
type: concept
title: "Zero-Downtime Deploy"
aliases: ["zero downtime", "deploy sem downtime", "deploy sem interrupção"]
date_created: 2026-04-22
date_updated: 2026-07-09
source_count: 3
tags: [devops, deploy, cicd, availability, infra, kubernetes, migrations]
skill: tech-mentor-system-design
status: stable
---

# Zero-Downtime Deploy

Deploy que não interrompe o serviço para usuários finais. Exige duas coisas: estratégia de tráfego + migrations backward compatible. **Regra fundamental: nunca migre schema e código no mesmo deploy.**

O oposto direto é o [[concepts/recreate-deployment]] — shutdown seguido de start, com uma janela de downtime inevitável entre os dois. Toda estratégia desta página existe justamente para eliminar essa janela.

## Por Estratégia

| Estratégia | Rollback | Custo Infra | Restrição |
|---|---|---|---|
| [[concepts/rolling-update]] | Lento | Normal | API compat obrigatória |
| [[concepts/blue-green-deploy]] | Instantâneo | 2× durante switch | DB suporta 2 versões |
| [[concepts/canary-release]] | Gradual/automático | Normal + roteamento | Observabilidade necessária |

## Pré-requisito: Expand-Contract

DB migrations backward compatible via [[concepts/expand-contract]] — sem isso, o código novo quebra contra o schema antigo durante a janela de transição.

```
Renomear coluna "email" → "email_address":

Deploy 1 — Expand:   ADD COLUMN email_address; dual-write
Deploy 2 — Migrate:  UPDATE users SET email_address = email (lotes)
Deploy 3 — Contract: DROP COLUMN email
```

Operações seguras em produção:
- `ADD COLUMN NULL` → safe direto
- `CREATE INDEX CONCURRENTLY` → não trava tabela
- `ADD FOREIGN KEY NOT VALID` → valida em passo separado
- `DROP COLUMN` imediato → **destrutivo, nunca fazer**

## Graceful Shutdown

Sem graceful shutdown, pods em terminação cortam conexões ativas — equivale a downtime parcial.

```yaml
spec:
  terminationGracePeriodSeconds: 60
  containers:
    - lifecycle:
        preStop:
          exec:
            command: ["/bin/sh", "-c", "sleep 5"]
# preStop sleep absorve lag entre Kubernetes remover endpoint e LB parar de rotear
```

Handler TypeScript:
```typescript
process.on("SIGTERM", async () => {
  isShuttingDown = true;
  server.close();
  await waitForActiveRequests(30_000);
  await db.$disconnect();
  process.exit(0);
});

app.get("/health/ready", (req, res) => {
  if (isShuttingDown) return res.status(503).json({ status: "shutting down" });
  res.json({ status: "ready" });
});
```

## Rolling Update no Kubernetes

```yaml
spec:
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 25%
      maxUnavailable: 0    # nunca reduz capacidade
  minReadySeconds: 30
```

## Checklist

```
[ ] /health/ready retorna 503 quando dependências críticas estão down
[ ] terminationGracePeriodSeconds configurado
[ ] preStop hook com sleep para lag do LB
[ ] Migrations via Expand-Contract
[ ] API backward compatible durante rolling update
[ ] Rollback testado antes do deploy
```

## Key Sources

- [[sources/blue-green-canary-rolling]]
- [[sources/zero-downtime-deploy]]
- [[sources/tipos-de-deploy]]
