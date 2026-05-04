---
type: concept
title: "RPI Workflow"
aliases: ["research plan implement", "RPI", "research-plan-implement"]
date_created: 2026-05-04
date_updated: 2026-05-04
source_count: 2
tags: [coding-agents, context-engineering, workflow, ai-engineering]
skill: tech-mentor-ai
status: stable
---

# RPI Workflow

Framework de três fases para trabalhar com coding agents em codebases reais. Objetivo central: manter o agente na [[concepts/dumb-zone|smart zone]] da context window durante todo o trabalho e preservar o [[concepts/mental-alignment]] do dev sobre o que está sendo construído.

## As Três Fases

### Research
- O agente **apenas observa** — sem modificar nada
- Coleta quais arquivos existem, como o código está organizado, dependências
- Output: documento com arquivos exatos e números de linha relevantes ao problema
- Regra crítica: o dev precisa ler o suficiente para ter um modelo mental do que o agente encontrou — não linha por linha, mas o suficiente para detectar se a direção está errada

### Plan
- Recebe o output do research como input
- Produz os passos exatos de implementação, com snippets de código reais
- Inclui como testar após cada mudança
- Tamanho ideal: revisável em ~10 minutos — o suficiente para confiança, não tanto que dobre o trabalho

### Implement
- Executa o plano mantendo a context window baixa
- Segue o [[concepts/plano-vertical]]: cada entrega é testável antes de continuar
- Dev acompanha o que está sendo gerado — sem deixar o agente ir longe demais sem revisão

## Por Que Funciona

LLMs são stateless. A única forma de obter melhor performance é colocar tokens melhores. O RPI estrutura o trabalho para que cada fase receba apenas os tokens que ela precisa, sem ruído de fases anteriores.

A separação research/plan evita [[concepts/separacao-de-contextos|contaminação de contexto]] — o modelo não toma decisões de arquitetura escondidas numa suposta fase de observação.

## Anti-patterns

- **Plano de 1.000 linhas** — dobra o trabalho sem garantia de que o código vai bater
- **Não ler o código** durante o research — você perde a capacidade de detectar problemas cedo
- **Mesma sessão para research e plan** — o modelo mistura o que observou com o que acha que deveria construir
- **Plano horizontal** (banco todo → serviços todos → API toda) — nada é testável no meio

## Relação com Spec-Driven Development

O RPI pertence à mesma família do Spec-Driven Development, mas com foco explícito em **context engineering** em vez de especificação formal. A distinção importa porque "spec-driven dev" sofreu semantic diffusion — o termo virou vago. O que importa não é o nome, mas os princípios: compaction, smart zone, human-in-the-loop nos pontos de maior alavancagem.

## Key Sources

- [[sources/erros-workflow-research-plan-implement]]
- [[sources/context-engineering-avancado-para-coding-agents]]
