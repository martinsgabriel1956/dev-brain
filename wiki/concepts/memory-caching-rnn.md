---
type: concept
title: "Memory Caching (RNN)"
aliases: ["MC", "Memory Caching: RNNs with Growing Memory"]
date_created: 2026-10-09
date_updated: 2026-10-09
source_count: 1
tags: [ai, rnn, memory-caching, eficiencia, google-research, paper]
skill: tech-mentor-ai
status: draft
---

## Definição

Técnica do paper *Memory Caching: RNNs with Growing Memory* (Behrouz et al., Google Research/Cornell/USC; arXiv 2602.24281, fev/2026; ICML 2026) [external: https://arxiv.org/abs/2602.24281]. Em vez de um único estado de memória fixo, a [[wiki/concepts/recurrent-neural-network|RNN]] **guarda checkpoints** dos estados ocultos ao longo da sequência; a memória efetiva cresce com o comprimento. Fica **entre** o custo O(L) da RNN e o O(L²) do [[wiki/concepts/transformer-architecture|Transformer]].

## O que a fonte afirma

- Gargalo da RNN = memória fixa; a solução não é uma nova atenção, é **cachear estados**.
- 1,3B de parâmetros: Transformer 53,19 vs Titans+MC 58,33 (média de language modeling + common sense reasoning).
- **Não** significa que a RNN supera o Transformer em geral; no paper, Transformers ainda lideram em recall *in-context* [external].
- Potencial para [[wiki/concepts/needle-in-a-haystack]].

## Por que importa

Exemplo de pesquisa de **eficiência** (menos custo por token de contexto), o eixo em que a fonte diz que o [[wiki/entities/google]] lidera — ver [[wiki/entities/google-research]]. Relaciona-se a [[wiki/concepts/context-window]] e à discussão de custo de contexto longo.

## Ressalvas

Só um experimento citado; escala >1,3B e custo real de inferência não discutidos na fonte.

## Key Sources

- [[wiki/sources/google-nao-esta-perdendo-corrida-ia-memory-caching-gemini-live]]
