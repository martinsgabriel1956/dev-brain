---
type: concept
title: "Métricas de Acoplamento (Aferente/Eferente, Abstração, Instabilidade, Sequência Principal)"
aliases: ["metricas de acoplamento", "afferent coupling", "efferent coupling", "acoplamento aferente", "acoplamento eferente", "abstractness", "instability", "main sequence", "sequencia principal", "zone of pain", "zone of uselessness", "zona de dor", "zona de inutilidade"]
date_created: 2026-08-12
date_updated: 2026-08-12
source_count: 1
tags: [acoplamento, metricas, arquitetura, clean-architecture, abstracao, instabilidade, sequencia-principal, software-design]
skill: tech-mentor-backend
status: draft
---

# Métricas de Acoplamento

Se [[wiki/concepts/acoplamento]] é qualitativo ("mudar A força mudar B"), estas são as **métricas que o tornam mensurável** por componente/pacote. Vêm de [[wiki/entities/uncle-bob|Robert C. Martin]] (*Agile Software Development* / *Clean Architecture*) e foram apresentadas de forma acessível em português por [[wiki/entities/matheus-castiglioni]] em [[wiki/sources/medindo-e-entendendo-acoplamento-matheus-castiglioni]].

## Acoplamento Aferente (Ca) e Eferente (Ce)

- **Aferente (_Afferent / Incoming_) — Ca**: número de conexões que **entram** no componente, ou seja, quem depende dele. Ca alto = muita gente usa você (você é uma dependência importante).
- **Eferente (_Efferent / Outgoing_) — Ce**: número de conexões que **saem** do componente, ou seja, de quantas coisas você depende. Ce alto = você é frágil, quebra quando o que você usa muda.

Mnemônico: **A**ferente = "**A** entrada"; **E**ferente = "sai (**E**xit)".

## Abstração (A)

Proporção de artefatos abstratos para o total.

```
A = ma / (ma + mc)
```

- `ma` = elementos abstratos (interfaces, classes abstratas).
- `mc` = elementos concretos (classes não abstratas).
- Resultado em `[0, 1]`: `0` = totalmente concreto, `1` = totalmente abstrato.
- Exemplo do post: 5.000 linhas numa única função `main` → numerador 1, denominador 5000 → **A ≈ 0** (nada abstrato).

## Instabilidade (I)

Volatilidade do componente: quanto ele tende a mudar por causa de dependências de saída.

```
I = Ce / (Ca + Ce)
```

- `I = 0` → **máxima estabilidade**: muitos dependem de você (Ca alto), você depende de ninguém (Ce baixo). Difícil e arriscado mudar.
- `I = 1` → **máxima instabilidade**: você depende de tudo (Ce alto), ninguém depende de você (Ca baixo). Fácil e barato mudar.
- Insight do post: alta instabilidade **quebra mais fácil quando mudada**, por causa do alto acoplamento eferente.

## Distância da Sequência Principal (D)

O ideal é um relacionamento inverso entre abstração e estabilidade: o que é **estável deve ser abstrato** (para poder ser estendido sem mudar), e o que é **instável deve ser concreto** (detalhes descartáveis). Isso é a reta `A + I = 1`, a **sequência principal**.

```
D = | A + I - 1 |
```

- `D = 0` → em cima da sequência principal (equilíbrio ideal).
- `D → 1` → longe da linha, numa das duas zonas-armadilha.

### As duas zonas-armadilha (gráfico A × I)

- **Zona de dor (_zone of pain_)** — canto inferior esquerdo (A baixo, I baixo): concreto **e** estável. Muita implementação, poucas abstrações, e muita gente depende disso → **frágil e difícil de mudar**. Ex.: um utilitário concreto usado por todo o sistema; um schema de banco rígido.
- **Zona de inutilidade (_zone of uselessness_)** — canto superior direito (A alto, I alto): abstrato **e** instável. Abstração que ninguém usa → **código morto/inútil**. Ex.: interfaces genéricas criadas "para o futuro" sem implementação real.

Compare com [[wiki/concepts/dumb-zone]] se aplicável ao seu vocabulário local.

## Como isso conecta com o resto da wiki

- Formaliza numericamente o que [[wiki/concepts/acoplamento]] descreve qualitativamente e o que a heurística "de quem é essa linha?" (ver [[wiki/sources/tres-estagios-de-acoplamento-observer-pattern-na-pratica]]) faz linha a linha.
- A busca por `I=0 + A=1` (estável e abstrato) é exatamente o alvo do [[wiki/concepts/dependency-injection]] e da regra de dependência da [[wiki/concepts/clean-architecture]]: dependa de abstrações estáveis, não de detalhes concretos voláteis.
- Complementa [[wiki/sources/quatro-tecnicas-ci-cd-gate-qualidade-codigo-ia-uncle-bob]], que trata de **automatizar** a detecção de acoplamento indevido no CI (import circular, camadas invertidas) — a análise de estrutura de dependências ali é a versão executável destas métricas.
- [[wiki/concepts/abstracao]] e [[wiki/concepts/coesao]] são os conceitos irmãos: alta coesão + baixo acoplamento eferente + abstração no lugar certo é o alvo.

## Key sources

- [[wiki/sources/medindo-e-entendendo-acoplamento-matheus-castiglioni]] — fórmulas de A, I, D, aferente/eferente e as duas zonas, em português
