---
type: source
title: "Rate Limit em APIs: história, onde aplicar e estado compartilhado"
aliases: ["rate limit arquitetura bernardo lobato", "rate limit onde aplicar"]
date_created: 2026-10-06
date_updated: 2026-10-06
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/rate-limit-arquitetura-onde-aplicar-estado-compartilhado-bernardo-lobato.md
source_url: ""
author: "Bernardo Lobato"
date_published: ""
date_ingested: 2026-10-06
source_count: 0
tags: [rate-limiting, token-bucket, leaky-bucket, api-gateway, estado-compartilhado, redis, http-429, borda, arquitetura-distribuida]
skill: tech-mentor-backend
status: draft
---

# Rate Limit em APIs: história, onde aplicar e estado compartilhado

## TL;DR

[[wiki/entities/bernardo-lobato]] trata [[wiki/concepts/rate-limiting]] como **decisão de arquitetura**, não como "limitadorzinho no código". Origem em redes de pacotes ([[wiki/concepts/traffic-shaping-e-traffic-policing]], [[wiki/concepts/leaky-bucket]], [[wiki/concepts/token-bucket]]) e chegada ao HTTP com o [[wiki/concepts/http-429-too-many-requests]] (RFC 6585, 2012). Três lugares para aplicar — aplicação, API Gateway/LB/proxy, borda (CDN/WAF) — cada um com um trade-off entre contexto e custo ([[wiki/concepts/rate-limit-camadas-de-posicionamento]]); não é preciso escolher só um. Com várias instâncias, contador em memória quebra a política (3 × 100 = 300): é preciso estado compartilhado, que traz latência, concorrência, consistência e vira dependência crítica e possível SPOF ([[wiki/concepts/rate-limit-estado-compartilhado]]). O 429 também muda o comportamento do cliente (backoff/retry). Algoritmos (fixed/sliding window) ficaram para uma parte 2 do vídeo.

## Key claims

**Claim:** rate limit é mais antigo que a web; vem do controle de taxa em redes de pacotes (traffic shaping retém pacotes, traffic policing descarta/marca os excedentes).
**Evidence:** "esse problema... é bem mais antigo que a web... traffic shaping... segurando temporariamente alguns pacotes... traffic policing... pode descartar ou marcar os pacotes."
**Confidence:** alta (coincide com o skill, `rate-limiting.md`: leaky bucket = saída constante, token bucket = bursts até a capacidade).

**Claim:** leaky bucket dá saída previsível; token bucket acumula fichas e permite picos controlados; sem tokens a requisição é rejeitada **ou adiada**.
**Evidence:** analogia do balde com saída controlada vs. balde de fichas repostas a taxa fixa.
**Confidence:** alta. Nota: o skill descreve o leaky bucket como fila FIFO com saída constante; o autor usa só a analogia.

**Claim:** o 429 Too Many Requests surgiu em 2012 na RFC 6585, com `Retry-After` opcional.
**Evidence:** "veio em 2012 com a RFC 6585... opcionalmente a resposta pode informar... retry after."
**Confidence:** alta; `[skill: tech-mentor-backend]` registra `Retry-After` como obrigatório na prática (ausência induz retry em loop apertado) — o autor diz "opcionalmente". Ver [[wiki/concepts/http-429-too-many-requests]].

**Claim:** rejeitar não é a única resposta ao limite; depende do algoritmo e da configuração.
**Evidence:** "a requisição não precisa necessariamente ser rejeitada."
**Confidence:** média (afirmado, não exemplificado; detalhe prometido para a parte 2). `[skill: tech-mentor-backend]`: throttling atrasa/degrada, rate limiting rejeita.

**Claim:** aplicação = mais contexto de negócio (usuário, plano, tenant, permissões) e mais complexidade; gateway/LB = equilíbrio e política central; borda = bloqueio cedo e barato, mas sem contexto; as camadas combinam.
**Evidence:** seção "Onde posicionar" e resumo final.
**Confidence:** alta (qualitativo). Ver [[wiki/concepts/rate-limit-camadas-de-posicionamento]].

**Claim:** contador em memória por instância multiplica o limite (3 instâncias × 100 = até 300); a correção é estado compartilhado externo, que traz latência, concorrência, consistência, disponibilidade e nova dependência crítica.
**Evidence:** exemplo numérico do vídeo.
**Confidence:** alta. Ver [[wiki/concepts/rate-limit-estado-compartilhado]], [[wiki/concepts/estado-compartilhado]].

**Claim:** o rate limiter pode virar gargalo e SPOF do sistema que protege; precisa ser tão escalável e resiliente quanto a aplicação.
**Evidence:** "todas as requisições precisam consultar um estado centralizado... não deveria se tornar um single point of failure."
**Confidence:** alta; sem número ou mitigação concreta no vídeo (lacuna; ver [[wiki/concepts/single-point-of-failure]]).

**Claim:** o cliente que recebe 429 precisa de política de backoff/retry; rate limit altera o comportamento e a experiência dos consumidores.
**Evidence:** "um cliente que receba um 429 precisa saber o que fazer."
**Confidence:** alta. Ver [[wiki/concepts/retry-backoff]].

## Entidades

[[wiki/entities/bernardo-lobato]], [[wiki/entities/cloudflare]], [[wiki/entities/kong]], [[wiki/entities/spring-cloud-gateway]], [[wiki/entities/bucket4j]], [[wiki/entities/nestjs-throttler]], [[wiki/entities/spring-boot]] (Bucket4j integra-se ao Spring Security/filtros), [[wiki/concepts/redis]].

## Conceitos

[[wiki/concepts/rate-limiting]], [[wiki/concepts/token-bucket]], [[wiki/concepts/leaky-bucket]], [[wiki/concepts/traffic-shaping-e-traffic-policing]], [[wiki/concepts/http-429-too-many-requests]], [[wiki/concepts/rate-limit-camadas-de-posicionamento]], [[wiki/concepts/rate-limit-estado-compartilhado]], [[wiki/concepts/api-gateway]], [[wiki/concepts/waf]], [[wiki/concepts/cdn]], [[wiki/concepts/load-balancer]], [[wiki/concepts/ddos-syn-flood]], [[wiki/concepts/api-economy]], [[wiki/concepts/retry-backoff]], [[wiki/concepts/single-point-of-failure]].

## Open questions

- Requisição que falha (4xx/5xx) conta para o limite? Contabilizar antes ou depois do 200? O autor levanta, não responde: [[wiki/questions/rate-limit-contabilizar-requisicao-falha-e-chave-de-identificacao]].
- Algoritmos fixed/sliding window: adiados para parte 2 (cobertos no skill, `rate-limiting.md`).
- Atomicidade do contador no Redis e falha do store (fail-open vs. fail-closed): não tratadas no vídeo; no skill há Lua script atômico.

## Raw quotes

> "em vez de simplesmente devolver se uma requisição pode ou não ser atendida podemos controlar a taxa com que o recurso é consumido"
> "rate limit aparentemente simples pode se transformar num problema clássico de estado compartilhado e sistemas distribuídos"
> "esse mecanismo precisa ser tão escalável e resiliente quanto a própria aplicação"

## Notas de ingest

Transcrição já em português (sem tradução). "Kong ou ox" ambíguo (provável Kong/Envoy/APISIX): não virou entidade. Cloud equivalentes (Memorystore, Azure Cache for Redis, DynamoDB) e nomes de ferramentas são relato do áudio, `[external, não verificado]` além de Spring Cloud Gateway/Bucket4j/NestJS, que correspondem ao ecossistema real.
