---
type: concept
title: "Escalonador"
aliases: ["scheduler", "escalonador de processos", "CPU scheduler", "agendador"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [sistema-operacional, scheduling, concorrência, cs-fundamentals]
skill: cs-fundamentals
status: stable
---

# Escalonador (Scheduler)

Componente do SO que decide qual processo ou thread roda em qual CPU, por quanto tempo e quando cede lugar para outro.

## Por que existe

Com dezenas de processos e uma CPU, alguém precisa decidir quem roda em qual momento. O escalonador faz essa arbitragem de forma justa e eficiente.

## Algoritmos

**Round-Robin**
- Cada processo recebe uma fatia de tempo igual (ex: 10ms)
- Depois da fatia, vai para o fim da fila, próximo assume
- Justo, mas ignora prioridade — processo de renderização de vídeo recebe o mesmo que processo esperando input do usuário

**Filas de Prioridade**
- Processos mais urgentes ficam em fila atendida primeiro
- Sistemas reais usam múltiplas filas com prioridades diferentes
- Problema: starvation — processos de baixa prioridade podem nunca rodar

**Aging**
- Solução para starvation: processo esperando há muito tempo tem prioridade aumentada progressivamente
- Garante que todo processo eventualmente execute

**Linux CFS (Completely Fair Scheduler)**
- Padrão para processos normais — time slice proporcional ao `nice value`
- Processos de real-time: FIFO ou Round-Robin com prioridade máxima

## Como o escalonador retoma o controle

O processo está rodando — como o escalonador interrompe ele?

Via [[concepts/interrupcao-de-hardware]]: um timer de hardware dispara a cada N ms, gerando uma interrupção que transfere controle ao SO. O escalonador decide quem roda em seguida.

## Ver também

- [[concepts/context-switch]] — operação que o escalonador executa ao trocar processos
- [[concepts/interrupcao-de-hardware]] — mecanismo que aciona o escalonador periodicamente
- [[concepts/processo]] — entidade agendada pelo escalonador
- [[concepts/thread]] — unidade de execução agendada pelo kernel

## Key Sources

- [[sources/sistema-operacional-por-baixo-dos-panos]]
