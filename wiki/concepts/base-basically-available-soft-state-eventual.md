---
type: concept
title: "BASE (Basically Available, Soft State, Eventual Consistency)"
aliases: ["base", "basically available soft state eventual consistency", "garantias base"]
date_created: 2026-07-03
date_updated: 2026-07-03
source_count: 1
tags: [banco-de-dados, base, nosql, consistencia-eventual, disponibilidade, system-design]
skill: tech-mentor-system-design
status: stub
---

# BASE (Basically Available, Soft State, Eventual Consistency)

Conjunto de garantias mais fracas que [[wiki/concepts/acid]], comum (mas não universal) em bancos de dados não relacionais como Cassandra, MongoDB e DynamoDB. Prioriza disponibilidade e escalabilidade em vez de consistência forte.

## Os três componentes

- **Basically Available** — o sistema tenta responder mesmo se partes dele estiverem falhando. Um banco ACID não consegue oferecer isso da mesma forma, porque parte do sistema falhando compromete as outras garantias.
- **Soft State** — o estado interno pode mudar mesmo sem um novo input explícito, por causa da sincronização entre réplicas — existe um tempo de propagação.
- **Eventual Consistency** — se nenhuma nova escrita ocorrer, todas as réplicas eventualmente convergem para o mesmo valor. Não há garantia de quando, nem de que leituras intermediárias vejam o valor mais recente. Ver [[wiki/concepts/consistency-models]] para o espectro completo (Linearizable → Sequential → Causal → Eventual).

## BASE não é garantido, é comum

Bancos não relacionais não *sempre* seguem BASE — é um padrão de design que tende a aparecer nesses sistemas, não uma propriedade fixa da categoria "NoSQL". Alguns bancos NoSQL oferecem opções de consistência forte sob demanda (ex.: `ConsistentRead: true` no DynamoDB).

## O tradeoff com ACID

Garantir consistência forte ([[wiki/concepts/acid]]) tem custo de performance: para garantir, por exemplo, que um e-mail é único, o banco precisa varrer registros ou manter um [[wiki/concepts/database-index|índice]] consultado a cada escrita. BASE troca essa garantia por disponibilidade — se uma réplica ou partição está fora, o sistema aceita a escrita mesmo assim e sincroniza depois, em vez de recusar a transação.

## Quando faz sentido

Contextos onde uma inconsistência temporária não importa: redes sociais (contagem de likes), analytics, logs, cache, sistemas de recomendação. Contraste com contextos que pedem ACID: pagamentos, estoque, tickets. Ver [[wiki/concepts/relational-vs-nosql]].

## Relação com outros conceitos

- [[wiki/concepts/acid]] — o contraponto de garantias fortes
- [[wiki/concepts/consistency-models]] — eventual consistency é um ponto no espectro mais amplo de modelos de consistência
- [[wiki/concepts/cap-theorem]] — BASE é essencialmente a escolha AP (disponibilidade sobre consistência) sob partição
- [[wiki/concepts/relational-vs-nosql]] — decisão prática de quando usar cada tipo de garantia

## Key Sources

- [[wiki/sources/acid-vs-base-garantias-bancos-de-dados]]
