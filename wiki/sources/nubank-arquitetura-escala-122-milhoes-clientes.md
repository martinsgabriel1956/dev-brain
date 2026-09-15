---
type: source
title: "Por Dentro da Arquitetura do Nubank: Como Escalar para 122 Milhões de Clientes"
aliases: ["nubank arquitetura escala", "nubank scalability units", "nubank alexandria observabilidade"]
date_created: 2026-09-15
date_updated: 2026-09-15
source_count: 0
tags: [nubank, clojure, datomic, kafka, event-sourcing, cqrs, sharding, cell-based-architecture, observabilidade, fraud-scoring, fintech, microsservicos]
skill: tech-mentor-backend
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/nubank-arquitetura-escala-122-milhoes-clientes.md
source_url: ""
author: "não identificado"
date_published: ""
date_ingested: 2026-09-15
---

# Por Dentro da Arquitetura do Nubank: Como Escalar para 122 Milhões de Clientes

## TL;DR

Vídeo (autor não identificado) que atualiza o retrato técnico do Nubank já coberto em [[wiki/sources/nubank-clojure-datomic-event-sourcing]] com números de 2025 (122M clientes, 4.000 microsserviços, 72 bilhões de eventos Kafka/dia, 20 shards, 600 TB de logs/dia) e três decisões arquiteturais **novas** para a wiki: **Scalability Units** (sharding como clone completo da infraestrutura, não só do banco), a otimização do caminho crítico de autorização de transação (10.000ms → 288ms no P90 via materialização na escrita) e a plataforma de observabilidade construída internamente, **Alexandria**. Reforça Clojure/Datomic/Kafka/Event Sourcing já documentados, sem contradizê-los.

## Claims Principais

### 1. Sharding no Nubank é clonagem de infraestrutura completa, não só partição de banco
**Evidência:** citação atribuída ao site do Nubank: sharding tradicional "bateu em limites físicos, incluindo a AWS ficando sem máquinas" em 2016. A resposta foi um esquema de **Scalability Units**: cada um dos 20 shards brasileiros replica toda a stack — microsserviços, clusters Kafka dedicados, bancos Datomic separados, redes isoladas — não apenas uma fatia do banco de dados.
**Confidence:** Média — não há link primário/paper citado no vídeo, mas a citação é atribuída explicitamente ao site oficial do Nubank; consistente com o padrão arquitetural **[[wiki/concepts/cell-based-architecture|Cell-Based Architecture]]** já documentado via `tech-mentor-backend`.

### 2. Roteamento por shard acontece no login, não por request
**Evidência:** "quando você faz login no app, o sistema sabe em qual shard você está e roteia todas as suas requisições para lá" — implica um roteador global/mapa de shard resolvido uma vez por sessão, não recalculado a cada chamada.
**Confidence:** Média — detalhe de implementação não aprofundado no vídeo.

### 3. Autorização de transação: latência crítica reduzida de ~10.000ms para 288ms (P90) via precomputação
**Evidência:** "removendo dependências síncronas do caminho crítico... precomputam e materializam as informações necessárias... os cálculos pesados acontecem no momento da escrita, não da leitura" — redução de 76% citada. O requisito de negócio (autorização de cartão) precisa responder em <100ms ponta a ponta na cadeia adquirente → bandeira → banco.
**Confidence:** Média-alta — número específico e verificável (288ms P90), mas sem link para o post/talk de engenharia original que o vídeo parafraseia.

### 4. Plataforma de observabilidade Alexandria foi construída internamente por custo, não por preferência técnica
**Evidência:** citação atribuída ao site do Nubank: "chegamos a um ponto em que poderíamos contratar o Lionel Messi como engenheiro de software pagando o mesmo valor que pagávamos pela solução externa" de logs. Arquitetura resultante: ingestão via Kafka em microbatch, processamento com filtros/agregações customizados, storage em S3 colunar com 95% de compressão, query engine distribuída. Resultado: 50% mais barato que a solução terceirizada anterior.
**Confidence:** Média — citação vívida e específica, mas não localizada por link direto nesta ingestão; volume (600 TB logs/dia, 15.000 queries/dia, ~150 PB escaneados) não verificado de forma independente.

### 5. Antifraude usa short-circuit: regra determinística evita rodar o modelo de ML
**Evidência:** "se uma regra simples já consegue classificar a transação como suspeita, o modelo de machine learning nem roda — economizando tempo e recurso". Plataforma processa 450 milhões de eventos/dia, dividida em detecção (regras + ML) e ação (bloquear/alertar/deixar passar).
**Confidence:** Média — padrão plausível e citado sem detalhe de implementação (qual regra, qual modelo).

### 6. Refatoração do orquestrador antifraude para DAG reduziu latência de 550ms para 350ms
**Evidência:** "cada componente espera apenas pelos dados que ele precisa e nada mais" — mudança de um modelo de orquestração anterior (não descrito) para um baseado em grafo acíclico dirigido (DAG), em fluxos complexos de decisão de fraude.
**Confidence:** Média — número específico, mas sem detalhe do "antes" (que tipo de orquestrador foi substituído).

### 7. Reforço: Clojure, Datomic, Kafka e Event Sourcing como já documentado
**Evidência:** repete a tese central de [[wiki/sources/nubank-clojure-datomic-event-sourcing]] — imutabilidade elimina race conditions e complexidade acidental; Datomic como "Git para banco de dados" com time-travel; extrato bancário como analogia de Event Sourcing. **Novo detalhe não presente na fonte anterior**: a arquitetura interna do Datomic é separada em **transactor** (processa todas as escritas) e múltiplos **peers** (leitura, escaláveis horizontalmente), com o storage por trás podendo ser DynamoDB, um relacional, ou outro backend — resolvendo o par clássico "escrita consistente vs. leitura performática".
**Confidence:** Alta para a tese já registrada (reforço direto); Média para o detalhe novo de transactor/peers (sem link primário, mas coerente com a arquitetura pública documentada do Datomic).

## Entidades e Conceitos Tocados

- [[wiki/entities/nubank]]
- [[wiki/entities/clojure]]
- [[wiki/concepts/datomic]]
- [[wiki/concepts/kafka]]
- [[wiki/concepts/event-sourcing]]
- [[wiki/concepts/cqrs]]
- [[wiki/concepts/sharding]]
- [[wiki/concepts/cell-based-architecture]] — novo stub criado nesta ingestão
- [[wiki/concepts/microsservicos]]
- [[wiki/concepts/observabilidade]]
- [[wiki/entities/alexandria-nubank]] — novo stub criado nesta ingestão
- [[wiki/concepts/dynamodb]]

## Open Questions

- **Fonte primária não localizada.** O vídeo cita repetidamente "uma citação no site do Nubank" (Edward Wible, "Lionel Messi", limites físicos da AWS em 2016) sem exibir URL. A wiki registra essas claims como atribuídas, não verificadas de forma independente — se uma ingestão futura localizar o(s) post(s) de engenharia do Nubank (blog `building.nubank.com` ou equivalente), promover confidence e adicionar `source_url`.
- **Qual orquestrador o DAG substituiu na plataforma antifraude?** O vídeo não descreve o modelo anterior (sequencial? outro grafo?) — só o resultado (550ms → 350ms).
- **Alexandria: qual solução terceirizada foi substituída?** Não nomeada (Datadog? Splunk? ELK gerenciado?) — relevante para futuras comparações de custo em [[wiki/concepts/observabilidade]].
- **Datomic transactor/peers**: esta ingestão registra esse detalhe de arquitetura pela primeira vez na wiki — vale checar contra a documentação oficial do Datomic (ver [[wiki/sources/sql-nao-e-banco-de-dados-uncle-bob]], que já cobre Datomic por outro ângulo) numa ingestão futura dedicada ao produto em si.

## Citações Brutas

> "Eu não encontrei uma opção melhor que o Datomic, com esse conceito de tempo como cidadão de primeira classe. Para mim, isso faz toda a diferença." — atribuída a Edward Wible (CTO Nubank)

> "Nós modelamos tudo no banco como stream processing. Até batch jobs são distribuídos como streams de mensagens no Kafka." — atribuída à InfoQ

> "Melhorias de escalabilidade como sharding funcionaram bem por um tempo, mas eventualmente bateram em limites físicos — incluindo a AWS ficando sem máquinas para acompanhar o ritmo de crescimento do Nubank." — atribuída ao site do Nubank

> "Chegamos a um ponto em que poderíamos contratar o Lionel Messi como engenheiro de software pagando o mesmo valor que pagávamos pela solução externa." — atribuída ao site do Nubank, sobre o custo da solução de logs terceirizada
