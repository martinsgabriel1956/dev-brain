---
date: 2026-04-16
tags: [tech-mentor, backend, apis, pagination, keyset, cursor, offset]
skill: tech-mentor-backend/references/apis
level: intermediário
---

# Paginação — Keyset, Cursor e Offset

## Contexto

Paginação é uma das APIs que mais parece simples e mais esconde problemas. Offset/LIMIT é a implementação padrão, mas falha em performance (PostgreSQL precisa contar `offset` rows antes de retornar) e em consistência (rows inseridas/deletadas durante a paginação causam páginas duplicadas ou skipped). Keyset (a.k.a. seek method) resolve ambos os problemas — ao custo de não poder pular para páginas arbitrárias.

---

## Offset Pagination — O Padrão com Problemas

```typescript
// Endpoint: GET /posts?page=3&limit=20

async function listPostsOffset(page: number, limit: number) {
  const offset = (page - 1) * limit;

  const [posts, total] = await Promise.all([
    prisma.post.findMany({
      skip: offset,
      take: limit,
      orderBy: { createdAt: "desc" }
    }),
    prisma.post.count()
  ]);

  return {
    data: posts,
    meta: {
      page,
      limit,
      total,
      totalPages: Math.ceil(total / limit),
      hasNext: page * limit < total,
      hasPrev: page > 1
    }
  };
}
```

**Problemas:**

```sql
-- PostgreSQL executa: varrer 1000 rows para retornar 20
SELECT * FROM posts ORDER BY created_at DESC LIMIT 20 OFFSET 1000;
-- OFFSET alto = table scan parcial — O(offset + limit)
-- Sem índice adequado: sequencial scan

-- Inconsistência: novo post inserido enquanto usuário pagina
-- Página 1: posts 1-20 (post A é o 20)
-- [novo post B inserido antes de A]
-- Página 2: posts 21-40 → post A aparece novamente na página 2
```

**Quando usar offset mesmo assim:** interfaces admin com paginação por número de página, conjuntos pequenos (<10k rows), relatórios onde consistência temporal não importa.

---

## Keyset Pagination (Seek Method) — O Padrão Correto

Em vez de pular rows, filtra pela última row vista. Performance O(log n) com índice no cursor field.

```typescript
// Endpoint: GET /posts?limit=20&after=2024-01-15T10:30:00Z_uuid-do-ultimo-post

type KeysetCursor = {
  createdAt: Date;
  id: string;  // desempate quando createdAt é igual
};

function encodeCursor(cursor: KeysetCursor): string {
  return Buffer.from(JSON.stringify(cursor)).toString("base64url");
}

function decodeCursor(encoded: string): KeysetCursor {
  return JSON.parse(Buffer.from(encoded, "base64url").toString());
}

async function listPostsKeyset(limit: number, afterCursor?: string) {
  const cursor = afterCursor ? decodeCursor(afterCursor) : null;

  const posts = await prisma.post.findMany({
    take: limit + 1,  // buscar N+1 para detectar se há próxima página
    where: cursor
      ? {
          OR: [
            // Posts com createdAt anterior ao cursor
            { createdAt: { lt: cursor.createdAt } },
            // Posts com mesmo createdAt mas id posterior (desempate estável)
            {
              createdAt: { equals: cursor.createdAt },
              id: { gt: cursor.id }
            }
          ]
        }
      : undefined,
    orderBy: [
      { createdAt: "desc" },
      { id: "asc" }  // ordem secundária para desempate determinístico
    ]
  });

  const hasNextPage = posts.length > limit;
  const items = hasNextPage ? posts.slice(0, -1) : posts;

  const nextCursor = hasNextPage
    ? encodeCursor({ createdAt: items[items.length - 1].createdAt, id: items[items.length - 1].id })
    : null;

  return {
    data: items,
    meta: {
      limit,
      hasNextPage,
      nextCursor,
      hasPrevPage: !!afterCursor  // simplificado — ver paginação bidirecional abaixo
    }
  };
}
```

### SQL equivalente

```sql
-- Índice composto necessário para performance
CREATE INDEX idx_posts_keyset ON posts (created_at DESC, id ASC)
  WHERE deleted_at IS NULL;

-- Query keyset — usa o índice, sem table scan parcial
SELECT * FROM posts
WHERE (created_at, id) < ('2024-01-15 10:30:00', 'uuid-do-ultimo-post')
  AND deleted_at IS NULL
ORDER BY created_at DESC, id ASC
LIMIT 21;
-- O banco para assim que encontra 21 rows — O(log n + result set)
```

---

## Cursor Opaco — Abstração do Mecanismo Interno

```typescript
// O cursor pode esconder qualquer mecanismo interno
// O consumer só vê: "me dê a próxima página usando este token opaco"

type CursorPayload = {
  strategy: "keyset" | "offset";
  data: unknown;
  createdAt: number;  // quando o cursor foi criado (para expiração)
};

function createCursor(payload: CursorPayload): string {
  return Buffer.from(JSON.stringify(payload)).toString("base64url");
}

function parseCursor(token: string): CursorPayload {
  try {
    const payload = JSON.parse(Buffer.from(token, "base64url").toString()) as CursorPayload;

    // Cursor expirado após 24h (evita queries com dados muito antigos)
    const isExpired = Date.now() - payload.createdAt > 86400 * 1000;
    if (isExpired) throw new Error("Cursor expired");

    return payload;
  } catch {
    throw new Error("Invalid or expired cursor");
  }
}

// Response padronizada que não expõe o mecanismo interno
type PaginatedResponse<T> = {
  data: T[];
  pagination: {
    nextCursor: string | null;
    prevCursor: string | null;
    hasNextPage: boolean;
    hasPrevPage: boolean;
  };
};
```

---

## Paginação Bidirecional

Para navegar para frente e para trás (essencial em apps mobile onde usuário faz pull-to-refresh):

```typescript
type BiDirectionalCursor = {
  id: string;
  createdAt: Date;
  direction: "forward" | "backward";
};

async function listPostsBidirectional(
  limit: number,
  cursor?: string
): Promise<PaginatedResponse<Post>> {
  const parsed = cursor ? decodeCursor(cursor) as BiDirectionalCursor : null;

  let where: Prisma.PostWhereInput = {};
  let orderBy: Prisma.PostOrderByWithRelationInput[] = [
    { createdAt: "desc" },
    { id: "asc" }
  ];

  if (parsed) {
    if (parsed.direction === "forward") {
      // Próxima página — posts mais antigos que o cursor
      where = {
        OR: [
          { createdAt: { lt: parsed.createdAt } },
          { createdAt: { equals: parsed.createdAt }, id: { gt: parsed.id } }
        ]
      };
    } else {
      // Página anterior — posts mais recentes que o cursor
      where = {
        OR: [
          { createdAt: { gt: parsed.createdAt } },
          { createdAt: { equals: parsed.createdAt }, id: { lt: parsed.id } }
        ]
      };
      // Inverter ordem para pegar os mais próximos do cursor
      orderBy = [{ createdAt: "asc" }, { id: "desc" }];
    }
  }

  const posts = await prisma.post.findMany({
    take: limit + 1,
    where,
    orderBy
  });

  // Re-ordenar se veio de backward (para manter ordem consistente na UI)
  if (parsed?.direction === "backward") posts.reverse();

  const hasNextPage = parsed?.direction === "forward"
    ? posts.length > limit
    : !!cursor;

  const hasPrevPage = parsed?.direction === "backward"
    ? posts.length > limit
    : !!cursor;

  const items = posts.length > limit ? posts.slice(0, -1) : posts;

  const last = items[items.length - 1];
  const first = items[0];

  return {
    data: items,
    pagination: {
      hasNextPage,
      hasPrevPage,
      nextCursor: hasNextPage && last
        ? encodeCursor({ id: last.id, createdAt: last.createdAt, direction: "forward" })
        : null,
      prevCursor: hasPrevPage && first
        ? encodeCursor({ id: first.id, createdAt: first.createdAt, direction: "backward" })
        : null
    }
  };
}
```

---

## Trade-offs

| Aspecto | Offset/LIMIT | Keyset (Cursor) |
|---|---|---|
| **Performance** | O(offset + limit) — degrada com offset alto | O(log n + result) — constante |
| **Pular para página X** | Sim (page * limit) | Não — somente sequencial |
| **Consistência** | Rows movem entre páginas durante paginação | Estável — rows inseridas não aparecem na próxima página |
| **Total de registros** | COUNT(*) simples | COUNT(*) possível mas caro — geralmente omitido |
| **Complexidade de impl** | Simples | Média (cursor encoding, desempate) |
| **Filtros arbitrários** | Qualquer WHERE | WHERE deve incluir os campos do cursor no índice |
| **UI com número de páginas** | Natural | Não suportado (sem total) |

## Quando Usar / Quando Evitar

**Offset:** admin panels, exports, relatórios onde usuário pula para página específica e o dataset não muda durante a sessão.

**Keyset:** feeds, timelines, listas em apps mobile, qualquer dataset em crescimento ativo, coleções grandes (>50k rows) onde performance de OFFSET degradaria.

**Keyset com total aproximado:** para não perder o "X de Y resultados", manter um contador separado (Redis counter ou materialized count) atualizado via trigger/CDC.

**Evitar:** paginação em queries que não têm índice composto nos campos do cursor — o keyset degrada para seq scan sem o índice correto.

## Conceitos Relacionados

[[rest-openapi]] · [[postgresql-avancado]] · [[read-replicas-connection-pooling]] · [[rate-limiting]]

---
*Fonte: tech-mentor skill · tech-mentor-backend · 2026-04-16*
