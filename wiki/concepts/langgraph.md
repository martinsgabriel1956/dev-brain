---
type: concept
title: "LangGraph"
aliases: ["LangGraph", "L Graph", "lang graph"]
date_created: 2026-07-10
date_updated: 2026-07-10
source_count: 2
tags: [langgraph, grafo, orquestracao, multi-agente, checkpointing, state-machine]
skill: tech-mentor-ai
status: draft
---

# LangGraph

Framework que representa o estado de um agente (ou sistema multi-agente) como um **grafo**: nós (nodes) são passos de execução — frequentemente uma chamada de LLM —, e arestas (edges) são transições condicionais entre esses passos. Permite loops, branches e human-in-the-loop nativamente, com state tipado e persistido automaticamente entre execuções (checkpointing).

## Por Que Grafo em Vez de Chain Linear

Chains lineares (uma sequência fixa de passos) não expressam bem fluxos com decisão condicional, repetição ou paralelismo — exigiriam código de controle manual em torno da chain. LangGraph modela essas decisões diretamente como arestas do grafo, e o motor do framework cuida do roteamento, do estado compartilhado e da persistência (retomar de onde parou após uma falha).

## O que os Nós e as Arestas Representam

Ver [[wiki/concepts/grafo-como-abstracao-de-agentes]] para a formalização completa do princípio (nós = computação/custo computacional, geralmente uma LLM; arestas = condição de fluxo determinística definida por quem constrói o sistema).

## LangGraph Não é a Única Forma de Implementar o Padrão

O grafo é uma abstração — G = (V, E) — independente de qualquer framework. LangGraph é uma escolha de implementação para quem já tem familiaridade com a abstração de grafo (de estruturas de dados/computação) e busca as garantias de checkpointing e state management do framework; o mesmo padrão pode ser desenhado sem framework algum ("no papel", como estrutura matemática, ou como scaffolding de código próprio).

## Uso Documentado no Wiki

- Implementação de [[wiki/concepts/planner-executor-critic|Planner-Executor-Critic]] com dynamic workflows: planner gera múltiplos prompts + rúbricas para subagentes, e o grafo controla o estado/roteamento entre planner, executores e verificador.
- Suporte nativo a human-in-the-loop e branches condicionais dentro do próprio grafo, sem precisar de lógica de controle externa.

## Key Sources

- [[wiki/sources/agentes-orquestracao]] — definição original: "LangGraph representa estado de agente como grafo — nodes são passos, edges são transições condicionais"
- [[wiki/sources/loop-engineering-planner-critic-grafo]] — demonstração prática com Planner-Executor-Critic e a defesa do grafo como novo nível de abstração da engenharia de agentes
