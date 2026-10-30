---
type: concept
title: "Eval de Revisor a Partir de Incidentes"
aliases: ["incidente vira caso de teste", "regressão do revisor", "post-mortem como eval"]
date_created: 2026-10-26
date_updated: 2026-10-26
source_count: 1
tags: [evals, code-review, post-mortem, regressao, agentes, anthropic]
skill: tech-mentor-ai
status: draft
---

# Eval de Revisor a Partir de Incidentes

Como a [[wiki/entities/anthropic]] sabe que o agente revisor é bom ([[wiki/sources/anthropic-code-review-por-agentes-sete-camadas]]):

1. **Todo incidente vira caso de teste**: PRs antigos que causaram incidentes, com seus consertos e reverts.
2. **Um engenheiro que conhece o código confirma** a causa (um revert nem sempre indica o PR culpado).
3. O caso confirmado entra no conjunto de evals; o que o revisor não pegou vira regra no CLAUDE.md, skill ou checagem nova ([[wiki/concepts/review-md]]).
4. **Qualquer mudança no revisor** — prompt, modelo, ferramenta — roda contra todos os casos antigos; se falha, recalibra.

É **teste de regressão aplicado ao revisor**, não só ao código: o apresentador diz ser a primeira vez que vê o paradigma assim. Análogo ao [[wiki/concepts/teste-de-regressao-de-prompt]] sobre um [[wiki/concepts/golden-dataset]] e ao uso de [[wiki/concepts/evals-llm]]; a fonte de casos é o [[wiki/concepts/blameless-post-mortem]].

## Medir o ruído pelo comportamento

A calibração também olha o que a pessoa fez com cada comentário (consertou / disse que errado / intencional / nitpick ignorado) para achar o ponto de equilíbrio entre pegar bugs e gerar falso positivo — ver [[wiki/concepts/ruido-e-loop-de-nitpick-em-revisao-por-agente]].

## Key sources

- [[wiki/sources/anthropic-code-review-por-agentes-sete-camadas]]
