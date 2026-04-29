# O Problema de Usar UUID como Primary Key no MySQL

date: 2026-04-23
tags: [tech-mentor, system-design, banco-de-dados, uuid, primary-key, mysql, performance]
skill: tech-mentor-data/references/database-internals.md
level: intermediário
source_url: https://planetscale.com/blog/the-problem-with-using-a-uuid-primary-key-in-mysql
author: Brian Morrison II (PlanetScale)
date_published: 2024-03-19

---

## Contexto

UUIDs foram criados para gerar IDs únicos sem coordenação entre sistemas — especialmente úteis em arquiteturas distribuídas onde múltiplos serviços criam registros. Parece uma boa ideia usar UUID como primary key, mas quando usados sem cuidado, degradam severamente a performance do banco.

---

## As Versões de UUID

### UUIDv1
Baseado no timestamp gregoriano + endereço MAC do nó. O problema: a porção menos significativa do timestamp vem primeiro, tornando o valor não-ordenável de forma útil. Rastreável até o hardware de origem.

### UUIDv4
Totalmente aleatório, exceto pela posição que identifica a versão (sempre `4` no início do terceiro segmento). É o mais comum — mas o mais problemático para MySQL por ser não-sequencial.

### UUIDv6
Quase idêntico ao v1, mas com os bits de timestamp invertidos: a porção mais significativa vem primeiro. Resultado: valores mais ordenáveis e compatíveis com v1.

### UUIDv7
Baseado em Unix Epoch timestamp (em vez do calendário gregoriano do v1). O nó é substituído por randomness — menos rastreável. **É o substituto recomendado ao v4** quando se precisa de UUIDs com ordenação temporal.

### UUIDv8
Totalmente customizável — estrutura definida pelo implementador. Para casos muito específicos.

---

## UUIDs e MySQL — Os Dois Problemas

### Problema 1 — Insert Performance (Page Splitting)

Indexes no MySQL são B+ Trees. Com chaves sequenciais (auto-increment), inserções vão sempre para a direita da árvore — MySQL preenche cada página a ~94% antes de criar uma nova.

Com UUIDv4 (aleatório), cada insert vai para uma posição aleatória na árvore:
- MySQL precisa encontrar a página correta, possivelmente trazendo-a do disco
- A página pode estar cheia → **page split**: MySQL divide a página e rebalanceia a árvore
- Páginas podem ficar com apenas ~50% de utilização
- Resultado: mais I/O, mais operações de disco, performance de insert até 10x pior em tabelas grandes

### Problema 2 — Storage

| Tipo | Armazenamento por valor |
|---|---|
| INT 32-bit (auto-increment) | 32 bits |
| UUID como `BINARY(16)` | 128 bits (4x) |
| UUID como `CHAR(36)` | 288 bits (9x) |

Secondary indexes também são afetados — eles armazenam o primary key como ponteiro, então crescem proporcionalmente ao tamanho do PK.

Page splitting piora ainda mais: com páginas 50% vazias, o banco ocupa o dobro do espaço necessário.

---

## Soluções

### 1. Armazenar como `BINARY(16)` (em vez de `CHAR(36)`)

```sql
CREATE TABLE users (
  id BINARY(16) NOT NULL,
  PRIMARY KEY (id)
);

INSERT INTO users SET
  id = UUID_TO_BIN('d211ca18-d389-11ee-a506-0242ac120002');

SELECT BIN_TO_UUID(id) FROM users;
```

Reduz de 288 bits para 128 bits — ainda 4x o int, mas muito melhor que string.

### 2. Usar UUID Ordenado (v6 ou v7)

UUIDv6/v7 colocam a porção mais significativa do timestamp primeiro → inserts se comportam de forma mais sequencial → menos page splitting.

```
UUIDv4 (aleatório):  550e8400-e29b-41d4-a716-446655440000
UUIDv7 (ordenado):   018e3a2f-3b7c-7f3e-95d3-e7b4b3e2e1f0
                     ^^^^^^^^^^^^ timestamp Unix Epoch primeiro
```

### 3. `UUID_TO_BIN` com swap flag (MySQL built-in)

MySQL só gera UUIDv1 nativo, mas a função `UUID_TO_BIN(uuid, 1)` reordena os bits do timestamp para torná-lo sequencial:

```sql
SET @uuid = UUID(); -- gera UUIDv1

-- Sem swap (não-ordenado):
SELECT HEX(UUID_TO_BIN(@uuid))   AS sem_swap;
-- D211CA18D38911EEA5060242AC120002

-- Com swap (ordenado):
SELECT HEX(UUID_TO_BIN(@uuid, 1)) AS com_swap;
-- 11EED389D211CA18A5060242AC120002
-- ^^^^^^^^ timestamp mais significativo na frente
```

### 4. Usar Tipo Alternativo de ID

UUIDs não são os únicos identificadores únicos distribuídos:

| Tipo | Exemplo | Ordenável | Tamanho |
|---|---|---|---|
| Snowflake ID | `7167350074945572864` | ✅ | 64 bits |
| ULID | `01HQF2QXSW5EFKRC2YYCEXZK0N` | ✅ | 128 bits |
| NanoID | `kw2c0khavhql` | ❌ | ~72 bits |
| UUIDv7 | `018e3a2f-...` | ✅ | 128 bits |

PlanetScale usa NanoID internamente para suas APIs.

---

## Trade-offs

| Abordagem | Performance | Storage | Distribuído | Complexidade |
|---|---|---|---|---|
| Auto-increment INT | ✅ Ótima | ✅ 32 bits | ❌ Coordenação necessária | Baixa |
| UUIDv4 `CHAR(36)` | ❌ Page splitting | ❌ 288 bits | ✅ | Baixa |
| UUIDv4 `BINARY(16)` | ❌ Page splitting | 🟡 128 bits | ✅ | Média |
| UUIDv7 `BINARY(16)` | ✅ Sequencial | 🟡 128 bits | ✅ | Média |
| Snowflake ID | ✅ Sequencial | ✅ 64 bits | ✅ | Alta (infra) |

---

## Quando Usar / Quando Evitar

**Use UUID (v6 ou v7) quando:**
- ✅ Múltiplos sistemas gerando IDs sem coordenação central
- ✅ IDs precisam ser opacos (não vazar sequência de criação)
- ✅ Migração de dados entre sistemas com merge de tabelas

**Evite UUIDv4 como primary key quando:**
- ❌ Tabela tende a crescer além de milhões de registros
- ❌ Performance de insert é crítica
- ❌ Storage é uma preocupação

**Prefira auto-increment quando:**
- ✅ Sistema centralizado (sem distribuição de geração de ID)
- ✅ Máxima performance de insert e menor storage

---

## Conceitos Relacionados

[[banco-de-dados]] · [[db-sharding]] · [[snowflake-id]] · [[consistent-hashing]] · [[read-replicas-connection-pooling]]
