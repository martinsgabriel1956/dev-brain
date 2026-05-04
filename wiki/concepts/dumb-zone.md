---
type: concept
title: "Dumb Zone"
aliases: ["zona de degradação", "smart zone", "zona de qualidade"]
date_created: 2026-05-04
date_updated: 2026-05-04
source_count: 1
tags: [context-engineering, coding-agents, llm, performance]
skill: tech-mentor-ai
status: stable
---

# Dumb Zone

Região da context window onde a qualidade das respostas começa a degradar. A partir de **~40% de uso da context window**, retornos decrescentes são observados empiricamente. A zona abaixo desse threshold é chamada de **smart zone**.

```
Context Window (ex: 168k tokens)
├── 0%  ─────────────────── Smart Zone ─────────────────── 40%
│                            ↑ boa qualidade
└── 40% ────────────────── Dumb Zone ────────────────── 100%
                             ↑ qualidade degradada
```

## Por Que Acontece

Em cada turno do loop, o agente escolhe entre centenas de próximos passos certos e centenas de errados. A única coisa que influencia essa escolha é o que está na conversa até aquele ponto. Quanto mais a context window cresce:

- Mais ruído de turnos anteriores (buscas de arquivos, output de builds, JSONs de MCPs)
- Menos "espaço de atenção" disponível para as informações realmente relevantes
- Trajetória negativa: histórico de correções aumenta a probabilidade do modelo errar novamente

## O Problema dos MCPs

MCPs que despejam JSON e UUIDs no contexto são a causa mais comum de trabalhar permanentemente na dumb zone. Cada chamada de MCP que retorna uma resposta verbosa consome tokens e empurra o contexto mais fundo na zona de degradação.

## Relação com 40%

O threshold de 40% é empírico e varia por:
- Complexidade da tarefa (tarefas simples toleram mais uso)
- Modelo (modelos com context window maior não necessariamente toleram mais — a degradação segue proporção, não valor absoluto)
- Qualidade do conteúdo (contexto limpo degrada menos que contexto com ruído)

Para modelos com context window de 1M+ tokens (ex: Gemini Flash), o threshold empírico ainda não está bem estabelecido — pode ser diferente.

## Estratégias para Ficar na Smart Zone

- [[concepts/compaction-intencional]] — comprimir o contexto periodicamente antes de cruzar o threshold
- [[concepts/separacao-de-contextos]] — sub-agentes com janelas novas para tarefas de exploração
- [[concepts/rpi-workflow]] — estrutura o trabalho para manter contexto baixo por design
- Evitar MCPs verbosos — ou configurar outputs compactos

## Key Sources

- [[sources/context-engineering-avancado-para-coding-agents]]
