---
type: entity
title: "Uncle Bob (Robert C. Martin)"
aliases: ["uncle bob", "robert c. martin", "robert cecil martin"]
date_created: 2026-07-03
date_updated: 2026-07-19
source_count: 3
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

## Key Sources

- [[wiki/sources/sql-nao-e-banco-de-dados-uncle-bob]]
- [[wiki/sources/5-principios-que-mudaram-como-programador]]
- [[wiki/sources/quality-gate-ratchet-multiplos-agentes-ia]] — citação sobre análise estática em PR como gatilho para o setup de quality gate do autor
