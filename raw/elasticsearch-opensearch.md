---
date: 2026-04-17
tags: [tech-mentor, banco, search, elasticsearch, opensearch, full-text]
skill: tech-mentor-backend/references/databases
level: intermediário
---

# Elasticsearch / OpenSearch

## Contexto
Elasticsearch (e seu fork OpenSearch, mantido pela AWS após a mudança de licença) é um mecanismo de busca distribuído baseado no Apache Lucene. Resolve o que o PostgreSQL full-text search não resolve bem em escala: busca de relevância, faceted search, autocomplete e análise em quase-realtime sobre volumes massivos.

**Quando usar sobre PostgreSQL FTS:** > 10M documentos, relevância customizada, facets/aggregations complexas, autocomplete sofisticado, geo-search em larga escala.

## Conceitos Fundamentais

```
Elasticsearch          PostgreSQL equivalente
Index          ←→      Tabela
Document       ←→      Linha
Field          ←→      Coluna
Shard          ←→      Partição (sem equivalente direto)
Mapping        ←→      Schema
```

**Inverted Index:** a estrutura central. Para cada termo, mantém a lista de documentos que o contêm e onde. Isso torna busca por texto O(1) vs. O(N) de LIKE.

```
"entrega rápida" → doc:1, doc:3, doc:7
"entrega"        → doc:1, doc:2, doc:3, doc:5, doc:7
"rápida"         → doc:1, doc:3, doc:7, doc:9
```

## Mapping — Schema de Índice

```json
PUT /products
{
  "mappings": {
    "properties": {
      "id":          { "type": "keyword" },
      "name":        { "type": "text", "analyzer": "portuguese" },
      "description": { "type": "text", "analyzer": "portuguese" },
      "category":    { "type": "keyword" },
      "price":       { "type": "float" },
      "rating":      { "type": "float" },
      "tags":        { "type": "keyword" },
      "location":    { "type": "geo_point" },
      "createdAt":   { "type": "date" },
      "name_suggest": {
        "type": "completion"
      }
    }
  }
}
```

## BM25 — Algoritmo de Relevância

BM25 (Best Match 25) é o algoritmo padrão do Elasticsearch para scoring. Considera:
- **TF (Term Frequency):** quantas vezes o termo aparece no documento
- **IDF (Inverse Document Frequency):** quão raro é o termo no índice — termos raros têm mais peso
- **Field Length:** documentos mais curtos são preferidos (normalização de tamanho)

## Queries Práticas

```typescript
import { Client } from "@elastic/elasticsearch";

const es = new Client({ node: process.env.ES_URL });

// Full-text search com relevância
const result = await es.search({
  index: "products",
  body: {
    query: {
      multi_match: {
        query: "notebook gamer",
        fields: ["name^3", "description"],  // name tem peso 3x
        fuzziness: "AUTO"                    // tolera typos
      }
    },
    highlight: {
      fields: { name: {}, description: {} } // destaca os termos encontrados
    }
  }
});

// Faceted search — filtros + contagens por categoria
const facetResult = await es.search({
  index: "products",
  body: {
    query: { match: { name: "notebook" } },
    aggs: {
      by_category: {
        terms: { field: "category", size: 10 }
      },
      price_range: {
        range: {
          field: "price",
          ranges: [
            { to: 1000 },
            { from: 1000, to: 3000 },
            { from: 3000 }
          ]
        }
      },
      avg_rating: { avg: { field: "rating" } }
    },
    post_filter: {
      term: { category: "notebooks" }  // filtro após aggregations
    }
  }
});

// Autocomplete com completion suggester
const suggest = await es.search({
  index: "products",
  body: {
    suggest: {
      product_suggest: {
        prefix: "note",
        completion: { field: "name_suggest", size: 5 }
      }
    }
  }
});
```

## Sincronização com PostgreSQL

Elasticsearch não é fonte da verdade — é um índice de busca. O dado canônico fica no PostgreSQL.

```typescript
// Estratégia 1: Dual-write no application layer
async function createProduct(data: CreateProductDTO) {
  const product = await prisma.product.create({ data });
  
  // Fire-and-forget — inconsistência eventual aceitável
  await es.index({
    index: "products",
    id: product.id,
    document: toSearchDocument(product)
  }).catch(err => {
    console.log({ message: "ES sync failed, will retry", productId: product.id, error: err });
    // Enfileirar para retry
  });

  return product;
}

// Estratégia 2 (preferível): CDC com Debezium → Kafka → ES sink connector
// PostgreSQL WAL → Debezium → Kafka → ES connector indexa automaticamente
```

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---|---|---|
| Relevância | BM25 nativo, customizável | Consistência eventual com o DB primário |
| Performance | Sub-segundo em bilhões de docs | Operacional complexo — shards, replicas, tuning |
| Funcionalidades | Facets, geo, autocomplete, highlight | Sem ACID — não substitui banco relacional |
| Custo | Open source | Alto consumo de RAM e disco |

## Conceitos Relacionados
[[postgresql-avancado]] · [[cdc-debezium]] · [[kafka]] · [[multi-tenancy]] · [[cache-strategies]]

---
*Fonte: tech-mentor skill · tech-mentor-backend · 2026-04-17*
