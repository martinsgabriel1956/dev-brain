---
type: concept
title: "Feature Freeze"
aliases: ["feature freeze", "congelamento de features", "code freeze"]
date_created: 2026-08-10
date_updated: 2026-08-10
source_count: 1
tags: [engineering-management, tech-debt, refactoring, processo, qualidade]
skill: tech-mentor-leadership
status: stub
---

# Feature Freeze

Parada pontual e planejada — tipicamente uma semana — em que a equipe **não desenvolve features novas** e usa o tempo para dar um respiro na saúde do sistema: corrigir apenas bugs críticos, repaginar a arquitetura, resolver TODOs, refatorar gambiarras, escrever testes mais compreensíveis e consertar [[wiki/concepts/teste-de-integracao-estreito-vs-amplo|testes]] flaky.

## Feature freeze vs. code freeze

[[wiki/sources/por-que-code-bases-degradam-estrategias-code-rot]] distingue os dois:

- **Code freeze** — parar de escrever código e apenas *testar* o sistema por um período. O autor da fonte não vê muito valor nisso, embora reconheça que alguma empresa possa ver.
- **Feature freeze** — parar apenas o *desenvolvimento de features*, liberando esforço para pagar dívida e melhorar a base. É a variante que a fonte recomenda como "respiro" para a equipe.

## Relação com outras práticas

- É uma parada *concentrada*, em contraste com a [[wiki/concepts/folga-de-capacidade-slack|folga de capacidade contínua]] (~20% embutido em toda sprint) — as duas atacam a [[wiki/concepts/entropia-de-software|entropia]] em cadências diferentes.
- Semelhante ao "debt sprint" descrito em [[wiki/concepts/tech-debt-como-ferramenta]]: eficaz para débitos maiores, mas com o risco de o negócio enxergar como "sprint improdutivo" se não for comunicado por impacto mensurável.

## Key Sources

- [[wiki/sources/por-que-code-bases-degradam-estrategias-code-rot]] — feature freeze como respiro pontual; contraste com code freeze
