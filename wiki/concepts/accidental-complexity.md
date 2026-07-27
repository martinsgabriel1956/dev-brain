---
type: concept
title: "Complexidade Acidental"
aliases: ["complexidade acidental", "accidental complexity", "tech debt estrutural"]
date_created: 2026-04-23
date_updated: 2026-07-27
source_count: 4
tags: [accidental-complexity, tech-debt, fred-brooks, arquitetura, refactoring]
skill: tech-mentor-system-design
status: stable
---

## Definição

Complexidade acidental é aquela que o time introduziu involuntariamente — não existe por necessidade do problema, existe porque foi mais fácil adicionar do que refatorar.

Conceito de Fred Brooks ("No Silver Bullet", 1986), em contraste com [[concepts/essential-complexity]].

## Diagnóstico

> "Essa complexidade existe porque o problema exige — ou porque o time a criou?"

- Se o problema exige: **complexidade essencial** — conviva com ela, projete bem.
- Se o time criou: **complexidade acidental** — tem custo operacional crescente sem contrapartida de valor.

## Formas mais comuns

**Abstração errada** — generalizar antes de ter dois casos concretos. A abstração vira obstáculo quando o segundo caso aparece e não se encaixa.

**Decisões não reconciliadas** — três times tomam três decisões independentes sobre o mesmo problema. A interseção é complexidade que não pertence a ninguém.

**Funções god** — 400 linhas que fazem 17 coisas. Cada adição foi mais fácil que refatorar. O resultado é complexidade que resiste a qualquer mudança.

**Camadas desnecessárias** — abstrações empilhadas sem problema a resolver. DAO → Repository → Service → Facade → Controller para um CRUD simples.

**Nomenclatura inconsistente** — `User`, `Account`, `Profile`, `Member` referenciando a mesma entidade em contextos diferentes. O leitor não sabe se são conceitos distintos ou sinônimos.

## Relação com tech debt

Complexidade acidental e tech debt não são sinônimos:

- Tech debt inclui atalhos intencionais com plano de pagamento futuro.
- Complexidade acidental é frequentemente não-intencional e sem plano.

A maioria do que times chamam de "tech debt" é complexidade acidental acumulada — chamada de debt para justificar não endereçar agora.

## Como endereçar

1. **Nomear** — dar nome ao problema é o primeiro passo. "Essa função tem complexidade acidental porque faz X e Y que não pertencem ao mesmo lugar."
2. **Isolar** — não espalhar mais. Mesmo sem refatorar agora, parar de adicionar ao problema.
3. **Refatorar com cobertura** — complexidade acidental em código sem testes é a mais perigosa de mexer. Adicionar testes antes de refatorar.
4. **Priorizar pelo custo** — complexidade no caminho crítico (deploy, onboarding, debugging) tem prioridade sobre complexidade em código estável.

## Uso análogo: tecnologia como o lado que muda (não é o mesmo framing de Brooks)

[[wiki/sources/refatoracao-pragmatic-programmer-martin-fowler-2a-edicao]] aplica "acidente" de forma mais solta que Brooks: não à complexidade dentro de um sistema, mas às tecnologias específicas usadas para ensinar princípios de refatoração — Java datado, uma classe (`Vector`) em desuso, um domínio didático obsoleto (locadora de vídeos) — tudo isso trocado na 2ª edição de *Refactoring* sem alterar os princípios essenciais do livro. É extensão popular da dicotomia, útil para justificar por que conhecimento específico de tecnologia tem prazo de validade curto e princípios de design não têm.

## Modelo cascata como gerador estrutural de complexidade acidental

[[wiki/sources/filosofia-do-design-de-software-introducao]] (John Ousterhout) descreve um mecanismo causal distinto de Fred Brooks para gerar complexidade acidental: no modelo cascata, os problemas do design inicial só ficam aparentes depois que a implementação já está avançada, e o processo não tem mecanismo para revisar o design nesse ponto — então desenvolvedores remendam os problemas sem mudar o design geral, causando "explosão de complexidade". Ver [[wiki/concepts/modelo-cascata-vs-desenvolvimento-incremental]]. Isso complementa o diagnóstico de Brooks (abstração errada, decisões não reconciliadas, funções god) com uma causa de processo: não é só decisão individual malfeita, é a ausência estrutural de um ponto de retorno ao design.

## Relação com outros conceitos

- [[concepts/essential-complexity]] — o contraponto: complexidade que não pode ser removida
- [[concepts/temporal-coupling]] — temporal coupling é uma forma específica de complexidade acidental
- [[concepts/evolutionary-architecture]] — fitness functions detectam aumento de complexidade acidental automaticamente
- [[entities/fred-brooks]] — autor do conceito ("No Silver Bullet", 1986)
- [[wiki/concepts/modelo-cascata-vs-desenvolvimento-incremental]] — mecanismo de processo (Ousterhout) que explica por que complexidade acidental se acumula sem correção sob cascata
- [[wiki/concepts/red-flags-de-design]] — heurística prática para detectar complexidade acidental cedo, antes que ela se acumule

## Key Sources

- [[sources/conceitos-que-ninguem-ensina]]
- [[sources/overengineering-carol-ate-quinta]]
- [[wiki/sources/filosofia-do-design-de-software-introducao]]
- [[wiki/sources/refatoracao-pragmatic-programmer-martin-fowler-2a-edicao]] — uso análogo (não-Brooks) aplicado a tecnologia de exemplo didático vs. princípios de refatoração
