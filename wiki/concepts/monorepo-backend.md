---
type: concept
title: "Monorepo Backend (apps/ + packages/)"
aliases: ["monorepo backend", "nx backend", "apps e packages"]
date_created: 2026-09-01
date_updated: 2026-09-01
source_count: 3
tags: [backend, monorepo, nx, arquitetura, composicao-de-modulos]
skill: tech-mentor-backend
status: stub
---

# Monorepo Backend (apps/ + packages/)

Estrutura de repositório único onde `packages/` (ou `libs/`) hospeda módulos de domínio/infraestrutura reutilizáveis e `apps/` hospeda múltiplos pontos de bootstrap/deploy que consomem esses módulos em diferentes combinações — o equivalente, no backend, ao padrão já documentado para frontend em [[wiki/concepts/monorepo-frontend]]. É a base estrutural sobre a qual [[wiki/concepts/composicao-de-modulos]] se apoia.

## Ferramental

NX (com `nx affected` para rodar build/test/lint só no que mudou) ou Turborepo — ver `references/monorepo-backend.md` da skill `tech-mentor-backend` para configuração detalhada (`nx.json`, `turbo.json`, Docker multi-stage por app, versionamento de libs internas via Changesets ou workspace protocols). [[wiki/sources/os-10-principios-arquitetura-modular-valdemar-neto]] cita também **Bazel** e **Maven** como alternativas comuns em ecossistema Java, sem demonstração prática nesta fonte (só o exemplo NestJS/NX é aprofundado).

## Regra de Ouro

Apps importam de packages; packages nunca importam de apps — mesma regra já documentada em [[wiki/concepts/monorepo-frontend]]. No caso backend, um módulo de domínio dentro de `packages/` não sabe nada sobre HTTP ou como vai ser exposto; quem decide isso é o app que o importa.

## Por que não é sempre a resposta

Monorepo grande pode ficar lento para operar (checkout, CI) à medida que cresce — mitigado por ferramental de "affected" moderno, mas não elimina o limite: quando a empresa cresce muito (múltiplos times, múltiplos fusos horários), pode valer migrar para polirrepo/microsserviços de fato. Ver [[wiki/concepts/microsservicos]] e [[wiki/concepts/monolith-first]] para os critérios de quando essa extração vale a pena.

## Key Sources

- [[wiki/sources/evoluir-software-sem-pagar-preco-de-microsservicos]] — demonstração concreta em NestJS/NX de `apps/` (billing-api, monolito) consumindo `packages/` (billing, content, identity)
- [[wiki/sources/os-10-principios-arquitetura-modular-valdemar-neto]] — Bazel e Maven citados como alternativas de ferramental (ecossistema Java); mesmo padrão nomeado "arquitetura modular"
- [[wiki/sources/tres-tipos-de-modulos-arquitetura-modular-valdemar-neto]] — critério de que módulos de domínio e de infraestrutura pura (não de feature) são os candidatos naturais a virar pacotes reusáveis nesse tipo de repositório
