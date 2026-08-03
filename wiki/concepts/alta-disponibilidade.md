---
type: concept
title: "Alta Disponibilidade"
aliases: ["HA", "High Availability", "Alta Disponibilidade Cloud"]
date_created: 2026-05-06
date_updated: 2026-08-03
source_count: 6
tags: ["alta-disponibilidade", "resiliência", "aws", "arquitetura", "sre"]
skill: tech-mentor-infra
status: stub
---

# Alta Disponibilidade (HA)

Propriedade de um sistema de permanecer operacional por uma porcentagem definida do tempo, mesmo diante de falhas de componentes. Em cloud, é implementada através de redundância geográfica em múltiplas [[zona-de-disponibilidade|AZs]] e [[regiao-aws|Regiões]].

## Níveis de Disponibilidade AWS

| Nível | Abordagem | Downtime/ano |
|---|---|---|
| Single AZ | Sem redundância | Sem SLA |
| Multi-AZ | 2-3 AZs na mesma região | ~4 min (99,999%) |
| Multi-Region | Regiões distintas | Segundos (99,9999%+) |

## Padrão Multi-AZ (mínimo para produção)

```
Load Balancer (Regional)
├── AZ-a: App + DB primary
├── AZ-b: App + DB standby (failover automático)
└── AZ-c: App + DB standby (failover automático)
```

Serviços gerenciados da AWS (RDS Multi-AZ, Aurora, ElastiCache) fazem o failover automaticamente em < 60s.

## HA vs. Disaster Recovery (DR)

| | Alta Disponibilidade | Disaster Recovery |
|---|---|---|
| Escopo | Falha de componente/AZ | Falha de região inteira |
| RTO | Segundos a minutos | Minutos a horas |
| Custo | Moderado (2-3x por AZ) | Alto (infra duplicada em 2ª região) |
| Automação | Automático (gerenciado) | Geralmente manual ou semi-auto |

Os valores de RTO nessa tabela não são metas soltas — são os indicadores formais [[wiki/concepts/rto]] (tempo de recuperação) e [[wiki/concepts/rpo]] (dado tolerável de perda), que devem ser definidos a partir do negócio *antes* de escolher entre HA e DR, não depois. Ver [[wiki/sources/rto-rpo-recovery-time-point-objective]]: a arquitetura escolhida impõe um piso de RTO/RPO que pode ser incompatível com o que o negócio tolera (ex.: um sistema financeiro não tolera RPO > 0, o que descarta arquiteturas com backup meramente periódico).

## Relação com a Infraestrutura AWS

O design com mínimo de **3 AZs por região** existe especificamente para suportar HA: qualquer serviço que distribua carga entre as 3 AZs sobrevive à perda de 1 AZ sem impacto no SLA.

## Alta Disponibilidade como Característica Definidora de Large Scale

[[wiki/sources/large-scale-vs-complex-architecture]] trata a necessidade de alta disponibilidade como a característica que define [[wiki/concepts/large-scale-architecture]] — sistemas com picos de tráfego (bancos, lojas virtuais, startups em crescimento) precisam dela por natureza, independente de a arquitetura ser complexa ou não.

## HA (Ativo-Passivo) vs. Tolerância a Falha (Ativo-Ativo)

[[wiki/concepts/tolerancia-a-falha]] é uma propriedade distinta e mais forte que HA, frequentemente confundida com ela. Nos exemplos didáticos de [[wiki/sources/ha-vs-ft-alta-disponibilidade-tolerancia-a-falha]]: HA usa topologia **ativo-passivo** — banco primário/secundário com failover, que gera uma janela de indisponibilidade durante o switch de carga; Tolerância a Falha usa topologia **ativo-ativo** — nós idênticos já servindo tráfego em paralelo, sem janela perceptível de failover porque não há promoção a fazer. O eixo ativo-passivo vs. ativo-ativo é ortogonal ao eixo Multi-AZ vs. Multi-Region (HA vs. DR) já documentado acima — o primeiro trata de *como* os nós respondem à falha, o segundo trata de *onde* os nós estão geograficamente.

## Disponibilidade como Capacidade de Recurso, Não Só Uptime

Framing complementar (mais amplo que redundância multi-AZ acima): disponibilidade não é apenas "está no ar ou não" — é ter CPU e memória suficientes para atender o usuário no momento em que ele precisa. Uma instância *up* mas sem headroom de recurso nega disponibilidade ao usuário do mesmo jeito que uma instância derrubada. Isso liga HA diretamente ao [[wiki/concepts/planejamento-de-capacidade]], não só à topologia de AZs/regiões.

## Key Sources

- [[wiki/sources/aws-infraestrutura-global]]
- [[wiki/sources/10-conceitos-fundamentais-backend]] — framing didático agnóstico de cloud: disponibilidade como "continuar rodando mesmo quando acontecem falhas", via load balancer que não manda tráfego a instância travada e deploy que não derruba todas as máquinas ao mesmo tempo
- [[wiki/sources/large-scale-vs-complex-architecture]] — alta disponibilidade como traço definidor de large scale architecture, distinto do eixo de complexidade
- [[wiki/sources/sre-capacidade-observabilidade-confiabilidade-custo]] — disponibilidade redefinida como ter recurso (CPU/memória) suficiente para o usuário, não só uptime
- [[wiki/sources/ha-vs-ft-alta-disponibilidade-tolerancia-a-falha]] — distinção HA (ativo-passivo, com janela de failover) vs. Tolerância a Falha (ativo-ativo, sem janela perceptível)
- [[wiki/sources/rto-rpo-recovery-time-point-objective]] — RTO/RPO como indicadores formais de cenário de desastre que devem ser definidos a partir do negócio antes de escolher entre HA e DR
