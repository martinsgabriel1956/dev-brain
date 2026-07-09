---
type: source
title: "Como Evitar o Over-Engineering"
aliases: ["comentário sobre vídeo do David Farley", "over-engineering vs under-engineering"]
date_created: 2026-07-09
date_updated: 2026-07-09
source_count: 0
tags: [over-engineering, under-engineering, dora, accelerate, tdd, continuous-delivery, walking-skeleton, agile, martin-fowler, david-farley, kiss]
skill: tech-mentor-leadership
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/como-evitar-over-engineering-david-farley.md
source_url: ""
author: "Criador de conteúdo (comentário reagindo a vídeo de David Farley); citação de Guilherme Fróes (Thoughtworks/Google)"
date_published: ""
date_ingested: 2026-07-09
---

## TL;DR

Comentário em vídeo, reagindo a um vídeo de David Farley sobre over-engineering. Argumento central: o "triângulo de ferro" (rápido/barato/bom — escolha dois) é um mito para software — dados do DORA/*Accelerate* mostram que velocidade de entrega e qualidade se correlacionam positivamente, não competem. O maior problema da indústria não é over-engineering, é **under-engineering**. Mas over-engineering existe e tem duas causas principais: (1) perfeccionismo por falta de objetivo/conhecimento, e (2) falta de confiança, que leva a resolver todos os requisitos não-funcionais (escala, performance, resiliência) antes de entregar qualquer valor — ilustrado pelo caso do LMAX, que usou a técnica do "walking skeleton" (esqueleto ambulante) para validar a arquitetura fim-a-fim com uma solução mínima antes de otimizar.

---

## Key Claims

**Claim:** O "triângulo de ferro" (rápido, barato, bom — escolha dois) não se aplica a software; velocidade e qualidade se correlacionam positivamente, não competem.
**Evidence:** Pesquisa DORA (DevOps Research and Assessment), publicada no livro *Accelerate*, mostra que equipes que entregam mais rápido também entregam com mais qualidade — as duas métricas andam juntas, não em tensão.
**Source:** DORA / *Accelerate* (citado de segunda mão pelo autor do vídeo).
**Confidence:** Alta — DORA é um corpo de pesquisa amplamente citado e replicado na indústria; consistente com [[wiki/concepts/dora-metrics]].

**Claim:** O maior problema da indústria de software não é over-engineering, é **under-engineering**.
**Evidence:** Comentário observado no próprio vídeo do David Farley, mais uma pesquisa informal do autor com desenvolvedores de uma comunidade, com resultado unânime na mesma direção.
**Source:** David Farley (citado) + pesquisa informal do autor.
**Confidence:** Média — não é um estudo controlado, é observação anedótica/consenso de comunidade, mas alinhada com o padrão já documentado em [[wiki/concepts/over-engineering]] (que aponta perfeccionismo e antecipação de requisitos hipotéticos como causas específicas, não que seja o problema *mais comum*).

**Claim:** Qualidade interna do software está diretamente ligada à facilidade de mudança — quanto mais fácil mudar, mais rápido se entrega valor de negócio.
**Evidence:** Software é meio, não fim — existe para gerar valor de negócio; práticas como TDD e boa arquitetura existem para tornar a mudança barata, não como fim em si mesmas.
**Source:** David Farley (citado) + elaboração do autor.
**Confidence:** Alta — consistente com a definição de [[wiki/concepts/tdd]] e com a filosofia original do Extreme Programming (tolerância à mudança, "embracing change").

**Claim:** A origem do movimento ágil, antes de ser confundida com Scrum como processo, era entregar pequenos incrementos rapidamente com testes automatizados, para permitir mudar o software sem medo.
**Evidence:** Anedota de um projeto atrasado um ano na Thoughtworks, no qual Martin Fowler foi chamado para ajudar — origem situada no Extreme Programming, não no Scrum.
**Source:** Anedota do autor sobre a Thoughtworks/Martin Fowler.
**Confidence:** Baixa/anedótica — nenhum link ou documento primário citado; tratado como história de origem não verificada nesta wiki. Ver "Open Questions".

**Claim:** Over-engineering por perfeccionismo nasce de falta de objetivo claro e/ou falta de conhecimento sobre por que se está aplicando um princípio (ex.: Clean Code, Clean Architecture aplicados sem entender o objetivo).
**Evidence:** Descrição do "gamer" (dev que tem noções vagas de Clean Code/Clean Architecture e aplica sem saber por quê) que fica perdido no processo em vez de entregar.
**Source:** Elaboração do autor a partir do vídeo de Farley.
**Confidence:** Alta — consistente com [[wiki/concepts/over-engineering]] (seção "Causa Raiz no Aprendizado") e com [[wiki/sources/overengineering-carol-ate-quinta]] (ego e falta de julgamento como causas).

**Claim:** Over-engineering por falta de confiança leva a resolver escala, performance e resiliência antes de qualquer valor de negócio — exemplificado pelo LMAX, que usou um "walking skeleton" (esqueleto ambulante): arquitetura mínima fim-a-fim, colocada em produção cedo, com uma peça deliberadamente provisória (mensageria XML/HTTP) atrás de uma abstração trocável, substituída depois por uma solução binária de alta performance.
**Evidence:** Exemplo dado por David Farley sobre o desenvolvimento do LMAX (sistema de trading financeiro que ele ajudou a construir, também associado ao LMAX Disruptor).
**Source:** David Farley, exemplo do LMAX (citado de segunda mão).
**Confidence:** Média-alta — o LMAX e o Disruptor são publicamente documentados por Farley e Martin Thompson; o autor não cita fonte primária específica (paper, talk, livro), mas o padrão descrito (walking skeleton → abstração de troca → substituição por solução binária de alta performance) é consistente com a prática de continuous delivery que Farley defende publicamente (coautor de *Continuous Delivery* com Jez Humble). Ver "Open Questions".

---

## Conceitos

- [[concepts/over-engineering]]
- [[concepts/dora-metrics]]
- [[concepts/walking-skeleton]]
- [[concepts/tdd]]
- [[concepts/ci-cd]]
- [[concepts/kiss]]

---

## Entidades

- [[entities/david-farley]] — coautor de *Continuous Delivery*, criador de conteúdo sobre engenharia de software, envolvido no desenvolvimento do LMAX.
- [[entities/martin-fowler]] — citado na anedota da Thoughtworks/origem do ágil.

---

## Open Questions

- A anedota da Thoughtworks (projeto atrasado um ano, Martin Fowler chamado para ajudar, origem do ágil) não tem fonte primária citada — vale checar contra *Extreme Programming Explained* (Kent Beck) ou biografia/talks de Fowler para verificar ou refutar.
- O exemplo do LMAX (mensageria XML/HTTP substituída por protocolo binário) não cita a fonte primária exata (paper, talk ou capítulo de livro do David Farley) — vale localizar a fonte original para uma citação mais rigorosa e para checar se o exemplo é mesmo LMAX Exchange ou outro projeto que Farley menciona em talks sobre Continuous Delivery.
- A claim de que "o maior problema da indústria é under-engineering" é medida de forma informal (pesquisa não controlada) — não há como validar generalização para além do círculo de desenvolvedores consultados pelo autor.

---

## Raw Quotes

> "Existe um mito que é a ideia do triângulo de ferro... no que diz respeito a software, isso não é verdade."

> "As equipes que entregam mais rápido também entregam com mais qualidade."

> "O problema maior da nossa indústria não é over-engineering, mas sim under-engineering."

> "Engenharia de software não é perfeccionismo, engenharia de software é resolver um problema e entregar."

> "A gente sabe que isso aqui não vai ser produção [final], mas como a gente criou aqui uma abstração na qual a gente consegue trocar essa tecnologia de mensageria..."

> "Isso não é desenvolver pensando lá no futuro, é desenvolver pensando agora mesmo: daqui a pouco eu vou me dar mal se eu fizer uma bagunça aqui."

---

## Contradições / Tensões com o Wiki

- Nenhuma contradição direta. Esta fonte **complementa** [[wiki/concepts/over-engineering]] com um ângulo que a página ainda não tinha: a correlação empírica (DORA) entre velocidade e qualidade, e a distinção explícita entre a causa "perfeccionismo" (já documentada) e a causa "falta de confiança / resolver requisitos não-funcionais cedo demais" (nova, com o exemplo concreto do walking skeleton do LMAX).
- Converge com [[wiki/sources/overengineering-carol-ate-quinta]] na causa "perfeccionismo/ego", mas adiciona uma segunda causa distinta (medo/falta de confiança) que aquela fonte não cobre.
- A recomendação de "deploy imediato do boilerplate" já documentada em [[wiki/concepts/ci-cd]] (seção "Deploy Imediato do Boilerplate") é, na prática, uma instância do padrão "walking skeleton" descrito aqui — esta fonte fornece o nome formal do padrão e um caso real (LMAX) que a página de CI/CD ainda não tinha.
