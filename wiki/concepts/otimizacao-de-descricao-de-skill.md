---
type: concept
title: "Otimização da Description de uma Skill"
aliases: ["description optimization", "should trigger", "loop de description"]
date_created: 2026-09-29
date_updated: 2026-09-29
source_count: 1
tags: [skills, description, trigger, evals, skill-creator, progressive-disclosure]
skill: tech-mentor-ai
status: draft
---

# Otimização da Description de uma Skill

## TL;DR

Como só `name` + `description` ficam sempre no contexto ([[wiki/concepts/skills-agente]], [[wiki/concepts/progressive-disclosure-ia]]), a **description decide se a skill é carregada**. O [[wiki/entities/skill-creator]] automatiza a melhoria dela num loop: gera descriptions candidatas, testa contra uma lista de queries marcadas `should trigger` (sim/não) e escolhe a melhor.

## Como foi demonstrado

1. Skill própria com a description **propositalmente capada pela metade** (não funcionava bem).
2. Pedido ao Claude Code: rodar o processo de evaluation com foco na description.
3. O loop (`run_loop.py`) iterou descriptions distintas, avaliando cada uma.
4. Saída: a melhor description; a skill voltou a ser acionada corretamente.
5. Dados e log guardados em `workspace/description-optimization` (lista de queries + log).

## Por que importa

Uma description vaga ou capada faz a skill não disparar (ou disparar fora de hora); o corpo perfeito é inútil se nunca carrega. Mesma raiz do problema de sobreposição de descriptions em [[wiki/concepts/skills-agente]].

## Cautelas

- Sem taxa de acionamento antes/depois na fonte ([[wiki/sources/avaliacao-de-skills-skill-creator-description-e-benchmark]]).
- Risco de overfitting às queries de teste — inferência [skill: tech-mentor-ai].

## Key sources

- [[wiki/sources/avaliacao-de-skills-skill-creator-description-e-benchmark]]
