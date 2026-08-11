---
type: concept
title: "Trunk-Based Development"
aliases: ["trunk based development", "desenvolvimento baseado em tronco", "só main", "single long-lived branch", "main como fonte de verdade"]
date_created: 2026-08-11
date_updated: 2026-08-11
source_count: 1
tags: [git, branching, processo, ci-cd, versionamento, times-pequenos, tech-mentor-leadership]
skill: tech-mentor-leadership
status: stub
---

# Trunk-Based Development

Modelo de branching em que existe **uma única branch de vida longa** (a `main`/`trunk`) como fonte de verdade, e as branches de feature são curtas e integradas de volta com frequência. É a contraposição direta ao [[wiki/concepts/git-flow]] (que mantém `develop`/`release`/`hotfix` de vida longa) e a base de fato dos pipelines de deploy contínuo.

## A variante de Lucas Montano (rebase-flow para times pequenos)

[[wiki/sources/git-flow-farsa-solucao-maturidade-rebase-lucas-montano]] descreve uma implementação concreta que funcionou por 4 anos (2020–2024) numa consultoria — mirando **times pequenos**, onde "burocracia é o problema". Quatro peças:

1. **Só a `main`** — nenhuma branch `dev`/`develop` de vida longa. Toda feature concluída entra na `main`; a versão na `main` pode ir a produção ou ficar em *staging* (um **ambiente**, não uma branch). Evita o trabalho extra de manter conflitos entre uma `dev` atrasada e uma `prod` que recebe hotfix.
2. **CI como [[wiki/concepts/ci-cd|single command deploy]] frictionless** — elimina o estado "código pronto mas não em produção".
3. **Um dono por entrega** — ownership centralizado que leva a feature à `main` e orquestra dependências.
4. **Integração por [[wiki/concepts/rebase-vs-merge|rebase]], não merge** — evita o "*subway train from hell*" (histórico de branching ilegível) e produz *fast-forward merges* limpos, com a ordem das entregas explícita.

## O trade-off: não escala

O ponto de maturidade da fonte é que **este fluxo não escala**. O rebase reescreve a branch da feature (se der ruim, perde-se a versão original) e resolve conflitos commit a commit — exige atenção e **ownership centralizado em uma pessoa**. Em time grande, centralizar o merge "vira uma loucura" — colide com o [[wiki/concepts/bus-factor|bus factor]] e a necessidade de substituibilidade. Daí a conclusão: bom para times pequenos, inadequado para grandes. IA reduz hoje o custo operacional do rebase, mas não a natureza do trade-off.

Trunk-based "puro" em escala costuma resolver isso de outra forma — commits diretos frequentes na trunk protegidos por CI e [[wiki/concepts/feature-flags|feature flags]], em vez de rebase centralizado de branches de feature (ex.: o caso Facebook em [[wiki/sources/rapid-release-at-massive-scale-facebook]]).

## Ver também

- [[wiki/concepts/git-flow]] — o modelo contraposto (múltiplas branches de vida longa)
- [[wiki/concepts/rebase-vs-merge]] — a mecânica de integração da variante de Montano
- [[wiki/concepts/ci-cd]] — o single command deploy que sustenta o fluxo
- [[wiki/concepts/atomic-commits]] — um-arquivo-um-commit torna os conflitos de rebase gerenciáveis
- [[wiki/concepts/maturidade-tecnica]] — por que a escolha do fluxo depende do contexto da empresa

## Key Sources

- [[wiki/sources/git-flow-farsa-solucao-maturidade-rebase-lucas-montano]] — variante rebase-flow só-main para times pequenos; por que não escala
