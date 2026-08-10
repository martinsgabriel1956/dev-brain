---
type: source
title: "O Paradoxo da Aceleração — 93% dos devs usam IA, produtividade sobe 10%"
aliases: ["paradoxo da aceleracao", "acceleration paradox", "faros ai productivity", "93% devs ia 10% produtividade"]
date_created: 2026-08-10
date_updated: 2026-08-10
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/paradoxo-da-aceleracao-ia-produtividade-metricas.md
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-08-10
source_count: 0
tags: [ia-produtividade, engineering-metrics, code-review, dora, goodharts-law, faros-ai, pragmatic-engineer, output-vs-outcome, ia-amplificador, tech-lead]
skill: tech-mentor-leadership
status: stable
---

## TL;DR

93% dos devs usam IA para escrever código, mas o ganho real de produtividade no nível da empresa é só 10% — apesar de os devs, individualmente, fazerem 21% mais tarefas e merge de quase o dobro de PRs. O gargalo migrou da **escrita** para a **revisão**: tempo de code review subiu 91% e não escalou junto. A Faros AI chama isso de **paradoxo da aceleração** — mais velocidade individual, mais atrito no sistema. Pior: 95% dos devs se *sentem* mais produtivos enquanto produzem código de qualidade menor (dissociação percepção × realidade). A IA age como **amplificador sem julgamento**: juniores em tarefas simples ganham 26–56%, mas sêniors em codebase legado têm ganho zero ou negativo. O problema não é a IA — é medir **output** (volume, velocidade) em vez de **outcome** (bug rate, ciclo de review, facilidade de mudar o sistema).

## Key Claims

**Claim:** Adoção de IA (93%) e ganho de produtividade organizacional (10%) estão radicalmente descolados.
**Evidence:** Pesquisa Faros AI sobre times de engenharia reais (dado de produção, não satisfação): 93% de adoção vs. 10% de ganho real de produtividade da empresa.
**Confidence:** média (número da fonte primária Faros AI, não cross-checado de forma independente)

**Claim:** O ganho individual é real e grande, mas não sobe para o nível da empresa.
**Evidence:** Devs fazem 21% mais tarefas e merge de quase o dobro de PRs individualmente; ainda assim o time cresce só 10%. Mesmo padrão de "vazamento" descrito em [[wiki/concepts/roi-de-ia]].
**Confidence:** alta (consistente com múltiplas fontes já na wiki)

**Claim:** O gargalo migrou da escrita para a revisão de código.
**Evidence:** Tempo de code review aumentou 91%. A revisão exige atenção humana, contexto do sistema e julgamento — a IA não resolve isso e ainda gera mais código para revisar. Código gerado por IA não é mais simples de revisar; às vezes é mais difícil.
**Confidence:** alta

**Claim:** Existe dissociação entre percepção e realidade de produtividade.
**Evidence:** 95% dos devs se sentem mais produtivos com IA, mas objetivamente produzem código de qualidade menor na mesma pesquisa. O risco não é a sensação ser "ruim" — é métricas erradas gerarem decisões erradas.
**Confidence:** média

**Claim:** A IA é um amplificador do que já existe — beneficia juniores em tarefas simples e prejudica sêniors em legado.
**Evidence:** Survey do Pragmatic Engineer (>90 devs, 2026): juniores em tarefas simples ganham 26–56%; sêniors em codebase legado têm ganho zero ou negativo. Explicação: a IA trata o código existente como verdade e não conhece o contexto histórico não documentado ("o pai do sistema" sabe, mas está na cabeça dele). Resultado: PR tecnicamente válido, arquiteturalmente errado — passa nos testes e quebra a lógica de negócio.
**Confidence:** média

**Claim:** As métricas usadas para medir produtividade com IA são métricas de output, não de outcome.
**Evidence:** Times medem quantidade/velocidade/volume — exatamente o que a IA infla independente de qualidade. As métricas que importam: bug rate pós-deploy, tempo de code review, frequência de incidentes. Caso clássico de [[wiki/concepts/goodharts-law]] e [[wiki/concepts/dora-metrics]] (output vs. outcome do SPACE).
**Confidence:** alta

**Claim:** A adoção atual não é sustentável.
**Evidence:** 30% dos devs já bateram nos limites de uso das ferramentas de IA (dado Faros AI) — sinal de receita para burnout, não de adoção saudável.
**Confidence:** média

**Claim:** Os papéis de engenheiro e manager vão convergir nos próximos ~2 anos.
**Evidence:** Com a IA gerando código, o trabalho do engenheiro vira decisão, revisão e direcionamento — gerenciamento do sistema. O dev que prospera não é o que escreve mais rápido, é o que julga o que foi gerado com critério.
**Confidence:** média (previsão)

## Entities & Concepts Touched

- [[wiki/concepts/paradoxo-da-aceleracao]]
- [[wiki/concepts/ia-como-amplificador]]
- [[wiki/concepts/output-vs-outcome]]
- [[wiki/entities/faros-ai]]
- [[wiki/entities/gergely-orosz]]
- [[wiki/concepts/goodharts-law]]
- [[wiki/concepts/dora-metrics]]
- [[wiki/concepts/code-review]]
- [[wiki/concepts/roi-de-ia]]
- [[wiki/concepts/ia-como-chicote-de-produtividade]]
- [[wiki/concepts/novo-perfil-dev-ia]]
- [[wiki/concepts/burnout-dev]]
- [[wiki/concepts/gaming-de-testes-por-ia]]
- [[wiki/concepts/divida-cognitiva]]
- [[wiki/concepts/codigo-legado-ia]]

## Open Questions

- Os números da Faros AI (93% / 10% / 21% / 91% / 30%) e da survey do Pragmatic Engineer (26–56% júnior; zero/negativo sênior) vêm da transcrição do vídeo e **não foram cross-checados contra os relatórios primários**. Registrar como não confirmados até localizar o report da Faros AI e a survey do Pragmatic Engineer citada.
- Autor/canal do vídeo original não identificado na transcrição.

## Raw Quotes

> "Sêniors bons ficam melhores; sêniors medíocres ficam mais difíceis de gerenciar."

> "Você tem um PR que passa nos testes e quebra a lógica de negócio."

> "O dev que vai prosperar não é o que escreve mais rápido — é o que consegue julgar o que foi gerado com critério."
