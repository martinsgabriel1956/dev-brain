---
type: source
title: "The Ambulance Pattern (Lição 56 — Developer to Architect)"
aliases: ["ambulance pattern", "padrão da ambulância", "message priority vs priority queue"]
date_created: 2026-09-02
date_updated: 2026-09-02
source_count: 0
tags: [system-design, arquitetura, filas, priorizacao, mensageria, mark-richards]
skill: tech-mentor-system-design
status: draft
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/ambulance-pattern-priorizacao-mensagens-mark-richards.md
source_url: https://www.developertoarchitect.com/lessons/lesson56.html
author: "Mark Richards"
date_published: 2019-04-08
date_ingested: 2026-09-02
---

# The Ambulance Pattern (Lição 56 — Developer to Architect)

## TL;DR

[[wiki/entities/mark-richards|Mark Richards]] apresenta o **Ambulance Pattern**: como dar prioridade a certas requisições dentro de um fluxo de mensageria, do mesmo jeito que carros abrem espaço para uma ambulância passar no trânsito. Compara duas técnicas: (1) **prioridade embutida na mensagem** (header com valor numérico ou baixo/médio/alto) — fácil de implementar, mas causa **starvation** do fluxo normal, porque mensagens de alta prioridade sempre furam a fila e podem travar completamente o processamento normal, gerando timeouts; (2) **fila de priorização** — separar fisicamente o tráfego em duas filas (normal e alta prioridade), permitindo processamento verdadeiramente paralelo sem que um fluxo bloqueie o outro. Aponta ainda um refinamento: combinar a fila separada com uma **instância de serviço dedicada** por fila, útil para isolar gargalos e escalar cada canal de forma independente — com o cuidado de configurar (idealmente em runtime) qual fila cada instância escuta, para não deixar a instância dedicada ociosa a maior parte do tempo.

## Key Claims

| Claim | Evidência |
|---|---|
| Priorizar mensagens via campo de prioridade no header (numérico ou baixo/médio/alto) é uma técnica ruim na prática | Mensagens marcadas como alta prioridade sempre vão para a cabeça da fila, desacelerando ou parando o processamento do fluxo normal — especialmente grave quando há espera síncrona por resposta, causando timeout |
| A técnica de prioridade na mensagem resolve "chegar na frente" mas cria starvation do fluxo normal | Demonstração visual: mensagens normais entram em fila única; assim que mensagens de alta prioridade passam a chegar, elas sempre vão para o topo, e o fluxo normal para de avançar |
| A alternativa recomendada é dividir fisicamente a fila em duas: uma normal, uma de alta prioridade | Cada tipo de mensagem tem seu próprio canal; ambos podem ser processados ao mesmo tempo, sem que a chegada de tráfego prioritário trave o fluxo normal |
| Combinar a fila de priorização com uma instância de serviço dedicada por fila melhora ainda mais o isolamento | Uma instância escuta apenas a fila de alta prioridade, outra escuta apenas a normal — processamento paralelo real, útil para lidar com gargalos e escalar cada canal de forma independente |
| Sem cuidado, a instância dedicada à fila de alta prioridade fica ociosa a maior parte do tempo | Recomendação de configurar (idealmente em runtime) qual fila cada instância escuta, permitindo redistribuir capacidade dinamicamente em vez de reservar hardware fixo ocioso |

## Conceitos

- [[wiki/concepts/ambulance-pattern]] (novo) — página dedicada ao padrão em si, com as duas técnicas e o refinamento
- [[wiki/concepts/mensageria]] — o Ambulance Pattern é uma técnica de roteamento dentro do modelo geral de queue-based messaging
- [[wiki/concepts/filas-e-workers]] — a variante "fila + instância dedicada" é um caso específico de separar workers por canal de trabalho
- [[wiki/concepts/priority-queue]] — falso cognato: o Ambulance Pattern **não** usa a estrutura de dados heap/priority-queue; usa filas físicas separadas justamente para evitar o problema de starvation que uma fila de prioridade única (baseada em campo de prioridade) causaria
- [[wiki/concepts/back-pressure]] — starvation do fluxo normal é um sintoma de desequilíbrio não controlado entre dois fluxos concorrendo pelo mesmo canal, tema irmão do back pressure entre produtor e consumidor

## Open Questions

- Vídeo curto (~5 min) sem exemplos de código ou nomes de tecnologia específicos (não cita SQS FIFO, RabbitMQ priority queue plugin, Kafka, etc.) — tratado aqui em nível conceitual/arquitetural, sem mapeamento a uma implementação concreta.
- Não fica claro no vídeo se "prioridade na mensagem" se refere a um recurso nativo de broker (ex.: RabbitMQ tem suporte nativo a priority queue via `x-max-priority`) ou a uma convenção de aplicação lida manualmente pelo consumidor — a crítica de Richards parece mirar ambos os casos, mas o vídeo não distingue.
- Skill drift novamente confirmado: caminho do `CLAUDE.md` (`/home/nemomartins/Documentos/new/skills/`) não existe nesta máquina — usado `/home/gabriel-martins/Documentos/skills/`.

## Raw Quotes

> "The ambulance pattern creates a fast-path for requests that need to go ahead of others - just like cars pulling over to let an ambulance through."

> "Notice how these messages are normally being processed, but now we have a high priority message, and this is a message that needs to go in front of everybody else, just like that ambulance."

> "Because those are set to high priority, those will always go to the head of the queue, and slow down or even stop any other messages from being processed — especially if we're waiting for a response from those messages, and those transactions may timeout."

> "Now, without having to play around with message priority, notice both of these messages can now be processed at the same time — therefore not slowing down the normal message flow, but allowing this other message, the high priority message, to actually get through."

## Key Sources

_Este é o documento primário._
