---
type: concept
title: "Monolito Modular (Frontend)"
aliases: ["arquitetura modular frontend", "modular monolith frontend", "fronteiras entre módulos"]
date_created: 2026-07-27
date_updated: 2026-08-10
source_count: 3
tags: [frontend, arquitetura, modularidade, monolito, module-boundaries]
skill: tech-mentor-frontend
status: stub
---

# Monolito Modular (Frontend)

Arquitetura frontend em que, em vez de organizar o código por camada técnica (`pages`/`components`/`services` — ver "Arquitetura em Camadas" abaixo), o código é quebrado em **módulos por domínio** dentro de um único build. Um módulo (ex.: "Alfa") contém os componentes que só dizem respeito a ele; alterar algo ali afeta apenas aquele escopo conhecido.

## Contraste com Arquitetura em Camadas

Arquitetura em camadas (a primeira que a maioria aprende) organiza por tipo técnico e não cria fronteira de domínio nenhuma: abrir uma pasta `components/` com 80 componentes não dá contexto sobre quantos locais uma mudança afeta, nem se ela pertence a um módulo específico ou a um caso de uso isolado — vira um problema de escala rapidamente.

## Fronteiras de Módulo Como Mecanismo de Escala de Time

O objetivo central é garantir atuação clara de escopo: um time pode ser dono de "Alfa e Pagamentos" porque essas são as fronteiras dele. Qualquer código genuinamente compartilhado passa a ser responsabilidade de um time de plataforma, e mudanças ali exigem review obrigatório para não quebrar consumidores existentes — o mesmo espírito dos Module Boundaries / Bounded Contexts descritos em `references/frontend-architecture.md` da skill `tech-mentor-frontend` (regra de dependência de uma via, Public API via `index.ts`, `dependency-cruiser` para enforçar).

## Ponto de Partida Correto

Monolito modular é descrito como a base sólida a partir da qual se decide, com necessidade real (não hype), evoluir para [[wiki/concepts/microfrontend-baseado-em-rotas]] — a transição é de baixo custo porque a estrutura de fronteiras já existe, só migrando de "pasta compartilhada" para "lib de monorepo" e de "módulo lógico" para "módulo com build/deploy próprio". Esse mesmo princípio de partida — extrair só quando necessário, não adiantar a complexidade — já está documentado do lado backend em [[wiki/concepts/microsservicos]] (monolito modular como ponto de partida correto para ~90% dos casos).

## Vertical Slice Dentro do Módulo

Quando uma funcionalidade dentro de um módulo já nasce complexa, a recomendação é isolá-la via [[wiki/concepts/vertical-slice-architecture|vertical slice]] dentro do próprio módulo antes de cogitar extração para projeto/serviço separado — extração só quando a necessidade real aparecer.

## Contraponto: Nem Sempre Vale Estender o Monolito Existente

[[wiki/sources/arquitetura-frontend-dash-fornecedores-vs-microfrontends-super-roupas]] traz um caso onde a solução enxuta não é adicionar um módulo ao monolito existente nem migrar para microfrontends — é criar um frontend novo, pequeno e somente leitura (dashboard + [[wiki/concepts/bff-pattern|BFF]]), isolado do resto do produto. Reforça, por outro caminho, o mesmo princípio central desta página (extrair/criar só com necessidade real): às vezes a unidade certa de decisão não é "que módulo/arquitetura usar dentro do produto existente", mas "isso nem precisa fazer parte do produto existente".

## Key Sources

- [[wiki/sources/arquitetura-frontend-microfrontends-monolito-modular-vertical-slice]] — contraste camadas vs. módulos, fronteiras como mecanismo de escala de time, e monolito modular como base da transição para microfrontend baseado em rotas
- [[wiki/sources/arquitetura-frontend-dash-fornecedores-vs-microfrontends-super-roupas]] — contraponto: um dashboard read-only isolado do produto principal, não um novo módulo do monolito
- [[wiki/sources/monolito-modular-transicao-mvp-empresa-madura]] — a versão backend do mesmo princípio: [[wiki/concepts/monolito-modular]] como etapa entre MVP e empresa madura, módulos comunicando por contratos/[[wiki/concepts/hexagonal-architecture|Ports & Adapters]] e extração tardia para microsserviço
