---
type: concept
title: "DDD — Domain-Driven Design"
aliases: ["domain-driven design", "ddd", "domínio"]
date_created: 2026-05-31
date_updated: 2026-08-17
source_count: 10
tags: [ddd, arquitetura, bounded-context, aggregate, domain-events, hexagonal]
skill: tech-mentor-backend
status: draft
---

# DDD — Domain-Driven Design

## TL;DR

Abordagem arquitetural que coloca o **domínio do negócio** no centro do design. O código deve espelhar o modelo mental dos especialistas do negócio. Conceitos centrais: Bounded Context, Aggregate, Domain Events, Ubiquitous Language.

## Pilares

- **Ubiquitous Language** — devs e negócio usam o mesmo vocabulário
- **Bounded Context** — fronteiras explícitas onde um modelo é válido
- **Aggregate** — unidade de consistência; processa commands, emite eventos
- **Domain Events** — fatos significativos que aconteceram no domínio
- **Repository** — abstração de persistência (domínio não conhece banco)

## Arquitetura Hexagonal + DDD

O domínio fica no centro, protegido de detalhes de infraestrutura:

```
[HTTP/gRPC Adapters]
        ↓
[Application Services]
        ↓
[Domain: Aggregates, Domain Events, Value Objects]  ← puro, sem I/O
        ↓
[Repository Interfaces] ← abstrações, não implementações
        ↓
[DB Adapters, Message Adapters]
```

[[efeitos-colaterais]] ficam nas bordas — o domínio é puro e testável.

## Conexão com Event Sourcing

DDD e [[event-sourcing]] são complementares: Domain Events (DDD) são exatamente os eventos persistidos em Event Sourcing. O Aggregate emite eventos que descrevem o que aconteceu; o Event Store os persiste.

[[wiki/sources/cqrs-e-event-sourcing-explicado-na-pratica]] reforça essa conexão pelo ângulo de estabilidade: a ação de domínio (ex.: "criar uma ordem com tais produtos") tende a mudar pouco ao longo do tempo mesmo quando a estrutura de persistência muda — reforça a tese de que o evento deve refletir a ação do domínio, não os detalhes de como ela é armazenada.

## Uso no Nubank

O [[nubank]] usa DDD como base para organizar o domínio financeiro — contas, transações, limites de crédito. A combinação DDD + [[programacao-funcional]] + [[event-sourcing]] permite que o codebase envelheça como vinho.

## Ubiquitous Language como Correção do Desalinhamento Dev-IA

[[wiki/sources/fundamentos-de-software-importam-mais-que-nunca-na-era-da-ia]] aplica o pilar Ubiquitous Language fora do contexto tradicional de DDD (dev ↔ especialista de domínio) para o contexto de dev ↔ IA: verborragia e desalinhamento entre plano e implementação são sintoma de que dev e IA não compartilham vocabulário. A prática descrita: extrair a terminologia de domínio já presente na base de código para um arquivo markdown com tabelas de termos, mantido aberto durante todo o planejamento com a IA. Relato do autor: isso reduziu a verbosidade dos "thinking traces" da IA e aumentou o alinhamento entre o que foi planejado e o que foi implementado — o mesmo mecanismo de "conversas, código e conversas com especialistas derivam do mesmo modelo" descrito no pilar acima, só que a IA ocupa o papel do "especialista" a ser alinhado.

## Value Object Precisa Ser Desembrulhado na Borda

Um Value Object (ex: `content` de uma `Notification`, validado e imutável no domínio) não é serializável diretamente para persistência ou banco — a conversão explícita (`notification.content.value`) fica a cargo do [[wiki/concepts/mapper-pattern]] na borda do domínio, não do Value Object em si. Isso mantém a regra "domínio não conhece infraestrutura" (ver seção "Arquitetura Hexagonal + DDD" acima) mesmo quando o dado que sai do domínio não é um primitivo.

## Especificação Agnóstica à Linguagem de Programação como Extensão de Ubiquitous Language

[[wiki/sources/rfcs-grill-me-e-o-risco-da-preguica-no-vibe-coding]] registra uma tese (atribuída a [[wiki/entities/fabricio-arcanjo]], discutida no Stubborn Club) que empurra o pilar Ubiquitous Language um passo além: especificações técnicas escritas para orientar agentes de IA deveriam ser **agnósticas à linguagem de programação**, focadas em DDD e padrões — documentando entradas/saídas rigorosamente em Markdown. A vantagem prática: com entradas e saídas bem definidas, a mesma especificação permite pedir a um agente que implemente (ou "transpile") a arquitetura em linguagens diferentes (Rust, .NET, Java, Go, TypeScript) sem perder a regra de negócio, reduzindo ambiguidade. É uma tese que gerou debate no grupo — o trade-off implícito é que abstrair a especificação da linguagem-alvo exige rigor extra na definição de contratos que, em uma especificação já acoplada a uma stack específica, muitas vezes fica implícito no próprio código.

## Bounded Context como Fronteira Social, não só Técnica

[[wiki/sources/application-boundary-martin-fowler]] — bliki entry de 2003, anterior à formalização de Bounded Context em *Domain-Driven Design* — chega ao mesmo problema por outra porta: onde termina uma "aplicação" não tem resposta puramente técnica, porque devs, negócio e quem controla o orçamento enxergam "uma unidade única" de formas diferentes e nem sempre alinhadas. O próprio Fowler aponta o strategic design de DDD como o desenvolvimento mais rigoroso dessa mesma questão. Ver [[wiki/concepts/application-boundary]] para o detalhamento das três lentes (código, funcionalidade, orçamento).

## Regra de Negócio do Domínio vs. da Aplicação

[[wiki/sources/arquitetura-limpa-na-pratica]] formaliza uma distinção que costuma ficar implícita: **regras de negócio do domínio** são dados e políticas que existiriam mesmo sem o sistema (ex: em um empréstimo — principal, taxa, período, e as operações de pagar/aplicar juros/cobrar multa) e pertencem à camada de Entidades; **regras de negócio da aplicação** descrevem *como o sistema automatiza* essas regras — os casos de uso — e são mais voláteis, podendo mudar de aplicação para aplicação mesmo dentro do mesmo domínio. A fronteira entre as duas é frequentemente uma decisão de projeto subjetiva, não uma classificação objetiva (ex: "usuário não pode ter duas notas com o mesmo título" pode legitimamente morar em Casos de Uso ou ser promovida para Entidades, dependendo de quão "fechada" se considera a regra).

## Pré-Requisito para Sharding de Sistemas Grandes

[[wiki/sources/sharding-charging-fragmentacao-banco-de-dados]] argumenta que tentar aplicar [[wiki/concepts/sharding]] diretamente a um monolito com centenas de tabelas não funciona — resulta em fragmentar poucas tabelas centrais e replicar dezenas de outras em todo shard. A ordem correta é primeiro usar DDD para decompor o sistema em bounded contexts/[[wiki/concepts/microsservicos]], e só então aplicar sharding no banco de um microsserviço específico, onde uma única entidade central (e portanto uma única shard key) faz sentido.

## Entidade Rica vs. Anêmica

No DDD, o agregado é responsável por proteger suas próprias invariantes — regras de negócio moram **dentro** da entidade, não em services externos. O oposto é o [[wiki/concepts/modelo-de-dominio-anemico]]: dados sem comportamento, um objeto que na verdade é uma estrutura de dados. [[wiki/sources/encapsulamento-proteger-estado-invalido]] demonstra a versão concreta disso em Java — pôr as validações (`price > 0`, `stock >= 0`) dentro dos métodos de comando da própria classe, via [[wiki/concepts/encapsulamento]], para que o objeto nunca entre em estado inválido.

## Key Sources

- [[wiki/sources/nubank-clojure-datomic-event-sourcing]]
- [[wiki/sources/encapsulamento-proteger-estado-invalido]] — entidade rica vs. anêmica na prática: invariantes protegidas dentro do objeto via encapsulamento
- [[wiki/sources/fundamentos-de-software-importam-mais-que-nunca-na-era-da-ia]]
- [[wiki/sources/rfcs-grill-me-e-o-risco-da-preguica-no-vibe-coding]] — especificações agnósticas à linguagem de programação (tese de Fabrício Arcanjo), transpilação de arquitetura entre stacks
- [[wiki/sources/mappers-conversao-entre-camadas]]
- [[wiki/sources/application-boundary-martin-fowler]] — application boundary como precursor social do bounded context
- [[wiki/sources/arquitetura-limpa-na-pratica]] — distinção formal entre regra de negócio do domínio (Entidades) e da aplicação (Casos de Uso), com exemplo de empréstimo de Robert Martin
- [[wiki/sources/sharding-charging-fragmentacao-banco-de-dados]] — DDD como pré-requisito para sharding de sistemas grandes; sem decomposição em bounded contexts não há uma única entidade/shard key candidata
- [[wiki/sources/cqrs-event-sourcing-full-cycle-wesley-williams]] — exemplo de agregado (ordem de serviço → pedido → cliente → indicação) usado para motivar a separação entre modelo de comando e modelo de leitura em [[wiki/concepts/cqrs]]
