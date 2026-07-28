---
type: source
title: "SGBD: Conceitos Fundamentais e Questões de Concurso"
aliases: ["sgbd concurso", "sgbdr vs nosql concurso", "aula sgbd"]
date_created: 2026-07-28
date_updated: 2026-07-28
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/sgbd-conceitos-fundamentais-questoes-concurso.md
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-07-28
source_count: 1
tags: [banco-de-dados, sgbd, sgbdr, nosql, acid, cap-theorem, concurso, backend]
skill: tech-mentor-backend
status: stable
---

## TL;DR

Aula preparatória para concurso público sobre SGBD (Sistema Gerenciador de Banco de Dados): definição, funções (transformar/apresentar dados, controlar acesso multiusuário, prover interfaces), o conceito de **visão** (view), a subdivisão entre **SGBDR** (relacional) e **SGBD NoSQL** (não relacional), os quatro modelos de NoSQL (chave-valor, documento, colunas, grafos) com exemplos canônicos, as propriedades **ACID** e o **Teorema CAP** — fechando com um bloco de questões reais de bancas de concurso brasileiras (CESPE/CEBRASPE, NC-UFPR, KIAC, IBADE, AOCP) e os gabaritos correspondentes.

## Key Claims

**Claim:** SGBD é o conjunto de programas que gerencia estrutura e dados de bancos de dados, funcionando como intermediário entre aplicações e a base de dados; funções centrais são transformar/apresentar dados, controlar acesso multiusuário e prover interfaces de comunicação.
**Evidence:** Consistente com [[wiki/concepts/acid]] e definição já presente na wiki via [[wiki/sources/como-escolher-banco-de-dados-historia-acid-cap]]. Reforçado por questão de banca (CESPE) que dá exatamente essa tripla de funções como gabarito.
**Confidence:** alta.

**Claim:** SGBDR (relacional) vs. SGBD NoSQL (não relacional) — SGBDR representa dados em tabelas (linhas = registros/tuplas, colunas = atributos/campos); NoSQL é um movimento que propõe estruturas alternativas.
**Evidence:** Alinhado com [[wiki/concepts/relational-vs-nosql]] e [[wiki/concepts/nosql]] já existentes na wiki.
**Confidence:** alta.

**Claim:** Existem quatro modelos de bancos NoSQL — chave-valor (DynamoDB, Redis, Riak, Memcached, Berkeley DB, LevelDB), documento (MongoDB, CouchBase/CouchDB, MarkLogic, RavenDB), colunas (Cassandra, HBase, Hypertable) e grafos (Neo4j, ArangoDB, AllegroGraph, InfoGrid, OrientDB/FlockDB, HyperGraphDB).
**Evidence:** Consistente com a tabela de tipos já presente em [[wiki/concepts/nosql]]; esta fonte adiciona exemplos adicionais por categoria (Riak, Berkeley DB, LevelDB, CouchBase, MarkLogic, RavenDB, Hypertable, AllegroGraph, InfoGrid, HyperGraphDB) não citados nas fontes anteriores da wiki.
**Confidence:** alta — lista de exemplos é factual e verificável, típica de bibliografia de concurso.

**Claim:** ACID (atomicidade, consistência, isolamento, durabilidade) são as quatro propriedades básicas de transação em bancos relacionais.
**Evidence:** Idêntico ao já documentado em [[wiki/concepts/acid]].
**Confidence:** alta.

**Claim:** Teorema CAP (Eric Brewer, ano 2000) — impossível manter Consistência, Disponibilidade e Tolerância a Partição simultaneamente; só dois de três. SGBDR e Neo4j mantêm CA; MongoDB/BigTable/HBase/Redis/Memcached mantêm CP; CouchDB/DynamoDB/SimpleDB/Cassandra mantêm AP.
**Evidence:** Direção geral consistente com [[wiki/concepts/cap-theorem]]. **Divergência a notar:** esta fonte classifica MongoDB, HBase e Redis como CP e Cassandra/DynamoDB como AP — mas a página [[wiki/concepts/cap-theorem]] já existente na wiki lista HBase como exemplo de CP (consistente) e Cassandra/DynamoDB como AP (consistente); porém o mesmo trecho da wiki cita Redis apenas como banco em memória sem posição CAP fixada, e o Neo4j como CA é uma classificação específica desta fonte não vista antes na wiki — vale registrar como ponto a confirmar, já que sistemas single-node como Neo4j (não clusterizado) tecnicamente não enfrentam partição da mesma forma que sistemas distribuídos.
**Confidence:** média — classificação de bancos específicos em CA/CP/AP varia conforme configuração (ex.: Cassandra pode ser tunado para CP via `QUORUM`); a fonte trata isso como categorização fixa, o que é uma simplificação didática típica de material de concurso.

**Claim:** O termo "visão" (view) em SGBD é o conceito que permite que diferentes usuários compartilhem dados e recursos de processamento — citado como gabarito de banca (KIAC).
**Evidence:** Conceito ainda não documentado como página própria na wiki; não há [[wiki/concepts/materialized-view]] equivalente direto (essa página trata de view materializada, um conceito relacionado mas distinto).
**Confidence:** alta quanto à definição factual; é definição de dicionário técnico usada em prova, não claim analítico.

## Entidades e Conceitos

- [[wiki/concepts/acid]]
- [[wiki/concepts/cap-theorem]]
- [[wiki/concepts/relational-vs-nosql]]
- [[wiki/concepts/nosql]]
- [[wiki/concepts/mongodb]]
- [[wiki/concepts/redis]]
- [[wiki/concepts/database-transactions]]
- [[wiki/entities/edgar-codd]]

## Open Questions

- A classificação didática de Neo4j como CA (consistência + disponibilidade, sem tolerância a partição) diverge da forma como bancos distribuídos costumam ser posicionados no CAP — Neo4j em modo single-instance não é realmente comparável a um cluster distribuído nesse eixo. Vale investigar se essa é uma simplificação comum em material de concurso ou um erro de categorização.
- A fonte não cobre PACELC nem a distinção entre "consistência" no sentido ACID vs. no sentido CAP com profundidade — apenas menciona que não são a mesma coisa, sem aprofundar (isso já está mais desenvolvido em [[wiki/concepts/cap-theorem]] e [[wiki/concepts/acid]]).
- Nenhuma página própria existe ainda para o conceito de "visão" (view) em SGBD — candidato a stub futuro se mais fontes tratarem do tema.

## Raw Quotes

> "O sgbd acaba gerenciando uma coleção de dados que estão ali na base de dados e que estão inter-relacionados e uma coleção de programas para acesso a esse banco de dados."

> "Os diversos sistemas gerenciadores de bancos de dados eles não conseguem nunca os três pontos do teorema CAP ao mesmo tempo... eles só conseguem manter dois desses elementos."

> "É preciso garantir que todos os servidores de um cluster terão cópias consistentes dos dados... a consistência aqui descrita não tem o mesmo significado que aquela consistência no ACID."

## Ver também

- [[wiki/sources/como-escolher-banco-de-dados-historia-acid-cap]]
- [[wiki/sources/acid-vs-base-garantias-bancos-de-dados]]
- [[wiki/sources/sql-nao-e-banco-de-dados-uncle-bob]]
