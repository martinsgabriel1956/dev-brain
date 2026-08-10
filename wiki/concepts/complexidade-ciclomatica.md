---
type: concept
title: "Complexidade Ciclomática"
aliases: ["cyclomatic complexity", "CCN", "cyclomatic complexity number"]
date_created: 2026-08-04
date_updated: 2026-08-10
source_count: 2
tags: [complexidade-ciclomatica, quality-gate, analise-estatica, sonarqube, harness]
skill: tech-mentor-ai
status: stub
---

# Complexidade Ciclomática

## TL;DR

Métrica que conta quantos **caminhos de execução independentes** existem dentro de uma função: cada `if`, `else`, `case` ou chamada que abre um novo ramo soma ao total (também chamado de CCN — cyclomatic complexity number). Diferente do [[wiki/concepts/big-o|Big-O]], que mede custo assintótico de execução, complexidade ciclomática mede o quanto uma função é difícil de ler, testar e cobrir com casos — um algoritmo pode ser eficiente (Big-O baixo) e ainda assim ter CCN alto.

## Por Que Importa em Código Gerado por IA

[[wiki/sources/quatro-tecnicas-ci-cd-gate-qualidade-codigo-ia-uncle-bob]] identifica um padrão específico de LLMs: tendência a gerar funções longas (exemplo citado: ~120 linhas) com muitos `if`s aninhados, tentando cobrir todos os casos dentro de uma função só em vez de decompor o problema. Isso é detectável de forma determinística e barrável no CI — a fonte cita como exemplo prático um limite de CCN entre 1 e 20, acima do qual o pull request é reprovado automaticamente, com SonarQube como ferramenta usada pelo autor para esse gate.

Essa métrica já era citada, sem página própria até esta ingestão, como um dos componentes listados em [[wiki/concepts/harness-de-qualidade]] ("Ferramentas que medem complexidade ciclomática na pipeline. Feedback objetivo: se a função está complexa demais, não commita.").

## Relação com Módulo Profundo e Tamanho de Módulo

Complexidade ciclomática mede o *interior* de uma função; [[wiki/concepts/god-object|tamanho de módulo]] mede o *tamanho do arquivo* como um todo. Os dois gates são complementares: uma função pode estar dentro do limite de linhas do arquivo e ainda assim ter complexidade ciclomática alta se concentrar muitos caminhos condicionais num espaço pequeno.

## Key Sources

- [[wiki/sources/quatro-tecnicas-ci-cd-gate-qualidade-codigo-ia-uncle-bob]] — definição operacional (contagem de caminhos), padrão de LLMs gerando funções com muitos `if`s aninhados, exemplo de limite bloqueante (CCN 1–20) e ferramenta (SonarQube)
- [[wiki/sources/por-que-code-bases-degradam-estrategias-code-rot]] — cita complexidade ciclomática como ferramenta de apoio contra code rot, com a ressalva da [[wiki/concepts/goodharts-law|Lei de Goodhart]]: útil como sinal, nociva quando vira meta
