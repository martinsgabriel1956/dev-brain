---
type: source
title: "Test-Driven Development (xUnitPatterns.com — Gerard Meszaros)"
aliases: ["test-driven development xunitpatterns", "TDD glossary xunitpatterns"]
date_created: 2026-09-04
date_updated: 2026-09-04
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/test-driven-development-xunitpatterns.md
source_url: "http://xunitpatterns.com/test-driven%20development.html"
author: "Gerard Meszaros"
date_published: 2003-01-01
date_ingested: 2026-09-04
source_count: 0
tags: [testes, tdd, xunit, fonte-primaria, terminologia, emergent-design]
skill: tech-mentor-testing
status: stable
---

# Test-Driven Development (xUnitPatterns.com — Gerard Meszaros)

## TL;DR

Verbete curto do Glossário do catálogo xUnitPatterns.com que define formalmente **test-driven development**: um processo de desenvolvimento em que se escreve e automatiza os [[wiki/concepts/tdd|unit tests]] antes que o desenvolvimento das unidades correspondentes comece, garantindo que as responsabilidades de cada unidade fiquem claras antes de serem codificadas. O verbete distingue explicitamente TDD de **test-first development** (termo mais amplo) e cunha o critério diferenciador: TDD implica fazer o [[wiki/concepts/tdd|código de produção]] funcionar **um teste de cada vez**, característica batizada de **emergent design**. Aponta ainda para **storytest-driven development** como termo relacionado, sem defini-lo.

---

## Afirmações Centrais

| Afirmação | Evidência | Fonte | Confiança |
|---|---|---|---|
| TDD é escrever/automatizar unit tests antes de desenvolver a unidade correspondente | "A development process that entails writing and automating unit tests before the development of the corresponding units is started" | fonte primária (Meszaros) | alta |
| O objetivo do TDD é garantir que as responsabilidades de cada unidade sejam entendidas antes da codificação | "This ensures that the responsibilities of each software unit are well understood before they are coded" | fonte primária | alta |
| TDD é distinto de test-first development: TDD implica fazer o código de produção funcionar um teste de cada vez | "Unlike test-first development, test-driven development is typically meant to imply that the production code is made to work one test at a time" | fonte primária | alta |
| Essa característica (um teste de cada vez) é chamada de emergent design | "a characteristic called emergent design" | fonte primária | alta |
| Termo relacionado: storytest-driven development | "See also: storytest-driven development" | fonte primária | média (sem definição própria nesta fonte) |

---

## Key Claims

### 1. TDD ⊂ test-first development, não é sinônimo
A wiki já tratava "test-driven development" como o termo central da prática (ver [[wiki/concepts/tdd]]), mas não tinha, até agora, uma fonte primária que isolasse a distinção formal entre **test-driven** e **test-first**. Segundo Meszaros, test-first development é o termo mais genérico — apenas "escrever o teste antes" —, enquanto test-driven development é uma prática mais específica dentro desse guarda-chuva: implica também que o código de produção evolui **incrementalmente**, um teste por vez, em vez de escrever todos os testes de antemão e implementar o código de uma vez. Essa distinção não estava formalizada na wiki antes desta ingestão — [[wiki/concepts/tdd]] mencionava a dupla RED-GREEN-REFACTOR sem citar "test-first" como um termo-irmão mais amplo.

### 2. "Emergent design" é o nome formal para a consequência de design de fazer TDD um teste por vez
A fonte cunha explicitamente o termo **emergent design** para a característica central do TDD "puro": o design do sistema emerge incrementalmente à medida que cada teste força uma pequena decisão de implementação, em vez de ser definido antecipadamente. É a mesma ideia que [[wiki/concepts/tdd]] já descrevia informalmente na seção "As duas escolas" (ex.: "o design emerge das interfaces que o teste exige" para a escola London), mas sem nomear o conceito nem citar a fonte primária que o formaliza.

### 3. Storytest-driven development fica registrado como termo relacionado, mas não definido
O verbete referencia "storytest-driven development" como ver-também, sem explicar o termo. Fica como lacuna aberta — provável candidato a expandir com [[wiki/concepts/bdd]] (que já cobre a extensão do TDD para linguagem de negócio) numa ingestão futura da mesma página do glossário.

---

## Entidades Mencionadas

- [[wiki/entities/gerard-meszaros]] — autor do verbete; mesma fonte primária do catálogo já usada para [[wiki/sources/test-double-xunitpatterns-meszaros]], [[wiki/sources/control-point-xunitpatterns]] e outras entradas do glossário xUnitPatterns.com

## Conceitos Tocados

- [[wiki/concepts/tdd]] — fonte primária formal do próprio termo central da página; distinção test-driven vs. test-first e definição de emergent design incorporadas
- [[wiki/concepts/emergent-design]] — novo stub criado a partir desta fonte; termo cunhado aqui pela primeira vez na wiki
- [[wiki/concepts/test-first-development]] — novo stub criado a partir desta fonte; termo-guarda-chuva mais amplo do qual TDD é um caso específico
- [[wiki/concepts/storytest-driven-development]] — novo stub criado a partir desta fonte; termo apenas referenciado, não definido pelo verbete original

## Questões Abertas

- **Storytest-driven development não está definido nesta fonte** — o verbete original do glossário para esse termo (`http://xunitpatterns.com/storytest-driven%20development.html`, se existir) é candidato natural para uma próxima ingestão da mesma série.
- **Test-first development também não está definido nesta fonte** — mesma situação; existe um verbete dedicado no glossário (`http://xunitpatterns.com/test%20first%20development.html`) que resolveria a definição completa em vez de inferida por contraste.
- Sem contradição com o resto da wiki — a fonte refina e formaliza distinções que já estavam presentes de forma implícita/informal em [[wiki/concepts/tdd]].

---

## Citações Relevantes

> "A development process that entails writing and automating unit tests before the development of the corresponding units is started. This ensures that the responsibilities of each software unit are well understood before they are coded."

> "Unlike test-first development, test-driven development is typically meant to imply that the production code is made to work one test at a time (a characteristic called emergent design.) See also: storytest-driven development."

*(Tradução completa em `raw/test-driven-development-xunitpatterns.md`.)*
