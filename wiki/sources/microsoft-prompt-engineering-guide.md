---
type: source
title: "Microsoft Prompt Engineering Guide"
aliases: ["Microsoft Codex Guide", "How to get Codex to produce the code you want"]
date_created: 2026-05-17
date_updated: 2026-05-17
source_count: 0
tags: [prompt-engineering, llm, codex, openai, few-shot, microsoft]
skill: tech-mentor-ai
status: stable
source_file: /home/nemomartins/Documentos/new/dev-study/raw/microsoft-prompt-engineering-guide.md
source_url: https://microsoft.github.io/prompt-engineering/
author: Microsoft
date_published: 2022-05-01
date_ingested: 2026-05-17
---

# Microsoft Prompt Engineering Guide

## TL;DR

Guia prático da Microsoft sobre como obter boas completions de modelos de código (Codex/GPT-3) via **prompt engineering**. Introduz quatro padrões fundamentais — Tell It, Show It, Describe It, Remind It — e o conceito de "Software 3.0" (Andrej Karpathy). Contexto de lançamento: Microsoft Build 2022, junto com o Azure OpenAI Service.

## Argumento Central

A qualidade das completions de um LLM depende diretamente de como o prompt é construído. Prompt engineering é uma skill de engenharia — iterável, barata e composable — que pode substituir fine-tuning na maioria dos casos de uso.

## Quatro Padrões de Prompt Engineering

### 1. Tell It — Descrição de Alto Nível
Começar sempre com uma instrução de alto nível do que se quer. Especificar: linguagem alvo, tom, restrições, o que fazer e o que **não** fazer. Declarar variáveis e tipos antes da instrução reduz ambiguidade.

### 2. Show It — Few-Shot com Exemplos
Incluir pares input→output como exemplos demonstrativos. O modelo aprende o padrão sem atualizar pesos. Sweet spot: 3–5 exemplos.

### 3. Describe It — Descrever APIs Desconhecidas
Quando a biblioteca/API não é conhecida pelo modelo, descrever assinaturas de funções no próprio prompt antes de usá-las. Usado no Minecraft Codex sample para a Simulated Player API.

### 4. Remind It — Histórico Conversacional
Modelos são stateless. Para manter contexto, incluir o par input+completion anterior como exemplo adicional. Na prática, usar janela deslizante (rolling window) do histórico porque o context window é finito.

## Estrutura Completa de um Prompt

```
[Descrição de alto nível] → [Contexto/Schema] → [Exemplos few-shot] → [Input do usuário]
```

Não há regra rígida de estrutura — os modelos são flexíveis. Experimento e iteração são o caminho.

## Hiperparâmetros Relevantes

| Parâmetro | Efeito |
|---|---|
| `temperature` | Criatividade. `0` = determinístico. Maior = mais variação. |
| `max_tokens` | Limite de tamanho do completion. Afeta latência. |
| `stop sequence` | Para geração ao encontrar a sequência. Ex: `#` para Python. |

## Considerações de Produção

- **Performance:** prompts maiores = maior latência. Fine-tuning reduz necessidade de prompts longos.
- **UX:** sempre deixar o usuário revisar e rejeitar outputs. Nunca executar código gerado automaticamente.
- **Responsabilidade:** modelos refletem vieses dos dados de treino. Usar content filtering em produção.

## Software 3.0

Andrej Karpathy cunhou o conceito: escrever prompts é a terceira geração de programação (Software 1.0 = código imperativo; 2.0 = pesos de redes neurais; 3.0 = prompts em linguagem natural).

## Entidades Mencionadas

- [[wiki/entities/openai]] — criadora do Codex e GPT-3
- [[wiki/entities/microsoft]] — publicou este guia + Azure OpenAI Service
- [[wiki/entities/andrej-karpathy]] — cunhou "Software 3.0"

## Conceitos Relacionados

- [[wiki/concepts/prompt-engineering]]
- [[wiki/concepts/completion]]
- [[wiki/concepts/few-shot-learning]]
- [[wiki/concepts/zero-shot-learning]]
- [[wiki/concepts/chain-of-thought]]
- [[wiki/concepts/context-window]]
- [[wiki/concepts/hyperparameters-llm]]
- [[wiki/concepts/in-context-learning]]
- [[wiki/concepts/fine-tuning]]
- [[wiki/concepts/software-3]]

## Questões em Aberto

- O guia foi escrito em 2022, focado em Codex. Em 2026, as técnicas centrais (few-shot, CoT, context priming) ainda se aplicam — mas o campo evoluiu muito com raciocínio estruturado (o1/o3, Claude extended thinking). Qual é o limite onde prompt engineering cede lugar a reasoning models?
- Fine-tuning era apresentado como alternativa custosa. Com LoRA/QLoRA, o trade-off mudou. A hierarquia zero-shot → few-shot → fine-tuning ainda é válida?
