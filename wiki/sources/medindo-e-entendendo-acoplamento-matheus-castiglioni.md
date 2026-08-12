---
type: source
title: "Medindo e Entendendo Acoplamento"
aliases: ["medindo acoplamento", "métricas de acoplamento castiglioni", "afferent efferent abstractness instability"]
date_created: 2026-08-12
date_updated: 2026-08-12
source_count: 0
tags: [acoplamento, metricas, arquitetura, clean-architecture, abstracao, instabilidade, sequencia-principal, software-design]
skill: tech-mentor-backend
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/medindo-e-entendendo-acoplamento-matheus-castiglioni.md
source_url: https://blog.matheuscastiglioni.com.br/medindo-e-entendendo-acoplamento/
author: Matheus Castiglioni
date_published:
date_ingested: 2026-08-12
---

# Medindo e Entendendo Acoplamento

## TL;DR

Post curto de [[wiki/entities/matheus-castiglioni]] que faz duas coisas com [[wiki/concepts/acoplamento]]: (1) taxonomiza os **tipos** de acoplamento (data, stamp, control, external, common, content) e as duas **categorias** (apropriado vs. não apropriado), e (2) apresenta as **métricas de acoplamento** de [[wiki/entities/uncle-bob|Robert C. Martin]] — acoplamento aferente (Ca) / eferente (Ce), abstração `A = ma/(ma+mc)`, instabilidade `I = Ce/(Ca+Ce)` e distância da sequência principal `D = |A + I − 1|` — mais as duas regiões-armadilha do gráfico A×I: a **zona de inutilidade** (abstrato demais) e a **zona de dor** (concreto/frágil demais). O valor do post é dar nomes e fórmulas concretas ao que o resto da wiki trata de forma qualitativa. Ver [[wiki/concepts/metricas-de-acoplamento]] para a página que consolida essas fórmulas.

## Key Claims

| Claim | Evidence | Confidence |
|---|---|---|
| Acoplamento é a medida do nível de interdependência entre módulos | Definição de abertura do post | Alta |
| Existem seis tipos de acoplamento, cada um com trade-off | data, stamp, control, external, common, content — "às vezes vamos ter mais de um tipo e menos de outro dependendo da situação e contexto" | Alta — taxonomia clássica da engenharia de software (Yourdon/Constantine) |
| Acoplamento também se divide em duas categorias qualitativas | apropriado (você sabe que existe e deveria existir) vs. não apropriado (você não sabe que existe, ou sabe e não deveria) | Média — enquadramento do autor, útil mas informal |
| Acoplamento pode ser medido por conexões de entrada e saída | Aferente (Ca) = conexões de entrada ao código; Eferente (Ce) = conexões que saem do código | Alta |
| Abstração é medida por A = ma/(ma+mc) | ma = elementos abstratos (interfaces/classes abstratas), mc = elementos concretos; ex.: 5.000 linhas numa única `main` → numerador 1, denominador 5000 (A ≈ 0) | Alta — métrica de Uncle Bob |
| Instabilidade é medida por I = Ce/(Ca+Ce) | mede volatilidade; alta instabilidade quebra mais fácil sob mudança por causa do alto acoplamento eferente | Alta — métrica de Uncle Bob |
| Distância da sequência principal é D = \|A + I − 1\| | A e I são frações entre 0 e 1; o ideal é ficar próximo da linha A+I=1 | Alta — métrica de Uncle Bob |
| Existem duas regiões-armadilha no gráfico A×I | Zona de inutilidade (abstrato demais → difícil de usar) e zona de dor (implementação demais sem abstração → frágil e difícil de manter) | Alta |

## Tipos de acoplamento (do post)

- **Data Coupling** — partes independentes que se comunicam apenas via informação (mais fraco/desejável).
- **Stamp Coupling** — estruturas de dados inteiras passadas de uma parte a outra.
- **Control Coupling** — passagem de parâmetros de controle que ativam comportamentos diferentes na outra parte.
- **External Coupling** — partes dependem de outras partes externas.
- **Common Coupling** — partes dependem de informação/estrutura global.
- **Content Coupling** — uma parte modifica dados internos ou o fluxo de controle de outra (mais forte/indesejável).

## As três métricas (fórmulas)

```
Abstração:    A = ma / (ma + mc)         # ma abstratos, mc concretos → [0,1]
Instabilidade: I = Ce / (Ca + Ce)        # Ce eferente (sai), Ca aferente (entra) → [0,1]
Distância:    D = | A + I - 1 |          # 0 = em cima da sequência principal (ideal)
```

Interpretação do gráfico A (eixo Y) × I (eixo X), com a **sequência principal** sendo a reta `A + I = 1`:

- Perto da linha → classe/módulo bem equilibrado.
- Canto superior (A alto, I baixo → abstrato + estável, mas ninguém usa) → **zona de inutilidade**.
- Canto inferior (A baixo, I baixo → concreto + estável, difícil de mudar) → **zona de dor**.

## Open Questions / Notas

- O post não cita explicitamente [[wiki/entities/uncle-bob|Robert C. Martin]] como origem, mas as três métricas (A, I, D, sequência principal, zonas de dor/inutilidade) são exatamente as definidas por ele em *Clean Architecture* / *Agile Software Development*. Atribuição marcada como inferência de alta confiança.
- A "categoria" apropriado/não apropriado é enquadramento informal do autor; casa bem com a distinção acoplamento *aferente/eferente* — dependências de entrada (Ca) são frequentemente "apropriadas" (você é usado), enquanto excesso de dependências de saída (Ce) tende ao "não apropriado".
- O post é introdutório: dá as fórmulas mas não mostra ferramentas para calcular as métricas num codebase real (ex.: JDepend, NDepend, `dependency-cruiser`). Complementa bem [[wiki/sources/quatro-tecnicas-ci-cd-gate-qualidade-codigo-ia-uncle-bob]], que trata da automação disso em CI.

## Raw quotes

> "Acoplamento é a medida do nível de interdependência entre os módulos, ou seja, são as dependências entre os códigos."

> "uma base de código que possui um alto nível de instabilidade quebra mais facilmente quando mudada por causa do alto acoplamento."

> "Código que é muito abstrato se torna difícil de usar. [...] Código com muita implementação e não tem abstrações o suficiente se torna frágil e difícil de manter."
