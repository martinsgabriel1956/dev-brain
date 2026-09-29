---
type: concept
title: "Aprender com Foco no Problema"
aliases: ["foco no problema não no como", "caçar problemas", "aprender pelo problema vs pelo como fazer"]
date_created: 2026-09-28
date_updated: 2026-09-28
source_count: 1
tags: [aprendizado, iniciante, requisitos, metodologia-de-estudo, carreira]
skill: tech-mentor-leadership
status: stub
---

# Aprender com Foco no Problema

## TL;DR

Segundo [[wiki/entities/andre-casciotti]], todo trabalho de dev nasce de um **problema**, não de uma instrução de "como fazer" ("conecta no banco e traz a lista de clientes" nunca é a tarefa real — a tarefa real é "preciso exibir X na tela" ou "preciso filtrar Y"). Aprender programação focado em qual método/framework/IDE usar treina o "como" mas deixa o iniciante sem saber "por onde começar" diante de um problema real. A alternativa: treinar deliberadamente a tradução problema → solução.

## O exercício recomendado

Criar um sistema do zero **usando um modelo real existente** (um SaaS, um marketplace, um software que você já usa) em vez de tentar tirar requisitos da própria cabeça — o que é difícil sem repertório ([[wiki/concepts/repertorio]]) de por que cada funcionalidade existe. A partir do modelo, "caçar problemas" para implementar — não bugs, mas cenários realistas:

- Autenticação **feita do jeito certo** (não senha em texto puro; pensar em como funciona login via Google, um IdP real — Azure AD, LDAP, OpenID, Auth0).
- Um filtro de consulta que força aprender sobre **índice de banco** (simples e composto) — sem o filtro, a necessidade do índice nunca apareceria.
- Um menu baseado em **permissão do usuário** — decidir entre carregar permissões num token JWT, consultar toda vez, ou usar sessão de servidor.
- Um **SLA de resposta** artificial (ex.: nenhuma requisição pode passar de 1 segundo) que força decidir sobre cache, número de consultas, N+1.

Essa é a mesma lógica de [[wiki/concepts/requisitos-funcionais-e-nao-funcionais|análise de requisitos]] praticada de forma autodirigida: transformar uma necessidade vaga ("preciso de um filtro") num requisito concreto e depois numa decisão técnica.

## Melhoria contínua como parte do método

Implementar cada coisa "meia boca" primeiro (ex.: autenticação simples) e melhorar depois, uma de cada vez, em vez de tentar fazer tudo perfeito de uma vez — o mesmo raciocínio de [[wiki/concepts/refatoracao]] aplicado ao processo de aprendizado, não só ao código já em produção.

## Relação com outros conceitos

- [[wiki/concepts/resolver-problemas-como-habilidade-central]] — a mesma tese (dev resolve problema, não escreve código bonito) aplicada ao trabalho profissional em vez de ao estudo
- [[wiki/concepts/requisitos-funcionais-e-nao-funcionais]] — "caçar problema" é, na prática, levantamento de requisitos autodirigido
- [[wiki/concepts/repertorio]] — usar um modelo real existente compensa a falta de repertório para gerar requisitos do zero

## Key Sources

- [[wiki/sources/o-que-estudar-guia-para-iniciantes-andre-casciotti]]
