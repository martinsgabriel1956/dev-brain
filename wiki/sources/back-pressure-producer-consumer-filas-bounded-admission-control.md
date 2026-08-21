---
type: source
title: "Back Pressure: Produtor, Consumidor, Filas Bounded e Admission Control"
aliases: ["back pressure explicado", "low watermark high watermark fila", "produtor mais rápido que consumidor"]
date_created: 2026-08-14
date_updated: 2026-08-14
source_count: 0
tags: [tech-mentor-system-design, back-pressure, producer-consumer, filas, admission-control, rate-limiting, auto-scaling, bullmq, redis]
skill: tech-mentor-system-design
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/back-pressure-producer-consumer-filas-bounded-admission-control.md
source_url:
author: desconhecido (canal de vídeo)
date_published:
date_ingested: 2026-08-14
---

# Back Pressure: Produtor, Consumidor, Filas Bounded e Admission Control

## TL;DR

Transcrição de vídeo que explica back pressure como o descasamento de velocidade entre produtor e consumidor em sistemas distribuídos, enfatiza que o primeiro passo é identificar o [[wiki/concepts/gargalo]] real antes de escalar hardware, e demonstra na prática — via dois exemplos de código com fila em memória e depois com BullMQ + Redis — a técnica de **low watermark / high watermark** para pausar e retomar o produtor conforme o tamanho da fila.

## Key Claims

1. **Back pressure é o problema de um produtor produzir mais rápido do que o consumidor consegue consumir.** Ocorre em qualquer sistema com relação produtor/consumidor — web crawler salvando páginas para um indexador, upload de vídeo para um serviço de compressão, etc. Sem tratamento explícito, o próprio sistema aplica back pressure de forma implícita: via OOM, crash ou degradação silenciosa (claim já registrada em [[wiki/concepts/back-pressure]]).
2. **A fila entre produtor e consumidor é um buffer com limite físico, não uma solução definitiva.** Ela amortece picos de curto prazo, mas se o descasamento de velocidade é sustentado, a fila cresce indefinidamente: itens envelhecem (podem já estar desatualizados quando processados) e o uso de memória pode crescer até crashar o sistema. Aumentar a capacidade da fila só empurra o problema para frente.
3. **Identificar o gargalo real é o primeiro passo, antes de qualquer solução.** Exemplo dado: se o consumidor só processa 10 itens/min porque o banco de dados tem essa limitação de velocidade, aumentar o hardware do consumidor não resolve nada — o gargalo está no banco, não no consumidor.
4. **Técnicas baratas antes de escalar hardware:** podar *stale jobs* (itens antigos, com erro ou irrelevantes) da fila; priorizar itens mais importantes; processar em **batches** (ex.: batch insert em vez de inserts individuais) para aumentar vazão sem aumentar capacidade de hardware.
5. **Fila bounded (limitada) é considerada boa prática.** Impedir que a fila cresça infinitamente evita que o sistema estoure — mas transfere o problema para o produtor, que precisa lidar com rejeição (perder itens) ou risco de estourar sua própria memória se o retry for mal implementado (retry infinito).
6. **Admission control e rate limit no produtor** são mecanismos complementares: admission control rejeita novos jobs quando a fila está cheia (implementável no produtor ou como middleware); rate limit no produtor trava a taxa de produção na mesma capacidade do consumidor — produzir mais rápido que isso só desperdiça recurso computacional.
7. **Mais consumidores em paralelo (cluster) e paralelização da fila** aumentam a vazão do sistema. Auto scaling baseado no tamanho da fila é viável, mas mais difícil de configurar — requer monitoramento e alertas para manter a fila num tamanho razoável.
8. **Retry entre produtor e fila deve ser usado com cautela.** Uma política de retry muito agressiva pode adicionar ainda mais pressão sobre um sistema que já está sobrecarregado.
9. **Demonstração prática — técnica de low watermark / high watermark:** implementação com fila BullMQ sobre Redis (Docker) em que o produtor checa o tamanho da fila periodicamente; se ultrapassa o *high watermark* (100 jobs), o produtor pausa completamente; ao cair abaixo do *low watermark* (30 jobs), retoma a produção. Resultado observado: o tamanho da fila oscila entre ~30 e ~93 itens, e o lag nunca cresce sem limite — em contraste com o exemplo sem controle, onde 922 jobs foram aceitos contra apenas 123 processados (lag de 799).

## Entidades Mencionadas

- **BullMQ** — biblioteca de filas usada na demo com watermark.
- **Redis** — broker subjacente ao BullMQ, rodando via Docker no exemplo.

## Conceitos Tocados

- [[wiki/concepts/back-pressure]]
- [[wiki/concepts/fila]]
- [[wiki/concepts/filas-e-workers]]
- [[wiki/concepts/buffer]]
- [[wiki/concepts/gargalo]]
- [[wiki/concepts/admission-control]]
- [[wiki/concepts/rate-limiting]]
- [[wiki/concepts/retry-backoff]]
- [[wiki/concepts/auto-scaling]]
- [[wiki/concepts/escalabilidade-horizontal]]
- [[wiki/concepts/bullmq]]
- [[wiki/concepts/redis]]

## Open Questions

- Fonte não cita autor, canal ou referências formais — mesmo padrão observado em [[wiki/sources/pub-sub-message-queue-bullmq-na-pratica]] e outras fontes deste wiki.
- O vídeo não detalha o algoritmo de rate limit no produtor (token bucket? sliding window?) nem compara com as estratégias já cobertas em [[wiki/concepts/rate-limiting]] — trata apenas como "trava a taxa na mesma capacidade do consumidor", sem entrar no mecanismo de implementação.
- A técnica de low/high watermark demonstrada aqui não tinha página própria no wiki antes desta ingestão — criada como stub em [[wiki/concepts/admission-control]]; pode merecer página independente se mais fontes tratarem do tema com profundidade.
