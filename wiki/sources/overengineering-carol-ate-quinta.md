---
type: source
title: "Over-Engineering: Quando o Código Bonito Vira um Problema"
aliases: ["overengineering ate quinta", "carol over-engineering", "codigo bonito pior que codigo feio"]
date_created: 2026-04-29
date_updated: 2026-04-29
source_count: 0
tags: [over-engineering, kiss, accidental-complexity, ego, code-quality, carreira, design-patterns, gambiarra]
skill: tech-mentor-backend
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/overengineering-carol-ate-quinta.md
source_url: ""
author: "Carol (Até Quinta)"
date_published: ""
date_ingested: 2026-04-29
---

## TL;DR

Over-engineering é tão prejudicial quanto gambiarra. Programadores ganham experiência, aprendem design patterns e arquitetura, e começam a aplicar complexidade onde ela não é necessária — impulsionados pelo ego e pela síndrome do impostor. O código abstrato demais dificulta manutenção, cria conhecimento restrito, força gambiarras no time, e gera os mesmos Frankensteins que tentava evitar.

---

## Key Claims

**Claim:** Over-engineering é tão prejudicial quanto gambiarra.
**Evidence:** Código com camadas desnecessárias de abstração força devs sem aquele conhecimento específico a criar gambiarras para contornar a arquitetura — gerando duplicação e Frankensteins.
**Source:** Carol, experiência de mercado e comentários coletados no LinkedIn.
**Confidence:** Alta — padrão documentado, exemplificado com casos concretos.

**Claim:** O KISS (Keep It Simple) é difícil de aplicar justamente para quem tem mais experiência.
**Evidence:** Iniciantes pensam simples por limitação de conhecimento. Seniores precisam ativamente suprimir o viés de complexidade adquirido com anos de estudo.
**Source:** Carol, análise da progressão de carreira.
**Confidence:** Alta — consistente com literatura (YAGNI, Extreme Programming).

**Claim:** O ego é um vetor de over-engineering.
**Evidence:** Devs abstraem "para ficar bonito" ao invés de abstrair por requisito real — "e se esse código de caldo de cana fosse usado para fritar pastel?"
**Source:** Carol, história do Pedro.
**Confidence:** Alta — anedota ilustrativa mas padrão reconhecível.

**Claim:** Padrões de projeto com conhecimento restrito no time geram gambiarras.
**Evidence:** Projetos com dois padrões arquiteturais diferentes precisam de gambiarras para conectá-los. Devs sem contexto forçam comportamentos ao redor da arquitetura.
**Source:** Carol + comentário Marcelo (LinkedIn).
**Confidence:** Alta.

**Claim:** Código simples nem sempre performa pior que código abstrato.
**Evidence:** Thread LinkedIn mostrou caso onde código "feio" performava melhor por ter menos camadas de abstração. Carol contra-argumenta: diferença em milissegundos não justifica abrir mão de manutenibilidade.
**Source:** Carol, thread LinkedIn.
**Confidence:** Média — depende do contexto, mas argumento de Carol é sólido para casos onde a diferença é negligenciável.

---

## Conceitos

- [[concepts/over-engineering]]
- [[concepts/kiss]]
- [[concepts/ego-driven-development]]
- [[concepts/accidental-complexity]]
- [[concepts/abstraction-bloat]]
- [[concepts/abstraction-illusion]]

---

## Entidades

- Carol (Até Quinta) — engenheira de software sênior, criadora do conteúdo.

---

## Open Questions

- Onde está a linha entre "pensar no futuro" (escalabilidade real) e over-engineering?
- Como operacionalizar KISS em code review? Qual rubrica usar para rejeitar abstração prematura?

---

## Raw Quotes

> "Muitas vezes o seu código bonito pode ser pior do que o código feio."

> "Pensar simples é uma das coisas mais difíceis na programação quando você tem bagagem e conhecimento."

> "O código abstrato extremamente complexo pode ser tão prejudicial quanto a gambiarra."

> "Você está ali aumentando a complexidade só para dizer: eu que fiz. Olha só que bonito. Como se um código social que você fosse emoldurar e colocar um troféu."

> "Você tem metade do projeto em um padrão e metade em outro, com gambiarra para conectar os dois."

---

## Contradições / Tensões com o Wiki

- [[sources/listen-notes-good-enough-engineering]] converge fortemente — Wenbin Fang defende "good enough engineering" com a mesma premissa de evitar over-engineering.
- [[sources/clean-architecture]] e [[sources/solid]] ensinam padrões que, mal aplicados, são a fonte do over-engineering descrito aqui. A tensão não é contradição — é contexto.
- [[concepts/abstraction-bloat]] documentou o mesmo fenômeno com IA como vetor. Este source documenta o vetor humano (ego + experiência).
