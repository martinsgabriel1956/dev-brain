---
date: 2026-04-17
tags: [tech-mentor, arquitetura, estilos-arquiteturais, resiliencia, cloud]
skill: tech-mentor-system-design/references/architecture-styles
level: avançado
---

# Cell-Based Architecture

## Contexto
Uma evolução do modelo de Availability Zones: em vez de zonas geográficas, o sistema é particionado em **células funcionalmente completas e independentes**. Cada célula serve um subconjunto de usuários ou tenants e pode falhar sem afetar as outras.

Adotada por Amazon (Availability Zones internas), Slack (sharding por workspace), Discord (guilds), DoorDash e Shopify. O driver principal é **blast radius containment**: uma falha em produção não derruba tudo.

## Como Funciona

```
          ┌─────────────┐
          │   Router    │  ← Cell Selector
          │ (Cell Map)  │    (user_id → cell_id)
          └──────┬──────┘
        ┌────────┼────────┐
        ▼        ▼        ▼
   ┌─────────┐ ┌─────────┐ ┌─────────┐
   │ Cell A  │ │ Cell B  │ │ Cell C  │
   │ App     │ │ App     │ │ App     │
   │ Cache   │ │ Cache   │ │ Cache   │
   │ DB      │ │ DB      │ │ DB      │
   │ Queue   │ │ Queue   │ │ Queue   │
   └─────────┘ └─────────┘ └─────────┘
   (users 1-1M)(users 1M-2M)(users 2M-3M)
```

**Cell:** stack completa e autossuficiente — app servers, banco, cache, filas. Não compartilha infra entre células.

**Cell Selector (Router):** mapeia o identificador do usuário/tenant para a célula correta. O mapeamento é geralmente armazenado em um serviço de roteamento global (fora das células).

**Cell Map:** tabela de mapeamento `{entity_id → cell_id}`. Precisa ser consultada com baixa latência — geralmente cacheada em memória no router.

**Rebalancing:** quando uma célula cresce demais, split a célula e migra metade dos tenants. É o ponto mais delicado operacionalmente.

## Código de Referência

```typescript
// Cell selector — lógica de roteamento
type CellMap = Map<string, string>; // tenantId → cellId

class CellRouter {
  constructor(
    private cellMap: CellMap,
    private cellEndpoints: Map<string, string> // cellId → base URL
  ) {}

  getEndpoint(tenantId: string): string {
    const cellId = this.cellMap.get(tenantId);
    if (!cellId) throw new Error(`No cell assigned for tenant ${tenantId}`);

    const endpoint = this.cellEndpoints.get(cellId);
    if (!endpoint) throw new Error(`Cell ${cellId} endpoint not found`);

    return endpoint;
  }

  // Chamado durante rebalancing
  reassign(tenantId: string, newCellId: string) {
    this.cellMap.set(tenantId, newCellId);
  }
}

// No middleware HTTP — injeta o endpoint da célula certa no request
async function cellRoutingMiddleware(req: Request, res: Response, next: NextFunction) {
  const tenantId = req.headers["x-tenant-id"] as string;
  const endpoint = router.getEndpoint(tenantId);
  req.cellEndpoint = endpoint;
  next();
}
```

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---|---|---|
| Blast Radius | Falha de célula afeta apenas ~1/N dos usuários | Infraestrutura N vezes mais cara |
| Deploy | Rollout célula por célula = canary natural | Coordenação de deploys entre células é complexa |
| Escalabilidade | Escala adicionando células sem rearquitetar | Rebalancing de tenants é complexo |
| Isolamento | Multi-tenancy com isolamento de hardware real | Cell-crossing operations são caras ou impossíveis |
| Compliance | Dados de um tenant ficam em uma célula (GDPR) | Global queries exigem fanout por todas as células |

## Quando Usar / Quando Evitar

**Usar quando:**
- O produto tem multi-tenancy e falha de um tenant não pode afetar outros
- SLA de disponibilidade exige isolamento real (99.99%+)
- O sistema já escala horizontalmente e o próximo passo é contenção de falhas

**Evitar quando:**
- O sistema tem operações cross-tenant frequentes (relatórios globais, analytics em tempo real)
- A base de usuários é pequena e a overhead operacional não se paga
- Você ainda está construindo o produto — Cell-Based é otimização de escala, não arquitetura inicial

## Conceitos Relacionados
[[microsservicos]] · [[multi-tenancy]] · [[db-sharding]] · [[consistent-hashing]] · [[multi-region-global-lb]]

---
*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-04-17*
