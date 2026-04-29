---
date: 2026-04-07
tags: [tech-mentor, ia, rag, retrieval, embeddings, vector-store, chunking, hybrid-search, reranking, hyde, graphrag]
skill: tech-mentor-ai/references/ai/rag-advanced.md
level: intermediário
---

# RAG & Retrieval

## Contexto

RAG (Retrieval-Augmented Generation) é o padrão dominante para dar conhecimento atualizado a um LLM sem re-treinar. Em vez de "ensinar" o modelo novos fatos (fine-tuning), você busca os fatos relevantes em runtime e os injeta no prompt. Isso resolve o problema de knowledge cutoff e permite bases de conhecimento que mudam frequentemente.

---

## Como Funciona

### Pipeline básico

```
[Documento] → [Chunking] → [Embedding] → [Vector Store]
                                               ↓
[Query] → [Embed Query] → [Busca Similar] → [Top-K Chunks]
                                               ↓
                            [Prompt = Query + Chunks] → [LLM] → [Resposta]
```

---

### Chunking — o fundamento do recall

A qualidade do chunking é o fator mais determinante no recall do RAG. Chunk ruim = busca ruim, independente do modelo.

**Fixed-size com overlap** (ponto de partida):
```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=512,
    chunk_overlap=50,           # overlap garante que frases na fronteira não se perdem
    separators=["\n\n", "\n", ". ", " ", ""],  # respeita estrutura natural
)
chunks = splitter.split_text(document)
```

**Semântico por estrutura do documento** (preferível para markdown/docs):
```python
from langchain.text_splitter import MarkdownHeaderTextSplitter

md_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=[
    ("#", "h1"), ("##", "h2"), ("###", "h3"),
])
docs = md_splitter.split_text(markdown_content)
```

**Regras de thumb para tamanho:**

| Caso | Chunk size | Overlap |
|---|---|---|
| Prosa genérica | 512 tokens | 50 tokens |
| Documentação técnica | 800–1000 tokens | 100–150 tokens |
| Q&A / FAQs | 256 tokens | 25 tokens |
| Código | 1 função completa | 0 (nunca cortar no meio) |

**Parent-Child chunking** — chunks pequenos para busca precisa, chunks grandes para contexto:
```python
# Indexa child (256 tokens) para busca
# Ao recuperar, retorna o parent (1024 tokens) com mais contexto
def parent_child_split(doc: str, child_size=256, parent_size=1024):
    parents = split_by_tokens(doc, parent_size)
    children = []
    for parent_id, parent in enumerate(parents):
        for child in split_by_tokens(parent, child_size):
            children.append({"text": child, "parent_id": parent_id})
    return parents, children
```

---

### Embeddings — representação vetorial do texto

```
"Como cancelar meu pedido"
       ↓ modelo de embedding
[0.23, -0.41, 0.88, ..., 0.12]  → 1536 dimensões

"Quero desistir da compra"
[0.21, -0.38, 0.91, ..., 0.14]  → distância coseno ~0.98 (muito similar)
```

**Modelos de embedding — escolha por caso de uso:**

| Modelo | Dimensões | Custo | Quando usar |
|---|---|---|---|
| text-embedding-3-small (OpenAI) | 1536 | $0.02/1M tokens | Default, bom custo-benefício |
| text-embedding-3-large (OpenAI) | 3072 | $0.13/1M tokens | Máxima qualidade |
| voyage-3 (Voyage AI) | 1024 | $0.06/1M tokens | Melhor para código e técnico |
| BGE-M3 (OSS) | 1024 | Self-hosted grátis | Português, multilingual |
| nomic-embed (OSS) | 768 | Self-hosted grátis | Leve, privacidade |

**Geração eficiente em produção:**
```typescript
import OpenAI from "openai";

const openai = new OpenAI();
const embeddingCache = new Map<string, number[]>();

async function embed(text: string): Promise<number[]> {
  const cacheKey = hashText(text);
  if (embeddingCache.has(cacheKey)) return embeddingCache.get(cacheKey)!;

  const response = await openai.embeddings.create({
    model: "text-embedding-3-small",
    input: text.slice(0, 8191),
  });

  const embedding = response.data[0].embedding;
  embeddingCache.set(cacheKey, embedding);
  return embedding;
}

// Batch embedding — muito mais eficiente que chamadas individuais
async function embedBatch(texts: string[]): Promise<number[][]> {
  const response = await openai.embeddings.create({
    model: "text-embedding-3-small",
    input: texts,  // até 2048 inputs por request
  });
  return response.data.map(d => d.embedding);
}
```

---

### Vector Stores e índice HNSW

HNSW (Hierarchical Navigable Small World) é o algoritmo de busca aproximada (ANN) padrão. Troca exatidão por velocidade — recall de ~95% com latência de ms vs 100% de recall em segundos.

**pgvector — quando já usa PostgreSQL:**
```sql
CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE documents (
  id         UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  content    TEXT NOT NULL,
  embedding  VECTOR(1536),
  tenant_id  UUID NOT NULL,
  category   TEXT,
  created_at TIMESTAMPTZ DEFAULT now()
);

-- HNSW: melhor para alta concorrência de queries
CREATE INDEX ON documents USING hnsw (embedding vector_cosine_ops)
  WITH (m = 16, ef_construction = 64);

-- Busca com filtro multi-tenant
SELECT content, 1 - (embedding <=> $1::vector) AS similarity
FROM documents
WHERE tenant_id = $2
ORDER BY embedding <=> $1::vector
LIMIT 10;
```

**Quando migrar do pgvector para Qdrant:**
- Volume > 5M vetores com latência P99 crítica
- Filtros complexos combinando múltiplos campos em vetores puros
- Necessidade de payload filtering sem SQL overhead

---

## Técnicas Avançadas

### Hybrid Search — Vetorial + BM25

Combina busca semântica (embedding) com busca por keyword (BM25). Melhora recall para termos técnicos, siglas e nomes próprios que embeddings não capturam bem.

```typescript
async function hybridSearch(query: string, topK = 10) {
  const [vectorResults, keywordResults] = await Promise.all([
    vectorSearch(query, topK * 2),
    bm25Search(query, topK * 2),
  ]);

  return reciprocalRankFusion([vectorResults, keywordResults], topK);
}

// RRF — combina rankings sem precisar normalizar scores entre sistemas diferentes
function reciprocalRankFusion(rankedLists: SearchResult[][], topK: number, k = 60) {
  const scores = new Map<string, number>();
  const docs = new Map<string, SearchResult>();

  for (const list of rankedLists) {
    list.forEach((doc, rank) => {
      const prev = scores.get(doc.id) ?? 0;
      scores.set(doc.id, prev + 1 / (k + rank + 1));
      docs.set(doc.id, doc);
    });
  }

  return [...scores.entries()]
    .sort((a, b) => b[1] - a[1])
    .slice(0, topK)
    .map(([id]) => docs.get(id)!);
}
```

**Use hybrid search quando:** base de conhecimento tem termos técnicos, siglas, nomes de produtos, códigos de erro. BM25 captura exatidão léxica que embedding perde.

---

### Re-ranking — precisão pós-busca

A busca vetorial retorna candidatos por similaridade de embedding, não por relevância real. Re-rankers são cross-encoders que lêem query + documento juntos para um score mais preciso.

```typescript
import { CohereClient } from "cohere-ai";

const cohere = new CohereClient({ token: process.env.COHERE_API_KEY });

async function ragWithRerank(query: string): Promise<string> {
  // 1. Busca ampla — top-20 para dar candidatos suficientes ao re-ranker
  const candidates = await hybridSearch(query, 20);

  // 2. Re-ranking preciso — reduz para top-5
  const reranked = await cohere.rerank({
    model: "rerank-english-v3.0",
    query,
    documents: candidates.map(c => c.content),
    topN: 5,
  });

  // 3. Filtrar por threshold de relevância
  const relevant = reranked.results.filter(r => r.relevanceScore > 0.4);

  if (relevant.length === 0) {
    return await llm.complete(buildNoContextPrompt(query));
  }

  const context = relevant.map(r => candidates[r.index].content);
  return await llm.complete(buildRAGPrompt(query, context));
}
```

**Alternativas de re-ranker:**
- `cross-encoder/ms-marco-MiniLM-L-6-v2` — open source, self-hosted
- `bge-reranker-v2-m3` — multilingual, ótimo para português
- LLM-as-reranker — GPT-4o-mini (mais caro, mais flexível)

---

### HyDE — Hypothetical Document Embeddings

Em vez de buscar pela query, gera um documento hipotético que a responderia e usa o embedding desse documento. Funciona porque documentos similares têm embeddings próximos — melhor que query curta.

```typescript
async function hydeSearch(query: string, topK = 5): Promise<string[]> {
  // 1. Gera documento hipotético que responderia a query
  const hypotheticalDoc = await llm.complete({
    prompt: `Write a detailed paragraph that directly answers this question.
Do not say "I don't know" — generate the most plausible answer.
Question: ${query}
Answer:`,
    temperature: 0,
    maxTokens: 300,
  });

  // 2. Usa o embedding do doc hipotético para buscar (não da query original)
  const embedding = await embed(hypotheticalDoc);
  const results = await vectorStore.search(embedding, topK);

  return results.map(r => r.content);
}
```

**Quando HyDE ajuda:** queries curtas ou ambíguas, linguagem de usuário diferente da documentação técnica.

**Quando NÃO usar:** queries factuais simples com vocabulário correto, base onde HyDE pode alucinar termos que o vector store não tem.

---

### Contextual Retrieval (Anthropic)

Antes de indexar cada chunk, gera um contexto explicando onde ele se encaixa no documento. Melhora recall em ~49% segundo experimentos da Anthropic.

```typescript
async function contextualizeChunk(chunk: string, fullDocument: string): Promise<string> {
  const context = await anthropic.messages.create({
    model: "claude-haiku-4-5-20251001",  // Haiku para economizar custo
    max_tokens: 100,
    messages: [{
      role: "user",
      content: `<document>
${fullDocument}
</document>

Here is the chunk we want to situate within the whole document:
<chunk>
${chunk}
</chunk>

Please give a short succinct context to situate this chunk within the overall document.
Answer only with the context, no preamble.`,
    }],
  });

  const contextText = context.content[0].type === "text" ? context.content[0].text : "";
  return `${contextText}\n\n${chunk}`;  // contexto prefixado ao chunk
}
```

**Custo:** Haiku + prompt caching → ~$0.50 para 1000 chunks de 500 tokens (vs ~$4.00 sem caching).

---

### GraphRAG & Knowledge Graphs

RAG vetorial trata documentos como blocos independentes — perde relações entre entidades. GraphRAG extrai entidades e relações e constrói um grafo de conhecimento.

```
RAG vetorial:  Doc A | Doc B | Doc C  (blocos independentes)
GraphRAG:      Entidade1 → relaciona → Entidade2 → relaciona → Entidade3
```

**Quando vale o custo (indexação com LLM é cara):**
- Multi-hop reasoning: "Quais empresas que forneceram para X também trabalham com Y?"
- Síntese de múltiplos documentos: "Qual é a posição geral sobre Z?"
- Bases com entidades ricamente interconectadas (pessoas, empresas, contratos)

**Quando usar RAG vetorial:** queries factuais pontuais, documentos independentes, orçamento limitado.

---

### Agentic RAG — Self-RAG e Query Rewriting

Em vez de buscar uma vez e gerar, o agente decide dinamicamente quando buscar, o quê buscar e se o resultado é suficiente.

```
[Query] → [Agente decide: precisa buscar?]
              ↓ sim
         [Reformula query para busca]
              ↓
         [Busca no vector store]
              ↓
         [Avalia: contexto suficiente?]
              ↓ não
         [Busca adicional com query refinada]
              ↓ sim
         [Gera resposta]
              ↓
         [Avalia: resposta fundamentada nos chunks?]
              ↓ não → corrige ou sinaliza baixa confiança
```

---

## Problemas Comuns e Soluções

| Problema | Causa | Solução |
|---|---|---|
| Resposta irrelevante | Chunks muito grandes | Reduzir chunk size |
| Não encontra a informação | Chunking quebra contexto | Aumentar overlap, chunking semântico |
| Alucinação | LLM ignora o contexto | Prompt mais restritivo, temperatura 0 |
| Latência alta | Embedding + busca sequencial | Cache de embeddings, busca paralela |
| Resposta desatualizada | Vector store com dados velhos | Pipeline de re-indexação incremental |
| Termos técnicos não encontrados | Embedding não captura léxico exato | Hybrid search (BM25 + vetorial) |
| Top-K traz ruído | Busca vetorial sem threshold | Re-ranking com threshold de relevância |

---

## Vector Stores — Quando Usar Cada Um

| Store | Quando usar |
|---|---|
| pgvector | Já usa PostgreSQL, volume < 5M vetores, filtros SQL complexos |
| Pinecone | SaaS gerenciado, sem ops, escala automática |
| Qdrant | OSS, alta performance, filtros + vetores, Rust |
| Weaviate | Open source, multimodal, self-hosted |
| Milvus | Volume massivo (>10M vetores), equipe com infra madura |
| Redis Vector | Cache + busca, latência ultra-baixa, real-time |

---

## Avaliação com RAGAS

```python
from ragas import evaluate
from ragas.metrics import faithfulness, answer_relevancy, context_precision, context_recall

dataset = Dataset.from_list([{
    "question": "Qual o prazo de devolução?",
    "answer": llm_answer,
    "contexts": retrieved_chunks,
    "ground_truth": "O cliente tem até 7 dias corridos para solicitar devolução.",
}])

results = evaluate(dataset, metrics=[faithfulness, answer_relevancy, context_precision, context_recall])
```

**O que cada métrica sinaliza:**

| Métrica | < threshold | Causa provável | Solução |
|---|---|---|---|
| `faithfulness` < 0.8 | LLM alucina além do contexto | Prompt mais restritivo, temperatura 0 |
| `context_precision` < 0.7 | Retrieval trazendo ruído | Re-ranking, threshold de relevância |
| `context_recall` < 0.7 | Chunks relevantes perdidos | Hybrid search, HyDE, query expansion |
| `answer_relevancy` < 0.8 | Resposta desviou do ponto | CoT no prompt, foco explícito |

---

## Arquitetura Production-Ready

```
[Query] → [Preprocessor: guardrails + PII removal]
              ↓
         [Query Expansion / HyDE]
              ↓
    [Hybrid Search: Vector + BM25]          paralelo
              ↓
         [Re-ranking (cross-encoder)]
              ↓
         [Context Assembly]
         [contextual chunks + metadata]
              ↓
         [LLM Generation]  temperature: 0
              ↓
         [Output Validation: faithfulness check]
              ↓
         [Response + Citations]

Paralelamente:
  [Eval Pipeline] ← logs prod → RAGAS → alertas de degradação
  [Re-indexer]    ← novos docs → contextualização → vector store
```

**Prioridade de implementação por orçamento:**
1. Hybrid search (maior ganho por menor custo)
2. Re-ranking
3. Contextual retrieval
4. HyDE + query expansion
5. GraphRAG (custo/complexidade altos — apenas se multi-hop for requisito)

---

## Quando Usar / Quando Evitar

**RAG básico resolve:** base pequena (<1k docs), queries simples, latência não crítica.

**Técnicas avançadas valem quando:** RAG básico tem recall < 70% no seu eval set, base com vocabulário técnico específico, perguntas que cruzam múltiplos documentos.

**RAG não resolve:** comportamento/estilo consistente (→ fine-tuning), conhecimento embutido no modelo (→ prompt engineering), decisões que exigem raciocínio complexo fora da base (→ agentes).

---

## Conceitos Relacionados

[[como-llms-funcionam]] · [[prompt-engineering]] · [[context-engineering]] · [[agentes-core]] · [[structured-outputs-function-calling]]

---
*Fonte: tech-mentor skill · tech-mentor-ai · 2026-04-07*
