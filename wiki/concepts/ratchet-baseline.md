---
type: concept
title: "Ratchet (Catraca de Baseline)"
aliases: ["ratchet pattern", "catraca de qualidade", "baseline congelada", "regra de ouro do quality gate"]
date_created: 2026-07-19
date_updated: 2026-07-19
source_count: 1
tags: [ratchet, quality-gate, baseline, ci-cd, debito-tecnico, era-agentica]
skill: tech-mentor-testing
status: draft
---

# Ratchet (Catraca de Baseline)

Padrão de [[wiki/concepts/quality-gate|quality gate]] onde uma baseline de métricas de qualidade (violações de lint, % de duplicação de código, % de cobertura de testes, arquivos acima de um limite de tamanho, etc.) é congelada em um ponto no tempo, e uma regra bloqueia qualquer mudança que piore qualquer uma dessas métricas em relação à baseline — mesmo que a piora seja mínima (uma violação a mais, uma linha a mais, 0,1 ponto percentual a mais). O nome vem da mecânica de uma catraca: só é possível girar em um sentido. A partir da baseline congelada, o repositório só pode **melhorar** ou **empatar** — nunca regredir.

## Por que Congelar em Vez de Exigir um Padrão Ideal Direto

[[wiki/sources/quality-gate-ratchet-multiplos-agentes-ia]] é explícito sobre uma armadilha comum: se um quality gate for configurado contra um padrão de qualidade ideal (ex.: 0% de duplicação, 100% de cobertura) num projeto que nunca teve controle de qualidade, **todo PR vai falhar** — porque a base já está distante do ideal antes mesmo de a mudança em questão existir. A saída é medir o estado atual do projeto e usar isso como baseline: o gate não pergunta "este código é perfeito?", pergunta "este PR deixou as coisas piores do que já estavam?".

## A "Regra de Ouro"

> "Cada PR pode adicionar código, mas não pode aumentar nenhuma das métricas — nem por uma violação, nem por uma linha, nem por 0,1 ponto percentual."

Essa regra é o que torna o padrão sustentável mesmo quando ~100% do código é gerado por agentes de IA rodando em paralelo: a IA tem liberdade total para escrever código, mas não tem liberdade para piorar a saúde estrutural do projeto. Isso desloca a responsabilidade de "escrever bom código desde a primeira tentativa" para "não regredir em relação ao que já existe" — um critério objetivo e automatizável, ao contrário de um julgamento de qualidade subjetivo.

## Métricas Tipicamente Colocadas sob Ratchet

- Quantidade de violações de lint (ex.: ESLint)
- Percentual de duplicação de código (ex.: medido via `jscpd`)
- Percentual de cobertura de testes (ou, de forma equivalente, % de código não coberto)
- Quantidade de arquivos acima de um limite de tamanho definido

Cada uma dessas métricas tem seu próprio valor de baseline registrado (ex.: em um `baseline.json`), e um coletor de métricas roda em CI a cada PR para gerar um snapshot atual, comparado contra a baseline.

## Como o Baseline Evolui

O ratchet não é estático para sempre — a intenção declarada pela fonte é abrir, ao longo do tempo, PRs de refatoração dedicados especificamente a melhorar a baseline (reduzir violações, reduzir duplicação, aumentar cobertura, quebrar arquivos grandes), e então **re-congelar** a baseline no novo patamar melhor. A catraca avança em pequenos incrementos deliberados, não em saltos.

## Relação com Débito Técnico e Boy Scout Rule

O ratchet é uma versão automatizada e obrigatória do espírito da [[wiki/concepts/boy-scout-rule|Boy Scout Rule]] (deixar o código um pouco melhor a cada mudança) — mas em vez de depender da disciplina individual de quem edita o código (humano ou agente de IA), o critério é imposto mecanicamente pelo CI. Isso é particularmente relevante quando a maior parte do código passa a ser gerado por IA: não é mais possível confiar em "boa vontade" linha a linha, porque o volume de código gerado por sessão excede a capacidade de revisão manual — ver [[wiki/concepts/code-review]] sobre o gargalo humano nesse cenário.

## Relação com Architecture Fitness Functions

O ratchet de baseline generaliza a ideia de *architecture fitness function* (testes automatizados que impedem erosão arquitetural) para métricas de qualidade de código mais amplas — não só regras estruturais binárias ("domínio não pode importar infraestrutura"), mas métricas contínuas que só podem se mover em uma direção.

## Key Sources

- [[wiki/sources/quality-gate-ratchet-multiplos-agentes-ia]] — caso prático completo (projeto Strawberry): baseline real (483 violações ESLint, 2,2% duplicação, 7% cobertura, 19 arquivos acima do limite), regra de ouro, e plano de evolução via PRs de refatoração dedicados
