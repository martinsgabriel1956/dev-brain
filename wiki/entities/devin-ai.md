---
type: entity
title: "Devin (Cognition AI)"
aliases: ["Devin AI", "Cognition Devin"]
date_created: 2026-07-30
date_updated: 2026-09-03
source_count: 2
tags: [devin, cognition, cloud-agent, agente-de-codigo]
skill: tech-mentor-ai
status: stub
---

# Devin (Cognition AI)

Agente de IA de codificação da Cognition, apresentado como "engenheiro de software autônomo" — precursor do padrão de **agente na nuvem** (cloud agent): sessão iniciada via chat (inclusive pelo Slack), que provisiona um sandbox isolado, clona o repositório-alvo, inicializa o ambiente e executa a tarefa por conta própria, sem exigir infraestrutura local do usuário.

## Uso Relatado no Mercado Brasileiro

Segundo [[wiki/sources/claude-tag-slack-terceiro-paradigma-llm]], o Nubank teria utilizado o Devin para refatorar um código estimado em meses de trabalho em poucos dias (relato de segunda mão na fonte, não confirmado com dado oficial do Nubank).

## Relação com o Claude Tag

Citado pelo apresentador da fonte como precedente direto do padrão de "agente na nuvem" que o Claude Tag da Anthropic (ver [[wiki/entities/anthropic]]) reintroduz em maior escala — mesma lógica de "iniciar pelo Slack, agente roda sozinho em ambiente isolado", agora com adição de memória compartilhada multiplayer por canal e integração organizacional ampla. Ver [[wiki/concepts/paradigmas-interface-llm]].

## Posição da Cognition Sobre Multi-Agente: "Subagentes São Perigosos"

[[wiki/sources/subagentes-quando-vale-a-pena-custo-velocidade-tlc-spec-driven]] cita a Cognition (empresa da Devin, que adquiriu o Windsurf) defendendo que subagentes atrapalham o contexto: toda ação de um agente carrega uma decisão que fica registrada na sua janela; quando o trabalho é delegado a um subagente novo, esse subagente não herda essas decisões anteriores. O autor da fonte conecta esse argumento a um resultado concreto do próprio benchmark que fez: um subagente por task (granularidade máxima) derrubou a nota de qualidade de 0,93 para 0,81 frente a rodar tudo num único agente — consistente com a tese da Cognition de que fragmentar demais o contexto entre agentes prejudica o resultado. Ver [[wiki/concepts/subagentes]].

## Key Sources

- [[wiki/sources/claude-tag-slack-terceiro-paradigma-llm]] — citado como precedente do padrão de cloud agent, incluindo caso de uso relatado (Nubank)
- [[wiki/sources/subagentes-quando-vale-a-pena-custo-velocidade-tlc-spec-driven]] — posição da Cognition contra multi-agente (fragmentação de decisões no contexto), conectada a um resultado de benchmark próprio do autor da fonte
