---
type: entity
title: "OpenCode"
aliases: ["Open Code"]
date_created: 2026-07-31
date_updated: 2026-07-31
source_count: 2
tags: [opencode, harness, cli, agentes-ia, model-routing]
skill: tech-mentor-ai
status: stub
---

# OpenCode

Harness de codificação agêntica em CLI, funcionalmente parecido com o [[wiki/entities/claude-code]], mas com uma diferença central: não é preso a um único provedor de modelo. Permite conectar qualquer provider compatível (tela de "connect provider") usando uma chave de API — incluindo provedores diretos como Anthropic e Moonshot (Kimi), ou um endpoint de roteamento customizado como o [[wiki/entities/abacus-ai|Custom Router da Abacus.AI]].

## Roteamento de Modelo via Provider Customizado

Segundo [[wiki/sources/gestao-de-custo-velocidade-modelos-de-ia-fable-sol]], a chave de API gerada por um Custom Router da Abacus pode ser conectada ao OpenCode do mesmo modo como qualquer outro provider — o que faz do OpenCode uma opção prática para quem já configurou um roteamento de modelo por categoria e quer usá-lo dentro de um harness agêntico completo, sem depender do ecossistema fechado de um único laboratório. Ver [[wiki/concepts/roteamento-automatico-de-modelo]].

## Migração desde o Claude Code por Loops de Correção Supérflua

[[wiki/sources/palantir-ceo-token-tax-nvidia-scam-ia]] cita (como anedota, sem link/benchmark independente) devs migrando do [[wiki/entities/claude-code]] para o OpenCode alegando que o primeiro entra em loops de "bug suspeito → sugestão de correção → reescreve testes → reescreve código → reescreve testes de novo" que consomem token sem ganho de valor proporcional — usado na fonte como exemplo concreto de como o [[wiki/concepts/harness|harness]] pode multiplicar custo mesmo com preço por token em queda.

## Key Sources

- [[wiki/sources/gestao-de-custo-velocidade-modelos-de-ia-fable-sol]] — conexão com Custom Router da Abacus.AI via API key
- [[wiki/sources/palantir-ceo-token-tax-nvidia-scam-ia]] — citado como destino de migração de devs saindo do Claude Code por loops de correção supérflua
