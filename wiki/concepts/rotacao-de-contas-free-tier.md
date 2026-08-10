---
type: concept
title: "Rotação de Contas Free Tier"
aliases: ["rotação de free tier", "account rotation", "conta descartável de llm"]
date_created: 2026-08-05
date_updated: 2026-08-05
source_count: 1
tags: [tech-mentor-ai, free-tier, rate-limiting, fallback, risco-de-conta, tos]
skill: tech-mentor-ai
status: stub
---

# Rotação de Contas Free Tier

Prática de cadastrar múltiplas contas free tier do mesmo provider de LLM (ex.: três contas Gemini, três contas Anthropic) atrás de um [[wiki/concepts/ai-gateway-llm-router|AI Gateway]], configurado para avançar automaticamente para a próxima conta assim que a corrente esgota sua cota gratuita — em vez de esperar o reset do rate limit (ex.: janela de 4h/24h) ou pagar por um plano superior.

## Como difere de model routing

Fácil de confundir com [[wiki/concepts/roteamento-automatico-de-modelo]], mas o eixo de decisão é diferente:

| | Model Routing | Rotação de Free Tier |
|---|---|---|
| O que varia entre as opções | Modelo (qualidade, custo, latência) | Credencial (mesma "qualidade" de modelo, conta diferente) |
| Critério de troca | Complexidade da tarefa, SLA, custo-tier | Cota da conta esgotada |
| Objetivo | Melhor resposta pelo menor custo | Contornar limite individual de uso gratuito |

## Risco reconhecido pela fonte

[[wiki/sources/rotacao-de-contas-free-tier-llm-router-hostinger]] descreve a prática mas não a recomenda para uso profissional: provedores como Gemini CLI e Claude Code têm detecção de uso não-oficial da ferramenta (fingerprint de client, padrão de chamadas fora do app oficial, etc.) e podem banir a conta. O autor situa isso como aceitável para estudo/projetos pessoais de baixo orçamento, mas explicitamente "não confiaria 100%" para trabalho do dia a dia onde continuidade de acesso importa.

Distinção que a própria fonte faz: isso não é pirataria (não quebra autenticação nem paga menos por um serviço específico contornando cobrança) — é descrito como uso de contas às quais o usuário já tem acesso legítimo, mas em volume/automação que provavelmente viola os termos de uso esperados de uma conta free tier individual (risco de ToS, não de ilegalidade).

## Relação com outros conceitos

- [[wiki/concepts/ai-gateway-llm-router]] — a rotação depende de um gateway para funcionar; é um dos dois usos descritos na fonte principal.
- [[wiki/concepts/rate-limiting]] — a rotação é, mecanicamente, uma forma de escapar do rate limit por conta.
- [[wiki/concepts/vendor-lock-in-cloud]] — motivação adjacente (usar ferramenta fora do vendor pretendido), mas eixo diferente (custo/acesso, não portabilidade de infraestrutura).

## Key Sources

- [[wiki/sources/rotacao-de-contas-free-tier-llm-router-hostinger]]
