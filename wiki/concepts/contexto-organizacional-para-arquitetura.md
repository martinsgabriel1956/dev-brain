---
type: concept
title: "Contexto Organizacional para Arquitetura"
aliases: ["maturidade organizacional", "restricoes organizacionais de arquitetura", "arquitetura e processo da empresa"]
date_created: 2026-07-03
date_updated: 2026-08-12
source_count: 4
tags: [arquitetura, processo, carreira, ia]
skill: tech-mentor-leadership
status: stub
---

# Contexto Organizacional para Arquitetura

Uma decisão arquitetural não depende só da tecnologia "certa" em abstrato — depende de restrições reais da organização que a vai operar.

## Fatores práticos a considerar

- Como as áreas estão definidas e qual a responsabilidade de cada uma
- Como as áreas se comunicam entre si
- Com que velocidade a empresa consegue colocar uma solução em produção
- Se a plataforma de contêineres é madura o suficiente para justificar essa escolha
- Se existe esteira de CI/CD que suporte, por exemplo, arquitetura de microsserviços
- Se a empresa tem *know-how* interno e licenciamento comercial para as tecnologias sugeridas

## Por que isso importa mais na era da IA

A IA consegue gerar um desenho de arquitetura "ideal" em segundos, mas não sabe (a menos que seja informada) se a empresa tem a maturidade de processo para operar aquilo. Sugerir microsserviços para uma empresa sem esteira de CI/CD madura, por exemplo, troca um problema técnico por um problema operacional maior. Ver [[wiki/concepts/arquitetura-de-software]] e [[wiki/concepts/engenheiro-vs-programador]].

## Relação com outros conceitos

- [[wiki/concepts/arquitetura-de-software]] — este conceito é um dos fatores que compõem a decisão arquitetural completa
- [[wiki/concepts/vibe-coding]] — um prompt de vibe coding não tem, por padrão, visibilidade sobre esse contexto organizacional
- [[wiki/concepts/application-boundary]] — mesma tese vista de outro ângulo: 20 anos antes, Fowler já argumentava que a fronteira de uma *aplicação* (não só a arquitetura escolhida para operá-la) é definida por relações humanas e política organizacional, não por critério técnico objetivo

## Precursor de 2003: Fronteiras Como Construção Social

[[wiki/sources/application-boundary-martin-fowler]] antecipa o argumento central desta página aplicado a uma pergunta mais básica — não "qual arquitetura operar", mas "onde termina uma aplicação". Fowler observa que devs, negócio e financiadores enxergam "uma unidade única" de formas diferentes (código, funcionalidade, orçamento), e que a fronteira real é traçada por política e relações humanas, não por um critério técnico que resolveria isso sozinho. Ver [[wiki/concepts/application-boundary]].

## A Lei de Conway como Mecanismo, Não Só Metáfora

[[wiki/sources/microsservicos-martin-fowler-james-lewis]] cita Melvin Conway (1968) diretamente: "qualquer organização que projeta um sistema (definido de forma ampla) produzirá um design cuja estrutura é uma cópia da estrutura de comunicação da organização". O artigo usa isso para explicar por que decompor um sistema por camada técnica (time de UI, time de lógica, time de banco) é um anti-padrão: qualquer mudança simples vira um projeto interequipes com aprovação orçamentária, e a lógica de negócio acaba forçada para dentro de qualquer camada com acesso mais fácil — "lógica em todo lugar". A saída proposta é decompor por [[wiki/concepts/microsservicos|capacidade de negócio]], com times multifuncionais cross-funcionais (UX, banco, gestão de projeto) dentro do mesmo time, reforçando fronteiras de serviço com fronteiras de time — o mesmo raciocínio depois formalizado como *Inverse Conway Maneuver* em Team Topologies (ver [[wiki/sources/conways-law]]).

## Plataforma como problema organizacional (Bottcher)

[[wiki/sources/talk-about-platforms-evan-bottcher]] é outra aplicação direta desta ideia: infra organizada por **silo técnico** (DBA, redes, middleware) faz a Lei de Conway operar contra a entrega, gerando [[wiki/concepts/backlog-coupling|acoplamento de backlog]] (tarefas dependentes de outro time "10-12x mais lentas"). Bottcher enquadra plataforma como **problema organizacional antes de técnico** — a solução técnica (self-service) só funciona se acompanhada de mudança de estrutura e funding (ver [[wiki/concepts/plataforma-como-produto]]).

## Key Sources

- [[wiki/sources/vibe-coding-limites-maturidade-profissional]]
- [[wiki/sources/application-boundary-martin-fowler]] — fronteiras de aplicação como construção social, precursor de 2003 do mesmo argumento
- [[wiki/sources/microsservicos-martin-fowler-james-lewis]] — Lei de Conway como justificativa central para decompor por capacidade de negócio, não por camada técnica
- [[wiki/sources/talk-about-platforms-evan-bottcher]] — plataforma como problema organizacional; silos técnicos → acoplamento de backlog
