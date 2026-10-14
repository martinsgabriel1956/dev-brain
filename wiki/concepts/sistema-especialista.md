---
type: concept
title: "Sistema Especialista"
aliases: ["expert system", "sistemas especialistas", "IA simbólica baseada em regras"]
date_created: 2026-10-14
date_updated: 2026-10-14
source_count: 1
tags: [ia, ia-simbolica, regras, historia]
skill: tech-mentor-ai
status: draft
---

## Definição

Sistema que representa o **conhecimento de um especialista** de um domínio numa **base de conhecimento** (regras e fatos) e usa um **motor de inferência** para aplicá-las automaticamente. Paradigma **declarativo**, tipicamente em Prolog ou Lisp, em contraste com o código imperativo (C, Java). Dominou as décadas de 70–80 como primeira aplicação comercial da [[wiki/concepts/inteligencia-artificial|IA]]. [[wiki/sources/10-conceitos-fundamentais-ia-moderna-bernardo-lobato]]

## Limite

Funciona enquanto o problema for pequeno o bastante para alguém escrever **todas as regras**. Em problemas de contexto mutável e sem especialista capaz de explicitar as regras (spam, rosto, direção autônoma) o custo de exceções explode, o que motivou o [[wiki/concepts/machine-learning]]. [[wiki/sources/10-conceitos-fundamentais-ia-moderna-bernardo-lobato]]

## Contraste com regras de negócio e com IA moderna

Exemplo do vídeo: `renda > X e score > Y → aprova` (simplificação grosseira). A inteligência vem de quem escreve as regras; no ML ela vem dos dados. Sistemas baseados em regras seguem relevantes onde se exige o mesmo resultado para a mesma entrada: ver [[wiki/concepts/determinismo-vs-probabilismo-em-ia]].

## Key Sources

- [[wiki/sources/10-conceitos-fundamentais-ia-moderna-bernardo-lobato]]
