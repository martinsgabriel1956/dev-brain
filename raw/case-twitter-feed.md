---
date: 2026-03-29
tags: [tech-mentor, system-design, cases, twitter, fan-out, timeline, cache]
skill: tech-mentor-system-design/references/system-design-cases
level: arquiteto
---

# Case: Twitter/X Feed

## Contexto

O feed do Twitter é um dos problemas mais clássicos de system design porque concentra os três desafios centrais de escala: **fan-out de escrita**, **latência de leitura** e **consistência eventual**. A solução é um bom exemplo de decisão híbrida baseada em dados reais de uso.

---

## Requisitos

**Funcionais:**
- Postar tweet (texto + mídia)
- Follow/unfollow usuários
- Ver home timeline: tweets de quem sigo, ordem cronológica
- Ver perfil de um usuário

**Não-funcionais (escala real):**
```
350M usuários registrados, 150M DAU
500M tweets postados por dia
Usuário médio segue 200 pessoas
Celebrity: Elon Musk tem 150M followers
Latência de leitura: < 100ms p99
```

---

## O Problema Central: Fan-out

Quando alguém com 1M de followers posta, o sistema precisa decidir: **quando** distribui esse tweet para os feeds dos seguidores?

### Opção A — Fan-out on Write (Push)

Ao postar, escreve o tweet no feed pré-computado de todos os seguidores imediatamente.

```
Post de usuário com 1M followers
  → 1M writes assíncronos no Redis (timeline de cada seguidor)
  → Leitura do feed: O(1) — já está pronto
```

- Leitura extremamente rápida
- Escrita cara para celebridades: 1 tweet = 1M writes

### Opção B — Fan-out on Read (Pull)

Armazena o tweet uma vez. Na leitura, busca todos os seguidos e agrega os tweets.

```
Leitura do feed (segue 200 pessoas):
  → 200 queries de tweets
  → merge e sort por timestamp
  → retorna 20 mais recentes
```

- Escrita O(1)
- Leitura lenta: O(N) sobre número de seguidos

### Solução Híbrida — Como o Twitter Resolve

```
Usuário normal (< 10k followers):  fan-out on write
Celebridade (> 10k followers):     fan-out on read
```

Na leitura do feed, o Timeline Service:
1. Busca o feed pré-computado do usuário (Redis)
2. Identifica celebridades que o usuário segue
3. Faz query dos tweets recentes dessas celebridades em tempo real
4. Faz merge + sort por timestamp
5. Retorna 20 tweets

O custo de injetar 5-10 celebridades on-read é trivial comparado a propagar um tweet de 150M followers on-write.

---

## Arquitetura

```
[Postar Tweet]
Client → API Gateway → Tweet Service
  → Persiste em Tweets DB (sharded por user_id)
  → Publica evento no Kafka (tweet.created)
        ↓
  Fan-out Service (consumers do Kafka)
    → Se usuário normal: escreve tweet_id no Redis de cada seguidor
    → Se celebridade: pula (fan-out on read)
  Media Service (se tiver imagem/vídeo)
    → Upload para S3 → CDN

[Ler Timeline]
Client → Timeline Service
  → Fetch Redis: user_id:timeline (sorted set de tweet_ids)
  → Inject: tweets recentes de celebridades seguidas (query direta)
  → Hydrate: busca dados completos dos tweet_ids (Tweet Service)
  → Merge + sort por timestamp
  → Return 20 tweets
```

---

## Storage

### Tweets DB

```
Cassandra ou MySQL sharded
  Partition key: user_id (para buscar tweets de um usuário por perfil)
  Clustering key: tweet_id DESC (ordem cronológica reversa)

Índice secundário: tweet_id global (para hydration pelo Timeline Service)
```

### Timeline Cache (Redis)

```
key:   timeline:{user_id}
type:  Sorted Set
score: timestamp Unix
value: tweet_id

TTL: 7 dias
  → Se usuário ficou inativo, descarta o cache
  → Na próxima visita: re-computa a partir do DB

Tamanho máximo: 800 tweet_ids por usuário
  → Janela deslizante — remove os mais antigos ao adicionar novos
```

### Media

```
Upload  → S3 (diretamente via presigned URL — não passa pelo backend)
Serving → CloudFront (CDN com cache agressivo)
Thumbnails → gerados assincronamente no upload (fila de processamento)
```

---

## Estimativas de Escala

```
Tweets:
  500M tweets/dia = ~5.800/s (write)
  Leituras >> escritas: ratio de ~100:1

Fan-out (usuários normais):
  Tweet médio: 200 followers × 500M tweets/dia = 100B writes Redis/dia
  = 1.15M writes Redis/segundo (pico)
  → Redis cluster com múltiplos shards por user_id range

Storage de tweets:
  500M tweets/dia × 200 bytes = 100GB/dia de texto
  Acumulado em 5 anos: ~180TB
  → Particionamento por tempo + arquivamento cold
```

---

## Trade-offs Importantes

| Decisão | Escolha | Por quê |
|---|---|---|
| Fan-out celebridades | On-read | 150M writes por tweet seria inviável |
| Timeline storage | Redis sorted set | O(log N) insert, O(1) range query |
| DB de tweets | Cassandra | Escrita intensa, append-only, TTL nativo |
| Media | S3 + CDN | Objetos imutáveis, cache agressivo, custo baixo |
| Fan-out transport | Kafka | Desacopla post do fan-out, replay em falha |

---

## Problemas a Aprofundar em Entrevista

**"E se um usuário segue 10k pessoas comuns?"**
Fan-out on read parcial para quem segue muita gente — mesmo problema invertido. Solução: threshold configurável.

**"Como lidar com tweets deletados?"**
Tweet_ids no Redis apontam para dados que podem não existir mais. Timeline Service filtra na hydration — missing tweet = não exibir.

**"Como funciona o ranking por relevância (não cronológico)?"**
Sorted set por score de relevância em vez de timestamp. O score é computado por modelo de ML separado (engajamento predito, relação com o autor, etc).

---

## Conceitos Relacionados

[[cache]] · [[mensageria]] · [[db-sharding]] · [[cdn]] · [[rate-limiting]] · [[horizontal-vs-vertical-scaling]]

---

*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-03-29*
