---
date: 2026-07-30
tags: [tech-mentor, arquitetura, clean-architecture, 3-tier, domain-centric]
skill: tech-mentor-system-design/references/architecture-patterns
level: intermediário
---
# Clean Architecture: Arquitetura Centrada no Domínio

## Contexto

Clean Architecture é um padrão arquitetural que coloca o foco no domínio — por isso é chamada de arquitetura **domain-centric** (centrada no domínio). O sistema é composto por vários componentes lógicos com interações bem definidas entre si.

Para entender o que significa "centrada no domínio", vale comparar a **arquitetura em 3 camadas (3-tier)** com a **Clean Architecture**, usando como exemplo uma aplicação de lembretes (reminders) com uma API que permite criar, deletar e buscar lembretes. Regra de negócio do exemplo: no plano básico o usuário pode criar até 3 lembretes diários; para lembretes ilimitados, é preciso assinar um plano pago.

## Como Funciona

### Arquitetura em 3 camadas (3-tier)

O cliente/usuário interage com a **camada de apresentação** (presentation layer), responsável pela interação com o mundo externo — é onde ficam os controllers de uma REST API, ou o equivalente para GraphQL, gRPC ou uma SPA.

Ao criar um lembrete, a lógica de negócio (ex.: verificar se o usuário atingiu o limite do plano) fica na **camada de negócio** (business layer). Essa camada tem uma dependência direta da **camada de acesso a dados** (data access layer) — normalmente implementada como projetos separados com referências entre si, onde os símbolos da business layer acessam diretamente os símbolos da data access layer.

Problemas dessa estrutura:
- Com o tempo, a lógica de negócio tende a se misturar com a lógica de acesso a dados.
- Como a presentation layer depende da business layer, e essa depende da data access layer, a dependência se torna transitiva — lógica de acesso a dados frequentemente vaza para a presentation layer.

### Clean Architecture

Na Clean Architecture, a lógica de negócio deixa de estar em uma única camada e se divide em duas:

- **Application layer**: contém os *use cases* (casos de uso) do sistema — `SetReminder`, `DismissReminder`, `DeleteReminder`. É responsável por orquestrar os objetos de domínio (ex.: adicionar um objeto `Reminder` ao objeto `User`).
- **Domain layer**: contém a definição dos objetos de domínio (`Reminder`, `User`) e as regras de negócio propriamente ditas (ex.: um `if` que verifica o tipo de plano do usuário antes de permitir criar um novo lembrete).

Diferente da arquitetura em camadas, o banco de dados não fica "embaixo" recebendo todas as dependências apontando para ele. Em vez disso, as preocupações de banco de dados, sistema de arquivos, relógio do sistema etc. ficam na **infrastructure layer**, e todas as dependências apontam **para dentro**, em direção ao domínio — daí o nome "arquitetura centrada no domínio".

### A Dependency Rule na prática

Pergunta natural: se nada depende da infraestrutura, como o domínio ou os use cases acessam o banco de dados?

Resposta: **as camadas internas definem interfaces; as camadas externas implementam essas interfaces.**

- A *application layer* define uma interface para o que precisa do banco (ex.: um método de persistência necessário a um use case).
- A implementação concreta dessa interface fica na *infrastructure layer*.

Esse é o mesmo princípio que permite trocar a tecnologia de uma camada externa (ex.: trocar REST por uma GUI) sem afetar a lógica de negócio interna — a camada externa apenas passa a chamar a lógica de negócio de outra forma.

### Estrutura completa de uma solução

- **Presentation layer**: controllers, definição da API.
- **Application layer**: use cases (`SetReminder`, `DismissReminder`, etc.). Quando um use case precisa de algo do banco, ele adiciona um método à interface — a implementação fica abstraída na infrastructure layer.
- **Domain layer**: objetos (`User`, `Reminder`) e regras de negócio (ex.: checar o tipo de plano antes de criar o lembrete).
- **Infrastructure layer**: implementação de acesso a banco de dados e outras preocupações de infraestrutura (sistema de arquivos, relógio do sistema, etc.).

## Observação

O vídeo original é material promocional de um curso ("Getting Started with Clean Architecture"), cobrindo padrões correlatos como Repository, Unit of Work, Mediator e Result. Essa parte promocional foi omitida aqui por não ser conteúdo técnico.
