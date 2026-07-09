---
type: concept
title: "A/B Testing Deployment"
aliases: ["a/b deployment", "a/b test deploy", "deploy ab"]
date_created: 2026-07-09
date_updated: 2026-07-09
source_count: 1
tags: [devops, deploy, cicd, produto, experimentacao, infra]
skill: tech-mentor-infra
status: stub
---

# A/B Testing Deployment

Mecanicamente quase idêntico ao [[concepts/canary-release]] — um percentual dos usuários vê a versão A, outro percentual vê a versão B — mas com objetivo diferente: **validar uma hipótese de negócio**, não reduzir risco técnico.

## Diferença central com Canary

| | Canary | A/B |
|---|---|---|
| Pergunta | "A v2 quebra alguma coisa?" | "A v2 performa melhor no negócio?" |
| Métrica | Error rate, latência, saúde técnica | Conversão, receita, engajamento |
| Decisão se OK | Aumenta gradualmente até 100% | Migra 100% para a variante vencedora |
| Decisão se ruim | Rollback técnico | Descarta a hipótese, sem rollback "de bug" |

Exemplo: testar se um checkout novo vende mais que o antigo. Se vender mais, migra todo o tráfego pra versão nova; se não vender mais, a versão nova é descartada — não porque quebrou, mas porque a hipótese de negócio não se confirmou.

## Relação com Feature Flags

Na prática, A/B testing quase sempre é implementado via [[concepts/feature-flags]] (categoria "Experiment toggle" no framework de Martin Fowler), não necessariamente via duas instâncias de infraestrutura separadas — mais fácil de segmentar por atributo do usuário (país, plano, cohort) do que por split de tráfego bruto no load balancer.

## Key Sources

- [[sources/tipos-de-deploy]]
