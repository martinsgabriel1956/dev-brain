---
type: concept
title: "Interface Segregation Principle (ISP)"
aliases: ["ISP", "interface segregation", "segregação de interface"]
date_created: 2026-08-06
date_updated: 2026-09-08
source_count: 3
tags: [solid, oop, architecture]
skill: tech-mentor-backend
status: stub
---

## Definição

Clientes não devem ser forçados a depender de métodos que não usam. Uma interface "gorda" com métodos que só fazem sentido para alguns implementadores deve ser quebrada em interfaces menores e mais específicas.

## Exemplo

Duas interfaces de robô, uma delas sem antena, forçadas a compartilhar um contrato único (`girar()`, `rotacionarBraços()`, `mexerAntena()`). O robô sem antena acaba com uma implementação vazia ou que lança exceção. A correção é segregar em interfaces menores — `Girável`, `RotacionávelDeBraços`, `ComAntena` — e cada robô implementa só o que faz sentido para ele.

## Relação com os outros princípios SOLID

Leitura comum: ISP é [[wiki/concepts/single-responsibility-principle|SRP]] + [[wiki/concepts/open-closed-principle|OCP]] + [[wiki/concepts/liskov-substitution-principle|LSP]] aplicados especificamente ao nível de interface, em vez de classe.

## Implicação Arquitetural [skill: tech-mentor-backend]

Em nível de sistema (não só de classe), ISP aparece como o motivo para APIs retornarem só o que o cliente precisa — BFF, GraphQL com resolução seletiva de campos — em vez de um contrato único de 40 campos quando um consumidor específico usa 5. Uma "god interface" em nível de API tem o mesmo efeito que em nível de classe: força todo consumidor a lidar com um contrato maior do que precisa.

## Definição Formal (Fonte Primária)

Via [[wiki/sources/solid-principles-in-pictures-ugonna-thelma]]: "clientes não deveriam ser forçados a depender de métodos que não usam" — o princípio divide um conjunto grande de ações em subconjuntos menores, para que cada classe implemente só o que de fato usa.

## Cliente HTTP "Gordo": get/post/put/delete numa Interface Só

[[wiki/sources/clean-architecture-frontend-vue-diagrama-camadas-login]] dá um exemplo de ISP aplicado a um cliente HTTP: é comum criar uma única interface `HttpClient` com `get`, `post`, `put`, `delete`, já que é tudo que um cliente HTTP pode fazer. Mas se `RemoteAuthentication` só precisa de `post`, essa interface gorda obriga (1) qualquer implementação concreta a implementar os quatro métodos mesmo quando só um é usado, e (2) qualquer implementação de teste (fake/stub) a fazer o mesmo, mesmo quando o teste só precisa validar o `post`. A correção é segregar por operação — `HttpPostClient` só com `post` — e cada caso de uso depende só do subconjunto que de fato usa. Citado na fonte como exemplo a ser aprofundado quando o cliente Axios for implementado em código, mais adiante no mesmo curso.

## Key Sources

- [[wiki/sources/principios-solid-ilustrados]]
- [[wiki/sources/solid-principles-in-pictures-ugonna-thelma]]
- [[wiki/sources/clean-architecture-frontend-vue-diagrama-camadas-login]] — `HttpClient` (get/post/put/delete) segregado em `HttpPostClient`, evitando implementações/mocks de métodos não usados
