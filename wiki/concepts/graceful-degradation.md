---
type: concept
title: "Graceful Degradation"
aliases: ["degradação graciosa", "degradação elegante"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [resiliencia, graceful-degradation, system-design]
skill: tech-mentor-system-design
status: stub
---

# Graceful Degradation

Sistema continua funcionando com capacidade reduzida quando um componente falha — ao invés de falhar completamente.

## Exemplos

- Notificações não-críticas são descartadas quando pool está cheio; pedido segue.
- Cache retorna dados stale quando banco está indisponível.
- Feature flag desativa funcionalidade não-essencial sob sobrecarga.

## Relação com Bulkhead

[[concepts/bulkhead]] separa recursos por criticidade — permite degradação graciosa ao proteger os críticos e deixar os não-críticos falharem silenciosamente.

```typescript
// Não-crítica — se o pool estiver cheio, descarta silenciosamente
notificationPool.execute(() => notificationService.send(order))
  .catch(err => console.log({ message: "Notification skipped", error: err.message }));
```

## Key Sources

- [[sources/bulkhead]]
