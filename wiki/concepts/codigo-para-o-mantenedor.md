---
type: concept
title: "Escrever Código Para o Mantenedor"
aliases: ["code for the maintainer", "write code for the maintainer", "código pensando em quem vai manter"]
date_created: 2026-07-09
date_updated: 2026-07-09
source_count: 1
tags: [craftsmanship, legibilidade, manutenibilidade, clean-code, ia]
skill: tech-mentor-leadership
status: draft
---

## Definição

Princípio segundo o qual código deve ser escrito priorizando a compreensão de quem vai mantê-lo no futuro — que pode ser outro desenvolvedor ou o próprio autor meses depois — em vez de otimizar apenas para "fazer funcionar agora".

Duas implementações podem ser funcionalmente idênticas, mas divergem drasticamente em quão fácil é entendê-las, alterá-las e depurá-las sem o contexto que o autor original tinha na cabeça no momento de escrevê-las.

## Por Que Importa

O código escrito hoje será lido muitas vezes mais do que será escrito. Se o único critério de "pronto" é "compila e passa no teste feliz", a dívida de compreensão fica invisível até alguém (frequentemente o próprio autor) precisar voltar àquele trecho sem lembrar o raciocínio original.

## Relevância na Era de Código Gerado por IA

O princípio ganha peso extra quando o código não é mais só escrito manualmente: agentes de IA geram trechos inteiros a partir de prompts, e a tentação é aceitar o output se ele "funciona" sem revisar sua clareza. A recomendação prática levantada é explícita: **sempre revisar se o código gerado é fácil de entender e manter antes de comitar** — o mesmo padrão que se aplicaria a código escrito à mão.

Isso conecta com o problema de [[wiki/concepts/abstraction-bloat]] — um agente pode gerar uma solução funcional, mas verbosa ou mal nomeada, que passa despercebida se o dev só valida comportamento e não legibilidade.

## Relação com Outros Princípios

- [[wiki/concepts/boy-scout-rule]] — ambos tratam a legibilidade como responsabilidade contínua, não só do autor original.
- [[wiki/concepts/code-review]] — revisão de código é o principal ponto de controle para aplicar este princípio, seja código humano ou gerado por IA.
- [[wiki/concepts/definicao-de-pronto]] — "pronto" inclui legibilidade, não só comportamento correto.

## Key Sources

- [[wiki/sources/5-principios-que-mudaram-como-programador]]
