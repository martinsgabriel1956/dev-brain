---
type: concept
title: "Roteamento Automático de Modelo"
aliases: ["model routing", "auto-seleção de modelo", "roteador de LLM"]
date_created: 2026-07-19
date_updated: 2026-08-05
source_count: 3
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

## Caso de produto: Custom Router da Abacus.AI

[[wiki/sources/gestao-de-custo-velocidade-modelos-de-ia-fable-sol]] descreve uma variante mais simples e transparente do padrão: o "Custom Router" da [[wiki/entities/abacus-ai]] não usa um classificador aprendido para decidir a rota (diferente do RouteLLM/complexity-based acima) — o usuário define manualmente categorias fixas ("Frontier", "Complexo", "Velocidade", "Balanceado", "Fallback") e associa um modelo a cada uma. É roteamento por categoria estática, não por inferência de dificuldade da query. A chave de API gerada pelo router pode então ser usada em qualquer harness que aceite endpoint customizado (ex.: [[wiki/entities/opencode]]), o que a fonte trata como padrão genérico de "AI Gateway", não exclusivo da Abacus — o mesmo conceito é dito funcionar via OpenRouter, integrações do Cursor, uma skill própria no Claude Code, ou um script local.

Diferença chave em relação ao caso Adapta ONE acima: aqui a decisão de qual modelo mapear para cada categoria é feita pelo humano, uma única vez, na configuração — não pelo sistema em tempo real a cada prompt. É routing configurado, não routing aprendido.

## Caso adjacente, eixo diferente: Rotação de Contas Free Tier

[[wiki/sources/rotacao-de-contas-free-tier-llm-router-hostinger]] descreve um mecanismo de "rotação" que **não é** roteamento por qualidade/custo de modelo como os casos acima — é [[wiki/concepts/rotacao-de-contas-free-tier]], que troca entre **contas/credenciais** do mesmo tipo quando uma esgota a cota, não entre modelos de capacidade diferente. Os dois padrões compartilham a mesma infraestrutura de fallback ([[wiki/concepts/ai-gateway-llm-router]]), mas resolvem problemas distintos: um otimiza qual modelo responde melhor, o outro contorna limite de free tier por conta.

## Relação com outros conceitos

- [[wiki/concepts/skills-agente]] — no caso da Adapta, o roteamento de modelo e as skills de contexto pessoal operam juntos: a skill fornece o contexto, o roteador escolhe o modelo que processa esse contexto
- [[wiki/concepts/prompt-engineering]] — roteamento reduz a necessidade de o usuário aplicar conhecimento de prompt engineering específico por modelo
- [[wiki/concepts/ai-gateway-llm-router]] — infraestrutura de proxy compartilhada entre model routing e rotação de contas free tier
- [[wiki/concepts/rotacao-de-contas-free-tier]] — mesmo mecanismo de fallback, eixo de decisão diferente (credencial, não modelo)

## Key Sources

- [[wiki/sources/sistema-produtividade-ia-adapta]]
- [[wiki/sources/gestao-de-custo-velocidade-modelos-de-ia-fable-sol]] — Custom Router da Abacus.AI como caso de roteamento por categoria estática configurada pelo humano
- [[wiki/sources/rotacao-de-contas-free-tier-llm-router-hostinger]] — contraste com rotação de contas free tier (eixo de credencial, não de modelo)
