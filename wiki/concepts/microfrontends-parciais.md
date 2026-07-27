---
type: concept
title: "Microfrontends Parciais"
aliases: ["microfrontends distribuídos", "microfrontends orquestrados", "partial microfrontends"]
date_created: 2026-07-27
date_updated: 2026-07-27
source_count: 1
tags: [frontend, microfrontends, arquitetura, module-federation, polirrepo]
skill: tech-mentor-frontend
status: stub
---

# Microfrontends Parciais

Estilo de microfrontend em que partes de uma mesma tela (ex.: um card específico) são renderizadas por aplicações independentes — potencialmente em frameworks diferentes (React, Angular, Solid.js) — rodando em hosts/portas separadas, sem se conhecerem, e compostas por um Shell que decide qual exibir a partir de eventos (Custom Events, `window.dispatchEvent`) e isolamento via Shadow DOM.

## Vantagem Vendida vs. Custo Real

A promessa é desacoplamento alto: polirrepos, CI/CD 100% independente por time, ownership isolado por microfrontend. Na prática, o custo tende a superar o benefício fora de bigtechs com ferramental maduro:

- **Performance:** múltiplos frameworks coexistindo na mesma tela multiplicam o JavaScript enviado ao cliente — um dos maiores oneradores de performance web.
- **CI/CD fragmentado:** N microfrontends = N pipelines para manter, sem consolidação natural.
- **Versionamento:** um bump de versão compartilhada (ex.: React) exige atualização manual em cada repositório separadamente — sem grafo de dependências único.
- **Mudança num Design System:** editar componente → bump → atualizar dependência em cada microfrontend consumidor → PR → deploy → validar em produção, repetido por consumidor.
- **Governança e observabilidade:** tendem a virar problema rápido conforme o número de microfrontends cresce — ex.: quanto tempo levaria para propagar a correção de uma vulnerabilidade (como as que já surgiram no Axios ou no Next) por todos os locais.

## Quando Faz Sentido

Segundo `references/micro-frontends-deep.md` da skill `tech-mentor-frontend`: múltiplos times independentes trabalhando no mesmo produto, áreas com tecnologias ou ciclos de release radicalmente diferentes, ou aplicação grande demais para um único time manter com qualidade. Fora desses cenários — time único/pequeno, produto pequeno a médio, time sem experiência prévia — a recomendação é começar com [[wiki/concepts/monolito-modular-frontend|monolito modular]].

## Posição na Escala de Complexidade

É o extremo mais custoso da escala de arquitetura frontend, contrastando com [[wiki/concepts/microfrontend-baseado-em-rotas]], que entrega grande parte do mesmo desacoplamento com um incremento de complexidade muito menor sobre o monolito modular.

## Key Sources

- [[wiki/sources/arquitetura-frontend-microfrontends-monolito-modular-vertical-slice]] — demo prática Shell + React/Angular/Solid.js via Custom Events, e o levantamento de custos (performance, CI/CD, versionamento, governança) que a "venda" de microfrontends costuma esconder
