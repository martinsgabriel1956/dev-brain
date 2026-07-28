---
type: entity
title: "Knight Capital"
aliases: ["Knight Capital Group", "Knight Capital incident", "incidente Knight Capital"]
date_created: 2026-07-28
date_updated: 2026-07-28
source_count: 1
tags: [tech-debt, post-mortem, incident, dead-code, caso-de-estudo]
skill: tech-mentor-leadership
status: stub
---

# Knight Capital

## TL;DR

Empresa de trading de alta frequência que sofreu, em agosto de 2012, um dos incidentes de software mais citados como exemplo de dívida técnica descontrolada: código morto ("dead code") reativado por engano durante um deploy causou ordens de compra/venda erráticas por cerca de 45 minutos, gerando uma perda estimada publicamente entre **US$ 440-460 milhões** [external] — quase levando a empresa à falência.

## O Que Aconteceu (contexto externo, não detalhado na fonte original)

[[wiki/sources/tech-debt-guia-completo-gestao-metricas]] cita o caso apenas de passagem, como exemplo de para onde leva "código morto" e dívida técnica não gerenciada, sem detalhar o incidente — e menciona o valor da perda como "$462 milhões". O valor amplamente documentado externamente para esse incidente é de aproximadamente $440-460 milhões [external] — a cifra citada pela fonte está dentro dessa faixa comumente reportada, mas nenhuma fonte primária foi apresentada no vídeo para o número exato.

## Por Que É Citado em Discussões de Tech Debt

Funciona como o exemplo extremo do risco de **não aplicar a [[wiki/concepts/boy-scout-rule]]** — código morto que devia ter sido removido permaneceu no sistema e foi reativado inadvertidamente, ilustrando por que "ver código morto, deletar" é mais que uma boa prática estética: é prevenção de incidente.

## Relacionado

[[wiki/concepts/tech-debt-como-ferramenta]] · [[wiki/concepts/boy-scout-rule]]

## Key Sources

- [[wiki/sources/tech-debt-guia-completo-gestao-metricas]]
