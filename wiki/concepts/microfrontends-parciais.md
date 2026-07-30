---
type: concept
title: "Microfrontends Parciais"
aliases: ["microfrontends distribuídos", "microfrontends orquestrados", "partial microfrontends"]
date_created: 2026-07-27
date_updated: 2026-07-30
source_count: 2
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

## Caso de Integração com Sistemas de Terceiros

[[wiki/sources/arquitetura-frontend-dash-fornecedores-vs-microfrontends-super-roupas]] aplica o padrão a um cenário diferente do demo original: em vez de módulos internos do mesmo produto, os "módulos" seriam 4 sistemas de gestão de fornecedores externos e heterogêneos, orquestrados por um container/shell com uma sidebar disparando eventos. A fonte usa esse caso para argumentar que o padrão, mesmo tecnicamente correto (baixo acoplamento, polirrepo, CDs independentes), resolve o problema errado quando a real necessidade é só visibilidade de status entre sistemas — nesse caso, um [[wiki/concepts/bff-pattern|BFF]] de leitura resolve a causa raiz muito mais barato. Ver [[wiki/concepts/causa-raiz]] e [[wiki/concepts/over-engineering]].

## Key Sources

- [[wiki/sources/arquitetura-frontend-microfrontends-monolito-modular-vertical-slice]] — demo prática Shell + React/Angular/Solid.js via Custom Events, e o levantamento de custos (performance, CI/CD, versionamento, governança) que a "venda" de microfrontends costuma esconder
- [[wiki/sources/arquitetura-frontend-dash-fornecedores-vs-microfrontends-super-roupas]] — caso aplicado a integração com sistemas de terceiros/fornecedores, usado como exemplo de over-engineering arquitetural (resolve fragmentação de experiência, não a causa raiz real)
