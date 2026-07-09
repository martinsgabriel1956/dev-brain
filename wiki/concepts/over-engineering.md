---
type: concept
title: "Over-Engineering"
aliases: ["overengineering", "verde neném", "engenharia excessiva", "gold plating"]
date_created: 2026-06-09
date_updated: 2026-07-09
source_count: 2
tags: [design, qualidade, anti-pattern, aprendizado, design-patterns, dora, under-engineering]
skill: tech-mentor-leadership
status: stable
---

## Definição

Aplicar soluções mais complexas do que o problema exige — frequentemente por falta de entendimento do domínio, por querer usar um conceito recém-aprendido, ou por antecipar requisitos que nunca chegarão.

No contexto de aprendizado, a forma mais comum é o **"verde neném"**: alguém que acabou de aprender design patterns tenta aplicar todos eles em tudo, tornando o código mais difícil, não melhor.

---

## O maior problema da indústria não é over-engineering — é under-engineering

Antes de tratar dos cuidados contra over-engineering, vale registrar a proporção: segundo observação de David Farley e consenso informal coletado entre desenvolvedores, o problema mais comum na indústria de software é o oposto — falta de engenharia, não excesso. Over-engineering é real e merece atenção, mas não é a causa mais frequente de sistemas ruins. Ver [[wiki/sources/como-evitar-over-engineering-david-farley]].

## Por Que Acontece

### Em iniciantes
- Querer aplicar tudo que aprendeu de uma vez
- Ainda não ter julgamento para saber quando um pattern cabe
- Confundir complexidade com qualidade

### Em devs experientes

**Perfeccionismo por falta de objetivo ou conhecimento** — construir uma "torre de marfim" sem fim, geralmente por não ter claro qual valor de negócio está sendo entregue, ou por aplicar princípios (Clean Code, Clean Architecture) sem entender por que — o "gamer" que tem noções vagas dos princípios e se perde no processo em vez de entregar.

**Falta de confiança — resolver requisitos não-funcionais antes de qualquer valor** — antecipar escala, performance e resiliência antes de ter algo rodando: já entrar com Kubernetes, microsserviços e arquitetura "à prova de tudo" de cara. O antídoto documentado por David Farley é o [[walking-skeleton]]: implementar uma fatia mínima da arquitetura fim-a-fim, colocar em produção cedo, isolar as peças provisórias atrás de abstrações trocáveis, e só otimizar quando a necessidade for comprovada (caso do LMAX).

- Antecipar requisitos hipotéticos ("vamos precisar disso no futuro")
- Otimizar prematuramente para flexibilidade que nunca será necessária

---

## Velocidade e qualidade não competem (refutação do "triângulo de ferro")

O "triângulo de ferro" — a ideia de que entre rápido, barato e bom você só pode escolher dois — é tratado como mito para software. Dados do [[dora-metrics|DORA]] (publicados em *Accelerate*) mostram que equipes que entregam mais rápido, em incrementos pequenos e frequentes, também entregam com **mais** qualidade, não menos. Isso reformula o motivo de se evitar over-engineering: não é só "para entregar mais rápido", é porque a mesma disciplina que evita over-engineering (fatias pequenas, feedback cedo, abstrações só quando necessárias) é a que a pesquisa DORA associa a menor change failure rate e menor MTTR.

Medo de quebrar em produção tende a gerar o efeito oposto ao pretendido: portões de deploy excessivos (muitas aprovações, PRs grandes por serem "a única chance" de revisão) atrasam o feedback e, paradoxalmente, aumentam o risco por deploy em vez de reduzi-lo.

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
- [[walking-skeleton]] — técnica concreta para evitar over-engineering por falta de confiança
- [[dora-metrics]] — evidência empírica de que a disciplina que evita over-engineering também melhora velocidade de entrega
- [[kiss]] — princípio irmão, mesma disciplina de suprimir complexidade desnecessária

---

## Key Sources

- [[wiki/sources/aprender-antes-de-aplicar-fundamentos-e-otimizacao-prematura]]
- [[wiki/sources/como-evitar-over-engineering-david-farley]]
