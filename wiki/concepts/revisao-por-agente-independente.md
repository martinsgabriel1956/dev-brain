---
type: concept
title: "Revisão por Agente Independente"
aliases: ["revisor independente", "implementador ≠ revisor", "agent reviewer separation"]
date_created: 2026-09-29
date_updated: 2026-09-30
source_count: 2
tags: [revisao-por-ia, code-review, agentes, contrato-de-revisao, separacao-de-contextos]
skill: tech-mentor-ai
status: draft
---

# Revisão por Agente Independente

Princípio: o agente que **implementou** não deve ser o que **revisa**. Na formulação de [[wiki/sources/pilares-desenvolvimento-com-ia-contrato-de-revisao-waves]], o implementador "fica com orgulho ferido" e tende a concluir que fez bem; a IA revisora, sem processo, costuma responder "terminei, revisei, pronto para produção".

## Condições para funcionar (segundo a fonte)

1. **Revisor distinto** do implementador (nova sessão/agente).
2. **Processo completo de revisão**, não um "revise isso" solto.
3. **Insumo claro para revisar:** o [[wiki/concepts/contrato-de-revisao]], que dá ao revisor tudo de que precisa sem o contexto do projeto.

## Leitura técnica [skill: tech-mentor-ai — inferência]

O "orgulho" é uma metáfora; o mecanismo mais plausível é o revisor herdar a mesma janela e o mesmo raciocínio do implementador (viés de confirmação). Isso conecta ao ganho de contexto limpo em [[wiki/concepts/separacao-de-contextos]] e [[wiki/concepts/subagentes]]. Não é medido na fonte.

## Relações

- [[wiki/concepts/code-review]] — revisão humana × por IA; aqui o foco é o desenho do processo.
- [[wiki/concepts/waves-de-desenvolvimento]] — cada PR paralelo é autorrevisado por agentes.
- [[wiki/concepts/quality-gate]] — checagens determinísticas complementam o revisor probabilístico.

## Variante: auditar a *issue* antes de codar

Além de revisar código, [[wiki/sources/omxterm-terminal-web-pty-websocket-ssh-deploy-docker-traefik-otavio-miranda]] usa agentes de contexto limpo para **explicar de volta** a issue antes da implementação, e um segundo agente limpo para julgar o entendimento ([[wiki/concepts/auditoria-de-issue-por-agente-de-contexto-limpo]]); depois, orquestrador → writer → reviewer, sempre com contextos limpos. Custo em tokens declarado como alto.

## Key sources

- [[wiki/sources/omxterm-terminal-web-pty-websocket-ssh-deploy-docker-traefik-otavio-miranda]] — auditoria de issue + orquestrador/writer/reviewer em contexto limpo
- [[wiki/sources/pilares-desenvolvimento-com-ia-contrato-de-revisao-waves]]
