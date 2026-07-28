---
type: source
title: "Dívida Técnica: Guia Completo de Gestão e Métricas"
aliases: ["everything about technical debt", "guia completo tech debt", "SQALE", "debt ratio", "PAID framework"]
date_created: 2026-07-28
date_updated: 2026-07-28
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/tech-debt-guia-completo-gestao-metricas.md
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-07-28
source_count: 0
tags: [tech-debt, fowler, sqale, debt-ratio, hotspot-analysis, paid-framework, refactor-vs-rewrite, tdd, pair-programming, boy-scout-rule, dora, exec-communication]
skill: tech-mentor-leadership
status: stable
---

## TL;DR

Vídeo-transcrição de tom introdutório/prático sobre dívida técnica: revisita o Quadrante de Fowler e a analogia com dívida financeira (já registrados na wiki), mas acrescenta camada nova de **mensuração formal** — fórmula de debt ratio (`remediation cost / development cost`) com faixas de risco ao estilo SonarQube, modelo de três fatores (impacto × custo fixo × espalhamento) para priorização, framework **PAID** (Performance/Architectural/Integration/Dependency) e uma matriz 2×2 de refatorar-vs-reescrever baseada em valor de negócio × risco técnico. Também documenta dois modelos concretos de alocação de tempo (regra dos 20% e regra dos 25% do Shopify) e um template de business case para comunicar dívida a stakeholders não técnicos.

## Key Claims

**Claim:** Times gastam em média 23-42% do tempo lidando com dívida técnica, o que desacelera a velocidade de desenvolvimento em cerca de 20-40% — o mesmo range que orçamentos de TI alocam para tratar o problema.
**Evidence:** Fonte cita isso como resultado de pesquisa (sem nomear o estudo original) — apresentado como um "número mágico" que se repete em três métricas independentes (tempo gasto, perda de velocidade, orçamento alocado).
**Confidence:** média — números citados sem link para o estudo primário, mas consistentes com a ordem de grandeza citada em outras fontes já registradas na wiki (ex. [[wiki/concepts/tech-debt-como-ferramenta]]).

**Claim:** O ratio de dívida técnica é calculável como `remediation cost / development cost`, com faixas de risco: <5% saudável, 5-10% ok mas monitorar, 10-20% risco moderado, >20% "briga com a base de código a cada passo".
**Evidence:** Fórmula descrita como a mesma usada por ferramentas como SonarQube (SQALE — Software Quality Assessment based on Lifecycle Expectations). Exemplo dado: $100k de remediation cost sobre $500k de development cost = 20% debt ratio.
**Confidence:** alta — fórmula e faixas batem com a documentação pública do método SQALE/SonarQube.

**Claim:** Priorizar dívida técnica por um modelo de três fatores — impacto, custo fixo de correção, espalhamento pela base de código — é mais eficiente que atacar dívida aleatoriamente.
**Evidence:** Descrito como "modelo triângulo"; o autor admite não achar muita documentação formal sobre o nome exato do modelo, mas o aplica como heurística de priorização (equivalente em espírito ao "Debt Register" com score de Impacto×Risco×Facilidade documentado em `references/tech-debt-management.md` da skill de liderança).
**Confidence:** média — heurística útil, mas sem fonte acadêmica única e nomeada.

**Claim:** O framework PAID (Performance impact, Architectural importance, Integration complexity, Dependency) combinado com a regra de Pareto (80% da dor vem de 20% dos arquivos) permite montar um roadmap de priorização de dívida técnica sem precisar de ferramentas complexas.
**Evidence:** Apresentado como "modelo simples" alternativo/complementar ao SQALE e ao modelo de três fatores — quatro perguntas binárias por item de dívida.
**Confidence:** média — framework mnemônico do autor, não uma metodologia com adoção de mercado documentada.

**Claim:** A decisão entre refatorar e reescrever segue uma matriz 2×2 de valor de negócio × risco técnico: alto valor + baixo risco = refatorar; alto valor + alto risco = reescrever; baixo valor + baixo risco = conviver; baixo valor + alto risco = depreciar.
**Evidence:** Reforçado por um caso de falha citado (não nomeado): empresa que reescreveu um sistema inteiro em vez de refatoração direcionada e ficou 18 meses sem entregar nenhuma feature nova.
**Confidence:** alta na lógica da matriz; o caso de falha é citado sem nome/fonte verificável.

**Claim:** A regra dos 25% do Shopify (10% dívida diária + 10% dívida semanal + 5% dívida mensal/anual) é mais granular que a regra genérica dos 20% por sprint, porque distingue explicitamente dívida "encontrada no fluxo de trabalho normal" (fricção ao implementar algo) de dívida "planejada e agendada" no board do projeto.
**Evidence:** Descrito com números concretos: 4h/semana de dívida diária, 16h/semana de dívida semanal dividida entre um time de 4 pessoas, e 2 reuniões de 1h/semana para dívida mensal/anual — mas a fonte não cita onde encontrou essa informação sobre o Shopify (não é primária).
**Confidence:** média — mecânica interna plausível e detalhada, mas sem link/fonte primária do Shopify citado.

**Claim:** O caso Knight Capital é citado como exemplo de dívida técnica descontrolada, com perda de "$462 milhões".
**Evidence:** Citado de passagem, sem detalhamento do incidente. O valor de perda amplamente documentado publicamente para o incidente Knight Capital (agosto de 2012, código morto reativado por engano num deploy) é de aproximadamente **US$ 440-460 milhões** em cerca de 45 minutos — o número da fonte (\$462M) está dentro dessa faixa comumente citada, mas não há uma fonte primária no vídeo para o valor exato.
**Confidence:** média — o incidente é real e bem documentado externamente [external], mas o valor específico citado pela fonte não vem acompanhado de referência.

## Entities & Concepts Touched

- [[wiki/concepts/quadrante-de-fowler]]
- [[wiki/concepts/tech-debt-como-ferramenta]]
- [[wiki/concepts/boy-scout-rule]]
- [[wiki/concepts/tdd]]
- [[wiki/concepts/pair-programming]]
- [[wiki/concepts/pipeline-de-qualidade]]
- [[wiki/concepts/dora-metrics]]
- [[wiki/concepts/debt-ratio-sqale]]
- [[wiki/concepts/paid-framework]]
- [[wiki/concepts/refactor-vs-rewrite-matrix]]
- [[wiki/concepts/hotspot-analysis]]
- [[wiki/entities/knight-capital]]
- [[wiki/entities/martin-fowler]]

## Open Questions

- Qual é a fonte primária dos números "23-42% do tempo" e "20-40% de desaceleração"? A fonte não cita o estudo original — vale reconciliar se algum outro material da wiki citar o mesmo dado com origem nomeada.
- O "modelo de três fatores" (impacto/custo fixo/espalhamento) não tem nome ou origem acadêmica confirmada — pode ser uma reformulação pessoal do autor do vídeo de heurísticas já conhecidas (como o próprio Debt Register da skill de liderança). Não tratar como framework com autoria estabelecida até achar fonte primária.
- Valor exato da perda do caso Knight Capital: a fonte cita "$462 milhões"; fontes públicas amplamente citadas mencionam "~$440-460 milhões" — não é uma contradição forte, mas o número específico não foi confirmado com uma fonte primária dentro deste ingest.

## Fontes Relacionadas

Nenhuma fonte na wiki cobre ainda a camada de **mensuração formal** de dívida técnica (SQALE/debt ratio, PAID, matriz refatorar-vs-reescrever) — esta é a primeira. As fontes existentes ([[wiki/sources/5-principles-that-changed-me-as-a-programmer]], [[wiki/sources/o-que-e-refatoracao-quando-usar]], [[wiki/sources/cognitive-debt-margaret-storey]]) cobrem o Quadrante de Fowler e a fronteira entre refatoração oportunista e débito formal, mas nenhuma trazia fórmulas de cálculo ou frameworks de priorização quantitativos. Complementar, não contraditório.
