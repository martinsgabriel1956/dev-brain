---
type: entity
title: "OpenCode"
aliases: ["Open Code"]
date_created: 2026-07-31
date_updated: 2026-09-04
source_count: 4
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

## Citado Junto ao Hermes como Harness "Aberto a Qualquer Modelo"

[[wiki/sources/harness-anatomia-tecnica-alem-do-claude-md]] cita o OpenCode, ao lado do [[wiki/entities/hermes-agent|Hermes]], como exemplo de harness onde "qualquer um" dos modelos de fundação (GPT, Kimi, GLM, Opus, Fable) pode ser conectado — reforçando, no mesmo ponto já documentado acima (roteamento via Custom Router da Abacus), que o modelo é o "miolo" comum entre harnesses e o OpenCode se diferencia por não travar esse miolo a um único provider.

## Usado como Harness para Comparar Custo de Agente Único vs. Agent Waves

[[wiki/sources/agent-waves-custo-modelos-fortes-fracos-kimi]] usa o OpenCode como harness para rodar um teste prático em produção (não simulação): a mesma tarefa (preview de e-mails num painel admin de newsletter) executada duas vezes — uma com um único agente Kimi K3 fazendo tudo, outra delegando a implementação a um Kimi K2.7 Code via [[wiki/concepts/subagentes|Agent Waves]] — medindo o custo real por diferença de saldo na plataforma da Kimi antes/depois de cada execução. Reforça o papel do OpenCode como harness agnóstico de provider já documentado acima: a troca entre K3 (agente único) e K3+K2.7 (Agent Waves) foi feita só trocando o modelo/prompt na mesma ferramenta, sem mudar de harness.

## Key Sources

- [[wiki/sources/harness-anatomia-tecnica-alem-do-claude-md]] — citado, junto do Hermes, como harness aberto a qualquer modelo de fundação
- [[wiki/sources/gestao-de-custo-velocidade-modelos-de-ia-fable-sol]] — conexão com Custom Router da Abacus.AI via API key
- [[wiki/sources/palantir-ceo-token-tax-nvidia-scam-ia]] — citado como destino de migração de devs saindo do Claude Code por loops de correção supérflua
- [[wiki/sources/agent-waves-custo-modelos-fortes-fracos-kimi]] — usado para testar, na prática, custo de agente único (K3) vs. Agent Waves (K3 coordinator + K2.7 worker) na mesma tarefa
