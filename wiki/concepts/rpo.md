---
type: concept
title: "RPO — Recovery Point Objective"
aliases: ["RPO", "Recovery Point Objective", "ponto de recuperação"]
date_created: 2026-08-03
date_updated: 2026-08-03
source_count: 1
tags: ["rpo", "disaster-recovery", "confiabilidade", "arquitetura", "infra"]
skill: tech-mentor-infra
status: stub
---

# RPO — Recovery Point Objective

Quanto dado um sistema pode perder após um desastre, medido pela distância até o último backup (ou ponto de replicação) válido. É um indicador focado em **cenário de desastre** — não em disponibilidade contínua.

## RPO Efetivo é a Distância até o Último Backup Válido

RPO não é um número abstrato definido de antemão e sim o resultado direto da frequência de backup: se o incidente ocorre ao meio-dia e o último backup válido foi às 10h, o RPO efetivo daquele incidente é de duas horas de dados perdidos — não importa qual era a "meta" declarada.

## Tolerância a RPO é Estritamente Dependente do Domínio

Não existe um valor de RPO "correto" universal — a tolerância depende do que o dado representa para o negócio:

| Domínio | Tolerância a perda de dado | Por quê |
|---|---|---|
| Sistema financeiro | Zero — RPO ≈ 0 | Ambiguidade sobre quem transferiu o quê é inaceitável |
| E-commerce (pedidos/vendas) | Zero para vendas já registradas | Perder uma compra confirmada é falha visível e direta ao cliente |
| Microsserviço de catálogo (cadastro de produto) | Pode tolerar horas, dependendo do caso | Afeta o negócio, mas de forma absorvível — não há transação financeira em jogo |

Essa tabela é o argumento central da fonte: o mesmo sistema (um e-commerce) pode ter RPOs radicalmente diferentes por microsserviço, porque a criticidade do dado — não a arquitetura geral do produto — é o que define a exigência.

## RPO Define a Estratégia de Backup/Replicação Necessária

Um RPO próximo de zero exige replicação síncrona ou contínua (não apenas backups periódicos); um RPO de horas comporta backup frequente porém assíncrono. Isso amarra RPO diretamente à escolha de [[wiki/concepts/replicacao-de-banco|estratégia de replicação]] — decidir o RPO antes da arquitetura é o que evita descobrir tarde demais que o mecanismo de backup escolhido não sustenta a tolerância real do negócio.

## RPO por Tier (Referência de Mercado)

Assim como RTO, é comum segmentar RPO por criticidade de serviço em vez de aplicar um valor único:

| Tier | RPO típico | Mecanismo |
|---|---|---|
| Crítico (pagamentos, autenticação) | ~15min | Backup frequente + snapshot |
| Importante (API principal) | ~1h | Backup periódico |
| Não-crítico (relatórios, jobs) | ~24h | Cold backup |

## Relação com Outros Conceitos

- [[wiki/concepts/rto]] — par indissociável: RPO mede dado perdido, RTO mede tempo até restaurar o serviço; a arquitetura de recuperação precisa satisfazer os dois simultaneamente.
- [[wiki/concepts/replicacao-de-banco]] — o mecanismo concreto que determina o RPO alcançável (síncrona vs. assíncrona, frequência de snapshot).
- [[wiki/concepts/alta-disponibilidade]] — HA (failover automático dentro da mesma região) normalmente já opera com RPO próximo de zero por replicação síncrona; RPO como indicador explícito importa mais no cenário de Disaster Recovery (região inteira), onde a replicação costuma ser assíncrona por distância geográfica.

## Key Sources

- [[wiki/sources/rto-rpo-recovery-time-point-objective]]
