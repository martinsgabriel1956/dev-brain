---
type: entity
title: "Uncle Bob (Robert C. Martin)"
aliases: ["uncle bob", "robert c. martin", "robert cecil martin"]
date_created: 2026-07-03
date_updated: 2026-07-24
source_count: 4
tags: [clean-code, clean-architecture, solid, autor, quality-gate]
skill: tech-mentor-backend
status: stub
---

# Uncle Bob (Robert C. Martin)

Autor e figura conhecida da indústria de software, associado aos princípios de Clean Code, Clean Architecture e SOLID. Citado numa thread do Twitter reagindo a uma afirmação de que SQL nunca deveria ter sido incorporado a programas de computador — SQL teria sido pensado originalmente como linguagem de console para relatórios, não para uso embutido em aplicações.

## Contexto da Menção

Numa thread analisada em [[wiki/sources/sql-nao-e-banco-de-dados-uncle-bob]], Uncle Bob reage a uma afirmação (atribuída a outro "Bob" na thread) de que incorporar SQL em programas foi "um dos erros mais graves da nossa indústria". A discussão gerou confusão generalizada no Twitter, com muitos comentaristas comparando SQL a NoSQL — um eixo de discussão diferente do que estava sendo levantado (SQL embutido no código vs. abstraído por camadas como ORM/DSL).

**Nota de verificação**: a transcrição de origem não cita URL nem data da thread, e o autor da transcrição não confirma se o post referenciado ("Bob Tables: SQL is Demon Spawn...") é de fato de Robert C. Martin. Tratar a atribuição com cautela.

## Boy Scout Rule

Segunda menção, em [[wiki/sources/5-principios-que-mudaram-como-programador]]: Uncle Bob é creditado como quem popularizou a [[wiki/concepts/boy-scout-rule]] na comunidade de programação — a prática de deixar o código um pouco mais limpo a cada mudança feita numa base de código existente.

## Análise Estática no Pull Request como Não Negociável

Terceira menção, em [[wiki/sources/quality-gate-ratchet-multiplos-agentes-ia]]: citado via Twitter argumentando que programadores são lentos para escrever código, mas isso não é motivo para abrir mão de qualidade — a recomendação concreta atribuída a ele é colocar análise estática e análise de qualidade de código diretamente no fluxo de pull request. O autor da fonte credita essa citação como o gatilho direto que o levou a montar seu próprio [[wiki/concepts/quality-gate|quality gate]] com padrão [[wiki/concepts/ratchet-baseline|ratchet]].

## Objetos vs. Estruturas de Dados (Post de Blog)

Quarta menção, em [[wiki/sources/objetos-vs-estruturas-de-dados-clean-architecture]]: um post do blog de Uncle Bob, escrito em formato de diálogo, define **objeto** e **estrutura de dados** como conceitos literalmente opostos — objeto é um conjunto de funções que operam sobre dados implícitos/encapsulados; estrutura de dados é um conjunto de dados operados por funções implícitas/externas. A partir dessa definição, Uncle Bob argumenta que não existe mapeamento direto entre objetos e relações de banco de dados (só transferência de dados), e sugere que "Object-Relational Mapper" é um nome equivocado. Essa distinção é a base teórica de [[wiki/concepts/objeto-vs-estrutura-de-dados]], que por sua vez fundamenta como [[wiki/concepts/clean-architecture]] alterna entre objetos (Entities, Use Cases, Presenter) e estruturas de dados (Input/Output Data, ViewModel) no fluxo de uma aplicação web — diagrama descrito no livro *Clean Architecture* do próprio Uncle Bob.

**Nota de verificação**: assim como na menção sobre SQL, a transcrição de origem não cita o título exato nem a URL do post do blog — vale confirmar contra `blog.cleancoder.com` se a atribuição precisar ser usada como fonte primária.

## Key Sources

- [[wiki/sources/sql-nao-e-banco-de-dados-uncle-bob]]
- [[wiki/sources/5-principios-que-mudaram-como-programador]]
- [[wiki/sources/quality-gate-ratchet-multiplos-agentes-ia]] — citação sobre análise estática em PR como gatilho para o setup de quality gate do autor
- [[wiki/sources/objetos-vs-estruturas-de-dados-clean-architecture]] — post de blog sobre objeto vs. estrutura de dados, e diagrama de cenário web do livro *Clean Architecture*
