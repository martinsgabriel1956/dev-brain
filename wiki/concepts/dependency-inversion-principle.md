---
type: concept
title: "Dependency Inversion Principle (DIP)"
aliases: ["DIP", "dependency inversion", "inversão de dependência"]
date_created: 2026-08-06
date_updated: 2026-08-06
source_count: 2
tags: [solid, oop, architecture, dependency-injection]
skill: tech-mentor-backend
status: stub
---

## Definição

Um módulo não deve depender diretamente de detalhes de implementação de outro módulo — deve existir uma abstração (interface) entre eles. Módulos de alto nível e módulos de baixo nível dependem ambos da abstração, não um do outro diretamente.

## Exemplo

Um robô com o braço fundido a uma faca de cortar pizza ("mãos de tesoura") não pode trocar de ferramenta — viola DIP. A versão correta dá ao robô um "soquete" (interface): qualquer ferramenta injetada que respeite esse soquete pode ser usada para cortar a pizza, sem o robô conhecer os detalhes da ferramenta.

## Relação com Open/Closed e Liskov Substitution

Segundo [[wiki/sources/principios-solid-ilustrados]], Robert C. Martin descreveu que o uso rigoroso conjunto de [[wiki/concepts/open-closed-principle|OCP]] e [[wiki/concepts/liskov-substitution-principle|LSP]] pode ser generalizado neste princípio à parte — DIP é o "efeito dominó" final dos outros quatro. Essa atribuição específica ao paper de 1996 ainda não foi cross-checada com a fonte primária (ver perguntas abertas na source).

Aplicação prática comum: injeção de dependência — a classe de alto nível recebe a implementação concreta (já atrás de uma interface) via construtor ou setter, em vez de instanciá-la diretamente.

## Implicação Arquitetural [skill: tech-mentor-backend]

Em Clean Architecture, é o que torna o domínio testável e substituível: o domínio define as interfaces (`IEmailService`, `IOrderRepository`), e a camada de infraestrutura as implementa — nunca o contrário. É o mesmo princípio que permite `PostgresOrderRepository` e `InMemoryOrderRepository` serem intercambiáveis em teste (ver também [[wiki/concepts/liskov-substitution-principle|LSP]], do qual essa intercambialidade depende).

## Definição Formal e Vocabulário (Fonte Primária)

Via [[wiki/sources/solid-principles-in-pictures-ugonna-thelma]]: "módulos de alto nível não deveriam depender de módulos de baixo nível — ambos deveriam depender da abstração." A autora define quatro termos com mais precisão que a ilustração do "soquete" usada em [[wiki/sources/principios-solid-ilustrados]]:

- **Módulo de alto nível**: a classe que executa uma ação usando uma ferramenta.
- **Módulo de baixo nível**: a própria ferramenta.
- **Abstração**: a interface que conecta as duas classes.
- **Detalhes**: como a ferramenta funciona por dentro.

## Key Sources

- [[wiki/sources/principios-solid-ilustrados]]
- [[wiki/sources/solid-principles-in-pictures-ugonna-thelma]]
