---
type: concept
title: "Roteamento Automático de Modelo"
aliases: ["model routing", "auto-seleção de modelo", "roteador de LLM"]
date_created: 2026-07-19
date_updated: 2026-07-19
source_count: 1
tags: [llm, model-routing, prompt-engineering, agregador-de-modelos]
skill: tech-mentor-ai
status: draft
---

# Roteamento Automático de Modelo

Padrão de infraestrutura de IA em que uma camada intermediária decide, para cada prompt, **qual modelo de linguagem deve respondê-lo**, em vez de o usuário escolher manualmente entre GPT, Claude, Gemini etc. O objetivo é sempre usar o modelo mais adequado ao tipo de tarefa (custo, latência, capacidade de raciocínio) sem exigir conhecimento do usuário sobre as diferenças entre modelos.

## Estratégias comuns de roteamento [skill: tech-mentor-ai]

- **Complexity-based (ex.: RouteLLM):** um classificador decide se a query é "fácil" ou "difícil" e direciona para um modelo barato ou forte de acordo.
- **Cascade pattern:** tenta primeiro o modelo mais barato; se a confiança da resposta for baixa, escala para um modelo mais forte.
- **Intent-based routing:** classifica a intenção da query (geração de código, análise de dados, pergunta simples) e mapeia para o modelo especialista correspondente.
- **Latency-budget / cost-tier routing:** escolhe o modelo em função de um SLA de latência ou do plano pago pelo usuário.

Essas estratégias são infraestrutura conhecida em produtos de IA multi-modelo — ver detalhamento técnico em `references/ai/model-routing-selection.md` (skill tech-mentor-ai).

## Caso de produto: Adapta ONE

[[wiki/entities/adapta]] implementa uma versão comercial desse padrão: o modelo "ONE" atua como um roteador que escolhe automaticamente, entre os modelos disponíveis no ecossistema (GPT, Claude, Gemini e outros), qual deve responder cada prompt — sem exigir que o usuário selecione manualmente. **[external]** Segundo a documentação pública da Adapta (`docs.adapta.org`), o "ONE Pro" implementa uma variante diferente: em vez de rotear para um único modelo, ele passa o mesmo prompt por múltiplos modelos de raciocínio e compõe uma resposta mais completa — mais próximo de um padrão de ensemble/self-consistency do que de roteamento puro.

**Confiança:** o mecanismo exato de decisão (qual classificador, quais critérios) não é público — é uma implementação proprietária descrita apenas em termos de resultado ("sempre a resposta do modelo mais adequado"), sem verificação independente possível a partir das fontes disponíveis.

## Relação com outros conceitos

- [[wiki/concepts/skills-agente]] — no caso da Adapta, o roteamento de modelo e as skills de contexto pessoal operam juntos: a skill fornece o contexto, o roteador escolhe o modelo que processa esse contexto
- [[wiki/concepts/prompt-engineering]] — roteamento reduz a necessidade de o usuário aplicar conhecimento de prompt engineering específico por modelo

## Key Sources

- [[wiki/sources/sistema-produtividade-ia-adapta]]
