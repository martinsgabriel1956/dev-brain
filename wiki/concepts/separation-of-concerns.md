---
type: concept
title: "Separation of Concerns"
aliases: ["separation of concerns", "soc", "separacao de responsabilidades"]
date_created: 2026-08-10
date_updated: 2026-11-16
source_count: 4
tags: [separation-of-concerns, encapsulamento, arquitetura, modularidade, backend]
skill: tech-mentor-backend
status: stub
---

# Separation of Concerns

Princípio de dividir um sistema em partes onde cada uma cuida de uma responsabilidade distinta, com interação limitada e explícita. Num [[wiki/concepts/monolito-modular]], é o que os **contratos/interfaces** entre módulos garantem: o módulo `user` define os modos de interagir com ele (input/output), e os demais módulos não alcançam seus internals — junto com [[wiki/concepts/encapsulamento]]. Relacionado a [[wiki/concepts/hexagonal-architecture]] e [[wiki/concepts/contrato-de-api]].

## No JStack, aula 06

Em [[wiki/sources/jstack-controller-de-usuarios-e-sistema-de-rotas]], a primeira separação do projeto: `index.js` (servidor), `routes.js` (tabela de rotas), `controllers/UserController.js` (handlers) e `mocks/users.js` (dados). Falta separar a regra de negócio da camada HTTP ([[wiki/concepts/controller]]).

Em [[wiki/sources/frontpush-modules-js-import-export-default]], o motivo dos módulos é separar assuntos: "em um mesmo arquivo eu estou tratando de funções que são respectivas ao retângulo, outra de string, então eu não consigo organizar da melhor forma o meu código".

## Key sources

- [[wiki/sources/monolito-modular-transicao-mvp-empresa-madura]]
- [[wiki/sources/jstack-controller-de-usuarios-e-sistema-de-rotas]]: index, routes, controllers e mocks separados

## Key sources (adição 2026-10-05)

- [[wiki/sources/tres-tipos-de-acoplamento-que-impedem-teste-unitario-andre-casciotti]] — Misturar contexto de tecnologia (HTTP) com negócio via herança ou estático impede o teste ([[wiki/concepts/acoplamento-que-impede-teste-unitario]]).
- [[wiki/sources/frontpush-modules-js-import-export-default]]: FrontPUSH, JavaScript aula 17: um arquivo por assunto
