---
type: concept
title: "Limites Empíricos da Revisão por IA"
aliases: ["revisor de IA em código fechado", "agente constrói o que não consegue verificar", "PR de agente precisa de mais fix"]
date_created: 2026-10-26
date_updated: 2026-10-26
source_count: 1
tags: [code-review, agentes, evidencia, papers, generalizacao, testes]
skill: tech-mentor-ai
status: draft
---

# Limites Empíricos da Revisão por IA

Três papers citados oralmente em [[wiki/sources/anthropic-code-review-por-agentes-sete-camadas]] para temperar o caso da [[wiki/entities/anthropic]]. **Nenhum foi verificado nesta ingestão** (links só na descrição do vídeo).

| Estudo | Resultado | Leitura |
|---|---|---|
| Benchmark de revisores (Microsoft, segundo o apresentador) — 1.000 tarefas com bugs reais, parte de 98 repositórios abertos, parte de repositórios fechados de uma empresa | 71% dos bugs nos 5 primeiros comentários em código aberto; desempenho **despenca** em código fechado | A Anthropic revisa código público que o modelo conhece: **melhor caso possível**. Ver [[wiki/entities/microsoft]] |
| ETH Zurique — agente escreve suíte de testes a partir da spec | até 88% dos testes passam na suíte válida, mas pegam **<60%** dos bugs plantados | "O agente constrói software que ele não consegue verificar" → não confiar em testes gerados sem [[wiki/concepts/harness-de-qualidade]] independente |
| 67.774 PRs de agentes mergeados vs 5.000 humanos | PR de agente precisa de fix posterior ~**1,5×** mais; ~70% dos fixes feitos pelo próprio agente | Agentes terminam o próprio serviço, mas geram mais retrabalho |

## Conta dos reverts

Reverts: proporção −40% (jun→set) e PRs mergeados ×2+ → em número absoluto o total pode subir; melhorou *por PR*, não necessariamente *por dia*. (Inferência do apresentador sobre dados da Anthropic.)

## Aplicabilidade

Custo (agentes paralelos + verificação + classificadores + evals diários), código público e token "infinito" tornam parte do pipeline irreplicável; o que dá para copiar sem custo: contexto limpo, [[wiki/concepts/review-md]], erro repetido → regra, teto de rodadas e aprovação de bot ≠ de pessoa. Relaciona-se a [[wiki/concepts/code-review]] e [[wiki/concepts/julgar-codigo-fora-de-contexto]].

## Key sources

- [[wiki/sources/anthropic-code-review-por-agentes-sete-camadas]]
