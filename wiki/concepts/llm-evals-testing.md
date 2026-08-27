---
type: concept
title: "Testes e Evals de Sistemas com IA"
aliases: ["llm evals", "avaliação de agentes", "promptings", "testes de prompt"]
date_created: 2026-08-14
date_updated: 2026-08-27
source_count: 2
tags: [testes, evals, llm, agentes-ia, qualidade, ci-cd]
skill: tech-mentor-testing
status: stub
---

# Testes e Evals de Sistemas com IA

Equivalente, para sistemas com LLM, dos testes automatizados de uma aplicação tradicional — mas testando **prompts e contextos** ("promptings") em vez de apenas lógica determinística. Necessário porque a IA se comporta de forma **não determinística**: os mesmos `if`/`else` que garantem previsibilidade em software tradicional não existem aqui.

## O que os frameworks de eval fazem

- Criam componentes de prompt testáveis, isolados do restante da aplicação
- Recebem pares de entrada/saída desejados e ajustam o prompt automaticamente, gerando variações até melhorar o resultado
- Avaliam agentes contra **datasets reais** e **snapshots** de comportamento esperado, permitindo rodar testes mais determinísticos para garantir que mudanças em modelo, código ou prompt mantêm (ou melhoram) o comportamento anterior

Ferramentas citadas no mercado: LangSmith. Plataformas de observabilidade tradicionais (Datadog, New Relic) também vêm incorporando agentes de IA embutidos para apoiar esse processo.

## Relação com Versionamento de Prompt

Evals são o mecanismo natural de gate em CI/CD para [[wiki/concepts/prompt-engineering|versionamento de prompt]]: uma nova versão de prompt só deveria subir se passar no conjunto de snapshots/dataset já validado — o equivalente a um teste de regressão para comportamento de LLM.

## Evals Como Parte da Observabilidade do Harness ("How We Know It Works")

[[wiki/sources/harness-anatomia-tecnica-alem-do-claude-md]] enquadra evals dentro da camada de observabilidade de um [[wiki/concepts/harness|harness]], ao lado de logs, custo por token e retries — não como categoria isolada. Resume a função dos evals numa frase: é assim que se sabe, de fato, que um agente construído está funcionando para a tarefa que foi desenhado para resolver ("how we know it works"). A fonte nota que essa camada completa (incluindo evals) é menos universal entre ferramentas comerciais fechadas do que em agentes customizados — reforçando que "ter evals" é uma decisão de harness, não algo garantido pela ferramenta usada.

## Relação com Outros Conceitos

- [[wiki/concepts/context-engineering-harness]] — os "sensores" (testes, linter, LLM de revisão) que dão feedback ao harness incluem evals como sensor específico de qualidade de prompt/agente.
- [[wiki/concepts/agente-ia]] — evaluation citada como resposta prática ao comportamento não determinístico de arquiteturas de agente.
- [[wiki/concepts/observabilidade]] — evals cobrem qualidade pré-deploy; observabilidade cobre comportamento em produção — complementares, não substitutos.

## Key Sources

- [[wiki/sources/harness-anatomia-tecnica-alem-do-claude-md]] — evals enquadrados como parte da camada de observabilidade do harness, resumidos como "how we know it works"
- [[wiki/sources/8-pontos-arquitetura-de-software-na-era-da-ia]] — testes de prompt/contexto, frameworks de eval, uso de dataset+snapshot para comportamento determinístico, LangSmith
