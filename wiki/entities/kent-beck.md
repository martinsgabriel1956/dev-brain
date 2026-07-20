---
type: entity
title: "Kent Beck"
aliases: ["kent beck"]
date_created: 2026-07-09
date_updated: 2026-07-19
source_count: 4
tags: [autor, tdd, extreme-programming, design-incremental, junit, xunit, yagni]
skill: tech-mentor-testing
status: stub
---

## Quem É

Criador do TDD (Test-Driven Development) moderno e da Extreme Programming (XP), coautor do Manifesto Ágil. Autor de *Test Driven Development: By Example* e *Tidy First?*.

## Criador do framework original e coautor do JUnit

Antes do TDD ser formalizado como prática, Beck já construía frameworks de teste caseiros em Smalltalk — usados por ele e clientes num ciclo de edição-e-teste rápido dentro da própria IDE. Preferia que cada time reconstruísse o próprio framework (levava poucas horas) em vez de compartilhar um único — um exemplo do que Fowler chamaria de [[wiki/concepts/seedwork|Seedwork]]. Esse framework foi usado no projeto [[wiki/entities/c3-project|C3]] (Chrysler, 1996), o "projeto de nascimento" da Extreme Programming, onde Ron Jeffries também foi apresentado a ele.

Em 1997, num voo de Zurique para a OOPSLA em Atlanta, Beck programou em par com [[wiki/entities/gang-of-four|Erich Gamma]] a primeira versão do [[wiki/entities/junit]] — feita test-first. JUnit se tornou o membro fundador da família de frameworks "Xunit" e, segundo Fowler, foi essencial para sustentar o crescimento de XP e TDD na indústria. Ver [[wiki/sources/xunit-martin-fowler]].

## Contribuições relevantes para o wiki

**TDD (RED-GREEN-REFACTOR):** ver [[wiki/concepts/tdd]] — a prática de escrever o teste antes do código de produção, com foco em sentir o acoplamento antes de criá-lo, não em cobertura.

**"Invest in the design of the system every day"** — citação usada em [[wiki/sources/fundamentos-de-software-importam-mais-que-nunca-na-era-da-ia]] para argumentar contra o movimento spec-driven ("specs to code") que trata o código como descartável: cada mudança deveria melhorar (ou ao menos preservar) o design do sistema, nunca só resolver o problema local ignorando a estrutura.

**Metáfora dos dois chapéus:** ver [[wiki/concepts/dois-chapeus-kent-beck]] — adicionar funcionalidade e refatorar são atividades mutuamente exclusivas no tempo, cada uma com sua própria disciplina de validação (testes passando vs. comportamento externo intacto). Citado em [[wiki/sources/o-que-e-refatoracao-quando-usar]] como o argumento central para nunca refatorar e mudar comportamento ao mesmo tempo.

## Autor de *Extreme Programming Explained* (1999) — origem do YAGNI

Beck é o autor do livro fundador da Extreme Programming, onde [[wiki/concepts/yagni]] foi apresentado. [[wiki/sources/kiss-yagni-entrega-rapida-qualidade]] atribui esse livro a Ron Jeffries — provável imprecisão da fonte, registrada como nota de verificação em [[wiki/concepts/yagni]]. Jeffries é cocriador da XP junto com Beck no [[wiki/entities/c3-project|projeto C3]], mas não é o autor do livro em questão.

## Nota de verificação

A citação acima foi atribuída a Beck na palestra-fonte, mas a obra exata não foi identificada durante a ingestão — provavelmente de *Tidy First?* ou de material de XP, a confirmar em ingestão futura.

## Key Sources

- [[wiki/sources/fundamentos-de-software-importam-mais-que-nunca-na-era-da-ia]]
- [[wiki/sources/o-que-e-refatoracao-quando-usar]] — metáfora dos dois chapéus
- [[wiki/sources/xunit-martin-fowler]] — origem do JUnit e do framework de testes que o antecedeu
- [[wiki/sources/kiss-yagni-entrega-rapida-qualidade]] — verificação de autoria de *Extreme Programming Explained*, origem do YAGNI
