---
date: 2026-04-17
tags: [tech-mentor, system-design, estimativas, capacidade, entrevista]
skill: tech-mentor-system-design/references/methodology
level: arquiteto
---

# Estimativas Back-of-Envelope

## Contexto
Em entrevistas de system design e no trabalho real, estimativas rápidas de carga guiam decisões de arquitetura antes de partir para o design detalhado. O objetivo não é precisão — é ordem de grandeza para evitar over/under-engineering.

## Números que Todo Arquiteto Deve Saber

```
Latências típicas:
  Memória RAM:          ~100 ns
  SSD read:             ~100 μs    (1.000x mais lento que RAM)
  Rede dentro do DC:    ~500 μs
  HDD seek:             ~10 ms     (100x mais lento que SSD)
  RTT cross-region:     ~150 ms
  RTT Brasil → EUA:     ~130 ms

Capacidade:
  1 Gbps link:          125 MB/s
  SSD throughput:       ~500 MB/s
  Disco → RAM:          ~3 GB/s

Tamanhos típicos:
  UUID v4:              36 bytes (string), 16 bytes (binary)
  Timestamp:            8 bytes
  Tweet/post médio:     ~200 bytes
  Imagem de perfil:     ~100 KB
  Foto de alta qualidade: ~1-5 MB
  Vídeo 1min 1080p:     ~100 MB
```

## Framework de Estimativa — 4 Passos

### 1. Clarificar o escopo
- Quantos usuários ativos? DAU, MAU
- Qual a proporção read/write? (ex: 100:1 em redes sociais)
- Peak vs. average? (ex: Black Friday = 10x o normal)

### 2. Estimar QPS (Queries Per Second)

```
Exemplo: Twitter-like com 300M DAU

Cada usuário ativo:
  - Entra na timeline 2x/dia
  - Lê ~20 tweets por sessão (read)
  - Posta 1 tweet/dia em média (write)

Reads/dia = 300M × 2 × 20 = 12B reads/dia
         = 12B / 86.400s ≈ 140.000 reads/s (avg)
         Peak: × 5 = 700.000 reads/s

Writes/dia = 300M × 1 = 300M writes/dia
           = 300M / 86.400s ≈ 3.500 writes/s
           Peak: × 5 = 17.500 writes/s
```

### 3. Estimar Storage

```
Exemplo: 5 anos de tweets

Tamanho de 1 tweet:
  - tweet_id: 8 bytes
  - user_id: 8 bytes
  - content: 280 chars × 2 bytes = 560 bytes
  - created_at: 8 bytes
  - metadata: ~50 bytes
  Total: ~640 bytes ≈ 1 KB (com índices e overhead)

Writes/dia = 300M tweets/dia × 1 KB = 300 GB/dia
5 anos = 300 GB × 365 × 5 ≈ 550 TB

Com replicação 3x: 550 TB × 3 ≈ 1.65 PB
→ Sharding necessário (nenhum banco único aguenta isso)
```

### 4. Estimar Bandwidth

```
Reads de timeline:
  700.000 reads/s × 20 tweets × 1 KB = 14 GB/s

Isso é tráfego de saída (egress) — caro em cloud.
→ Cache agressivo é necessário (CDN + Redis)
→ Meta usa compressão (zstd) — reduz 3-4x

Com compressão: ~4 GB/s → ~32 Gbps de link necessário
```

## Tabela de Referência Rápida

| Escala | QPS | Arquitetura |
|---|---|---|
| Startup | < 1.000 | Monolito + PostgreSQL |
| Crescimento | 1k-10k | + Read replicas + Cache |
| Scale | 10k-100k | + Sharding + CDN |
| Internet-scale | > 100k | Microsserviços + Cell-based |

## Exemplo Prático — URL Shortener

```
Requisitos: 100M URLs/dia criadas, 10:1 read/write

Writes: 100M / 86.400 ≈ 1.200 QPS (peak: 6.000)
Reads:  1.200 × 10 = 12.000 QPS (peak: 60.000)

URL armazenada: ~500 bytes × 100M/dia × 365 × 5 anos = 91 TB
→ PostgreSQL ou DynamoDB com sharding por hash da short URL

Com 60.000 leituras/s: cache hit rate de 99% = 600 queries/s ao DB
→ Redis cluster + PostgreSQL read replicas é suficiente

Short URL de 7 chars (base62): 62^7 = 3.5 trilhões de URLs únicas
→ mais que suficiente para anos de operação
```

## Conceitos Relacionados
[[cap-theorem]] · [[db-sharding]] · [[consistent-hashing]] · [[rate-limiting]] · [[cache-strategies]]

---
*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-04-17*
