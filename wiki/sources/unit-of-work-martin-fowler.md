---
type: source
title: "Unit of Work (eaaCatalog, Martin Fowler)"
aliases: ["unitOfWork.html", "unit of work catalog entry"]
date_created: 2026-08-19
date_updated: 2026-08-19
source_file: "raw/unit-of-work-martin-fowler.md"
source_url: "https://martinfowler.com/eaaCatalog/unitOfWork.html"
author: "Martin Fowler"
date_published: "2003-03-05"
date_ingested: 2026-08-19
source_count: 0
tags: [unit-of-work, design-patterns, poeaa, martin-fowler, catalog-entry]
skill: tech-mentor-backend
status: stable
---

## TL;DR

Página curta do catálogo online de *Patterns of Enterprise Application Architecture* (eaaCatalog) que define Unit of Work na fonte primária: "mantém uma lista de objetos afetados por uma transação de negócio e coordena a escrita das alterações e a resolução de problemas de concorrência". O problema que o padrão resolve é dado em duas frases: sem rastrear o que foi alterado, os dados não voltam para o banco; e a alternativa ingênua — escrever no banco a cada modificação de objeto — gera excesso de pequenas chamadas ao banco (problema de performance) e exigiria janelas de transação impraticavelmente longas abertas por múltiplos requests. A página é apenas o resumo do padrão no catálogo — remete ao Capítulo 11 do ebook para o detalhamento completo (não lido nesta ingestão). Não traz exemplo de código; a mecânica concreta (classe com listas de novo/sujo/removido, `commit`, exemplo real com SQLAlchemy incluindo `flush` vs. `commit` e rollback) já está registrada em [[wiki/sources/unit-of-work-padrao-de-design]] e em [[wiki/concepts/unit-of-work]].

## Key Claims

**Claim:** Sem um mecanismo de rastreamento, alterações feitas em objetos em memória durante uma transação de negócio simplesmente não são persistidas.
**Evidence:** "it's important to keep track of what you've changed; otherwise, that data won't be written back into the database" — mesma lógica vale para inserção de objetos novos e remoção de objetos excluídos, não só updates.
**Confidence:** alta — definição textual da fonte primária do padrão.

**Claim:** A alternativa a Unit of Work — persistir cada modificação individualmente, assim que ocorre — tem dois problemas distintos: performance (muitas chamadas pequenas ao banco) e viabilidade transacional (transações não podem razoavelmente durar múltiplos requests).
**Evidence:** Citado como os dois "key challenges" que motivam o padrão no resumo do catálogo.
**Confidence:** alta, mas a página não detalha o *porquê* de cada um (ex: não explica que leitura inconsistente é resolvida rastreando objetos já acessados) — esse nível de detalhe fica implícito, só nomeado como terceiro desafio ("avoiding inconsistent reads requires tracking previously accessed objects").
**Confidence:** média para esse terceiro ponto especificamente — mencionado em uma linha, sem elaboração.

**Claim:** Unit of Work resolve dois problemas ao mesmo tempo: coordenar a escrita das mudanças acumuladas *e* a resolução de problemas de concorrência.
**Evidence:** É a segunda metade da definição formal do padrão ("...coordinates the writing out of changes and the resolution of concurrency problems"). Esse segundo aspecto (concorrência) não é aprofundado nesta página — é o mesmo ponto que [[wiki/concepts/repository-pattern]] já registrava como limitação de repositórios simples resolvida por Unit of Work, via [[wiki/sources/arquitetura-limpa-na-pratica]].
**Confidence:** alta quanto à afirmação em si (é a definição do autor do padrão); a mecânica de *como* Unit of Work resolve concorrência não está nesta página — só no Capítulo 11 do livro, não lido aqui.

## Entities & Concepts Touched

- [[wiki/concepts/unit-of-work]]
- [[wiki/entities/martin-fowler]]
- [[wiki/concepts/repository-pattern]]
- [[wiki/sources/unit-of-work-padrao-de-design]] — fonte-irmã com a mecânica completa e exemplo de código

## Open Questions

- **Capítulo 11 do livro não foi lido** — a página do catálogo é apenas o resumo; a mecânica de resolução de concorrência (a parte da definição que esta página não detalha) provavelmente está lá, não nesta ingestão.
- **Terceiro desafio ("avoiding inconsistent reads requires tracking previously accessed objects") citado em uma linha, sem exemplo** — candidato a aprofundar se outra fonte primária (ex: o próprio livro) for ingerida no futuro.
