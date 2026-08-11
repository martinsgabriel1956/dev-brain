---
type: concept
title: "NoSQL"
aliases: ["not only sql", "bancos não relacionais"]
date_created: 2026-04-22
date_updated: 2026-08-10
source_count: 6
tags: [banco-de-dados, nosql, mongodb, redis, cassandra, system-design]
skill: tech-mentor-system-design
status: stable
---

# NoSQL

Categoria de bancos de dados que não seguem o modelo relacional. Cada tipo resolve um problema diferente.

| Tipo | Exemplos | Use para |
|---|---|---|
| **Document** | MongoDB, Firestore | Dados semi-estruturados, schema flexível |
| **Key-Value** | Redis, DynamoDB | Acesso por chave única, alta performance |
| **Wide-Column** | Cassandra, DynamoDB | Escrita massiva, série temporal, IoT |
| **Graph** | Neo4j, Neptune | Relacionamentos complexos |
| **Search** | Elasticsearch | Full-text search, faceted search |

## Quando Não Usar

- Dados financeiros ou transacionais → use relacional com [[concepts/acid]]
- Relacionamentos complexos entre entidades → JOINs relacionais são mais simples
- Quando você quer schema flexível mas já tem PostgreSQL → use `JSONB`

## Consistência

A maioria oferece consistência eventual. Para inventário crítico e saldos, isso é inaceitável. → [[concepts/relational-vs-nosql]]

## Escalabilidade

Bancos NoSQL escalam melhor **horizontalmente** ([[escalabilidade-horizontal]]): adicionam máquinas ao invés de mais recursos na mesma. Bancos relacionais escalam melhor verticalmente (mais CPU/RAM).

## Não Confundir com a Discussão "SQL Embutido no Código"

Uma thread analisada em [[wiki/sources/sql-nao-e-banco-de-dados-uncle-bob]] gerou confusão generalizada: pessoas comparando SQL a NoSQL quando a discussão original era sobre **acoplar aplicação a SQL como linguagem de query** (vs. abstrair via ORM/DSL) — um eixo ortogonal a "qual modelo de dados usar". Firestore/MongoDB não substituem a pergunta "devo escrever SQL cru no código", eles resolvem um problema diferente (modelo de dados documental vs. relacional).

## MongoDB: Exemplo Concreto de Schema Variável

Caso didático de [[wiki/sources/como-escolher-banco-de-dados-historia-acid-cap]]: um e-commerce que vende notebook (processador, RAM, polegadas), camiseta (tamanho, cor, material) e livro (ISBN, autor, edição) no mesmo catálogo. Em SQL, as duas opções são ruins — tabela com 200 colunas majoritariamente nulas, ou arquitetura EAV (entity-attribute-value) tecnicamente correta mas com péssima performance de query. No MongoDB, cada produto é um documento só com os campos que fazem sentido para ele; um novo tipo de produto começa a ser inserido sem migration, sem `ALTER TABLE`, sem downtime. Ver [[wiki/concepts/mongodb]].

## Termo de Concurso: SGBD NoSQL e Seus Quatro Modelos

Provas de concurso brasileiras tratam "SGBD NoSQL" como termo formal (em oposição a SGBDR) e cobram os quatro modelos com listas de exemplos mais extensas que o uso corrente: **chave-valor** (DynamoDB, Redis, Riak, Memcached, Berkeley DB, LevelDB), **documento** (MongoDB, CouchBase, CouchDB, MarkLogic, RavenDB), **colunas** (Cassandra, HBase, Hypertable) e **grafos** (Neo4j, ArangoDB, AllegroGraph, InfoGrid, OrientDB/FlockDB, HyperGraphDB). Ver [[wiki/sources/sgbd-conceitos-fundamentais-questoes-concurso]].

## Key Sources

- [[sources/banco-de-dados]]
- [[wiki/sources/como-arquitetar-com-cache-e-redis]]
- [[wiki/sources/sql-nao-e-banco-de-dados-uncle-bob]]
- [[wiki/sources/como-escolher-banco-de-dados-historia-acid-cap]] — exemplo concreto de catálogo com schema variável (notebook/camiseta/livro) e limite de conexões do MongoDB em instância única
- [[wiki/sources/sgbd-conceitos-fundamentais-questoes-concurso]] — lista estendida de exemplos por modelo (chave-valor, documento, colunas, grafos), como cobrada em concurso
- [[wiki/sources/escalar-para-um-milhao-de-usuarios]] — regra prática de quando sair do "SQL por padrão": latência super baixa, esquema flexível (logs/JSON) ou throughput muito alto (armazenar todos os requests); também NoSQL como store externo de sessões/preferências fora dos servidores stateless
