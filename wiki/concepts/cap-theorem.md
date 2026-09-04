---
type: concept
title: "Teorema CAP"
aliases: ["CAP theorem", "CAP", "consistência disponibilidade partição", "PACELC"]
date_created: 2026-06-26
date_updated: 2026-09-04
source_count: 7
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

## Marcador de Nível Sênior em Entrevista

[[wiki/concepts/niveis-de-senioridade-system-design]] cita CAP explicitamente como vocabulário esperado de candidatos sênior/sênior-plus, junto ao tradeoff latência vs. vazão vs. disponibilidade — não é cobrado de júnior e aparece só "em algum nível" para pleno.

## Consistência é Negociável Conforme o Domínio

[[wiki/sources/anatomia-entrevista-system-design-bigtech]] ilustra a escolha C vs. A com dois extremos concretos: transação bancária não pode abrir mão de consistência forte; contador de likes de vídeo pode aceitar garantia BASE (301 vs. 302 exibido não muda nada na prática). A compreensão do problema — não uma regra técnica universal — é o que define essa fronteira. A mesma fonte liga o tradeoff de escrita do SQL (mais difícil de escalar) ao motivo pelo qual sistemas de alto throughput preferem NoSQL e abrem mão de ACID.

## Escolha de Banco como Decisão de Negócio, Não Técnica

[[wiki/sources/como-escolher-banco-de-dados-historia-acid-cap]] resume a implicação prática do CAP para escolha de stack: bancos relacionais (MySQL, PostgreSQL, Oracle) escolhem CP — preferem indisponibilidade temporária a dado errado; bancos NoSQL em geral escolhem AP via consistência eventual. Quando alguém recomenda "usa MongoDB que é mais rápido", o que está sendo dito de fato é que aquele banco abre mão de consistência forte em troca de disponibilidade/escala — uma troca que pode ser excelente ou desastrosa dependendo do domínio.

## Classificação Didática de Concurso (CA / CP / AP)

Material de prova de concurso costuma ensinar o CAP com categorização fixa por produto, útil para memorização mas simplificada: **CA** (consistência + disponibilidade, sem tolerância a partição) — SGBDR em geral e Neo4j; **CP** — MongoDB, BigTable, HBase, Redis, Memcached; **AP** — CouchDB, DynamoDB, SimpleDB, Cassandra. Vale notar que essa fonte inclui Neo4j como exemplo de CA, o que é uma simplificação: um Neo4j single-instance não enfrenta partição de rede da mesma forma que um cluster distribuído, então classificá-lo no eixo CAP tradicional (pensado para sistemas distribuídos) é didaticamente conveniente mas tecnicamente questionável. Ver [[wiki/sources/sgbd-conceitos-fundamentais-questoes-concurso]].

## Paralelo com Local-First vs Offline-First

[[wiki/sources/local-first-vs-offline-first]] descreve, para arquiteturas de sincronização client-side, um trade-off estruturalmente parecido com CP vs. AP: em [[wiki/concepts/offline-first]] o servidor é a autoridade e a escrita local só é definitiva após aceite remoto (análogo a priorizar consistência); em [[wiki/concepts/local-first]] cada réplica local aceita escritas offline e converge depois (análogo a priorizar disponibilidade). Não é o mesmo teorema (CAP é sobre partição de rede em sistemas distribuídos server-side; local-first é sobre onde reside a autoridade do dado entre cliente e servidor), mas a pergunta de fundo — "se duas cópias divergem, quem tem razão?" — é a mesma forma de decisão.

## Key sources

- [[wiki/sources/local-first-vs-offline-first]] — paralelo estrutural entre CP/AP e offline-first/local-first
- [[wiki/sources/escalabilidade-vertical-horizontal-system-design]] (menção superficial — necessita fonte dedicada)
- [[wiki/sources/acid-vs-base-garantias-bancos-de-dados]] — BASE como formalização prática da escolha AP
- [[wiki/sources/system-design-por-nivel-junior-pleno-senior]]
- [[wiki/sources/anatomia-entrevista-system-design-bigtech]]
- [[wiki/sources/como-escolher-banco-de-dados-historia-acid-cap]] — CP vs AP aplicado à escolha de MySQL/PostgreSQL/Oracle (CP) vs. MongoDB/Redis-eventual (AP tendencial)
- [[wiki/sources/sgbd-conceitos-fundamentais-questoes-concurso]] — categorização CA/CP/AP fixa por produto, como cobrada em prova de concurso
