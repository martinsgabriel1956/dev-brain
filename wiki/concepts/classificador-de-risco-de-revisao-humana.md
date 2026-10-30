---
type: concept
title: "Classificador de Risco para Revisão Humana"
aliases: ["níveis de revisão humana", "classificador de mudança", "quem define o nível é a mudança"]
date_created: 2026-10-26
date_updated: 2026-10-26
source_count: 1
tags: [code-review, risco, agentes, llm-as-judge, human-in-the-loop, anthropic]
skill: tech-mentor-ai
status: draft
---

# Classificador de Risco para Revisão Humana

Camada 5 do pipeline da [[wiki/entities/anthropic]] ([[wiki/sources/anthropic-code-review-por-agentes-sete-camadas]]): **o número de pessoas que revisam depende do risco da mudança**, decidido por um agente.

| Nível | Exemplos | Humanos |
|---|---|---|
| Baixo | documento de texto, feature interna, algo atrás de flag | **0** |
| Médio | mudança normal de produto, feature nova, **áreas sensíveis** (cache, auto-updater, system prompt) | **≥1** — pode ser o próprio autor |
| Alto | "hot code", caminhos que trazem muito revenue | **2** |

- Um **agente classificador** lê a mudança e escolhe o nível; um **segundo classificador** pergunta se *aquela* mudança precisa do número de pessoas que o nível diz ([[wiki/concepts/llm-as-judge]]).
- Princípio: **"quem define o nível é a mudança, não o autor"** — impede que o autor (ou o agente autor) escolha o rigor.
- Regra do fecho: aprovação de bot **nunca** conta como aprovação de pessoa.

## Relação com a matriz do wiki

Equivale, em operação plena, ao que [[wiki/concepts/matriz-risco-dificuldade-review-ia]] propõe como *transição* (merge automático / amostragem / pares), mas aqui o classificador é automatizado e o eixo é só risco; auth/pagamentos/migração aparecem lá como alto risco, aqui os exemplos são cache, auto-updater e system prompt. Ver também [[wiki/concepts/human-in-the-loop]] e [[wiki/concepts/code-review]] (seção "IA aprovando PR de IA").

## Key sources

- [[wiki/sources/anthropic-code-review-por-agentes-sete-camadas]]
