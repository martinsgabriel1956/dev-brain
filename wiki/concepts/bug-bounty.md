---
type: concept
title: "Bug Bounty"
aliases: ["bug bounty", "programa de recompensa por falhas", "vdp"]
date_created: 2026-08-19
date_updated: 2026-08-19
source_count: 1
tags: [bug-bounty, pentest, appsec, red-team, xss]
skill: tech-mentor-security
status: stub
---

# Bug Bounty

Programa no qual uma empresa oferece recompensa financeira a quem encontrar e reportar responsavelmente uma vulnerabilidade de segurança em seus sistemas, dentro de um escopo e regras definidos publicamente. É a versão formalizada e legal de procurar falhas — só é permitido testar sistemas explicitamente incluídos no programa.

## Relação com Pentest e Treino

Bug bounty é uma aplicação prática das mesmas técnicas de [[wiki/concepts/attack-surface|reconhecimento e exploração]] treinadas em laboratórios controlados como o [[wiki/concepts/dvwa]] — a diferença é o alvo: um laboratório é deliberadamente vulnerável e isolado; um programa de bug bounty é um sistema real de produção, com escopo e regras que devem ser respeitados sob risco legal.

Classes de vulnerabilidade comuns e "simples" — como [[wiki/concepts/xss]] e [[wiki/concepts/sql-injection]] — continuam presentes em aplicações reais de grande escala, o que torna bug bounty acessível mesmo para quem está começando, desde que a base técnica (como identificar e explorar cada classe) já tenha sido praticada.

## Relação com Outros Conceitos

- [[wiki/concepts/dvwa]] — ambiente de treino recomendado antes de participar de programas reais
- [[wiki/concepts/xss]] / [[wiki/concepts/sql-injection]] — classes de falha citadas como exemplo de achado comum em bug bounty

## Key Sources

- [[wiki/sources/xss-cross-site-scripting-luiz-viana]] — bug bounty citado como motivação prática para aprender XSS, com ressalva de que testes só valem em sistemas com permissão explícita
