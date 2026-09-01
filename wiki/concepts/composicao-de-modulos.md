---
type: concept
title: "Composição de Módulos (Module Composition)"
aliases: ["module composition", "composição de módulos", "compor módulos de domínio", "arquitetura modular"]
date_created: 2026-09-01
date_updated: 2026-09-01
source_count: 3
tags: [module-composition, monorepo, monolito-modular, nx, arquitetura, backend]
skill: tech-mentor-backend
status: draft
---

# Composição de Módulos (Module Composition)

Estratégia de monorepo em que módulos de domínio (`packages/`) — que não sabem nada sobre HTTP ou runtime, só contêm lógica de domínio — são combinados em diferentes "apps" de bootstrap (`apps/`), cada uma inicializando um subconjunto arbitrário de módulos. O mesmo módulo `billing` pode ser carregado sozinho por um app `billing-api` (rodando isolado, como se fosse um microsserviço) ou junto com `content` e `identity` num app "monolito" (rodando tudo agregado). A composição acontece na camada de bootstrap, não no módulo de domínio em si — o módulo não sabe, e não precisa saber, como vai rodar.

## Por que existe

É o passo seguinte ao [[wiki/concepts/monolito-modular]] clássico. No monolito modular clássico, módulos com fronteiras explícitas ainda compartilham o mesmo codebase e o mesmo processo/deploy — uma mudança num módulo pode forçar redeploy de outro processo que nem depende diretamente dele (ex.: mudar `identity` força redeploy de um worker que só usa `content`). Module composition resolve isso restruturando o repositório em `packages/` (módulos de domínio puros) + `apps/` (bootstraps), permitindo compor "infinitas" combinações de módulos a partir de um único codebase — obtendo, na prática, o equivalente a múltiplos microsserviços sem pagar o preço de múltiplos repositórios, pipelines e infraestrutura separada. Ver [[wiki/sources/evoluir-software-sem-pagar-preco-de-microsservicos]].

## Mecanismo Concreto (NestJS + NX)

```
packages/
  billing/     ← módulo de domínio puro (sem HTTP)
  content/
  identity/
  shared/      ← infraestrutura compartilhada
apps/
  billing-api/     ← main.ts que carrega só billing + expõe API
  monolith/        ← main.ts que carrega content + identity juntos
```

Cada app é só um ponto de bootstrap: carrega o(s) módulo(s) de domínio que escolher e expõe uma API sobre eles. A necessidade de escala é tratada separadamente da necessidade de organização de código — quando um módulo precisa escalar individualmente, cria-se (ou já existe) um app dedicado só para ele.

## Ferramental

Depende de um build system de monorepo com detecção de "affected" (NX ou Turborepo) para não pagar o custo de CI lento à medida que o repositório cresce — `nx affected --target=test` roda pipeline só para o que mudou. Ver [[wiki/concepts/monorepo-backend]].

## Nomenclatura Alternativa: "Arquitetura Modular"

[[wiki/sources/os-10-principios-arquitetura-modular-valdemar-neto]] descreve o mesmo mecanismo (packages/apps recombináveis via monorepo) sob o nome **[[wiki/concepts/arquitetura-modular|arquitetura modular]]**, em contraste explícito com "monolito modular" (um único deploy fixo). Duas fontes independentes chegaram ao mesmo padrão técnico com termos próprios diferentes — tratado aqui como sinônimo, não como conceito novo. Essa fonte acrescenta um argumento específico: microsserviços não compõem (não cabem vários numa mesma app/processo), o que torna a componibilidade de packages/apps uma vantagem estrutural que microsserviços perdem.

## Diferença de Serviços de Domínio

[[wiki/concepts/servicos-de-dominio]] já quebra um monolito grande em vários monolitos menores por domínio — mas cada um deles ainda é uma unidade fixa de deploy. Module composition vai além: a mesma base de módulos pode ser recombinada em diferentes apps sem duplicar código, dando granularidade ajustável sem multiplicar repositórios.

## Que Tipo de Módulo Vira `packages/`

[[wiki/sources/tres-tipos-de-modulos-arquitetura-modular-valdemar-neto]] esclarece qual granularidade de módulo é a candidata natural a virar um pacote reusável em `packages/`: módulos de domínio (billing, content, identity) e módulos de infraestrutura pura (HTTP, logger, persistência) — não módulos de feature, que o autor evita por perderem o bounded context e serem granulares demais para compor de forma limpa. Ver [[wiki/concepts/tipos-de-modulos]].

## Key Sources

- [[wiki/sources/evoluir-software-sem-pagar-preco-de-microsservicos]] — origem do termo nesta wiki; demonstração concreta em NestJS/NX (`billing-api` vs. app "monolito" agregando `content`+`identity`)
- [[wiki/sources/os-10-principios-arquitetura-modular-valdemar-neto]] — mesmo mecanismo sob o nome "arquitetura modular"; argumento de que microsserviços não compõem
- [[wiki/sources/tres-tipos-de-modulos-arquitetura-modular-valdemar-neto]] — módulos de domínio e infraestrutura pura como candidatos naturais a `packages/`; módulos de feature desaconselhados por perderem o bounded context
