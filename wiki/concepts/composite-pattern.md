---
type: concept
title: "Composite Pattern"
aliases: ["composite", "padrão composite", "composição de objetos"]
date_created: 2026-09-08
date_updated: 2026-09-08
source_count: 1
tags: [design-patterns, structural, gof, oop, composite]
skill: tech-mentor-backend
status: stub
---

# Composite Pattern

Padrão estrutural [[wiki/entities/gang-of-four|GoF]] que compõe objetos com a mesma interface em estruturas maiores, permitindo tratar um objeto individual e uma composição de objetos de forma uniforme — quem consome não precisa saber se está lidando com um único elemento ou com vários agrupados.

## Exemplo prático: composição de validadores de formulário

[[wiki/sources/clean-architecture-frontend-vue-diagrama-camadas-login]] usa Composite para resolver um problema concreto: um formulário de login precisa de vários validadores (`RequiredFieldValidation` para o e-mail, `RequiredFieldValidation` para a senha, `EmailFieldValidation` para o formato do e-mail, etc.), mas o componente só quer injetar **um** objeto de validação. A solução: todos os validadores implementam a mesma interface (`Validation`), e um `ValidationComposite` os agrupa — por fora, o componente de login enxerga um único `Validation`, por dentro o Composite distribui a chamada para cada validador que agrupa.

## Diferença para Factory

[[wiki/concepts/factory-pattern|Factory]] resolve *quem cria* o objeto; Composite resolve *como vários objetos do mesmo tipo se combinam* depois de criados. No exemplo do login, a [[wiki/concepts/composition-root|composition root]] (`LoginFactory`) é quem instancia cada validador individual e o `ValidationComposite` que os agrupa — os dois padrões trabalham juntos, em papéis diferentes.

## Posição no catálogo GoF

Listado em [[wiki/concepts/structural-patterns]] junto com [[wiki/concepts/adapter-pattern]], [[wiki/concepts/facade-pattern]], [[wiki/concepts/decorator-pattern]] e [[wiki/concepts/proxy-pattern]] — ainda sem exemplo próprio documentado na wiki até esta fonte.

## Key Sources

- [[wiki/sources/clean-architecture-frontend-vue-diagrama-camadas-login]] — `ValidationComposite` agrupando validadores de campo num formulário de login
