---
type: concept
title: "Código Espaguete"
aliases: ["code espaguete", "codigo espaguete", "spaghetti code", "codigo sopa"]
date_created: 2026-08-10
date_updated: 2026-08-14
source_count: 2
tags: [code-espaguete, acoplamento, legado, arquitetura, backend, anti-patterns, fluxo-de-controle]
skill: tech-mentor-backend
status: draft
---

# Código Espaguete

Estado de degradação em que partes do código chamam funções umas das outras em cadeia, sem organização nem fronteiras claras — "uma coisa chama outra, que chama funções de outra". Formalmente, é código cujo **[[wiki/concepts/fluxo-de-controle|fluxo de controle]]** é convoluto e difícil de entender, como macarrão "torcido e emaranhado" ([[wiki/sources/codigo-espaguete-wikipedia]]). Tipicamente surge quando um [[wiki/concepts/monolito]] cresce de forma desorganizada e vira legado.

## Origem histórica e etimologia

O termo é anterior à era OO: nasceu da prática de empilhar saltos `goto`. [[wiki/entities/richard-hamming|Hamming]] descreve que, nos primórdios da programação em binário, corrigir um bug significava substituir uma instrução por um salto para memória vazia e voltar — e o acúmulo desses saltos fazia "o caminho de controle tomar a aparência de uma lata de espaguete". Foi essa dinâmica que motivou a cruzada de [[wiki/entities/edsger-dijkstra|Dijkstra]] contra o `goto` (*"Go To Statement Considered Harmful"*, 1968). Ver [[wiki/sources/codigo-espaguete-wikipedia]].

## Família de anti-padrões e a escala macro

O código espaguete é um [[wiki/concepts/anti-pattern|anti-padrão]] com parentes por analogia de massas: [[wiki/concepts/lasagna-code|lasagna code]] (camadas entrelaçadas) e [[wiki/concepts/ravioli-code|ravioli code]] (fragmentação excessiva). Quando escala para o nível arquitetural, vira uma [[wiki/concepts/big-ball-of-mud|Big Ball of Mud]] — sistema sem arquitetura perceptível. A causa raiz comum é a [[wiki/concepts/entropia-de-software|entropia de software]]: pressão de prazo, turnover e reparos improvisados. Prevenção segundo a Wikípédia: melhores ferramentas, treino e processos — na prática, [[wiki/concepts/refatoracao|refatoração]] contínua e gates como [[wiki/concepts/complexidade-ciclomatica|complexidade ciclomática]].

## Como cada arquitetura o combate

- **[[wiki/concepts/microsservicos]]** o eliminam por **impossibilidade estrutural**: um serviço não consegue chamar funções de outro; a comunicação passa a ser via rede/API. O acoplamento em cadeia deixa de ser possível — mas ao custo de latência e overhead distribuído (e ainda é possível cair num distributed monolith).
- **[[wiki/concepts/monolito-modular]]** o combate por **contratos/interfaces** entre módulos ([[wiki/concepts/hexagonal-architecture|Ports & Adapters]]), sem pagar o custo da rede.

Ver [[wiki/sources/monolito-modular-transicao-mvp-empresa-madura]].

## Key sources

- [[wiki/sources/monolito-modular-transicao-mvp-empresa-madura]]
- [[wiki/sources/codigo-espaguete-wikipedia]] — definição formal (fluxo de controle convoluto), etimologia via Hamming, família de anti-padrões e ponte para Big Ball of Mud
