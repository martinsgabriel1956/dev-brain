---
type: concept
title: "Escalabilidade Independente"
aliases: ["scale independently", "escalar por serviço"]
date_created: 2026-10-02
date_updated: 2026-10-02
source_count: 1
tags: [escalabilidade, arquitetura-distribuida, microsservicos]
skill: tech-mentor-system-design
status: stub
---

# Escalabilidade Independente

Capacidade de escalar **apenas o componente sobrecarregado**, sem replicar o sistema inteiro: serviço de pagamentos numa Black Friday, serviço de entrega de vídeo num lançamento muito esperado. É o primeiro motivo citado para [[wiki/concepts/arquitetura-distribuida]]; num [[wiki/concepts/monolito]] só se escala a aplicação toda. Base técnica: [[wiki/concepts/escalabilidade-horizontal]]. Custo: mais infraestrutura e [[wiki/concepts/observabilidade]]; o vídeo não dá números.

## Key sources

- [[wiki/sources/arquitetura-distribuida-introducao-historico-desafios-bernardo-lobato]] — introdução da série de arquiteturas distribuídas de [[wiki/entities/bernardo-lobato]]
