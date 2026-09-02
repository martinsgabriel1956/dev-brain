---
type: concept
title: "Ambulance Pattern"
aliases: ["padrão da ambulância", "message priority routing", "priority queue separation"]
date_created: 2026-09-02
date_updated: 2026-09-02
source_count: 1
tags: [system-design, arquitetura, filas, priorizacao, mensageria, mark-richards]
skill: tech-mentor-system-design
status: stub
---

# Ambulance Pattern

Padrão de roteamento para dar prioridade a certas mensagens dentro de um fluxo de mensageria — nome vem da imagem de carros abrindo espaço no trânsito para uma ambulância passar. Descrito por [[wiki/entities/mark-richards|Mark Richards]] em [[wiki/sources/ambulance-pattern-priorizacao-mensagens-mark-richards]].

## O Problema: Prioridade Embutida na Mensagem (não recomendada)

A implementação mais óbvia é marcar a mensagem com um campo de prioridade no header (numérico, ou baixo/médio/alto). Mensagens de alta prioridade sempre vão para a cabeça da fila.

Isso funciona no papel, mas quebra na prática: assim que mensagens de alta prioridade começam a chegar com volume, elas **sempre furam a fila**, desacelerando ou parando completamente o fluxo normal — um caso de **starvation**. É especialmente grave se o sistema espera resposta síncrona das mensagens normais: elas podem sofrer timeout por nunca chegarem a ser processadas enquanto houver tráfego prioritário suficiente.

## A Solução: Fila de Priorização Separada

Em vez de competir por posição dentro de uma única fila, o tráfego é dividido em **duas filas fisicamente separadas** — uma para o fluxo normal, uma dedicada à alta prioridade. Cada canal tem seu próprio caminho, e ambos podem ser processados **em paralelo**: a chegada de tráfego prioritário não bloqueia mais o fluxo normal, porque eles nunca competem pela mesma posição de fila.

## Refinamento: Fila + Instância de Serviço Dedicada

Uma evolução da separação de filas é dedicar também uma **instância de serviço** por fila — uma instância escuta só a fila de alta prioridade, outra só a fila normal, em vez de um único componente escutando as duas. Isso dá isolamento mais forte: se o componente de serviço vira gargalo, o tráfego crítico já tem capacidade reservada e isolada, sem competir por recursos com o tráfego normal.

O risco desse refinamento é a instância dedicada ficar ociosa a maior parte do tempo (tráfego de alta prioridade normalmente é minoria). Mitigação sugerida: configurar — idealmente em runtime, via configuração — qual fila cada instância escuta, permitindo redistribuir capacidade dinamicamente em vez de reservar hardware fixo ocioso.

## Relação com outros conceitos

- [[wiki/concepts/priority-queue]] — **não é a mesma coisa**. A estrutura de dados priority queue/heap reordena elementos dentro de uma única coleção por prioridade — é exatamente esse comportamento (o de maior prioridade sempre sai primeiro) que causa o starvation descrito aqui. O Ambulance Pattern evita esse problema *saindo* do modelo de fila única e usando canais físicos separados.
- [[wiki/concepts/back-pressure]] — starvation por competição de fluxos é um sintoma correlato ao desequilíbrio produtor/consumidor tratado em back pressure, ainda que a causa aqui seja competição entre dois fluxos concorrentes, não velocidade de consumo.
- [[wiki/concepts/filas-e-workers]] — a variante "fila + instância dedicada" é um caso específico de escalar workers por canal de trabalho, em vez de um pool único de workers genéricos.
- [[wiki/concepts/mensageria]] — o padrão se aplica sobre o modelo geral de comunicação assíncrona via filas (queue), não sobre streams com replay.

## Key sources

- [[wiki/sources/ambulance-pattern-priorizacao-mensagens-mark-richards]] — fonte primária e única até o momento
