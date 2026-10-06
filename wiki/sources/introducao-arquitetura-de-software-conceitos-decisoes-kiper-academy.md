---
type: source
title: "Introdução à Arquitetura de Software: conceitos para decisões arquiteturais (Kiper Academy)"
aliases: ["intro arquitetura de software kiper", "stateful stateless sincrono acoplamento idempotencia cache"]
date_created: 2026-10-06
date_updated: 2026-10-06
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/introducao-arquitetura-de-software-conceitos-decisoes-kiper-academy.md
source_url: ""
author: "Kiper Academy (apresentador não identificado)"
date_published: ""
date_ingested: 2026-10-06
source_count: 0
tags: [arquitetura, system-design, stateless, stateful, sincrono-assincrono, acoplamento, idempotencia, cache, decisao-arquitetural, fowler]
skill: tech-mentor-system-design
status: draft
---

# Introdução à Arquitetura de Software: conceitos para decisões arquiteturais

Vídeo introdutório da [[wiki/entities/kiper-academy]] (série sobre arquitetura backend). Transcrição limpa em `raw/introducao-arquitetura-de-software-conceitos-decisoes-kiper-academy.md` (já em português; sem tradução).

## TL;DR

[[wiki/concepts/arquitetura-de-software]] é dividir o sistema, definir como as partes se comunicam e acomodar restrições (orçamento, prazo, equipe), qualidades esperadas e dados. Antes de decidir, é preciso fixar o **contexto/limite da aplicação** ([[wiki/concepts/application-boundary]]) com dev e negócio, e saber em qual **dimensão** a decisão está ([[wiki/concepts/dimensoes-de-decisao-arquitetural]]: estrutural ou design de código). Cinco conceitos viram perguntas-guia: [[wiki/concepts/stateless]] (a próxima requisição exige estado local?), [[wiki/concepts/comunicacao-sincrona]] vs. [[wiki/concepts/comunicacao-assincrona]] (o usuário precisa do resultado agora?), [[wiki/concepts/acoplamento]] (se B mudar, o que muda em A?), [[wiki/concepts/idempotencia]] (e se chegar duas vezes?) e [[wiki/concepts/cache]] (quanta desatualização aceito? ver [[wiki/concepts/tolerancia-a-desatualizacao-de-cache]]).

## Key claims

1. **Arquitetura = divisão + comunicação + restrições + qualidades + dados.** Evidência: lista de papéis no vídeo. Fowler: "entendimento compartilhado dos desenvolvedores especialistas" ([[wiki/entities/martin-fowler]]).
2. **Arquitetura influencia custo de mudança, custo de operação, desempenho, trabalho em equipe e complexidade** (e a influência é mútua com a organização das equipes). Evidência: bug como sintoma de causa espalhada em sistema complexo.
3. **"Aplicação" não tem definição única:** dev (repositório), cliente (interface), negócio (verba única). Evidência: exemplos Globoplay e [[wiki/entities/mercado-livre]]. Alinha com [[wiki/sources/application-boundary-martin-fowler]].
4. **Microsserviços em excesso viram caos:** a [[wiki/entities/uber]] (50+ microsserviços por equipe) introduziu o DOMA; a [[wiki/entities/shopify]] migrou de monolito para microsserviços. Evidência: artigos citados no vídeo (links não disponíveis; relato do áudio `[external, não verificado]`). Ver [[wiki/concepts/microsservicos]].
5. **Stateless não é regra, mas habilita escala horizontal e substituição de instâncias;** stateful faz sentido em multiplayer em tempo real. Evidência: analogia do crachá.
6. **Síncrono vs. assíncrono se decide pela pergunta "preciso do resultado agora?"** (ex.: verificação de CNH/CPF de até 30 min obriga assíncrono).
7. **Acoplamento legítimo (regra de negócio) deve se limitar ao contrato (status), nunca a detalhes internos.** Evidência: exemplo matrícula × cobrança e mudança do campo de endereço. Ver [[wiki/concepts/acoplamento-de-negocio-vs-detalhe-interno]].
8. **Chave de idempotência não é bala de prata:** concorrência e registro confiável do resultado continuam sendo problema da implementação.
9. **Cache troca frescor por latência/custo; a tolerância depende do domínio** (saldo bancário não tolera; post de blog tolera). Ver [[wiki/concepts/tolerancia-a-desatualizacao-de-cache]].

## Entidades

[[wiki/entities/kiper-academy]], [[wiki/entities/martin-fowler]], [[wiki/entities/uber]], [[wiki/entities/shopify]], [[wiki/entities/mercado-livre]].

## Conceitos

[[wiki/concepts/arquitetura-de-software]], [[wiki/concepts/application-boundary]], [[wiki/concepts/dimensoes-de-decisao-arquitetural]], [[wiki/concepts/stateless]], [[wiki/concepts/comunicacao-sincrona]], [[wiki/concepts/comunicacao-assincrona]], [[wiki/concepts/acoplamento]], [[wiki/concepts/acoplamento-desejavel-vs-indesejavel]], [[wiki/concepts/acoplamento-de-negocio-vs-detalhe-interno]], [[wiki/concepts/idempotencia]], [[wiki/concepts/cache]], [[wiki/concepts/tolerancia-a-desatualizacao-de-cache]], [[wiki/concepts/tradeoff-de-cache]], [[wiki/concepts/clean-architecture]], [[wiki/concepts/hexagonal-architecture]], [[wiki/concepts/ports-adapters]], [[wiki/concepts/adapter-pattern]], [[wiki/concepts/microsservicos]].

## Open questions

- Nome do apresentador e links dos artigos Shopify/Uber não constam na transcrição.
- O vídeo cita DOMA só de passagem; vale ingerir o artigo da Uber como fonte própria.
- "PICP" no ASR provavelmente é PicPay (incerto).

## Quotes

> "the shared understanding that the expert developers have of the system" (Martin Fowler, citado)

> Acoplamento não saudável: "um problema em uma parte da aplicação impede outra parte diferente de funcionar, mesmo sem nenhuma necessidade de negócio entre elas."
