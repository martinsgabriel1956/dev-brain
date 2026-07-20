---
type: concept
title: "Pipeline de Qualidade"
aliases: ["quality pipeline", "pipeline de código", "ci quality gates"]
date_created: 2026-05-31
date_updated: 2026-07-19
source_count: 5
tags: [pipeline-de-qualidade, harness, qualidade, ci-cd, testes, segurança, era-agentica, ratchet, npm-audit, under-engineering]
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

## Exemplo — Quality Gate de Qualidade de Modelo (não só de código)

Um quality gate não precisa se limitar a lint/tipagem/segurança de código — pode validar a qualidade de um *modelo de ML* embarcado no produto. Exemplo real: um app de transcrição por voz (Persua) mantém dois áudios de referência (um gravado por humano, um gerado por IA) a partir do mesmo texto-alvo. Todo PR aciona um workflow de CI que roda os modelos Whisper locais do projeto contra esses áudios, compara a transcrição gerada com o texto-alvo, calcula uma nota de qualidade e **falha o teste (bloqueando o merge) se a nota cair abaixo de um baseline definido**. Combinado com um segundo gate de qualidade de código (lint, duplicação, complexidade ciclomática), esse padrão permitiu ao autor delegar uma tarefa inteira a um agente — inclusive deixá-lo rodar sem supervisão por horas — com confiança de que nem dívida técnica nem regressão de qualidade do modelo passariam despercebidas.

## Exemplo Concreto — Pipeline com Ratchet de Baseline (npm audit em Dois Níveis)

[[wiki/sources/quality-gate-ratchet-multiplos-agentes-ia]] documenta um pipeline real, camada por camada: `npm ci` (instalação determinística) → `npm audit --audit-level critical` (bloqueia o merge) → `npm audit --audit-level high` (só avisa, não bloqueia — separar os dois níveis evita que uma vulnerabilidade de severidade média trave todo PR) → lint → testes com coverage (Jest) → um script de quality gate dedicado, que coleta métricas atuais (incluindo duplicação de código via `jscpd`) e as compara contra uma baseline congelada (ver [[wiki/concepts/ratchet-baseline]]). O diferencial em relação à descrição genérica desta página: os artefatos de coverage e relatórios são enviados como **upload de CI**, não apenas comentados no PR, especificamente para que o próprio agente de IA tenha acesso a eles durante o [[wiki/concepts/quality-gate|babysitting]] do pull request.

## Exemplo Mínimo — Pipeline de ~31 Linhas Como Piso Aceitável

[[wiki/sources/underengineering-overengineering-mario-souto]] descreve o outro extremo da escala em relação aos exemplos elaborados já documentados acima (ratchet, quality gate de modelo de ML): um pipeline de apenas dois workflows de GitHub Actions — lint e teste automatizado, cerca de 31 linhas de YAML no total — configurado como *required status check* via regra de proteção de branch (branch protection rule exigindo pull request + status checks aprovados antes do merge). O autor trata esse setup mínimo como o "caminho mínimo" que evita [[wiki/concepts/under-engineering]] sem exigir nenhuma das camadas mais sofisticadas da pipeline completa (mutação, complexidade ciclomática, SAST) — reforçando que "pipeline de qualidade" não é binário entre "nada" e "todas as sete camadas": mesmo duas camadas, obrigatórias via CI, já mudam o comportamento de um projeto pequeno.

## Key Sources

- [[wiki/sources/conteudo-tecnico-ia-robustez-sistemas]]
- [[wiki/sources/conteudo-tecnico-ia-hype-sistemas-robustos]]
- [[wiki/sources/html-vs-markdown-para-agentes-de-ia]] — exemplo concreto de quality gate para qualidade de transcrição (Whisper local), não apenas para qualidade de código
- [[wiki/sources/gate-de-qualidade-definicoes-formais]] — fundamentação teórica: cada camada desta pipeline é um [[wiki/concepts/quality-gate|quality gate]] no sentido formal (critérios de entrada/saída, resultado binário, disparo por critério não por data)
- [[wiki/sources/quality-gate-ratchet-multiplos-agentes-ia]] — pipeline concreto com npm audit em dois níveis de severidade, jscpd para duplicação, e artefatos de CI expostos para o próprio agente de IA consumir durante o babysitting do PR
- [[wiki/sources/underengineering-overengineering-mario-souto]] — pipeline mínimo de ~31 linhas (lint + teste) como piso aceitável contra under-engineering, sem exigir as camadas mais sofisticadas
