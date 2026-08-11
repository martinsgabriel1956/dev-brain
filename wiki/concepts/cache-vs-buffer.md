---
type: concept
title: "Cache vs. Buffer"
aliases: ["cache vs buffer", "diferença cache buffer", "cache não é buffer"]
date_created: 2026-08-11
date_updated: 2026-08-11
source_count: 1
tags: [cache, buffer, system-design, backend, arquitetura, fundamentos]
skill: tech-mentor-backend
status: draft
---

# Cache vs. Buffer

Cache e buffer são confundidos porque compartilham **uma única característica**: ambos armazenam dados temporariamente, muitas vezes em RAM, às vezes por poucos segundos, e em alguns casos com a mesma tecnologia (Redis serve tanto como [[wiki/concepts/cache]] quanto, via Redis Streams, como [[wiki/concepts/buffer]]). O que os distingue **não é a implementação — é o motivo** do armazenamento.

## A diferença em uma frase

- **[[wiki/concepts/cache|Cache]]** existe pela **expectativa de reutilização**: um dado foi obtido por uma operação cara e há boa chance de ser pedido de novo, então guarda-se uma cópia para não repetir o trabalho. *Pergunta: "vale a pena guardar isso? alguém vai usar novamente?"*
- **[[wiki/concepts/buffer|Buffer]]** existe para **absorver diferença de velocidade** entre um produtor e um consumidor: o dado fica ali só até ser processado e então é descartado, sem intenção de reuso. *Pergunta: "como evitar que um componente mais rápido sobrecarregue um componente mais lento?"*

## Tabela comparativa

| Dimensão | Cache | Buffer |
|---|---|---|
| Problema que resolve | Repetir trabalho caro | Desequilíbrio de velocidade produtor/consumidor |
| Reuso do dado | **Sim** — é a razão de existir | **Não** — descartado após consumo |
| Cresce conforme aumenta | Quantidade de dados reutilizados | Diferença entre velocidade de produção e consumo |
| Perspectiva temporal | **Passado** — o dado já foi usado, pode voltar | **Presente** — organiza o fluxo que acontece agora |
| Vida útil típica | Segundos, minutos, horas | Muito curta — liberado assim que o dado segue |
| Preocupação principal | Invalidação / sincronização ([[wiki/concepts/tradeoff-de-cache]]) | Dimensionamento / [[wiki/concepts/filas-e-workers|backpressure]] |

## A mesma ideia em duas escalas

**Hardware:** cache L1/L2/L3 da CPU guarda instruções/dados prováveis de reuso entre processador e RAM (reutilização); buffer de teclado, impressora e placa de rede equilibra periféricos de velocidades diferentes (fluxo).

**Arquitetura distribuída:** cache de aplicação / [[wiki/concepts/redis]] responde queries caras e frequentes sem ir ao banco (reutilização); [[wiki/concepts/mensageria|fila de mensagens]] (Kafka, SQS, RabbitMQ) absorve picos de tráfego permitindo consumidores em ritmo constante (fluxo).

## Armadilha do nome

Nome não define conceito. O [[wiki/concepts/buffer-pool]] do banco funciona como **cache** (páginas retidas para reuso), apesar de "buffer" no nome. E o primeiro cache de CPU (IBM System/360) foi originalmente chamado de *high speed buffer*. Classifique pelo **motivo**, não pela etiqueta.

## Sistemas usam os dois

Não é escolha exclusiva. O YouTube usa **buffer** (leitura antecipada no player, ver [[wiki/concepts/latencia-streaming-ao-vivo]]) **e** cache (via [[wiki/concepts/cdn]]) ao mesmo tempo. Arquiteturas robustas conhecem e combinam os dois.

## Relação com outros conceitos

- [[wiki/concepts/cache]] · [[wiki/concepts/buffer]] — os dois lados
- [[wiki/concepts/mensageria]] · [[wiki/concepts/fila]] · [[wiki/concepts/filas-e-workers]] — buffer em nível de sistema
- [[wiki/concepts/buffer-pool]] — o "buffer" que na verdade é cache
- [[wiki/concepts/tradeoff-de-cache]] — o custo de invalidação que só o cache carrega

## Key Sources

- [[wiki/sources/cache-vs-buffer-diferenca-conceitual]] — Bernardo Lobato: cache olha pro passado (reutilização), buffer olha pro presente (fluxo)
