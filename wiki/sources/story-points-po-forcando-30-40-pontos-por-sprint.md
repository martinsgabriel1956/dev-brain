---
type: source
title: "Story Points, Scrum Master e PO — Por Que Forçar 30-40 Pontos por Sprint Está Errado"
aliases: ["30 a 40 story points por sprint", "PO forçando story points"]
date_created: 2026-07-28
date_updated: 2026-07-28
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/story-points-po-forcando-30-40-pontos-por-sprint.md
source_url: ""
author: "Lucas Badico"
date_published: ""
date_ingested: 2026-07-28
tags: [agile, scrum, story-points, engineering-management, mentoria]
skill: tech-mentor-leadership
status: stable
---

# Story Points, Scrum Master e PO — Por Que Forçar 30-40 Pontos por Sprint Está Errado

## TL;DR

Vídeo de Lucas Badico originado de uma pergunta no grupo de mentorados: um PO exigia 30-40 [[wiki/concepts/story-points]] por sprint por pessoa. As respostas dos mentorados (Bruno, Thiago, Italo) convergem no mesmo diagnóstico: quando um número de pontos é imposto de cima para baixo em vez de emergir da estimativa honesta do time via [[wiki/concepts/planning-poker]], a métrica perde todo o valor — o time passa a inflar estimativas para "bater a meta" em vez de estimar complexidade real. O vídeo usa isso para discutir o papel correto do [[wiki/concepts/scrum-master]] e a origem histórica do Agile.

## Key Claims

- **Story points medem complexidade relativa, não tempo absoluto.** O valor numérico e a escala escolhida (Fibonacci, primos, ímpares) são arbitrários — o que importa é a constância do critério e a tendência (estabilidade ou crescimento) da [[wiki/concepts/story-points#velocity|velocity]] ao longo dos sprints. [[wiki/concepts/story-points]]
- **Sprint é tempo fixo, não entrega.** Tratar sprint como sinônimo de deliverable é um erro comum; o que não foi concluído no prazo vai para o próximo sprint, o sprint atual encerra do mesmo jeito.
- **Planning Poker existe para gerar conversa, não uma média.** Divergência grande entre estimativas (1 vs. 13) é o sinal mais valioso da cerimônia — revela que alguém enxergou um risco ou dependência que o resto do time não viu. [[wiki/concepts/planning-poker]]
- **Times novos devem chutar a calibração inicial e iterar.** Relato do mentorado Italo: time todo novo convencionou 1 ponto = 1 dia por falta de histórico; meses depois, com dados acumulados, um ponto já não equivale a um dia e a faixa de pontos por dev mudou de ~10 para 12-16/sprint — a métrica amadureceu organicamente, sem imposição externa.
- **Forçar uma meta de pontos corrompe a métrica (Lei de Goodhart).** Quando o PO/Scrum Master decide um número sem consultar o time, o time passa a inflar estimativas (ex.: 20 pontos num CRUD de três horas) — a métrica vira exibição, análoga a manter o GitHub "verdinho" com commits vazios. [[wiki/concepts/goodharts-law]]
- **Forçar pontos reduz colaboração e pode gerar jornadas excessivas.** Se o incentivo é "fechar meus pontos", ninguém ajuda colegas durante o sprint; um mentorado relatou um colega trabalhando 10h/dia e fins de semana para "bater" 40 pontos autoimpostos — sintoma de erro de planejamento, não de falta de esforço.
- **O Agile "industrializado" reproduz o Waterfall com verniz de cerimônias.** Cronometrar dailies ao segundo e cobrar apenas se "os pontos batem" — sem se interessar pelo valor real entregue — garante cobrança semana a semana em vez de só no final, mas não resolve o problema que o Agile nasceu para resolver (crunch e software ruim sob processo rígido). [[wiki/concepts/scrum-master]]
- **O Agile é mais veloz por valorizar aprendizado e bem-estar, não por forçar mais output.** Forçar mais código ou mais pontos por pessoa não é o mesmo que ser mais veloz, mesmo que pareça assim para quem só olha o número.

## Concepts

- [[wiki/concepts/story-points]]
- [[wiki/concepts/planning-poker]]
- [[wiki/concepts/scrum-master]]
- [[wiki/concepts/goodharts-law]]
- [[wiki/concepts/user-stories]]
- [[wiki/concepts/dora-metrics]]

## Entities

- [[wiki/entities/lucas-badico]]

## Open Questions

- Qual seria uma abordagem construtiva para um dev que recebe uma meta arbitrária de pontos de um PO — negociar recalibração com dados de velocity histórica, ou é sempre um sinal de saída do time/projeto?
- O vídeo não detalha como o "technical manager" do relato de Italo mediu e comunicou a mudança de calibração (1 ponto = 1 dia → pontos desacoplados de dias) para o resto da organização (PM, stakeholders) sem gerar confusão de expectativa.

## Raw Quotes

> "É só jogar 20 pontos num CRUD que tu faz em três horas." — Bruno

> "Quando o seu PO tá pedindo um número X de pontos, ele não tá nem aí pro valor que tá sendo entregue — o que ele tá querendo é usar esses pontos para se gabar ou para atender uma demanda das pessoas acima dele." — Lucas Badico

> "Quando o time é novo, Story Points é só um chute — e é mesmo. Tem que iterar algumas vezes para sentir a velocidade do time." — Italo

> "O número arbitrário não significa nada. Quando uma quantidade é forçada no time, essa métrica de pontos deixa de ter qualquer valor." — Italo (parafraseado por Lucas Badico)

> "A gente entende que o Agile é mais veloz — mas ele é veloz porque valoriza o aprendizado e melhora o bem-estar do dev." — Lucas Badico
