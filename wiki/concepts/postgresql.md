---
type: concept
title: "PostgreSQL"
aliases: ["postgres", "pg"]
date_created: 2026-04-22
date_updated: 2026-09-01
source_count: 10
tags: [banco-de-dados, postgresql, relacional, jsonb, vetorial]
skill: tech-mentor-system-design
status: stable
---

# PostgreSQL

Banco relacional open-source. Default para a maioria dos casos — migre só quando claramente não serve.

## Capacidades Além do Básico

| Feature | Substitui |
|---|---|
| `JSONB` | MongoDB para dados semi-estruturados |
| Full-text search nativo | Elasticsearch para casos simples |
| `pg_vector` extension | Pinecone/Weaviate para busca vetorial em IA |
| Timescaledb extension | InfluxDB para série temporal |

## Regra de Ouro

Não migre para NoSQL por performance antes de:
1. Criar os [[concepts/database-index]] corretos
2. Resolver [[concepts/n-plus-one]] queries
3. Configurar [[concepts/connection-pooling]] com PgBouncer
4. Avaliar [[concepts/read-replicas]] para reads

## Backend as a Service Ainda é Postgres

Supabase é um exemplo de BaaS que expõe Postgres via API REST/realtime. Chamar a API não elimina SQL — por baixo, o motor continua sendo Postgres executando SQL. Ver [[wiki/sources/sql-nao-e-banco-de-dados-uncle-bob]].

## JSONB como Ponte para NoSQL

A coluna `JSONB` indexável é o motivo prático de muita gente não precisar de uma infraestrutura poliglota: cobre boa parte do caso de uso que levaria alguém a adotar um banco não relacional para dado semi-estruturado. Ver [[wiki/concepts/relational-vs-nosql]] e [[wiki/sources/orm-sql-organizacao-regras-negocio-bancos-dados]].

## Processo por Conexão, Não Thread

Diferença arquitetural fundamental frente ao [[wiki/concepts/mysql|MySQL]]: o Postgres usa um **processo do sistema operacional** (fork) para cada conexão, não uma thread. Isolamento melhor — um processo travando não derruba os outros — mas custo maior: manter centenas de conexões IDLE consome recurso real mesmo sem query rodando. É por isso que [[wiki/concepts/connection-pooling|PgBouncer]] é considerado obrigatório em produção, e não apenas uma otimização — ele multiplexa milhares de conexões de aplicação em algumas centenas de conexões reais no banco (limite prático direto costuma ficar em 500–2.000).

## Postgres vs MySQL em Cargas Analíticas

Benchmarks independentes citados mostram Postgres até 50% mais rápido que MySQL em cargas com CTEs e agregações pesadas — uma das razões pelas quais equipes migram de MySQL para Postgres quando os relatórios/joins complexos começam a pesar. PostGIS (geoespacial) e pgvector (busca vetorial para IA) reforçam o mesmo padrão do JSONB: extensão nativa cobrindo o que levaria a adotar um banco especializado à parte.

## Migrations Contra um Postgres Local

Exemplo prático de fluxo de [[wiki/concepts/database-migration]] contra Postgres local: `docker-compose` sobe `postgres:16-alpine`, e um script `migrate` aplica arquivos de migration numerados (com `up`/`down` pareados) rastreando a versão atual do banco — permitindo aplicar só o que está pendente e reverter (`rollback`) de forma determinística. Ver [[wiki/sources/database-migrations-sql-cru-vs-orm-drizzle]].

## Full-Text Search em Profundidade — tsvector, tsquery e GIN

O "Full-text search nativo" citado acima significa, na prática: `to_tsvector(idioma, texto)` converte o conteúdo em lexemas indexáveis, `to_tsquery`/`plainto_tsquery` converte o termo pesquisado, e o operador `@@` faz o match entre os dois. Um índice `GIN` sobre a expressão `to_tsvector(...)` é o que transforma isso de "mais lento que `LIKE`" (recalculando o vetor a cada chamada) em ordens de grandeza mais rápido — ver [[wiki/concepts/full-text-search]] para a demonstração completa.

O diferencial real frente ao [[wiki/concepts/mysql|MySQL]] (que também tem Full-Text Search via `FULLTEXT INDEX`) é o **stemming avançado com suporte a idioma**: o Postgres reduz variações morfológicas ("programador", "programando", "programação") ao mesmo lexema automaticamente, entende plural/singular sem precisar da forma exata no texto, e permite configurar tesauros (sinônimos) — nenhum dos dois recursos existe no MySQL. Ver [[wiki/sources/full-text-search-mysql-postgresql]].

## Por Baixo do Motor: Buffer Pool, WAL, MVCC

O comportamento descrito acima (processo por conexão, PgBouncer obrigatório) é a camada de acesso; por baixo dela, o motor relacional segue o fluxo genérico documentado em [[wiki/sources/como-um-banco-de-dados-funciona-por-dentro]]: páginas em [[wiki/concepts/buffer-pool]], durabilidade via [[wiki/concepts/write-ahead-log]], concorrência via [[wiki/concepts/mvcc]] e [[wiki/concepts/isolation-levels]] (Read Committed é o default do Postgres), e recuperação via checkpoints ([[wiki/concepts/database-recovery]]). O `autovacuum` citado na skill `tech-mentor-data` é a implementação concreta de Postgres para limpar as versões antigas que o MVCC acumula.

## PG Vector Como Ponto de Entrada para RAG

Reforçando o padrão já descrito acima (extensão nativa cobrindo o que levaria a adotar um banco especializado à parte): [[wiki/sources/rag-introducao-pipeline-completo]] cita o Postgres com a extensão `pgvector` como opção viável para armazenar embeddings de um pipeline de [[wiki/concepts/rag-arquitetura-avancada|RAG]] — "aguenta bastante carga" e roda em produção mesmo havendo bancos vetoriais dedicados (Pinecone, Weaviate). Cada registro guarda o vetor (embedding), o texto cru do [[wiki/concepts/chunking|chunk]] e metadados de filtro, na mesma linha do padrão JSONB já documentado aqui: menos infraestrutura poliglota.

## Particionamento Nativo: RANGE vs. LIST

Feature nativa do motor (`PARTITION BY RANGE|LIST|HASH`), diferente de [[wiki/concepts/sharding]] — continua sendo o mesmo banco, com o motor roteando cada linha para a tabela filha certa e permitindo *partition pruning* em queries filtradas pela coluna de particionamento. `LIST` cabe quando a coluna tem um conjunto conhecido e finito de valores (UF, categoria, tenant); sem uma partição `DEFAULT` como catch-all, um INSERT para um valor não mapeado falha. Ver [[wiki/concepts/particionamento-de-tabela]] para RANGE vs. LIST em detalhe.

## Key Sources

- [[sources/banco-de-dados]]
- [[wiki/sources/como-um-banco-de-dados-funciona-por-dentro]] — mecânica interna genérica (buffer pool, WAL, MVCC, isolation levels, checkpoint/recovery) que fundamenta o comportamento específico do Postgres já documentado acima
- [[wiki/sources/sql-nao-e-banco-de-dados-uncle-bob]]
- [[wiki/sources/orm-sql-organizacao-regras-negocio-bancos-dados]]
- [[wiki/sources/como-escolher-banco-de-dados-historia-acid-cap]] — arquitetura processo-por-conexão, PgBouncer como padrão, e comparação de performance analítica com MySQL
- [[wiki/sources/database-migrations-sql-cru-vs-orm-drizzle]] — migrations cruas via docker-compose + script de versão contra Postgres local
- [[wiki/sources/full-text-search-mysql-postgresql]] — tsvector/tsquery/GIN, stemming por lexema, e comparação de performance com/sem índice
- [[wiki/sources/infraestrutura-como-codigo-cdk-aws]] — citado como o banco de dados de exemplo numa stack ilustrativa de [[wiki/concepts/infraestrutura-como-codigo|IaC]] (dois Lambdas atrás de um API Gateway, ambos conectados ao mesmo Postgres, sem acesso direto à internet); menção arquitetural breve, sem claim técnico novo sobre o motor
- [[wiki/sources/rag-introducao-pipeline-completo]] — `pgvector` como vector store viável para RAG em produção, com exemplo de estrutura de registro (embedding + texto cru + metadados)
- [[wiki/sources/particionamento-por-list-postgresql-sql-30-dias]] — `PARTITION BY LIST`, partição DEFAULT como catch-all, chave primária composta em tabela particionada
