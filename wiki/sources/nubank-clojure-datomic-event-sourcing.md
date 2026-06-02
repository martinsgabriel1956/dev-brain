---
type: source
title: "Por que o Nubank Escolheu Clojure e Datomic"
aliases: ["nubank clojure datomic", "nubank event sourcing"]
date_created: 2026-05-31
date_updated: 2026-05-31
source_count: 0
tags: [nubank, clojure, datomic, event-sourcing, cqrs, functional-programming, ddd, fintech]
skill: tech-mentor-backend
status: stable
source_file: /home/nemomartins/Documentos/new/dev-study/raw/nubank-clojure-datomic-event-sourcing.md
source_url: ""
author: "Vinícius Pasco Antônio (Nova Devs)"
date_published: ""
date_ingested: 2026-05-31
---

# Por que o Nubank Escolheu Clojure e Datomic

## TL;DR

O Nubank (100M clientes, maior banco digital da América Latina) tomou suas decisões técnicas fundacionais baseado em um paper acadêmico que identifica mutabilidade e efeitos colaterais como as principais fontes de complexidade acidental em sistemas grandes. Isso levou à escolha de Clojure (funcional, imutável), Datomic (banco de dados imutável/append-only) e uma arquitetura baseada em Event Sourcing + CQRS + DDD.

---

## Claims Principais

### 1. Mutabilidade e efeitos colaterais são a raiz da complexidade acidental
**Evidência:** O CTO do Nubank citou o paper "Out of the Tar Pit" (Moseley & Marks) como fundação das escolhas técnicas.
**Confidence:** Alta — citação direta em vídeo.
> *"Mutable state and effects are the source of most of the accidental complexity in large systems."*

### 2. Clojure foi escolhido por ser funcional e rodar na JVM
**Evidência:** Clojure oferece imutabilidade nativa + ecossistema Java maduro. Sem precisar reinventar bibliotecas básicas.
**Confidence:** Alta.
> *"Being able to access the entire Java ecosystem of mature libraries was really valuable."*

### 3. Datomic como banco imutável para auditoria e time-travel
**Evidência:** Para um banco com requisitos regulatórios, a capacidade de ver o estado em qualquer ponto do tempo é um superpoder que bancos legados não têm.
**Confidence:** Alta.
> *"The ability to go back in time and look at the state as it evolved — that looked like an unbelievable superpower."*

### 4. Codebases envelhecem como leite (Java/Ruby) ou como vinho (funcional)
**Evidência:** Experiência direta do engenheiro com sistemas Java que viraram legado intocável vs. sistemas funcionais mantidos por anos.
**Confidence:** Alta (experiência empírica).

### 5. Efeitos colaterais devem ficar nas periferias (não no domínio)
**Evidência:** Padrão de arquitetura hexagonal + DDD: domínio puro no centro, adapters com I/O na borda.
**Confidence:** Alta — padrão consolidado validado pelo Nubank.

---

## Entidades Mencionadas

- [[nubank]] — empresa que tomou essas decisões
- [[rich-hickey]] — criador do Clojure e do Datomic
- [[clojure]] — linguagem principal do Nubank

---

## Conceitos Tocados

- [[event-sourcing]] — persistir eventos, não estado; reaplica eventos para calcular estado atual
- [[cqrs]] — separação entre leitura e escrita; estado em memória derivado do event log
- [[imutabilidade]] — variáveis não mudam após criadas; elimina toda uma classe de bugs
- [[efeitos-colaterais]] — funções que fazem mais do que prometem; devem ser explícitos e periféricos
- [[programacao-funcional]] — paradigma que força imutabilidade e funções puras
- [[ddd]] — domínio no centro, adapters na borda; aggregates, domain events
- [[complexidade-acidental]] — complexidade que vem de escolhas de implementação, não do problema
- [[datomic]] — banco de dados imutável, append-only, com time-travel nativo
- [[ledger-imutavel]] — padrão fintech: nunca atualizar saldo, acumular transações

---

## Quotes Valiosas

> *"Codebases age like milk pretty quickly."* — sobre Java/Ruby

> *"You have a log of events. The bank reapplies all those events to calculate the current state."*

> *"Mutable state and effects are the source of most of the accidental complexity in large systems."* — Out of the Tar Pit

---

## Contradições / Questões Abertas

- O Nubank usa framework interno (não público) — difícil avaliar detalhes de implementação.
- Curva de aprendizado de Event Sourcing é alta; a fonte não discute como o Nubank fez onboarding de novos engenheiros.
- Clojure é uma linguagem de nicho — como o Nubank lida com contratação e formação de time?

---

## Domínios Secundários

- `tech-mentor-ai` — não aplicável
- `lang-dynamic` — Clojure (Lisp dinâmico sobre JVM)
- `tech-mentor-system-design` — trade-offs de arquitetura em escala
