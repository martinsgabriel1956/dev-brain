---
type: concept
title: "Investigação de Incidentes com IA e MCP"
aliases: ["ia observabilidade", "agente investigando incidentes", "relatório automatizado de telemetria", "grafana mcp"]
date_created: 2026-07-15
date_updated: 2026-07-15
source_count: 1
tags: [observabilidade, mcp, ia, agente-ia, opentelemetry, incident-response]
skill: tech-mentor-infra
status: draft
---

# Investigação de Incidentes com IA e MCP

Padrão em que um agente de IA, conectado a servidores MCP que expõem backends de observabilidade (ex. **Grafana MCP**, dando acesso a Prometheus, Loki e Tempo/Jaeger), correlaciona métricas, logs e traces automaticamente para diagnosticar a causa raiz de um incidente — sem que um humano precise entrar manualmente em cada base de dados e cruzar IDs.

## Pré-requisito: os dados já têm que existir

O padrão só funciona se a aplicação já estiver instrumentada de ponta a ponta com [[wiki/concepts/distributed-tracing|OpenTelemetry]] (ou equivalente), com [[wiki/concepts/observabilidade|os três pilares]] centralizados. O agente de IA acelera a **correlação**, não substitui a **coleta** — sem telemetria coletada, não há o que correlacionar. Essa é a lição central da fonte que originou esta página: "o ouro está nos dados, não na IA".

## Como funciona na prática

1. Um dashboard (ex. Grafana) já aponta um sintoma — ex. "914 erros 500 num endpoint específico".
2. O operador escreve um prompt simples pedindo investigação daquele endpoint num intervalo de tempo, com relatório final.
3. O agente, via [[wiki/concepts/model-context-protocol|MCP]], consulta métricas (Prometheus), logs (Loki) e traces (Tempo/Jaeger) sozinho.
4. O relatório retornado não fica só no "o quê" — chega até a linha de código específica da causa raiz (ex. "linhas 25–31: limite de conexões de banco excedido").

Ponto notável: é possível que o agente sequer tenha acesso ao repositório de código-fonte — apenas às bases de telemetria via MCP — e ainda assim aponte a linha de código exata da causa, porque stack traces e mensagens de erro nos logs/spans já carregam essa informação.

## Extensão natural: relatório vira PR automaticamente

Combinando o MCP de observabilidade com um MCP de documentação de código (ex. **Context7**, para obter a doc atualizada da lib que precisa mudar), o mesmo fluxo pode virar um agente disparado a cada deploy ou a cada alerta, que investiga, abre um PR de correção, e o time humano só revisa e aprova — em vez de investigar do zero.

## Por que isso não é "mágica de IA"

O agente não está adivinhando — está fazendo o mesmo trabalho de correlação manual (cruzar traceId entre logs/traces/métricas) que um especialista faria, só que em segundos em vez de semanas. A etapa que historicamente consumia mais tempo (reunir e cruzar dados espalhados manualmente) é a etapa que a automação elimina; o raciocínio sobre causa raiz continua dependendo dos dados estarem lá.

## Relacionado

[[wiki/concepts/observabilidade]] · [[wiki/concepts/distributed-tracing]] · [[wiki/concepts/mcp-server]] · [[wiki/concepts/model-context-protocol]] · [[wiki/concepts/agente-ia]]

## Key Sources

- [[wiki/sources/observabilidade-ponta-a-ponta-opentelemetry-ia-amsterdam]]
