---
type: concept
title: "Clean Architecture"
aliases: ["arquitetura limpa", "clean arch"]
date_created: 2026-07-24
date_updated: 2026-07-24
source_count: 2
tags: [clean-architecture, uncle-bob, dependency-inversion, use-case, presenter, view-model, arquitetura]
skill: tech-mentor-backend
status: draft
---

# Clean Architecture

Estilo arquitetural de Robert C. Martin (Uncle Bob) organizado em camadas concêntricas, com uma regra de dependência única: **dependências sempre apontam para dentro** — o domínio nunca conhece detalhes de infraestrutura (framework, banco, HTTP).

```
Domínio (Entities) → Use Cases → Interface Adapters → Frameworks/DB/HTTP
```

Ver [[wiki/concepts/hexagonal-architecture]] para a variação de Alistair Cockburn (Ports & Adapters) — a diferença é de nomenclatura, o princípio de isolamento é o mesmo.

## Cenário típico numa aplicação web

O livro *Clean Architecture* descreve um fluxo concreto de requisição numa aplicação web, alternando entre **objetos** (comportamento) e **estruturas de dados** (transporte puro, sem lógica) — ver [[wiki/concepts/objeto-vs-estrutura-de-dados]] para a distinção completa entre os dois.

1. O **servidor web** recebe a entrada do usuário e repassa ao **Controller**.
2. O **Controller** empacota a entrada numa estrutura de dados (**Input Data**) — só dados simples (strings, números).
3. O Input Data atravessa uma interface, o **Input Boundary**, até o **Use Case**. Essa interface existe só para permitir **inversão de dependência**: o Use Case não depende do Controller — os dois dependem da mesma abstração (também chamada de "protocolo").
4. O **Use Case** (objeto, com comportamento de aplicação) interpreta os dados e orquestra as **Entities** (objetos, comportamento de domínio).
5. O Use Case acessa o banco via uma **Data Access interface**; um **Data Mapper** transfere os dados brutos do banco para dentro das Entities — ver [[wiki/concepts/mapper-pattern]] e [[wiki/concepts/repository-pattern]].
6. Ao concluir, o Use Case monta um **Output Data** (estrutura de dados — pode conter tipos de domínio como `Date` ou Value Objects de dinheiro) e o entrega via **Output Boundary** (outra interface de inversão de dependência) ao **Presenter**.
7. O **Presenter** (objeto) reempacota o Output Data num **ViewModel** — estrutura de dados ainda mais simples, só strings e flags.
8. A **View** apenas despeja o ViewModel numa página HTML — não formata nada, não decide nada.

### Objetos vs. estruturas de dados no fluxo

| Peça | Tipo | Função |
|---|---|---|
| Input Data | Estrutura de dados | Entrada empacotada pelo Controller |
| Input Boundary | Interface | Inversão de dependência Controller ↔ Use Case |
| Use Case | Objeto | Orquestra Entities, lógica de aplicação |
| Entities | Objeto | Comportamento e regra de negócio do domínio |
| Data Access interface | Interface | Inversão de dependência Use Case ↔ persistência |
| Output Data | Estrutura de dados | Saída do Use Case, pode carregar tipos de domínio |
| Output Boundary | Interface | Inversão de dependência Use Case ↔ Presenter |
| Presenter | Objeto | Reempacota Output Data em ViewModel |
| ViewModel | Estrutura de dados | Só strings/flags, pronto para a View exibir |

Nomear essas interfaces de fronteira como "protocolo" é o mesmo mecanismo de [[wiki/concepts/adapter-pattern|inversão de dependência via polimorfismo]] usado no vocabulário de Ports & Adapters em [[wiki/concepts/hexagonal-architecture]].

## Quando vale o investimento

Sistemas com lógica de negócio complexa que vai mudar ao longo do tempo. Para CRUDs simples, a quantidade de camadas e interfaces é over-engineering — ver [[wiki/concepts/over-engineering]].

## Key Sources

- [[wiki/sources/presenters]] — papel do Presenter e ViewModel especificamente na camada HTTP/apresentação (REST, GraphQL, CLI)
- [[wiki/sources/objetos-vs-estruturas-de-dados-clean-architecture]] — fluxo completo do diagrama de cenário web, e a justificativa teórica (objeto vs. estrutura de dados) por trás de cada camada
