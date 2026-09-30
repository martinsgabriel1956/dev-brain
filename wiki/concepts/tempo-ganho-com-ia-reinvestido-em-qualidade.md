---
type: concept
title: "Tempo Ganho com IA Reinvestido em Qualidade"
aliases: ["reinvestir tempo da ia em qualidade", "dívida de qualidade adiada pelo time to market", "go horse e qualidade adiada"]
date_created: 2026-09-29
date_updated: 2026-09-29
source_count: 1
tags: [ia, qualidade, testes, quality-gate, ci-cd, time-to-market, divida-tecnica]
skill: tech-mentor-ai
status: stub
---

# Tempo Ganho com IA Reinvestido em Qualidade

## TL;DR

Segundo [[wiki/sources/dev-na-era-da-ia-qualidade-esteira-e-novas-preocupacoes]]: antes da IA, o *go horse* e o **time to market** empurravam para frente cobertura de testes, quality gate, melhorias de CI/CD e refatoração/revisão — porque o produto "paga a conta". Essas necessidades cresciam até virarem **crise**. Com o tempo de geração de código achatado ([[wiki/concepts/valor-do-codigo-com-tempo-achatado]]), a pergunta passa a ser **o que fazer com o tempo ganho**, e a resposta do autor é investir em qualidade: todo código novo sair com boa cobertura de testes.

## Como fazer (segundo a fonte)

- **Draft com IA, conhecimento seu:** a IA pode gerar os primeiros casos de teste, mas bons casos exigem conhecimento técnico **e de negócio** — construção conjunta, não delegação total.
- **IA para fortalecer a esteira** (gates, testes, linters), não para executá-la — ver [[wiki/concepts/ia-na-esteira-ci-cd]].
- **Aprender junto:** usar a IA para dominar ferramentas desconhecidas, sem terceirizar o entendimento.

## Ressalvas e ligações

- Coverage alto fica fácil com IA, mas cobertura ≠ qualidade: sem [[wiki/concepts/teste-de-mutacao]] e sem impedir que a IA enfraqueça testes ([[wiki/concepts/gaming-de-testes-por-ia]]), o tempo "reinvestido" vira número vazio.
- A infraestrutura que impõe isso: [[wiki/concepts/harness-de-qualidade]], [[wiki/concepts/quality-gate]].
- Dívida acumulada por falta de tempo: [[wiki/concepts/ciclo-da-desgraca-software]] (ciclo de pressão → atalho → crise).

## Key Sources

- [[wiki/sources/dev-na-era-da-ia-qualidade-esteira-e-novas-preocupacoes]]
