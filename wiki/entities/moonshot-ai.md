---
type: entity
title: "Moonshot AI"
aliases: ["Moonshot", "Kimi"]
date_created: 2026-07-21
date_updated: 2026-09-04
source_count: 5
tags: [moonshot, kimi, china, llm, open-source, organização]
skill: tech-mentor-ai
status: stub
---

# Moonshot AI

Lab de IA chinês, criador da família de modelos **Kimi**. Autor do modelo já citado nesta wiki [[wiki/concepts/modelo-frontier|Kimi K2.6]] (referenciado como open-weight competitivo com frontier fechados por fração do preço) e, mais recentemente, do **Kimi K3**.

## Kimi K3 (lançamento parcial)

Divulgado em [[wiki/sources/kimi-k3-china-mercado-ia-open-source]]: modelo de **2,8 trilhões de parâmetros**, arquitetura [[wiki/concepts/mixture-of-experts|MoE]] com **896 experts, dos quais só 16 ativados por inferência**. Lançamento parcial — API oficial e benchmarks já disponíveis, pesos ainda não públicos no momento da fonte. Divulgou um novo método de inferência com até 75% de economia de [[wiki/concepts/kv-cache|KV Cache]], com perda de precisão considerada irrelevante nos benchmarks.

## Estratégia de abertura como diferencial de mercado

Diferente de labs fechados (OpenAI, Anthropic), a Moonshot publica não só o modelo mas o método de servi-lo em inferência — qualquer provedor com hardware suficiente pode replicar a "receita" e servir o modelo, descentralizando o conhecimento de inferência que hoje é concentrado em poucas big techs (Microsoft, AWS). Isso é discutido como parte do contexto mais amplo de [[wiki/concepts/export-controls-chips-ia|sanções de exportação de chips]] pressionando inovação arquitetural em labs sem acesso irrestrito a hardware de ponta.

## Kimi como Modelo de Fallback por Custo-Benefício

[[wiki/sources/gestao-de-custo-velocidade-modelos-de-ia-fable-sol]] recomenda o Kimi como opção de "fallback" para tarefas simples/em background, citado ao lado do Sonnet e do DeepSeek como boa relação custo-benefício, e usado como exemplo na categoria "balanceado" de um roteador customizado — ver [[wiki/concepts/roteamento-automatico-de-modelo]].

## Kimi K3 como Pressão de Preço no Mid-Tier

[[wiki/sources/precificacao-ancoragem-anthropic-opus-5-lancamento]] cita um benchmark de custo do Cline (antes do lançamento do Opus 5): na mesma task, o **Kimi K3 custou US$ 0,92** contra **US$ 2,13 do Fable** ([[wiki/entities/anthropic]]) — com a ressalva de que o Fable foi mais rápido e gastou menos token. Essa pressão por baixo no *mid-tier* (junto ao [[wiki/entities/xai|Grok 4.5]]) é apresentada como o motivo pelo qual a Anthropic recorreu à [[wiki/concepts/ancoragem-de-preco|ancoragem de preço]].

## Kimi K3 Como Escape de Guardrails Agressivos

[[wiki/sources/levelsio-china-guardrails-multi-modelo-opus-5]] relata o caso de [[wiki/entities/pieter-levels|Pieter Levels]]: o Kimi K3, acessado via [[wiki/entities/opencode|Opencode]] com uma chave de API própria do Kimi Server (~19 USD, upstream — alternativa ao acesso via [[wiki/entities/openrouter|OpenRouter]]), completou uma lista de tarefas de um projeto hobby (simulador de Windows XP) sem o throttling a cada 5 minutos percebido no Claude Code, e sem os bloqueios "por segurança" que levaram o Claude a rebaixar o modelo usado (Opus → Sonnet) na mesma sessão. Ilustra concretamente por que modelos chineses mais permissivos atraem usuários frustrados com [[wiki/concepts/ai-safety-guardrails|guardrails]] agressivos — mesmo quando a tarefa em si é de baixo risco real (hobby pessoal, não produção crítica).

## Kimi K3 (Coordenador) vs. Kimi K2.7 Code (Worker): Preços Internos à Família

[[wiki/sources/agent-waves-custo-modelos-fortes-fracos-kimi]] cita preços granulares dos dois modelos da própria Moonshot, usados para justificar uma estratégia de [[wiki/concepts/roteamento-automatico-de-modelo|roteamento por papel]] dentro de um pipeline de [[wiki/concepts/subagentes|Agent Waves]]: **Kimi K3** — US$15/M tokens de output, US$3/M de input em cache miss, US$0,30/M em cache hit; **Kimi K2.7 Code** (modelo específico da Moonshot para código) — US$1,4/M output, US$0,95/M input em cache miss, US$0,19/M em cache hit. Ou seja, dentro da própria família Kimi, o K3 é "o caro" e o K2.7 é "o barato" (diferença de ~3× a ~10× conforme o regime de cache) — contraste interno que complementa a comparação já registrada acima contra o Fable (fonte externa à família). A fonte usa esse contraste para propor: modelo caro (K3) só no coordenador que planeja/decide, modelo barato (K2.7) nos workers de implementação — uma simulação projetou ~34% de economia com essa segregação, mas um teste real na mesma tarefa (pequena) confirmou só ~5%.

A Moonshot também oferece assinatura mensal com créditos inclusos (citada com faixa de alguns dólares a ~US$199/mês), como alternativa ao pagamento por token via API — sem comparação de custo-benefício entre os dois modelos de cobrança na fonte.

## Key Sources

- [[wiki/sources/levelsio-china-guardrails-multi-modelo-opus-5]] — Kimi K3 via Opencode/Kimi Server como escape de guardrails agressivos do Claude Code num projeto hobby
- [[wiki/sources/kimi-k3-china-mercado-ia-open-source]]
- [[wiki/sources/gestao-de-custo-velocidade-modelos-de-ia-fable-sol]] — Kimi como modelo de fallback recomendado por custo-benefício
- [[wiki/sources/precificacao-ancoragem-anthropic-opus-5-lancamento]] — Kimi K3 mais barato que o Fable em benchmark de custo (Cline)
- [[wiki/sources/agent-waves-custo-modelos-fortes-fracos-kimi]] — preços de cache hit/miss de K3 vs. K2.7 Code; K3 como coordenador caro, K2.7 como worker barato num pipeline de Agent Waves
