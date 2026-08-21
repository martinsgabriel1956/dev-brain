---
type: source
title: "Arquitetura Limpa: Por Que Ela É Tão Popular"
aliases: ["clean architecture por que é popular", "arquitetura limpa vs alternativas"]
date_created: 2026-08-19
date_updated: 2026-08-19
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/arquitetura-limpa-por-que-e-tao-popular.md
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-08-19
source_count: 0
tags: [clean-architecture, hexagonal-architecture, arquitetura-em-3-camadas, dependency-injection, over-engineering, uncle-bob, debugging, testabilidade]
skill: tech-mentor-backend
status: stable
---

## TL;DR

Transcrição de vídeo (pt-BR, colada pelo usuário no chat) explicando por que Clean Architecture é tão popular, com um exemplo de código prático (`CreateUser` use case + `User` entity + `UserRepository` interface + adapter Postgres) para demonstrar injeção de dependência e inversão de dependência na prática. Contrasta Clean Architecture com Hexagonal, Onion/Layered e DDD, e lista pontos fortes (testabilidade, independência de framework, lógica de negócio centralizada) e pontos fracos (boilerplate, risco de más abstrações, dificuldade de debugar, atrito com frameworks opinativos). Conclui que a popularidade da arquitetura vem menos de méritos técnicos exclusivos e mais da fama de Robert C. Martin (Uncle Bob).

## Key Claims

**Claim:** O nome "Arquitetura Limpa" é tendencioso — implica que as outras arquiteturas são "sujas" — mas codebases sem padrão nenhum, não só as que não usam Clean Architecture, é que degradam para código legado (lógica de negócio vazando para controllers/UI, entropia natural conforme o código passa de mão em mão).
**Evidence:** "o nome Arquitetura Limpa ele é pouco tendencioso porque o oposto disso deixa implícito que todas as outras são sujas né mas não é muito o caso [...] não é necessariamente culpa da empresa não é necessariamente culpa dos funcionários [...] é difícil segurar a entropia de uma code base."
**Confidence:** média — é uma opinião do autor sobre nomenclatura e cultura de engenharia, não uma claim técnica verificável.

**Claim:** O uso de injeção de dependência via interface (`UserRepository` como abstração entre `CreateUser` e `PostgresUserRepository`) evita que uma troca de banco de dados, ou uma mudança de caso de uso, exija alterar todos os casos de uso da aplicação — e é o que viabiliza testes com repositório mockado.
**Evidence:** Exemplo de código no vídeo: `CreateUser` depende só da interface `UserRepository` (método `save(user): void`), nunca de `PostgresUserRepository` diretamente; comparação explícita com a alternativa de instanciar o repositório com `new` dentro do use case, citada como "gambiarra" para testar.
**Confidence:** alta — consistente com o mecanismo já documentado em [[wiki/concepts/hexagonal-architecture]] (Port/Adapter) e [[wiki/concepts/dependency-injection]].

**Claim:** Clean Architecture e Hexagonal Architecture são, na prática, a mesma coisa com nomenclatura diferente — a única diferença citada é que Hexagonal fala em "domain" em vez de "entidades e use cases".
**Evidence:** "ela é bem parecida com hexagonal [...] a diferença é que o exagonal tem o tal do domain ao invés de entidades e use cases mas assim na prática as implementações vão ser muito parecidas."
**Confidence:** alta — reforça claim já registrada com mais detalhe em [[wiki/concepts/hexagonal-architecture]] (tabela de equivalência Port/Adapter ↔ Interface/Infra).

**Claim:** Onion/Layered architecture (citada como popular no NestJS) e Clean Architecture compartilham o mesmo princípio central — círculos concêntricos com dependências sempre apontando para dentro, em direção ao domínio — mudando pouco além da nomenclatura das camadas.
**Evidence:** "você tem também a onion ou arquitetura em layers [...] não é muito diferente da exagonal não é muito diferente da arquitetura limpa são círculos concêntricos em que as dependências sempre apontam para dentro."
**Confidence:** média — observação qualitativa do autor, sem comparação estrutural detalhada como a feita para Hexagonal.

**Claim:** A arquitetura "Layered" clássica (Presentation/Business/Data Access) tem menos abstrações que Clean Architecture, sendo mais rápida para aplicações CRUD simples, mas ainda mantém a lógica de negócio isolada do acesso a dados e a apresentação isolada de ambos — herdando a mesma lógica geral de separação de responsabilidades.
**Evidence:** "você tem um pouco menos de abstrações [...] acaba sendo um pouquinho mais simples um pouquinho mais rápido para aplicativos crude [...] business tá isolado de data access [...] e a apresentação costuma estar isolado de ambos."
**Confidence:** média — consistente com [[wiki/concepts/arquitetura-em-3-camadas]], mas essa página já documenta que a dependência da 3-tier vaza de forma transitiva; o vídeo não entra nesse detalhe de forma explícita ao descrever Layered.

**Claim:** Depurar código em Clean Architecture pode ser mais difícil porque a implementação concreta usada por um use case não está visível diretamente — é preciso rastrear onde o use case foi instanciado e qual adapter concreto foi passado como parâmetro para descobrir onde o método (ex.: `save`) está de fato implementado.
**Evidence:** "para debugar pode adicionar uma complexidade a mais devido a quantidade de níveis de abstrações que a gente tem [...] eu vou ter que descobrir que o repositório postgres foi passado e que é isso daqui que tá rodando de fato."
**Confidence:** alta — ponto específico e concreto, não coberto explicitamente ainda em [[wiki/concepts/clean-architecture]] nem em [[wiki/concepts/dependency-injection]] antes desta fonte.

**Claim:** Clean Architecture pode entrar em atrito com frameworks fortemente opinativos e orientados a MVC (Rails, Django, Laravel) — nesses casos, aplicar a arquitetura exige "lutar contra" os padrões do próprio framework.
**Evidence:** "ela pode brigar com convenções de frameworks se você pegar um framework com muitas opiniões tipo um Rails um jungle um laravel [...] às vezes você vai ver que para você fazer uma arquitetura limpa em jungle por exemplo você tem que brigar contra o jungle."
**Confidence:** média — observação qualitativa do autor, sem exemplo de código demonstrando o atrito.

**Claim:** A popularidade da Clean Architecture vem, em grande parte, não de méritos técnicos exclusivos frente às alternativas (Hexagonal, Onion, Layered, DDD), mas da fama de Robert C. Martin (Uncle Bob) como autor e divulgador.
**Evidence:** "eu acho que ela ficou muito popular na verdade não necessariamente pelos méritos ou deméritos dela [...] eu acho que ela ficou realmente muito popular por causa do livro do Robert C Martin por causa do Uncle Bob [...] porque o Uncle Bob é alguém muito popular e popularizou ainda mais essa arquitetura."
**Confidence:** baixa — opinião pessoal explícita do autor ("eu acho"), não uma claim factual verificável.

## Entities & Concepts Touched

- [[wiki/concepts/clean-architecture]]
- [[wiki/concepts/hexagonal-architecture]]
- [[wiki/concepts/arquitetura-em-3-camadas]]
- [[wiki/concepts/dependency-injection]]
- [[wiki/concepts/over-engineering]]
- [[wiki/concepts/ddd]]

## Open Questions

- Autor/canal não identificado explicitamente na transcrição (só a menção a uma ferramenta de IA patrocinadora, sem relevância técnica) — tratado como fonte sem entidade de autoria, sem forçar link.
- A claim sobre atrito entre Clean Architecture e frameworks opinativos (Rails/Django/Laravel) não vem acompanhada de exemplo concreto — candidata a aprofundamento numa fonte futura dedicada a esse trade-off.
- A comparação entre Onion e Clean Architecture é mais superficial que a comparação com Hexagonal (que já tinha uma fonte dedicada e detalhada); não há página própria para Onion Architecture na wiki ainda — se uma fonte futura aprofundar essa arquitetura especificamente, criar `wiki/concepts/onion-architecture.md`.
