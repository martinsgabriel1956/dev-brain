---
type: concept
title: "Otimização Prematura"
aliases: ["premature optimization", "otimizar prematuramente", "premature optimization root of all evil"]
date_created: 2026-06-09
date_updated: 2026-06-09
source_count: 1
tags: [performance, qualidade, design, engenharia-de-software, anti-pattern]
skill: tech-mentor-leadership
status: stable
---

## Definição

Prática de otimizar o código para performance antes de ter um projeto bem estruturado. É um [[anti-pattern]] clássico — gera código difícil de manter que frequentemente nem performa melhor.

> **"Premature optimization is the root of all evil."** — Donald Knuth

---

## Por Que É Prejudicial

Otimizar antes de ter o design correto:

1. **Torna o código difícil de refatorar** — estruturas otimizadas para performance costumam ser rígidas; mudar o design depois é penoso
2. **Resolve o problema errado** — sem profiling, otimizações atacam partes que não são o gargalo real
3. **Aumenta complexidade desnecessariamente** — micro-otimizações prematuramente introduzem código confuso sem ganho mensurável
4. **Dificulta o debug** — código otimizado é mais difícil de entender e rastrear

---

## A Ordem Correta

```
1. Fazer funcionar corretamente
2. Refatorar para um design bom e legível
3. Medir onde está o gargalo real (profiling)
4. Otimizar apenas o gargalo identificado
```

> "É muito mais fácil otimizar um código bem refatorado do que refatorar um código já otimizado para performance."

Um código bem projetado é naturalmente mais fácil de otimizar — as abstrações corretas facilitam a substituição de implementações por versões mais eficientes.

---

## Relação com Over-Engineering

[[over-engineering]] e otimização prematura compartilham a mesma raiz: aplicar uma solução antes de entender o problema. No over-engineering, o exagero é de complexidade de design. Na otimização prematura, o exagero é de esforço em performance. Ambos produzem código mais difícil de manter sem benefício proporcional.

---

## Quando Otimização É Legítima

- Após profiling confirmar que há um gargalo real
- Em sistemas onde performance é requisito não-funcional crítico e conhecido desde o início (sistemas embarcados, engines de jogos, processamento de imagem em tempo real)
- Na escolha de algoritmo ou estrutura de dados — decisão de design, não micro-otimização

---

## Conexões

- [[over-engineering]] — análogo no nível de design em vez de performance
- [[quadrante-de-fowler]] — tech debt prudente+deliberado é diferente de otimização prematura
- [[fundacao-tecnica]] — sem fundação sólida, é impossível identificar onde otimizar

---

## Key Sources

- [[wiki/sources/aprender-antes-de-aplicar-fundamentos-e-otimizacao-prematura]]
