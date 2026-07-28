---
type: source
title: "Loop Engineering, Harness e a Frase Que Viralizou"
aliases: ["loop engineering matou harness engineering", "loop engineering > harness engineering", "ReAct pattern origem loop"]
date_created: 2026-07-28
date_updated: 2026-07-28
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/loop-engineering-harness-e-a-frase-que-viralizou.md
source_url: ""
author: "Pedro Nauke"
date_published: ""
date_ingested: 2026-07-28
source_count: 0
tags: [loop-engineering, harness, react-pattern, agent-loop, worktree, compose, pedro-nauke]
skill: tech-mentor-ai
status: stable
---

## TL;DR

Primeiro de uma série de três vídeos de Pedro Nauke (criador do Compose) sobre loop engineering. Define loop como quatro peças (objetivo checável, ação, feedback, condição de parada), lista quatro ganhos concretos sobre prompt a prompt (autonomia, paralelização, velocidade da máquina, composição via memória), situa a origem da ideia no padrão **ReAct** (2022/2023) — não é conceito novo — e argumenta que o que destravou loop engineering em 2026 foram três fatores externos à ideia do loop: capacidade de long tasks dos modelos frontier, evolução do harness em compactação de contexto, e estado persistente em arquivo/board. Conclusão central: a frase viral "loop engineering matou harness engineering" está invertida — o loop **contém** o harness, não o substitui.

## Key Claims

**Claim:** Um loop de harness se reduz a quatro componentes mínimos: objetivo checável, ação (agente executando), feedback (avaliação do resultado) e condição de parada.
**Evidence:** Definição apresentada como framework didático pelo autor, ilustrada com o funcionamento do Compose (gera PRD → quebra em tarefas → executa uma a uma → revisa → guarda em memória → segue para a próxima).
**Confidence:** média — framework proposto pelo autor, não citação de paper ou padrão formal da indústria; consistente com o que `references/ai/agentic-patterns-2025.md` da skill descreve como scaffolding mínimo de agent loop (ver [[wiki/concepts/ciclo-agente]]).

**Claim:** A ideia central do loop agêntico não é nova em 2026 — vem do padrão **ReAct** (Reason + Act), de 2022/2023: um ciclo que agrega a resposta anterior ao contexto e repete até concluir a tarefa.
**Evidence:** Citado pelo autor como "padrão de 2023 ou até 2022" que já era a base de qualquer ferramenta agêntica antes do termo "loop engineering" popularizar. Consistente com o Padrão 6 (Agent Scaffolding) de `references/ai/agentic-patterns-2025.md` da skill, que descreve exatamente esse loop mínimo (mensagens acumuladas, tool_use, resposta final).
**Confidence:** alta — alinhado à literatura de referência da skill sobre ReAct/scaffolding.

**Claim:** O que destravou a execução eficiente de loops longos em 2026 não foi a ideia do loop, mas três fatores: (1) modelos frontier aguentando long tasks por horas/dias sem se perder, (2) harness evoluindo em compactação de contexto — alimentado por um ciclo de retroalimentação onde logs de execução viram dado de treinamento, (3) estado persistente escrito em arquivo/board em vez de mantido só na "cabeça" do modelo.
**Evidence:** Argumento do autor, sem cifra ou paper citado — nível de confiança tratado como narrativa qualitativa, não benchmark. O terceiro ponto (estado persistente) é diretamente descrito em `references/ai/agents-runtime.md` da skill como "Checkpointing de Estado" (ver [[wiki/concepts/harness]]).
**Confidence:** média — argumento qualitativo consistente com a skill, mas sem dado quantitativo de suporte na própria fonte.

**Claim:** A frase viral "loop engineering é maior que harness engineering" (ou "matou harness engineering") está invertida — o loop **contém** o harness; sem harness (compactação de contexto, estado persistente, execução de tool calls) sustentando o ciclo, nenhum modelo, por mais inteligente, mantém um loop rodando por horas sem quebrar.
**Evidence:** Argumento central do vídeo, reforçado pelo próprio design do Compose (loop determinístico construído sobre um harness que gerencia runs, contexto, persistência e revisão).
**Confidence:** alta como posicionamento conceitual do autor; consistente com a taxonomia já registrada em [[wiki/concepts/harness]] e [[wiki/concepts/loop-engineering]], que tratam loop engineering como "próximo degrau" sobre harness engineering, não como substituto.

**Claim:** Paralelização de loops via worktrees isoladas tem um limite prático de gerenciamento — o próprio autor relata perder controle acima de 4-5 loops simultâneos.
**Evidence:** Relato de experiência pessoal do autor, sem generalização para outros usuários.
**Confidence:** baixa/anedótica — número específico a um único usuário.

## Entities & Concepts Touched

- [[wiki/concepts/loop-engineering]]
- [[wiki/concepts/harness]]
- [[wiki/concepts/ciclo-agente]]
- [[wiki/concepts/worktree-paralelismo]]
- [[wiki/concepts/spec-driven-development]]
- [[wiki/entities/pedro-nauke]]

## Open Questions

- O vídeo promete dois vídeos seguintes na série (não ingeridos ainda) — um deles citado como aprofundando o aviso "isso só vale a pena se a tarefa for repetitiva, revisável e valiosa". Verificar se contradiz ou expande [[wiki/concepts/loop-engineering]] quando publicados.
- Nenhum dado quantitativo é dado para o "ciclo de retroalimentação" entre logs de execução e treinamento de modelos futuros — fica marcado aqui como afirmação qualitativa do autor, não fato verificado externamente.

## Fontes Relacionadas

- [[wiki/sources/loop-engineering-niveis-dev-loop-jogo-mmo]] — já documentava a distinção loop fixo/loop criador e citava o "Loop React" como primeiro nível do dev loop antes do termo loop engineering; esta fonte nomeia explicitamente a origem no padrão ReAct (2022/2023) e detalha os três fatores técnicos (modelo, harness, estado persistente) que tornaram loops longos viáveis em 2026 — ângulo complementar, sem contradição.
- [[wiki/sources/loop-engineering-planner-critic-grafo]] — propôs loop engineering como degrau seguinte a harness engineering; esta fonte reforça e formaliza essa relação com a frase "o loop contém o harness", corrigindo diretamente a leitura popular oposta ("loop > harness" / "loop matou harness").
