---
type: concept
title: "RTO — Recovery Time Objective"
aliases: ["RTO", "Recovery Time Objective", "tempo de recuperação"]
date_created: 2026-08-03
date_updated: 2026-08-03
source_count: 1
tags: ["rto", "disaster-recovery", "confiabilidade", "arquitetura", "infra"]
skill: tech-mentor-infra
status: stub
---

# RTO — Recovery Time Objective

Quanto tempo um serviço pode ficar indisponível até ser restaurado após um desastre (queda total, corrupção de dados, região inteira fora do ar). É um indicador focado em **cenário de desastre** — distinto de disponibilidade contínua medida por [[wiki/concepts/sli|SLI]]/[[wiki/concepts/slo|SLO]].

## RTO é Imposto pela Arquitetura, Não Escolhido Livremente

O padrão arquitetural adotado define um piso estrutural de RTO possível — algumas arquiteturas simplesmente não conseguem restaurar em menos de uma janela mínima de tempo, independente de esforço operacional. Isso torna o RTO um **insumo de decisão arquitetural**, não uma meta definida depois que a arquitetura já existe: se o negócio exige RTO de minutos, arquiteturas com restore manual de banco inteiro estão descartadas de saída.

## RTO Precisa ser Confrontado com Custo de Downtime

Um RTO "aceitável" isolado do negócio não tem sentido. Exemplo didático: um site de vendas faturando ~$1.000/minuto perde diretamente esse valor por cada minuto de indisponibilidade — duas horas de RTO custam ~$120.000 em receita perdida, o que deveria pressionar a escolha por uma arquitetura de recuperação mais rápida (e mais cara). Ver [[wiki/concepts/finops]], que documenta o mesmo raciocínio de forma quantificada (loja fora do ar por 1h perdendo R$1 milhão) — RTO alto sem justificativa de negócio é, na prática, uma decisão de custo disfarçada de decisão técnica.

## RTO por Tier (Referência de Mercado)

Prática comum em ambientes com múltiplos serviços de criticidade distinta (ex. Kubernetes com Velero/Kasten): definir RTO diferente por tier, não um valor único para todo o sistema.

| Tier | RTO típico | Estratégia |
|---|---|---|
| Crítico (pagamentos, autenticação) | ~30min | Active-active cross-region |
| Importante (API principal) | ~2h | Warm standby cross-region |
| Não-crítico (relatórios, jobs) | ~8h | Cold backup |

## Relação com Outros Conceitos

- [[wiki/concepts/rpo]] — par indissociável: RTO mede tempo de recuperação, RPO mede dado perdido; juntos definem a arquitetura de recuperação necessária.
- [[wiki/concepts/alta-disponibilidade]] — HA reduz a *frequência* de eventos que acionam RTO (falha de componente/AZ já é absorvida automaticamente); RTO entra em jogo no cenário mais severo de Disaster Recovery (falha de região inteira), onde a tabela HA vs. DR já registra RTO de "minutos a horas".
- [[wiki/concepts/sre]] — confiabilidade como guarda-chuva inclui disponibilidade de recursos; RTO/RPO são os indicadores concretos do pior caso desse guarda-chuva (desastre), enquanto SLI/SLO/SLA cobrem o caso contínuo.

## Key Sources

- [[wiki/sources/rto-rpo-recovery-time-point-objective]]
