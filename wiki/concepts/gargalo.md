---
type: concept
title: "Gargalo"
aliases: ["bottleneck", "gargalo de sistema", "ponto de contenção"]
date_created: 2026-06-26
date_updated: 2026-07-15
source_count: 2
tags: [system-design, performance, escalabilidade, debugging, monitoramento]
skill: tech-mentor-system-design
status: draft
---

# Gargalo

O componente de um sistema que **limita o throughput total** — o ponto mais lento da cadeia que determina a velocidade máxima do sistema inteiro. Identificar o gargalo correto é a primeira regra antes de qualquer ação de escalabilidade.

> "A corrente é tão forte quanto seu elo mais fraco."

## Por que identificar antes de escalar

Adicionar recursos na camada errada não resolve — e ainda desperdiça dinheiro:

- Adicionar servidores de aplicação se o banco está travando → banco continua travando
- Otimizar código se o problema é rede → rede continua lenta
- Escalar a API se o gargalo é uma fila de jobs → fila continua represada

## Gargalos comuns por camada

| Camada | Sintoma | Solução típica |
|---|---|---|
| **CPU** | CPU acima de 70% constantemente | Escalabilidade vertical ou horizontal |
| **Memória** | RAM no limite, swap ativo | Aumentar RAM ou reduzir footprint |
| **Banco de dados** | Queries lentas, connection pool esgotado | Cache, índices, read replicas, sharding |
| **Rede** | Latência alta, timeouts | CDN, compressão, HTTP/2, proximidade geográfica |
| **Fila** | Fila crescendo mais rápido do que é processada | Mais workers, particionamento |
| **Código** | CPU alta sem carga externa | Profiling, algoritmo ineficiente ([[big-o]]) |

## Banco de dados é o gargalo mais comum

Na maioria dos sistemas web, a camada de aplicação escala facilmente (é [[stateless]], horizontal). O banco de dados é stateful por natureza e concentra toda a contention. Por isso:

1. **Cache primeiro** — [[cache]] reduz hits ao banco sem complexidade de escala
2. **Índices** — a diferença entre 1s e 1ms em uma query
3. **Read replicas** — distribui carga de leitura ([[replicacao-de-banco]])
4. **Sharding** — último recurso quando writes também precisam escalar ([[sharding]])

## Métricas de alerta

| Métrica | Threshold de preocupação |
|---|---|
| Latência | Requisições de 100ms agora levam 500ms |
| CPU | Acima de 70% sem folga para picos |
| Memória | Constantemente no limite, swap em uso |
| Fila | Tamanho crescendo consistentemente |

## Regra de ouro

> "Não escale prematuramente. Identifique o gargalo. Escale a camada certa."

## Relação com outros conceitos

- [[big-o]] — complexidade algorítmica ruim é gargalo de código puro
- [[cache]] — a ferramenta mais eficiente para aliviar gargalo de banco
- [[sharding]] e [[replicacao-de-banco]] — soluções para gargalo no banco de dados
- [[escalabilidade-horizontal]] — solução para gargalo na camada de aplicação
- [[auto-scaling]] — automatiza a resposta ao gargalo detectado por métricas

## Key sources

- [[wiki/sources/escalabilidade-vertical-horizontal-system-design]]
- [[wiki/sources/observabilidade-ponta-a-ponta-opentelemetry-ia-amsterdam]] — CPU profile/flame graph como técnica prática de "gargalo de código": tirar uma foto da CPU para achar a função que mais consome tempo de execução; caso real onde isso revelou um pacote compartilhado travando o event loop, corrigido com ~50% de ganho de velocidade
