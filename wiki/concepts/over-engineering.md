---
type: concept
title: "Over-Engineering"
aliases: ["overengineering", "verde neném", "engenharia excessiva", "gold plating"]
date_created: 2026-06-09
date_updated: 2026-06-09
source_count: 1
tags: [design, qualidade, anti-pattern, aprendizado, design-patterns]
skill: tech-mentor-leadership
status: stable
---

## Definição

Aplicar soluções mais complexas do que o problema exige — frequentemente por falta de entendimento do domínio, por querer usar um conceito recém-aprendido, ou por antecipar requisitos que nunca chegarão.

No contexto de aprendizado, a forma mais comum é o **"verde neném"**: alguém que acabou de aprender design patterns tenta aplicar todos eles em tudo, tornando o código mais difícil, não melhor.

---

## Por Que Acontece

### Em iniciantes
- Querer aplicar tudo que aprendeu de uma vez
- Ainda não ter julgamento para saber quando um pattern cabe
- Confundir complexidade com qualidade

### Em devs experientes
- Antecipar requisitos hipotéticos ("vamos precisar disso no futuro")
- Otimizar prematuramente para flexibilidade que nunca será necessária

---

## Sintomas

- Abstração onde não há variação real
- Padrões GoF aplicados a problemas simples
- Interfaces com uma única implementação criadas "por precaução"
- Hierarquias de herança profundas para algo que poderia ser um enum
- Mais infraestrutura do que lógica de negócio

---

## Causa Raiz no Aprendizado

Over-engineering em quem está aprendendo é quase sempre sintoma de **pular etapas na progressão**. Quem aprende design patterns sem antes dominar [[modelagem-orientada-a-objetos]] não tem julgamento para saber quando um pattern resolve um problema real — então aplica em tudo.

A progressão que evita isso:
1. Dominar [[logica-de-programacao]] e algoritmos
2. Dominar [[modelagem-orientada-a-objetos]]
3. Só então estudar [[design-patterns]] e arquitetura

---

## Relação com Otimização Prematura

[[otimizacao-prematura]] é o análogo de over-engineering no nível de performance: aplicar esforço excessivo onde não há necessidade comprovada. Ambos são sintomas de afoiteza.

---

## Conexões

- [[otimizacao-prematura]] — análogo em performance
- [[anti-pattern]] — over-engineering é um anti-pattern clássico
- [[design-patterns]] — fonte mais comum de over-engineering em quem está aprendendo
- [[modelagem-orientada-a-objetos]] — o pré-requisito que, quando pulado, leva ao verde neném
- [[fundacao-tecnica]] — base necessária para o julgamento de quando não sobre-engenheirar

---

## Key Sources

- [[wiki/sources/aprender-antes-de-aplicar-fundamentos-e-otimizacao-prematura]]
