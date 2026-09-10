---
type: concept
title: "Composition Root"
aliases: ["composition root", "composição grude", "raiz de composição", "main layer"]
date_created: 2026-09-08
date_updated: 2026-09-08
source_count: 3
tags: [design-patterns, dependency-injection, clean-architecture, factory-pattern, acoplamento]
skill: tech-mentor-backend
status: stub
---

# Composition Root

Ponto único da aplicação onde todas as implementações concretas são instanciadas e "encaixadas" nas interfaces que as demais camadas dependem — o único lugar do sistema que se acopla a tudo, para permitir que todo o resto fique desacoplado entre si. Em Clean Architecture, costuma corresponder a uma camada própria (**Main**), separada do domínio, dos casos de uso e da UI.

## Por que precisa existir

Se o domínio e os casos de uso dependem só de interfaces (via [[wiki/concepts/dependency-inversion-principle|inversão de dependência]]), alguém precisa, em algum ponto do sistema, decidir *qual* implementação concreta usar e injetá-la — sem isso, nada roda de fato. Esse "alguém" é o composition root. É por isso que [[wiki/concepts/dependency-injection]] não elimina acoplamento — só o desloca inteiro para um único ponto, deliberadamente.

## Mecanismo comum: Factory

Uma forma prática de implementar o composition root é o design pattern [[wiki/concepts/factory-pattern|Factory]]: uma classe (ex.: `LoginFactory`) que conhece todas as implementações concretas necessárias (validadores, cliente HTTP, implementação de autenticação) e monta o componente final já com todas as dependências injetadas. Ver exemplo concreto em [[wiki/sources/clean-architecture-frontend-vue-diagrama-camadas-login]].

## Por que não aparece com setas individuais no diagrama de arquitetura

Como o composition root depende de virtualmente todas as camadas do sistema (não só de uma, como as demais camadas fazem entre si), desenhar uma seta de dependência para cada componente individual polui o diagrama. A convenção prática é desenhar a dependência do composition root apontando só para as camadas (Data, Infraestrutura, Validation), não para cada classe concreta.

## Custo: rastreabilidade

O mesmo mecanismo que dá testabilidade e substituibilidade (trocar `PostgresUserRepository` por um mock, ou `AxiosHttpClient` por um fake) tem um custo simétrico: ler o código de um caso de uso não revela qual implementação concreta está de fato rodando em produção — é preciso rastrear até o composition root para descobrir qual adapter foi injetado ali. Ver [[wiki/concepts/dependency-injection]] e [[wiki/concepts/clean-architecture]] para essa mesma tensão do lado do backend.

## Key Sources

- [[wiki/sources/clean-architecture-frontend-vue-diagrama-camadas-login]] — exemplo concreto no frontend (`LoginFactory` como composition root de uma tela de login em Vue), termo informal "composição grude"
- [[wiki/sources/arquitetura-limpa-por-que-e-tao-popular]] — menção inline do termo (sem exemplo de código), no contexto do custo de rastreabilidade de implementação escondida
