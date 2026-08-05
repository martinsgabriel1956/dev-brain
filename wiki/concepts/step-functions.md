---
type: concept
title: "AWS Step Functions"
aliases: ["Step Functions"]
date_created: 2026-08-04
date_updated: 2026-08-04
source_count: 1
tags: ["aws", "step-functions", "orquestracao", "maquina-de-estados", "serverless", "infra"]
skill: tech-mentor-infra
status: stub
---

# AWS Step Functions

Serviço para coordenar workflows complexos na AWS através de um modelo mental de **máquina de estados**: uma porta de entrada dispara um passo (tipicamente um [[wiki/concepts/aws-lambda]]), e o resultado (sucesso/falha) determina o próximo passo do fluxo — falha pode ir para uma dead letter queue, sucesso segue para outro processamento até desaguar, por exemplo, num banco de dados ou no [[wiki/concepts/amazon-s3|S3]]. Preço é baseado em transições de estado.

## Prós

- Encoraja modularidade: quebra tarefas que tradicionalmente seriam monolíticas em pedaços menores e nomeados.
- Suporte de integração nativo para retries e filas entre os passos.

## Contras

- **Lock-in extremo.** É citado como o serviço com maior [[wiki/concepts/vendor-lock-in-cloud|vendor lock-in]] entre os cobertos no toolkit essencial da AWS.
- **Complexidade desnecessária na maioria dos casos.** A lógica interna de um servidor já costuma resolver fluxos parecidos a máquinas de estado de outras formas (eventos emitidos por um banco de dados, um message broker tipo Kafka) — Step Functions tende a fazer sentido só para arquiteturas orientadas a eventos com necessidade real de orquestração visual/declarativa entre múltiplos serviços gerenciados.

## Relação com outros conceitos

- [[wiki/concepts/aws-lambda]] — unidade de execução mais comum dentro de um step
- [[wiki/concepts/event-driven-architecture]]
- [[wiki/concepts/saga-pattern]] — outra forma de coordenar workflows multi-passo com compensação em caso de falha

## Key Sources

- [[wiki/sources/toolkit-aws-servicos-essenciais-para-aplicacoes-escalaveis]]
