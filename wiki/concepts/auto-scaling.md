---
type: concept
title: "Auto Scaling"
aliases: ["autoscaling", "escalamento automático", "horizontal pod autoscaler", "HPA"]
date_created: 2026-06-26
date_updated: 2026-09-03
source_count: 5
tags: [system-design, escalabilidade, cloud, infra, automatizacao, performance]
skill: tech-mentor-system-design
status: draft
---

# Auto Scaling

Mecanismo que **adiciona e remove instâncias de servidor automaticamente** em resposta a métricas de carga — sem intervenção manual. É a automação da [[escalabilidade-horizontal]].

## Como funciona

Você define **regras** baseadas em métricas:

```
CPU > 70% por 5 minutos  → adicionar 1 servidor
CPU < 30% por 10 minutos → remover 1 servidor
```

A ferramenta de auto scaling monitora as métricas, toma as decisões e provisiona/desprovisiona instâncias automaticamente.

## Exemplo prático — Black Friday

```
09:00 — carga normal   → 3 instâncias
10:00 — tráfego sobe   → auto scaling detecta CPU > 70%
10:05 — adiciona instância → 4 instâncias
11:00 — adiciona mais  → 6 instâncias
18:00 — tráfego cai    → auto scaling detecta CPU < 30%
18:10 — remove instância → 4 instâncias
21:00 — normaliza      → 3 instâncias
```

## Métricas comuns para trigger

| Métrica | Quando usar |
|---|---|
| **CPU** | Workload compute-bound (processamento) |
| **Memória** | Workload memory-bound |
| **Requisições por segundo** | Workload I/O-bound (APIs) |
| **Tamanho da fila** | Workloads assíncronos, workers de jobs |
| **Latência P99** | SLA-driven — escala antes de impactar usuários |

## Pré-requisito: servidores [[stateless]]

Auto scaling só funciona bem se novas instâncias podem atender qualquer requisição sem estado prévio. Se o servidor for stateful, escalar cria inconsistências.

## Ferramentas

- **AWS Auto Scaling Groups** — EC2 com regras de CloudWatch
- **Kubernetes HPA** (Horizontal Pod Autoscaler) — escala pods por CPU/memória/custom metrics
- **Kubernetes VPA** (Vertical Pod Autoscaler) — ajusta requests/limits de pods
- **Google Cloud MIG** (Managed Instance Groups)

## Abordagem preventiva vs reativa

| | Preventiva | Reativa |
|---|---|---|
| **Quando escala** | Antes do pico (scheduled scaling) | Após métricas dispararem |
| **Risco** | Custo extra de instâncias ociosas | Latência alta durante ramp-up |
| **Ideal para** | Picos previsíveis (Black Friday, horário comercial) | Carga imprevisível |

## Ressalva: "Monolito" Não É Sinônimo de "Servidor Único Sem Réplicas"

[[wiki/sources/arquitetura-monolitica-vantagens-desvantagens]] descreve auto scaling como "mais difícil" num [[wiki/concepts/monolito|monolito]], ilustrando com o processo manual de desligar/trocar tipo de instância/religar (escala **vertical**). Isso simplifica demais: um monolito escala **horizontalmente** como qualquer outra aplicação stateless — múltiplas réplicas idênticas atrás de um [[wiki/concepts/load-balancer]], com Auto Scaling Group. A limitação real que a fonte descreve é de single-server sem réplicas, não do estilo arquitetural monolítico em si — a confusão entre os dois é comum na prática (times pequenos rodando monolito numa única instância), mas não é uma restrição inerente ao monolito.

## Relação com outros conceitos

- [[escalabilidade-horizontal]] — auto scaling é a automação dela
- [[stateless]] — pré-requisito para que novas instâncias funcionem corretamente
- [[load-balancer]] — precisa detectar e registrar novas instâncias automaticamente
- [[gargalo]] — identificar o gargalo antes de configurar auto scaling evita escalar a camada errada

## AWS Auto Scaling Group (ASG) — Min/Desejado/Máximo

Na AWS, o ASG define três números: mínimo, desejado e máximo de instâncias [[wiki/concepts/ec2|EC2]]. Gatilho típico: CPU acima de ~70% escala para cima, abaixo escala para baixo. Sempre acoplado a um [[wiki/concepts/load-balancer|Application Load Balancer (ALB)]] na frente — o ALB distribui tráfego e faz health checks; instâncias que falham são removidas do pool automaticamente. Arquitetura clássica: ALB na frente, ASG atrás — tráfego sobe, ASG escala, ALB distribui; tráfego cai, ASG reduz. Ver [[wiki/sources/15-servicos-essenciais-aws-para-dominar-qualquer-arquitetura]].

## Key sources

- [[wiki/sources/escalabilidade-vertical-horizontal-system-design]]
- [[wiki/sources/15-servicos-essenciais-aws-para-dominar-qualquer-arquitetura]] — ASG com min/desejado/máximo sempre acoplado ao ALB, incluindo health checks e remoção automática de instâncias falhas
- [[wiki/sources/back-pressure-producer-consumer-filas-bounded-admission-control]] — auto scaling baseado no tamanho da fila como resposta a [[wiki/concepts/back-pressure]]; citado como viável mas mais difícil de configurar do que as alternativas mais baratas (poda de stale jobs, batching, admission control)
- [[wiki/sources/escalando-aplicacao-zero-a-um-milhao-usuarios-renato-augusto]] — motivação de negócio para elasticidade: pico sazonal de tráfego (Black Friday numa API de e-commerce) torna provisionamento manual impraticável (custo de esquecer desprovisionar vs. indisponibilidade por não provisionar a tempo)
- [[wiki/sources/arquitetura-monolitica-vantagens-desvantagens]] — descreve auto scaling como mais difícil em monolito, citando o processo manual de resize vertical (desligar/trocar tipo/religar); conflates monolito com single-server sem réplicas, ver ressalva acima
