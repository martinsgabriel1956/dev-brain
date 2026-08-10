---
type: concept
title: "Investigação de Incidentes com IA e MCP"
aliases: ["ia observabilidade", "agente investigando incidentes", "relatório automatizado de telemetria", "grafana mcp"]
date_created: 2026-07-15
date_updated: 2026-08-06
source_count: 3
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

## Duas Superfícies para o Mesmo Padrão: Chat Web vs. MCP no Editor

O mesmo padrão de correlação automática aparece em pelo menos duas superfícies distintas no ecossistema Grafana, com implicação de custo diferente:

- **Grafana MCP no editor de código** (ex. Claude Code): o agente do editor chama o MCP como tool. Consome créditos de IA do próprio editor/plano de IA do usuário.
- **Assistente de IA embutido na interface web do Grafana Cloud**: chat próprio da plataforma, sem sair do navegador. Não consome créditos de IA do editor do usuário — o custo (se houver) é do plano do Grafana Cloud, não do assistente de código.

Em ambos os casos, o mesmo prompt genérico ("investigue os erros dessa aplicação, correlacionando logs/métricas/traces, e aponte a linha de código") produziu resultado equivalente: relatório com causa raiz e linha de código específica, sem contexto adicional fornecido e sem acesso ao repositório — nesse caso um vazamento de conexões PostgreSQL nunca liberadas ao pool, esgotando o limite de conexões e causando timeouts (ver [[wiki/concepts/connection-pooling]]). O chat web ainda oferece, direto da mesma conversa, criar alerta, criar dashboard, e abrir Pull Request de correção via integração com GitHub — estendendo na prática o fluxo "relatório vira PR automaticamente" descrito abaixo sem precisar de um segundo MCP de documentação de código.

## O Limite do Padrão: Guardrails Podem Recusar Investigar o Próprio Ataque

[[wiki/sources/modelo-openai-escapa-sandbox-benchmark-cyberseguranca]] documenta um caso em que este padrão falhou por um motivo que a página original não previa: durante um incidente real de segurança (~17.000 linhas de eventos gerados por um ataque, volume acima da capacidade de análise manual humana), o time tentou usar modelos padrão com [[wiki/concepts/agent-containment|guardrails]] ativos (via API pública) exatamente como descrito acima — pedir que o agente correlacione os dados e aponte a causa raiz. Os modelos **se recusaram a ajudar**, porque não distinguiram "investigar um ataque" (uso defensivo legítimo) de "executar um ataque" (o que os guardrails de intenção existem para bloquear). A solução encontrada foi hospedar um modelo sem guardrails (GLM 5.2) na própria infraestrutura, especificamente para essa investigação — ver [[wiki/concepts/soberania-digital]].

Isso expõe uma tensão que não estava explícita nesta página: o padrão de "agente investiga telemetria via MCP" assume implicitamente que o agente vai cooperar com a tarefa de investigação. Quando a telemetria em si descreve um ataque em andamento, essa suposição pode quebrar — o mesmo classificador de intenção que protege o produto em produção pode bloquear o time que está tentando se defender usando a mesma ferramenta.

## Relacionado

[[wiki/concepts/observabilidade]] · [[wiki/concepts/distributed-tracing]] · [[wiki/concepts/mcp-server]] · [[wiki/concepts/model-context-protocol]] · [[wiki/concepts/agente-ia]]

## Key Sources

- [[wiki/sources/observabilidade-ponta-a-ponta-opentelemetry-ia-amsterdam]]
- [[wiki/sources/modelo-openai-escapa-sandbox-benchmark-cyberseguranca]] — caso em que guardrails padrão recusaram ajudar a investigar um ataque real, exigindo modelo self-hosted sem guardrails
- [[wiki/sources/monitoramento-aplicacoes-ia-grafana-cloud-opentelemetry]] — mesmo padrão via chat web do Grafana Cloud (não MCP), sem consumo de créditos do editor; identificou vazamento de connection pool e ofereceu abrir PR de correção direto do chat
