---
type: source
title: "Context Engineering Avançado para Coding Agents"
aliases: ["dex talk", "12 factor agents context", "rpi dex", "smart zone dumb zone"]
date_created: 2026-05-04
date_updated: 2026-05-04
source_file: /home/nemomartins/Documentos/new/dev-study/raw/context-engineering-avancado-para-coding-agents.md
source_url: null
author: Dex
date_published: null
date_ingested: 2026-05-04
source_count: 0
tags: [context-engineering, coding-agents, rpi, smart-zone, compaction, ai-engineering]
skill: tech-mentor-ai
status: stable
---

# Context Engineering Avançado para Coding Agents

## TL;DR

Talk de Dex (autor de "12 Factor Agents") sobre como sua equipe de 3 pessoas conseguiu 2–3x mais throughput com Claude Code ao construir um sistema de **context engineering** para coding agents. O princípio central: LLMs são stateless, então a única alavanca de performance é a qualidade dos tokens na context window. O método — Research → Plan → Implement — existe para manter o agente na "smart zone" (abaixo de ~40% da context window) durante todo o trabalho.

---

## Key Claims

### Claim 1 — A context window tem uma zona de degradação a partir de ~40%
**Evidence:** A partir de ~40% de uso, retornos decrescentes são observados empiricamente. Times com MCPs pesados fazem todo o trabalho na "dumb zone" e nunca conseguem bons resultados.
**Source:** Dex, talk AI Engineer
**Confidence:** médio — empírico, não benchmarkado formalmente; varia por complexidade da tarefa

### Claim 2 — Sub-agentes servem para controlar contexto, não para antropomorfizar papéis
**Evidence:** Um sub-agente faz toda a exploração e retorna uma mensagem sucinta para o agente pai. O pai lê só o arquivo relevante e vai direto ao trabalho — sem contaminar sua context window com buscas.
**Source:** Dex, talk AI Engineer
**Confidence:** alto — padrão arquitetural direto e verificável

### Claim 3 — A trajetória da conversa influencia o comportamento do modelo
**Evidence:** Se o histórico da conversa contém um padrão de "erro → correção → erro → correção", o próximo token mais provável é o modelo errar novamente — porque é o padrão estabelecido.
**Source:** Dex, talk AI Engineer
**Confidence:** alto — consequência direta de como LLMs predizem o próximo token

### Claim 4 — Equipe de 3 pessoas entregou 35.000 linhas em 7 horas com o método
**Evidence:** Sessão de sábado com Vibhav (CEO Boundary ML). Estimativa de 1–2 semanas de trabalho equivalente. Um dos PRs foi mergeado pelo CTO uma semana depois.
**Source:** Dex, talk AI Engineer
**Confidence:** médio — auto-reportado, sem auditoria externa

---

## Conceitos Centrais

- [[concepts/dumb-zone]] — zona de degradação da context window (~40%+)
- [[concepts/compaction-intencional]] — compressão periódica do contexto em markdown
- [[concepts/rpi-workflow]] — Research → Plan → Implement como framework de context management
- [[concepts/mental-alignment]] — code review como sincronização do modelo mental do time
- [[concepts/instruction-budget]] — limite implícito de instruções seguíveis com consistência
- [[concepts/separacao-de-contextos]] — sub-agentes e sessões separadas para controle de contexto

---

## O Workflow RPI em Detalhe

### Research
- Objetivo: entender como o sistema funciona, encontrar os arquivos certos
- Regra: só observar, não planejar
- Output: documento com arquivos exatos e números de linha relevantes

### Plan
- Objetivo: delinear os passos exatos com snippets de código reais
- Regra: ser explícito sobre como testar após cada mudança
- Output: plano com código snippets — "até o modelo mais simples não vai errar"

### Implement
- Objetivo: executar o plano mantendo o contexto baixo
- Regra: não deixar o contexto crescer além do necessário

---

## Sobre Spec-Driven Development

O autor argumenta que "spec-driven dev" sofreu **semantic diffusion** (conceito de Martin Fowler, 2006). O termo foi diluído para significar coisas diferentes por pessoas diferentes — de "prompt mais detalhado" a "documentação de biblioteca open source".

O que importa não é o nome: é **compaction, context engineering e ficar na smart zone**.

---

## Resultados Práticos

| Experimento | Resultado |
|---|---|
| Fix em codebase Rust 300k linhas | PR aceito pelo CTO |
| 35k linhas em 7h (Boundary ML BAML) | ~1-2 semanas equivalente |
| Remoção Hadoop do Parquet Java | Não funcionou — voltaram ao whiteboard |

O terceiro caso é tão importante quanto os sucessos: quando o domínio exige pensar de verdade, o método não substitui o pensamento — apenas amplifica.

---

## Conexões com o Wiki

- [[sources/erros-workflow-research-plan-implement]] — perspectiva complementar sobre os erros do mesmo método
- [[sources/context-engineering]] — fundamentos de sliding window, summarization, prompt cache
- [[sources/divida-cognitiva-ai-brainfry]] — o custo cognitivo de não manter mental alignment
- [[sources/addy-osmani-80-problem-agentic-coding]] — abstraction bloat como consequência de contexto não gerenciado
- [[concepts/vertical-slice-architecture]] — plano vertical é VSA aplicado a workflow de agente
- [[concepts/comprehension-debt]] — o que acontece quando você não lê o que o agente gerou

---

## Open Questions

- O threshold de 40% é válido para modelos com 1M+ de context window (Gemini)?
- Como medir "mental alignment" de um time objetivamente?
- Compaction intencional tem custo de tokens de escrita — qual o break-even?
