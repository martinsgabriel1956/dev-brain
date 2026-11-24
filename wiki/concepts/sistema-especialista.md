---
type: concept
title: "Sistema Especialista"
aliases: ["expert system", "sistemas especialistas", "IA simbólica baseada em regras"]
date_created: 2026-10-14
date_updated: 2026-11-24
source_count: 2
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

## FrontPUSH: a 1ª geração como if/else

Em [[wiki/sources/frontpush-ia-o-que-voce-deve-saber-de-ia]], a primeira geração aparece como "o que a gente faz em if else" ("SE temperatura > 30 ENTÃO ligar ventilador"). O limite: "você teria que programar milhões de regras", com erro humano e conhecimento limitado. Ele chama os ramos do if/else de "probabilidades", mas eles são caminhos determinísticos, não probabilidades. O exemplo é imperativo, não o par base de conhecimento + motor de inferência descrito acima: serve como intuição, não como definição de sistema especialista.

## Key Sources

- [[wiki/sources/10-conceitos-fundamentais-ia-moderna-bernardo-lobato]]
- [[wiki/sources/frontpush-ia-o-que-voce-deve-saber-de-ia]]: FrontPUSH, módulo de IA, parte 1: regras à mão e o limite das "milhões de regras"
