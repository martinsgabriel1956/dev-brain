---
date: 2026-04-14
tags: [tech-mentor, backend, arquitetura, microsserviços]
skill: tech-mentor-backend/references/arquitetura
level: avançado
---

# Microsserviços

## Contexto

Microsserviços é um estilo arquitetural onde o sistema é decomposto em serviços pequenos, independentes, cada um rodando em seu próprio processo e se comunicando via rede. É a evolução natural de um monolito modular que atingiu os limites de escalabilidade de deploy.

O termo foi popularizado por Martin Fowler e James Lewis em 2014, mas o conceito de "autonomia de serviços" vem de antes — SOA (Service-Oriented Architecture) tentou isso, mas com acoplamento de infraestrutura (ESB) que acabou criando monolitos distribuídos.

## Como Funciona

### Decomposição por Domínio

O critério correto de decomposição é **Bounded Context do DDD** — cada serviço possui um domínio coeso, linguagem ubíqua própria e dados isolados. Decomposição errada é por camadas técnicas (ex: "serviço de banco de dados").

```
❌ Decomposição técnica (errado)
  ├── data-service
  ├── api-service
  └── ui-service

✅ Decomposição por domínio (correto)
  ├── orders-service        → cria, cancela, rastreia pedidos
  ├── payments-service      → cobra, reembolsa, reconcilia
  ├── inventory-service     → estoque, reserva, movimentação
  └── notifications-service → email, push, SMS
```

### Autonomia de Deploy

Cada serviço deve poder ser deployado **independentemente**, sem coordenar com outros times. Isso exige:
- **Contrato estável** entre serviços (API versionada ou eventos com schema evolution)
- **Database per Service** — nenhum serviço acessa o banco do outro diretamente
- **CI/CD próprio** — pipeline por repositório ou por serviço no monorepo

### Comunicação

| Padrão | Quando usar | Trade-off |
|---|---|---|
| REST/gRPC síncrono | Query que precisa de resposta imediata | Acoplamento temporal |
| Mensageria assíncrona | Comandos, eventos, notificações | Complexidade de garantia de entrega |
| BFF (Backend for Frontend) | Múltiplos clientes com necessidades diferentes | Mais um serviço para manter |

### Padrões de Resiliência Obrigatórios

Em microsserviços, falhas parciais são o estado normal. Sem resiliência, uma falha em cascata derruba tudo.

```typescript
// Circuit Breaker + Retry — padrão mínimo para chamadas síncronas
import CircuitBreaker from "opossum";

const options = {
  timeout: 3000,          // falha se demorar > 3s
  errorThresholdPercentage: 50,
  resetTimeout: 10000     // tenta reabrir após 10s
};

const breaker = new CircuitBreaker(callPaymentsService, options);
breaker.fallback(() => ({ status: "unavailable", retry: true }));

async function processOrder(orderId: string) {
  return breaker.fire(orderId);
}
```

### Service Discovery

Serviços precisam descobrir uns aos outros sem IPs hardcoded.

```yaml
# Kubernetes — DNS-based discovery automático
# payments-service pode ser alcançado como:
# http://payments-service.namespace.svc.cluster.local

apiVersion: v1
kind: Service
metadata:
  name: payments-service
spec:
  selector:
    app: payments
  ports:
    - port: 3000
```

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---|---|---|
| **Deploy** | Deploys independentes, menor blast radius | Orquestração complexa (K8s, service mesh) |
| **Escalabilidade** | Escala seletiva por serviço | Latência de rede entre serviços |
| **Times** | Times autônomos por domínio (Conway's Law) | Proliferação de repositórios/serviços |
| **Tecnologia** | Polyglot (linguagem certa por domínio) | Inconsistência de stack, maior superfície de manutenção |
| **Dados** | Isolamento de banco, autonomia | Queries cross-service, sem JOINs nativos |
| **Observabilidade** | Granularidade de métricas por serviço | Distributed tracing obrigatório para debugar |
| **Consistência** | — | Sem transações ACID entre serviços (Saga obrigatória) |

## Quando Usar / Quando Evitar

**Usar quando:**
- Times de 50+ engenheiros que travam uns aos outros em deploys
- Partes do sistema têm características de escala radicalmente diferentes (ex: search vs. billing)
- Domínios com SLAs diferentes (ex: checkout deve ter 99.99%, backoffice pode ter menos)
- Maturidade de CI/CD, observabilidade e on-call já está estabelecida

**Evitar quando:**
- Time pequeno (< 10 engenheiros) — overhead operacional mata produtividade
- Sistema ainda em descoberta de produto — fronteiras de domínio ainda mudam muito
- Sem cultura de on-call e observabilidade — microsserviços sem tracing é um pesadelo
- O problema real é falta de modularidade, não de deployabilidade — **modularize primeiro**

> **Regra prática:** Comece com Monolito Modular. Extraia microsserviços quando um módulo específico tem requisito de escala ou autonomia de deploy que o monolito não consegue atender.

## Conceitos Relacionados

[[monolito-modular]] · [[bounded-context]] · [[saga-pattern]] · [[outbox-pattern]] · [[service-mesh]] · [[event-driven-architecture]] · [[conways-law]]

---
*Fonte: tech-mentor skill · tech-mentor-backend · 2026-04-14*
