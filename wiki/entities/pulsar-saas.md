---
type: entity
title: "Pulsar (SaaS)"
aliases: ["pulsar", "pulsar saas"]
date_created: 2026-07-31
date_updated: 2026-07-31
source_count: 1
tags: [saas, produto, appsec, pentest, desafio-de-estudos, instagram]
skill: tech-mentor-security
status: stub
---

# Pulsar (SaaS)

SaaS pessoal em construção, documentado em série de vlog, cujo propósito declarado é sustentar um desafio de estudos gratuito de 100 dias divulgado no Instagram (início previsto: dia 22 de um mês não especificado no vídeo). A autora usa o próprio Pulsar como caso real para aprender infraestrutura, DevOps e segurança de aplicação — não é um projeto de brinquedo: é descrito como "produtivo, com usuários reais".

## Autenticação

Login via Google Auth, com gestão de sessão para evitar bater repetidamente nos endpoints de autenticação. Um dos testes de segurança realizados verificou explicitamente se o logout de fato invalida o acesso a rotas autenticadas.

## Autopentest assistido por Claude Code

A autora, sem background em segurança, conduziu um autopentest do Pulsar usando o Claude Code como guia — não como executor autônomo — cobrindo autenticação/sessão, [[wiki/concepts/idor|IDOR]], CSRF, [[wiki/concepts/xss|XSS]]/[[wiki/concepts/sql-injection|SQL Injection]], abuso de regra de negócio, vazamento de informação em mensagens de erro, [[wiki/concepts/rate-limiting|rate limiting]], dependências vulneráveis e segredos vazados em histórico de git. Detalhes completos em [[wiki/sources/testes-de-seguranca-pentest-com-claude-code-pulsar-saas]].

## Autoria (não confirmada)

O vídeo-fonte não identifica a autora nominalmente. Há forte coincidência de padrão com [[wiki/entities/eduarda-rocket-city]] — engenheira já documentada na wiki como criadora de conteúdo técnico, e o vídeo menciona ter feito um curso de segurança da Rocket City via parceria. Tratado como inferência razoável, não como fato confirmado.

## Key Sources

- [[wiki/sources/testes-de-seguranca-pentest-com-claude-code-pulsar-saas]]
