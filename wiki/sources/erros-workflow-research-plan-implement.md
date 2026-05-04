---
type: source
title: "Os Três Erros do Workflow RPI com 10.000 Devs"
aliases: ["erros rpi", "erros research plan implement", "workflow rpi erros"]
date_created: 2026-05-04
date_updated: 2026-05-04
source_file: /home/nemomartins/Documentos/new/dev-study/raw/erros-workflow-research-plan-implement.md
source_url: null
author: null
date_published: null
date_ingested: 2026-05-04
source_count: 0
tags: [rpi, context-engineering, coding-agents, workflow, ai-engineering]
skill: tech-mentor-ai
status: stable
---

# Os Três Erros do Workflow RPI com 10.000 Devs

## TL;DR

Uma empresa publicou o workflow **Research → Plan → Implement (RPI)** que acumulou mais de 10.000 devs. Meses depois, subiram num palco e admitiram dois erros críticos. O autor identifica um terceiro, mencionado de passagem mas com peso técnico alto. Os três erros revelam exatamente o que mais devs fazem errado hoje com agentes de código.

---

## Key Claims

### Claim 1 — Não ler o código durante o research leva a erros difíceis de detectar
**Evidence:** A empresa passou seis meses sem revisar o código que o agente explorava, confiando apenas no plano gerado. Resultado: jogaram fora uma parte grande do sistema.
**Source:** análise do vídeo EAI Engineering
**Confidence:** alto — padrão reportado por múltiplos times em produção

### Claim 2 — Planos muito detalhados dobram o trabalho sem ganho proporcional
**Evidence:** Planos de 500–800 linhas exigem o mesmo esforço de revisão que o código gerado a partir deles. O dev revisa duas vezes em vez de uma.
**Source:** análise do vídeo EAI Engineering
**Confidence:** alto — lógica direta, sem contra-evidência

### Claim 3 — Instruction budget total do agente é ignorado pela maioria dos devs
**Evidence:** System prompt de 85 instruções + CLAUDE.md com 30 + MCPs = facilmente no limite de ~150–200 instruções seguíveis com consistência. Cada instrução além do budget é um dado — o modelo pode ou não seguir.
**Source:** análise do autor (terceiro erro identificado)
**Confidence:** médio — estimativa empírica da empresa, não benchmark oficial

---

## Conceitos Centrais

- [[concepts/rpi-workflow]] — Research → Plan → Implement e sua filosofia
- [[concepts/instruction-budget]] — limite implícito de instruções seguíveis por LLMs
- [[concepts/plano-vertical]] — fatias testáveis vs plano horizontal monolítico
- [[concepts/design-discussion]] — alinhamento de direção antes de qualquer linha de código
- [[concepts/separacao-de-contextos]] — research e plan em sessões distintas para evitar contaminação

---

## Entidades Tocadas

- EAI Engineering (empresa que publicou o workflow original)

---

## O Método Evoluído (CRISPY)

A empresa chamou o método evoluído de **CRISPY**. Três mudanças principais:

1. **Design Discussion** no lugar de plano detalhado — foca o modelo no entendimento, não no código. 200 linhas revisáveis em 10 minutos vs 1.000 linhas de plano.

2. **Plano vertical** — cada entrega é testável imediatamente. Evita o problema do "banco existe mas a API não" — quando o erro aparece, já estão em 1.500 linhas de contexto.

3. **Janelas de contexto separadas** — a sessão de research não sabe sobre o que vai ser construído. Impede decisões de arquitetura escondidas numa fase de coleta.

---

## Conexões com o Wiki

- [[sources/addy-osmani-80-problem-agentic-coding]] — abstraction bloat gerado por agentes sem método
- [[sources/divida-cognitiva-ai-brainfry]] — o custo cognitivo de supervisar sem entender
- [[sources/context-engineering]] — fundamentos de gerenciamento de context window
- [[concepts/vertical-slice-architecture]] — plano vertical é a versão de workflow do VSA
- [[concepts/comprehension-debt]] — o que acontece quando você para de ler o código gerado

---

## Open Questions

- Existe um threshold objetivo de linhas de plano onde o ROI de revisão inverte?
- Como aplicar separação de contextos em ferramentas que não suportam múltiplas sessões (ex: Cursor inline)?
- Instruction budget de 150–200 é por conversa ou por turn?
