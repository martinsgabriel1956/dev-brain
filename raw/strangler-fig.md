---
date: 2026-04-14
tags: [tech-mentor, arquitetura, migração, legado, padrões]
skill: tech-mentor-system-design/references/arquitetura
level: avançado
---

# Strangler Fig Pattern

## Contexto

O nome vem da figueira-mata-pau (strangler fig): uma planta que cresce ao redor de uma árvore hospedeira, gradualmente a substituindo enquanto a árvore original ainda está viva e funcional. O padrão descreve exatamente isso: substituir um sistema legado incrementalmente, em vez de uma big-bang rewrite.

Big-bang rewrites falham em cerca de 80% dos casos (dados do Standish Group). O custo de manter dois sistemas rodando por um período é sempre menor que o risco de uma migração que leva meses ou anos sem entregar valor.

## Como Funciona

### Os Três Estágios

```
Estágio 1: Transform
  → Criar o novo sistema em paralelo com o legado
  → Implementar a nova feature no novo sistema (não no legado)

Estágio 2: Coexist
  → Proxy/façade roteia parte do tráfego para o novo sistema
  → Legado e novo sistema rodam simultaneamente
  → Feature flags controlam o roteamento

Estágio 3: Eliminate
  → Quando o novo sistema cobre 100% do legado: desligar o legado
  → Remover o proxy/façade se ele não tiver mais propósito
```

### Implementação com Proxy/Façade

```typescript
// API Gateway ou Reverse Proxy com roteamento baseado em feature flags
// Exemplo: migrando /orders do monolito para microsserviço

type RouteConfig = {
  path: string;
  legacyUrl: string;
  newUrl: string;
  rolloutPercentage: number; // 0-100
};

async function strangerProxy(req: Request, res: Response, config: RouteConfig) {
  const isNewSystem = shouldRouteToNew(req, config.rolloutPercentage);

  const target = isNewSystem ? config.newUrl : config.legacyUrl;

  const response = await fetch(`${target}${req.url}`, {
    method: req.method,
    headers: req.headers,
    body: req.body
  });

  // Log para monitorar divergências entre sistemas
  if (process.env.NODE_ENV === "production") {
    const altResponse = await fetch(`${isNewSystem ? config.legacyUrl : config.newUrl}${req.url}`, {
      method: req.method,
      headers: req.headers,
      body: req.body
    });

    if (response.status !== altResponse.status) {
      console.log({ message: "Response divergence detected", path: req.url, newStatus: response.status, legacyStatus: altResponse.status });
    }
  }

  return response;
}

function shouldRouteToNew(req: Request, percentage: number): boolean {
  // Consistente por user ID: mesmo usuário sempre vai para o mesmo sistema
  if (req.headers["x-user-id"]) {
    const hash = parseInt(req.headers["x-user-id"].slice(-2), 16);
    return (hash % 100) < percentage;
  }
  return Math.random() * 100 < percentage;
}
```

### Migração de Banco de Dados

O banco é geralmente a parte mais difícil. Estratégia com CDC (Change Data Capture):

```
Fase 1: Legado escreve apenas no banco legado
  Legado → DB_legado
  CDC Debezium → replica para DB_novo em tempo real

Fase 2: Novo sistema lê do DB_novo (somente leitura)
  → Validar consistência entre os dois bancos

Fase 3: Novo sistema escreve no DB_novo
  CDC → replica de volta para DB_legado (para rollback de emergência)

Fase 4: Cortar o legado
  → Remover replicação reversa
  → Desativar legado
```

### Expand-Contract para APIs

Quando o contrato da API precisa mudar durante a migração:

```
Expand: adicionar o novo campo opcional sem remover o antigo
  { "userId": "123", "user_id": "123" }  // ambos presentes

Contract (após migração dos consumers):
  { "userId": "123" }  // remove o campo antigo
```

### Monitoramento Durante Migração

```typescript
// Shadow mode: envia request para ambos os sistemas, usa resposta do primário
// Útil para validar comportamento antes de migrar tráfego real

async function shadowRequest(primaryUrl: string, shadowUrl: string, req: Request) {
  const [primary, shadow] = await Promise.allSettled([
    fetch(primaryUrl, { method: req.method, body: req.body }),
    fetch(shadowUrl, { method: req.method, body: req.body })
  ]);

  if (primary.status === "fulfilled" && shadow.status === "fulfilled") {
    const primaryData = await primary.value.json();
    const shadowData = await shadow.value.json();

    if (JSON.stringify(primaryData) !== JSON.stringify(shadowData)) {
      console.log({ message: "Shadow divergence", path: req.url });
      // Incrementar métrica para análise
    }
  }

  // Retorna sempre a resposta do primário
  return primary.status === "fulfilled" ? primary.value : new Response("", { status: 500 });
}
```

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---|---|---|
| **Risco** | Rollback imediato se o novo sistema falha | Período de manutenção de dois sistemas |
| **Entrega** | Valor entregue incrementalmente | Migração pode se arrastar por meses |
| **Dados** | Migração gradual com validação | Sincronização entre dois bancos é complexa |
| **Débito** | Legado não cresce mais (novas features no novo) | Proxy/façade precisa de manutenção |

## Quando Usar / Quando Evitar

**Usar quando:**
- Sistema legado em produção com usuários ativos — downtime inaceitável
- Reescrita completa é muito arriscada ou demorada (> 6 meses)
- Equipe pequena que não pode paralisar o desenvolvimento de produto durante a migração
- Migração de monolito para microsserviços por domínio

**Evitar quando:**
- Sistema legado é pequeno e tem cobertura de testes — reescrita direta é mais simples
- O legado tem um contrato de dados impossível de sincronizar durante transição
- A arquitetura do legado é tão diferente que manter proxy custaria mais que a reescrita

## Conceitos Relacionados

[[microsservicos]] · [[feature-flags]] · [[zero-downtime-deploy]] · [[event-driven-architecture]] · [[anti-patterns]]

---
*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-04-14*
