---
type: concept
title: "Monorepo com Libs/Packages (Frontend)"
aliases: ["monorepo frontend", "libs de monorepo", "feature packages monorepo"]
date_created: 2026-07-27
date_updated: 2026-07-27
source_count: 1
tags: [frontend, monorepo, nx, arquitetura, libs]
skill: tech-mentor-frontend
status: stub
---

# Monorepo com Libs/Packages (Frontend)

Estrutura em que um repositório único hospeda múltiplos `apps/` (ex.: `web`, `admin`, `mobile`) que consomem `packages/`/`libs/` compartilhados (design system, utils, design tokens) como se fossem dependências instaláveis, sem sair do repositório. Ferramentas como Nx geram e versionam essas libs internamente.

## Regra de Ouro

Apps importam de packages; packages nunca importam de apps — a dependência flui numa via só (ver `references/frontend-architecture.md` da skill `tech-mentor-frontend`). O mesmo princípio aparece em [[wiki/concepts/microfrontend-baseado-em-rotas]]: o que era pasta compartilhada dentro de um monolito modular vira lib instalável do monorepo, permitindo que um grafo de dependências propague updates ("atualizei um pacote → atualizem todos os locais que dependem disso") sem o custo de coordenar N repositórios separados.

## Papel na Escala de Complexidade Arquitetural

É a peça que permite ao [[wiki/concepts/microfrontend-baseado-em-rotas|microfrontend baseado em rotas]] entregar builds/deploys independentes por módulo sem herdar a fragmentação de governança e versionamento dos [[wiki/concepts/microfrontends-parciais|microfrontends parciais/polirrepo]] — o versionamento continua centralizado num único grafo de dependências, em vez de exigir bump manual repo a repo.

## Key Sources

- [[wiki/sources/arquitetura-frontend-microfrontends-monolito-modular-vertical-slice]] — libs de monorepo (ex. Nx) como substituto de pasta compartilhada na transição de monolito modular para microfrontend baseado em rotas
