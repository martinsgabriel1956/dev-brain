---
type: concept
title: "Cache"
aliases: ["caching", "cache de aplicação"]
date_created: 2026-06-26
date_updated: 2026-09-04
source_count: 12
tags: [cache, performance, redis, arquitetura, backend, grande-rollback, buffer]
skill: tech-mentor-backend
status: stable
---

# Cache

## TL;DR

Estratégia de guardar dados já processados em memória de acesso rápido para evitar recomputação ou viagem ao banco. O objetivo é encurtar o caminho entre a aplicação e os dados.

## Quando Usar

Cache resolve bem **dados com baixa volatilidade e alta frequência de leitura**:

- Feature flags / toggles
- Menus e permissões de usuário
- Saldo e extrato (atualiza só em transações)
- Tokens de sessão
- Catálogos de produto, configurações

## Quando NÃO Usar

- Dados financeiros críticos (consistência > performance)
- Dados que mudam a cada request (overhead > ganho)
- Datasets pequenos (L1 in-process resolve sem Redis)
- Endpoints write-heavy (cache ajuda read-heavy)

## Padrões de Cache

| Padrão | Leitura | Escrita | Consistência |
|---|---|---|---|
| [[cache-aside]] (Lazy) | Cache + DB on miss | Só DB (invalida cache) | Eventual |
| Write-Through | Cache hit | Cache + DB simultâneo | Forte |
| Write-Behind | Cache hit | Só cache (sync assíncrono) | Eventual |

## Hierarquia de Velocidade

```
L1 — In-process (Map/LRU)   ns   — por processo, sem I/O
L2 — Redis / Memcached       μs  — compartilhado entre instâncias
L3 — CDN Edge               ms   — economiza RTT de rede
L4 — Database               ms   — fonte de verdade
```

## Tradeoffs

Adicionar cache aumenta a complexidade: [[tradeoff-de-cache]]. Cache não deve ser confundido com [[wiki/concepts/buffer]]: cache guarda dados **para reutilizá-los** (olha para o passado), enquanto buffer absorve **diferença de velocidade** entre produtor e consumidor e descarta o dado após o consumo (olha para o presente) — ver [[wiki/concepts/cache-vs-buffer]]. É necessário pensar em:

- Estratégia de invalidação (TTL fixo, evento, tag)
- Sincronismo entre cache e banco de dados
- Manutenção de mais uma tecnologia no stack

## Principais Implementações

- **[[redis]]** — banco in-memory chave-valor; caso de uso principal
- Memcached — alternativa mais simples ao Redis (sem persistência, sem tipos ricos)
- In-process LRU — L1 local ao processo (node-lru-cache, Guava Cache)

## Cache Como Solução para Cross-Shard Fan-Out

Em bancos [[wiki/concepts/sharding|shardeados]], queries agregadas simples (ex.: "10 posts mais populares") viram *fan-out*: consultar todos os shards, trazer resultados à memória e agregar — latência alta mesmo para query conceitualmente trivial. A solução recomendada é armazenar o resultado agregado em cache com TTL (minutos a horas, dependendo da regra de negócio), evitando repetir o fan-out a cada requisição. Ver [[wiki/sources/sharding-charging-fragmentacao-banco-de-dados]].

## Cache em Aplicações com LLM

Além dos padrões clássicos acima, IA adiciona uma camada de cache específica:

- **Cache de tokens em LLMs** — cada provider implementa de forma diferente (OpenAI, Gemini, Claude), mas o objetivo é o mesmo: não reprocessar/repagar por tokens de contexto repetidos entre chamadas. Ver [[wiki/concepts/kv-cache]].
- **Cache de contexto e embeddings** — relevante em [[wiki/concepts/rag-arquitetura-avancada|RAG]], para não recalcular embeddings de conteúdo já indexado.
- **Cache-aware prompts e fingerprints** — usar identificadores do prompt/contexto para decidir se uma resposta pode vir do cache em vez de nova chamada ao modelo.

Não entender bem essa camada de cache impacta latência, mas principalmente **custo**: cada chamada e cada token de LLM tem custo direto — ver [[wiki/concepts/ai-gateway-llm-router]].

**Exemplo numérico concreto de cache hit vs. miss:** [[wiki/sources/agent-waves-custo-modelos-fortes-fracos-kimi]] cita preços reais da [[wiki/entities/moonshot-ai|Moonshot AI]] onde o cache de tokens de input muda o custo em até 10×: o Kimi K3 cobra US$3/M tokens de input em cache miss contra US$0,30/M em cache hit; o Kimi K2.7 Code cobra US$0,95/M em cache miss contra US$0,19/M em cache hit. Isso mostra concretamente por que "cache de tokens em LLMs" (acima) não é um detalhe de implementação do provider — é uma alavanca de custo de ordem de grandeza, visível diretamente na tabela de preços pública.

## Key Sources

- [[wiki/sources/como-arquitetar-com-cache-e-redis]]
- [[wiki/sources/escalabilidade-vertical-horizontal-system-design]] — cache como "melhor amigo antes de escalar"; banco é o gargalo mais comum
- [[wiki/sources/shopify-redis-para-mysql-skip-locked-black-friday]] — contraponto: cache como camada de reserva foi removido em favor do banco relacional puro, ver [[wiki/concepts/grande-rollback]]
- [[wiki/sources/10-conceitos-fundamentais-backend]] — framing didático de cache hit/miss; a pergunta central não é "usar cache ou não" mas "quando essa resposta deixa de ser verdade"
- [[wiki/sources/system-design-simulador-hotel-booking-replit]] — demonstração num simulador interativo: mesmo tráfego, banco de dados saturado a 115% cai drasticamente ao conectar cache, porque a maioria das leituras de um sistema de reserva de hotel repete os mesmos quartos populares (read-heavy); IA avaliadora do exercício aponta cache invalidation como lacuna não tratada
- [[wiki/sources/escalar-leituras-banco-de-dados-entrevista-tier-s]] — cache posicionado como o **último** degrau (não o primeiro): especialista em dois problemas — hotspots (perfil de celebridade a 200k req/s) e queries caras (joins/agregações de leaderboard/dashboard) — ambos respondidos em <1ms; cilada de entrevista é adicionar cache antes de otimizar índices/pooling
- [[wiki/sources/system-design-por-nivel-junior-pleno-senior]] — em entrevista sênior, "adicionar cache" como escolha de escala é seguido de aprofundamento esperado sobre o tipo (ex.: cache-aside) — não basta citar a peça, é preciso justificar a estratégia
- [[wiki/sources/sharding-charging-fragmentacao-banco-de-dados]] — cache como solução recomendada para cross-shard operations (fan-out) em bancos shardeados
- [[wiki/sources/cache-vs-buffer-diferenca-conceitual]] — cache definido pela expectativa de reutilização e explicitamente contrastado com [[wiki/concepts/buffer]] (diferença de velocidade); origem histórica no cache de CPU (IBM System/360, chamado *high speed buffer*)
- [[wiki/sources/8-pontos-arquitetura-de-software-na-era-da-ia]] — camada específica de IA: cache de tokens por provider, cache de contexto/embeddings em RAG, cache-aware prompts e fingerprints; caching como alavanca de custo, não só de latência
- [[wiki/sources/system-design-load-balancer-nivel-macaco]] — cache citado, numa pergunta frequente de aula introdutória, como técnica alternativa a "só adicionar mais servidor/load balancer" para escalar, reforçando o mesmo framing de "melhor amigo antes de escalar" já registrado acima
- [[wiki/sources/agent-waves-custo-modelos-fortes-fracos-kimi]] — preços reais de cache hit vs. miss da Moonshot AI (Kimi K3 e K2.7 Code), diferença de até 10× no custo de input tokens
