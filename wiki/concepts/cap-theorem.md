---
type: concept
title: "Teorema CAP"
aliases: ["CAP theorem", "CAP", "consistência disponibilidade partição", "PACELC"]
date_created: 2026-06-26
date_updated: 2026-07-03
source_count: 2
tags: [system-design, sistemas-distribuidos, cap-theorem, consistencia, disponibilidade]
skill: tech-mentor-system-design
status: stub
---

# Teorema CAP

Em um sistema distribuído, é impossível garantir simultaneamente as três propriedades abaixo. Quando ocorre uma partição de rede, você precisa escolher entre **consistência** ou **disponibilidade**.

| Propriedade | Definição |
|---|---|
| **Consistency (C)** | Toda leitura retorna o dado mais recente ou um erro |
| **Availability (A)** | Toda requisição recebe uma resposta (pode ser dado desatualizado) |
| **Partition Tolerance (P)** | O sistema continua operando mesmo quando nós perdem comunicação |

> Partição de rede sempre pode acontecer em sistemas distribuídos reais. Portanto, a escolha real é entre **CP** ou **AP**.

## CP vs AP

| | CP | AP |
|---|---|---|
| **Prioriza** | Consistência | Disponibilidade |
| **Em partição** | Recusa responder (erro) até consistência restaurada | Responde com dado potencialmente desatualizado |
| **Exemplos** | HBase, Zookeeper, etcd | Cassandra, DynamoDB, CouchDB |
| **Quando usar** | Transações financeiras, inventário crítico | Feeds sociais, analytics, recomendações |

## Relação com escalabilidade

O Teorema CAP se torna relevante quando você distribui dados horizontalmente — seja via [[sharding]], [[replicacao-de-banco]] ou sistemas de mensageria. Cada estratégia implica uma posição no espectro CAP.

## Nota sobre PACELC

O CAP descreve o comportamento *em partição*. PACELC estende: mesmo sem partição, há trade-off entre **latência** e **consistência**. Sistemas CP tendem a ter latência maior (esperam confirmação de múltiplos nós).

> Esta é uma página stub — o Teorema CAP merece fonte dedicada para profundidade. Ver open questions em [[wiki/sources/escalabilidade-vertical-horizontal-system-design]].

## Relação com outros conceitos

- [[escalabilidade-horizontal]] — distribuir dados entre máquinas é quando o CAP se torna relevante
- [[sharding]] — a escolha da shard key e do modelo de consistência reflete o CAP
- [[replicacao-de-banco]] — replicação assíncrona = AP; síncrona = CP

## Relação com ACID/BASE

A escolha AP do teorema CAP é essencialmente o que [[wiki/concepts/base-basically-available-soft-state-eventual|BASE]] formaliza como padrão de design (Basically Available + Eventual Consistency); a escolha CP tende a se aproximar das garantias de [[wiki/concepts/acid]]. Ver exemplos de domínio por tipo de garantia em [[wiki/sources/acid-vs-base-garantias-bancos-de-dados]].

## Key sources

- [[wiki/sources/escalabilidade-vertical-horizontal-system-design]] (menção superficial — necessita fonte dedicada)
- [[wiki/sources/acid-vs-base-garantias-bancos-de-dados]] — BASE como formalização prática da escolha AP
