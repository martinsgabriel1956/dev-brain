---
type: source
title: "RAG com Spring AI: microagente de recomendação de passeios (Michele Brito)"
aliases: ["rag spring ai", "microagente de recomendação", "rag em microsserviços"]
date_created: 2026-10-06
date_updated: 2026-10-06
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/rag-spring-ai-microagente-recomendacao-michele-brito.md
source_url: ""
author: "[[wiki/entities/michele-brito]]"
date_published: ""
date_ingested: 2026-10-06
source_count: 0
tags: [rag, spring-ai, java, microsservicos, microagente, vector-store, pgvector, embeddings, llm]
skill: tech-mentor-ai
status: draft
---

# RAG com Spring AI: microagente de recomendação de passeios (Michele Brito)

## TL;DR

[[wiki/entities/michele-brito]] explica o [[wiki/concepts/rag-tres-etapas|RAG em três etapas]] (recuperar → aumentar → gerar) e o implementa em Java com o [[wiki/entities/spring-ai]]: um [[wiki/concepts/microagente]] de recomendação, dentro de uma arquitetura de microsserviços, que é acionado por uma nova *order* (HTTP ou evento). Primeiro faz-se a [[wiki/concepts/indexacao-vetorial]] (catálogo e histórico de pedidos viram `Document`s no [[wiki/concepts/vector-store]] [[wiki/entities/pgvector]]); depois, a cada pedido, o agente faz [[wiki/concepts/recuperacao-com-filtro-de-metadados|busca por similaridade com filtros]], monta um [[wiki/concepts/prompt-aumentado-rag|prompt aumentado]] (entrada + contexto + regras) e chama o LLM (Gemini) via `ChatClient`. Demo: 21 tours (Roma, Paris, Londres); a recomendação muda conforme o histórico do cliente.

## Key claims

**Claim:** RAG é um pipeline de três etapas: recuperação de trechos relevantes numa base externa, injeção no prompt e geração pelo LLM.
**Evidence:** definição inicial do vídeo; é o mesmo desenho de [[wiki/concepts/rag-arquitetura-avancada]] e de [[wiki/sources/rag-introducao-pipeline-completo]].
**Confidence:** alta.

**Claim:** sem contexto relevante a resposta tende a ser genérica e com [[wiki/concepts/alucinacao-llm|alucinações]]; com contexto específico fica mais precisa e aderente ao cenário.
**Evidence:** argumento da autora; no demo, só se recomenda o que está no catálogo e na mesma cidade. Sem métrica de redução de alucinação.
**Confidence:** média (qualitativo; consistente com a literatura geral, mas não medido no vídeo).

**Claim:** o histórico de RAG: "recuperar então gerar" em 2017 (Danqi Chen, *Reading Wikipedia to Answer Open-Domain Questions*); o termo RAG em 2020 (Patrick Lewis et al.); adoção prática com LLMs e vector stores a partir de 2023.
**Evidence:** citado pela autora; ver [[wiki/entities/danqi-chen]] e [[wiki/entities/patrick-lewis]]. O artigo de 2020 existe (Lewis et al., NeurIPS 2020) **[external, não verificado nesta sessão: https://arxiv.org/abs/2005.11401]**; o de 2017 é DrQA (Chen et al., ACL 2017) **[external, não verificado: https://arxiv.org/abs/1704.00051]**. Nota: a autora diz que Chen "introduziu o padrão"; DrQA é um ancestral clássico, mas "introduziu" é simplificação.
**Confidence:** média-alta nas datas e autores; média na narrativa de "introdução".

**Claim:** em microsserviços, RAG vira capacidade de uma nova camada, os [[wiki/concepts/microagente|microagentes]] (recomendação, detecção de fraude), útil onde regras em `if` seriam inviáveis pelo número de casos.
**Evidence:** arquitetura mostrada: serviços de negócio (order, payment, notification, products), serviços de configuração (config server, service registry) e microagentes. O agente é disparado por HTTP ([[wiki/concepts/comunicacao-sincrona]]) ou eventos ([[wiki/concepts/comunicacao-assincrona]], menor acoplamento), e propaga a resposta (ex.: ao `notification`).
**Confidence:** média (argumento arquitetural sem comparação de custo/latência/risco frente a regras determinísticas; ver Open questions).

**Claim:** salvam-se vetores (não o texto) porque a recuperação é semântica por similaridade, não exata como SQL.
**Evidence:** explicação do vídeo; ver [[wiki/concepts/busca-semantica]] e [[wiki/concepts/embedding-vectors]] (nota: lá o conceito é o embedding de token; aqui, embedding de documento para busca).
**Confidence:** alta. (Nuance **[skill: tech-mentor-ai]**: o texto cru também é guardado na coluna `content`, como em [[wiki/concepts/chunking]].)

**Claim:** o texto a indexar deve ser escrito em linguagem natural, próximo de uma possível pergunta, e os metadados gravados na indexação habilitam filtros na consulta.
**Evidence:** método isolado que monta a `String` (nome, localização, categoria, descrição); metadados (tipo, customer etc.) usados em `FilterExpression` separando "catálogo" de "histórico". Ver [[wiki/concepts/indexacao-vetorial]].
**Confidence:** alta no mecanismo; a escolha de campos é do exemplo.

**Claim:** a query de busca também é linguagem natural ("tours relacionados a <order> + localização"); `topK` fixo em 4; o filtro difere para catálogo e para histórico.
**Evidence:** código descrito no vídeo; ver [[wiki/concepts/top-k-retrieval]].
**Confidence:** alta (descritivo). Valor 4 é arbitrário no exemplo.

**Claim:** o prompt final combina a entrada, o contexto recuperado (catálogo + histórico) e regras/políticas pré-definidas (mesma região; não repetir tour já comprado).
**Evidence:** método de montagem do prompt isolado. Ver [[wiki/concepts/prompt-aumentado-rag]].
**Confidence:** alta.

**Claim:** o Spring AI entrega a abstração pronta: `VectorStore`, `Document`, modelo de embedding chamado "por baixo dos panos" e `ChatClient` para vários LLMs.
**Evidence:** código do demo (starters Google/Gemini para chat e embedding; PGVector). Detalhes de API (nomes de métodos, versão) vêm só da narração.
**Confidence:** média-alta (API exata não verificada na documentação oficial **[external, não verificado: https://docs.spring.io/spring-ai/reference/]**).

**Claim:** o resultado muda com o histórico: cliente que comprou Coliseu e depois Catacumbas recebeu Fórum Romano/Palatino; usuário novo em Londres, sem histórico, recebeu um leque mais aberto.
**Evidence:** três requisições do demo.
**Confidence:** média: três execuções ilustrativas, catálogo de 21 itens, sem avaliação ([[wiki/concepts/llm-evals-testing]]).

## Entities & Concepts Touched

Entidades: [[wiki/entities/michele-brito]], [[wiki/entities/spring-ai]], [[wiki/entities/pgvector]], [[wiki/entities/patrick-lewis]], [[wiki/entities/danqi-chen]], [[wiki/entities/spring-boot]], [[wiki/entities/neon-database]], [[wiki/entities/google]].

Conceitos novos: [[wiki/concepts/rag-tres-etapas]], [[wiki/concepts/microagente]], [[wiki/concepts/indexacao-vetorial]], [[wiki/concepts/vector-store]], [[wiki/concepts/prompt-aumentado-rag]], [[wiki/concepts/recuperacao-com-filtro-de-metadados]].

Conceitos existentes: [[wiki/concepts/rag-arquitetura-avancada]], [[wiki/concepts/busca-semantica]], [[wiki/concepts/chunking]], [[wiki/concepts/top-k-retrieval]], [[wiki/concepts/alucinacao-llm]], [[wiki/concepts/postgresql]], [[wiki/concepts/agente-ia]], [[wiki/concepts/comunicacao-assincrona]], [[wiki/concepts/comunicacao-sincrona]], [[wiki/concepts/event-driven-architecture]], [[wiki/concepts/embedding-vectors]], [[wiki/concepts/prompt-engineering]].

## Open questions

- **Microagente vs. RAG puro vs. agente:** [[wiki/sources/rag-introducao-pipeline-completo]] diz que RAG com contexto injetado é "uma consulta de API", não um agente. Aqui o "microagente" é essencialmente um serviço que faz RAG + uma chamada de LLM + propagação do resultado; o termo "agente" é usado de forma mais frouxa. Ver [[wiki/concepts/microagente]] e [[wiki/concepts/agente-ia]].
- Faltam: avaliação da qualidade (recall, relevância), custo e latência por evento, falha do LLM (timeout, fallback), idempotência na reentrega de eventos, [[wiki/concepts/elegibilidade-de-chunks|threshold de similaridade]], re-ranking/[[wiki/concepts/hybrid-search|busca híbrida]]. O demo também usa a mesma base para catálogo e histórico; privacidade/isolamento por usuário depende só do filtro de metadados (ver risco em [[wiki/sources/rag-introducao-pipeline-completo]]).
- O vídeo afirma que o RAG reduz alucinações, mas a regra "só recomendar o que está no catálogo" é garantida só pelo prompt: nada valida a saída (o LLM pode citar tour fora do catálogo). **Inferência minha.**

## Raw quotes

- "RAG ... é a técnica que conecta contexto ao raciocínio da IA utilizando de um pipeline de três etapas."
- "o que vai ser recuperado ... vai ser de forma semântica e não uma resposta exata que seria caso utilizássemos de uma query SQL."
- "podemos utilizar destes agentes que são capazes de agir e também de melhorar e otimizar todo o fluxo."
