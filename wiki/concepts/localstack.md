---
type: concept
title: "LocalStack"
aliases: ["local stack", "aws local dev", "aws local emulation"]
date_created: 2026-08-18
date_updated: 2026-08-18
source_count: 1
tags: [aws, localstack, desenvolvimento-local, dynamodb, lambda, cloud, testing]
skill: tech-mentor-backend
status: stub
---

# LocalStack

Ferramenta que emula serviços da AWS (DynamoDB, Lambda, S3, SQS, entre outros) **localmente**, permitindo desenvolver e testar contra uma "AWS local" sem custo de nuvem nem dependência de rede durante o desenvolvimento. Normalmente roda via Docker Compose, com um script de inicialização que provisiona os recursos simulados (tabelas, filas, funções) no boot do container.

## Caso real: setup do core de um sistema de mentoria em Go

[[wiki/entities/lucas-badico]] usa LocalStack para emular DynamoDB e Lambdas no desenvolvimento local do "core" do seu sistema de mentoria — o banco principal do sistema é PostgreSQL/PostGIS, com DynamoDB reservado para os casos de uso que já nascem pensados para AWS (ex.: acionar notificação uma hora antes de uma mentoria). Configurar essa stack local foi, segundo o autor, o primeiro vídeo do projeto e levou 6 horas. Ver [[wiki/sources/sistema-mentoria-golang-monolito-modular-live-lucas-badico]].

## Trade-off

Ganha-se velocidade de iteração e custo zero durante desenvolvimento; perde-se fidelidade total ao comportamento da AWS real (emulação nunca é 100% idêntica) — normalmente mitigado com testes de integração/staging contra a AWS real antes de produção.

## Key Sources

- [[wiki/sources/sistema-mentoria-golang-monolito-modular-live-lucas-badico]] — setup de LocalStack para DynamoDB e Lambdas no desenvolvimento do core em Go
