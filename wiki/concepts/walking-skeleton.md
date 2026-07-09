---
type: concept
title: "Walking Skeleton (Esqueleto Ambulante)"
aliases: ["esqueleto ambulante", "steel thread", "tracer bullet"]
date_created: 2026-07-09
date_updated: 2026-07-09
source_count: 1
tags: [arquitetura, over-engineering, cicd, mvp, continuous-delivery]
skill: tech-mentor-leadership
status: stub
---

# Walking Skeleton (Esqueleto Ambulante)

Técnica de arranque de projeto: em vez de desenvolver todas as features até ter algo "completo" para só então colocar em produção, implementa-se primeiro uma fatia mínima do sistema que atravessa **toda a arquitetura fim-a-fim** — todos os componentes essenciais presentes, mas cada um na versão mais simples possível — e coloca-se essa fatia em produção imediatamente.

O objetivo não é entregar valor de negócio significativo nessa primeira versão. É validar a arquitetura e a infraestrutura de ponta a ponta cedo, quando o custo de descobrir um problema (de infra, de integração entre serviços, de deploy) ainda é baixo.

## Exemplo: LMAX

David Farley descreve o caso do LMAX, um sistema financeiro que precisava de alto desempenho e alta taxa de processamento. Em vez de já entrar com Kubernetes, microsserviços otimizados e a tecnologia de mensageria definitiva, o time:

1. Definiu o mínimo de arquitetura necessário — dois serviços que precisavam se comunicar via mensageria.
2. Implementou a comunicação com uma tecnologia deliberadamente **não** definitiva (XML sobre HTTP) — sabendo que não teria performance suficiente para produção real.
3. Colocou isso para rodar, escondendo a tecnologia de mensageria atrás de uma **abstração trocável**.
4. Mais tarde, com o esqueleto já validado e rodando, substituiu a mensageria por um protocolo binário de alta performance — sem precisar redesenhar a arquitetura, porque a peça provisória já estava isolada atrás de uma interface.

## Por que evita over-engineering

O padrão oposto — tentar resolver escala, performance e resiliência antes de qualquer coisa rodar — é uma das duas causas centrais de over-engineering descritas em [[over-engineering]]: a falta de confiança que leva a "já lidar com todos os requisitos não funcionais de cara". O walking skeleton inverte essa ordem: adia a otimização para quando ela é comprovadamente necessária, mas garante que a peça provisória está isolada atrás de uma abstração, para que trocá-la depois seja barato.

## Relação com prática já documentada nesta wiki

[[ci-cd]] já documentava, sem nome formal, a mesma técnica na seção "Deploy Imediato do Boilerplate": fazer deploy do Hello World gerado pelo framework antes de qualquer feature, para descobrir problemas de ambiente cedo e isolado. O walking skeleton é a versão mais geral desse princípio — não só o boilerplate, mas uma fatia mínima e funcional de toda a arquitetura.

## Conexões

- [[over-engineering]] — o walking skeleton é a técnica que evita a causa "falta de confiança / resolver tudo cedo demais"
- [[ci-cd]] — "Deploy Imediato do Boilerplate" é uma instância concreta já documentada deste padrão
- [[abstracao]] — abstrações trocáveis são o mecanismo que torna a peça provisória substituível sem redesenho
- [[dora-metrics]] — colocar algo em produção cedo é o que possibilita medir lead time e deployment frequency desde o início do projeto

## Key Sources

- [[wiki/sources/como-evitar-over-engineering-david-farley]]
