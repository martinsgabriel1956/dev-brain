---
type: concept
title: "Jogar Código Fora Como Prática"
aliases: ["escreva e jogue fora", "codigo descartavel", "throwaway prototyping", "cowsay como exercicio"]
date_created: 2026-09-18
date_updated: 2026-09-18
source_count: 1
tags: [prototipagem, aprendizado, craftsmanship, medo-de-comecar]
skill: tech-mentor-leadership
status: stub
---

# Jogar Código Fora Como Prática

**TL;DR:** Posição pedagógica de [[wiki/entities/fabio-akita]]: programar não é majoritariamente "digitar código que vai ficar" — é escrever protótipos, testar ideias e **jogar fora a maior parte do que se escreve**. Quem nunca escreve código sem objetivo, só para depois descartar, é descrito como provavelmente medíocre — o hábito de nunca jogar nada fora sinaliza medo de errar, não disciplina.

## O Argumento

Na dúvida sobre como resolver um problema, o primeiro passo é fazer um protótipo — "um código que talvez você vá jogar fora, talvez não, um código que certamente vai jogar fora em algum momento". Só depois de chegar numa versão mínima com a qual se sinta confortável é que vale a pena se comprometer com esse código: adicionar testes unitários, refatorar, pagar dívida técnica. Comprometer-se cedo demais com o primeiro rascunho é descrito como fonte de repetição de erros.

## Exercício Concreto: `cowsay`

A fonte usa como exemplo prático o programa Unix `cowsay` (desenha uma vaca em ASCII art a partir de uma mensagem, sem propósito funcional nenhum) como exercício recomendado para iniciantes: reimplementar `cowsay` em várias linguagens diferentes, sem outro objetivo além de programar em si, e jogar o código fora depois. O objetivo não é o artefato — é perder o medo da "tela vazia do editor".

## Comparação Implícita com Consumo Passivo

A fonte contrasta esse hábito com o tempo gasto em redes sociais/jogos casuais (TikTok, Instagram, Candy Crush): mesmo um exercício de programação "inútil" e descartável produz mais valor (perda do medo de começar, familiaridade com a linguagem) do que entretenimento passivo equivalente em tempo.

## Ver também

- [[wiki/concepts/beira-do-caos]] — jogar código fora funciona como o componente de "caos controlado" no ciclo ordem/caos aplicado à prática de programação
- [[wiki/concepts/mvp]] — mesma lógica em escala de produto: escopo mínimo, descartável se a hipótese falhar
- [[wiki/concepts/aprendizado-por-exposicao]] — já documenta a prática de copiar/escrever código massivamente sem objetivo imediato como formação de fluência; esta página cobre especificamente o hábito de **descartar** o que foi escrito, não só escrevê-lo

## Key Sources

- [[wiki/sources/aprendizado-gestao-e-beira-do-caos-fabio-akita]] — fonte primária e única desta ingestão
