---
type: concept
title: "Lei de Goodhart"
aliases: ["Goodhart's Law", "Goodhart's Law Metrics"]
date_created: 2026-07-28
date_updated: 2026-07-28
source_count: 1
tags: [metrics, engineering-management, tomada-de-decisao]
skill: tech-mentor-leadership
status: stable
---

# Lei de Goodhart

**TL;DR:** "Quando uma medida se torna um alvo, ela deixa de ser uma boa medida." (Charles Goodhart). Qualquer métrica, ao ser transformada em meta cobrada de cima para baixo, cria incentivo para otimizar o número em vez do comportamento real que o número deveria representar.

## Mecanismo

Uma métrica só funciona como sinal enquanto ela é **observada**, não **perseguida**. No momento em que vira alvo formal (bônus, cobrança, meta contratual), as pessoas medidas passam a ter incentivo racional para inflar o número por caminhos que não representam a melhoria real que a métrica pretendia capturar.

## Exemplo Central: Story Points Forçados

Quando um PO ou [[wiki/concepts/scrum-master|Scrum Master]] exige que cada pessoa do time entregue 30–40 [[wiki/concepts/story-points]] por sprint, a métrica deixa de medir complexidade relativa entregue e passa a medir a capacidade do time de inflar estimativas para bater a meta — por exemplo, atribuir 20 pontos a um CRUD que leva três horas. A métrica não desaparece, mas perde toda a capacidade preditiva que tinha (ex.: usar velocity histórica para prever prazos), porque o número deixou de refletir a realidade.

Isso é análogo a manter o gráfico de contribuições do GitHub "verdinho" com commits vazios (apagar/colar código só para gerar atividade) — uma métrica de exibição, não de valor real entregue.

## Como Usar Métricas Sem Cair em Goodhart

- Preferir métricas de **tendência do próprio time ao longo do tempo** a metas absolutas impostas externamente — ver [[wiki/concepts/dora-metrics]], que segue o mesmo princípio (não comparar times entre si, não usar para avaliação individual).
- Deixar a métrica **emergir** do processo (ex.: velocity calculada a partir de estimativas honestas via [[wiki/concepts/planning-poker]]) em vez de definir o número desejado primeiro e forçar o processo a produzi-lo.
- Se uma meta precisa existir, negociá-la com quem vai ser medido por ela, entendendo o impacto real na qualidade e na colaboração do time — não impô-la sem consulta.

## Conceitos Relacionados

[[wiki/concepts/story-points]] · [[wiki/concepts/scrum-master]] · [[wiki/concepts/dora-metrics]] · [[wiki/concepts/planning-poker]]

## Key Sources

- [[wiki/sources/story-points-po-forcando-30-40-pontos-por-sprint]]
