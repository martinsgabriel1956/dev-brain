---
type: concept
title: "Design Discussion"
aliases: ["discussão de design", "design before code"]
date_created: 2026-05-04
date_updated: 2026-05-04
source_count: 1
tags: [coding-agents, workflow, rpi, planning]
skill: tech-mentor-ai
status: draft
---

# Design Discussion

Fase de alinhamento que substitui o plano de implementação detalhado no [[concepts/rpi-workflow]]. Em vez de pedir ao agente um plano de 1.000 linhas com arquivos, funções e imports, você conduz uma **conversa sobre o design** — focando no entendimento mútuo, não no código que vai ser gerado.

## Diferença do Plano Tradicional

| | Plano Tradicional | Design Discussion |
|---|---|---|
| Foco | O que vai ser gerado | Como a solução vai funcionar |
| Tamanho | 500–1.000 linhas | ~200 linhas |
| Tempo de revisão | Equivalente ao código | ~10 minutos |
| Quando corrige erro | Tarde (já planejou tudo) | Cedo (ainda não escreveu nada) |
| Output | Lista de mudanças | Entendimento compartilhado |

## Analogia

É a diferença entre revisar a planta de um edifício e revisar a construção depois que as paredes já foram levantadas. A planta é muito mais fácil de mudar — e uma discussão de design de 200 linhas é a planta.

## Como Conduzir

1. Descrever o problema/feature para o agente
2. Pedir para o agente explicar **como** ele abordaria a solução — qual pattern, quais trade-offs, qual ordem
3. Questionar a abordagem, propor alternativas, realinhar se necessário
4. Só então passar para a fase de implement

A discussão de design não gera código. Ela calibra a direção **antes** de qualquer linha ser escrita.

## Quando Não É Necessário

Para tasks simples (mudar a cor de um botão, ajustar um texto), a design discussion é overkill. O RPI completo — com research, design discussion e implement separados — é para features médias a complexas. Ver [[concepts/rpi-workflow]] para o guia de calibragem.

## Key Sources

- [[sources/erros-workflow-research-plan-implement]]
