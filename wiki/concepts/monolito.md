---
type: concept
title: "Monolito"
aliases: ["monolito", "monolith", "monolito tradicional"]
date_created: 2026-08-10
date_updated: 2026-08-10
source_count: 2
tags: [monolito, arquitetura, deploy, mvp, backend]
skill: tech-mentor-backend
status: stub
---

# Monolito

Aplicação entregue como **um único artefato**, com deploy único, geralmente um repositório, uma versão e (tradicionalmente) uma equipe. Módulos e domínios (produtos, users, pagamentos, hotéis...) coexistem no mesmo processo e comunicam-se por **chamadas de função** diretas.

## Vantagens

Simplicidade: sem APIs entre serviços, sem comunicação via protocolos de rede (que adicionam latência e complexidade), sem orquestração mirabolante de deploys. Um deploy só — não há o problema de versões divergentes entre serviços.

## Risco

Sem disciplina de fronteiras, o monolito cresce de forma desorganizada — uma função chamando outra em cadeia — e degenera em [[wiki/concepts/code-espaguete]] / projeto legado. As saídas discutidas são melhorar o monolito, evoluir para [[wiki/concepts/monolito-modular]], ou migrar para [[wiki/concepts/microsservicos]].

## Quando basta

Monolitos levam MVPs muito longe. Exemplo citado: produtos solo do Pieter Levels, todos monolitos, faturando milhões — com ~1M de usuários basta rodar em 3-4 máquinas com load balancer e réplica de banco ([[wiki/concepts/escalabilidade-horizontal]]). Ver [[wiki/sources/monolito-modular-transicao-mvp-empresa-madura]].

## Key sources

- [[wiki/sources/arquitetura-de-sacrificio]] — Fowler recomenda o monolito como a melhor *arquitetura de sacrifício* por padrão (microsserviços adicionam distribuição/assincronia cedo demais)
- [[wiki/sources/monolito-modular-transicao-mvp-empresa-madura]]
