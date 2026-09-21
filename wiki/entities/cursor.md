---
type: entity
title: "Cursor"
aliases: ["Cursor IDE", "Cursor AI"]
date_created: 2026-08-27
date_updated: 2026-09-21
source_count: 2
tags: [cursor, harness, ide, agentes-ia, ia-para-devs]
skill: tech-mentor-ai
status: stub
---

# Cursor

IDE agêntica multi-modelo — permite escolher entre diversos modelos de fundação (Opus, GPT, outros) dentro de uma interface de editor de código. Citado repetidamente na wiki como referência de harness de codificação ao lado do [[wiki/entities/claude-code]] e do [[wiki/entities/codex-openai|Codex]], mas ainda sem página própria até esta ingestão apesar de aparecer em múltiplas fontes já indexadas ([[wiki/sources/formacao-ia-devs-aula-04-harness]], [[wiki/sources/product-engineer-vale-do-silicio-2026]], [[wiki/sources/formacao-ia-devs-aula-05-hands-on]]).

## Menor Controle de Harness Entre as Ferramentas Comparadas

[[wiki/sources/harness-anatomia-tecnica-alem-do-claude-md]] posiciona o Cursor no extremo de menor controle de usuário sobre o harness, num gradiente de três pontos: [[wiki/entities/open-claw|OpenClaw]] (construir o próprio agente — controle quase total) > [[wiki/entities/codex-openai|Codex]]/[[wiki/entities/claude-code|Claude Code]] (meio-termo) > **Cursor** (a ferramenta mantém a maior parte do harness fechado; o usuário fica, na prática, limitado à parcela de [[wiki/concepts/harness#Duas Camadas do Harness|user harness]]). A mesma fonte usa o Cursor como exemplo de que o modelo (ex. Opus) é intercambiável entre harnesses — o mesmo Opus roda tanto no Cursor quanto no Claude Code, mudando só o que está construído ao redor dele.

## Automations — Agentes Disparados por Evento/Schedule

Segundo [[wiki/sources/7-coisas-desenvolvedores-2026-max-lorian]], o **Cursor Automations** roda agentes a partir de agendamento ou de eventos externos — mensagem no Slack, ticket no Linear, pull request mesclado no GitHub, incidente no PagerDuty — sem nenhum humano abrindo uma janela de chat para iniciar a execução. Ver [[wiki/concepts/loop-engineering#Produto Comercial do Loop Disparado por Evento: Cursor Automations|loop engineering]] para o enquadramento teórico do padrão e os números de adoção (Faire, Amplitude) citados na fonte.

## Execução Multi-Modelo em Paralelo (N-modelos-mesmo-problema)

A mesma fonte descreve uma funcionalidade do Cursor que envia o mesmo problema para múltiplos modelos de fundação simultaneamente, cada um isolado em sua própria [[wiki/concepts/worktree-paralelismo|worktree]], para depois comparar os resultados e manter o melhor — variante do padrão de paralelismo via worktree que paraleliza a mesma tarefa entre modelos, não subtarefas diferentes.

## Desktop Operável por Agente

Agentes na nuvem do Cursor podem operar um desktop completo: abrir a aplicação recém-modificada, clicar dentro dela, coletar screenshots/vídeo e decidir se o resultado funcionou antes de continuar corrigindo — capacidade citada como exemplo do padrão mais amplo de dar ao agente uma máquina própria (terminal, browser, credenciais, rede). Ver [[wiki/concepts/agent-containment#Máquina Própria como Padrão de Produto (2026)|agent containment]].

## Key Sources

- [[wiki/sources/harness-anatomia-tecnica-alem-do-claude-md]] — menor grau de controle de harness entre as ferramentas comparadas; exemplo de modelo (Opus) intercambiável entre Cursor e Claude Code
- [[wiki/sources/7-coisas-desenvolvedores-2026-max-lorian]] — Cursor Automations (evento/schedule), execução multi-modelo em worktrees paralelas, desktop operável por agente
