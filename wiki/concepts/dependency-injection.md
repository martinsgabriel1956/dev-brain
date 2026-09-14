---
type: concept
title: "Dependency Injection"
aliases: ["DI", "injeção de dependência"]
date_created: 2026-08-04
date_updated: 2026-09-11
source_count: 7
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

[[wiki/sources/arquitetura-limpa-por-que-e-tao-popular]] nomeia o reverso da testabilidade: quando um componente recebe sua dependência via DI através de uma interface (ex.: um use case recebendo `UserRepository`), o ponto onde o componente é lido não revela qual implementação concreta está rodando — é preciso rastrear onde o componente foi instanciado (a [[wiki/concepts/composition-root|composition root]]) e qual implementação foi passada como parâmetro naquele ponto. Ganha-se substituibilidade e testabilidade, perde-se rastreabilidade direta na leitura do código.

## Quem faz a injeção: a Composition Root

[[wiki/sources/clean-architecture-frontend-vue-diagrama-camadas-login]] nomeia explicitamente quem cumpre esse papel numa arquitetura em camadas: uma camada própria (**Main**), implementada como uma [[wiki/concepts/factory-pattern|Factory]] (`LoginFactory`), que conhece todas as implementações concretas do sistema e as injeta no componente final. É o único ponto do sistema que se acopla a tudo — "sacrifício" deliberado para que as demais camadas fiquem desacopladas entre si. Ver [[wiki/concepts/composition-root]] para o conceito isolado.

## DI vs. Dependency Lookup como mecanismo de instalação de Test Double

[[wiki/sources/replace-dependency-with-test-double-xunitpatterns]] situa DI como um dos dois mecanismos possíveis para substituir uma dependência real por um [[wiki/concepts/test-doubles|Test Double]] num teste — o outro é [[wiki/concepts/dependency-lookup|Dependency Lookup]] (buscar a dependência via um registro/service locator). A fonte aponta DI como a opção preferida para **unit tests**, enquanto Dependency Lookup costuma funcionar melhor para **customer tests**, sem detalhar a causa raiz dessa preferência por nível de teste. Em linguagens estaticamente tipadas, essa substituição normalmente exige primeiro extrair uma interface da dependência real (refatoração **[[wiki/concepts/extract-interface|Extract Interface]]** [Fowler]), para que a variável injetada seja tipada pela interface, não pela classe concreta.

## Extract Interface: o mecanismo que viabiliza DI em linguagens estaticamente tipadas

[[wiki/sources/extract-interface-xunitpatterns]] fecha, com fonte primária dedicada (conteúdo atribuído a [[wiki/entities/martin-fowler|Fowler]], não a Meszaros), o mecanismo concreto por trás dessa exigência: uma variável tipada pela **classe concreta** de uma dependência real não aceita um Test Double no lugar, mesmo que o double implemente toda a API relevante — o compilador rejeita, porque o double não *é* aquela classe. Extraindo uma interface que cobre a API usada pelo SUT e retipando a variável para essa interface, tanto a implementação real quanto o double passam a satisfazer o mesmo tipo declarado. Ver [[wiki/concepts/extract-interface]].

## O termo guarda-chuva: substitutable dependency

[[wiki/sources/substitutable-dependency-xunitpatterns]] fecha, com fonte primária dedicada, o termo que nomeia a propriedade que DI provê: **substitutable dependency** (dependência substituível) — a capacidade de trocar o [[wiki/concepts/test-doubles|DOC]] real por um Test Double. DI é um dos três mecanismos formais catalogados por Meszaros para obter essa propriedade, ao lado de Dependency Lookup e do terceiro mecanismo revelado por essa fonte, [[wiki/concepts/test-specific-subclass|Test-Specific Subclass]] (sobrescrever, numa subclasse só de teste, o ponto do SUT onde a dependência real seria criada/obtida).

## Key Sources

- [[wiki/sources/tres-estagios-de-acoplamento-observer-pattern-na-pratica]] — DI citada como técnica que afrouxa mas não remove o acoplamento do segundo estágio; base de testes unitários e de integração
- [[wiki/sources/design-pattern-facade-codigo-fonte-tv]] — tensão entre DI completa e a simplicidade que o Facade deveria oferecer ao cliente
- [[wiki/sources/arquitetura-limpa-por-que-e-tao-popular]] — exemplo prático (`CreateUser`/`UserRepository`/`PostgresUserRepository`) e o custo de rastreabilidade na hora de debugar
- [[wiki/sources/replace-dependency-with-test-double-xunitpatterns]] — DI como mecanismo preferido para instalar Test Doubles em unit tests, em contraste com Dependency Lookup para customer tests
- [[wiki/sources/clean-architecture-frontend-vue-diagrama-camadas-login]] — camada Main/Factory (`LoginFactory`) como composition root concreto numa tela Vue.js
- [[wiki/sources/substitutable-dependency-xunitpatterns]] — fonte primária do termo guarda-chuva "substitutable dependency"; situa DI como um dos três mecanismos formais para obtê-la, ao lado de Dependency Lookup e Test-Specific Subclass
- [[wiki/sources/extract-interface-xunitpatterns]] — mecanismo concreto por trás do pré-requisito "Extract Interface" citado nas duas fontes acima: retipar a variável injetada para uma interface extraída, viabilizando a troca da implementação real por um Test Double sem alterar o SUT
