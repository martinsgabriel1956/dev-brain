---
type: concept
title: "Planning Poker"
aliases: ["Poker de Planejamento", "Scrum Poker"]
date_created: 2026-07-28
date_updated: 2026-08-18
source_count: 2
tags: [agile, scrum, estimativa, engineering-management]
skill: tech-mentor-leadership
status: stable
---

# Planning Poker

**TL;DR:** Cerimônia de estimativa em que o time atribui [[wiki/concepts/story-points]] a uma tarefa através de um "jogo de cartas" simultâneo. O objetivo real não é chegar a uma média — é **revelar divergências de entendimento** sobre a tarefa e forçar o time a conversar sobre elas.

## Processo

1. PO ou tech lead apresenta a história (idealmente até 5 minutos).
2. Cada pessoa do time escolhe um valor da escala de pontos, sem revelar.
3. Todos revelam ao mesmo tempo.
4. Se houver divergência grande entre o menor e o maior valor (ex.: 1 vs. 13), quem deu o menor e quem deu o maior explicam o raciocínio — geralmente um dos dois enxergou uma complexidade ou um risco que o outro não viu.
5. Repete-se a rodada até o time convergir em um valor comum.

## Regras Práticas

- **Sem anchor bias:** ninguém fala um número em voz alta antes da revelação simultânea — falar primeiro ancora o resto do time no seu valor.
- **Limite de tempo:** se uma única história consome mais de ~15 minutos, ela provavelmente precisa ser subdividida em vez de estimada à força.
- **Se após 3 rodadas não há convergência:** o time não tem informação suficiente para estimar — vale mais um spike técnico de investigação antes de tentar estimar de novo do que forçar um número.

## Por Que Não é Sobre o Número

O valor final atribuído a uma história é quase um efeito colateral do processo. O que o Planning Poker realmente produz é a conversa: alguém que estimou baixo pode não ter visto uma dependência externa; alguém que estimou alto pode ter contexto de uma dívida técnica que os outros desconhecem. Quando essa conversa não acontece — por exemplo, porque o PO já chegou com o número decidido — a cerimônia perde a função e o valor atribuído volta a ser arbitrário. Ver [[wiki/concepts/story-points#o-erro-de-forçar-um-número-alvo|o erro de forçar um número-alvo]].

## Quem Deveria Estar na Sala

[[wiki/sources/por-que-estimativas-de-software-falham-como-melhorar]] reforça um critério prático de participação: quanto mais pessoas envolvidas na estimativa — especialmente quem tem a expertise específica de uma parte do sistema — maior a chance de alguém já ter enfrentado um obstáculo concreto daquela tarefa antes. Quem vai efetivamente executar uma tarefa deveria participar da estimativa dela, não apenas o tech lead estimando "de fora" com base em quem ele imagina que vai executar.

## Conceitos Relacionados

[[wiki/concepts/story-points]] · [[wiki/concepts/scrum-master]] · [[wiki/concepts/user-stories]] · [[wiki/concepts/reducao-de-incerteza-antes-de-estimar]]

## Key Sources

- [[wiki/sources/story-points-po-forcando-30-40-pontos-por-sprint]]
- [[wiki/sources/por-que-estimativas-de-software-falham-como-melhorar]] — reforça a participação de quem tem expertise específica na estimativa de cada tarefa
