---
date: 2026-03-27
tags: [tech-mentor, system-design, infraestrutura, latencia, performance, back-of-envelope]
skill: tech-mentor-system-design/references/system-design.md
level: fundamento
---

# Números de Latência

## Contexto

Todo arquiteto precisa ter esses números na memória. Não para decorar — para raciocinar. Quando alguém pergunta "isso vai escalar?", a resposta começa aqui. São a base de qualquer estimativa back-of-envelope e da pergunta certa: não "vai funcionar?" — mas "onde está o gargalo?"

## Como Funciona

### A Hierarquia Completa

```
Operação                          Latência        Relativo
─────────────────────────────────────────────────────────
L1 cache reference                   0.5 ns        1×
Branch mispredict                    5   ns        10×
L2 cache reference                   7   ns        14×
Mutex lock/unlock                   25   ns        50×
L3 cache reference                   ~40 ns        ~80×
Main memory (RAM) access            100   ns       200×
─────────────────────────────────────────────────────────
Compress 1KB (Snappy)             3,000   ns       6.000×
Send 1KB over 1 Gbps network     10,000   ns      20.000×    (10 μs)
Read 4KB randomly from SSD       150,000   ns     300.000×   (150 μs)
Read 1MB sequentially from RAM   250,000   ns     500.000×   (250 μs)
─────────────────────────────────────────────────────────
Round trip mesmo datacenter      500,000   ns       1 ms
Read 1MB sequentially from SSD 1,000,000   ns       1 ms
HDD seek                       10,000,000   ns      10 ms
Read 1MB sequentially from HDD 20,000,000   ns      20 ms
─────────────────────────────────────────────────────────
Send packet SP → EUA           ~130,000,000  ns     130 ms
Send packet SP → Europa        ~180,000,000  ns     180 ms
Send packet SP → Ásia          ~250,000,000  ns     250 ms
```

### O que Isso Significa na Prática

**RAM é 1000× mais rápida que SSD. SSD é 100× mais rápido que HDD.**

```
Redis (RAM):      ~0.1 ms   → cache acerto
PostgreSQL (SSD): ~1-10 ms  → query com índice
S3/objeto:        ~20-100ms → leitura de arquivo
Cross-region:     ~130ms+   → chamada de outro continente
```

Cada hop de rede no mesmo datacenter custa ~0.5ms. Uma cadeia de 10 microserviços no mesmo AZ = ~5ms só em rede, antes de qualquer lógica.

## Código de Referência

### Estimativas Back-of-Envelope

**Throughput de leitura:**
```
SSD sequencial:   500 MB/s
RAM sequencial: 4.000 MB/s
Rede 1 Gbps:      125 MB/s
```

**Regras de bolso:**
```
1 ms   = limite para UX perceber como "instantâneo"
10 ms  = limite aceitável para operações de banco
100 ms = usuário percebe lentidão
1 s    = usuário abandona se não houver feedback
```

**Capacidade de uma máquina comum (referência):**
```
Requests HTTP simples:  ~10.000/s por core
Queries PostgreSQL:     ~1.000-5.000/s (com índice)
Redis ops:              ~100.000/s por instância
Kafka mensagens:        ~1.000.000/s por broker
```

### Aplicando em System Design

**Quantos servidores precisamos?**
```
Dado:
- 10M usuários ativos/dia
- Pico: 10× a média
- Cada request: ~50ms de CPU

Cálculo:
- 10M req/dia ÷ 86.400s = ~115 req/s (média)
- Pico: ~1.150 req/s
- 1 core: ~20 req/s a 50ms cada
- 1.150 ÷ 20 = ~58 cores → ~15 servidores 4-core (com folga 2×)
```

**Cache vai ajudar?**
```
Sem cache:
- 1.000 req/s × 10ms (db) = 10.000ms de trabalho/s = 10 cores de DB

Com cache (80% hit rate):
- 200 req/s chegam no banco × 10ms = 2.000ms = 2 cores de DB
- Banco precisa de 5× menos capacidade
```

**Sync ou async?**
```
Fluxo sync: Order → Payment → Inventory → Email
- Payment: 200ms
- Inventory: 100ms
- Email: 500ms
- Total: ~800ms de latência para o usuário

Com mensageria:
- Order retorna em ~10ms
- O resto acontece em paralelo, fora do critical path
```

## Trade-offs

| Camada | Latência | Use para |
|---|---|---|
| **L1/L2 cache** | < 10 ns | Computação in-process |
| **RAM** | ~100 ns | Estado local, buffers |
| **Redis** | ~0.1 ms | Cache distribuído, sessões |
| **SSD (random)** | ~150 μs | Banco com índice |
| **Banco (query)** | 1–10 ms | Leitura com índice |
| **Mesmo DC (rede)** | ~0.5 ms | Microserviços locais |
| **Cross-region** | 130–250 ms | Apenas quando necessário |

## Quando Usar / Quando Evitar

**Os números que mais importam em decisões:**
- Redis vs banco: 100× diferença → cache justifica complexidade para leituras frequentes
- SSD vs HDD: 100× diferença → nunca use HDD para banco OLTP
- Mesmo DC vs cross-region: 260× diferença → coloque serviços dependentes na mesma região
- Sync vs async: quando a soma de latências > SLA → use mensageria para tirar do critical path

**Armadilha comum:** ignorar o custo de rede em microserviços. 10 chamadas no mesmo DC = ~5ms só em overhead de rede. Agrupe operações relacionadas — não fragmente demais.

## Conceitos Relacionados

[[fase-1-fundamentos-infraestrutura]] · [[cache]] · [[banco-de-dados]] · [[load-balancer]] · [[mensageria]]

---
*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-03-27*
