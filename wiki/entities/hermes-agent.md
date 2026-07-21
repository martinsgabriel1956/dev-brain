---
type: entity
title: "Hermes Agent"
aliases: ["Hermes", "hermes.md"]
date_created: 2026-07-21
date_updated: 2026-07-21
source_count: 1
tags: [tech-mentor-ai, hermes-agent, agent-memory, learning-loop, open-source, mit]
skill: tech-mentor-ai
status: stub
---

# Hermes Agent

Agente de codificação open source (licença MIT), comparado ao [[wiki/entities/open-claw]] por rodar localmente ou em VPS própria. Implementa um [[wiki/concepts/closed-loop-skill-learning|closed-loop skill learning system]] sobre uma [[wiki/concepts/agent-memory-tres-camadas|memória em três camadas]] (sessão, persistente, skill) indexada via FTS5 do SQLite, além de um messaging gateway conectável a Telegram, Discord e Slack.

Segundo [[wiki/sources/hermes-agent-open-claw-learning-loop]], liderou o ranking global de uso de tokens do OpenRouter na semana anterior à publicação da fonte, superando Open Claw, Kilo Code, Claude Code e Descript — sinal de tração citado com ressalva explícita contra tratá-lo como validação de qualidade.

`hermes.md` é citado como convenção de nomeação real (não exclusiva deste projeto) para arquivos de especificação de prompt de sistema em projetos de agentes de IA — relevante porque essa string, presente em Git history, foi o gatilho de um bug de billing no Claude Max 20 da Anthropic (ver [[wiki/entities/anthropic]]).

## Key Sources

- [[wiki/sources/hermes-agent-open-claw-learning-loop]]
