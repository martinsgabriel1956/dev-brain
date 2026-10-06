---
type: concept
title: "Trava Determinística no Harness (Princípio de Hashimoto)"
aliases: ["trava determinística", "deterministic guard", "erro vira trava"]
date_created: 2026-10-06
date_updated: 2026-10-06
source_count: 1
tags: [harness, determinismo, hashimoto, guardrail, feedback-loop, harness-engineering]
skill: tech-mentor-ai
status: stub
---

# Trava Determinística no Harness

Quando o agente erra, a resposta de engenharia não é só reescrever o prompt: é **mudar o harness** para que aquele erro se torne impossível (ou detectado automaticamente). Atribuído a [[wiki/entities/mitchell-hashimoto]] em [[wiki/sources/harness-engineering-dicionario-do-programador-guias-sensores]].

## Ideia

- Prompt é probabilístico: corrigir "no braço" reduz a chance, não a elimina.
- Trava determinística (teste, linter, type check, hook, permissão, validador) falha **sempre** que a condição ocorre — vira [[wiki/concepts/sensores-vs-guias|sensor]] permanente ou [[wiki/concepts/hooks-agente|hook]].
- Cada erro vira ativo do repositório; o harness só melhora com o tempo.

## Relações

[[wiki/concepts/harness]] · [[wiki/concepts/harness-de-qualidade]] · [[wiki/concepts/determinismo-vs-probabilismo-em-ia]] · [[wiki/concepts/ai-safety-guardrails]]

## Key Sources

- [[wiki/sources/harness-engineering-dicionario-do-programador-guias-sensores]] — enunciado do princípio (relato do áudio, sem link para o texto original de Hashimoto `[external, não verificado]`)
