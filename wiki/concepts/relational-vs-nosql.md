---
type: concept
title: "Relacional vs NoSQL"
aliases: ["sql vs nosql", "relational vs document", "escolha de banco"]
date_created: 2026-04-22
date_updated: 2026-07-27
source_count: 5
tags: [banco-de-dados, nosql, postgresql, system-design, trade-offs]
skill: tech-mentor-system-design
status: stable
---

# Relacional vs NoSQL

Não existe escolha universal. Cada tipo resolve um problema diferente.

## Trade-offs

| Aspecto | Relacional | NoSQL |
|---|---|---|
| **Consistência** | [[concepts/acid]] completo | Eventual (geralmente) |
| **Queries** | JOINs complexos, agregações | Simples, por chave |
| **Escala de escrita** | Vertical (um primário) | Horizontal nativo |
| **Schema** | Rígido — segurança + integridade | Flexível — agilidade |

## Decisão

- Financeiro, multi-entidade, transações → **Relacional** ([[concepts/postgresql]])
- Dados semi-estruturados, schema muda muito → **Document** (MongoDB)
- Cache, sessão, acesso por chave → **Key-Value** (Redis)
- Escrita massiva, IoT, série temporal → **Wide-Column** (Cassandra)
- Relacionamentos complexos → **Graph** (Neo4j)
- Full-text search → **Search** (Elasticsearch)

## Antes de Migrar

[[concepts/postgresql]] consegue JSONB, full-text search básico, pg_vector e Timescaledb. Avalie extensões antes de adicionar complexidade operacional.

## Eixo Diferente: SQL Embutido no Código vs. Modelo de Dados

Essa comparação (relacional vs. NoSQL) é frequentemente confundida com uma discussão diferente: se a aplicação deve escrever SQL diretamente no código ou abstrair isso via [[wiki/concepts/orm]]/[[wiki/concepts/domain-specific-language]]. São eixos ortogonais — você pode usar SQL cru ou um ORM tanto num banco relacional quanto (via camadas de tradução) sobre um BaaS documental. Ver [[wiki/sources/sql-nao-e-banco-de-dados-uncle-bob]].

## Por Domínio de Negócio: ACID vs. BASE

Além do eixo técnico (queries, escala, schema), a escolha também depende do domínio:

| Quer consistência forte ([[wiki/concepts/acid]]) | Quer disponibilidade/escala ([[wiki/concepts/base-basically-available-soft-state-eventual|BASE]]) |
|---|---|
| Pagamentos, bancos, estoque, tickets | Redes sociais, analytics, logs, cache, recomendação |

Na prática, essa regra não é absoluta: já existem bancos relacionais usados onde não precisavam e bancos NoSQL usados em instituições de pagamento. Ver [[wiki/sources/acid-vs-base-garantias-bancos-de-dados]].

## Critério Prático: Precisa de Junções Múltiplas?

Se o sistema precisa alcançar um mesmo dado por vários caminhos diferentes via junções (essencialmente teoria dos conjuntos), a necessidade de um schema formalizado e relacionamentos declarados aponta para banco relacional. Já cenários de dado não estruturado, machine learning ou data lake tendem a se encaixar melhor em não relacional — não como categoria única, mas por estratégia (grafo, documento, etc., conforme a necessidade específica). Bancos relacionais modernos com coluna JSON indexável (ver [[wiki/concepts/postgresql]]) já cobrem boa parte do que levaria alguém a montar uma infraestrutura poliglota. Ver [[wiki/sources/orm-sql-organizacao-regras-negocio-bancos-dados]].

## Guia Direto por Cenário (Instância Única)

[[wiki/sources/como-escolher-banco-de-dados-historia-acid-cap]] propõe um guia objetivo, cobrindo também bancos não citados nas seções acima:

| Cenário | Banco | Por quê |
|---|---|---|
| App mobile/desktop, usuário único | [[wiki/concepts/sqlite]] | Zero overhead, zero instalação, embarcado |
| Blog, loja simples, CRUD padrão | [[wiki/concepts/mysql]] | Rápido de desenvolver, atende ~80% da web |
| Financeiro, relatórios complexos, geoespacial, busca vetorial | [[wiki/concepts/postgresql]] | ACID sólido + extensões (PostGIS, pgvector) cobrem o que levaria a um banco especializado |
| Missão crítica, budget real, SLA contratual 24/7 | [[wiki/concepts/oracle-database]] | Suporte e robustez a preço de licenciamento por núcleo |
| Stack Microsoft (.NET, Excel, Power BI) | [[wiki/concepts/sql-server]] | Integração nativa reduz fricção operacional |
| Cache de sessão, rate limit, contador, fila leve | [[wiki/concepts/redis]] | Sub-milissegundo é o padrão, não a exceção |
| Catálogo com schema variável, log, IoT | [[wiki/concepts/mongodb]] | Flexibilidade de documento sem custo de schema fixo |

A mesma fonte reforça que todo número de conexão/volume/latência citado assume instância única, sem réplicas, shards ou clusters — é o piso de capacidade, não o teto.

## Key Sources

- [[sources/banco-de-dados]]
- [[wiki/sources/sql-nao-e-banco-de-dados-uncle-bob]]
- [[wiki/sources/acid-vs-base-garantias-bancos-de-dados]] — quadro de decisão ACID vs. BASE por domínio de negócio
- [[wiki/sources/orm-sql-organizacao-regras-negocio-bancos-dados]]
- [[wiki/sources/como-escolher-banco-de-dados-historia-acid-cap]] — guia direto por cenário cobrindo também Oracle, SQL Server e SQLite
