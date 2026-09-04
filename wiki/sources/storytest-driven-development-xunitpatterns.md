---
type: source
title: "Storytest-Driven Development (xUnitPatterns.com — Gerard Meszaros)"
aliases: ["storytest-driven development xunitpatterns", "STDD glossary xunitpatterns"]
date_created: 2026-09-04
date_updated: 2026-09-04
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/storytest-driven-development-xunitpatterns.md
source_url: "http://xunitpatterns.com/storytest-driven%20development.html"
author: "Gerard Meszaros"
date_published: 2003-01-01
date_ingested: 2026-09-04
source_count: 0
tags: [testes, tdd, xunit, fonte-primaria, terminologia, emergent-design, bdd]
skill: tech-mentor-testing
status: stable
---

# Storytest-Driven Development (xUnitPatterns.com — Gerard Meszaros)

## TL;DR

Verbete curto do Glossário do xUnitPatterns.com que finalmente define **storytest-driven development (STDD)**, termo que já aparecia como "ver também" em [[wiki/sources/test-driven-development-xunitpatterns]] sem explicação própria. STDD é uma variação do [[wiki/concepts/tdd|test-driven development]] que consiste em escrever (e geralmente automatizar) **customer tests** antes do desenvolvimento da funcionalidade correspondente começar — garantindo que a integração das unidades verificadas pelos unit tests resulte num todo utilizável para o cliente, não só em unidades corretas isoladamente. A fonte credita a cunhagem do termo a **Joshua Kerievsky**, como parte da metodologia "Industrial XP" (IXP).

---

## Afirmações Centrais

| Afirmação | Evidência | Fonte | Confiança |
|---|---|---|---|
| STDD é uma variação do processo de TDD | "A variation of the test-driven development process" | fonte primária (Meszaros) | alta |
| Consiste em escrever/automatizar customer tests antes de desenvolver a funcionalidade correspondente | "that entails writing (and usually automating) customer tests before the development of the corresponding functionality is started" | fonte primária | alta |
| O objetivo é garantir que a integração das unidades (verificadas por unit tests) resulte num todo utilizável | "This ensures that integration of the various software units verified by the unit tests results in a usable whole" | fonte primária | alta |
| O termo foi cunhado por Joshua Kerievsky, como parte da metodologia "Industrial XP" (IXP) | "The term storytest-driven development was first coined by Joshua Kierievsky as part of his methodology \"Industrial XP\" [IXP]" | fonte primária | alta |

---

## Key Claims

### 1. Fecha, com fonte primária, a lacuna deixada por duas ingestões anteriores
Tanto [[wiki/sources/test-driven-development-xunitpatterns]] quanto [[wiki/sources/test-first-development-xunitpatterns]] citavam STDD apenas como termo relacionado, sem defini-lo — e a wiki já havia registrado a suspeita, em [[wiki/concepts/storytest-driven-development]] e [[wiki/concepts/test-first-development]], de que STDD seria operacionalmente equivalente a praticar test-first no nível de *customer test*. Este verbete confirma essa suspeita: STDD é definido exatamente como escrever customer tests antes da funcionalidade correspondente — a mesma prática que [[wiki/sources/test-first-development-xunitpatterns]] descrevia como "test-first no nível de customer test", agora nomeada e formalizada como um caso específico dentro do guarda-chuva de TDD (não de test-first development genérico).

### 2. Diferença sutil de foco: unidade vs. "todo utilizável"
Enquanto o verbete de TDD enfatiza fazer o código de produção funcionar um teste por vez ([[wiki/concepts/emergent-design]]), o de STDD desloca o foco para o **resultado da integração**: o objetivo explícito é que a soma das unidades corretas (cada uma validada por unit tests) produza algo utilizável do ponto de vista do cliente. É a mesma preocupação que motiva a existência da camada de customer test na [[wiki/concepts/piramide-de-testes]] — unidades corretas isoladamente não garantem que o sistema integrado funcione para quem o usa.

### 3. Origem do termo: Joshua Kerievsky e Industrial XP (IXP)
Dado novo e específico: a atribuição de autoria do termo a Kerievsky, via sua metodologia "Industrial XP" — uma variação/evolução prática do [[wiki/concepts/extreme-programming|XP]] clássico. Não havia menção a Kerievsky ou a IXP na wiki antes desta ingestão; ambos ficam registrados como possíveis stubs de entidade/conceito futuros, caso outra fonte aprofunde o tema.

---

## Entidades Mencionadas

- [[wiki/entities/gerard-meszaros]] — autor do verbete; mesma fonte primária do catálogo já usada para [[wiki/sources/test-driven-development-xunitpatterns]], [[wiki/sources/test-first-development-xunitpatterns]] e outras entradas do glossário xUnitPatterns.com
- Joshua Kerievsky — citado como o cunhador do termo "storytest-driven development", como parte de sua metodologia "Industrial XP" (IXP); sem página própria na wiki ainda, dado insuficiente nesta fonte curta para justificar um stub

## Conceitos Tocados

- [[wiki/concepts/storytest-driven-development]] — promovido de stub inferido/citado por contraste para definição com fonte primária própria; `source_count` 1 → 2, `status` stub → stable
- [[wiki/concepts/tdd]] — STDD registrado como variação formal do TDD, focada em customer tests
- [[wiki/concepts/test-first-development]] — confirma a suspeita registrada nessa página: STDD ≈ test-first no nível de customer test
- [[wiki/concepts/piramide-de-testes]] — reforça a distinção unit test vs. customer test como o eixo em que STDD se posiciona
- [[wiki/concepts/emergent-design]] — mencionado por contraste: o verbete de STDD não enfatiza "um teste de cada vez" como o de TDD faz

## Questões Abertas

- **Joshua Kerievsky e "Industrial XP" (IXP)** não têm página própria na wiki — dado específico demais para justificar um stub isolado a partir desta única fonte curta; candidato a stub caso surja outra fonte que aprofunde IXP.
- Sem contradição com o resto da wiki — a fonte confirma e formaliza, com citação direta, uma relação que já havia sido inferida por contraste nas duas ingestões anteriores da mesma série.

---

## Citações Relevantes

> "A variation of the test-driven development process that entails writing (and usually automating) customer tests before the development of the corresponding functionality is started. This ensures that integration of the various software units verfied by the unit tests results in a usable whole."

> "The term storytest-driven development was first coined by Joshua Kierievsky as part of his methodology \"Industrial XP\" [IXP]."

*(Tradução completa em `raw/storytest-driven-development-xunitpatterns.md`.)*
