---
type: source
title: "Formação IA para Devs — Aula 03: LLM"
aliases: ["IA para Devs Aula 3", "LLM Fundamentos Branas"]
date_created: 2026-06-02
date_updated: 2026-06-02
source_count: 0
tags: [ia-para-devs, llm, modelos, contexto, reasoning, open-source, degradacao]
skill: tech-mentor-ai
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/Aula 03 - LLM.md"
source_url: ""
author: "Rodrigo Branas, Pedro Nauke"
date_published: "2026"
date_ingested: 2026-06-02
---

# Formação IA para Devs — Aula 03: LLM

## TL;DR

Fundamentos práticos de LLMs para devs: o que é um modelo, como o harness o empodera, degradação de contexto acima de 400k tokens, níveis de reasoning e quando usá-los, comparativo de modelos frontier vs open source, e por que rodar modelos locais raramente faz sentido econômico.

## Key Claims

- **LLM é um gerador de tokens probabilístico** — não sabe "que horas são", não tem memória entre sessões, não lê código sem ser solicitado. O harness fornece tudo isso. Evidência: explicação técnica de Branas com demo de chamada direta à API.
- **"Attention is all you need" (2017)** = paper fundador do Transformer; OpenAI pegou essa arquitetura e a colocou numa API simples em 2023, democratizando o acesso. Evidência: contexto histórico dado por Nauke.
- **Degradação começa ~400k tokens**: após esse limite, todos os modelos de 1M de contexto degradam consideravelmente. Anthropic publicou paper dizendo Opus não degrada — Nauke discorda por experiência prática. Evidência: experience report + referência à pesquisa da Anthropic.
- **Solução recomendada**: setar auto-compact em 400k. Um modelo que bate 92% de qualidade pode cair para 65% após degradação — pior que open source. Evidência: cálculo ilustrativo de Branas.
- **Reasoning levels** (low/medium/high/extra-high) controlam quantos tokens internos o modelo gera antes de responder. Tarefa bem definida + extra-high = desperdício. Tarefa ambígua/complexa + medium = bom custo-benefício. Evidência: explicação mecânica + recomendação dos instrutores.
- **Modelos frontier recomendados** (2026): Opus 4.7, GPT-5.5, GPT-5.4, Gemini 3.1, Kimi K2.6, GLM 5.1, Qwen 3.6. Open source como Kimi K2.6 já entrega resultado muito bom para muitas tarefas. Evidência: opinião dos instrutores com base em uso extensivo.
- **Preferência de Nauke**: modelos OpenAI (GPT-5.x) para backend complexo / tarefas novas; Opus para frontend/design/review. Evidência: processo real de trabalho de Pedro.
- **Preços (2026)**: GPT-5.4 = $1.75/M input → subiu para $5/M; Opus (antes $15.75) baixou. GPT-5.5 output = $30/M. Ver tabela comparativa abaixo.
- **MoE (Mixture of Experts)** = razão pela qual modelos open source chineses são mais baratos. Evidência: Nauke explica a arquitetura de forma simplificada.
- **Modelos locais NÃO fazem sentido** para trabalho profissional a não ser para: (1) compliance/dado sensível, (2) empresas que proveem IA em escala, (3) aprendizado/experimento. AWS: máquina com 24GB VRAM = $2.500/mês; 192GB = $16.000/mês. Evidência: cotação de preços AWS no momento da aula.
- **Slides da aula custaram ~$250** para fazer no Codex (8h de trabalho, 42M tokens, 4 compactações), demonstrando que até tarefas "simples" podem consumir contexto enorme em modo agêntico. Evidência: relato direto de Branas.

## Tabela de Preços (snapshot 2026)

| Modelo | Input ($/1M) | Output ($/1M) | Obs |
|---|---|---|---|
| GPT-5.5 | $5 | $30 | frontier OpenAI |
| GPT-5.4 | $1.75→$5 | — | subiu de preço |
| Opus 4.7 | ~$5 | — | baixou de $15.75 |
| Sonnet 4.6 | $3 | — | — |
| Gemini 3.1 | $2 / $4 | — | escalonado por volume |
| Qwen (Alibaba) | $0.50 / $2 | — | até/acima de limiar |
| Kimi K2.6 | ~baixo | — | open source frontier |

## Entities

- [[wiki/entities/rodrigo-branas]]
- [[wiki/entities/pedro-nauke]]
- [[wiki/entities/openai]] — democratizou LLMs via API em 2023
- [[wiki/entities/anthropic]] — Opus, Sonnet; fez research sobre degradação de contexto
- [[wiki/entities/google-deepmind]] — Gemini; puxou o contexto de 1M tokens
- [[wiki/entities/alibaba-qwen]] — modelos open source MoE baratos

## Concepts

- [[wiki/concepts/degradacao-de-contexto]]
- [[wiki/concepts/reasoning-level]]
- [[wiki/concepts/modelo-frontier]]
- [[wiki/concepts/mixture-of-experts]]
- [[wiki/concepts/modelos-locais-trade-offs]]
- [[wiki/concepts/harness]]
- [[wiki/concepts/janela-de-contexto]] — atualizar com dado de degradação

## Open Questions

- O claim da Anthropic de que "Opus não degrada" ainda se sustenta em 2026 com os modelos 4.x?
- Qual o impacto real de custo ao usar 400k vs 1M de contexto no mesmo modelo?

## Raw Quotes

> "Não é porque tem um milhão de tokens no contexto, você tem que usar um milhão de tokens. Não é porque tem espaço que você vai seguir usando esse espaço." — Rodrigo Branas

> "Se eu tenho muita coisa, mais coisa para eu dar atenção... isso é alucinação. O Transformer é baseado no mecanismo de atenção." — Rodrigo Branas

> "Você vai gastar 20 mil dólares para rodar um modelo Open Source que vai te cobrar 30 centavos no provider." — Rodrigo Branas

> "Uma tarefa que demoraria meia hora, demora uma hora, uma hora e meia... Se você pegar uma switch de teste em Rush, nossa, é 30 minutos." — Pedro Nauke (sobre Rust)
