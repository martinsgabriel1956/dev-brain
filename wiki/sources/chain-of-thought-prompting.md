---
type: source
title: "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"
aliases: ["CoT paper", "Wei et al. 2022"]
date_created: 2026-05-17
date_updated: 2026-05-17
source_count: 0
tags: [llm, prompt-engineering, chain-of-thought, raciocínio, emergent-ability, few-shot, scaling]
skill: tech-mentor-ai
status: stable
source_file: /home/nemomartins/Documentos/new/dev-study/raw/chain-of-thought-prompting.md
source_url: https://arxiv.org/abs/2201.11903
author: Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, Fei Xia, Ed H. Chi, Quoc V. Le, Denny Zhou
date_published: 2022-01-28
date_ingested: 2026-05-17
---

# Chain-of-Thought Prompting Elicits Reasoning in Large Language Models

**Wei et al., Google Brain, 2022** | arXiv:2201.11903

## TL;DR

[[chain-of-thought]] prompting — fornecer exemplares few-shot com passos de raciocínio intermediários — é uma [[emergent-ability]] de modelos com ~100B+ parâmetros. Com apenas 8 exemplares, PaLM 540B supera GPT-3 fine-tuned com verificador no GSM8K. Não requer fine-tuning.

## Argumento Central

Escala sozinha não resolve raciocínio complexo. A combinação de duas ideias existentes — rationales em linguagem natural + [[few-shot-learning]] via prompting — cria uma técnica simples que desbloqueia raciocínio em modelos grandes sem nenhum gradient update.

## Reivindicações-Chave

| Claim | Evidência | Confiança |
|---|---|---|
| CoT é uma propriedade emergente de escala | Modelos <100B não se beneficiam; curva aumenta abruptamente após esse limiar | Alta |
| CoT supera fine-tuned SOTA via prompting only | PaLM 540B: ~57% no GSM8K vs ~35% do melhor fine-tuned anterior | Alta |
| O conteúdo dos passos intermedários importa | Ablação: "variable compute only" (tokens sem conteúdo) não ajuda | Alta |
| Raciocínio deve vir antes da resposta | Ablação: "reasoning after answer" não produz melhora | Alta |
| CoT é robusto a diferentes anotadores e estilos | 3 anotadores independentes, variação de conciso a detalhado | Alta |
| CoT facilita generalização OOD em raciocínio simbólico | Standard prompting falha completamente OOD; CoT mantém curva crescente | Alta |

## Entidades Mencionadas

- [[jason-wei]] — lead author, Google Brain
- [[entities/openai]] — GPT-3 usado como baseline
- Google Brain — PaLM e LaMDA

## Conceitos Trazidos / Aprofundados

- [[chain-of-thought]] — técnica central do paper
- [[emergent-ability]] — CoT como exemplo canônico de capacidade emergente
- [[few-shot-learning]] — CoT é uma extensão com passos de raciocínio
- [[in-context-learning]] — CoT funciona sem gradient updates
- [[scaling-laws]] — CoT não segue scaling law suave; emergência abrupta
- [[fine-tuning]] — CoT via prompting supera fine-tuned GPT-3 no GSM8K
- [[prompt-engineering]] — CoT é uma técnica dentro da hierarquia de prompt engineering

## Setup Experimental

- **Modelos:** GPT-3 (até 175B), LaMDA (até 137B), PaLM (8B, 62B, 540B)
- **Método base:** 8 exemplares few-shot fixos, sem fine-tuning de nenhum modelo
- **Comparação:** standard prompting vs chain-of-thought prompting
- **Benchmarks aritmético:** GSM8K, SVAMP, ASDiv, MAWPS
- **Benchmarks senso comum:** CSQA, StrategyQA, Date Understanding, Sports Understanding, SayCan
- **Benchmarks simbólico:** Last letter concatenation, Coin flip (in-domain e OOD)

## Ablação Chave

| Variante | Resultado | Interpretação |
|---|---|---|
| Equation only | Não ajuda em GSM8K | Linguagem natural nos passos é necessária |
| Variable compute only (`...`) | Não ajuda | Extensão de tokens sem conteúdo não é o fator |
| Reasoning after answer | Não ajuda | Raciocínio deve preceder a resposta |

## Quando CoT Ajuda Mais

1. Tarefa desafiadora com raciocínio multi-etapas
2. Modelo com ~100B+ parâmetros
3. Curva de escala do standard prompting é plana

## Limitações

- Cadeias geradas nem sempre são factuais (hallucinated reasoning)
- Requer modelos muito grandes
- Custo de inferência maior (mais tokens)
- Não recomendado em cenários reais sem verificação das cadeias

## Questões em Aberto

- O que exatamente no pré-treinamento causa a emergência do CoT em ~100B?
- Reasoning models (o1/o3/Claude extended thinking) internalizam CoT no treinamento — a relação com CoT prompting explícito ainda precisa ser mapeada
- CoT com modelos menores é possível via destilação (ver [[fine-tuning]] com rationale distillation)?

## Quotes Notáveis

> "Chain-of-thought reasoning is an emergent property of model scale that allows sufficiently large language models to perform reasoning tasks that otherwise have flat scaling curves."

> "No language models were finetuned in the process of writing this paper."
