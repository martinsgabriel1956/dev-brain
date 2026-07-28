---
type: concept
title: "DORA Metrics"
aliases: ["DORA", "DevOps Research and Assessment", "Accelerate"]
date_created: 2026-07-09
date_updated: 2026-07-28
source_count: 3
tags: [devops, metrics, cicd, qualidade, engineering-culture, tech-debt]
skill: tech-mentor-leadership
status: stub
---

# DORA Metrics

Corpo de pesquisa do **DevOps Research and Assessment** (DORA), publicado no livro *Accelerate* (Forsgren, Humble, Kim), que identificou quatro métricas empiricamente correlacionadas com alta performance de engenharia:

- **Deployment Frequency** — com que frequência o time faz deploy para produção
- **Lead Time for Changes** — tempo do primeiro commit até o código estar em produção
- **Change Failure Rate** — percentual de deploys que causam degradação e exigem hotfix/rollback
- **Mean Time to Recovery (MTTR)** — tempo médio para restaurar o serviço após incidente

## Faixas de referência (Elite/Alto/Médio/Baixo)

| Métrica | Elite | Baixo |
|---|---|---|
| Deployment Frequency | múltiplas vezes/dia | < 1x/mês |
| Lead Time for Changes | < 1 hora | 1–6 meses |
| Change Failure Rate | 0–15% | > 45% |
| MTTR | < 1 hora | > 1 semana |

## O achado central: velocidade e qualidade não competem

O resultado mais citado da pesquisa contraria a intuição do **"triângulo de ferro"** (rápido, barato, bom — escolha dois): equipes que entregam com mais frequência e menor lead time *também* apresentam menor change failure rate e menor MTTR. Velocidade e qualidade se correlacionam positivamente em software, não competem — ao contrário do que a intuição de "ir rápido = quebrar mais" sugere.

Isso é consistente com a natureza incremental do software: entregar em lotes pequenos e frequentes reduz o risco por deploy (menos mudança acumulada), permite validar hipóteses de produto mais cedo, e força o time a manter o sistema sempre em estado implantável — o que por si só exige testes, pipelines confiáveis e arquitetura fácil de mudar.

## Como usar (e como não usar)

Não usar para comparar times entre si (contextos diferentes) nem para avaliar performance individual. Usar como tendência do próprio time ao longo do tempo, e para identificar gargalos: deployment frequency baixa aponta para onde está o bloqueio no processo de entrega.

## Conexões

- [[over-engineering]] — o "triângulo de ferro" é o mito que a pesquisa DORA refuta; medo de quebrar leva a portões de deploy excessivos (PRs grandes, muitas aprovações), que por sua vez pioram tanto a velocidade quanto a qualidade
- [[ci-cd]] — a prática que operacionaliza deploys frequentes e lead time curto
- [[tdd]] — testes automatizados são pré-condição para manter o sistema sempre implantável
- [[zero-downtime-deploy]] — reduz o custo/risco percebido de cada deploy, incentivando frequência maior
- [[wiki/concepts/goodharts-law]] — a mesma regra de "não usar para comparar times nem avaliar indivíduos" é uma defesa contra o mesmo risco que corrompe [[wiki/concepts/story-points]] quando forçados como meta: a métrica vira alvo e para de medir o que deveria medir

## Lead Time como Sinal Indireto de Dívida Técnica

[[wiki/sources/tech-debt-guia-completo-gestao-metricas]] usa o Lead Time for Changes como proxy de dívida técnica não medida diretamente: se o tempo entre commit e produção para o mesmo tipo de feature cresce ao longo do tempo, é sinal de que dívida técnica está entupindo o pipeline — e isso costuma acontecer gradualmente, sem que o time perceba, até que alguém compare "isso costumava levar 2 dias, agora leva uma semana". Ver [[wiki/concepts/hotspot-analysis]] para as métricas complementares (complexidade ciclomática, code churn) usadas para localizar *onde* no código está a causa desse alongamento.

## Key Sources

- [[wiki/sources/como-evitar-over-engineering-david-farley]]
- [[wiki/sources/tech-debt-guia-completo-gestao-metricas]] — lead time crescente como proxy indireto de dívida técnica acumulada
