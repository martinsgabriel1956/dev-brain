---
type: concept
title: "Building Blocks de System Design"
aliases: ["building blocks", "blocos de construção", "componentes de system design"]
date_created: 2026-09-30
date_updated: 2026-09-30
source_count: 1
tags: [system-design, building-blocks, load-balancer, cache, cdn, filas, sharding, rate-limiter]
skill: tech-mentor-system-design
status: draft
---

# Building Blocks de System Design

Componentes recorrentes com propósito conhecido, combinados para resolver um gargalo específico. O ponto do autor da fonte: decorar a definição não basta; é preciso saber **qual problema cada bloco resolve, quando usar e o custo** ([[wiki/sources/como-estudar-system-design-building-blocks-instagram-simplificado]]).

| Bloco | Problema que resolve | Quando usar | Páginas |
|---|---|---|---|
| Load balancer | sobrecarga/queda do back end com muitos acessos | múltiplas instâncias servindo a mesma API | [[wiki/concepts/load-balancer]] |
| CDN (+ object storage) | conteúdo estático lento (latência) | imagens, vídeos, arquivos | [[wiki/concepts/cdn]], [[wiki/concepts/amazon-s3]] |
| Cache | carga no banco e latência de leitura | dado muito lido e que muda pouco (TTL, invalidação no write) | [[wiki/concepts/cache]], [[wiki/concepts/redis]] |
| Rate limiter | spam/abuso, DDoS aplicacional | endpoints públicos, principalmente de escrita (429) | [[wiki/concepts/rate-limiting]] |
| Fila + worker | trabalho lento no caminho da requisição; picos | resposta não precisa ser síncrona | [[wiki/concepts/filas-e-workers]], [[wiki/concepts/processamento-assincrono]] |
| Banco (SQL/NoSQL) | persistência, conforme padrão de leitura/escrita | sempre; escolha depende do acesso | [[wiki/concepts/postgresql]] |
| Réplicas de leitura / sharding | leitura/escrita além de um nó | leitura pesada → réplicas; depois, particionar | [[wiki/concepts/read-replicas]], [[wiki/concepts/sharding]] |

## Como usar

Escolher o bloco pelo [[wiki/concepts/gargalo]] observado, não pelo catálogo, e registrar o trade-off (latência, consistência, resiliência, custo). Aplicação incremental em [[wiki/concepts/design-em-camadas]].

## Nota de calibração

`[skill: tech-mentor-system-design]` A skill lista ainda blocos que o vídeo não cita: API gateway, service discovery, [[wiki/concepts/consistent-hashing]], particionamento de mensagens, health checks. A lista do vídeo é introdutória, não exaustiva.

## Key sources

- [[wiki/sources/como-estudar-system-design-building-blocks-instagram-simplificado]] — catálogo de 7 blocos (LB, rate limiter, cache, fila, database, CDN, sharding) com problema/quando usar/decisão no caso Instagram simplificado
