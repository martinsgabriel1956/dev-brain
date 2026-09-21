---
type: source
title: "Continuous Integration (xUnitPatterns.com — Gerard Meszaros)"
aliases: ["continuous integration", "integração contínua", "CI"]
date_created: 2026-09-21
date_updated: 2026-09-21
source_file: "raw/continuous-integration-xunitpatterns.md"
source_url: "http://xunitpatterns.com/continuous%20integration.html"
author: "Gerard Meszaros"
date_published: 2003-01-01
date_ingested: 2026-09-21
source_count: 0
tags: [testes, ci-cd, xunit, fonte-primaria, terminologia]
skill: tech-mentor-testing
status: stable
---

# Continuous Integration (xUnitPatterns.com — Gerard Meszaros)

## TL;DR

Verbete de Glossário do xUnitPatterns.com que define **continuous integration** do ponto de vista específico de testes: a prática ágil de integrar mudanças de código a cada poucas horas ou dias, tipicamente acoplada a um build automatizado disparado por check-in que roda todos os testes automatizados (incluindo, às vezes, testes lentos demais para rodar antes do check-in). O critério de "build falho" é binário — qualquer teste falhando falha o build inteiro — e a consequência organizacional é a regra do **stop-the-line**: consertar o build vira prioridade máxima, e nenhuma mudança de código é permitida além das que visam corrigir o build. É a primeira fonte da wiki a formalizar essa regra de prioridade como parte da própria definição de CI, não como prática derivada — reforça, de fonte primária dedicada ao vocabulário de testes, o gate de CI contra **Lost Test** já registrado em [[wiki/sources/production-bugs-xunitpatterns]] e o [[wiki/concepts/ci-cd|CI/CD]] já documentado por [[wiki/entities/martin-fowler]].

---

## Afirmações Centrais

| Afirmação | Evidência | Fonte | Confiança |
|---|---|---|---|
| Continuous integration é a prática ágil de integrar mudanças de código continuamente — na prática, a cada poucas horas ou dias | "The agile software development practice of integrating software changes continuously. In practice, this means that developers integrate their changes every few hours to days" | fonte primária (Meszaros) | alta |
| CI costuma incluir um build automatizado disparado por cada check-in, que roda todos os testes automatizados, inclusive alguns lentos demais para rodar antes do check-in | "Continuous integration often includes the practice of an automated build that is triggered by each check in. The build process typically runs all the automated tests an may even run tests that aren't run before check in because they take too long" | fonte primária | alta |
| O build é considerado "falho" se qualquer teste falhar | "The build is considered to have 'failed' if any tests fail" | fonte primária | alta |
| Quando o build falha, consertá-lo vira prioridade máxima do time; só mudanças de código voltadas à correção do build são permitidas até haver um build bem-sucedido | "When the build fails, teams typically consider getting the build working again to be the top priority; only code changes aimed at fixing the build are allowed until a successful build has occured" | fonte primária | alta |

---

## Key Claims

### 1. A definição é centrada em teste, não em deploy — mais estreita que a de Fowler
[[wiki/concepts/ci-cd]] já documenta a definição de **Continuous Delivery** de Martin Fowler, focada em manter o software sempre "releasable". Este verbete de Meszaros, escrito para o vocabulário de xUnit, é deliberadamente mais estreito: CI aqui é sobre **frequência de integração de código + automação de build/teste**, sem menção a deploy, ambiente de produção ou releasability. É consistente com o escopo do livro (padrões de teste, não de entrega), e complementa — não contradiz — a definição mais ampla já presente na wiki.

### 2. "Build falho = qualquer teste falhando" formaliza o critério binário que sustenta o gate de Lost Test
[[wiki/sources/production-bugs-xunitpatterns]] já recomendava configurar o CI para falhar o build acima de um limiar de testes ignorados. Este verbete fecha a peça que faltava: a definição do próprio evento "build falho" — qualquer teste falhando (não uma média, não um threshold de porcentagem) reprova o build inteiro. É esse critério binário que torna o gate de Lost Test possível de se expressar como regra de CI.

### 3. "Stop the line" é regra de prioridade organizacional, não só técnica
A fonte não apenas descreve a mecânica técnica (build automatizado, todos os testes rodando); ela nomeia explicitamente a consequência de processo: quando o build quebra, a prioridade do time muda — só código que conserta o build é aceito até o build voltar a passar. É uma regra emprestada da manufatura enxuta (Andon cord / stop-the-line da Toyota), aplicada aqui a build de software sem citar a origem — primeira vez que a wiki registra essa regra de prioridade como parte formal da definição de CI, e não apenas como prática cultural derivada.

---

## Entidades Mencionadas

- [[wiki/entities/gerard-meszaros]] — autor do verbete; mesma fonte primária do catálogo já usada para dezenas de outros verbetes
- [[wiki/entities/martin-fowler]] — autor da definição mais ampla de Continuous Delivery/Deployment Pipeline já documentada em [[wiki/concepts/ci-cd]], contrastada aqui pela definição mais estreita de Meszaros

## Conceitos Tocados

- [[wiki/concepts/ci-cd]] — este verbete acrescenta a definição de escopo mais estreito (centrada em teste) do mesmo termo, de uma fonte primária diferente de Fowler
- [[wiki/concepts/production-bugs]] — fecha a definição de "build falho" que sustenta o gate de CI contra Lost Test já recomendado nessa fonte

## Questões Abertas

- A fonte não detalha **quem** dispara o build automatizado (servidor de CI dedicado vs. hook local) nem cita ferramentas — deixa a mecânica de implementação totalmente em aberto, ao contrário de fontes mais recentes já na wiki (ex.: GitHub Actions).
- Não há menção a ambientes de staging/produção nem a frequência mínima recomendada além de "a cada poucas horas a dias" — sem detalhe sobre o que acontece depois do build passar (deploy? apenas integração de código?).

---

## Citações Relevantes

> "The agile software development practice of integrating software changes continuously. In practice, this means that developers integrate their changes every few hours to days."

> "The build is considered to have 'failed' if any tests fail. When the build fails, teams typically consider getting the build working again to be the top priority; only code changes aimed at fixing the build are allowed until a successful build has occured."

*(Tradução completa em `raw/continuous-integration-xunitpatterns.md`.)*
