---
type: concept
title: "Monolith First"
aliases: ["monolito primeiro", "monolith first", "martinfowler.com/bliki/monolithfirst"]
date_created: 2026-08-18
date_updated: 2026-08-21
source_count: 3
tags: [monolito, monolito-modular, microsservicos, martin-fowler, arquitetura, ddd, yagni, bounded-context]
skill: tech-mentor-backend
status: stable
---

# Monolith First

Princípio arquitetural de Martin Fowler (bliki, martinfowler.com/bliki/MonolithFirst.html): **não comece um projeto novo com microsserviços**, mesmo com certeza de que o sistema vai crescer o suficiente para justificar essa arquitetura mais tarde.

## As Duas Percepções que Fundamentam o Princípio

Segundo [[wiki/sources/microsservicos-monolito-first-renato-augusto]], Fowler chegou a esse princípio observando um padrão consistente no mercado:

1. Quase todas as histórias de microsserviços bem-sucedidas começaram como um **monolito** que cresceu e foi quebrado/dividido depois.
2. Quase todos os sistemas criados **do zero já como microsserviços** acabaram tendo sérios problemas.

## Por Que Isso Acontece: Conhecimento de Domínio

O motivo estrutural por trás do padrão observado por Fowler é a falta de conhecimento de domínio no início de um projeto: as fronteiras de serviço corretas só ficam visíveis depois que o domínio real (não o domínio imaginado) se revela. Decompor cedo demais gera fronteiras erradas, que exigem refatorar múltiplos serviços e seus bancos de dados isolados quando o domínio real aparece — o mesmo argumento central já registrado em [[wiki/concepts/microsservicos]] ("Decomposição Correta") e em [[wiki/concepts/ddd]].

## O Caminho Recomendado: Monolito Modular

A implementação prática do princípio é começar por um [[wiki/concepts/monolito-modular]] — módulos internos = bounded contexts do [[wiki/concepts/ddd]], com fronteiras de contrato explícitas (Ports & Adapters), mas ainda um único deploy/banco/processo — e só extrair para [[wiki/concepts/microsservicos]] quando a maturidade de domínio **e** a necessidade real de escala/time justificarem, via [[wiki/concepts/strangler-fig-pattern|estrangulamento]] incremental do monolito.

## A Imagem dos Dois Caminhos

O bliki de Fowler ilustra a escolha com dois caminhos ao iniciar um sistema: o caminho de ir direto para microsserviços é desenhado com dragões (complexidade e risco extremos, por falta de conhecimento de domínio e pela camada extra de infraestrutura distribuída desde o dia 1); o caminho de baixo é o monolito modular, mais seguro por permitir que a arquitetura evolua junto com o conhecimento do domínio.

## Relação com Sacrificial Architecture

Distinto mas complementar a [[wiki/sources/arquitetura-de-sacrificio]] (outro artigo de Fowler, 2014): Sacrificial Architecture argumenta que a primeira arquitetura de um produto deve ser tratada como descartável, otimizada para aprendizado rápido, não para durar — Monolith First é mais específico, focado diretamente na escolha monolito vs. microsserviços no dia 1. Ambos convergem na mesma recomendação prática: monolito primeiro, distribuir depois, com necessidade real como critério de extração.

## Fonte Primária: o Artigo Original de Fowler

[[wiki/sources/monolith-first-martin-fowler]] é o bliki original (3 jun 2015) — confirma ponto a ponto o relato secundário que já estava registrado nesta página e acrescenta: o termo formal **MicroservicePremium** (o "prêmio"/sobretaxa de gerenciar um conjunto de serviços, que só compensa em sistemas mais complexos, ver [[wiki/concepts/microservice-premium]]); os dois argumentos centrais nomeados explicitamente como [[wiki/concepts/yagni|YAGNI]] e dificuldade de acertar [[wiki/concepts/bounded-context|BoundedContexts]] logo no início; quatro caminhos práticos de execução da estratégia (monolito modular desenhado com cuidado, descascar microsserviços gradualmente das bordas, tratar o monolito como [[wiki/concepts/arquitetura-de-sacrificio|Sacrificial Architecture]], ou começar com poucos serviços de granulação grossa — um "duolith"); e um contra-argumento que Fowler reconhece explicitamente: começar direto com microsserviços pode fazer sentido em substituições de sistemas existentes, onde as fronteiras já são conhecidas, desde que o time já tenha experiência com microsserviços.

## Mesmo Padrão Retórico em Seedwork

[[wiki/sources/seedwork-martin-fowler]] (2003) usa a mesma estrutura de argumento, décadas antes: em vez de esperar por um framework de reuso perfeito (raro e difícil de alcançar), Fowler recomenda uma alternativa pragmática e imperfeita — o [[wiki/concepts/seedwork]]. Monolith First aplica o mesmo raciocínio à escolha arquitetural de dia 1: em vez de esperar ter certeza sobre os [[wiki/concepts/bounded-context|bounded contexts]] corretos antes de distribuir, comece pelo monolito modular e evolua a decomposição depois. Em ambos os casos, o critério de decisão de Fowler é "o que é útil agora", não "o que é ideal em teoria".

## Key Sources

- [[wiki/sources/monolith-first-martin-fowler]] — fonte primária: MicroservicePremium, os dois argumentos (YAGNI e BoundedContexts), quatro caminhos práticos, contra-argumento
- [[wiki/sources/microsservicos-monolito-first-renato-augusto]] — nomeação explícita do princípio, as duas percepções de Fowler, e a imagem dos "dois caminhos" do bliki
- [[wiki/sources/seedwork-martin-fowler]] — mesmo padrão retórico de Fowler (pragmatismo imperfeito sobre ideal inalcançável), aplicado a reuso de framework em vez de arquitetura de serviços
