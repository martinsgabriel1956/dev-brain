---
date: 2026-04-07
tags: [tech-mentor, ia, context-engineering, sliding-window, summarization, prompt-caching, token-budget, lost-in-the-middle, long-context]
skill: tech-mentor-ai/references/ai/context-engineering.md
level: intermediário
---

# Context Engineering

## Contexto

Gerenciar contexto é gerenciar custo, latência e qualidade ao mesmo tempo. A janela de contexto é o recurso mais escasso de um sistema LLM — cada token importa. Context engineering é a disciplina de preencher essa janela com informação de máxima densidade e descartar o que não contribui para a resposta.

---

## Modelo Mental

```
┌─────────────────────────────────────────────────────────────┐
│                    Janela de Contexto                       │
│                                                             │
│  [System Prompt]  [Histórico]  [Docs Relevantes]  [Query]  │
│       ~500tk         ~3000tk        ~2000tk         ~200tk  │
│                                                             │
│  Total: ~5700 de 128k tokens disponíveis                    │
│  ← usar muito = custo/latência; usar pouco = respostas rasas│
└─────────────────────────────────────────────────────────────┘
```

**Regra:** preencha o contexto com informação de alta densidade. Cada token deve contribuir para a qualidade da resposta.

---

## Estratégias de Gerenciamento de Histórico

### Sliding Window — janela deslizante

A estratégia mais simples: descarta mensagens antigas quando o contexto enche.

```python
from collections import deque

class SlidingWindowMemory:
    def __init__(self, max_tokens = 4000):
        self.messages = deque()
        self.max_tokens = max_tokens
        self.current_tokens = 0

    def add(self, message: dict):
        tokens = count_tokens(message["content"])
        self.messages.append((message, tokens))
        self.current_tokens += tokens
        self._evict_old()

    def _evict_old(self):
        while self.current_tokens > self.max_tokens and self.messages:
            _, old_tokens = self.messages.popleft()
            self.current_tokens -= old_tokens

    def get_messages(self) -> list:
        return [msg for msg, _ in self.messages]
```

**Limitação:** perde continuidade. Se o usuário mencionar algo 20 mensagens atrás, o LLM não sabe mais.

---

### Summarization — compressão de histórico antigo

Comprime o histórico antigo em um resumo. Mantém a semântica sem consumir todos os tokens.

```python
async def compress_history(messages: list, llm) -> str:
    old_messages = messages[:-10]  # tudo exceto últimas 10 mensagens

    summary = await llm.ainvoke([
        SystemMessage("Resuma esta conversa preservando: "
                      "decisões tomadas, preferências do usuário, "
                      "contexto técnico estabelecido, próximos passos."),
        HumanMessage(f"Conversa:\n{format_messages(old_messages)}")
    ])
    return summary.content

class SummarizingMemory:
    def __init__(self, llm, summary_threshold=20, keep_recent=8):
        self.messages = []
        self.summary = ""
        self.threshold = summary_threshold
        self.keep_recent = keep_recent
        self.llm = llm

    async def add(self, message):
        self.messages.append(message)
        if len(self.messages) > self.threshold:
            await self._summarize()

    async def _summarize(self):
        to_compress = self.messages[:-self.keep_recent]
        new_summary = await compress_history(to_compress, self.llm)
        if self.summary:
            new_summary = f"Resumo anterior: {self.summary}\n\nAtualização: {new_summary}"
        self.summary = new_summary
        self.messages = self.messages[-self.keep_recent:]

    def get_context(self) -> list:
        messages = []
        if self.summary:
            messages.append(SystemMessage(f"Contexto da conversa: {self.summary}"))
        messages.extend(self.messages)
        return messages
```

**Custo adicional:** +1 chamada ao LLM por compressão. Use um modelo pequeno (haiku, gpt-4o-mini) para summarização.

---

### Vector Memory — memória de longo prazo

Armazena mensagens em um vector store e recupera apenas as relevantes para a query atual.

```python
class VectorMemory:
    def __init__(self):
        self.vectorstore = Chroma(embedding_function=OpenAIEmbeddings())
        self.short_term = []  # últimas N mensagens completas

    def store(self, message: str, metadata: dict):
        self.vectorstore.add_texts(
            texts=[message],
            metadatas=[{**metadata, "timestamp": datetime.utcnow().isoformat()}]
        )

    def retrieve_relevant(self, query: str, k = 3) -> list:
        docs = self.vectorstore.similarity_search(query, k=k)
        return [doc.page_content for doc in docs]

    def build_context(self, current_query: str) -> list:
        relevant = self.retrieve_relevant(current_query)
        context = []
        if relevant:
            context.append(SystemMessage(
                "Memórias relevantes desta conversa:\n" + "\n---\n".join(relevant)
            ))
        context.extend(self.short_term[-8:])
        return context
```

---

### Selective Context — injetar apenas o necessário

Para RAG e qualquer contexto de documentos: filtre por relevância e threshold antes de injetar.

```python
def build_rag_context(query: str, docs: list, max_tokens = 3000) -> str:
    scored_docs = rerank(query, docs)  # re-ranker para relevância

    context_parts = []
    tokens_used = 0

    for doc, score in scored_docs:
        if score < 0.5:  # threshold de relevância mínima
            break

        doc_tokens = count_tokens(doc.content)
        if tokens_used + doc_tokens > max_tokens:
            remaining = max_tokens - tokens_used
            doc_content = truncate_to_tokens(doc.content, remaining)
        else:
            doc_content = doc.content

        context_parts.append(f"[{doc.source}]\n{doc_content}")
        tokens_used += count_tokens(doc_content)

        if tokens_used >= max_tokens:
            break

    return "\n\n".join(context_parts)
```

---

### Map-Reduce para documentos longos

Quando o documento não cabe no contexto, processe em partes e combine:

```python
# Map: processa cada chunk separadamente
chunk_summaries = await asyncio.gather(*[
    llm.complete(f"Extraia informações relevantes sobre '{question}' deste trecho: {chunk}")
    for chunk in chunks
])

# Reduce: combina os summaries
final_answer = await llm.complete(
    f"Com base nos seguintes resumos, responda: {question}\n\nResumos:\n" +
    "\n\n".join(chunk_summaries)
)
```

---

## Token Budget — controle explícito de gasto

Defina um orçamento de tokens por request e respeite-o:

```python
import tiktoken

CONTEXT_LIMITS = {
    "gpt-4o": 128_000,
    "gpt-4o-mini": 128_000,
    "claude-3-5-sonnet": 200_000,
    "gemini-1.5-pro": 1_000_000,
    "llama-3.1-70b": 128_000,
}

def count_tokens(text: str, model = "gpt-4o") -> int:
    enc = tiktoken.encoding_for_model(model)
    return len(enc.encode(text))

def check_context_budget(messages: list, model: str, reserve_output = 4000) -> bool:
    """Verifica se ainda há espaço para a resposta esperada."""
    used = count_messages_tokens(messages, model)
    limit = CONTEXT_LIMITS.get(model, 8000)
    return used + reserve_output <= limit
```

**Alertas recomendados:**
- Utilização > 80% → risco de truncamento em conversas longas
- Custo por usuário > threshold → possível loop ou conversa muito longa

---

## Lost-in-the-Middle

LLMs têm atenção não uniforme sobre o contexto. Informação no meio de prompts longos é frequentemente ignorada.

```
Atenção do modelo:
Início do contexto  ████████████  Alta
Meio do contexto    ████          Baixa ← informação crítica aqui é ignorada
Fim do contexto     ████████████  Alta
```

**Como mitigar:**
- Coloque a informação mais crítica no **início** ou no **fim** do contexto
- Para RAG: coloque os chunks mais relevantes no início da lista de contexto
- Use re-ranking para garantir que o chunk certo está na posição certa
- Repita informação crítica perto da query se necessário

---

## Prompt Caching — economia de 80–90%

Providers cacheiam o prefix do prompt quando é idêntico entre requests. System prompts longos e documentos estáticos são os maiores beneficiários.

### Arquitetura cache-friendly

```
[System prompt estático]    ← cacheado — nunca muda entre requests
[Documentos estáticos]      ← cacheado — muda raramente
[Histórico da conversa]     ← não cacheado — muda por request
[Query do usuário]          ← não cacheado — sempre novo
```

**Anti-pattern:** data/hora dinâmica no início do prompt invalida o cache sempre:

```python
# ❌ Cache sempre miss — timestamp muda a cada segundo
SYSTEM_PROMPT_BAD = f"Current time: {datetime.now().isoformat()}\n{LONG_STATIC_DOCS}"

# ✅ Estático no topo (cacheado), dinâmico no fim (não cacheado)
SYSTEM_PROMPT_GOOD = f"{LONG_STATIC_DOCS}"
messages = [{"role": "user", "content": f"[{datetime.now()}]\n{user_query}"}]
```

### Anthropic — cache breakpoints explícitos

```python
import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    system=[{
        "type": "text",
        "text": LONG_STATIC_SYSTEM_PROMPT,      # > 1024 tokens para ser elegível
        "cache_control": {"type": "ephemeral"}   # TTL padrão: 5 minutos
    }],
    messages=[{"role": "user", "content": user_query}]
)

# Verificar uso do cache
print(response.usage)
# 1a chamada: cache_creation_input_tokens=12450, cache_read_input_tokens=0
# 2a chamada: cache_creation_input_tokens=0, cache_read_input_tokens=12450
```

**Custos (claude-sonnet-4-6):**
- Cache write: 3.75× o custo normal (pago uma vez)
- Cache read: 0.1× o custo normal (10× mais barato)
- TTL padrão: 5 minutos
- Mínimo para cache: 1024 tokens

### OpenAI — cache automático

```python
from openai import OpenAI

client = OpenAI()

# Cache automático — nenhuma configuração necessária
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": LONG_SYSTEM_PROMPT},  # > 1024 tokens
        {"role": "user", "content": user_query}
    ]
)

print(response.usage)
# prompt_tokens=1500, cached_tokens=1400, completion_tokens=250
```

**Custos (gpt-4o):** cache hit = 50% de desconto automático no input.

### Break-even analysis

```
Fórmula:
  Custo sem cache = N × custo_normal × tamanho_prefix
  Custo com cache = 1 × custo_write + (N-1) × custo_read × tamanho_prefix

Exemplo (Anthropic Sonnet, prefix de 10k tokens):
  cache_write = $0.0375
  cache_read  = $0.0030
  normal      = $0.0300

  Break-even: N > 0.0375 / (0.030 - 0.003) ≈ 1.4 chamadas
  → A partir da 2ª chamada dentro do TTL, caching já compensa.
```

---

## Semantic Cache — cache por similaridade

Para queries que variam na forma mas têm a mesma semântica:

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
SIMILARITY_THRESHOLD = 0.92

def semantic_cache_lookup(query: str):
    query_embedding = model.encode(query)

    results = vector_store.search(
        embedding=query_embedding,
        top_k=1,
        score_threshold=SIMILARITY_THRESHOLD
    )

    if results and results[0].score >= SIMILARITY_THRESHOLD:
        return results[0].metadata["cached_response"]  # cache hit

    # Cache miss — gerar e armazenar
    response = call_llm(query)
    vector_store.upsert(embedding=query_embedding,
                        metadata={"query": query, "cached_response": response})
    return response

# "Qual o preço do produto X?" e "Me diga o preço do produto X"
# → mesma semântica → cache hit com threshold 0.92
```

---

## Long Context 2026 — Quando Usar vs RAG

Com Llama 4 Scout (10M tokens), Gemini 3.1 Flash (1M tokens) e janelas crescentes, a constraint que forçava RAG em 2024 foi removida para a maioria dos casos. O debate mudou: não é "como chunkar", é "quando RAG ainda faz sentido vs jogar o documento completo".

### Use Long Context quando:
```
├── Documento cabe com folga (< 50% da janela)
├── Queries exigem raciocínio sobre o documento inteiro
│   (ex: "compare seção 3 com seção 7", "quais contradições existem?")
├── Ordem e estrutura do documento importam
├── Latência < 2s não é requerida (long context aumenta TTFT)
└── One-shot (não há reutilização em múltiplas queries)
```

### Use RAG quando:
```
├── Knowledge base > 10M tokens (não cabe em nenhuma janela atual)
├── Dados atualizados frequentemente (RAG atualiza sem re-prompt)
├── Múltiplas queries sobre o mesmo corpus (retrieval amortiza custo)
├── Latência crítica < 500ms (retrieval paralelo é mais rápido)
├── Custo crítico — ver math abaixo
└── Precisão de citação requerida (RAG retorna source exata)
```

### Hybrid RAG + Long Context (padrão emergente)

Para bases 1M–10M tokens — o melhor dos dois mundos:

```python
async def hybrid_retrieval(query: str, corpus: list[Document]) -> str:
    # 1. Retrieval rápido para candidatos (BM25 + embedding)
    candidates = await retriever.search(query, top_k=20)

    # 2. Re-ranking semântico para top-5
    top_docs = reranker.rerank(query, candidates, top_k=5)

    # 3. Jogar o documento completo (não apenas chunk) no contexto longo
    #    Evita perda de contexto local do chunk
    context = "\n\n".join(doc.full_text for doc in top_docs)

    return await llm.complete(
        system="Answer based only on the provided context.",
        user=f"Context:\n{context}\n\nQuery: {query}",
        model="gemini-3-1-flash",  # 1M context a $0.07/M
    )
```

### Custo real de Long Context — math de decisão

```
Contrato de 50 páginas ≈ 25K tokens

Claude Opus 4.6 ($15/M input):
  1 query: 25K × $15/M = $0.375
  100 queries/dia: $37.50/dia → $1.125/mês

Gemini 3.1 Flash ($0.07/M input):
  1 query: 25K × $0.07/M = $0.00175
  100 queries/dia: $0.175/dia → $5.25/mês

→ Gemini Flash é 200× mais barato para long context pesado
→ Com prompt caching (mesmo contrato, N queries): economia adicional de 88%
```

| Critério | Long Context | RAG |
|---|---|---|
| Recall | 100% (vê tudo) | Depende do retrieval |
| Latência | Alta | Baixa |
| Custo | Alto (mas Gemini Flash muda o math) | Baixo |
| Atualização de dados | Reinjetar tudo | Re-indexar incrementalmente |
| Base > 10M tokens | Impossível | ✅ |
| Lost-in-the-middle | Risco (mitigado em frontier) | Controlado |

---

## Trade-offs das Estratégias

| Estratégia | Continuidade | Custo | Latência | Complexidade |
|---|---|---|---|---|
| Sliding Window | Baixa | Baixo | Baixa | Baixa |
| Summarization | Média | Médio (+1 call) | Média | Média |
| Vector Memory | Alta | Médio | Média | Alta |
| Full Context (janela grande) | Alta | Alto | Alta | Baixa |
| Prompt Caching | — | Muito baixo | Baixa | Baixa |

**Recomendação para produção:** Sliding Window + Summarization para chatbots. Vector Memory para assistentes com memória persistente. Prompt Caching sempre que system prompt > 1k tokens.

---

## Estrutura de System Prompt Otimizado

```python
SYSTEM_PROMPT = """
# Papel e Objetivo
Você é um assistente técnico especializado em arquitetura de software.

# Contexto Permanente
Empresa: fintech B2B. Stack: Node.js, PostgreSQL, Kubernetes.
Princípios: simplicidade, observabilidade, deploy seguro.

# Instruções de Comportamento
- Respostas diretas, sem introduções genéricas
- Sempre mostre trade-offs em decisões arquiteturais
- Use exemplos de código quando clarificar

# Formato de Saída
Para análises: Problem → Options → Recommendation → Risks
Para código: contexto → snippet → explicação
"""
# Anti-padrão: system prompt com 10k tokens de contexto irrelevante
# Isso degrada qualidade e aumenta custo desnecessariamente
```

---

## Quando Usar / Quando Evitar

**Sliding Window:** chatbots simples onde continuidade longa não é requisito.

**Summarization:** chatbots com sessões longas. Use modelo pequeno para sumarizar.

**Vector Memory:** assistentes pessoais, agentes com memória persistente entre sessões.

**Map-Reduce:** análise de documentos que não cabem no contexto (relatórios, codebase inteira).

**Prompt Caching:** sempre que system prompt > 1k tokens e há tráfego recorrente no mesmo sistema.

**Semantic Cache:** FAQ, suporte ao cliente, perguntas que variam na forma mas repetem em conteúdo.

---

## Conceitos Relacionados

[[como-llms-funcionam]] · [[prompt-engineering]] · [[rag-retrieval]] · [[agentes-core]] · [[agent-memory]]

---
*Fonte: tech-mentor skill · tech-mentor-ai · 2026-04-07*
