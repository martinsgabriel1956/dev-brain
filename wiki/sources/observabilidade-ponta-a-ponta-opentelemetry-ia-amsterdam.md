---
type: source
title: "Observabilidade de Ponta a Ponta com OpenTelemetry — Palestra em Amsterdã"
aliases: ["observabilidade ponta a ponta opentelemetry", "palestra amsterdam opentelemetry"]
date_created: 2026-07-15
date_updated: 2026-07-15
source_count: 0
tags: [observabilidade, opentelemetry, distributed-tracing, mcp, ia, performance, seguranca, supply-chain]
skill: tech-mentor-infra
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/observabilidade-ponta-a-ponta-opentelemetry-ia-amsterdam.md
source_url: ""
author: "Eric (ver [[wiki/entities/eric-lenda]])"
date_published: ""
date_ingested: 2026-07-15
---

# Observabilidade de Ponta a Ponta com OpenTelemetry — Palestra em Amsterdã

## TL;DR

Reapresentação em vídeo de uma palestra dada em Amsterdã: como instrumentar aplicações de ponta a ponta (front-end + back-end) com OpenTelemetry — logs, métricas e traces de um único SDK, roteados por um Collector central para backends especializados (Prometheus, Loki, Tempo/Jaeger), visualizados no Grafana. O ponto central é que o valor não está na investigação nem na IA isoladamente, mas na **coleta de dados**: uma vez que a telemetria está centralizada, um agente de IA conectado via servidores MCP (Grafana MCP, Context7) consegue correlacionar métricas + logs + traces sozinho e produzir, em minutos, o mesmo relatório de causa-raiz que antes levava semanas de investigação manual.

## Key Claims

**Claim:** OpenTelemetry é um padrão vendor-neutral, não uma ferramenta de um fornecedor — praticamente todos os concorrentes do mercado de observabilidade (New Relic, Splunk, Google, Amazon, Grafana, Datadog) contribuem para o mesmo projeto.
**Evidence:** Gráfico de contribuições ao longo dos anos mostrado na palestra, citando essas empresas nominalmente como contribuidoras do mesmo protocolo, apesar de cada uma manter sua própria ferramenta de coleta/visualização.
**Confidence:** alta (consistente com o status de projeto CNCF graduated já documentado em [[wiki/concepts/distributed-tracing]] e na referência `tech-mentor-infra/observability/opentelemetry-deep.md`)

**Claim:** A arquitetura correta em produção é a aplicação enviar telemetria para o OpenTelemetry Collector, e o Collector distribuir para os backends especializados — nunca a aplicação enviar direto para Prometheus/Loki/Tempo.
**Evidence:** Apontado explicitamente como "erro comum": mandar o dado direto da aplicação pro Prometheus. A boa prática é ter um ponto único de configuração/formatação/roteamento (o Collector), de onde os dados são distribuídos para métricas → Prometheus, logs → Loki, traces → Tempo/Jaeger, e o Grafana funciona como hub de consulta correlacionando as três fontes.
**Confidence:** alta

**Claim:** Instrumentar bibliotecas de terceiros (não só o próprio código de negócio) revela gargalos que o desenvolvedor não suspeitaria.
**Evidence:** Caso real relatado pelo autor: instrumentação revelou que um pacote compartilhado por todos os microsserviços de uma empresa estava travando o event loop do Node.js; atualizar o pacote gerou ~50% de ganho de velocidade nas aplicações.
**Confidence:** alta (relato de primeira mão do autor, mas sem nome do pacote/empresa identificável)

**Claim:** Ambientes de staging não são confiáveis para investigação de performance porque divergem de produção em dados e capacidade de máquina — a investigação deve mirar produção (ou simular carga localmente com ferramentas como Clinic.js).
**Evidence:** Relato do processo de consultoria do autor: staging tinha "potência de máquina reduzida" e dados não fiéis ao tráfego real, então ele sempre mirava produção diretamente, complementando com testes de carga locais quando precisava reproduzir um cenário controlado.
**Confidence:** média — é uma prática pessoal relatada, não uma regra universalmente citada com fonte externa

**Claim:** Uma vez com a telemetria centralizada via OpenTelemetry, um agente de IA com acesso a servidores MCP (ex. Grafana MCP, expondo Prometheus/Loki/Tempo) consegue correlacionar métricas, logs e traces e identificar a causa raiz de um erro em código específico — mesmo sem ter acesso ao código-fonte do projeto, apenas às bases de telemetria.
**Evidence:** Demonstração ao vivo: prompt simples pedindo investigação de um endpoint retornando erro `500` nos últimos 15 minutos; o agente retornou linhas de código específicas (25–31) e a causa (limite de conexões de banco excedido), tendo acesso apenas ao Grafana MCP, não ao repositório.
**Confidence:** média-alta — demonstração ao vivo e reproduzível em conceito, mas é um único exemplo, sem generalização estatística sobre taxa de acerto do agente em causas mais sutis

**Claim:** Um servidor comprometido por RCE (Next.js/React) só não teve o ataque escalado porque estava isolado em um container Kubernetes — o isolamento de execução limitou o blast radius mesmo com código arbitrário sendo executado.
**Evidence:** Caso relatado pelo autor: minerador de Bitcoin rodando em memória (binário autodeletado do disco), identificado via GitHub Copilot investigando um pico de CPU; o Copilot reportou que a tentativa de escalar privilégios/se espalhar falhou por causa do isolamento do container.
**Confidence:** média — relato de primeira mão sem CVE citado; consistente com o princípio geral de defesa em profundidade já documentado na wiki

## Concepts & Entities Touched

[[wiki/concepts/observabilidade]] · [[wiki/concepts/distributed-tracing]] · [[wiki/concepts/mcp-server]] · [[wiki/concepts/model-context-protocol]] · [[wiki/concepts/investigacao-de-incidentes-com-ia-e-mcp]] · [[wiki/concepts/gargalo]] · [[wiki/entities/eric-lenda]] · [[wiki/entities/anthropic]]

## Open Questions

- O nome do framework em que o autor prestou consultoria de performance saiu distorcido na transcrição ("Miture JS" / "mito"). Não foi possível identificar com confiança — registrado aqui em vez de arriscar um nome errado na wiki.
- Nenhum link real do repositório de exemplo "multi-serviço instrumentado de ponta a ponta" citado na palestra foi capturado na transcrição (só a menção a um QR code/slide).
- A vulnerabilidade específica do Next.js/React explorada no caso do minerador de Bitcoin não foi identificada por CVE — o autor menciona ter vídeo dedicado ao assunto no próprio canal, não referenciado aqui por falta de URL.

## Raw Quotes

> "O ouro não está na investigação, o ouro não está na inteligência artificial, ele está na coleta dos dados."

> "Sem dados, você fica no escuro."

> "Todos os concorrentes se juntaram em um único lugar para transformar uma ferramenta em algo melhor."
