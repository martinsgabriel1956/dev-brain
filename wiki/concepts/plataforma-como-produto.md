---
type: concept
title: "Plataforma como Produto (Platform as a Product)"
aliases: ["platform as a product", "plataforma como produto interno", "product over project", "products over projects"]
date_created: 2026-08-12
date_updated: 2026-08-12
source_count: 1
tags: [platform-engineering, produto-interno, product-over-project, funding, devops, adocao]
skill: tech-mentor-infra
status: draft
---

# Plataforma como Produto

## TL;DR

A postura que torna uma [[plataforma-digital]] efetiva: tratá-la como **produto interno** com usuários reais (os times de produto), e não como infraestrutura compartilhada imposta. Tese de [[wiki/entities/evan-bottcher]] em [[wiki/sources/talk-about-platforms-evan-bottcher]]: só mandato falha porque infra compartilhada obrigatória é um **monopólio** — pensamento de produto de verdade exige **competição viável** (o time poderia construir a própria).

## Teste central

> É mais fácil consumir a capacidade da plataforma do que construir e manter a sua própria coisa?

Se a resposta for não, a plataforma não é um produto — é um imposto.

## Características de uma plataforma atraente

- **self-service** na esmagadora maioria dos casos de uso;
- **componível** — serviços discretos usáveis de forma independente;
- formas de trabalhar **não engessadas**;
- onboarding **rápido e barato** (quick start, docs, exemplos);
- **comunidade interna** rica de usuários;
- **segura e em conformidade por padrão**;
- **atualizada**.

## Pré-requisitos organizacionais

1. funding de **produto**, não de **projeto** ("products over projects") — time estável e de vida longa;
2. a plataforma constrói **e opera** ([[you-build-it-you-run-it]]);
3. transferir a operação da aplicação para os times de aplicação;
4. trocar consistência estrita de implementação por **autonomia**.

## Armadilhas

- **incompleta**: só APIs/infra não bastam — precisa consultoria, treinamento, evangelização, change management;
- **requisitos desconhecidos**: comece pequeno, "colha" soluções já provadas pelos times, teste antes de escalar;
- **rótulo superficial**: re-etiquetar infra travada como "plataforma" não muda nada.

## Relacionados

- [[plataforma-digital]] — a definição
- [[sensible-defaults-paved-road]] — o mecanismo de adoção
- [[you-build-it-you-run-it]] — a divisão de responsabilidade

## Key sources

- [[wiki/sources/talk-about-platforms-evan-bottcher]] — Evan Bottcher, *What I Talk About When I Talk About Platforms* (2018)
