---
type: concept
title: "Emergent Ability"
aliases: ["capacidade emergente", "emergência em LLMs", "emergent capabilities"]
date_created: 2026-05-17
date_updated: 2026-05-17
source_count: 1
tags: [llm, scaling, emergência, raciocínio, chain-of-thought]
skill: tech-mentor-ai
status: draft
---

# Emergent Ability

## Definição

Capacidade que **não existe em modelos pequenos** e aparece abruptamente quando o modelo ultrapassa um certo limiar de escala — sem que tenha sido explicitamente treinada para isso. Contrasta com as [[scaling-laws]] suaves: a maioria das métricas melhora gradualmente, mas certas capacidades emergem de forma não-linear.

Formalizado em Wei et al. (2022b) "Emergent Abilities of Large Language Models" [external] e exemplificado empiricamente em [[wiki/sources/chain-of-thought-prompting]].

## Exemplo Canônico: Chain-of-Thought

[[chain-of-thought]] prompting é o exemplo mais documentado:

- Modelos < ~100B parâmetros: geram cadeias fluentes mas ilógicas → performance igual ou **pior** que standard prompting
- Modelos ≥ ~100B parâmetros: raciocínio encadeado correto → ganhos expressivos

O limiar não é uma fronteira nítida, mas a transição é muito mais abrupta do que as scaling laws suaves preveem.

## Por que Emergência Acontece?

Hipóteses (nenhuma definitiva):

1. **Composição de sub-habilidades** — raciocínio requer compreensão semântica + mapeamento simbólico + aritmética + fidelidade ao contexto; cada uma melhora gradualmente, mas a composição exige que todas estejam acima de um threshold simultaneamente.
2. **Quantidade de padrões absorvidos** — modelos maiores, treinados em mais dados, viram mais exemplos de raciocínio explícito no corpus.
3. **Artefato de métrica** — algumas "emergências" podem ser artefatos de métricas não-lineares (ex: acurácia exata vs. partial credit).

## Implicações Práticas

- Técnicas como CoT **não devem ser testadas em modelos pequenos** para validar sua utilidade — o sinal é enganoso.
- Ao escolher modelo para produção, checar se a capacidade que você precisa já emergiu naquela escala.
- Emergência dificulta previsão — [[scaling-laws]] não cobrem bem esse fenômeno.

## Relação com Outros Conceitos

- [[scaling-laws]] — emergência é o fenômeno que as scaling laws suaves não capturam bem
- [[chain-of-thought]] — exemplo canônico de capacidade emergente
- [[few-shot-learning]] — também melhora de forma não-linear com escala
- [[foundation-model]] — modelos treinados a escala suficiente para que emergências ocorram

## Fontes

- [[wiki/sources/chain-of-thought-prompting]]
- Wei et al. (2022b) — "Emergent Abilities of Large Language Models" [external]
