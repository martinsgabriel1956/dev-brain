---
type: concept
title: "Git Flow"
aliases: ["gitflow", "git-flow", "modelo de branching de Vincent Driessen", "develop/release/hotfix branches"]
date_created: 2026-08-11
date_updated: 2026-08-11
source_count: 1
tags: [git, branching, processo, versionamento, cargo-cult, tech-mentor-leadership]
skill: tech-mentor-leadership
status: stub
---

# Git Flow

Modelo de branching publicado por Vincent Driessen em 2010 ("A successful Git branching model"), baseado em **múltiplas branches de vida longa e efêmeras com papéis fixos**: `main` (produção), `develop` (integração), e branches temporárias de `feature/*`, `release/*` e `hotfix/*`, com regras rígidas de origem e destino de merge para cada uma.

## A crítica: padrão de influenciador, não de indústria

[[wiki/entities/lucas-montano]], em [[wiki/sources/git-flow-farsa-solucao-maturidade-rebase-lucas-montano]], chama o Git Flow de **"uma das maiores falácias da bolha dev"** e lança a provocação: *"me diga uma grande empresa que está usando Git Flow"*. O argumento é que o modelo foi **elevado à estátua de "padrão industrial" por influenciadores** ("modificadores de cultura") sem que a indústria de fato o adotasse — mesmo mecanismo de [[wiki/concepts/cargo-cult-tecnologico|cargo cult tecnológico]] que ele identifica em squads-do-Spotify, no movimento ágil e em orientação a objetos: uma ideia de um post/palestra abraçada "como um gospel".

O peso da crítica recai sobre **times pequenos**, onde a burocracia de Git Flow (várias branches de vida longa, merges cerimoniais entre `develop`/`release`/`hotfix`) é custo puro: "muito mais contras do que prós". A própria nota de Driessen dos anos posteriores reconhece que o modelo foi pensado para software versionado com múltiplas versões em produção e é inadequado para produtos web de deploy contínuo — onde [[wiki/concepts/trunk-based-development|trunk-based development]] é a recomendação corrente.

## A alternativa proposta

Montano contrapõe um fluxo próximo de trunk-based — **só a `main` como fonte de verdade**, sem `develop` de vida longa, integração por [[wiki/concepts/rebase-vs-merge|rebase]] gerando *fast-forward merges* limpos, e CI como [[wiki/concepts/ci-cd|single command deploy]] frictionless. Detalhes e trade-offs em [[wiki/concepts/trunk-based-development]]. Ressalva central: **não existe processo universal** — a escolha depende do porte e da natureza da empresa, e o profissional maduro se adapta ao processo existente (ver [[wiki/concepts/maturidade-tecnica]]).

## Ver também

- [[wiki/concepts/trunk-based-development]] — o modelo contraposto (branch única de vida longa)
- [[wiki/concepts/rebase-vs-merge]] — a mecânica de integração usada na alternativa
- [[wiki/concepts/cargo-cult-tecnologico]] — o mecanismo por trás da adoção acrítica de Git Flow
- [[wiki/concepts/maturidade-tecnica]] — por que "não existe resposta final" para processo de Git

## Key Sources

- [[wiki/sources/git-flow-farsa-solucao-maturidade-rebase-lucas-montano]] — a crítica ao Git Flow como cargo cult e a proposta de um fluxo só-main com rebase para times pequenos
