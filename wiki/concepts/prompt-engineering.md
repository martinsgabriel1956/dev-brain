---
type: concept
title: "Prompt Engineering"
aliases: ["engenharia de prompt", "prompt design"]
date_created: 2026-05-17
date_updated: 2026-05-17
source_count: 2
tags: [prompt-engineering, llm, few-shot, codex, software-3]
skill: tech-mentor-ai
status: stable
---

# Prompt Engineering

## Definição

Prática de construir sequências de texto (prompts) para elicitar outputs específicos de modelos de linguagem. É a primeira alavanca de controle sobre um LLM — barata, iterável e sem infra adicional.

Andrej Karpathy chama isso de [[software-3]] — a terceira geração de programação.

## Hierarquia de Abordagens (custo crescente)

```
Zero-shot → Few-shot → Chain-of-Thought → Self-Consistency → Fine-tuning
↑ Mais rápido, menos custo                    Mais lento, mais custo ↑
```

Sempre experimente da esquerda para a direita antes de ir para a próxima etapa.

## Quatro Padrões Fundamentais

### Tell It — Instrução de Alto Nível
Descreva a tarefa explicitamente: linguagem, tom, restrições, o que fazer e o que não fazer. Declare variáveis e tipos antes da instrução.

### Show It — Exemplos (Few-Shot)
Inclua pares input→output no prompt. O modelo aprende o padrão sem atualizar pesos. Sweet spot: 3–5 exemplos. Ver [[few-shot-learning]].

### Describe It — Descrever Contexto Desconhecido
Para APIs ou domínios que o modelo não conhece, descreva assinaturas de funções, schemas ou glossário diretamente no prompt antes de usá-los.

### Remind It — Histórico Conversacional
Modelos são stateless — não lembram turnos anteriores. Para manter contexto, inclua o histórico como exemplos adicionais. Use janela deslizante (rolling window) para não exceder o [[context-window]].

## Estrutura Completa de um Prompt

```
[Instrução de alto nível]
[Contexto / Schema / API hints]
[Exemplos few-shot]
[Input do usuário]
```

Não há estrutura obrigatória — os modelos são flexíveis. Itere e meça.

## Quando Usar vs Fine-Tuning

| Situação | Abordagem |
|---|---|
| Tarefa genérica, modelo grande | Zero-shot |
| Padrão de output específico | Few-shot |
| Raciocínio complexo | Chain-of-Thought |
| Dataset grande, latência crítica | Fine-tuning |

## Relação com Outros Conceitos

- [[in-context-learning]] — o mecanismo subjacente ao few-shot e zero-shot
- [[few-shot-learning]] — variante com exemplos no prompt
- [[zero-shot-learning]] — sem exemplos, só instrução
- [[chain-of-thought]] — forçar raciocínio passo a passo
- [[completion]] — o output gerado pelo modelo
- [[context-window]] — limite de tamanho do prompt
- [[hyperparameters-llm]] — controles de temperatura, stop sequence etc.
- [[fine-tuning]] — alternativa mais custosa

## Fontes

- [[wiki/sources/microsoft-prompt-engineering-guide]]
- [[wiki/sources/gpt3-language-models-are-few-shot-learners]]
- [[wiki/sources/chain-of-thought-prompting]] — evidência empírica de que CoT (few-shot com passos intermediários) é a técnica mais eficaz para raciocínio multi-etapas
