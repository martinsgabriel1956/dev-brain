---
type: concept
title: "Self-Attention"
aliases: ["mecanismo de atenção", "attention mechanism", "scaled dot-product attention"]
date_created: 2026-09-18
date_updated: 2026-09-18
source_count: 1
tags: [self-attention, transformers, llm-fundamentals, attention-is-all-you-need]
skill: tech-mentor-ai
status: stable
---

## Definição

Mecanismo central da [[transformer-architecture|arquitetura Transformer]] que calcula, para cada token de uma sequência, o quanto os demais tokens são relevantes para determinar seu significado *naquele contexto específico*. É o que resolve a ambiguidade que um [[embedding-vectors|embedding vector]] sozinho não resolve — um token só carrega significado geral até ser combinado, via self-attention, com o contexto da frase em que aparece.

## O Problema que Resolve: Ambiguidade Contextual

Um embedding vector é fixo por token e representa a média de todos os usos daquele token no corpus de treino. A palavra "banco" carrega, no seu embedding, sinais tanto para "instituição financeira" quanto para "assento". Só o contexto da frase ("o banco aprovou o crédito" vs. "a menina sentou no banco") desambiguiza qual significado se aplica — e é exatamente isso que self-attention calcula.

## Q, K (e V) — Query, Key, Value

Para cada token, o mecanismo gera (pelo menos) dois vetores adicionais, derivados do embedding + positional encoding via matrizes de peso aprendidas durante o treino:

- **Q (Query)**: o que aquele token está "buscando" nos demais.
- **K (Key)**: o que cada token "oferece" quando outros o consultam.
- **V (Value)**: [external] o conteúdo real que é agregado na saída, ponderado pelos scores — terceiro vetor do mecanismo padrão Q/K/V, não coberto em [[wiki/sources/self-attention-mecanismo-transformers]].

## Cálculo do Attention Score

```
scores = (Q · Kᵀ) / √d_k        ← produto escalar, escalado pela raiz da dimensão
weights = softmax(scores)        ← normaliza para distribuição de probabilidade por linha
output = weights · V             ← [external] média ponderada dos Values
```

O produto Q × K gera uma matriz onde cada célula representa a importância de um token para outro. Exemplo ilustrativo (não real) com "o banco aprovou o crédito": "banco"→"crédito" tem peso alto (~60%, adiciona muito contexto), "o"→"banco" tem peso baixo (~5%, artigo quase não muda significado). O resultado passa por **softmax** para normalizar os scores.

## Positional Encoding — Pré-requisito

Self-attention, por si só, é invariante à posição — não distingue a ordem dos tokens. Por isso um vetor de [[positional-encoding]] é somado ao embedding antes do cálculo de Q/K, injetando informação de ordem. Sem isso, "a mãe matou a filha" e "a filha matou a mãe" seriam tratadas como equivalentes.

## Multi-Head Attention

[external] Na prática, o cálculo acima roda em paralelo H vezes ("heads"), cada uma em um subespaço diferente do embedding, aprendendo tipos de relação distintos (sintaxe, semântica, correferência). Mencionado en passant em [[wiki/sources/como-llms-funcionam]], sem aprofundamento em nenhuma fonte da wiki até o momento.

## Output Final

O resultado do cálculo de atenção é um novo vetor por token, combinando significado semântico (do embedding original) com o contexto específico da frase de input. É esse vetor enriquecido que alimenta a previsão do próximo token com muito mais precisão do que o embedding bruto sozinho permitiria.

## Custo: O(n²)

Para n tokens, a matriz de atenção é n×n — custo quadrático no comprimento da sequência. Ver [[transformer-architecture]] para o impacto disso em context window e as otimizações ([[flash-attention]], [[mamba-ssm]]) que existem para mitigar.

## Conexões

- [[transformer-architecture]] — arquitetura onde self-attention é o componente central
- [[embedding-vectors]] — a entrada semântica sobre a qual Q/K/V são calculados
- [[positional-encoding]] — pré-requisito para que attention capture ordem
- [[wiki/entities/attention-is-all-you-need-paper]] — paper que introduziu o mecanismo (2017)
- [[flash-attention]] — implementação IO-aware do mesmo cálculo matemático, muito mais eficiente

## Key Sources

- [[wiki/sources/self-attention-mecanismo-transformers]] — explicação didática completa do mecanismo (tokens → embeddings → Q/K → attention score → output), com a ressalva de que a fonte não cobre V nem detalha o cálculo matemático exato
