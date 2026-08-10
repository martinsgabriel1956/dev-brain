---
type: entity
title: "Grafana Labs"
aliases: ["Grafana", "Grafana Cloud"]
date_created: 2026-08-06
date_updated: 2026-08-06
source_count: 2
tags: [observabilidade, grafana, opentelemetry, saas, open-source]
skill: tech-mentor-infra
status: stub
---

# Grafana Labs

Empresa por trás do **Grafana** (visualização/dashboards, open source e self-hosted) e do **Grafana Cloud** (SaaS gerenciado com plano gratuito permanente além do trial temporário de onboarding). Mantém também Loki (logs), Tempo (traces) e Mimir (métricas de longo prazo) — ver `references/observability-platform.md` da skill [[wiki/concepts/observabilidade|tech-mentor-infra]] para detalhes técnicos da stack LGTM. Contribui para o OpenTelemetry junto com concorrentes diretos (Datadog, New Relic, Splunk), o que permite trocar de backend sem reinstrumentar aplicações — ver [[wiki/concepts/distributed-tracing]].

O Grafana Cloud oferece um assistente de IA embutido na própria interface web, capaz de correlacionar métricas/logs/traces automaticamente a partir de prompts em linguagem natural, criar alertas e dashboards, e abrir Pull Requests de correção via integração com GitHub — alternativa ao **Grafana MCP** usado direto no editor de código (que consome créditos de IA do editor, ao contrário do chat web). Ver [[wiki/concepts/investigacao-de-incidentes-com-ia-e-mcp]].

## Key sources

- [[wiki/sources/observabilidade-ponta-a-ponta-opentelemetry-ia-amsterdam]] — Grafana MCP usado via editor de código para correlação de telemetria
- [[wiki/sources/monitoramento-aplicacoes-ia-grafana-cloud-opentelemetry]] — assistente de IA embutido no Grafana Cloud (chat web), onboarding de conta gratuita, integração com GitHub para PRs automáticos
