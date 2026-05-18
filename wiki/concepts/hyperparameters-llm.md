---
type: concept
title: "Hiperparâmetros de LLM"
aliases: ["hyperparameters", "temperature", "stop sequence", "max tokens", "top-p"]
date_created: 2026-05-17
date_updated: 2026-05-17
source_count: 1
tags: [llm, hyperparameters, temperature, prompt-engineering, inferência]
skill: tech-mentor-ai
status: stable
---

# Hiperparâmetros de LLM

## Definição

Parâmetros que controlam o comportamento de **inferência** de um modelo de linguagem — distintos dos pesos do modelo. Não alteram o modelo; alteram como ele amostra tokens durante a geração.

## Parâmetros Principais

### Temperature
Controla aleatoriedade na distribuição de probabilidade dos tokens.

| Valor | Comportamento |
|---|---|
| `0` | Determinístico — sempre o token mais provável. Mesma entrada = mesma saída (dentro da sessão). |
| `0.1–0.4` | Conservador, consistente. Bom para código e extração estruturada. |
| `0.7–0.9` | Criativo, variado. Bom para geração de texto, brainstorming. |
| `1.0+` | Muito aleatório — pode gerar incoerências. |

### Max Tokens
Limite máximo de tokens no [[completion]]. Afeta latência e custo diretamente. Inclui apenas os tokens do output — não conta os tokens do prompt.

### Stop Sequence
Sequência de texto que interrompe a geração quando encontrada. Essencial para:
- Evitar que o modelo gere variações adicionais de código
- Delimitar onde a resposta termina

Exemplos por linguagem:
- Python: `#`
- JavaScript: `//`
- Output estruturado: `\n\n`

### Top-P (Nucleus Sampling)
Alternativa à temperature. Restringe a amostragem ao conjunto mínimo de tokens que somam probabilidade `p`. `top_p=0.9` = considera apenas os tokens que cobrem 90% da probabilidade acumulada.

Regra prática: ajuste **ou** temperature **ou** top-p — não os dois simultaneamente.

### Frequency / Presence Penalty
Penaliza tokens que já apareceram no completion — reduz repetição. Útil para gerar texto mais diverso.

## Relação com Outros Conceitos

- [[completion]] — os hiperparâmetros controlam como o completion é gerado
- [[prompt-engineering]] — prompt + hiperparâmetros juntos definem o output
- [[context-window]] — `max_tokens` é um dos controles do context window

## Fontes

- [[wiki/sources/microsoft-prompt-engineering-guide]]
