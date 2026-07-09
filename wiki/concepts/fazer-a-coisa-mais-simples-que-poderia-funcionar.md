---
type: concept
title: "Faça a Coisa Mais Simples Que Poderia Funcionar"
aliases: ["do the simplest thing that could possibly work", "simplest thing that could possibly work", "solução mais simples que resolve"]
date_created: 2026-07-09
date_updated: 2026-07-09
source_count: 1
tags: [extreme-programming, kiss, simplicidade, principios, craftsmanship]
skill: tech-mentor-leadership
status: draft
---

## Definição

Princípio da Extreme Programming (XP): diante de um problema, escolha a solução mais simples que de fato o resolve — não a mais elegante, não a mais "à prova de futuro", a mais simples que funciona agora. A ideia é construir algo simples primeiro e refatorar para algo melhor depois, se e quando necessário.

## Por Que Existe

Muitos desenvolvedores tentam construir a solução "perfeita" desde a primeira tentativa — antecipando casos de uso, generalizando cedo, escolhendo a abstração mais "correta" antes de ter evidência de que ela é necessária. Isso tende a supercomplicar a solução e atrasar a entrega de algo que já resolveria o problema.

Com este princípio, chega-se a código funcional mais rápido. Se depois for preciso mudar, alterar uma solução simples costuma ser mais barato do que desfazer um design complexo que nasceu errado — porque a complexidade prematura não foi validada contra um caso de uso real.

## Diferença Para KISS

Sobrepõe-se a [[wiki/concepts/kiss]], mas não é idêntico:

- **KISS** é uma disciplina geral de não aumentar complexidade além do necessário, aplicável a qualquer decisão de design, em qualquer momento do projeto.
- **"Do the simplest thing that could possibly work"** é mais específico: é uma heurística de *primeira tentativa* — o critério de parada ao escrever a primeira versão de uma solução, vindo do ciclo de XP (fazer funcionar → refatorar → repetir).

Na prática, os dois convergem: ambos resistem à tentação de resolver o problema que você *acha* que vai ter, em vez do problema que você *tem*.

## Relação com Outros Princípios

- [[wiki/concepts/yagni]] — irmão direto, também com origem em XP/Kent Beck: YAGNI ataca a construção antecipada de funcionalidade; este princípio ataca a complexidade antecipada da solução para o problema atual.
- [[wiki/concepts/otimizacao-prematura]] — mesma lógica aplicada a performance em vez de design: resolver o problema real primeiro, otimizar/generalizar depois, com evidência.
- [[wiki/concepts/over-engineering]] — este princípio é o antídoto processual: perguntar "qual é a coisa mais simples que resolve isso agora?" antes de desenhar qualquer abstração.

## Key Sources

- [[wiki/sources/5-principios-que-mudaram-como-programador]]
