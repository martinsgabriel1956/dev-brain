---
type: concept
title: "Dependency Injection"
aliases: ["DI", "injeção de dependência"]
date_created: 2026-08-04
date_updated: 2026-08-19
source_count: 3
tags: [design-patterns, acoplamento, testabilidade, di]
skill: tech-mentor-backend
status: stub
---

# Dependency Injection

Técnica em que um componente recebe suas dependências de fora (via construtor, parâmetro ou setter) em vez de criá-las internamente. Não elimina [[wiki/concepts/acoplamento]] entre o componente e a dependência — o componente ainda precisa conhecer a interface da dependência — mas torna essa dependência **substituível** sem alterar o código do componente, o que é a base de testes unitários com mocks/stubs e de teste de integração com implementações reais.

## Onde entra na escala de acoplamento

[[wiki/sources/tres-estagios-de-acoplamento-observer-pattern-na-pratica]] situa DI dentro do "segundo estágio" de desacoplamento (componentes isolados com chamada estática/explícita entre eles): DI torna a dependência flexível e testável, mas a camada que recebe a dependência injetada ainda a conhece explicitamente — só o [[wiki/concepts/observer-pattern|Observer]] chega ao terceiro estágio, onde nenhum componente conhece o outro nem estaticamente.

## Tensão com Facade: DI completa devolve a complexidade ao cliente

[[wiki/sources/design-pattern-facade-codigo-fonte-tv]] expõe um trade-off concreto: um [[facade-pattern|Facade]] que instancia seus serviços internos com `new` fica acoplado a implementações concretas, mas se em vez disso recebesse esses serviços via DI no construtor, o código cliente teria que montar e passar todos eles na hora de usar a Facade — anulando parte do ganho de simplicidade que motivou criar a Facade. Nenhuma solução é apresentada; é registrado como trade-off real, não como erro a corrigir.

## Custo Reverso: Implementação Real Fica Difícil de Rastrear

[[wiki/sources/arquitetura-limpa-por-que-e-tao-popular]] nomeia o reverso da testabilidade: quando um componente recebe sua dependência via DI através de uma interface (ex.: um use case recebendo `UserRepository`), o ponto onde o componente é lido não revela qual implementação concreta está rodando — é preciso rastrear onde o componente foi instanciado (a composition root) e qual implementação foi passada como parâmetro naquele ponto. Ganha-se substituibilidade e testabilidade, perde-se rastreabilidade direta na leitura do código.

## Key Sources

- [[wiki/sources/tres-estagios-de-acoplamento-observer-pattern-na-pratica]] — DI citada como técnica que afrouxa mas não remove o acoplamento do segundo estágio; base de testes unitários e de integração
- [[wiki/sources/design-pattern-facade-codigo-fonte-tv]] — tensão entre DI completa e a simplicidade que o Facade deveria oferecer ao cliente
- [[wiki/sources/arquitetura-limpa-por-que-e-tao-popular]] — exemplo prático (`CreateUser`/`UserRepository`/`PostgresUserRepository`) e o custo de rastreabilidade na hora de debugar
