---
type: concept
title: "Guardrails de IA"
aliases: ["guardrails", "ai guardrails", "input/output filters llm"]
date_created: 2026-08-14
date_updated: 2026-08-14
source_count: 2
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

## Relação com Outros Conceitos

- [[wiki/concepts/prompt-injection-jailbreak]] — ataques que os guardrails existem para mitigar.
- [[wiki/concepts/agent-containment]] — a camada de contenção (sandboxing) é a última linha de defesa do modelo de guardrails, para quando input/output filters já falharam.
- [[wiki/concepts/design-patterns-ia]] — guardrails como uma das categorias de "pattern de segurança" focado em IA.

## Key Sources

- [[wiki/sources/ai-safety-guardrails]]
- [[wiki/sources/8-pontos-arquitetura-de-software-na-era-da-ia]] — guardrails como validação antes/depois de chamar agente ou tool, ao lado de jailbreak/prompt injection e OWASP Top 10 LLM
