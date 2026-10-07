---
type: concept
title: "Diagnóstico Antes de Reestruturar"
aliases: ["achar o gargalo antes de migrar", "investigar antes de quebrar o monolito"]
date_created: 2026-10-07
date_updated: 2026-10-07
source_count: 1
tags: [arquitetura, performance, observabilidade, microsservicos, gargalo]
skill: tech-mentor-system-design
status: draft
---

# Diagnóstico Antes de Reestruturar

Antes de mudar a arquitetura por causa de lentidão ou dificuldade de manutenção, **localizar a causa**. No exemplo de [[wiki/sources/decisoes-de-arquitetura-tradeoffs-e-contexto-bernardo-lobato]] (monolito, ~20.000 acessos/dia), o mesmo sintoma tem causas com remédios distintos:

| Causa provável | Remédio mais barato | Quebrar em serviços ajuda? |
|---|---|---|
| Consulta pesada no banco | índice, reescrever consulta, mudar estrutura ([[wiki/concepts/database-index]]) | não; soma complexidade |
| Trabalho pesado síncrono na requisição | fila / assíncrono ([[wiki/concepts/filas-e-workers]]) | não necessariamente |
| Módulos acoplados (mudança espalhada) | redefinir fronteiras e responsabilidades ([[wiki/concepts/acoplamento]], [[wiki/concepts/monolito-modular]]) | só se as fronteiras forem corrigidas antes |
| Um componente com carga desproporcional | isolar e escalar à parte ([[wiki/concepts/escalabilidade-independente]]) | sim, é o caso clássico |

Ferramentas citadas: [[wiki/entities/opentelemetry]], Jaeger, Zipkin e APM (Datadog, New Relic, Dynatrace) para requisições; [[wiki/entities/prometheus]] e Grafana ([[wiki/entities/grafana-labs]]) ou métricas da nuvem para CPU/memória/disco/rede; `EXPLAIN`/`ANALYZE` para SQL. Objetivo: saber se o problema está na aplicação, no banco, na infra ou numa operação ineficiente, **sem** ligar tudo ao mesmo tempo. Ver [[wiki/concepts/gargalo]], [[wiki/concepts/observabilidade]], [[wiki/concepts/distributed-tracing]], [[wiki/concepts/over-engineering]].

## Key sources

- [[wiki/sources/decisoes-de-arquitetura-tradeoffs-e-contexto-bernardo-lobato]]
