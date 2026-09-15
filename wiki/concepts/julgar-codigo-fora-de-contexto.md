---
type: concept
title: "Julgar Código Fora de Contexto"
aliases: ["armadilha do código legado", "comparar código legado com greenfield", "código fora de contexto"]
date_created: 2026-09-15
date_updated: 2026-09-15
source_count: 1
tags: [code-review, contexto-organizacional, tech-debt, legado, mentoria]
skill: tech-mentor-leadership
status: draft
---

# Julgar Código Fora de Contexto

**TL;DR:** Avaliar um trecho de código (geralmente legado) isoladamente, comparando-o com o código que se escreveria "começando o projeto hoje do zero", é uma armadilha comum — mesmo entre desenvolvedores experientes. O código real carrega restrições que o código imaginado do zero não tem: dependências externas, decisões anteriores, contratos de API que não podem ser quebrados, limitação de infraestrutura.

## O Mecanismo da Armadilha

Um profissional que "cai de paraquedas" num projeto (ex.: entra numa equipe de sustentação) enxerga apenas o código — não o histórico de restrições que produziu aquele código. Refatorar para o "ideal" muitas vezes exigiria reescrever o sistema inteiro, o que é impraticável num legado sem testes. O que sobra é entregar "o que o sistema permite", não o que o dev sabe fazer.

A comparação injusta é implícita: código legado vs. código greenfield imaginário, sem considerar que o segundo nunca vai encontrar as mesmas restrições reais de produção, prazo e dependência que o primeiro encontrou.

## Por Que Isso Importa em Code Review

[[wiki/concepts/code-review]] é o lugar onde essa armadilha se manifesta com mais frequência — revisar ou criticar código de um sistema legado sem contexto suficiente sobre por que aquelas decisões foram tomadas leva a comentários que confundem "código difícil de mudar por restrição real" com "código malfeito por incompetência".

## Relação com Contexto Organizacional

Esta armadilha é o espelho, no nível de julgamento individual de um trecho de código, do argumento mais amplo de [[wiki/concepts/contexto-organizacional-para-arquitetura]]: assim como uma decisão arquitetural depende de restrições reais da organização (maturidade de plataforma, esteira de CI/CD), um trecho de código específico depende de restrições reais do sistema em que foi escrito (legado, dependência externa, contrato de API imutável). Ambos os argumentos rejeitam avaliar código/arquitetura "em abstrato", sem considerar as condições reais de produção.

## Relacionado

[[wiki/concepts/contexto-organizacional-para-arquitetura]] · [[wiki/concepts/code-review]] · [[wiki/concepts/fatores-nao-tecnicos-qualidade-de-codigo]] · [[wiki/concepts/boy-scout-rule]]

## Key Sources

- [[wiki/sources/fatores-nao-tecnicos-codigo-ruim-bons-desenvolvedores-bernardo-lobato]] — anedota de origem: colegas criticando código de projeto legado escrito por profissionais excelentes
