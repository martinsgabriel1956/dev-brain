---
type: source
title: "O Google está perdendo a corrida da IA? Memory Caching, Gemini 3.8 Live e o negócio por trás"
aliases: ["google corrida ia", "memory caching rnn vídeo"]
date_created: 2026-10-09
date_updated: 2026-10-09
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/google-nao-esta-perdendo-corrida-ia-memory-caching-gemini-live.md
source_url: ""
author: "não identificado"
date_published: ""
date_ingested: 2026-10-09
source_count: 1
tags: [ai, google, gemini, rnn, memory-caching, speech-to-speech, gcp, tpu, eficiencia]
skill: tech-mentor-ai
status: stable
---

## TL;DR

Vídeo em PT-BR que rebate a ideia de que o [[wiki/entities/google]] está perdendo a corrida da IA. Tese: o Google perde na percepção dos devs (modelos de código, Antigravity ruim, timing de divulgação ruim), mas ganha em **negócio** (Google Cloud +82% a/a, ~US$ 24,8 bi; [[wiki/concepts/tensor-processing-unit|TPUs]]; IA embutida em produtos) e em **pesquisa de eficiência** — o paper [[wiki/concepts/memory-caching-rnn|Memory Caching]] dá [[wiki/concepts/recurrent-neural-network|RNNs]] uma memória crescente que reduz o gap para o [[wiki/concepts/transformer-architecture|Transformer]] sem o custo quadrático. Em produto, o [[wiki/entities/gemini-live|Gemini 3.8 Live]] ([[wiki/concepts/speech-to-speech]]) seria >3× mais barato que o GPT Live 1 com benchmark melhor.

## Key Claims

**Claim:** O Google ganha dinheiro com IA via infraestrutura e soluções corporativas: Cloud com US$ 24,8 bi de receita (+82% a/a) e backlog de ~US$ 514 bi, puxado pelo [[wiki/entities/google-cloud-platform|GCP]].
**Evidence:** relatórios citados na tela (Alphabet 1T26; resumo de Cloud Q2 2026); números ditos pelo autor, sem exibir a fonte primária.
**Confidence:** média (números plausíveis, não verificados contra o relatório; autor hesita no backlog "se eu não me engano").

**Claim:** O Google compete por estar em três camadas — cloud, chip ([[wiki/concepts/tensor-processing-unit|TPU]]) e soluções —, complementando mais do que combatendo a [[wiki/entities/nvidia]].
**Evidence:** argumento do autor.
**Confidence:** média (opinião; TPU como alternativa à GPU é consenso [external]).

**Claim:** Modelos baratos do Google (Gemini 3.7/3.8 Flash, ~US$ 0,75/M tokens) servem de motor de eficiência para produtos próprios; "eficiência em IA exige resultado para o usuário final", não só custo por token.
**Evidence:** argumento do autor; ver [[wiki/concepts/modelo-por-leverage-tarefa]].
**Confidence:** média. Unidade do preço ambígua no áudio ("0.75 centavos" por milhão).

**Claim:** O paper de **Memory Caching** (Google Research + Cornell + USC) cacheia checkpoints do estado de memória de RNNs, dando memória crescente entre o custo O(L) da RNN e O(L²) do Transformer; em 1,3B de parâmetros, Titans+MC pontuou 58,33 vs 53,19 do Transformer na média de language modeling + common sense reasoning.
**Evidence:** números lidos pelo autor no paper; paper confirmado em [external] https://arxiv.org/abs/2602.24281 (Behrouz et al., fev/2026; ICML 2026) — ele afirma que Transformers ainda são os melhores em recall *in-context*, variantes MC "fecham o gap".
**Confidence:** alta para a existência/ideia; média para os números exatos (não conferidos tabela a tabela). Autor: isso **não** significa que RNN matará o Transformer.

**Claim:** Memory Caching ataca o gargalo de memória fixa da RNN e poderia melhorar tarefas tipo [[wiki/concepts/needle-in-a-haystack|agulha no palheiro]].
**Evidence:** raciocínio do autor; o paper (via [external]) diz competitivo, mas ainda atrás do Transformer em recall.
**Confidence:** baixa-média (especulativo).

**Claim:** O Gemini 3.8 Live (e Extended Thinking) supera GPT Live 1 (effort medium) e Grok Voice no Speech-to-Speech Index, e custa ~US$ 0,84/h contra ~US$ 3/h do GPT Live 1 (US$ 0,05/min) — >3× mais barato.
**Evidence:** gráficos exibidos no vídeo; ver [[wiki/entities/gemini-live]].
**Confidence:** média (benchmark e preços citados de tela; não verificados).

**Claim:** Voz com IA barateando levará a ondas de ligações automatizadas (telemarketing e golpes) no Brasil; Grok Voice ainda é caro.
**Evidence:** previsão do autor.
**Confidence:** baixa (especulação).

**Claim:** A percepção negativa vem do **Antigravity** (produto de dev ruim) e do timing de lançamentos.
**Evidence:** opinião/feedback do autor.
**Confidence:** baixa (subjetivo).

## Entities

[[wiki/entities/google]], [[wiki/entities/google-cloud-platform]], [[wiki/entities/google-research]], [[wiki/entities/gemini-live]], [[wiki/entities/openai]], [[wiki/entities/xai]], [[wiki/entities/nvidia]], [[wiki/entities/jev]] (citado só como "o assunto do momento").

## Concepts

[[wiki/concepts/recurrent-neural-network]], [[wiki/concepts/memory-caching-rnn]], [[wiki/concepts/transformer-architecture]], [[wiki/concepts/self-attention]], [[wiki/concepts/needle-in-a-haystack]], [[wiki/concepts/context-window]], [[wiki/concepts/speech-to-speech]], [[wiki/concepts/time-to-first-token]], [[wiki/concepts/tensor-processing-unit]], [[wiki/concepts/modelo-por-leverage-tarefa]].

## Open Questions

- Autor/canal não identificado; nomes do ASR incertos ("Gemini 3.8 Flash cyber", "GRM", "DLA", "GPT Live 1 Astra").
- Quão bem Memory Caching escala para >1,3B e contextos de milhões de tokens? O vídeo só cita um experimento.
- O paper compara custo de inferência real (tokens/s, memória) vs Transformer? O vídeo foca em acurácia.
- Segmento patrocinado (Higlobe) não tem valor técnico; ignorado.

## Quotes

> "O Google sabe fazer negócios."

> "Para ter eficiência na IA tu precisa ter, de fato, resultado pro teu usuário final."

> "Imagina o superpoder da formiga se ela conseguisse lembrar do início da conversa."
