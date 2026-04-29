---
type: source
title: "Circuit Breaker"
aliases: ["circuit breaker pattern", "opossum", "falha em cascata"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 0
tags: [resiliencia, circuit-breaker, system-design, node]
skill: tech-mentor-system-design
status: stable
source_file: /home/nemomartins/Documentos/new/dev-study/raw/circuit-breaker.md
source_url:
author:
date_published: 2026-03-27
date_ingested: 2026-04-22
---

# Circuit Breaker

## TL;DR

O padrão mais importante de resiliência em sistemas distribuídos. Resolve falha em cascata: quando um downstream fica lento, threads acumulam até o pool esgotar e o serviço saudável cai junto. Circuit breaker rejeita imediatamente no estado OPEN, libera recursos e dá tempo ao downstream se recuperar.

---

## Key Claims

**O problema: falha em cascata**
- Um serviço lento com timeout de 30s faz threads do chamador acumularem
- Thread pool esgota → chamador rejeita novos requests → serviços acima também caem
- "Um serviço lento derrubou dois saudáveis"

**Três estados**
- `CLOSED`: normal, monitora taxa de erro
- `OPEN`: falhas > threshold → rejeita imediatamente, sem tentar downstream
- `HALF-OPEN`: timeout expirou → deixa um request de teste; se passar, fecha; se falhar, reabre

**Implementação Opossum (Node.js) — parâmetros chave**
```typescript
new CircuitBreaker(fn, {
  timeout: 3000,                 // request falha após 3s
  errorThresholdPercentage: 50,  // abre se 50%+ falhar
  resetTimeout: 30000,           // testa recuperação após 30s no OPEN
  volumeThreshold: 10,           // mínimo de requests antes de avaliar
});
```

**Fallback obrigatório**
```typescript
breaker.fallback(order => ({
  status: "pending",
  message: "Pagamento em processamento — você será notificado",
  fallback: true
}));
```

**Retry dentro do circuit breaker — ordem importa**
```
✅ paymentBreaker.fire( () => retryWithBackoff(fn) )
   → retry tenta antes de contar como falha no circuito

❌ retryWithBackoff( () => paymentBreaker.fire(fn) )
   → cada retry conta como nova falha — abre o circuito prematuramente
```

**Métricas essenciais**
```
circuit_breaker_state{service}          # 0=closed, 1=open, 2=half-open
circuit_breaker_calls_total{service, result}  # success / failure / rejected
circuit_breaker_open_duration_seconds   # quanto tempo ficou aberto
```
Alertar quando `state = 1` por mais de N segundos.

**Ajuste de parâmetros por criticidade**
```
API crítica (pagamento):     threshold 70%, resetTimeout 60s
API não-crítica (analytics): threshold 30%, resetTimeout 10s
```

**Quando NÃO usar**
- Operações locais sem I/O de rede
- Banco de dados primário → prefira connection pool + timeout
- Jobs assíncronos → use DLQ e retry na fila

---

## Conceitos Tocados

- [[concepts/circuit-breaker]] — o padrão em si
- [[concepts/falha-em-cascata]] — problema que o circuit breaker resolve
- [[concepts/retry-backoff]] — deve ficar dentro do circuit breaker, não fora
- [[concepts/bulkhead]] — decide QUANTOS tentam; circuit breaker decide SE tenta
- [[concepts/graceful-degradation]] — fallback é a expressão prática de graceful degradation
- [[concepts/observabilidade]] — métricas de state e calls_total

---

## Open Questions

- Qual biblioteca de circuit breaker para outros runtimes (Java, Python, Go)?
- Como testar circuit breaker em integration tests sem derrubar serviço real?
