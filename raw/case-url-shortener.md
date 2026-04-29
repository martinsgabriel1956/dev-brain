---
date: 2026-03-29
tags: [tech-mentor, system-design, cases, url-shortener, hashing, cache, redirect]
skill: tech-mentor-system-design/references/system-design-cases
level: arquiteto
---

# Case: URL Shortener

## Contexto

URL Shortener parece trivial mas é um ótimo exercício de system design porque força decisões reais sobre geração de IDs distribuídos, estratégia de cache, trade-off entre rastreabilidade e performance (301 vs 302), e como escalar uma operação de leitura extremamente intensa.

---

## Requisitos

**Funcionais:**
- Dado uma URL longa, gerar uma URL curta (ex: `bit.ly/4c92xk`)
- Dado uma URL curta, redirecionar para a URL original
- URLs podem expirar após X dias (opcional)
- Analytics: contagem de cliques por URL

**Não-funcionais:**
```
Alta disponibilidade — redirect nunca pode falhar
Baixa latência: redirect < 10ms p99
Scale:
  100M URLs criadas/dia
  10B redirects/dia
  Read:Write ratio = 100:1
```

---

## Estimativas

```
Escritas (criar URLs):
  100M/dia ÷ 86.400s = 1.160 req/s

Leituras (redirects):
  10B/dia ÷ 86.400s = 115.740 req/s

Storage:
  URL longa: ~500 bytes
  100M/dia × 365 × 5 anos = 182B URLs → ~91TB
  Na prática: 80% do tráfego vai para 20% das URLs (Pareto)
  → Cache resolve a grande maioria sem tocar o banco

Tamanho do short code:
  Base62 (a-z, A-Z, 0-9): 7 chars = 62^7 = 3,5 trilhões de combinações
  → suficiente para 100M/dia por ~95 anos
```

---

## Geração do Short Code

Quatro abordagens, com trade-offs distintos:

### Opção 1 — Hash (MD5/SHA256) truncado

```
MD5(url_longa) → "a3f9b2c1d4..." → pegar primeiros 7 chars → "a3f9b2c"
```

- Problema: **colisões** — URLs diferentes podem gerar o mesmo hash truncado
- Resolve colisão com sufixo incremental, mas complica a implementação
- Não recomendado para produção

### Opção 2 — ID sequencial + Base62

```
id = 1.000.001 → base62 → "4c92x"
```

- Simples e sem colisão
- Problema: **previsível e enumerável** — scraping trivial de todas as URLs do sistema

### Opção 3 — ID sequencial + embaralhamento de bits

```
id → embaralha bits com chave privada → base62
```

- Único e não previsível sem a chave
- Difícil de enumerar
- Boa opção para escala moderada

### Opção 4 — Snowflake ID + Base62 ✅ Recomendado

```
Snowflake: timestamp (41 bits) + worker_id (10 bits) + sequence (12 bits)
  → ID único distribuído sem coordenação central
  → base62 → short code de 7-8 chars
```

- Sem colisão garantida
- Sem coordenação central (cada worker gera IDs independentemente)
- Ordenado por tempo — útil para debugging
- Escala horizontal trivial

---

## Arquitetura

```
[Criar URL curta]
Client → API Service
  → Gera Snowflake ID → converte para base62 → short_code
  → Persiste: { short_code, original_url, user_id, expires_at, created_at }
  → Salva no Redis (TTL 24h)
  → Retorna: https://bit.ly/{short_code}

[Redirect]
Client → CDN (cache de redirects populares)
  → miss → API Service
      → Redis: GET short_code → hit (95%) → redirect
      → miss → PostgreSQL → atualiza Redis → redirect
      → Incrementa contador (async via Kafka → Analytics Service)
```

---

## 301 vs 302 — Trade-off Real

```
301 Permanent Redirect:
  Browser cacheia → próximas visitas não chegam ao servidor
  ✅ Menos carga no servidor
  ❌ Impossível rastrear clicks (request não chega mais ao backend)
  ❌ Impossível fazer rollback se URL de destino mudar

302 Temporary Redirect:
  Sem cache no browser → todo request passa pelo servidor
  ✅ Analytics preciso: cada click registrado
  ✅ URL de destino pode ser alterada a qualquer momento
  ❌ Mais load no servidor
```

**Decisão prática**: 302 por padrão (analytics). Oferecer 301 como opção para quem não precisa de tracking — ex: CDNs internos, links de assets estáticos.

---

## Cache Strategy

```
Redis com TTL:
  key:   short:{short_code}
  value: original_url
  TTL:   24h para URLs comuns, 7 dias para URLs marcadas como "populares"

Hot cache (in-memory na API):
  Top 1.000 URLs = ~60% de todo o tráfego
  Cache local LRU de 10k entradas por instância da API
  → evita round-trip ao Redis para URLs virais

Cache invalidation:
  URL deletada → Redis DEL imediato
  URL com destino atualizado → Redis DEL + re-insert
```

### Por que 95% resolve no cache

Distribuição de acesso a URLs segue power law:
- Top 1% das URLs = ~80% dos redirects
- A vasta maioria das 91TB de dados nunca é acessada
- Storage barato, cache quente: Redis de 50GB resolve o volume relevante

---

## Analytics

Analytics não pode estar no caminho crítico do redirect — adiciona latência e cria acoplamento.

```
Redirect acontece → publica evento no Kafka: { short_code, timestamp, ip, user_agent }
                                                    ↓
                                        Analytics Consumer
                                          → agrega por janela de tempo
                                          → persiste no ClickHouse (OLAP)
                                          → dashboards via API separada
```

Contadores em tempo real (se necessário):
```
Redis INCR clicks:{short_code}
  → flush para DB a cada 60s (batch write)
  → evita write amplification no banco principal
```

---

## Trade-offs

| Decisão | Escolha | Por quê |
|---|---|---|
| Geração de ID | Snowflake + base62 | Distribuído, sem colisão, sem coordenação central |
| Redirect | 302 por padrão | Analytics preciso, destino mutável |
| Cache | Redis + hot cache local | 95% dos redirects sem tocar o DB |
| Analytics | Kafka async | Fora do caminho crítico do redirect |
| DB principal | PostgreSQL | Escala de write comportável (1.160 req/s), ACID para integridade |

---

## Problemas a Aprofundar em Entrevista

**"Como prevenir que alguém enumere todas as URLs?"**
Snowflake ID torna a enumeração computacionalmente inviável. Adicionalmente: rate limiting por IP no endpoint de redirect.

**"E se dois workers gerarem o mesmo Snowflake ID?"**
Impossível se worker_id for único — Snowflake garante unicidade por worker. A atribuição de worker_id é o único ponto que precisa de coordenação (ex: via ZooKeeper ou registro no startup).

**"Como escalar para 1 trilhão de URLs?"**
Sharding do PostgreSQL por `short_code` (hash-based). Cada shard cuida de um range de prefixos.

**"URLs maliciosas (phishing)?"**
Integração com Google Safe Browsing API na criação. Rejeitar URLs na lista negra antes de persistir.

---

## Conceitos Relacionados

[[cache]] · [[rate-limiting]] · [[db-sharding]] · [[mensageria]] · [[numeros-de-latencia]] · [[horizontal-vs-vertical-scaling]]

---

*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-03-29*
