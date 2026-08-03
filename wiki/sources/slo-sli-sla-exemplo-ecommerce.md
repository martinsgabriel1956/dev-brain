---
type: source
title: "SLO, SLI e SLA — Exemplo com E-commerce"
aliases: ["slo sli sla exemplo", "aula slo sla sli ecommerce"]
date_created: 2026-08-03
date_updated: 2026-08-03
source_count: 0
tags: [sre, sli, slo, sla, confiabilidade, contrato]
skill: tech-mentor-infra
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/slo-sli-sla-exemplo-ecommerce.md
source_url: ""
author: ""
date_published: 2026-08-03
date_ingested: 2026-08-03
---

# SLO, SLI e SLA — Exemplo com E-commerce

## TL;DR

Aula introdutória que distingue SLO, SLI e SLA usando um exemplo narrativo de e-commerce: o mesmo número de disponibilidade (ex.: 99,9%) é um SLO quando o acordo é interno entre times/áreas da mesma empresa, e vira um SLA quando o acordo é um contrato entre duas empresas distintas com consequência formal. O SLI é a métrica bruta (ex.: proporção de HTTP 200) que alimenta o SLO.

## Key Claims

**Claim:** A diferença entre SLO e SLA não está na métrica ou no número, mas em quem são as partes do acordo — mesma empresa (SLO) vs. empresas distintas com contrato (SLA).
**Evidence:** Exemplo do time de banco de dados que promete "99,9% disponível para a aplicação" dentro da mesma empresa — isso é um SLO, e se violado gera só "problemas internos". Quando esse mesmo banco de dados é operado por uma empresa B contratada pela empresa A, a mesma promessa de 99,9% vira um SLA, com consequência contratual (multa).
**Confidence:** alta — consistente com [[wiki/sources/sre-sli-slo-sla]] e com a skill `tech-mentor-infra` (`references/reliability-slo.md`), que também define SLA como "contrato com o cliente".

**Claim:** Usuário final tipicamente não tem SLA com o e-commerce onde compra — a única consequência de indisponibilidade é ele comprar em outro lugar.
**Evidence:** Exemplo do usuário "Douglas" que tenta comprar e a loja está indisponível: ele não tem acordo formal, apenas deixa de comprar ali. Já um lojista que contrata a plataforma para vender seus produtos e recebe uma garantia formal de "99% do tempo disponível" tem, sim, um SLA — porque há uma promessa explícita com consequência para quem vende.
**Confidence:** alta — distinção didática, não contraditória com fontes anteriores.

**Claim:** SLI é a métrica concreta (ex.: proporção de respostas HTTP 200), SLO é a porcentagem/meta sobre essa métrica, SLA é a camada contratual sobre a mesma promessa.
**Evidence:** "SLI é a métrica, o SLO é a porcentagem, o SLA é a questão contratual." Exemplo: 98% dos requests HTTP retornando 200 vira o SLI; o compromisso de manter isso é o SLO; se formalizado em contrato externo, vira SLA.
**Confidence:** alta — mesma definição de [[wiki/concepts/sli]], [[wiki/concepts/slo]], [[wiki/concepts/sla]] já registradas na wiki.

**Claim:** Operacionalizar um SLO requer observabilidade (métrica coletada) e alarmes configurados sobre o threshold acordado.
**Evidence:** "Você tem que usar uma ferramenta de observabilidade e, dado essa métrica, você tem que ter alarmes para o seu SLO."
**Confidence:** média — mencionado de forma genérica, sem detalhamento técnico (ex.: burn rate, Prometheus) como em [[wiki/sources/sre-sli-slo-sla]].

## Concepts & Entities Touched

[[wiki/concepts/sli]] · [[wiki/concepts/slo]] · [[wiki/concepts/sla]] · [[wiki/concepts/sre]] · [[wiki/concepts/observabilidade]]

## Open Questions

- A fonte não menciona Error Budget — fica implícito que "violar o SLO" gera só "problema interno", sem framework de decisão explícito (comparar com o tratamento mais completo em [[wiki/sources/sre-sli-slo-sla]]).
- Não há exemplo de como o SLA se torna tecnicamente mensurável quando o "banco de dados como serviço" está envolvido (ex.: RDS, serviços gerenciados) — o exemplo permanece hipotético/didático.

## Quotes

> "SLI é a métrica, o SLO é a porcentagem, o SLA é a questão contratual."

> "Uma área não vai pagar multa para outra, certo?"

> "Isso vai gerar problemas internos, mas só isso."
