---
type: concept
title: "Object Space"
aliases: ["Object Spaces", "espaço de objetos"]
date_created: 2026-08-21
date_updated: 2026-08-21
source_count: 1
tags: [sistemas-distribuidos, coordenacao, tuple-space, exclusao-mutua]
skill: tech-mentor-backend
status: stub
---

# Object Space

Generalização do [[wiki/concepts/tuple-space|tuple space]] proposta por [[wiki/entities/david-gelernter|David Gelernter]] em Yale, anos 1980: em vez de tuplas de dados passivos, o espaço compartilhado guarda **objetos** — um provedor encapsula um serviço como objeto e o deposita no espaço, registrando-o num Object Directory; clientes localizam objetos por *properties lookup* e podem bloquear esperando um aparecer.

Objetos são **passivos** enquanto estão no espaço — seus métodos só podem ser invocados depois que um processo os **recupera para memória local**, usa o serviço, atualiza o estado e devolve o objeto ao espaço.

## Exclusão mútua embutida

Uma vez acessado, o objeto é **removido** do espaço e só reaparece quando liberado — nenhum outro processo pode tocá-lo enquanto está em uso. É a mesma garantia que um [[wiki/concepts/distributed-lock|distributed lock]] oferece, mas obtida pela própria semântica de remoção atômica (take), não por uma primitiva de lock separada.

## Key sources

- [[wiki/sources/tuple-space-wikipedia]] — definição, ciclo de vida do objeto no espaço, mecanismo de exclusão mútua
