---
date: 2026-03-27
tags: [tech-mentor, system-design, infraestrutura, dns, load-balancer, cdn, cache, banco, mensageria]
skill: tech-mentor-system-design/references/system-design.md
level: fundamento
---

# Fase 1 — Fundamentos de Infraestrutura

## Contexto

Esses são os blocos que compõem qualquer sistema. Não é necessário memorizar configuração de cada um — é preciso entender **o que cada um resolve** e **onde se encaixa na arquitetura**. A pergunta-chave para cada componente: _"Se esse componente cair, o que acontece com o sistema?"_

## Como Funciona

### 1. DNS — Como uma requisição chega até você

Processo de resolver `api.empresa.com` → IP do servidor.

```
Browser digita "api.empresa.com"
        ↓
1. Cache local (browser + OS)
        ↓
2. Recursive Resolver (ISP ou 8.8.8.8)
        ↓
3. Root Server → TLD Server (.com)
        ↓
4. Authoritative NS → retorna IP → cacheado por TTL
```

**O que importa para system design:**
- **TTL baixo** (30s): mudanças propagam rápido, mais carga nos DNS servers — use para failover rápido
- **TTL alto** (24h): propagação lenta, menos carga — use para estabilidade
- **A record**: hostname → IPv4
- **CNAME**: hostname → outro hostname
- **DNS como LB**: múltiplos IPs no mesmo A record — simples, sem health check

### 2. Load Balancer — Distribuindo tráfego

```
                   ┌── App Server 1
Client → LB ───────┼── App Server 2
                   └── App Server 3
```

**L4 vs L7:**

| | L4 (Transport) | L7 (Application) |
|---|---|---|
| **Opera em** | TCP/UDP | HTTP/HTTPS |
| **Decisão por** | IP + porta | URL, headers, cookies |
| **Velocidade** | Mais rápido | Mais lento (lê o payload) |
| **Exemplos** | AWS NLB | AWS ALB, Nginx, Traefik |

**Algoritmos:**
- **Round-robin**: sequência simples, ignora carga real
- **Least connections**: servidor com menos conexões ativas — melhor para workloads heterogêneos
- **IP hash**: mesmo cliente → mesmo servidor (sessões sem cache distribuído)
- **Weighted**: servidores mais potentes recebem mais tráfego proporcionalmente

**Health check**: LB pinga `/health` a cada N segundos. X falhas → remove da rotação. Recuperou → reinsere. Isso habilita deploy sem downtime.

### 3. CDN — Conteúdo próximo do usuário

```
Usuário (São Paulo)
        │
[PoP: GRU — Cloudflare/Fastly]
        │
        ├── Cache HIT  → responde em ~5-10ms
        └── Cache MISS → busca no origin (~120ms) → cacheia → responde
```

**Quando usar:**
- ✅ Arquivos estáticos (JS, CSS, imagens) — cache longo com hash na URL
- ✅ Vídeo — CDN é obrigatório, origin não aguenta
- ✅ APIs com respostas públicas e cacheáveis

**Quando não resolve:**
- ❌ Dados personalizados por usuário
- ❌ Mutações (POST/PUT/DELETE)
- ❌ Real-time (WebSocket)

**Cache invalidation no CDN:**
- Por TTL: automático, pode servir stale
- Por purge: chamada de API no deploy
- Por versionamento de URL: `style.abc123.css` — URL muda com o conteúdo, zero problema

### 4. Cache — Evitando trabalho repetido

**Cache-aside** (mais comum):
```
App busca no cache
    ├── HIT → retorna direto
    └── MISS → busca no DB → salva no cache → retorna
```

**Write-through**: escreve no cache E no DB na mesma operação — consistência forte, write mais lento.

**Write-behind**: escreve no cache → retorna. Persiste no DB async — write rápido, risco de perda se o cache cair.

**Redis:**
```
~100.000 ops/s | ~1ms latência | TTL por key
Eviction: LRU quando memória esgota
```

**Cache invalidation**: das coisas mais difíceis em computação.
- TTL curto: aceita dado levemente stale
- Invalidação explícita: ao escrever no DB, deleta a chave no cache
- CDC + eventos: mudança no DB → evento → consumer invalida

### 5. Banco de Dados — Onde o estado vive

| Critério | Relacional (PostgreSQL) | NoSQL |
|---|---|---|
| **Queries** | JOINs, agregações | Simples, por chave |
| **Consistência** | ACID completo | Eventual (geralmente) |
| **Escala de escrita** | Vertical (um primário) | Horizontal nativo |
| **Use para** | Financeiro, multi-entidade | Catálogos, feeds, escala massiva |

**Índices:**
```sql
-- Sem índice: full table scan O(n)
-- Com índice B-tree: O(log n)
CREATE INDEX idx_orders_user_id ON orders(user_id);
```

Indexe colunas frequentes em `WHERE`, `JOIN ON`, `ORDER BY`. Índice acelera leitura e tem overhead nas escritas.

**Read replicas:**
```
Writes → Primary
Reads  → Replica 1, Replica 2, Replica 3
```
Réplicas têm replication lag (ms). Se o caso exige "ler o que acabei de escrever" → leia do primário.

### 6. Mensageria — Comunicação assíncrona

| | Fila (SQS, RabbitMQ) | Stream (Kafka) |
|---|---|---|
| **Entrega** | 1 consumer por mensagem | Todos os consumer groups leem |
| **Retenção** | Deleta após consumo | Retém por tempo (ex: 7 dias) |
| **Replay** | Não | Sim — reprocessar desde offset X |
| **Use para** | Tasks, jobs, work distribution | Logs, eventos, audit trail |

**Kafka — o que todo arquiteto precisa saber:**
```
Topic     → categoria de mensagens ("orders")
Partition → divisão paralela — ordering garantido dentro da partition
Offset    → posição do consumer — ele controla
Consumer Group → N consumers dividem as partitions entre si

Por que é rápido: append-only log = sequential disk writes
Sequential: ~500 MB/s vs Random: ~100 IOPS — diferença de 1000x
```

**Quando usar mensageria:**
- Processos que podem ser assíncronos (email, notificação, relatório)
- Absorver bursts: fila absorve o pico, workers processam no ritmo deles
- Desacoplamento: `payment-service` publica `OrderPaid`, `notification-service` consome

### 7. Números para ter na cabeça

```
LATÊNCIAS:
  L1 cache CPU:          0.5 ns
  RAM:                   100 ns
  SSD (NVMe):            100 μs
  HDD:                   10 ms
  Rede (mesma DC):       500 μs
  Rede (cross-region):   50 ms

CAPACIDADE TÍPICA:
  Node.js (API simples): ~10.000 req/s
  PostgreSQL (indexado): ~10.000 queries/s
  Redis:                 ~100.000 ops/s
  Kafka:                 ~1.000.000 msgs/s por partição

CONVERSÕES ÚTEIS:
  1M req/dia  = ~12 req/s
  1B req/dia  = ~12.000 req/s
```

## Código de Referência

### Estimativa back-of-envelope

```
DAU: 10M usuários
Requests/usuário/dia: 20
Total: 200M req/dia → ~2.300 req/s (média)
Pico: 2.300 × 3 = ~7.000 req/s

→ 1 servidor Node.js aguenta o pico
→ 2 servidores + LB: redundância
→ PostgreSQL aguenta se indexado
→ Redis obrigatório se query for repetitiva
```

## Trade-offs

| Componente | Se cair... |
|---|---|
| CDN | Origin recebe todo o tráfego — pode não aguentar |
| Cache | Todas as leituras vão para o banco — sobrecarrega |
| Load Balancer | Sistema fica indisponível (SPOF) |
| Read Replica | Leituras vão para o primário — escrita fica mais lenta |
| Mensageria | Comunicação vira síncrona — acoplamento aumenta |

## Conceitos Relacionados

[[fase-2-framework-system-design]] · [[redis]] · [[kafka]] · [[postgresql]] · [[cdn]] · [[load-balancer]]
