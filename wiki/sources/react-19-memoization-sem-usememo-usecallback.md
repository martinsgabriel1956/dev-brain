---
type: source
title: "React 19 Memoization: Chega o Fim do useMemo e useCallback?"
aliases: ["react 19 memoization", "no more usememo usecallback"]
date_created: 2026-07-04
date_updated: 2026-07-04
source_file: /home/nemomartins/Documentos/dev-brain/raw/react-19-memoization-sem-usememo-usecallback.md
source_url: "https://medium.com/front-end-world/react-19-memoization-no-more-usememo-usecallback-3a09a986f9c7"
author: "Komal Raut"
date_published: 2026-02-25
date_ingested: 2026-07-04
source_count: 0
tags: [react, frontend, hooks, performance, memoização, react-compiler]
skill: tech-mentor-frontend
status: stable
---

# React 19 Memoization: Chega o Fim do useMemo e useCallback?

## TL;DR

Artigo de blog (Medium, fev/2025) explicando que o React Compiler do React 19 automatiza a memoização que antes exigia `useMemo`/`useCallback` manuais, analisando o código e memoizando valores/funções por baixo dos panos. Argumenta que os hooks manuais continuam necessários apenas em casos de borda (bibliotecas de terceiros dependentes de referência estável, cálculos extremos que escapam à análise do compiler, ou integração com `React.memo` em cenários específicos).

---

## Claims Principais

| Claim | Evidência | Confiança |
|---|---|---|
| `useMemo`/`useCallback` existiam para evitar recomputação/recriação a cada render | Exemplo antes/depois no artigo | Alta |
| Uso excessivo de `useMemo`/`useCallback` piora legibilidade e manutenibilidade | Afirmação do autor, sem benchmark citado | Média |
| React Compiler detecta re-renders desnecessários e memoiza automaticamente | Descrição do funcionamento, alinhada com [[react-compiler]] e a doc oficial do React | Alta |
| Ainda vale `useMemo` para libs de terceiros que dependem de valor memoizado, ou cálculos que o compiler não otimiza | Ressalva do próprio autor | Média — não lista exemplos concretos de "cálculos que o compiler não captura" |
| Ainda vale `useCallback` ao passar função para filho com `React.memo` que depende de igualdade referencial estrita | Ressalva do autor | Média — o React Compiler memoiza automaticamente também esse caso na maioria das vezes; a ressalva é mais um caso residual do que a regra |

## Conceitos Abordados

- [[wiki/concepts/react-compiler]] (criado nesta ingestão)
- [[wiki/concepts/useMemo]]
- [[wiki/concepts/useCallback]]
- [[wiki/concepts/concurrent-mode]]

## Entidades Abordadas

- [[wiki/entities/react]]

## Observações / Contradições

O artigo é superficial em relação ao que já está documentado em [[wiki/concepts/react-performance]]-adjacent (`useMemo`/`useCallback`) e em [[wiki/concepts/concurrent-mode]]: não cita `babel-plugin-react-compiler`, não menciona a limitação de que o compiler exige aderência às Rules of Hooks, e não diferencia claramente "código anotado" vs. "code automático" (compilationMode). Nenhuma contradição de fato com a wiki existente — é um resumo de nível introdutório do mesmo tema já coberto com mais profundidade técnica em [[wiki/sources/react-tudo-que-voce-precisa-saber]].

## Perguntas Abertas

- O artigo não detalha *quais* cálculos "extremamente custosos" escapariam à otimização do compiler — não há exemplo concreto citado na fonte.
- Não há menção a benchmarks reais comparando código memoizado manualmente vs. compilado — a afirmação de ganho de performance é qualitativa.

## Raw Quotes

> "Memoization is an optimization technique that stores the result of expensive function calls and returns the cached result when the same inputs occur again."

> "The React Compiler analyzes your components and automatically optimizes them by: Detecting unnecessary re-renders and skipping them. Memoizing expensive calculations behind the scenes. Ensuring stable function references to prevent prop changes from triggering re-renders."
