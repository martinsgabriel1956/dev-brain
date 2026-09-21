---
type: source
title: "Production Code (xUnitPatterns.com — Gerard Meszaros)"
aliases: ["production code", "código de produção"]
date_created: 2026-09-21
date_updated: 2026-09-21
source_count: 0
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/production-code-xunitpatterns.md"
source_url: "http://xunitpatterns.com/production%20code.html"
author: "Gerard Meszaros"
date_published: 2003-01-01
date_ingested: 2026-09-21
tags: [testes, xunit, production-code, test-code, terminologia, fonte-primaria, tech-mentor-testing]
skill: tech-mentor-testing
status: stable
---

# Production Code (xUnitPatterns.com — Gerard Meszaros)

## TL;DR

Verbete curtíssimo do Glossário do catálogo xUnitPatterns.com que finalmente dá fonte primária dedicada a um termo já citado repetidamente em outras fontes da wiki — [[wiki/sources/control-point-xunitpatterns]], [[wiki/sources/observation-point-xunitpatterns]], [[wiki/sources/test-driven-development-xunitpatterns]] e [[wiki/sources/test-first-development-xunitpatterns]] — mas nunca definido por si mesmo até agora. Meszaros explica a origem do termo: ele precisava de uma forma de distinguir o [[wiki/concepts/test-doubles|código de teste]] do código que está sendo testado. Como o ambiente onde aplicações rodam em produção é chamado de **production**, ele escolheu **production code** para nomear o código que se escreve para embarcar num produto ou implantar em produção — em oposição a **test code**. É um par de termos puramente terminológico, sem mecanismo técnico próprio, mas que funciona como pressuposto silencioso de todo o vocabulário SUT/DOC já documentado em [[wiki/concepts/test-doubles]] e [[wiki/concepts/indirect-input-output]]: o **SUT** e o **DOC** são sempre production code; o teste que os exercita é test code.

---

## Afirmações-chave

| Afirmação | Evidência | Confiança |
|---|---|---|
| Meszaros cunhou "production code" para nomear o código que não é código de teste, em oposição a "test code" | "I needed a term to distinguish test code from the code that we are testing [...] So I'm choosing to call the code that we are writing [...] 'production code'" | Alta — fonte primária, origem explícita do termo |
| "Production" (o ambiente) é o que empresta o nome — production code é o código destinado a rodar lá, tenha ou não sido de fato implantado ainda | "In IT shops, the environment in which applications run is often called production" | Alta |
| O par é aplicável tanto a código embarcado num produto quanto a código implantado em produção | "whether to ship in a product or deploy into production" | Alta |

---

## Entidades Mencionadas

- [[wiki/entities/gerard-meszaros]] — autor do verbete; mesmo cluster de fontes primárias do catálogo já ingerido

## Conceitos Tocados

- [[wiki/concepts/production-code]] — fonte primária dedicada que esta ingestão finalmente traz, criando a página até agora inexistente
- [[wiki/concepts/test-doubles]] — SUT e DOC, como definidos ali, são sempre production code; o double é o que se injeta no lugar de um DOC real durante o teste
- [[wiki/concepts/indirect-input-output]] — a regra "control points/observation points exclusivos de teste não devem ser usados pelo production code", já registrada ali a partir de duas fontes diferentes, agora ganha a definição formal do próprio termo "production code" que faltava

## Open Questions

1. **"Test code"** — o termo irmão citado explicitamente neste verbete ("obvious", nas palavras do próprio Meszaros) segue sem página de glossário dedicada própria na wiki; candidato natural para uma próxima ingestão, ainda que o autor o trate como autoexplicativo.
2. O verbete não elabora sobre a fronteira entre production code e test utility code (código de teste reutilizável, mas que não é o teste em si) — distinção que aparece implicitamente em outras fontes da wiki (ex.: Test Utility Method em [[wiki/sources/testcase-object-xunitpatterns]]) mas não é resolvida aqui.

## Raw Quotes

> "I needed a term to distinguish test code from the code that we are testing. 'Test code' is obvious. What to call the other kind of code? In IT shops, the environment in which applications run is often called production. So I'm choosing to call the code that we are writing, whether to ship in a product or deploy into production, 'production code'. So, we have test code and we have 'production code'."

*(Tradução completa em `raw/production-code-xunitpatterns.md`.)*

## Key Sources (fontes citadas nesta ingestão)

- [[wiki/sources/control-point-xunitpatterns]] — já usava "production code" na regra de design sobre control points exclusivos de teste, sem definição própria do termo; esta fonte fecha essa lacuna
- [[wiki/sources/observation-point-xunitpatterns]] — mesma situação, do lado da regra de design sobre observation points exclusivos de teste
- [[wiki/sources/test-driven-development-xunitpatterns]] — usa "production code" para descrever o que o TDD faz funcionar um teste de cada vez
- [[wiki/sources/test-first-development-xunitpatterns]] — usa "production code" na distinção entre test-first development e TDD
