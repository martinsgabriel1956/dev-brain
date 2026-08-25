---
type: concept
title: "Guardrails de IA"
aliases: ["guardrails", "ai guardrails", "input/output filters llm"]
date_created: 2026-08-14
date_updated: 2026-08-25
source_count: 3
tags: [guardrails, seguranca, ai-safety, prompt-injection, agent-containment]
skill: tech-mentor-security
status: stub
---

# Guardrails de IA

Camadas de validação que mantêm um agente de IA dentro de limites determinados, aplicadas antes e/ou depois de cada chamada ao modelo e antes e/ou depois de cada chamada de tool. Modelo em camadas (ver [[wiki/sources/ai-safety-guardrails]]):

```
Input filters  → detectar intenção maliciosa antes de chegar ao modelo
Output filters → grounding, PII, policy — checar a resposta antes de entregá-la
Containment    → sandboxing, circuit breaker — última linha de defesa se as anteriores falharem
```

## Falso Positivo Como Efeito Colateral de Guardrail Mais Agressivo

[[wiki/sources/levelsio-china-guardrails-multi-modelo-opus-5]] documenta um caso concreto de fricção: [[wiki/entities/pieter-levels|Pieter Levels]] relata ter sido "rebaixado" de modelo (Opus → Sonnet) pelo Claude Code "por segurança" e ter perdido duas semanas em bloqueios num projeto pessoal de baixíssimo risco (simulador de Windows XP), enquanto o [[wiki/entities/moonshot-ai|Kimi K3]] completou as mesmas tarefas sem fricção. Relata também um segundo caso — o Claude respondendo com um "sermão" de saúde a uma pergunta rotineira de exame de sangue. [[wiki/entities/lucas-montano]] liga esse padrão ao aumento de guardrails da [[wiki/entities/anthropic]] pós-incidente de junho de 2026 (Fable 5 induzido a produzir código de exploit por pesquisadores da Amazon — ver contexto mais amplo em "Mitos e Fable 5" em [[wiki/entities/anthropic]]): mais guardrail tende, estatisticamente, a produzir mais falso positivo, e o efeito de mercado é empurrar usuários frustrados para modelos mais permissivos (frequentemente chineses/open-weight). **Confiança:** o mecanismo de "downgrade automático por risco percebido" não é confirmado publicamente pela Anthropic nesta fonte — tratar a explicação causal como interpretação do autor, não fato verificado.

## Guardrail Como Critério de Escolha de Modelo (Não Só Capacidade)

A mesma fonte descreve o guardrail como um **eixo de roteamento de modelo**, ortogonal à capacidade bruta: [[wiki/entities/lucas-montano]] relata rotear deliberadamente para o Claude em tarefas que tocam dados sensíveis de produção (Stripe + Resend conectados para e-mail de usuário), justamente pelo guardrail alto — "eu nunca utilizaria um modelo chinês aqui, não tem jeito" — e para um modelo mais permissivo em tarefas de hobby sem risco real. Ver detalhamento em [[wiki/concepts/roteamento-automatico-de-modelo]].

## Relação com Outros Conceitos

- [[wiki/concepts/prompt-injection-jailbreak]] — ataques que os guardrails existem para mitigar.
- [[wiki/concepts/agent-containment]] — a camada de contenção (sandboxing) é a última linha de defesa do modelo de guardrails, para quando input/output filters já falharam.
- [[wiki/concepts/design-patterns-ia]] — guardrails como uma das categorias de "pattern de segurança" focado em IA.

## Key Sources

- [[wiki/sources/ai-safety-guardrails]]
- [[wiki/sources/8-pontos-arquitetura-de-software-na-era-da-ia]] — guardrails como validação antes/depois de chamar agente ou tool, ao lado de jailbreak/prompt injection e OWASP Top 10 LLM
- [[wiki/sources/levelsio-china-guardrails-multi-modelo-opus-5]] — caso Levelsio (falso positivo/downgrade Opus→Sonnet, sermão de saúde) como fricção real de guardrail agressivo; guardrail como eixo de roteamento de modelo
