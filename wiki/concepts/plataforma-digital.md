---
type: concept
title: "Plataforma Digital (Compelling Internal Product)"
aliases: ["digital platform", "plataforma como produto interno", "compelling internal product", "delivery infrastructure platform"]
date_created: 2026-08-12
date_updated: 2026-08-12
source_count: 1
tags: [platform-engineering, plataforma-digital, self-service, produto-interno, devops, thoughtworks]
skill: tech-mentor-infra
status: draft
---

# Plataforma Digital

## TL;DR

Definição canônica de [[wiki/entities/evan-bottcher]] em [[wiki/sources/talk-about-platforms-evan-bottcher]]: uma plataforma digital é **"uma fundação de APIs, ferramentas, serviços, conhecimento e suporte self-service, organizados como um produto interno atraente"** (*a compelling internal product*). A palavra que carrega o significado é **atraente** — a plataforma existe para ser *escolhida*, não imposta.

## O que a definição exige

- **self-service** — provisionamento, configuração e operação sem depender de outro time (o antídoto ao [[backlog-coupling]]);
- **fundação composta** — não é uma coisa só, mas APIs + ferramentas + serviços + conhecimento + suporte;
- **produto interno** — tem usuários (os times de produto), roadmap, onboarding, documentação e evangelização;
- **atraente** — tem que ser mais fácil consumir a capacidade da plataforma do que construir e manter a sua própria.

## Escopo é maior que software

Bottcher enfatiza que a plataforma inclui **documentação, consultoria, suporte, evangelização, templates e guidelines** — não apenas software e APIs. Uma plataforma "incompleta" (só infra, sem consultoria/change management) é uma das armadilhas do artigo.

## Foco: infraestrutura de entrega

A [[wiki/entities/thoughtworks]] distingue várias acepções de "plataforma" (infra de entrega, APIs de negócio, dados self-service, etc.). O artigo trata especificamente da **plataforma de infraestrutura de entrega** — hospedagem em cloud, ferramental de DevOps, deploy.

## Evolução do vocabulário

A definição é de 2018. O termo evoluiu para **Internal Developer Platform (IDP)** com **golden paths** e portais como Backstage — mesma ideia, vocabulário mais maduro `[skill: tech-mentor-infra]` (`references/platform-engineering.md`). Ver [[plataforma-como-produto]] e [[sensible-defaults-paved-road]].

## Relacionados

- [[backlog-coupling]] — o problema que a plataforma resolve
- [[plataforma-como-produto]] — a postura de produto interno
- [[sensible-defaults-paved-road]] — o mecanismo de adoção sem mandato
- [[you-build-it-you-run-it]] — a divisão de responsabilidade
- [[contexto-organizacional-para-arquitetura]] — por que é um problema organizacional

## Key sources

- [[wiki/sources/talk-about-platforms-evan-bottcher]] — Evan Bottcher, *What I Talk About When I Talk About Platforms* (2018)
