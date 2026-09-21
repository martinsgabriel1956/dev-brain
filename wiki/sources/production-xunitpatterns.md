---
type: source
title: "Production (xUnitPatterns.com — Gerard Meszaros)"
aliases: ["production", "produção (ambiente)"]
date_created: 2026-09-21
date_updated: 2026-09-21
source_count: 0
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/production-xunitpatterns.md"
source_url: "http://xunitpatterns.com/production.html"
author: "Gerard Meszaros"
date_published: 2003-01-01
date_ingested: 2026-09-21
tags: [testes, xunit, production, terminologia, fonte-primaria, tech-mentor-testing]
skill: tech-mentor-testing
status: stable
---

# Production (xUnitPatterns.com — Gerard Meszaros)

## TL;DR

Verbete curtíssimo do Glossário do catálogo xUnitPatterns.com que define a **palavra-raiz** de todo o par terminológico test code / production code já coberto na wiki: **production** é o nome dado, em ambientes de TI, ao ambiente onde aplicações rodam para usuários reais — em contraste com os diversos ambientes de teste ("acceptance", "integration", "development", "qual"). É o verbete mais básico possível: [[wiki/sources/production-code-xunitpatterns]] já citava essa definição de passagem ("In IT shops, the environment in which applications run is often called production") ao explicar a origem do termo "production code", mas até agora essa citação não tinha fonte primária isolada própria — esta ingestão fecha essa lacuna final da série.

---

## Afirmações-chave

| Afirmação | Evidência | Confiança |
|---|---|---|
| "Production" nomeia o ambiente onde aplicações rodam para usuários reais, em ambientes de TI | "the environment in which applications being used by real users run is often called 'Production'" | Alta — fonte primária, definição direta |
| O termo existe para se distinguir de outros ambientes: acceptance, integration, development, qual | "This is to distinguish it from the various test environments such as 'acceptance', 'integration', 'development', 'qual' [...] etc." | Alta |
| "Qual" é abreviação de "quality assessment or assurance" | "'qual' (short for 'quality assessment or assurance')" | Alta |

---

## Entidades Mencionadas

- [[wiki/entities/gerard-meszaros]] — autor do verbete; mesmo cluster de fontes primárias do catálogo já ingerido

## Conceitos Tocados

- [[wiki/concepts/production-code]] — o termo "production code" deriva diretamente deste, tomando emprestado o nome do ambiente para nomear o código destinado a rodar nele
- [[wiki/concepts/pensamento-em-producao]] — sentido relacionado mas distinto: aquele conceito trata da mentalidade de engenharia voltada ao comportamento do sistema em produção; este verbete define o próprio substantivo "production" como ambiente

## Open Questions

1. Os quatro ambientes de teste citados de passagem ("acceptance", "integration", "development", "qual") não têm elaboração própria no verbete nem, até esta ingestão, fonte primária dedicada na wiki — "acceptance" já aparece indiretamente via [[wiki/sources/customer-test-xunitpatterns]], mas os demais seguem como menção lateral.
2. O verbete não distingue "production" (o ambiente) de "produção" no sentido de mentalidade/prática de engenharia ([[wiki/concepts/pensamento-em-producao]]) — a wiki já tratava esse segundo sentido antes desta ingestão, sem cruzamento explícito entre os dois usos da palavra.

## Raw Quotes

> "In IT shops, the environment in which applications being used by real users run is often called 'Production'. This is to distinguish it from the various test environments such as 'acceptance', 'integration', 'development', 'qual' (short for 'quality assessment or assurance'), etc."

*(Tradução completa em `raw/production-xunitpatterns.md`.)*

## Key Sources (fontes citadas nesta ingestão)

- [[wiki/sources/production-code-xunitpatterns]] — já citava esta definição de passagem, sem fonte primária isolada própria; esta fonte fecha essa lacuna
