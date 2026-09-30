---
type: concept
title: "Retrospectiva de Erros de IA (Feedback para o Gerador de Código)"
aliases: ["retro com ia", "cerimônia de feedback para ia", "lições aprendidas com llm", "feedback loop de erros de ia"]
date_created: 2026-09-29
date_updated: 2026-09-29
source_count: 1
tags: [ia, harness-engineering, retrospectiva, feedback, qualidade, agentes, lições-aprendidas]
skill: tech-mentor-ai
status: stub
---

# Retrospectiva de Erros de IA (Feedback para o Gerador de Código)

## TL;DR

Problema levantado em [[wiki/sources/dev-na-era-da-ia-qualidade-esteira-e-novas-preocupacoes]]: na retrospectiva de sprint clássica, o time olhava o que deu errado e registrava lições aprendidas para não repetir os erros. Com a LLM gerando o código, **qual é a cerimônia equivalente?** Se ocorre um bug, foi porque a IA não seguiu um padrão de código (meu ou da empresa)? Ou porque a regra de negócio estava desatualizada? E como dar feedback eficiente à IA para que **cada nova geração não caia no mesmo erro**?

A fonte formula a pergunta e diz que *harness engineering* dá uma visão, mas que "vai muito além" — **não propõe solução**.

## Diagnóstico em duas causas (da fonte)

| Causa do bug | O que corrigir |
|---|---|
| A IA **não seguiu** um padrão de código (pessoal ou da empresa) | Tornar o padrão **imposto**, não pedido: regra/linter/gate — ver [[wiki/concepts/harness-de-qualidade]], [[wiki/concepts/quality-gate]] |
| A **regra de negócio** estava desatualizada | Atualizar a fonte de verdade (docs/spec/contexto) que a IA lê |

## Caminhos plausíveis já presentes na wiki (inferência, não da fonte)

- Transformar a lição em **regra/skill/instrução** carregada automaticamente: [[wiki/concepts/skills-agente]], [[wiki/concepts/rules-agente]], [[wiki/concepts/agents-md-vs-claude-md]].
- Fechar o ciclo automaticamente (o agente aprende com a falha e cria/atualiza skill): [[wiki/concepts/closed-loop-skill-learning]].
- Todo bug vira um **caso novo em teste/eval** (golden dataset), para o erro não voltar: [[wiki/concepts/llm-evals-testing]]. [skill: tech-mentor-ai, `llm-testing.md`] recomenda adicionar caso ao golden dataset a cada bug de produção.
- Preferir sensor determinístico a instrução em prosa quando possível: [[wiki/concepts/sensores-vs-guias]].
- Cuidado: uma lição mal formulada pode virar skill/regra que **piora** o modelo (relato da própria fonte sobre skills que "deixam a LLM burra") — medir antes de adotar.

## Open Questions

- Quem conduz a cerimônia e com que periodicidade (por bug? por sprint)?
- Como saber se a regra nova reduziu a recorrência do erro (métrica)?

## Key Sources

- [[wiki/sources/dev-na-era-da-ia-qualidade-esteira-e-novas-preocupacoes]]
