---
type: concept
title: "Hydration"
aliases: ["hidratação", "hydration mismatch", "arquitetura de ilhas", "islands architecture"]
date_created: 2026-08-03
date_updated: 2026-08-03
source_count: 1
tags: [frontend, ssr, hydration, islands-architecture, performance]
skill: tech-mentor-frontend
status: stable
---

# Hydration

Processo pelo qual o JavaScript do cliente "acorda" um HTML já renderizado no servidor (SSR): o navegador exibe o HTML estático quase instantaneamente, mas botões e inputs ainda não respondem até o JavaScript carregar, ler o HTML existente e conectar event listeners + estado a cada elemento.

## Vantagem e armadilha

- **Vantagem**: o usuário vê conteúdo antes do JavaScript terminar de carregar — em conexões lentas, pode ser a diferença entre o usuário ficar ou sair da página.
- **Hydration mismatch**: se o HTML gerado pelo servidor difere do HTML que o JavaScript geraria no cliente (ex. dado que muda entre o render do servidor e o do cliente), o framework detecta a divergência. No pior caso, descarta o HTML existente e renderiza tudo de novo do zero no cliente — perdendo o ganho de performance percebida que o SSR deveria trazer.

## Por que não hidratar a página inteira: arquitetura de ilhas

Se só uma fração da página é interativa, hidratar tudo desperdiça JavaScript e tempo de CPU. **Islands architecture** hidrata seletivamente: a maior parte da página fica como HTML puro (zero JS), e só os componentes que precisam de interatividade ("ilhas") recebem hydration — implementada por Astro (`client:load` / `client:idle` / `client:visible`), Qwik e Fresh.

## Variantes relacionadas

- **Partial hydration**: mesmo princípio de ilhas, aplicado dentro de frameworks tradicionais.
- **Resumability (Qwik)**: vai além de adiar/seletivizar hydration — serializa estado e listeners no próprio HTML, evitando re-executar o framework inteiro no cliente. Ver `frontend-rendering.md` na skill `tech-mentor-frontend` para o comparativo completo hydration vs. resumability.

## Ver também

- [[wiki/concepts/dom]] — o que a hydration está conectando
- [[wiki/concepts/client-side-routing]] — outro mecanismo que troca conteúdo sem full page reload

## Key Sources

- [[wiki/sources/10-conceitos-internos-frameworks-frontend]]
