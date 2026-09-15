---
type: source
title: "Prompt Caching e KV Cache: Como Fazer Prompting Como um Profissional"
aliases: ["prompt caching ronald hulk", "kv cache por provedor", "time to first token cache"]
date_created: 2026-09-15
date_updated: 2026-09-15
source_count: 0
tags: [prompt-caching, kv-cache, inferencia, custo-de-ia, ttft, anthropic, openai, openrouter, deepseek, tech-mentor-ai]
skill: tech-mentor-ai
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/prompt-caching-kv-cache-engenharia-de-contexto-ronald-hulk.md
source_url: ""
author: "Ronald Hulk"
date_published: ""
date_ingested: 2026-09-15
---

# Prompt Caching e KV Cache: Como Fazer Prompting Como um Profissional

## TL;DR

Vídeo (Ronald Hulk) que explica prompt caching como técnica prática de engenharia de prompt: como o [[wiki/concepts/kv-cache|KV Cache]] de inferência pode ser reaproveitado entre chamadas quando o prefixo do prompt é idêntico, evitando reprocessamento e reduzindo custo e latência (menor [[wiki/concepts/time-to-first-token|time to first token]]). Cobre diferenças de implementação entre Anthropic (cache mais "forçado", TTL configurável), OpenAI (cache implícito/automático) e OpenRouter (depende de modelo+provedor, com DeepSeek citado como caso fácil de acionar com prompts pequenos). Descreve dois antipadrões comuns em consultoria — colocar timestamp/dado dinâmico no início do prompt (invalida o prefixo cacheável) e não estruturar o prompt em blocos fixo→variável — e lista cinco requisitos mínimos para alcançar cache hit: suporte do modelo/provedor, cuidado com o prefixo, tamanho mínimo de tokens, continuidade/TTL, e medição (idealmente via telemetria independente do provider, ex. LangSmith/Langfuse).

## Key Claims

**Claim:** O KV Cache armazena, durante a inferência, a informação já processada de um prompt para evitar reprocessamento em chamadas subsequentes com o mesmo prefixo.
**Evidence:** Analogia com cache tradicional de aplicação; descrição do fluxo de duas chamadas — a primeira "escreve" no cache, a segunda com o mesmo prefixo (ferramentas, system prompt, documentos fixos) reaproveita o que já foi computado e processa apenas a parte nova (ex.: a pergunta do usuário).
**Confidence:** Alta — consistente com o mecanismo já documentado em [[wiki/concepts/kv-cache]] e com `references/ai/context-engineering.md` (skill tech-mentor-ai).

**Claim:** Soluções que não usam prompt caching reprocessam o input inteiro a cada chamada, pagando o custo completo de algo já processado anteriormente.
**Evidence:** Contraste direto com o fluxo de cache: sem cache, o contexto é sempre repetido e cobrado do zero.
**Confidence:** Alta — mecanismo coerente com a natureza autorregressiva descrita em [[wiki/sources/tokens-o-que-sao-e-por-que-custam-caro]] e [[wiki/concepts/autoregressive-language-model]], embora aquela fonte trate do custo de *output* (geração token a token) e esta trate do custo de *input* reprocessado — dois mecanismos relacionados mas distintos, ambos mitigados por caching de diferentes formas.

**Claim:** Anthropic historicamente exigia mais esforço para acionar o cache (prefixo mínimo maior) que OpenAI, que hoje tem caching implícito sem configuração.
**Evidence:** Descrição qualitativa: "antigamente [na Anthropic] você tinha que forçar muito mais pro cash ocorrer"; já a OpenAI "hoje é implícito, você não precisa fazer nada, só entrar dentro da condição".
**Confidence:** Alta para a direção geral do claim — confirmado por `references/ai/context-engineering.md` (skill tech-mentor-ai): Anthropic requer marcação explícita de `cache_control` (cache breakpoints), enquanto a OpenAI faz cache automático sem configuração a partir de 1024 tokens. O vídeo simplifica o mecanismo da Anthropic (não menciona `cache_control` explicitamente), mas a direção da comparação está correta.

**Claim:** O mínimo de tokens para acionar o cache varia por modelo — modelos antigos da Anthropic (ex.: Sonnet 4.5) exigiam 4096 tokens de entrada, enquanto o Opus 5 já aceita a partir de 512.
**Evidence:** Números específicos citados no vídeo como "paradigma antigo" (4096 tokens) vs. o comportamento atual do Opus 5 (512 tokens), atribuindo a mudança a uma preocupação crescente da indústria com esse limite.
**Confidence:** Baixa-média — `references/ai/context-engineering.md` (skill tech-mentor-ai) documenta um mínimo geral de **1024 tokens** para cache na Anthropic, sem diferenciar por modelo/geração. Os números específicos do vídeo (4096 e 512) não puderam ser cross-checados contra documentação oficial da Anthropic nesta ingestão — ficam registrados como afirmação da fonte, não como fato verificado. Ver Open Questions.

**Claim:** Na OpenRouter, o suporte a prompt caching depende da combinação modelo + provedor, e modelos como DeepSeek aceitam caching com prompts pequenos, sendo fáceis de usar.
**Evidence:** Descrição do funcionamento da OpenRouter como agregador de modelo+provedor, com DeepSeek citado como exemplo de baixo mínimo de tokens para cache.
**Confidence:** Média — consistente com o padrão geral já documentado em [[wiki/entities/openrouter]] (roteamento modelo+provedor) e com [[wiki/entities/deepseek]] como provider de custo-benefício agressivo, mas o mínimo específico de tokens do DeepSeek para cache não foi verificado nesta ingestão contra documentação oficial.

**Claim:** Colocar timestamp ou dado dinâmico do cliente logo no início do prompt invalida o cache, porque o prefixo muda a cada chamada; a correção é colocar informação dinâmica no final do prompt.
**Evidence:** Exemplo didático de system prompt com data/hora logo após a instrução inicial, fazendo o prefixo nunca bater entre chamadas.
**Confidence:** Alta — este é o antipadrão canônico documentado quase palavra por palavra em `references/ai/context-engineering.md` (skill tech-mentor-ai), incluindo a mesma correção (conteúdo estático no topo, dinâmico no fim).

**Claim:** A estrutura ideal de prompt cacheável é: system prompt → descrição de ferramentas → documentos fixos → dados variáveis por último.
**Evidence:** "Shape" de prompt recomendado no vídeo, com exemplo prático de uma ferramenta (Rock Pro) onde o primeiro turno de uma conversa vira prefixo fixo reaproveitado em perguntas subsequentes.
**Confidence:** Alta — corresponde exatamente à "arquitetura de prompt cache-friendly" descrita em `references/ai/context-engineering.md` (skill tech-mentor-ai): estático (system + docs) no topo, histórico e query variável no fim.

**Claim:** Existem cinco requisitos mínimos para alcançar cache hit: (1) suporte do modelo/provedor, (2) prefixo bem estruturado, (3) tamanho mínimo de tokens conhecido, (4) continuidade/TTL do cache conhecida, (5) medição confiável — idealmente via ferramenta de telemetria independente do provider (ex.: LangSmith, Langfuse).
**Evidence:** Lista enumerada no vídeo, incluindo o alerta de que a informação de cache hit/miss aparece em locais diferentes do payload de resposta dependendo do provider.
**Confidence:** Alta como checklist prático — os cinco pontos são consistentes com o que a skill documenta: TTL configurável por provider (Anthropic: 5 min padrão, extended 1h; Gemini: configurável até dias), formato de `usage` diferente por provider (`CacheUsage` na Anthropic vs. `cached_tokens` na OpenAI), e o uso de Langfuse como padrão de observabilidade já registrado em [[wiki/sources/llmops-observabilidade]].

## Entidades e Conceitos Tocados

- [[wiki/concepts/kv-cache]]
- [[wiki/concepts/prompt-caching]]
- [[wiki/concepts/time-to-first-token]]
- [[wiki/entities/anthropic]]
- [[wiki/entities/openai]]
- [[wiki/entities/openrouter]]
- [[wiki/entities/deepseek]]
- [[wiki/concepts/ai-gateway-llm-router]]
- [[wiki/concepts/autoregressive-language-model]]
- [[wiki/concepts/prompt-engineering]]
- [[wiki/sources/llmops-observabilidade]]
- [[wiki/sources/tokens-o-que-sao-e-por-que-custam-caro]]

## Open Questions

1. **Números específicos de mínimo de tokens por geração de modelo na Anthropic (4096 para modelos antigos, 512 para Opus 5)** não batem com o valor único documentado na skill (1024 tokens geral) e não foram cross-checados contra a tabela oficial de preços/limites da Anthropic nesta ingestão. Vale verificar em uma ingestão futura com fonte primária (docs.anthropic.com) se o mínimo de fato varia por modelo/geração ou se o vídeo está descrevendo um comportamento específico de uma API/feature diferente (ex.: extended thinking, batch API).
2. **Mínimo de tokens do DeepSeek via OpenRouter para acionar cache** citado como "bem pequenininho" sem número específico — não verificado nesta ingestão.
3. Esta fonte preenche diretamente uma lacuna identificada em [[wiki/sources/tokens-o-que-sao-e-por-que-custam-caro]], que registrava como open question a ausência de qualquer menção a KV Cache/prompt caching como técnica que mitiga parcialmente o custo de reprocessamento — esta fonte cobre exatamente essa lacuna, mas do lado do custo de **input** (reprocessamento de prefixo), não do custo de **output** (geração autorregressiva) tratado naquela fonte. Os dois mecanismos são complementares, não conflitantes.

## Quotes

> "Ao invés de pagar pela mesma coisa, você vai deixar de pagar pela mesma coisa, você vai pagar com um valor bem descontado."

> "As soluções que não usam o cash, elas vão fazer com que o contexto seja repetido... você tá literalmente desperdiçando o recurso."

> "Na Antrópic, sei lá, seis meses atrás... se você mandasse um prompt muito pequenininho ele nunca batia, ele nunca fazia um cash."

> "Hoje na OpenAI isso é implícito, você não precisa fazer nada, só entrar dentro da condição... e ele vai ativar o prompt casting. Antigamente não era assim."

> "Se você tiver usando timestamp, tiver usando data, bota ela no fim do teu prompt, assim como for qualquer informação dinâmica vindo do teu cliente."

> "Você pode estar hitando o cash, mas você tá tentando olhar no lugar errado no teu payload."

> "Esse muito desse conhecimento não está em livros, está apenas nas ruas."
