---
type: concept
title: "Pipeline de Qualidade"
aliases: ["quality pipeline", "pipeline de código", "ci quality gates"]
date_created: 2026-05-31
date_updated: 2026-05-31
source_count: 1
tags: [pipeline-de-qualidade, harness, qualidade, ci-cd, testes, segurança, era-agentica]
skill: tech-mentor-backend
status: stable
---

# Pipeline de Qualidade

## TL;DR

Sequência automatizada de verificações que o código precisa passar antes de ser commitado ou mergeado. Na [[era-agentica]], é o mecanismo que garante [[robustez-de-sistemas]] quando a velocidade de geração de código aumentou drasticamente. Determina a qualidade de forma **determinística** — passa ou não passa — independente do julgamento da IA.

## Por que É Central Agora

A IA gera código rapidamente. Sem pipeline de qualidade, velocidade de geração = velocidade de acumulação de débito técnico. Com pipeline, cada commit precisa passar por um conjunto de critérios objetivos antes de existir.

> *"Você consegue com a harness ter um ferramental que roda de maneira determinística. Não é o que a IA acha — a ferramenta passou ou não passou."*

## Camadas da Pipeline

```
[1. Formatação e Lint]
    ↓ Biome / ESLint / Prettier / Black / rustfmt
    ↓ Regras de estilo e padrões do projeto

[2. Tipagem e Compilação]
    ↓ TypeScript, mypy, javac
    ↓ Erros de tipo detectados antes de rodar

[3. Testes Unitários + Coverage]
    ↓ Jest / Pytest / JUnit
    ↓ Coverage mínimo configurado (ex: 80%)

[4. Complexidade Ciclomática]
    ↓ Ferramentas de análise de complexidade
    ↓ Funções com complexidade > N são rejeitadas

[5. Análise Estática de Segurança]
    ↓ Semgrep / Bandit / CodeQL / Snyk
    ↓ Vulnerabilidades conhecidas detectadas

[6. Testes de Mutação]
    ↓ Stryker / PIT / Mutmut
    ↓ Mutation score mínimo configurado

[7. Testes de Integração / E2E]
    ↓ Playwright / Cypress / Testcontainers
    ↓ Fluxos críticos do negócio validados
```

Cada camada é um **quality gate**: se falhar, o código não avança.

## O que a IA Faz em Cada Camada

| Camada | Papel da IA |
|--------|------------|
| Lint/formatação | Segue as regras que o linter rejeita |
| Testes | Gera testes unitários em volume |
| Cobertura | Eleva coverage de forma antes impraticável manualmente |
| E2E | Gera o ferramental de teste quando você especifica os fluxos |
| Segurança | **Não confie** — use ferramenta determinística |

## Diferença de Harness de IA

[[harness-de-qualidade]] é o conceito mais amplo (inclui TDD, revisão de PR, cultura). Pipeline de qualidade é a parte automatizada e executável desse harness — o que roda em CI/CD.

## Construindo com IA

Hoje é mais fácil do que nunca criar o ferramental completo:
- "Crie um workflow GitHub Actions que roda linter, testes, coverage e Semgrep"
- A IA gera o YAML; você revisa as regras de negócio
- Uma vez configurado, a pipeline roda para todo código gerado pela mesma IA

## Key Sources

- [[wiki/sources/conteudo-tecnico-ia-robustez-sistemas]]
- [[wiki/sources/conteudo-tecnico-ia-hype-sistemas-robustos]]
