---
type: concept
title: "Monolith First"
aliases: ["monolito primeiro", "monolith first", "martinfowler.com/bliki/monolithfirst"]
date_created: 2026-08-18
date_updated: 2026-08-18
source_count: 1
tags: [monolito, monolito-modular, microsservicos, martin-fowler, arquitetura, ddd]
skill: tech-mentor-backend
status: stub
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

## Key Sources

- [[wiki/sources/microsservicos-monolito-first-renato-augusto]] — nomeação explícita do princípio, as duas percepções de Fowler, e a imagem dos "dois caminhos" do bliki
