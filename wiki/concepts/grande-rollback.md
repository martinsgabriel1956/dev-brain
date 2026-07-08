---
type: concept
title: "Grande Rollback"
aliases: ["the great rollback", "volta ao boring tech", "voltar para o relacional"]
date_created: 2026-07-07
date_updated: 2026-07-07
source_count: 1
tags: [tendencias, arquitetura, redis, mysql, postgresql, boring-technology, backend]
skill: tech-mentor-backend
status: stub
---

# Grande Rollback

Observação recorrente (não uma métrica formal) de que empresas de alta escala estão abandonando peças de stack que a indústria havia normalizado como "óbvias" — Redis para tudo, brokers externos para tudo, microsserviços para tudo — e voltando para soluções mais simples e já presentes no banco relacional que já operam. O nome vem da ideia de "reverter" um consenso de arquitetura que virou dogma sem ser reexaminado.

## Padrão Observado

```
Problema de concorrência/fila/lock → resposta automática: "bota Redis" / "bota Kafka"
     ↓
Em escala, alguém questiona: "por que não usamos o que o banco já oferece?"
     ↓
Redesenho usando primitivas do banco relacional (SKIP LOCKED, advisory lock,
fila baseada em tabela) → menos sistemas para operar, mesma ou melhor performance
```

## Casos Observados

- **[[wiki/entities/shopify]]** — substituiu reserva de estoque Redis+MySQL por um modelo 100% MySQL com [[wiki/concepts/skip-locked]], segurando US$ 5,1 milhões/minuto na Black Friday de 2025. Ver [[wiki/sources/shopify-redis-para-mysql-skip-locked-black-friday]].
- **[[wiki/entities/37signals]]** — saiu do cloud para hardware próprio; construiu o **[[wiki/concepts/solid-queue]]**, fila de processamento 100% sobre banco relacional, sem broker externo.
- **[[wiki/sources/listen-notes-boring-tech-one-person-company]]** — não é uma saída do relacional, mas reforça o tema adjacente: PostgreSQL como "fonte única de verdade", Redis e Elasticsearch tratados como camadas derivadas e descartáveis.

## Por Que Isso Não É "Redis É Ruim"

O ponto não é que ferramentas como Redis sejam inadequadas — é que elas viraram **resposta automática** para qualquer problema de concorrência, sem reavaliar se o banco relacional já resolveria com menos complexidade operacional. O custo real de manter dois sistemas sincronizados (Redis + banco) é maior do que o custo de infraestrutura pura: inclui depuração cross-system, operação/replicação de um cluster adicional, e carga cognitiva do time.

## Tensão com o Mercado de Trabalho

Em entrevistas técnicas, sugerir abandonar Redis por MySQL/PostgreSQL ainda pode ser lido como sinal de fraqueza técnica, dependendo de quem entrevista — o dogma de mercado está atrasado em relação à prática observada em empresas que efetivamente operam nessa escala.

## Key Sources

- [[wiki/sources/shopify-redis-para-mysql-skip-locked-black-friday]]
