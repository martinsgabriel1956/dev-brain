---
type: concept
title: "Confidencialidade de Dados em Prompts de IA"
aliases: ["nao jogar dado sigiloso na ia", "confidencialidade prompt", "vazamento de dados via chatgpt"]
date_created: 2026-07-03
date_updated: 2026-07-03
source_count: 1
tags: [ia, seguranca, confidencialidade, dados-sensiveis]
skill: tech-mentor-ai
status: stub
---

# Confidencialidade de Dados em Prompts de IA

Princípio: código-fonte, dados de negócio ou qualquer informação corporativa sigilosa não deve ser colada em ferramentas de IA de terceiros (ex.: ChatGPT) que não rodam dentro dos limites da empresa. Fazer isso expõe informação crítica a um sistema fora do controle da organização.

## Por que importa

Um arquiteto pode usar IA para brainstorm de arquitetura, discutir alternativas e explicar trade-offs — mas o prompt não pode carregar dados sigilosos do negócio para isso. Se o modelo não roda dentro da empresa (self-hosted, VPC, contrato de processamento de dados adequado), qualquer dado sensível colado ali já saiu do perímetro de controle da organização.

## Relação com outros conceitos

- [[wiki/concepts/vibe-coding]] — o mesmo cuidado se aplica ao usar IA para gerar código a partir de contexto de negócio real
- [[wiki/concepts/arquitetura-de-software]] — brainstorm de arquitetura com IA precisa acontecer sem detalhes sigilosos concretos da empresa

## Key Sources

- [[wiki/sources/vibe-coding-limites-maturidade-profissional]]
