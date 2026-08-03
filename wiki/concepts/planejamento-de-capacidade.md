---
type: concept
title: "Planejamento de Capacidade"
aliases: ["capacity planning", "planejamento de capacidade", "capacidade de infraestrutura"]
date_created: 2026-08-03
date_updated: 2026-08-03
source_count: 1
tags: [capacity-planning, sre, infraestrutura, observabilidade, finops]
skill: tech-mentor-infra
status: stub
---

# Planejamento de Capacidade

Estimar os recursos de infraestrutura (CPU, memória, storage, IOPS, conexões) necessários para suportar o crescimento futuro de tráfego, sem sobre nem sub-provisionar.

## De Onde Vêm os Dados

O planejamento de capacidade não é adivinhação — ele se alimenta diretamente dos dados coletados pela [[wiki/concepts/observabilidade]]: RPS atual e sua taxa de crescimento, latência P50/P95/P99, utilização de CPU/memória em pico, e tamanho/crescimento do banco de dados. Sem observabilidade madura, capacity planning vira estimativa às cegas.

## Back-of-Envelope (regra prática)

```
Serviço atual: 500 RPS com 2 instâncias (CPU em pico: 60%)
Headroom desejado: 40% CPU livre
Crescimento esperado: 3x em 12 meses → 1500 RPS

Instâncias necessárias ≈ 2 * (1500/500) * (1/0.6) ≈ 10 instâncias
```

Banco de dados: storage = tamanho atual + (crescimento mensal × 12) × 1.5 de margem; monitorar IOPS em pico; se `max_connections` estourar 80% regularmente, adicionar pooler (ex. PgBouncer) ou subir de instância.

## Disponibilidade como Função de Capacidade, Não Só de Uptime

Um ponto frequentemente esquecido: disponibilidade não é apenas "o serviço está no ar" — é ter CPU/memória suficientes para atender a carga real do usuário no momento. Uma instância *up* mas sem headroom de recurso efetivamente nega disponibilidade ao usuário do mesmo jeito que uma instância caída. Isso liga capacity planning diretamente a [[wiki/concepts/alta-disponibilidade]] e a [[wiki/concepts/robustez-de-sistemas]].

## Otimização de Custo Não é Só Cortar Gasto

Capacity planning e [[wiki/concepts/finops]] se cruzam de um jeito contra-intuitivo: às vezes a otimização de custo correta é *aumentar* recurso. Exemplo: uma loja virtual fora do ar por 1h perde R$ 1 milhão; dobrar de 10 para 20 servidores custa R$ 100 mil a mais — o resultado líquido é um ganho de R$ 900 mil (perda evitada − custo extra), não um gasto adicional de R$ 100 mil. A métrica certa é "quanto deixei de perder", não "quanto gastei a mais".

## Load Testing Antes de Eventos

Antes de picos previsíveis (Black Friday, lançamento viral), simular a carga esperada com ferramentas como k6, Gatling ou Locust — validar que o plano de capacidade aguenta o pico antes que o pico aconteça de verdade.

## Key Sources

- [[wiki/sources/sre-capacidade-observabilidade-confiabilidade-custo]]
