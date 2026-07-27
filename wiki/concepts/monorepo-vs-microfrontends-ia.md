---
type: concept
title: "Monorepo vs. Microfrontends para Contexto de IA"
aliases: ["monorepo para agentes de ia", "microfrontends e contexto de ia", "arquitetura para ia frontend"]
date_created: 2026-07-21
date_updated: 2026-07-27
source_count: 2
tags: [frontend, monorepo, microfrontends, harness, ia-para-devs, context-engineering]
skill: tech-mentor-frontend
status: stub
---

# Monorepo vs. Microfrontends para Contexto de IA

Observação de campo: a escolha entre monorepo e microfrontends muda de peso quando o trabalho de implementação passa a ser feito majoritariamente por agentes de IA, porque o custo real que se está otimizando deixa de ser só "acoplamento entre times" e passa a incluir "quanto contexto o agente precisa reunir para fazer uma mudança".

## O Argumento

- **Monorepo**: uma alteração vertical que toca vários módulos (ex.: mudar um contrato de API e propagar para as telas que o consomem) acontece dentro de um único contexto — o agente lê tudo que precisa num só lugar.
- **Microfrontends**: a mesma alteração pode se fragmentar em várias tarefas espalhadas por repositórios diferentes. Uma mudança simples pode virar, por exemplo, seis tarefas — e o dev pode precisar linkar manualmente um [[wiki/concepts/worktree-paralelismo|worktree]]/PR do backend ao worktree/PR do frontend só para sinalizar a interface entre os dois lados, permitindo que o agente extraia contexto de um PR a partir do outro.

Isso não invalida microfrontends como escolha arquitetural — os motivos clássicos para adotá-los (times independentes, ciclos de deploy separados, isolamento de blast radius) continuam válidos. O ponto é que, com agentes de IA fazendo parte relevante da implementação, a fragmentação de contexto entre repositórios vira um custo adicional explícito que um monorepo não tem.

## Relação com Outros Conceitos

- [[wiki/concepts/worktree-paralelismo]] — o mecanismo usado para paralelizar tarefas; aqui aparece sua limitação quando o contexto está espalhado entre repositórios
- [[wiki/concepts/monorepo-mobile]] — mesmo trade-off (consistência/compartilhamento vs. blast radius), aplicado a apps mobile em vez de microfrontends web
- [[wiki/concepts/harness]] — parte do ferramental que um projeto precisa construir para IA trabalhar bem é justamente reduzir esse atrito entre repositórios

## Reforço Independente: Custo de Coordenação Já Existe Sem IA

[[wiki/sources/arquitetura-frontend-microfrontends-monolito-modular-vertical-slice]] chega à mesma conclusão por um ângulo totalmente independente — sem falar de agentes de IA. O custo de fragmentar uma mudança entre repositórios (bump de versão de framework repetido N vezes, atualização de Design System exigindo PR e deploy por microfrontend consumidor) já é alto para humanos em [[wiki/concepts/microfrontends-parciais|microfrontends parciais/polirrepo]] — o [[wiki/concepts/monorepo-frontend|monorepo com libs]] resolve isso via grafo de dependências único, o mesmo mecanismo que aqui reduz o custo de contexto para o agente. Ou seja: o argumento "monorepo > polirrepo para mudanças verticais" não nasceu da IA, só ganhou um custo adicional explícito com ela.

## Key Sources

- [[wiki/sources/impacto-ia-mercado-frontend]]
- [[wiki/sources/arquitetura-frontend-microfrontends-monolito-modular-vertical-slice]] — mesmo trade-off monorepo/libs vs. polirrepo de microfrontends, justificado por CI/CD, versionamento e governança — independente de agentes de IA
