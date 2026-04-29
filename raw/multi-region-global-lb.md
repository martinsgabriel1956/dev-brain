---
date: 2026-03-29
tags: [tech-mentor, system-design, arquitetura, multi-region, load-balancer, disponibilidade]
skill: tech-mentor-system-design/references/multi-region-global-lb
level: arquiteto
---

# Multi-region & Global Load Balancing

## Contexto

SLA de 99,99% significa no máximo 52 minutos de downtime por ano. Uma única região não garante isso — data centers inteiros já caíram. Multi-region é a resposta para disponibilidade global, latência baixa próximo ao usuário e conformidade regulatória (LGPD, GDPR exigem dados em regiões específicas).

O custo é real: multi-region custa 2-3× mais que single-region. A decisão precisa ser justificada pelo negócio.

---

## Estratégias de Roteamento Global

### Latency-based Routing

Roteia o usuário para a região com menor RTT medido. É o mais comum para performance.

```
Usuário em São Paulo → ap-southeast-1 (60ms RTT)
Usuário em Nova York → us-east-1 (8ms RTT)
```

- **AWS Route 53**: latency routing policy com mapa de latências por região atualizado continuamente
- **Cloudflare**: Anycast por padrão — tráfego automaticamente vai ao PoP mais próximo
- **GCP**: Global Load Balancer com IP Anycast único global

### Geo-based Routing

Roteia com base na localização geográfica do IP de origem (país, continente).

- Útil para compliance: usuários brasileiros → região Brasil (LGPD)
- Menos preciso que latency-based para otimização de performance pura

### Weighted Routing

Divide tráfego por percentual entre regiões. Base para canary deployment global e blue/green inter-regional.

### Failover Routing (Active-Passive)

Região primária ativa; secundária em standby. Health check determina o failover. RTO depende do TTL do DNS (mínimo ~60s) mais tempo de warmup.

---

## Arquiteturas Multi-region

### Active-Active

Todas as regiões servem tráfego simultaneamente.

```
Usuários → Global LB → us-east-1     (50%)
                     → eu-west-1     (30%)
                     → ap-southeast  (20%)
```

- **Prós**: máxima disponibilidade e menor latência para usuários em qualquer ponto
- **Contras**: consistência de dados é o problema central — requer replicação multi-region e gestão de conflitos de escrita
- **Requer**: banco multi-master ou read-local/write-global, filas replicadas, secrets disponíveis em todas as regiões

### Active-Passive

Região primária serve tráfego; secundária em standby quente.

```
Usuários → Route 53 → us-east-1 (primary — health OK)
                    → eu-west-1 (failover — só ativa se primary falhar)
```

- **Prós**: muito mais simples de operar, consistência de dados garantida
- **Contras**: usuários fora da região primária têm latência maior; failover tem delay (TTL do DNS)

### Read-local / Write-global

O padrão mais equilibrado para a maioria dos casos:

- **Writes** vão para a região primária → consistência forte garantida
- **Reads** servidos pela réplica mais próxima → latência baixa para leitura

Implementações: Aurora Global Database, CockroachDB, Cloud Spanner.

```
Escrita:  Usuário BR → us-east-1 (primary) → replica async → sa-east-1
Leitura:  Usuário BR → sa-east-1 (réplica local, RPO < 1s)
```

---

## Consistência de Dados Multi-region

| Padrão | Consistência | Latência Write | Complexidade |
|---|---|---|---|
| Single-region primary | Forte | Baixa | Baixa |
| Aurora Global DB | Forte (write region), RPO < 1s | Baixa | Média |
| CockroachDB / Spanner | Serializável global | Alta (consensus cross-region) | Alta |
| DynamoDB Global Tables | Eventual | Baixa (multi-master) | Média |

**Regra de ouro**: consistência forte cross-region custa latência. Consensus (Raft/Paxos) entre regiões significa round-trips intercontinentais em cada write. Escolha conscientemente.

---

## Global Load Balancers — Comparativo por Provider

### AWS

| Serviço | Nível | Uso principal |
|---|---|---|
| **Route 53** | DNS | Latency/geo/weighted/failover routing |
| **Global Accelerator** | Rede (Anycast) | Failover em segundos, não 60s de TTL |
| **CloudFront** | CDN + L7 | Edge cache, Lambda@Edge, static assets |

**Route 53 vs Global Accelerator**: Route 53 depende de TTL (mínimo 60s para failover). Global Accelerator usa Anycast na rede AWS — failover em ~30s sem dependência de DNS TTL. Para SLAs agressivos, Global Accelerator é a escolha.

### GCP

- **Cloud Load Balancing**: IP Anycast único global, Premium Tier mantém tráfego na rede Google até o PoP mais próximo do usuário
- Integrado nativamente com Cloud Armor (WAF) e Cloud CDN

### Cloudflare

- Anycast nativo em 300+ PoPs
- **Load Balancing**: health checks + geo steering + latency steering
- **Argo Smart Routing**: otimiza rota dentro da rede Cloudflare, reduzindo latência em 30% em média

---

## Implementação de Failover

```
1. Health checks a cada 10s por região
2. Threshold: 3 falhas consecutivas = região unhealthy
3. Route 53 TTL: 60s (mínimo prático)
   Global Accelerator: ~30s (sem dependência de TTL)
4. Alertas ao detectar failover (PagerDuty, OpsGenie)
5. Runbook documentado e testado trimestralmente
```

### Checklist antes de precisar

- [ ] Banco replicado para região secundária (RDS Multi-region, Aurora Global)
- [ ] Secrets disponíveis em todas as regiões (AWS Secrets Manager replication)
- [ ] Filas/mensageria com tolerância a falha regional
- [ ] DNS TTL baixo configurado **antes** de um incidente — reduzir TTL durante crise não adianta (cache já está distribuído)
- [ ] Chaos Engineering trimestral — failover não testado é failover quebrado

---

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---|---|---|
| **Disponibilidade** | Sobrevive a falha regional completa | Complexidade operacional alta |
| **Latência** | Usuário sempre próximo de um servidor | Writes cross-region têm latência extra |
| **Compliance** | Dados em região específica (LGPD/GDPR) | Particionamento de dados aumenta complexidade |
| **Custo** | — | 2-3× mais caro que single-region |
| **Consistência** | Read-local resolve leitura | Multi-master exige resolução de conflitos |

---

## Quando Usar / Quando Evitar

**Use multi-region quando:**
- SLA exige 99,99%+ (52 min/ano) — Multi-AZ não resolve
- Base de usuários globalmente distribuída (latência percebida importa)
- Regulatório exige dados em regiões específicas
- Negócio justifica o custo operacional 2-3× maior

**Não use multi-region quando:**
- Produto em validação — complexidade mata velocidade de iteração
- SLA de 99,9% é suficiente (8,7h/ano) — single-region com Multi-AZ resolve
- Base de usuários concentrada geograficamente
- Time não tem maturidade operacional para gerenciar failover cross-region

**Multi-AZ primeiro**: antes de multi-region, garanta que sua aplicação é resiliente a falha de availability zone dentro da mesma região. É 90% do benefício com 10% da complexidade.

---

## Conceitos Relacionados

[[load-balancer]] · [[cdn]] · [[dns]] · [[banco-de-dados]] · [[observabilidade]] · [[microservicos-vs-monolito-modular]]

---

*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-03-29*
