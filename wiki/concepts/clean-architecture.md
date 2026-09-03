---
type: concept
title: "Clean Architecture"
aliases: ["arquitetura limpa", "clean arch"]
date_created: 2026-07-24
date_updated: 2026-09-01
source_count: 9
tags: [clean-architecture, uncle-bob, dependency-inversion, use-case, presenter, view-model, arquitetura, dci, bce]
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

## Por que "domain-centric" — contraste com 3-tier

Comparando com a [[wiki/concepts/arquitetura-em-3-camadas]] tradicional, fica claro o porquê do nome: na 3-tier, a presentation layer depende da business layer, que depende diretamente da data access layer — toda a cadeia de dependência aponta "para baixo", em direção ao banco. Com o tempo, isso tende a misturar lógica de negócio com lógica de acesso a dados, e o acoplamento acaba vazando até a presentation layer.

Na Clean Architecture, a lógica de negócio que ficava numa única business layer se divide em duas: **Application** (use cases, ex.: `SetReminder`, `DismissReminder`) e **Domain** (entidades como `User`/`Reminder` e as regras de negócio, ex.: checar o plano do usuário antes de criar um lembrete). O banco de dados deixa de estar "embaixo" recebendo dependências e passa a viver na **infrastructure layer**, uma camada externa — todas as dependências apontam para dentro, em direção ao domínio.

## Quando vale o investimento

Sistemas com lógica de negócio complexa que vai mudar ao longo do tempo. Para CRUDs simples, a quantidade de camadas e interfaces é over-engineering — ver [[wiki/concepts/over-engineering]].

## Genealogia: síntese de três arquiteturas anteriores

Segundo o próprio Robert Martin (citado em [[wiki/sources/arquitetura-limpa-na-pratica]]), a Clean Architecture é "uma tentativa de integrar várias arquiteturas desenvolvidas nas últimas décadas em uma ideia prática" — ver [[wiki/concepts/dci-e-bce]] para o detalhamento das três: [[wiki/concepts/hexagonal-architecture]] (Cockburn), DCI/Data-Context-Interaction (Reenskaug e Coplien) e BCE/Boundary-Control-Entity (Jacobson). As cinco camadas do estudo de caso do livro (Entidades, Casos de Uso, Adaptadores de Interface, Frameworks & Drivers, e uma quinta camada — Principal & Configuração — que o autor adiciona por conta própria para módulos de composição/injeção de dependência) mapeiam diretamente para o diagrama de círculos concêntricos e a Regra de Dependência descritos acima.

## Dificuldade de Debugar: Implementação Concreta Fica "Escondida"

[[wiki/sources/arquitetura-limpa-por-que-e-tao-popular]] nomeia um custo concreto da Regra de Dependência que costuma ficar implícito: como o use case depende só da interface (ex.: `UserRepository`), a implementação concreta que roda de fato (ex.: `PostgresUserRepository`) não fica visível no ponto onde o use case é lido — é preciso rastrear onde o use case foi instanciado (a composition root) e qual adapter concreto foi injetado ali para descobrir onde o método (`save`) está realmente implementado. É o reverso da mesma moeda que dá testabilidade: a indireção que permite trocar o Postgres por um mock também exige um salto a mais para achar o código que roda em produção.

## Boilerplate e Risco de Más Abstrações

A mesma fonte também nomeia o principal custo de adoção: um exemplo mínimo (`User`, `CreateUser`, `UserRepository`, `PostgresUserRepository`) já exige quatro arquivos/pastas para algo que poderia ser resolvido em quatro ou cinco linhas sem a arquitetura. Como criar boas abstrações é uma das partes mais difíceis do trabalho de um desenvolvedor, quanto mais abstrações a arquitetura exige, maior a chance de que algumas delas sejam más abstrações — o setup inicial só se paga se o projeto durar tempo suficiente (a fonte cita "meses" como possivelmente insuficiente, "anos" como cenário onde a manutenibilidade compensa) e se a regra de negócio efetivamente não vazar para outras camadas.

## Atrito com Frameworks Opinativos

Frameworks fortemente opinativos e orientados a MVC (Rails, Django, Laravel) podem entrar em atrito direto com a Regra de Dependência — nesses casos, aplicar Clean Architecture exige "lutar contra" as convenções que o próprio framework já prescreve, em vez de simplesmente segui-las. Ver [[wiki/sources/arquitetura-limpa-por-que-e-tao-popular]].

## Popularidade Não é Só Mérito Técnico

A mesma fonte propõe uma leitura cultural, não técnica: Clean Architecture não seria necessariamente superior a Hexagonal, Onion/Layered ou DDD nos méritos — cada uma é adequada a tipos de projeto diferentes. A popularidade desproporcional de Clean Architecture é atribuída, em boa parte, à fama de Robert C. Martin (Uncle Bob) como autor e divulgador, mais do que a uma vantagem técnica exclusiva sobre as arquiteturas concorrentes. Marcado como opinião do autor da fonte, não como claim factual.

## Uso em produção: Netflix, Uber, iFood

[[wiki/sources/arquitetura-limpa-na-pratica]] documenta casos de adoção real: a Netflix trocou a fonte de dados de uma API de JSON para GraphQL em ~2 horas graças a repositórios abstraídos por interface (Arquitetura Hexagonal); a Uber descreve sua "Domain-Oriented Microservices Architecture" (DOMA) como baseada em DDD e Clean Architecture — ambos com posts de engenharia públicos como fonte. Relatos sobre iFood, Amazon, Mercado Livre e Nubank são anedóticos (conversas pessoais do autor do livro), com confiança mais baixa.

## Either monad para tratamento de erros

No estudo de caso do livro, erros esperados (email inválido, usuário já existente) são tratados retornando um tipo `Either<Erro, Sucesso>` (implementado com classes `Left`/`Right`) em vez de lançar exceções — reservando `try-catch` só para o nível mais externo (`WebController`, middleware). A justificativa citada é a mesma usada em *Object Design* (Wirfs-Brock et al.): preferir retornar o erro a lançá-lo, quando o erro é uma condição prevista do domínio.

## Métricas por trás da Regra de Dependência

As métricas de pacote de Robert Martin — abstração `A`, instabilidade `I = Ce/(Ca+Ce)` e distância da sequência principal `D = |A + I − 1|` — são a formalização quantitativa da própria Regra de Dependência: componentes estáveis (I baixo) devem ser abstratos (A alto) para poderem ser dependidos sem impedir a evolução; componentes voláteis (I alto) devem ser concretos. Ver [[wiki/concepts/metricas-de-acoplamento]] e [[wiki/sources/medindo-e-entendendo-acoplamento-matheus-castiglioni]].

## Gráfico de Complexidade-Versus-Tempo Citado Fora de Contexto de Código: Justificativa de Harness Engineering

[[wiki/sources/prompt-context-harness-engineering-tres-pilares]] cita o gráfico de complexidade crescente ao longo do tempo do livro Clean Architecture — sem detalhar o gráfico especificamente, apenas de memória — como argumento para uma tese fora do escopo usual desta página: a complexidade de software cresce com ou sem IA, e o [[wiki/concepts/harness|harness]] (regras, guidelines, mecanismos de verificação) é o que, na era de agentes, cumpre o mesmo papel que "ter uma boa arquitetura" sempre cumpriu — manter essa complexidade sob controle. Claim de baixa especificidade (não aponta capítulo/página do livro), mas é o primeiro cruzamento na wiki entre esse gráfico específico e a motivação de harness engineering.

## Clean Architecture como Base de um Módulo em Arquitetura Modular

[[wiki/sources/tres-tipos-de-modulos-arquitetura-modular-valdemar-neto]] mapeia o vocabulário de Clean Architecture (Use Cases, Entities) para dentro de um único módulo de [[wiki/concepts/monolito-modular|monolito modular]]: Use Cases/Entities formam o **Core** (lógica de negócio); Controllers/repositórios formam a camada de **Supporting Infrastructure**, com conhecimento específico do contexto de domínio (por isso não totalmente compartilhável); e uma terceira camada, **Infraestrutura Pura** (lib de banco, logger, config), fica de fora do módulo e é compartilhada entre módulos diferentes. A tese da fonte: Clean Architecture isola bem o domínio do mundo externo, mas não trata de como reusar infraestrutura *entre* módulos/contextos nem de rodar módulos em processos separados — lacuna que a [[wiki/concepts/arquitetura-modular|arquitetura modular]] cobre. Ver taxonomia completa em [[wiki/concepts/tipos-de-modulos]].

## Key Sources

- [[wiki/sources/tres-tipos-de-modulos-arquitetura-modular-valdemar-neto]] — mapeamento de Use Cases/Entities para a camada "Core" de um módulo; lacuna de reuso de infraestrutura entre módulos que a arquitetura modular cobre
- [[wiki/sources/prompt-context-harness-engineering-tres-pilares]] — gráfico de complexidade-versus-tempo citado como justificativa para harness engineering, fora do escopo usual de Clean Architecture como estilo de código
- [[wiki/sources/medindo-e-entendendo-acoplamento-matheus-castiglioni]] — métricas de acoplamento (A, I, D) como formalização da Regra de Dependência
- [[wiki/sources/presenters]] — papel do Presenter e ViewModel especificamente na camada HTTP/apresentação (REST, GraphQL, CLI)
- [[wiki/sources/objetos-vs-estruturas-de-dados-clean-architecture]] — fluxo completo do diagrama de cenário web, e a justificativa teórica (objeto vs. estrutura de dados) por trás de cada camada
- [[wiki/sources/classes-vs-estruturas-de-dados-uncle-bob]] — post original de Uncle Bob (fonte primária): mesma justificativa teórica, com o argumento adicional de que interfaces de fronteira (Input/Output Boundary) invertem a direção da dependência de código-fonte, isolando cada camada de recompilação em cascata
- [[wiki/sources/clean-architecture-arquitetura-centrada-no-dominio]] — comparação direta com a arquitetura em 3 camadas, explicando a origem do nome "domain-centric"
- [[wiki/sources/arquitetura-limpa-na-pratica]] — estudo de caso completo em TypeScript (theWisePad), genealogia DCI/BCE/Hexagonal, casos reais de adoção (Netflix, Uber, iFood), e o padrão Either para tratamento de erros
- [[wiki/sources/arquitetura-limpa-por-que-e-tao-popular]] — exemplo prático de DI (`CreateUser`/`UserRepository`/adapter Postgres), custo de debugar implementação "escondida" atrás da interface, boilerplate, atrito com frameworks opinativos, e leitura de que a popularidade vem mais da fama de Uncle Bob que de mérito técnico exclusivo
