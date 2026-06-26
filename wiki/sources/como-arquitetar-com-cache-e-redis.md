---
type: source
title: "Como Arquitetar com Cache e Redis"
aliases: []
date_created: 2026-06-26
date_updated: 2026-06-26
source_count: 0
tags: [redis, cache, nosql, arquitetura, feature-flag, cqrs, backend]
skill: tech-mentor-backend
status: stable
source_file: /home/nemomartins/Documentos/new/dev-study/raw/como-arquitetar-com-cache-e-redis.md
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-06-26
---

# Como Arquitetar com Cache e Redis

## TL;DR

Guia de decisão e arquitetura para uso de [[redis]] como solução de [[cache]]: o que é, pontos fortes e fracos, e três padrões de arquitetura reais (Feature Flags, Flyweight/Cache-Aside e CQRS com camada de leitura).

## Key Claims

| Claim | Evidência | Confiança |
|---|---|---|
| Redis é um banco [[nosql]] in-memory do tipo chave-valor | Estrutura descrita na fonte; tipos suportados: string, hash, list, set | Alta |
| Cache serve para encurtar o caminho entre aplicação e dados — não para tudo | Fonte distingue casos de baixa volatilidade como adequados | Alta |
| Redis roda em single CPU — o caminho para mais capacidade é clusterizar | Limitação explicitada na fonte; cada instância usa 1 núcleo | Alta |
| [[cache-aside]] (Flyweight) popula o cache sob demanda com TTL | Exemplo 2 da fonte; coincide com padrão da referência `redis-advanced.md` | Alta |
| [[cqrs]] pode usar Redis como camada de leitura, mantendo SQL como fonte de verdade | Exemplo 3 da fonte; batch/trigger sincroniza SQL → Redis | Alta |
| Adicionar cache aumenta complexidade — é necessário pensar em sincronismo e TTL | Seção de tradeoffs da fonte; não é solução universal | Alta |

## Entidades

- [[redis]] — banco NoSQL in-memory, foco do conteúdo
- [[nosql]] — categoria de banco de dados sem esquema relacional

## Conceitos

- [[cache]] — estratégia de manter dados em memória para resposta rápida
- [[cache-aside]] — padrão lazy loading: busca no cache, em miss vai ao banco
- [[feature-flag]] — interruptores de funcionalidade; caso de uso ideal para Redis
- [[banco-in-memory]] — modelo onde os dados vivem na RAM principal
- [[escalabilidade-horizontal]] — adicionar máquinas ao invés de mais recursos na mesma
- [[cqrs]] — separar modelos de escrita e leitura; Redis como read layer
- [[tradeoff-de-cache]] — complexidade adicionada vs ganho de performance
- [[nosql]] — bancos sem esquema relacional, escalam horizontalmente

## Arquiteturas Documentadas

### 1. Feature Flags com Redis

```
[Tela de Gestão] → [Microsserviço Manutenção] → [Banco SQL]
                                                      ↓
                                                 [Batch Job]
                                                      ↓
                                                   [Redis]
                                                      ↑
[Aplicação] → [Microsserviço Feature Toggle] ─────────┘
```

### 2. Cache-Aside / Flyweight

```
Aplicação → Microsserviço → Redis (existe?) → retorna
                                 ↓ miss
                             Banco SQL → salva no Redis (TTL) → retorna
```

### 3. CQRS com Redis como Read Layer

```
[Domínio]
  ├── Write → [SQL]          ← fonte de verdade
  └── Read  → [Redis]        ← projeção rápida
                  ↑
          [Batch/Trigger de sync]
```

## Quando Usar Cache

**Bons candidatos (baixa volatilidade + alta leitura):**
- Feature flags
- Menus e permissões de usuário
- Saldo e extrato (muda apenas em transações)
- Tokens de sessão
- Chaves de configuração

**Evitar:**
- Dados financeiros críticos onde consistência supera performance
- Dados que mudam a cada request
- Datasets pequenos que cabem em memória da aplicação

## Open Questions

- A fonte menciona "segurança limitada" do Redis (permissões estáticas). Redis 6+ introduziu ACLs granulares — a afirmação pode estar desatualizada para versões modernas.
- A fonte compara Redis vs banco relacional, mas não menciona Memcached como alternativa de cache in-memory.

## Raw Quotes

> "O objetivo do cache é encurtar o caminho — uma vez que você já pegou aquelas informações, você segura em memória para ter performance na resposta."

> "Quando você coloca um cache no meio, a sua aplicação automaticamente fica mais complexa. Não saia utilizando para tudo — nenhuma solução serve para tudo."
