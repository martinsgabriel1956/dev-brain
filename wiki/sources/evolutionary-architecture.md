---
type: source
title: "Evolutionary Architecture"
aliases: ["evolutionary architecture", "strangler fig", "incremental change", "architecture evolution", "fitness functions"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/evolutionary-architecture.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [evolutionary-architecture, strangler-fig, fitness-functions, feature-flags, incremental-change, big-bang-rewrite]
skill: tech-mentor-system-design
status: stable
---

## TL;DR

Evolutionary Architecture (Ford, Parsons, Kua): arquitetura que suporta mudança guiada por múltiplas dimensões. 3 princípios: Fitness Functions como guardrails automatizados, mudança incremental (sem big bang rewrites), múltiplas dimensões de evolução simultânea (técnica, processo, dados). Strangler Fig para migrar sistemas legados sem downtime. Feature Flags para evolução segura.

## Key Claims

**Claim:** Big bang rewrite é o padrão de falha mais comum em arquitetura — Strangler Fig é a alternativa segura.
**Evidence:** Reescrita completa: 6-18 meses sem valor entregue, risco alto de não ter feature parity, equipe divide atenção entre legado e novo. Strangler Fig: proxy na frente do legado, rotas migradas incrementalmente para o novo sistema. Em qualquer ponto, o legado cobre o que o novo ainda não tem. Rollback: redirecionar no proxy.
**Confidence:** alta

**Claim:** Acoplamento baixo é um requisito não-funcional mensurável — não apenas uma aspiração.
**Evidence:** Acoplamento alto = deployabilidade baixa. Métrica: quantos serviços precisam ser deployados juntos? Se a resposta é > 1 regularmente, o acoplamento está alto. Fitness function: `assert(deployments.independent_percentage > 95%)`. Equipes independentes = serviços independentes = deployabilidade alta.
**Confidence:** alta

**Claim:** Feature Flags permitem deploy sem release — código em produção antes de estar disponível para usuários.
**Evidence:** Feature flag: `if (featureFlag.enabled("new-checkout")) { newFlow() } else { oldFlow() }`. Deploy do código novo sem ativar. Ativar para 1% dos usuários, monitorar, aumentar gradualmente. Rollback: desativar flag sem redeploy. Trunk-based development requer feature flags.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/evolutionary-architecture]]
- [[concepts/strangler-fig]]
- [[concepts/fitness-functions]]
- [[concepts/feature-flags]]
- [[concepts/incremental-change]]
- [[concepts/big-bang-rewrite]]

## Open Questions

- Strangler Fig com dados compartilhados — como lidar com migração de schema quando legado e novo sistema compartilham banco?
- Feature flags em microserviços — como garantir consistência de flags entre serviços para uma mesma request?
