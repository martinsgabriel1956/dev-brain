---
type: concept
title: "Ruído e Loop de Nitpick em Revisão por Agente"
aliases: ["loop de revisão infinito", "teto de rodadas de revisão", "nitpick loop"]
date_created: 2026-10-26
date_updated: 2026-10-26
source_count: 1
tags: [code-review, agentes, ruido, nitpick, loop, anthropic]
skill: tech-mentor-ai
status: draft
---

# Ruído e Loop de Nitpick em Revisão por Agente

Barulho de revisão é barato quando o autor é humano (ignora o nitpick em 2 s) e **caro quando o autor é agente**: corrige → commit novo → nova rodada → novo nitpick → … Na [[wiki/entities/anthropic]] houve um PR com **mais de 50 rodadas numa noite**, até alguém intervir ([[wiki/sources/anthropic-code-review-por-agentes-sete-camadas]]).

## Correção adotada

- Após **3 rodadas**, o revisor **para de pedir conserto** e manda o autor **repensar a abordagem**.
- Rodadas seguintes **olham só o que mudou** (delta).
- Ao achar um bug, apontar a **classe inteira** para corrigir tudo de uma vez.
- Limitar nitpicks por PR e exigir arquivo+linha ([[wiki/concepts/review-md]]); filtrar por [[wiki/concepts/consenso-multiagente-em-code-review]].

Efeito relatado: PRs resolvidos em **uma rodada de 65% → 78%** (o dado de PRs com 5+ rodadas ficou ilegível na legenda).

## Heurística para humanos

Teto de 3–4 rodadas e então um humano verifica ([[wiki/concepts/human-in-the-loop]]). Relacionado ao alerta de que alarme demais esconde o incidente real ([[wiki/concepts/observabilidade]]) e a [[wiki/concepts/ciclo-agente]] sem condição de parada ([[wiki/concepts/loop-engineering]]).

## Key sources

- [[wiki/sources/anthropic-code-review-por-agentes-sete-camadas]]
