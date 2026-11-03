---
type: concept
title: "Circuit Breaker"
aliases: ["circuit breaker pattern", "disjuntor", "opossum"]
date_created: 2026-04-22
date_updated: 2026-11-03
source_count: 5
tags: [resiliencia, circuit-breaker, system-design]
skill: tech-mentor-system-design
status: stable
---

# Circuit Breaker

Padrão de resiliência inspirado no disjuntor elétrico: quando um downstream falha com frequência, interrompe o circuito para proteger o chamador — evita [[wiki/concepts/falha-em-cascata]] e libera recursos enquanto o downstream se recupera.

## O Problema que Resolve

Um serviço lento com timeout de 30s faz threads do chamador acumularem. O thread pool esgota, o chamador para de aceitar requests, e serviços acima também caem — um único serviço degradado derrubou dois saudáveis.

## Os Três Estados

```
          falhas > threshold (ex: 50% em 10s)
CLOSED ─────────────────────────────────────→ OPEN
  ↑                                              │
  │                                              │ timeout expirou (ex: 30s)
  │                                              ↓
  │                                          HALF-OPEN
  │     request de teste passou                  │
  └──────────────────────────────────────────────┘
                               │
               request de teste falhou
                               ↓
                            OPEN (reset timer)
```

- **CLOSED**: operação normal — monitora taxa de erro
- **OPEN**: rejeita imediatamente, sem tentar downstream — recursos liberados
- **HALF-OPEN**: deixa um request de teste; se passar, fecha; se falhar, reabre

## Implementação — Opossum (Node.js)

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
  message: "Pagamento em processamento — você será notificado",
  fallback: true
}));

paymentBreaker.on("open", () =>
  console.log({ message: "Circuit breaker OPEN", service: "payment" })
);
```

## Retry + Circuit Breaker — Duas Composições

```typescript
// Retry dentro: o breaker conta uma falha por operação, depois de esgotar as tentativas
paymentBreaker.fire(async () =>
  retryWithBackoff(() => paymentApi.charge(order), { maxRetries: 2 })
);

// Retry fora: o breaker conta cada tentativa, e o retry precisa tratar a rejeição do circuito aberto
retryWithBackoff(() => paymentBreaker.fire(order), { maxRetries: 3 });
```

Não há ordem universalmente correta, e a escolha muda o que o breaker mede. [[wiki/sources/circuit-breaker]] defende retry dentro e chama retry fora de errado, porque abriria o circuito cedo demais. A documentação oficial não confirma essa regra: retry fora é a [ordem padrão do Resilience4j](https://resilience4j.readme.io/docs/getting-started-3) `[external]`, que pode ser alterada, e é o cenário do [exemplo do Polly](https://www.pollydocs.org/strategies/circuit-breaker.html) `[external]`. Evidência e trade-offs em [[wiki/questions/ordem-retry-circuit-breaker]].

## Métricas Essenciais

```
circuit_breaker_state{service}               # 0=closed, 1=open, 2=half-open
circuit_breaker_calls_total{service, result} # success / failure / rejected
circuit_breaker_open_duration_seconds        # quanto tempo ficou aberto
```

Alertar quando `state = 1` por mais de N segundos — sinal de downstream degradado.

## Ajuste de Parâmetros por Criticidade

```
API crítica (pagamento):     threshold 70%, resetTimeout 60s
API não-crítica (analytics): threshold 30%, resetTimeout 10s
```

## Quando NÃO Usar

- Operações locais sem I/O de rede
- Banco de dados primário → prefira connection pool + timeout
- Jobs assíncronos → use DLQ e retry na fila

## Relação com Bulkhead

Circuit breaker decide **SE** tenta. [[wiki/concepts/bulkhead]] decide **QUANTOS** tentam ao mesmo tempo. Use os dois juntos — bulkhead envolve circuit breaker.

## Origem na Literatura de Microsserviços: Design for Failure

[[wiki/sources/microsservicos-martin-fowler-james-lewis]] situa o circuit breaker (junto de Bulkhead e Timeout, de *Release It!*) como resposta padrão ao princípio de "Design for Failure": qualquer chamada a um serviço remoto pode falhar por indisponibilidade do fornecedor, e o cliente precisa responder de forma graciosa — desvantagem inerente de decompor um sistema em serviços que um monolito em processo não tem. O artigo cita o Simian Army da Netflix (indução deliberada de falhas de serviços e datacenters em produção, durante o horário comercial) como prática de validar essa resiliência na prática, não só em teoria. Também cita a regra prática do Guardian.co.uk — no máximo uma chamada síncrona por requisição de usuário — como forma de evitar o "efeito multiplicativo de downtime" (downtime do sistema = produto dos downtimes de cada componente numa cadeia síncrona).

## Ver também

- [[wiki/concepts/falha-em-cascata]] — problema que o circuit breaker resolve
- [[wiki/concepts/retry-backoff]] — pode ficar dentro ou fora do breaker: ver [[wiki/questions/ordem-retry-circuit-breaker]]
- [[wiki/concepts/bulkhead]] — complemento: limita concorrência
- [[wiki/concepts/graceful-degradation]] — fallback é graceful degradation na prática
- [[wiki/concepts/fail-fast]] — OPEN é o mecanismo de fail fast

## Breaker global para provedor fora do ar

[[wiki/sources/cinco-design-patterns-strategy-observer-adapter-state-machine-retry-circuit-breaker]] traz o caso de um app cujos requests caem sempre no mesmo provedor de IA ou de pagamento: se ele já está offline, não há por que tentar a cada cliente. O breaker corta a chamada e faz uma sondagem de vez em quando (o exemplo é a cada 10 minutos), o que corresponde ao HALF-OPEN (mapeamento da wiki). A fonte não diz se "global" significa por processo ou compartilhado entre instâncias.

## Key Sources

- [[wiki/sources/agentes-em-producao]] — Pilotos de agentes funcionam. Produção quebra em 3 pontos: integração com sistemas legados (APIs internas sem docs), state management (sessões longas não cabem no contexto), e governança (auditoria,...
- [[wiki/sources/bulkhead]]
- [[wiki/sources/circuit-breaker]]
- [[wiki/sources/vale-a-pena-estudar-microsservicos-mesmo-sem-usar]] — circuit breaker citado como conceito que se aplica em qualquer chamada de API externa (banco, serviço de pagamento, terceiro), mesmo dentro de uma aplicação única — não é exclusividade de sistemas distribuídos, ver [[wiki/concepts/microsservicos]]
- [[wiki/sources/cinco-design-patterns-strategy-observer-adapter-state-machine-retry-circuit-breaker]] — breaker global: não chamar a cada request um provedor que já se sabe offline, sondando a cada 10 minutos
