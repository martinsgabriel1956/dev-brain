---
type: concept
title: "Ralph Loop"
aliases: ["Ralph Loop", "Ralph Wiggum loop"]
date_created: 2026-07-28
date_updated: 2026-08-03
source_count: 2
tags: [ralph-loop, loop-engineering, harness, bash, agente]
skill: tech-mentor-ai
status: stub
---

# Ralph Loop

Técnica de loop agêntico publicada por [[wiki/entities/geoffrey-huntley]] em julho de 2025 — descrita como deliberadamente simples: uma linha de bash que reenvia o mesmo prompt para o agente repetidamente até a tarefa terminar (se não terminou, roda de novo). Batizada em homenagem a Ralph Wiggum, personagem d'Os Simpsons descrito como o mais "burro" da série, precisamente por ser uma técnica tão simples que "parecia piada".

## Por Que Importa

Não é sofisticação técnica que faz um loop funcionar — é simplicidade e uma condição de parada clara. Um ano depois da publicação do Ralph Loop, esse mesmo princípio (rodar um agente em loop até um critério objetivo) virou disciplina institucionalizada: a [[wiki/entities/anthropic]] publicou o guia oficial "Getting Started with Loops", definindo quatro níveis formais de autonomia (turn-based, goal-based, time-based, proactive) — ver [[wiki/concepts/loop-engineering]]. O Ralph Loop é o ponto intermediário histórico entre a ideia original do padrão ReAct (2022/2023) e a maturidade atual do [[wiki/concepts/harness|harness]]/loop engineering em 2026.

## Relação com Loop Engineering

O Ralph Loop, na prática, é a versão mínima de um loop "goal-based": não há planner, verificador ou rúbrica formal — só a repetição do prompt até a IA (ou um humano observando) considerar a tarefa concluída. É citado como precursor histórico, não como implementação recomendada para produção — os mecanismos de verificação e checkpoints descritos em [[wiki/concepts/harness]] são o que separa um Ralph Loop simples de um loop que não desperdiça tokens sem supervisão.

## Citado Como "Escola 4" em Taxonomia de Programação com IA

[[wiki/sources/cinco-escolas-programacao-com-ia]] descreve o mesmo padrão (agente em loop sem supervisão em tempo real, tentando de novo até passar nos testes) como a posição mais extrema — "Escola 4" — numa taxonomia de cinco escolas de programação com IA, sob o nome `[transcrição incerta]` de "Half Wigun" (provável trocadilho com "Ralph Wiggum", mesma origem de nome já documentada acima). A fonte cita um argumento comercial de custo por hora (US$ 10-42/hora, valor não confirmado com precisão) associado a repositórios construídos com esse método — tratar como retórica de venda, não benchmark verificado. Ver [[wiki/concepts/escolas-de-programacao-com-ia]] para o mapa completo.

## Key Sources

- [[wiki/sources/harness-engineering-voce-e-o-harness-nao-o-modelo]]
- [[wiki/sources/cinco-escolas-programacao-com-ia]] — mesmo mecanismo citado como "Escola 4" (loop sem supervisão), com argumento comercial de custo por hora não verificado
