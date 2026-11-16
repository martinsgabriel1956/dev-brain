---
type: concept
title: "Mobile first"
aliases: ["mobile-first", "mobile first CSS", "primeiro o mobile"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 1
tags: [css, responsivo, mobile-first, media-query, breakpoint, frontend]
skill: tech-mentor-frontend
status: stub
---

# Mobile first

Estratégia de [[wiki/concepts/design-responsivo|design responsivo]] em que o layout nasce para a tela pequena e ganha regras conforme a tela cresce. No CSS, os estilos fora de qualquer media query são os do celular, e cada [[wiki/concepts/breakpoint]] usa `@media (min-width: ...)` para acrescentar o que telas maiores precisam. O contrário, desktop first, parte da tela grande e remenda com `max-width`.

`[skill: tech-mentor-frontend]` Vantagens citadas: o celular baixa e avalia menos CSS, o conteúdo essencial é priorizado e acrescentar é mais simples que desfazer. Unidades relativas (`%`, `rem`, `vw`) ajudam, mas não são o mobile first em si; ver [[wiki/concepts/unidades-de-medida-css]].

## Na NLW #2, dia 1 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-1-programacao-web-html-css-proffy]], [[wiki/entities/mayk-brito|Mayk]] apresenta o conceito para o Proffy: dá para desenvolver "toda funcional num desktop" ou "numa maneira mobile first, ou seja, vou primeiro ver essa página funcionando em dispositivos pequenos [...] e depois eu vou arrumar essa página para o desktop". Ele liga a ideia às unidades: "todo o controle de medida que eu vou fazer daqui pra frente, eu vou usar rem [...] ou porcentagens"; pixel "só quando eu for mexer no desktop". O dia 1 não tem media query, então a regra `min-width` ainda não aparece.

Na NLW #1, a página do Ecoleta foi desktop first, com `max-width: 900px` ([[wiki/sources/nlw-1-dia-1-programacao-web-html-css-ecoleta]]); ver [[wiki/concepts/breakpoint]].

## Key sources

- [[wiki/sources/nlw-2-dia-1-programacao-web-html-css-proffy]]: mobile first anunciado para o Proffy, com rem e porcentagem como unidades
