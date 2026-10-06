---
type: concept
title: "Microagente"
aliases: ["micro agente", "microagent", "microagente de recomendação"]
date_created: 2026-10-06
date_updated: 2026-10-06
source_count: 1
tags: [microsservicos, agentes, rag, arquitetura, llm]
skill: tech-mentor-ai
status: draft
---

# Microagente

Termo da fonte para um **microsserviço inteligente**: uma nova camada ao lado dos serviços de negócio (order, payment, notification, products) e de configuração (config server, service registry) que usa LLM + [[wiki/concepts/rag-tres-etapas|RAG]] para decidir e agir. Exemplos: recomendação e detecção de fraude.

## Padrão de funcionamento

1. **Gatilho:** HTTP ([[wiki/concepts/comunicacao-sincrona]]) ou evento ([[wiki/concepts/comunicacao-assincrona]], menor acoplamento; ver [[wiki/concepts/event-driven-architecture]]).
2. **Núcleo RAG:** recupera contexto próprio (catálogo, histórico, regras) no [[wiki/concepts/vector-store]].
3. **LLM:** gera a decisão/resposta.
4. **Ação:** propaga o resultado pela arquitetura (ex.: serviço de notificação).

Também **indexa** eventos que chegam (novo produto, nova order) para manter a base atualizada ([[wiki/concepts/indexacao-vetorial]]).

## Quando faz sentido (segundo a fonte)

Quando as decisões exigiriam número inviável de `if`s/regras. O vídeo não discute o contrário: custo, latência, não-determinismo e falha do LLM no caminho do negócio.

## Tensão com "agente de IA"

[[wiki/concepts/agente-ia]] e [[wiki/sources/rag-introducao-pipeline-completo]] distinguem RAG (consulta de API com contexto) de agente (laço de decisão com ferramentas). O "microagente" do vídeo é, no código mostrado, um fluxo fixo (recuperar → prompt → chamar LLM → propagar), sem laço nem tool use. **Inferência minha:** é mais um microsserviço com RAG do que um agente no sentido estrito; o rótulo é da fonte.

## Key Sources

- [[wiki/sources/rag-spring-ai-microagente-recomendacao-michele-brito]]
