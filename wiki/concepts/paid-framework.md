---
type: concept
title: "PAID Framework (Priorização de Dívida Técnica)"
aliases: ["PAID acronym", "performance architectural integration dependency"]
date_created: 2026-07-28
date_updated: 2026-07-28
source_count: 1
tags: [tech-debt, priorizacao, framework]
skill: tech-mentor-leadership
status: stub
---

# PAID Framework

## TL;DR

Mnemônico de quatro perguntas para decidir por onde começar a atacar dívida técnica, sem precisar de ferramenta de análise estática:

- **P**erformance impact — isso está deixando o app lento?
- **A**rchitectural importance — isso é central ao sistema ou uma feature marginal?
- **I**ntegration complexity — isso está amarrado a muitos outros sistemas?
- **D**ependency — mudar isso vai quebrar um monte de coisa?

## Como Usar

Aplicar as quatro perguntas a cada item candidato de dívida técnica; itens que respondem "sim" a mais perguntas (mais impacto de performance, mais central à arquitetura, mais integrado, mais dependências) sobem na prioridade. Combinar com a regra de Pareto — 80% da dor geralmente vem de 20% dos arquivos — para não precisar avaliar a base de código inteira.

## Limites

É um framework qualitativo e mnemônico, não uma metodologia com adoção de mercado documentada — mais próximo de uma heurística pessoal do autor da fonte do que de algo com origem acadêmica rastreável. Serve como ponto de partida rápido; para times que já têm ferramentas como SonarQube/CodeScene, o [[wiki/concepts/hotspot-analysis]] e o [[wiki/concepts/debt-ratio-sqale]] dão números mais objetivos.

## Relacionado

[[wiki/concepts/refactor-vs-rewrite-matrix]] — depois de priorizar com PAID, a próxima decisão é *como* pagar o item: refatorar ou reescrever.

## Key Sources

- [[wiki/sources/tech-debt-guia-completo-gestao-metricas]]
