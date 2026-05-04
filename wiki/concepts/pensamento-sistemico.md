---
type: concept
title: "Pensamento Sistêmico"
aliases: ["systems thinking", "pensar em sistema", "visão de sistema"]
date_created: 2026-04-29
date_updated: 2026-04-29
source_count: 2
tags: [arquitetura, sistemas, fundamentos, carreira, design]
skill: tech-mentor-leadership
status: draft
---

# Pensamento Sistêmico

Pensar em *sistema* em vez de em *arquivo*. A diferença: código que passa em testes vs sistema que funciona com carga real, inputs inesperados e dependências externas falhando.

## Código que Funciona vs Sistema que Funciona

| Código que funciona | Sistema que funciona |
|---|---|
| Passa nos testes locais | Aguenta milhares de usuários simultâneos |
| Cobre os casos previstos | Resiste a inputs que ninguém previu |
| Funciona na máquina do dev | Funciona com dependências externas instáveis |

## Elementos do Pensamento Sistêmico

- **Modelar antes de codar** — fluxo de dados, responsabilidades, fronteiras de módulo, antes de abrir o editor
- **Acoplamento e dependências** — entender como módulos se conectam e onde crescimento vai quebrar
- **Decisões de banco** — cada banco é uma decisão arquitetural que altera o design do sistema inteiro
- **Escalabilidade** — o que acontece quando volume triplica?

## Onde Mais Falta

Devs que focam em "fazer funcionar" sem perguntar "o que acontece quando cresce?" acumulam dívida arquitetural que troca de velocidade de entrega por fragilidade de sistema.

## Relações

- [[concepts/acoplamento]] — dependências são o maior gargalo de sistemas que crescem
- [[concepts/observabilidade]] — ver o sistema como sistema vivo em produção
- [[concepts/paridade-local-producao]] — sistemas em prod se comportam diferente do dev

## Key Sources

- [[sources/roadmap-dev-senior-2026]]
- [[sources/pensamento-estruturado-resolucao-de-problemas]] — complementa: pensar sobre o problema antes de qualquer código
