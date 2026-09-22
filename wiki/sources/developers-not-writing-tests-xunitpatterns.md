---
type: source
title: "Developers Not Writing Tests (xUnitPatterns.com — Gerard Meszaros)"
aliases: ["developers not writing tests", "desenvolvedores não escrevem testes", "test debt", "dívida de teste"]
date_created: 2026-09-22
date_updated: 2026-09-22
source_file: "raw/developers-not-writing-tests-xunitpatterns.md"
source_url: "http://xunitpatterns.com/Developers%20Not%20Writing%20Tests.html"
author: "Gerard Meszaros"
date_published: 2003-01-01
date_ingested: 2026-09-22
source_count: 0
tags: [testes, test-smell, project-smell, xunit, fonte-primaria, terminologia, test-debt]
skill: tech-mentor-testing
status: stable
---

# Developers Not Writing Tests (xUnitPatterns.com — Gerard Meszaros)

## TL;DR

Segundo **Project Smell** da wiki vindo do catálogo xUnitPatterns.com de [[wiki/entities/gerard-meszaros]], irmão de [[wiki/concepts/production-bugs|Production Bugs]] — na verdade o próprio verbete de Production Bugs já citava este de passagem ("Ambos os casos estão relacionados a *Developers Not Writing Tests*"), e esta ingestão fecha essa referência com fonte primária dedicada. O smell é o sintoma de nível de gestão ("ouvimos dizer que os devs não estão escrevendo testes"), não um smell de código. A fonte cunha formalmente o termo **test debt** (dívida de teste): não escrever testes para tudo "que poderia quebrar" hipoteca o futuro do time, tornando cada vez mais lento adicionar funcionalidade e mais arriscado refatorar — o mesmo mecanismo de juros compostos já documentado para tech debt genérico em [[wiki/concepts/tech-debt-como-ferramenta]], mas aplicado especificamente à ausência de testes. A árvore de causas tem três ramos: falta de tempo, código difícil de testar (que remete a [[wiki/concepts/hard-to-test-code|Hard-to-Test Code]], ainda sem página própria) e estratégia de automação de testes errada (testes frágeis ou obscuros demais para escrever rápido). A fonte também é explícita sobre **quem detecta** o smell: geralmente não é o desenvolvedor, é gestão (PM, Scrum master, tech lead) — o oposto de smells de código, que o próprio dev encontra lendo o código.

---

## Afirmações Centrais

| Afirmação | Evidência | Fonte | Confiança |
|---|---|---|---|
| Não escrever testes para tudo que poderia quebrar coloca o time em "test debt", tornando features mais lentas de adicionar e refactoring mais arriscado ao longo do tempo | "it is mortgaging its future [...] the system will be in test debt. It will take longer and longer to add new functionality and refactoring of the code [...] will be fraught with peril" | fonte primária (Meszaros) | alta |
| Falta de tempo (prazo agressivo, ordem explícita de "não perder tempo com testes", ou falta de skill/curva de aprendizado) é uma causa raiz, e o ajuste de cronograma para supri-la deveria ser temporário | "This should only need to be a temporary adjustment while they develop the skills [...] once developers have internalized the process, they can write the tests and the code in the same time" | fonte primária | alta |
| Código difícil de testar (tipicamente legado sem suíte completa) é outra causa raiz, tratada em detalhe na página irmã Hard-to-Test Code | "the design of the software is not conducive to automated testing. This situation is described in more detail in its own smell section, Hard-to-Test Code" | fonte primária | alta |
| Estratégia de automação errada gera Fragile Tests ou Obscure Tests demorados demais de escrever; a técnica recomendada para achar a causa raiz é os "cinco porquês" (Toyota Production System) | "leading to Fragile Tests or Obscure Tests that take too long to write. We need to ask the 'five why's' [TPS] to find the root causes" | fonte primária | alta |
| Esse smell de nível de projeto é detectado tipicamente por gestão (PM/Scrum master/tech lead), não pelo desenvolvedor individual, e metas de melhoria devem ser qualitativas o bastante para não incentivar gaming (ex.: escrever testes clonados só para inflar contagem) | "more likely to be detected by a project manager, Scrum master or team lead than by a developer [...] A goal of 205 more tests written could be achieved without increasing the test coverage one iota simply by splitting tests into smaller pieces or cloning tests" | fonte primária | alta |

---

## Key Claims

### 1. "Test debt" é o mesmo mecanismo de tech debt, mas Meszaros o nomeia e o ancora especificamente em ausência de testes
[[wiki/concepts/tech-debt-como-ferramenta]] já documenta extensamente o mecanismo de dívida técnica genérica (Quadrante de Fowler, regra do if, Boy Scout Rule). Esta fonte contribui um caso específico e nomeado: dívida que se acumula não por atalho de design, mas pela ausência lisa e simples de testes automatizados para código "que poderia quebrar". A consequência descrita — velocidade decrescente para adicionar feature, refactoring cada vez mais arriscado — é textualmente o mesmo efeito de juros compostos já registrado para tech debt genérica, mas aqui a causa raiz é singular e concreta o bastante para virar checklist de gestão, não decisão arquitetural.

### 2. O smell tem três causas raiz que apontam para três páginas-irmãs distintas do catálogo, nenhuma ainda com fonte primária dedicada
A fonte lista, com nomes próprios que remetem a outras páginas do site: **Hard-to-Test Code** (design não testável, típico de legado), **Fragile Test** e **Obscure Test** (consequências de uma estratégia de automação errada). Nenhuma das três tem página própria na wiki ainda — são citadas de passagem aqui, assim como já eram citadas de passagem em [[wiki/sources/production-bugs-xunitpatterns]] (que menciona Fragile/Obscure Test em outro contexto). É o segundo sinal, agora, de que essas três páginas-irmãs seriam ingests de alto valor: cada citação de passagem que se repete em fontes diferentes reforça a centralidade do termo sem ele ainda ter uma fonte primária isolada.

### 3. Quem detecta o smell muda o tipo de ação recomendada — e a fonte alerta contra metas gameáveis
Diferente dos smells de código (que o próprio dev encontra ao ler/mexer no código), este é um smell de nível de projeto detectável majoritariamente por quem tem visão de time inteiro — gestão. A fonte recomenda perguntar ao time *por que*, *em quais circunstâncias* e *quanto tempo leva* escrever testes, e dá apoio total (incluindo tempo para montar infraestrutura de teste) em vez de só cobrar. O ponto mais afiado: uma meta de "escrever N testes a mais" pode ser satisfeita sem qualquer ganho real de cobertura — dividindo testes existentes em pedaços menores ou clonando-os — então metas de melhoria de processo devem mirar em nível "alto o bastante para encorajar o comportamento certo" (ex.: redução percentual de código não testado), não em contagem bruta. É uma aplicação direta e nomeada do fenômeno já registrado como [[wiki/concepts/goodharts-law|Goodhart's Law]] em outras páginas da wiki.

---

## Entidades Mencionadas

- [[wiki/entities/gerard-meszaros]] — autor do verbete; mesma fonte primária do catálogo já usada para dezenas de outros verbetes

## Conceitos Tocados

- [[wiki/concepts/production-bugs]] — smell-irmão que já citava este de passagem ("Ambos os casos estão relacionados a Developers Not Writing Tests"); esta ingestão fecha essa referência com fonte dedicada
- [[wiki/concepts/tech-debt-como-ferramenta]] — "test debt" é o mesmo mecanismo de dívida técnica genérica, nomeado e ancorado especificamente em ausência de testes
- [[wiki/concepts/code-smells]] — segundo Project Smell da taxonomia irmã de Meszaros a ganhar página na wiki
- [[wiki/concepts/goodharts-law]] — o aviso contra metas de "N testes a mais" gameáveis é uma aplicação direta e nomeada do fenômeno

## Questões Abertas

- **Hard-to-Test Code**, **Fragile Test** e **Obscure Test** seguem sem página própria na wiki, agora citadas de passagem em duas fontes diferentes (esta e Production Bugs) — candidatos fortes a ingestão dedicada.
- **Five Whys / TPS (Toyota Production System)** é citado como técnica de troubleshooting, mas a wiki ainda não tem página sobre o método em si.
- A fonte não detalha o que conta como "código que poderia quebrar" (critério de risco) além de exemplos implícitos — potencial ponto de expansão se uma fonte futura tratar do assunto.

---

## Citações Relevantes

> "If the team isn't writing automated tests for every piece of software 'that could possibly break', it is mortgaging its future [...] the system will be in test debt."

> "Project level smells such as Developers Not Writing Tests are more likely to be detected by a project manager, Scrum master or team lead than by a developer."

> "A goal of 205 more tests written could be achieved without increasing the test coverage one iota simply by splitting tests into smaller pieces or cloning tests."

*(Tradução completa em `raw/developers-not-writing-tests-xunitpatterns.md`.)*
