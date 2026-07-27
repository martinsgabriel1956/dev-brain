---
type: concept
title: "Microfrontend Baseado em Rotas"
aliases: ["route-based microfrontend", "microfrontend por rota", "arquitetura frontend intermediária"]
date_created: 2026-07-27
date_updated: 2026-07-27
source_count: 1
tags: [frontend, microfrontends, arquitetura, monorepo, module-federation]
skill: tech-mentor-frontend
status: stub
---

# Microfrontend Baseado em Rotas

Arquitetura em que um proxy reverso roteia diferentes seções da aplicação para builds independentes, mantendo a estrutura de um monorepo por baixo — o que antes era um único build com módulos-fronteira (ver [[wiki/concepts/monolito-modular-frontend]]) passa a ter builds separados por módulo, cada um com deploy próprio.

## Mecânica

- O que era pasta/pacote compartilhado dentro do monolito modular vira **lib instalável do monorepo** (ex.: libs Nx) — acessada pelos módulos como se fosse uma dependência externa.
- O que eram módulos-fronteira (organização lógica) passam a ser módulos com **build e deploy independentes** de fato.
- Um grafo de dependências propaga updates de forma direta: "atualizei um pacote → atualizem todos os locais que dependem disso".

## Por Que É um Meio-Termo Eficiente

Resolve o gargalo natural do monolito modular com build único — CI/CD, tempo de teste e deploys começando a esbarrar uns nos outros conforme o time cresce — sem herdar a complexidade dos [[wiki/concepts/microfrontends-parciais|microfrontends parciais/distribuídos]] (múltiplos frameworks coexistindo na tela, polirrepo, comunicação via eventos). Entrega autonomia de deploy, autonomia de build e autonomia de execução de testes por escopo, mantendo observabilidade e governança tratáveis porque a estrutura de monorepo preserva um único grafo de dependências.

## Posição na Escala de Complexidade

Descrito como a arquitetura preferida do autor da fonte primária: a maior parte dos benefícios de desacoplamento pela menor taxa de complexidade adicionada, situando-se — junto do [[wiki/concepts/monolito-modular-frontend|monolito modular]] — na faixa onde a maioria das decisões saudáveis de arquitetura frontend deveria ficar, evitando os dois extremos (camadas sem fronteira e microfrontends parciais distribuídos).

## Key Sources

- [[wiki/sources/arquitetura-frontend-microfrontends-monolito-modular-vertical-slice]] — descrição da transição monolito modular → builds separados via monorepo/libs, e a defesa de que essa é a arquitetura com melhor relação benefício/complexidade
