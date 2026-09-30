---
type: source
title: "Como Estudar System Design — Building Blocks e o Caso Instagram Simplificado"
aliases: ["instagram simplificado", "como estudar system design", "building blocks system design video"]
date_created: 2026-09-30
date_updated: 2026-09-30
source_count: 0
tags: [system-design, building-blocks, load-balancer, cdn, cache, rate-limiter, filas, sharding, read-replicas, trade-offs, estudo]
skill: tech-mentor-system-design
status: stable
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/como-estudar-system-design-building-blocks-instagram-simplificado.md"
source_url: ""
author: "não identificado na transcrição"
date_published: ""
date_ingested: "2026-09-30"
---

## TL;DR

Vídeo em PT-BR que propõe um roteiro de 5 etapas para estudar System Design: (1) aprender os **[[wiki/concepts/building-blocks-system-design|building blocks]]**, (2) estudar problemas reais, (3) projetar [[wiki/concepts/design-em-camadas|em camadas]] (versão simples → complexa), (4) justificar cada decisão com trade-offs, (5) comparar com empresas reais. O caso didático é um **"Instagram simplificado"** (upload em disco local, PostgreSQL com `users` e `profile_url`, imagem servida pelo back end), com quatro problemas — back end lento, imagem lenta, picos derrubando o servidor, spam — e cada um mapeado a um bloco: [[wiki/concepts/load-balancer]] (múltiplas instâncias), [[wiki/concepts/cdn]] + [[wiki/concepts/amazon-s3]] (imagem estática), [[wiki/concepts/cache]] com [[wiki/concepts/redis]] (TTL de 5 min), [[wiki/concepts/rate-limiting]] (10 uploads/min/IP → 429), [[wiki/concepts/filas-e-workers]] (miniatura assíncrona) e [[wiki/concepts/read-replicas]] + [[wiki/concepts/sharding]] por região. Mensagem central: a pergunta não é "o que é um load balancer", e sim "qual é o [[wiki/concepts/gargalo]] agora e qual o custo da decisão" (latência, consistência, resiliência, custo). Fecha com a dica de treino: montar cenários próprios ([[wiki/concepts/treino-system-design-por-cenarios|YouTube simplificado]]).

---

## Reivindicações Principais

**Claim:** System Design não é decorar padrões; é entender problemas reais e tomar decisões técnicas diante deles.
**Evidência:** Afirmação do autor na abertura.
**Confiança:** Alta — converge com [[wiki/sources/como-se-comportar-na-entrevista-de-system-design-tier-s]] e [[wiki/sources/escalar-leituras-banco-de-dados-entrevista-tier-s]] (perguntar antes de dar a receita) e com [[wiki/concepts/entrevista-system-design]].

**Claim:** Existe um "padrão" de estudo em cinco etapas: building blocks → problemas reais → projeto em camadas → justificativa por trade-offs → comparação com empresas reais.
**Evidência:** Lista apresentada pelo autor; é um método pedagógico, não um resultado empírico.
**Confiança:** Média — heurística de estudo plausível e coerente com o framework de 4 etapas da skill (requisitos → estimativas → HLD → deep dive) [skill: tech-mentor-system-design, `references/system-design.md`]. **Lacuna:** o vídeo não cita a etapa de esclarecer requisitos nem de estimativas back-of-envelope, que a skill e [[wiki/concepts/entrevista-system-design]] tratam como passos iniciais obrigatórios; o caso já entra com os problemas dados, sem números (RPS, volume).

**Claim:** Load balancer resolve "muitos acessos derrubando o back end": adicionar múltiplas instâncias e balancear a carga; usar sempre que houver múltiplos servidores servindo a mesma API (Nginx, AWS).
**Evidência:** Caso Instagram simplificado; sem medição.
**Confiança:** Alta — ver [[wiki/concepts/load-balancer]], [[wiki/concepts/escalabilidade-horizontal]]. Ressalva [skill]: o LB em si vira ponto único de falha se não for redundante, e o ganho pressupõe API stateless; o vídeo não discute.

**Claim:** CDN resolve a imagem lenta; decisão: guardar a imagem em bucket S3, gerar URL pública e servir via CDN (Cloudflare, CloudFront); usar para qualquer conteúdo estático.
**Evidência:** Descrição do autor.
**Confiança:** Alta — ver [[wiki/concepts/cdn]], [[wiki/concepts/amazon-s3]], [[wiki/concepts/aws-cloudfront]]. Nota: a mudança também tira o disco local do back end (problema de estado e de escala horizontal que o vídeo não nomeia) [skill: tech-mentor-system-design].

**Claim:** Cache (Redis) evita bater no banco a cada leitura de `profile_photo_url`; indicado quando o dado é muito lido e muda pouco; guardar `user_id` + `photo_url` com TTL de 5 min e atualizar a cada novo upload.
**Evidência:** Decisão descrita pelo autor, sem medição de hit ratio.
**Confiança:** Alta para o padrão ([[wiki/concepts/cache-aside]] + [[wiki/concepts/ttl]]). Inferência: "atualizar a cada upload" equivale a invalidar/sobrescrever a chave ([[wiki/concepts/cache-invalidation]]); TTL de 5 min define a janela máxima de dado desatualizado caso a atualização falhe — o vídeo não discute esse trade-off nem [[wiki/concepts/cache-stampede]].

**Claim:** Rate limiter deve existir em endpoints públicos, sobretudo de escrita; exemplo: 10 uploads/min por IP, acima disso responder 429 Too Many Requests; trata spam/DDoS "de forma simples".
**Evidência:** Exemplo numérico do autor (1.000–10.000 uploads/s como cenário de abuso).
**Confiança:** Média-alta — ver [[wiki/concepts/rate-limiting]]. Ressalvas: limite só por IP falha contra atacantes distribuídos e pune usuários atrás de NAT (limite por usuário/token é complementar); rate limit não substitui proteção DDoS volumétrica em camada de rede/CDN ([[wiki/concepts/ddos-syn-flood]]) [skill: tech-mentor-system-design, `references/system-design-gaps.md`; não consultado em detalhe nesta sessão].

**Claim:** Fila desacopla serviços e absorve picos; após o upload, publica-se uma mensagem e um worker gera a miniatura de forma assíncrona; o usuário segue usando a plataforma enquanto uma barra de progresso indica o andamento. Autor prefere RabbitMQ (mais simples) a Kafka (muito grande) — depende do contexto.
**Evidência:** Descrição do autor, com analogia a Instagram/Twitter (não verificada).
**Confiança:** Alta para o padrão ([[wiki/concepts/filas-e-workers]], [[wiki/concepts/processamento-assincrono]], [[wiki/entities/rabbitmq]], [[wiki/concepts/kafka]]). A comparação RabbitMQ × Kafka é opinião de contexto; o vídeo omite idempotência do worker e DLQ ([[wiki/concepts/idempotencia]]). Afirmação sobre "como o Instagram faz" é não verificada [external: não consultado].

**Claim:** Para escalar leitura de banco com milhões de acessos a perfis: várias réplicas de leitura do PostgreSQL e, se preciso, sharding por região.
**Evidência:** Decisão resumida do autor.
**Confiança:** Média — corresponde à escada de leitura de [[wiki/concepts/read-replicas]] → [[wiki/concepts/sharding]]. **Ressalva:** o vídeo não cita replication lag (leitura desatualizada após upload) nem custo operacional do sharding; a wiki já registra que sharding vem depois de alternativas mais baratas (cache, réplicas) — ver [[wiki/sources/escalar-leituras-banco-de-dados-entrevista-tier-s]]. O caso aqui (cache antes de réplicas, réplicas antes de sharding) é coerente, embora a ordem de apresentação no vídeo não seja explicitamente hierárquica.

**Claim:** A pergunta certa é "qual o gargalo atual, o que posso resolver agora e qual o custo", sempre ponderando latência, consistência, resiliência e custo.
**Evidência:** Fecho conceitual do autor.
**Confiança:** Alta — reforça a regra de ouro de [[wiki/concepts/gargalo]] (medir/identificar antes de escalar) e o preceito da skill "nunca diga 'depende' sem completar o critério" [skill: tech-mentor-system-design].

**Claim:** Treinar com cenários reais próprios (ex.: YouTube simplificado com upload, vídeo, comentários, contagem de views e recomendação na home).
**Evidência:** Dica final (frase interrompida na transcrição).
**Confiança:** Média — conselho de prática, sem evidência; alinhado a [[wiki/concepts/simulador-de-system-design]] e [[wiki/concepts/treino-system-design-por-cenarios]].

---

## Entidades e Conceitos Tocados

- [[wiki/concepts/building-blocks-system-design]] — novo: catálogo dos 7 blocos e critério "quando usar"
- [[wiki/concepts/design-em-camadas]] — novo (stub): simples → complexo, um gargalo por vez
- [[wiki/concepts/treino-system-design-por-cenarios]] — novo (stub): treino com casos próprios
- [[wiki/concepts/load-balancer]], [[wiki/concepts/cdn]], [[wiki/concepts/cache]], [[wiki/concepts/rate-limiting]], [[wiki/concepts/filas-e-workers]], [[wiki/concepts/read-replicas]], [[wiki/concepts/sharding]] — os blocos aplicados ao caso
- [[wiki/concepts/amazon-s3]], [[wiki/concepts/redis]], [[wiki/concepts/postgresql]], [[wiki/concepts/ttl]], [[wiki/entities/rabbitmq]], [[wiki/concepts/kafka]] — tecnologias citadas
- [[wiki/concepts/gargalo]], [[wiki/concepts/entrevista-system-design]], [[wiki/concepts/processamento-assincrono]] — enquadramento do raciocínio

---

## Perguntas Abertas

- Qual a escala-alvo do "Instagram simplificado" (DAU, RPS, GB/dia)? Sem ela não há como justificar cada bloco — ver estimativas em [[wiki/concepts/entrevista-system-design]].
- Como manter coerência entre cache (TTL 5 min) e réplicas de leitura após upload novo (lag)?
- Sharding "por região": qual a shard key e como fica o acesso cross-region ao perfil de um usuário viajando? (ver [[wiki/concepts/db-sharding]])
- Autor e canal não identificados na transcrição; afirmações sobre Instagram/Twitter não verificadas.

## Citações Brutas

> "o System Design ele é uma habilidade de criar soluções escaláveis, resilientes e performáticas [...] não é sobre você decorar padrões e sim entender problemas reais e tomar decisões mais técnicas"

> "a pergunta não é o que é o load balancer [...] a pergunta que tu tem que te fazer é: qual é o gargalo atual do meu sistema [...] e qual o custo que eu vou ter dessa decisão"
