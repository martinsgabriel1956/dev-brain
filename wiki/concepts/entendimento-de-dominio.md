---
type: concept
title: "Entendimento de Domínio"
aliases: ["domain understanding", "contexto de negócio", "entender o domínio"]
date_created: 2026-06-20
date_updated: 2026-07-03
source_count: 2
tags: [dominio, negocio, arquitetura, onboarding, carreira]
skill: tech-mentor-leadership
status: stable
---

# Entendimento de Domínio

Conhecimento do propósito e contexto de negócio do software que está sendo construído. Distinto do entendimento técnico — é saber *para quê* e *para quem* o sistema existe, não *como* ele funciona internamente.

## Por que importa

Decisões arquiteturais sempre refletem restrições e prioridades do domínio. Sem entender o domínio, você:
- Não consegue avaliar se uma decisão técnica faz sentido
- Não entende por que certas features existem ou têm a forma que têm
- Não consegue contribuir com sugestões relevantes
- Faz re-trabalho ao resolver o problema técnico errado

## Como desenvolver

- Entenda **quem são os usuários** e como eles usam o sistema
- Aprenda o **"por quê"** de cada task atribuída — contexto de negócio e decisão técnica
- Explore o backlog e roadmap para ver o que está sendo construído e por quê
- Converse com stakeholders quando possível

## Exemplos

- Construindo para designers → aprenda como designers trabalham, quais ferramentas usam, quais fricções têm
- Plataforma de trading → estude fundamentos de mercados financeiros
- Sistema de saúde → entenda fluxos clínicos, regulações, privacidade de dados

## Relação com [[wiki/concepts/onboarding-de-codebase]]

É a etapa mais frequentemente ignorada no onboarding técnico. Um dev que entende o domínio aprende a codebase com mais profundidade porque cada linha de código passa a ter contexto.

## Modelagem de domínio como tradução

[[wiki/sources/engenheiro-vs-programador-mercado-ia|Outra fonte]] enquadra essa mesma ideia como "design de software e modelagem de domínio": o objetivo não é decorar padrões de design (Singleton, Factory, Observer) isoladamente, mas saber modelar o domínio de negócio de forma que o código conte a história do problema. Cita *Domain-Driven Design* (Eric Evans) e *A Philosophy of Software Design* (Ousterhout) como referências. Ver [[wiki/concepts/arquitetura-de-software]].

## Key sources

- [[wiki/sources/como-aprender-novas-codebases]]
- [[wiki/sources/engenheiro-vs-programador-mercado-ia]]
