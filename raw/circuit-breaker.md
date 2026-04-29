---
date: 2026-03-27
tags: [tech-mentor, system-design, resiliencia, circuit-breaker, falha-em-cascata, opossum]
skill: tech-mentor-system-design/references/graceful-degradation.md
level: intermediário
---

# Circuit Breaker

## Contexto

O padrão mais importante de resiliência em sistemas distribuídos. Inspirado no disjuntor elétrico: quando há sobrecarga, interrompe o circuito para proteger o sistema. O problema não é a falha em si — é que o serviço saudável fica preso esperando o serviço com falha, consumindo recursos até não sobrar nada.

## Como Funciona

### Falha em Cascata — O Problema

```
Order Service → chama → Payment Service (lento, timeout 30s)
      │
      ├── Thread 1: esperando Payment... (30s)
      ├── Thread 2: esperando Payment... (30s)
      │   ... 200 threads acumuladas ...
      └── Thread pool esgotada → Order Service rejeita tudo

Checkout Service → chama → Order Service (sem threads disponíveis)
      └── Checkout cai também

→ Um serviço lento derrubou dois saudáveis
```

### Os Três Estados

```
          falhas > threshold (ex: 50% em 10s)
CLOSED ──────────────────────────────────────→ OPEN
  ↑                                               │
  │                                               │ timeout expirou (ex: 30s)
  │                                               ↓
  │                                           HALF-OPEN
  │                                               │
  │   request de teste passou                     │
  └───────────────────────────────────────────────┘
                                    │
                    request de teste falhou
                                    ↓
                                 OPEN (reset timer)
```

- **CLOSED**: operação normal — monitora taxa de erro
- **OPEN**: muitas falhas — rejeita imediatamente, sem tentar o downstream
- **HALF-OPEN**: timeout expirou — deixa um request de teste para verificar recuperação

## Código de Referência

### Implementação com Opossum (Node.js)

```typescript
import CircuitBreaker from "opossum";

const paymentBreaker = new CircuitBreaker(callPaymentService, {
  timeout: 3000,                 // request falha após 3s
  errorThresholdPercentage: 50,  // abre se 50%+ das chamadas falharem
  resetTimeout: 30000,           // testa recuperação após 30s no OPEN
  volumeThreshold: 10,           // mínimo de requests antes de avaliar
});

paymentBreaker.fallback(order => ({
  status: "pending",
  orderId: order.id,
  message: "Pagamento em processamento — você será notificado",
  fallback: true
}));

paymentBreaker.on("open", () => {
  console.log({ message: "Circuit breaker OPEN", service: "payment" });
  metrics.increment("circuit_breaker.open", { service: "payment" });
});

paymentBreaker.on("halfOpen", () => {
  console.log({ message: "Circuit breaker HALF-OPEN, testing recovery", service: "payment" });
});

paymentBreaker.on("close", () => {
  console.log({ message: "Circuit breaker CLOSED, service recovered", service: "payment" });
});

async function processPayment(order: Order) {
  return paymentBreaker.fire(order);
}
```

### Combinando Circuit Breaker + Retry

A ordem importa: retry dentro do circuit breaker, não o contrário.

```typescript
// ✅ Correto: retry tenta antes de contar como falha no circuit breaker
async function callWithResilience(order: Order) {
  return paymentBreaker.fire(async () => {
    return retryWithBackoff(() => paymentApi.charge(order), {
      maxRetries: 2,
      baseDelayMs: 100
    });
  });
}

// ❌ Errado: cada retry conta como nova falha — abre o circuito prematuramente
async function callWithResilience(order: Order) {
  return retryWithBackoff(() => paymentBreaker.fire(order), { maxRetries: 3 });
}
```

### Métricas Essenciais

```
circuit_breaker_state{service="payment"}          # 0=closed, 1=open, 2=half-open
circuit_breaker_calls_total{service, result}       # success / failure / rejected
circuit_breaker_open_duration_seconds{service}     # quanto tempo ficou aberto
```

Alerte quando `circuit_breaker_state = 1` por mais de N segundos — serviço downstream degradado.

## Trade-offs

| Aspecto | Sem Circuit Breaker | Com Circuit Breaker |
|---|---|---|
| **Falha em cascata** | Propaga para serviços saudáveis | Contida no serviço com problema |
| **Latência sob falha** | Alta — espera timeout de cada request | Baixa — rejeita imediatamente no OPEN |
| **Recursos** | Thread pool esgota | Recursos liberados rapidamente |
| **Recuperação** | Manual ou por timeout | Automática via HALF-OPEN |
| **Complexidade** | Zero | Biblioteca + fallback + métricas |

## Quando Usar / Quando Evitar

**Use Circuit Breaker em:**
- ✅ Toda chamada HTTP para serviço externo ou microserviço
- ✅ APIs de terceiros (Stripe, CEP, notificações)
- ✅ Qualquer operação com latência variável que pode travar threads

**Não use em:**
- ❌ Operações locais (in-process, sem I/O de rede)
- ❌ Banco de dados primário — prefira connection pool + timeout
- ❌ Jobs assíncronos — use DLQ e retry na fila

**Ajuste os parâmetros pelo contexto:**
```
API crítica (pagamento):     threshold alto (70%), resetTimeout longo (60s)
API não-crítica (analytics): threshold baixo (30%), resetTimeout curto (10s)
```

## Conceitos Relacionados

[[fase-3-resiliencia]] · [[mensageria]] · [[load-balancer]] · [[rate-limiting]] · [[graceful-degradation]]

---
*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-03-27*
