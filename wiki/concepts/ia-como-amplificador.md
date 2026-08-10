---
type: concept
title: "IA como Amplificador (sem julgamento)"
aliases: ["ia amplificador", "ai as amplifier", "amplificador sem julgamento"]
date_created: 2026-08-10
date_updated: 2026-08-10
source_count: 1
tags: [ia-produtividade, seniority, codigo-legado, code-review, julgamento]
skill: tech-mentor-leadership
status: draft
---

# IA como Amplificador (sem julgamento)

**TL;DR:** A IA não é uniformemente boa ou ruim — ela **amplifica o que já existe**: o contexto do sistema, a qualidade do código legado e o critério de quem a usa. Como amplificador não tem julgamento próprio, o resultado depende inteiramente do julgamento humano que a supervisiona. Por isso o ganho é desigual entre perfis.

## Ganho desigual por perfil (Pragmatic Engineer, 2026)

| Perfil / contexto | Ganho de produtividade |
|---|---|
| Júnior em tarefa simples | **+26% a +56%** |
| Sênior em codebase legado | **zero ou negativo** |

Parece contraintuitivo — uma ferramenta que "ajuda todo mundo" prejudicando os mais experientes no contexto mais crítico. A explicação: a IA trata o **código existente como se fosse a verdade**.

- **Sênior bom + legado:** conhece as nuances e decisões de design tomadas anos atrás por razões não documentadas. Ao verificar o que a IA gerou, está comparando contra um código-base que ele sabe não ser bom → verificação custosa, ganho corroído.
- **Sênior mediano + legado:** delega mais e aceita sugestões sem checar o contexto histórico — especialmente se não é "o pai do sistema". O contexto crítico está na cabeça de alguém, não [[wiki/concepts/codigo-legado-ia|documentado]].

Resultado típico: PR **tecnicamente válido** (segue padrões) mas **arquiteturalmente errado** — passa nos testes e quebra a lógica de negócio.

> "Sêniors bons ficam melhores; sêniors medíocres ficam mais difíceis de gerenciar."

Isso **não** significa que a IA é ruim para sêniors — significa que ela **não substitui o julgamento**, só o multiplica (em qualquer direção).

## Consequência prática

O diferencial deixa de ser "escrever rápido" e passa a ser **julgar o que foi gerado com critério** — a base da convergência engenheiro → tech lead descrita em [[wiki/concepts/novo-perfil-dev-ia]]. Também é um argumento forte para **externalizar o contexto que mora na cabeça do time** (docs, ADRs) — ver [[wiki/concepts/divida-cognitiva]] e [[wiki/concepts/teoria-do-programa-naur]].

## Conceitos Relacionados

[[wiki/concepts/paradoxo-da-aceleracao]] · [[wiki/concepts/gaming-de-testes-por-ia]] · [[wiki/concepts/codigo-legado-ia]] · [[wiki/concepts/apagao-de-seniors]] · [[wiki/concepts/novo-perfil-dev-ia]]

## Key Sources

- [[wiki/sources/paradoxo-da-aceleracao-ia-produtividade-metricas]]
