---
type: concept
title: "Arquitetura de Software"
aliases: ["software architecture", "decisao arquitetural"]
date_created: 2026-07-03
date_updated: 2026-07-03
source_count: 2
tags: [arquitetura, carreira, fundamentos, ia]
skill: tech-mentor-leadership
status: draft
---

# Arquitetura de Software

Como sistemas são estruturados e como certas decisões de estrutura escalam bem enquanto outras criam bola de neve de problemas. Não existe arquitetura boa para tudo — existe **arquitetura certa para o contexto certo** (restrições reais de tempo, escala, dinheiro, equipe).

## Por que é parte da fundação do engenheiro

Decisão arquitetural errada não se corrige com refatoração pontual — pode custar meses de trabalho jogados fora e gerar [[wiki/concepts/complexidade-acidental|dívida técnica]] que a equipe carrega por anos. Ver a distinção entre execução (programador) e decisão arquitetural (engenheiro) em [[wiki/concepts/engenheiro-vs-programador]].

## Decisão Arquitetural Não É Um Prompt

A IA ajuda um arquiteto a discutir alternativas, explicar trade-offs para públicos não técnicos e gerar rascunhos de solução — mas a decisão em si exige analisar o [[wiki/concepts/contexto-organizacional-para-arquitetura|contexto organizacional]] real:

- Como os dados são manipulados e onde estão armazenados
- Quais integrações entre sistemas existem
- Custo da arquitetura sugerida vs. disposição do cliente a pagar por ela
- Se a empresa tem *know-how* e licenciamento para as tecnologias sugeridas

Perguntar para uma IA "que arquitetura eu uso?" com um prompt enxuto não substitui essa análise. Ver [[wiki/sources/vibe-coding-limites-maturidade-profissional]].

## Leituras de referência citadas

- *Clean Architecture* (Robert Martin) — princípios
- *Fundamentals of Software Architecture* (Mark Richards & Neal Ford) — trade-offs práticos
- *Designing Data-Intensive Applications* (Martin Kleppmann) — sistemas distribuídos, o livro que "separa júnior de sênior" nesse tema
- *Domain-Driven Design* (Eric Evans) e *A Philosophy of Software Design* (John Ousterhout) — tradução de domínio de negócio em modelo de código, ver [[wiki/concepts/entendimento-de-dominio]]

Nenhum desses livros foi lido/ingerido diretamente ainda no wiki — são citações de segunda mão a partir da fonte abaixo.

## Key Sources

- [[wiki/sources/engenheiro-vs-programador-mercado-ia]]
- [[wiki/sources/vibe-coding-limites-maturidade-profissional]] — fatores de contexto de negócio e organizacional que uma decisão arquitetural precisa considerar
