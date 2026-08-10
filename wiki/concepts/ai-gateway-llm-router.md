---
type: concept
title: "AI Gateway / LLM Router (Proxy Multi-Provider)"
aliases: ["ai gateway", "llm gateway", "proxy multi-provider", "litellm", "portkey"]
date_created: 2026-08-05
date_updated: 2026-08-05
source_count: 1
tags: [tech-mentor-ai, ai-gateway, llm-router, proxy-pattern, fallback, multi-provider]
skill: tech-mentor-ai
status: stub
---

# AI Gateway / LLM Router (Proxy Multi-Provider)

Camada de proxy (self-hosted ou gerenciada) que fica entre a aplicação/ferramenta cliente e os providers reais de LLM (Anthropic, OpenAI, Google, OpenRouter, providers chineses etc.), expondo uma única URL/API compatível — normalmente o formato da API da Anthropic ou da OpenAI — para que o cliente funcione como *drop-in replacement*: só troca a `base_url` e a chave de API, sem mudar código nem fazer login real na conta original. Exemplos conhecidos de mercado: LiteLLM, Portkey (ver `references/ai/ai-gateway.md`, skill tech-mentor-ai). [skill: tech-mentor-ai]

## Por que existe

Sem gateway, uma aplicação fica hardcoded a um provider: se ele cai, a app cai; não há roteamento por custo, nem visibilidade centralizada de logs/gasto, nem retry inteligente em rate limit. O gateway resolve isso concentrando logging, rate limiting, cache e fallback numa única camada — ver diagrama em `references/ai/ai-gateway.md`.

## Caso concreto: [[wiki/sources/rotacao-de-contas-free-tier-llm-router-hostinger]]

A fonte descreve um gateway self-hosted (deploy de um clique via [[wiki/entities/hostinger]]) usado para dois fins distintos que costumam ser confundidos:

1. **Mapeamento de modelo** — a ferramenta cliente ([[wiki/entities/claude-code]]) "acha" que está chamando um modelo Anthropic, mas o gateway redireciona para outro modelo real (ex.: GLM 5.2 via [[wiki/entities/openrouter]]) sem o cliente perceber.
2. **[[wiki/concepts/rotacao-de-contas-free-tier]]** — cadastro de múltiplas contas do mesmo provider e rotação automática entre elas quando uma esgota a cota. Este é o padrão distinto: não escolhe o *melhor* modelo para a tarefa (isso é [[wiki/concepts/roteamento-automatico-de-modelo]]), escolhe a *próxima credencial disponível* do mesmo tipo.

Ambos os usos compartilham o mesmo mecanismo de infraestrutura — fallback com ordem de tentativa ("try in order") — mas servem objetivos diferentes: um contorna o lockin de modelo de uma ferramenta, o outro contorna limite de free tier por conta.

## Fallback: silencioso vs. observável

A fonte distingue implicitamente dois comportamentos de fallback:
- **Fallback silencioso** — a troca de modelo/conta acontece sem indicação visível ao usuário, preservando o mesmo histórico de conversa entre as trocas (o que dá a sensação de uma janela de contexto "infinita" ao longo de uma sessão longa).
- **Fallback com dashboard de custo** — apesar de silencioso na interface do cliente, o gateway mantém um painel próprio de uso (tokens de input/output, leitura de cache, custo estimado por chamada), permitindo auditoria posterior mesmo quando o roteamento em si é invisível durante o uso.

## Relação com outros conceitos

- [[wiki/concepts/roteamento-automatico-de-modelo]] — routing por *qualidade/custo de modelo*; este conceito aqui é sobre routing por *disponibilidade de credencial*, um eixo ortogonal.
- [[wiki/concepts/proxy-pattern]] — o gateway é uma aplicação concreta do padrão proxy à camada de chamadas de LLM.
- [[wiki/concepts/rate-limiting]] — a rotação de contas é, na prática, uma forma de contornar rate limiting por conta individual.
- [[wiki/concepts/vendor-lock-in-cloud]] — o autor da fonte descreve o gateway como forma de "quebrar o lockin" de uma ferramenta que só aceita, nativamente, modelos de um único vendor.

## Key Sources

- [[wiki/sources/rotacao-de-contas-free-tier-llm-router-hostinger]]
