---
type: source
title: "8 Pontos de Arquitetura de Software na Era da IA"
aliases: ["8 pontos arquitetura IA", "roadmap arquitetura IA Full Cycle"]
date_created: 2026-08-14
date_updated: 2026-08-14
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/8-pontos-arquitetura-de-software-na-era-da-ia.md
source_url: ""
author: "Full Cycle (apresentador não identificado no áudio)"
date_published: "2026"
date_ingested: 2026-08-14
source_count: 0
tags: [arquitetura, ia, agentes-ia, mcp, design-patterns, cache, seguranca, prompt-engineering, context-engineering, system-design, observabilidade, testes, custos, carreira]
skill: tech-mentor-system-design
status: stable
---

# 8 Pontos de Arquitetura de Software na Era da IA

## TL;DR

Vídeo da [[wiki/entities/full-cycle|Full Cycle]] propondo um roadmap de oito frentes que todo desenvolvedor precisa estudar porque a IA tornou geração de código commodity e elevou o piso de exigência em arquitetura: (1) agentes de IA e protocolos de comunicação (MCP, A2A), (2) design patterns focados em IA (12 Factor Agents), (3) caching (de LRU/TTL clássico a cache de tokens/embeddings), (4) segurança (jailbreak, prompt injection, guardrails, OWASP Top 10 LLM), (5) prompt engineering e context engineering (com versionamento de prompt em CI/CD), (6) system design/escala/observabilidade com IA (RAG, bancos vetoriais, tracing de LLM), (7) testes de qualidade em sistemas com IA (evals, snapshots), (8) controle de custos (tokens de input/output, cache, roteamento de modelo por tarefa). Tese central: o desenvolvedor vai atuar cada vez mais como arquiteto porque pilotar IA exige entender o impacto do código gerado — sem isso, ele não consegue avaliar o que está aceitando.

## Key Claims

| Claim | Evidência | Confiança |
|---|---|---|
| O papel do desenvolvedor está migrando para o de arquiteto | Sem entender arquitetura, o dev não consegue avaliar o código que a IA gera nem seu impacto no projeto | Alta (tese central, sem dado quantitativo) |
| Um agente de IA é estruturalmente diferente de um software comum, mesmo rodando como microsserviço | Comparação direta feita no vídeo entre arquitetura de agente e arquitetura de microsserviço tradicional | Média — afirmação qualitativa do autor, sem detalhamento técnico da diferença estrutural |
| SSE está depreciado no ecossistema MCP em favor de streamable HTTP | Citado diretamente no vídeo como mudança de transporte necessária para escalar MCP dentro de empresas | Média — não citada fonte primária (spec MCP); consistente com [[wiki/concepts/model-context-protocol]] |
| Caching mal compreendido em IA afeta latência e principalmente custo | Cada chamada a LLM e cada token tem custo direto; sem estratégia de cache, custo escala com uso | Alta — consistente com [[wiki/concepts/cache]] e a lógica de token pricing |
| Prompt injection é mais grave que jailbreak | Jailbreak muda o comportamento/tom da resposta; prompt injection pode extrair dados sensíveis e executar operações destrutivas no sistema | Alta — distinção padrão na literatura de segurança de LLM |
| Escalar com IA exige balancear performance, custo e qualidade como um trade-off, não uma meta única | Nem todo modelo serve para todo caso de uso; multi-model pipelines podem ser mais baratos e rápidos que um único modelo | Média — afirmação de bom senso de mercado, sem benchmark citado no vídeo |
| RAG bem feito é mais complexo que "buscar no banco vetorial e jogar no contexto" | Cita metadado, estruturação, tipos de documento, versionamento, invalidação e sincronização como exigências reais em escala | Alta — consistente com a complexidade de RAG documentada na literatura |
| Versionamento de prompt não é trivial (não é só Git) | Uma nova versão de prompt pode quebrar o sistema; requer validação e rollback, idealmente via gate em CI/CD | Média — recomendação prática do autor, sem exemplo de ferramenta específica no vídeo |

## Pontos e Conceitos

### 1 — Agentes de IA e Protocolos de Comunicação

- [[wiki/concepts/agente-ia]] — distinção agente vs. microsserviço tradicional; tipos de arquitetura (paralela, sequencial, customizada/workflow forçado, autônoma)
- [[wiki/concepts/model-context-protocol]] — MCP como protocolo para tools/resources/prompts; mudança de STDIO para streamable HTTP; SSE depreciado
- [[wiki/concepts/agent-to-agent-protocol]] — A2A (Google), comunicação entre agentes de frameworks diferentes
- Evaluation de agentes como resposta ao comportamento não determinístico — ver [[wiki/concepts/llm-evals-testing]]

### 2 — Design Patterns Focados em IA

- [[wiki/concepts/design-patterns-ia]] — patterns de integração com LLM, patterns de criação de agentes, patterns de segurança (múltiplos agentes contra contaminação por prompt injection), **12 Factor Agents** como analogia ao [[wiki/concepts/twelve-factor-app|Twelve-Factor App]] da Heroku

### 3 — Caching

- [[wiki/concepts/cache]] — conceitos clássicos (TTL, cache-aside, write-through, LRU/LFU/FIFO/MRU) continuam válidos; camada nova: cache de tokens (por provider), cache de contexto/embeddings em RAG, cache-aware prompts e fingerprints

### 4 — Segurança

- [[wiki/concepts/prompt-injection-jailbreak]] — jailbreak (sugestionar comportamento fora do esperado) vs. prompt injection (extração de dados sensíveis, execução destrutiva)
- [[wiki/concepts/ai-safety-guardrails|Guardrails]] — validação antes/depois de chamar agente ou tool
- OWASP Top 10 para LLM/IA Generativa como equivalente ao OWASP Top 10 tradicional

### 5 — Prompt Engineering e Context Engineering

- [[wiki/concepts/prompt-engineering]] — técnicas citadas: chain of thought, tree of thoughts, skeleton of thoughts, ReAct, self-refining
- [[wiki/concepts/context-engineering-harness]] — dar o máximo de contexto real-time (docs, design docs, playbooks) como ativo de longo prazo, análogo a teste automatizado
- Versionamento de prompt e histórico de interação com validação e rollback via CI/CD — não é "versionar no Git e pronto"

### 6 — System Design, Escala e Observabilidade

- Triângulo performance/custo/qualidade como trade-off central de escala — ver [[wiki/concepts/ai-gateway-llm-router]]
- Pipelines/mensageria (Kafka, RabbitMQ), bancos vetoriais (inclusive Redis com suporte a vetor como camada de cache)
- [[wiki/concepts/rag-arquitetura-avancada]] — RAG além de "buscar e jogar no contexto": metadado, estruturação, versionamento, invalidação, sincronização
- [[wiki/concepts/observabilidade]] — tracing de LLM, latência entre chamadas de agentes, Open Telemetry orientado a IA

### 7 — Testes de Qualidade em Sistemas com IA

- [[wiki/concepts/llm-evals-testing]] — testes de prompts/contextos ("promptings"), frameworks que geram variações de prompt, avaliação com datasets reais e snapshots para comportamento determinístico

### 8 — Controle de Custos em Arquiteturas com IA

- [[wiki/concepts/ai-gateway-llm-router]] — input tokens vs. output tokens, limites por modelo, estratégias de cache para custo, estimativas por usuário/chamada/multiagente, truncamento e sumarização, uso de múltiplos modelos mais baratos em pipeline em vez de um único modelo caro

## Entidades

- [[wiki/entities/full-cycle]] — canal/MBA autor do conteúdo

## Open Questions

- O vídeo não cita fonte primária para "SSE está depreciado" no MCP — vale checar a spec oficial do protocolo para confirmar o status exato (depreciado vs. apenas superado em uso).
- Não fica claro no vídeo se "arquitetura de agente estruturalmente diferente de microsserviço" se refere a diferenças de runtime, de contrato de interface, ou só ao comportamento não determinístico — carece de detalhamento técnico.
- Quais frameworks concretos de teste de prompt (além de LangSmith, citado de passagem) o autor recomendaria na prática?

## Quotes

> "O desenvolvedor não vai mais ficar digitando o código o tempo todo, ele vai ter que ser capaz de pilotar IA. E para isso ele precisa de conhecimentos profundos para inclusive entender aquele código que está sendo gerado e qual vai ser o impacto que tudo aquilo vai ter no projeto."

> "Nada muda mais o seu software do que quando a escala do seu software muda."

> "Cada vez que a gente chama um LLM a gente gasta. Cada token custa dinheiro."

> "A trabalha [a IA] de forma não determinística. Ela não funciona apenas com ifs e elses que a gente tá acostumado nos nossos softwares."
