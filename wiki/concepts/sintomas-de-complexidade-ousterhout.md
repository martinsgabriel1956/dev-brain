---
type: concept
title: "Sintomas de Complexidade (Ousterhout)"
aliases: ["change amplification", "amplificação de mudanças", "cognitive load burden", "unknown unknowns", "incógnitas desconhecidas", "sintomas de complexidade de software", "sistema óbvio"]
date_created: 2026-09-08
date_updated: 2026-11-25
source_count: 2
tags: [complexidade, design, ousterhout, arquitetura, deteccao]
skill: tech-mentor-backend
status: draft
---

# Sintomas de Complexidade (Ousterhout)

## TL;DR

Três manifestações que [[wiki/entities/john-ousterhout]] usa (*A Philosophy of Software Design*, cap. 2.2) para reconhecer que um sistema está complexo demais sem precisar de uma métrica: **amplificação de mudanças** (*change amplification*), **carga cognitiva** (*cognitive load*) e **incógnitas desconhecidas** (*unknown unknowns*). São sintomas, não causas. As causas são dependências e obscuridade ([[wiki/concepts/causas-de-complexidade-ousterhout]]). O oposto dos três é um sistema **óbvio**.

## Os três sintomas

Os exemplos vêm do texto do livro ([[wiki/sources/filosofia-do-design-de-software-cap-02-natureza-da-complexidade]]), todos em torno do mesmo site com banner colorido (Figura 2.1).

- **Amplificação de mudanças:** uma mudança aparentemente simples exige editar muitos lugares. Na Figura 2.1(a), cada página define `bg = 'red'`, e trocar a cor significa editar milhares de páginas. A dependência aqui é **conhecida**: o problema é a quantidade de lugares. Objetivo de design: reduzir a quantidade de código afetada por cada decisão de projeto.
- **Carga cognitiva:** quanto o desenvolvedor precisa saber para concluir a tarefa. Exemplo: uma função em C que aloca memória e deixa a liberação para quem chama. Fontes típicas: APIs com muitos métodos, variáveis globais, inconsistências e dependências entre módulos ([[wiki/concepts/carga-cognitiva]]). Não é o mesmo que tamanho: "às vezes, uma abordagem que exige mais linhas de código é, na verdade, mais simples".
- **Incógnitas desconhecidas:** não é óbvio que código mudar nem que informação é preciso ter. Na Figura 2.1(c), algumas páginas usam um tom mais escuro do banner escrito à mão. Quem troca `bannerBg` não fica sabendo e só descobre pelo bug.

## Por que as incógnitas desconhecidas são as piores

O autor compara os três. A amplificação "é irritante", mas, se está claro que código mudar, o sistema funciona ao final. A carga cognitiva encarece a mudança, mas, se está claro o que ler, a mudança tende a sair certa. Com incógnitas desconhecidas, não se sabe o que fazer nem se a solução vai funcionar. A única garantia seria ler todas as linhas do sistema, o que é impossível, e nem isso basta se a mudança depende de uma decisão de design que nunca foi documentada. O que separa os três é **saber onde olhar**: os dois primeiros são caros, mas visíveis.

## O oposto: sistema óbvio

Um dos objetivos mais importantes do design é que o sistema seja óbvio: o desenvolvedor dá um palpite rápido sobre o que fazer, sem pensar muito, e pode confiar que acertou. É o oposto de carga cognitiva alta e de incógnitas desconhecidas. O livro trata do tema no cap. 18.

## Como reconhecer na prática

[[wiki/sources/filosofia-design-software-podcast-eduardo-matos-otavio-santana-mauricio-linhares]] trata esses sintomas como os primeiros sinais que dois engenheiros experientes procuram ao chegar numa base de código nova. Uma mudança que parecia isolada numa classe se espalha para dependências que ninguém conhecia. Um onboarding longo porque "a documentação sou eu" mostra que o conhecimento necessário para mudar o sistema nunca foi registrado.

**Nuance:** o podcast chama o primeiro caso de amplificação de mudanças, mas, como a dependência era desconhecida, no vocabulário do livro ele é sobretudo uma **incógnita desconhecida**. A amplificação pura é a da Figura 2.1(a), em que todos sabem onde mexer. Na prática os dois sintomas costumam vir juntos, o que explica a mistura.

## Relação com outros conceitos

- [[wiki/concepts/causas-de-complexidade-ousterhout]]: dependências geram amplificação e carga cognitiva; a obscuridade gera incógnitas desconhecidas e carga cognitiva.
- [[wiki/concepts/ocultamento-de-informacao]]: o vazamento de informação (a mesma decisão de design espalhada por vários módulos) é uma causa estrutural comum de amplificação de mudanças.
- [[wiki/concepts/modulo-profundo]]: módulos rasos aumentam a carga cognitiva, porque o leitor precisa acompanhar mais peças pequenas ao mesmo tempo.
- [[wiki/concepts/red-flags-de-design]]: os sinais de alerta do livro são heurísticas para achar as causas desses sintomas antes que eles apareçam.
- [[wiki/concepts/comprehension-debt]]: fenômeno próximo da carga cognitiva, do lado de código gerado por IA.
- [[wiki/concepts/zonas-de-desconhecimento]]: as mesmas incógnitas desconhecidas, aplicadas ao uso de IA.

## Key Sources

- [[wiki/sources/filosofia-do-design-de-software-cap-02-natureza-da-complexidade]]: texto do cap. 2.2, com a Figura 2.1, a comparação entre os sintomas e o objetivo de sistema óbvio
- [[wiki/sources/filosofia-design-software-podcast-eduardo-matos-otavio-santana-mauricio-linhares]]: amplificação de mudanças e incógnitas desconhecidas como os primeiros sinais práticos de complexidade, com exemplos de onboarding
