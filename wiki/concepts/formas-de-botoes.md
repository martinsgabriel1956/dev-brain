---
type: concept
title: "Formas de botões"
aliases: ["formato de botão", "estilização de botões", "botão retangular", "botão arredondado", "botão circular", "botão pill", "botão chanfrado", "botão diagonal", "botão hexagonal"]
date_created: 2026-11-13
date_updated: 2026-11-13
source_count: 1
tags: [ui, ui-design, botoes, formas, border-radius, geometrico, organico, branding]
skill: ux-ui-mentor
status: stub
---

# Formas de botões

A forma do [[wiki/concepts/botoes-em-interfaces|botão]] é uma aplicação direta de [[wiki/concepts/formas-geometricas-e-organicas]]: cada contorno passa uma ideia, e a escolha depende do que a interface quer comunicar. "O grande segredo está na predominância" ([[wiki/sources/formas-de-botoes-reto-arredondado-circular-chanfrado-diagonal-hexagonal]]).

## Catálogo

| Forma | Passa | Onde aparece (exemplos da aula) |
|---|---|---|
| Retangular (90°) | Modernidade, seriedade, racionalidade, disciplina, precisão | Moda, corporações, negócios, tecnologia; Madero, site de arquitetura |
| Bordas arredondadas | Amigável; "ótimo coringa" | Site do próprio autor |
| Bordas circulares (pill) | Carismático, cativante, harmonia; "traz mais para perto" | Entretenimento, música, jogos; [[wiki/entities/nubank]], [[wiki/entities/apple]] |
| Chanfrado | Imaginação, abstração, ficção científica, futurista | Cinema, jogo do Homem-Aranha |
| Diagonal | Dinamicidade, movimento, direção ("de vai"); vem com seta | Esporte, PES, FIFA, páginas de eventos |
| Hexagonal | "Toque de administração e balanço" (literal) | Interfaces gamificadas, apps para crianças; também futurista |

Os três primeiros predominam; os três últimos "também existem".

## O botão como contraste

O botão pode ir contra a predominância da página de propósito. O Madero é orgânico (foto de comida, logo com serifa) e usa botões retos e letra sem serifa como [[wiki/concepts/contraste]]. O site de arquitetura é todo reto e põe o orgânico numa foto de pessoa. "Um site totalmente geométrico [...] fica muito longe da pessoa" ([[wiki/sources/formas-de-botoes-reto-arredondado-circular-chanfrado-diagonal-hexagonal]]). Ver [[wiki/concepts/harmonia-visual]].

## Relação com o raio

Do reto ao pill, a variável é o [[wiki/concepts/border-radius]]. Chanfrado, diagonal e hexagonal saem dessa escala: não são raio, são outro contorno.

## Olhar de dev

- `[skill: ux-ui-mentor]` Reto, arredondado e pill são um token (`--radius-button`: `0`, `8px`, `9999px`). Uma forma por sistema, aplicada em todos os botões ([[wiki/concepts/consistencia-visual]]).
- `[external]` Chanfrado, diagonal e hexágono usam `clip-path` ou `transform: skew`. `clip-path` corta o `outline` de foco e o `box-shadow` e limita o clique à área recortada; ponha foco e sombra num elemento pai. A [[wiki/concepts/area-clicavel]] mínima vale para a forma visível.
- `[external]` A preferência por curvas tem base empírica: Bar e Neta (2006), *Psychological Science* (https://doi.org/10.1111/j.1467-9280.2006.01759.x).

## Key Sources

- [[wiki/sources/formas-de-botoes-reto-arredondado-circular-chanfrado-diagonal-hexagonal]] — catálogo das seis formas (edição "W7")
