---
type: concept
title: "Remontagem de Pacotes Fora de Ordem"
aliases: ["reordenação de pacotes","reassembly","reordering"]
date_created: 2026-09-30
date_updated: 2026-09-30
source_count: 1
tags: [networking, pacotes, sequencia, array, protocolo]
skill: tech-mentor-networking
status: stub
---

# Remontagem de Pacotes Fora de Ordem

Redes não garantem que pacotes cheguem na ordem enviada. Sem TCP ([[wiki/concepts/tcp-three-way-handshake]]) a aplicação precisa: (1) saber **quantos** pedaços existem; (2) **posicioná-los**.

Solução do [[wiki/entities/icmp-browser]]: os **4 primeiros bytes** do campo de dados de cada pacote informam o total; o receptor cria um [[wiki/concepts/array]] desse tamanho e grava cada pedaço na posição dada pelo **número de sequência** do [[wiki/concepts/icmp]]. O autor reconhece que não é o método mais eficiente, mas basta para prova de conceito. Lacunas (sem retransmissão, timeout, duplicatas): ver [[wiki/concepts/fragmentacao-ip]].

## Key sources

- [[wiki/sources/icmp-browser-navegar-na-internet-via-ping-go-michel-leonardo]] — total de pedaços nos 4 primeiros bytes + array indexado pela sequência
