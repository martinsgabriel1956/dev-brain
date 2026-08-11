---
type: concept
title: "Buffer"
aliases: ["buffer", "buffering", "área de buffer", "buffer de fluxo"]
date_created: 2026-08-11
date_updated: 2026-08-11
source_count: 1
tags: [buffer, backend, system-design, mensageria, streaming, io, desacoplamento, backpressure]
skill: tech-mentor-backend
status: draft
---

# Buffer

Área de armazenamento temporário que **absorve a diferença de velocidade entre um produtor e um consumidor** que trabalham em ritmos diferentes. O dado fica no buffer apenas pelo tempo necessário para o consumidor processá-lo — cumprido esse papel, deixa de ter utilidade e pode ser descartado.

O buffer **não existe para reutilizar dados** (isso é [[wiki/concepts/cache|cache]]). Ele existe para que um componente rápido não sobrecarregue nem perca dados de um componente lento. A pergunta que ele responde é: *"como evitar que um produtor mais rápido atropele um consumidor mais lento?"* — em contraste com o cache, que pergunta *"vale a pena guardar isso para usar de novo?"*. Ver [[wiki/concepts/cache-vs-buffer]] para a distinção completa.

## Por que existe

Sempre que um componente produz informações mais rápido do que outro consegue consumi-las, surge um desequilíbrio. Sem um espaço intermediário, ou o produtor precisa esperar o consumidor, ou parte dos dados se perde. O buffer resolve isso guardando o excedente momentâneo até que o consumidor o alcance.

## Onde aparece

**Hardware / I/O (origem histórica):**
- Teclado envia caracteres enquanto a CPU está ocupada — sem buffer, teclas se perderiam.
- Impressora, disco rígido, placa de rede: o equipamento gera dados num ritmo, outro processa no seu.
- Buffers de leitura/escrita de arquivo e de rede criados automaticamente pelo SO ou pela linguagem (ex.: `BufferedInputStream` / `BufferedOutputStream` em Java).

**Arquitetura distribuída:**
- [[wiki/concepts/mensageria|Fila de mensagens]] como "grande buffer" — absorve picos (ex.: Black Friday) e permite que consumidores trabalhem em ritmo constante, reduzindo acoplamento entre produtor e consumidor. Tecnologias: RabbitMQ, Apache Kafka, Amazon SQS, Redis Streams.
- Pipelines de processamento, ingestão de eventos, upload de arquivos e arquiteturas orientadas a evento.

**Streaming:**
- O player acumula alguns segundos de vídeo (buffer de leitura antecipada) para tocar enquanto baixa, absorvendo oscilações de rede. Sem ele, uma queda de banda travaria a reprodução. Ver [[wiki/concepts/latencia-streaming-ao-vivo]] e [[wiki/concepts/adaptive-bitrate-streaming]].

## Buffer vs. Cache (resumo)

| | Buffer | [[wiki/concepts/cache|Cache]] |
|---|---|---|
| Problema | Diferença de velocidade produtor/consumidor | Reutilização de dado caro de obter |
| Reuso do dado | Não — descartado após consumo | Sim — é a razão de existir |
| Cresce com | Diferença de velocidade | Quantidade de dados reutilizados |
| Perspectiva | Presente (fluxo atual) | Passado (dado já usado) |
| Vida útil | Muito curta | Segundos a horas |

## Nota: buffer ≠ buffer pool

O [[wiki/concepts/buffer-pool]] do banco de dados, apesar do nome, funciona conceitualmente como **cache** (páginas retidas para reuso), não como buffer de fluxo — um bom exemplo de como o nome não define o conceito.

## Relação com outros conceitos

- [[wiki/concepts/cache-vs-buffer]] — a distinção completa entre os dois
- [[wiki/concepts/cache]] — o conceito oposto (reutilização, não fluxo)
- [[wiki/concepts/mensageria]] — fila/stream como buffer distribuído
- [[wiki/concepts/fila]] — a estrutura FIFO que sustenta o buffer de mensageria
- [[wiki/concepts/filas-e-workers]] — load leveling: absorver picos sem perder requisições
- [[wiki/concepts/latencia-streaming-ao-vivo]] — buffer de leitura antecipada do player

## Key Sources

- [[wiki/sources/cache-vs-buffer-diferenca-conceitual]] — buffer como absorvedor de diferença de velocidade, de I/O de hardware a filas de mensagem e streaming
