---
date: 2026-04-08
tags: [tech-mentor, ia, ai-gateway, litellm, portkey, routellm, cascade-pattern, semantic-cache, batch-api, token-economics, finops, cost-optimization]
skill: tech-mentor-ai/references/ai/ai-gateway.md
level: avançado
---

# AI Gateway & Token Economics

## Contexto

Em produção com múltiplos modelos, o problema não é "qual modelo usar" — é gerenciar custo, latência, disponibilidade e qualidade de forma programática. AI Gateways abstraem providers, roteiam por custo/qualidade, implementam fallback, cache semântico e budget enforcement. Token economics é a disciplina de otimizar o que você gasta para obter o resultado que precisa.

---

## LiteLLM — Proxy Multi-provider Open Source

Interface unificada para 100+ modelos via API OpenAI-compatible.

```yaml
# litellm_config.yaml
model_list:
  - model_name: gpt-4o
    litellm_params:
      model: openai/gpt-4o
      api_key: os.environ/OPENAI_API_KEY

  - model_name: claude-sonnet
    litellm_params:
      model: anthropic/claude-sonnet-4-6
      api_key: os.environ/ANTHROPIC_API_KEY

  - model_name: fast-cheap
    litellm_params:
      model: gemini/gemini-2.0-flash
      api_key: os.environ/GEMINI_API_KEY

router_settings:
  routing_strategy: cost-based-routing   # cheapest model first
  fallbacks:
    - {"gpt-4o": ["claude-sonnet", "fast-cheap"]}
  retry_policy:
    num_retries: 3
    retry_after: 1

litellm_settings:
  success_callback: ["langfuse"]
  failure_callback: ["langfuse"]
```

```python
import litellm

# Interface idêntica independente do provider
response = litellm.completion(
    model="claude-sonnet",
    messages=[{"role": "user", "content": "Explain CQRS"}],
    max_tokens=512
)

# Fallback automático — se claude falhar, tenta gpt-4o
# Logging automático para Langfuse/LangSmith
```

**Deploy como proxy:**
```bash
litellm --config litellm_config.yaml --port 8000
# Qualquer SDK OpenAI aponta para localhost:8000
```

---

## Portkey — AI Gateway Managed

Gateway gerenciado com fallback declarativo, semantic cache e observabilidade nativa.

```python
from portkey_ai import Portkey

portkey = Portkey(
    api_key=PORTKEY_API_KEY,
    config={
        "strategy": {
            "mode": "fallback"
        },
        "targets": [
            {
                "provider": "anthropic",
                "api_key": ANTHROPIC_API_KEY,
                "override_params": {"model": "claude-sonnet-4-6"}
            },
            {
                "provider": "openai",
                "api_key": OPENAI_API_KEY,
                "override_params": {"model": "gpt-4o-mini"}
            }
        ],
        "cache": {
            "mode": "semantic",    # cache por similaridade, não match exato
            "max_age": 86400       # 24h TTL
        },
        "retry": {
            "attempts": 3,
            "on_status_codes": [429, 500, 502, 503]
        }
    }
)

response = portkey.chat.completions.create(
    messages=[{"role": "user", "content": "What is RAG?"}]
)
```

**Diferencial Portkey vs LiteLLM:**

| | LiteLLM | Portkey |
|---|---|---|
| Self-host | ✅ Open source | ❌ Managed |
| Semantic cache | Manual | ✅ Built-in |
| Observabilidade | Via callbacks | ✅ Dashboard nativo |
| Config | YAML | SDK declarativo |
| Custo | Infra própria | Pago por volume |

---

## Roteamento Inteligente por Complexidade

Rotear queries para o modelo mais barato que consegue resolver a task.

```python
from dataclasses import dataclass
from enum import Enum

class TaskComplexity(Enum):
    SIMPLE = "simple"     # classificação, extração, FAQ
    MEDIUM = "medium"     # sumarização, análise, QA
    COMPLEX = "complex"   # raciocínio multi-step, código, planejamento

@dataclass
class ModelProfile:
    name: str
    cost_per_1k_tokens: float   # input + output médio
    avg_latency_ms: int
    strengths: list[str]

MODEL_PROFILES = {
    TaskComplexity.SIMPLE: ModelProfile(
        name="gemini-2.0-flash",
        cost_per_1k_tokens=0.0001,
        avg_latency_ms=200,
        strengths=["classification", "extraction", "simple_qa"]
    ),
    TaskComplexity.MEDIUM: ModelProfile(
        name="claude-haiku-4-5",
        cost_per_1k_tokens=0.0008,
        avg_latency_ms=400,
        strengths=["summarization", "analysis", "multi-turn"]
    ),
    TaskComplexity.COMPLEX: ModelProfile(
        name="claude-sonnet-4-6",
        cost_per_1k_tokens=0.015,
        avg_latency_ms=1200,
        strengths=["reasoning", "code", "planning", "nuanced_analysis"]
    )
}

async def classify_task_complexity(query: str) -> TaskComplexity:
    """Usa modelo barato para classificar antes de rotear."""
    prompt = f"""Classify this query complexity:
- SIMPLE: direct lookup, yes/no, extraction
- MEDIUM: summarization, multi-fact analysis
- COMPLEX: reasoning, code generation, planning

Query: {query}
Return only: SIMPLE, MEDIUM, or COMPLEX"""

    response = await fast_model.complete(prompt)
    return TaskComplexity(response.strip().lower())

async def smart_route(query: str) -> str:
    complexity = await classify_task_complexity(query)
    model = MODEL_PROFILES[complexity]
    return await call_model(model.name, query)
```

---

## Cascade Pattern — Cheap First, Scale Up

Tenta modelo barato primeiro, escala para modelo caro apenas se confiança for baixa.

```python
async def cascade_completion(prompt: str, threshold: float = 0.85) -> str:
    models_cascade = [
        ("gemini-2.0-flash",   0.0001),   # (model, cost_per_1k)
        ("claude-haiku-4-5",   0.0008),
        ("claude-sonnet-4-6",  0.015)
    ]

    for model_name, cost in models_cascade:
        response = await call_model_with_logprobs(model_name, prompt)

        # Confiança estimada via média dos log-probs dos tokens gerados
        confidence = estimate_confidence(response.logprobs)

        if confidence >= threshold:
            log_cascade_hit(model_name, confidence, cost)
            return response.text

        # Confiança baixa → escala para o próximo modelo
        log_cascade_miss(model_name, confidence)

    return response.text  # usa o melhor disponível


def estimate_confidence(logprobs: list[float]) -> float:
    """Média das probabilidades dos tokens — proxy de confiança."""
    import math
    probs = [math.exp(lp) for lp in logprobs if lp is not None]
    return sum(probs) / len(probs) if probs else 0.5
```

**Economia típica com Cascade:** 60–80% das queries resolvidas pelo modelo barato → redução de custo de 40–60%.

---

## Semantic Cache — Cache por Similaridade

Queries semanticamente similares reutilizam a resposta em cache, sem chamar o LLM.

```python
import redis
import numpy as np
from openai import OpenAI

client = OpenAI()
r = redis.Redis(host="localhost", port=6379, decode_responses=False)

CACHE_PREFIX = "semantic_cache:"
SIMILARITY_THRESHOLD = 0.92

async def embed_query(text: str) -> list[float]:
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding

def cosine_similarity(a: list[float], b: list[float]) -> float:
    a_arr, b_arr = np.array(a), np.array(b)
    return float(np.dot(a_arr, b_arr) / (np.linalg.norm(a_arr) * np.linalg.norm(b_arr)))

async def cached_completion(query: str, system_prompt: str) -> str:
    query_embedding = await embed_query(query)

    # Busca nas chaves de cache existentes
    cache_keys = r.keys(f"{CACHE_PREFIX}*")
    for key in cache_keys:
        cached = r.hgetall(key)
        stored_embedding = np.frombuffer(cached[b"embedding"], dtype=np.float32).tolist()
        similarity = cosine_similarity(query_embedding, stored_embedding)

        if similarity >= SIMILARITY_THRESHOLD:
            return cached[b"response"].decode()

    # Cache miss → chama LLM e armazena
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": query}
        ]
    )
    answer = response.choices[0].message.content

    cache_key = f"{CACHE_PREFIX}{hash(query)}"
    r.hset(cache_key, mapping={
        "embedding": np.array(query_embedding, dtype=np.float32).tobytes(),
        "response": answer,
        "query": query
    })
    r.expire(cache_key, 86400)  # TTL 24h

    return answer
```

**Hit rate típico em FAQ/suporte:** 30–50% → redução proporcional de custo.

---

## Batch API — 50% de Desconto Assíncrono

Para workloads sem latência crítica, Batch API oferece metade do preço com SLA de 24h.

```python
import anthropic
import json

client = anthropic.Anthropic()

# Preparar batch de requests
requests = [
    {
        "custom_id": f"analysis-{i}",
        "params": {
            "model": "claude-haiku-4-5-20251001",
            "max_tokens": 512,
            "messages": [{"role": "user", "content": document}]
        }
    }
    for i, document in enumerate(documents_to_analyze)
]

# Submeter batch (retorna imediatamente)
batch = client.messages.batches.create(requests=requests)
print(f"Batch ID: {batch.id}")  # poll depois

# Verificar status (pode ser cron job ou webhook)
batch_status = client.messages.batches.retrieve(batch.id)

if batch_status.processing_status == "ended":
    results = {}
    for result in client.messages.batches.results(batch.id):
        if result.result.type == "succeeded":
            results[result.custom_id] = result.result.message.content[0].text
        else:
            results[result.custom_id] = None  # tratar falha
```

**Quando usar Batch API:**
- Análise de documentos em bulk
- Geração de embeddings em escala
- Avaliação de evals offline
- Processamento noturno / pipelines ETL com LLM
- **Não usar:** qualquer fluxo que precise de resposta imediata

---

## Comparativo de Custo — Modelos Q1-Q2 2026

| Modelo | Input ($/1M) | Output ($/1M) | Contexto | Melhor para |
|---|---|---|---|---|
| Claude Opus 4.6 | $15.00 | $75.00 | 200k | Coding agents, 80.8% SWE-Bench |
| Claude Sonnet 4.5 | $3.00 | $15.00 | 200k (beta 1M) | Equilíbrio custo/qualidade |
| Claude Haiku 4.5 | $0.80 | $4.00 | 200k | Latência baixa, alta throughput |
| GPT-5.4 | $2.50 | $10.00 | 1M | Generalista, computer use |
| GPT-5.4 Pro | $30.00 | $180.00 | 1M | Extended reasoning máximo |
| Gemini 3.1 Pro | $1.25 | $10.00 | 2M | ARC-AGI-2 líder, multimodal |
| Gemini 3.1 Flash | $0.07 | $0.30 | 1M | Long context econômico |
| Gemini Flash Lite | $0.025 | $0.10 | 1M | Volume extremo, simples |
| DeepSeek V4 | $0.28 | $1.10 | 128k | Alto volume, 1/50 do Claude |
| Qwen3.5 27B (self-host) | ~$0.30 | ~$0.30 | 32k | Apache 2.0, privacidade |
| Gemma 4 E4B (local) | $0 | $0 | 128k | Edge/local, triagem simples |

*Preços aproximados Q1 2026 — verificar docs oficiais dos providers*

---

## FinOps — Budget Enforcement por Tenant

```python
from decimal import Decimal
import asyncio

BUDGET_LIMITS = {
    "free":       Decimal("1.00"),    # $1/dia
    "pro":        Decimal("10.00"),   # $10/dia
    "enterprise": Decimal("100.00")   # $100/dia
}

COST_PER_TOKEN = {
    "claude-sonnet-4-6": {"input": Decimal("0.000003"), "output": Decimal("0.000015")},
    "claude-haiku-4-5":  {"input": Decimal("0.0000008"), "output": Decimal("0.000004")},
    "gpt-4o-mini":       {"input": Decimal("0.00000015"), "output": Decimal("0.0000006")}
}

async def check_and_charge_budget(
    tenant_id: str,
    tier: str,
    model: str,
    input_tokens: int,
    output_tokens: int
) -> bool:
    cost = (
        COST_PER_TOKEN[model]["input"] * input_tokens +
        COST_PER_TOKEN[model]["output"] * output_tokens
    )

    # Redis para acumulação atômica por tenant/dia
    redis_key = f"budget:{tenant_id}:{date.today()}"
    current_spend = Decimal(await redis.get(redis_key) or "0")

    if current_spend + cost > BUDGET_LIMITS[tier]:
        raise BudgetExceededError(
            tenant_id=tenant_id,
            limit=BUDGET_LIMITS[tier],
            current=current_spend
        )

    await redis.incrbyfloat(redis_key, float(cost))
    await redis.expire(redis_key, 86400)  # TTL 24h
    return True


# Detecção de anomalia — custo > 3σ do histórico
async def detect_cost_anomaly(tenant_id: str) -> bool:
    # Query dos últimos 30 dias de gasto
    history = await db.fetchall("""
        SELECT date, SUM(cost_usd) as daily_cost
        FROM ai_cost_ledger
        WHERE tenant_id = $1
          AND created_at > NOW() - INTERVAL '30 days'
        GROUP BY date
        ORDER BY date
    """, tenant_id)

    if len(history) < 7:
        return False

    costs = [row["daily_cost"] for row in history]
    mean = sum(costs) / len(costs)
    std = (sum((c - mean) ** 2 for c in costs) / len(costs)) ** 0.5

    today_cost = costs[-1]
    return today_cost > mean + (3 * std)
```

---

## Streaming com Cancelamento

```typescript
async function streamWithCancellation(
  prompt: string,
  onChunk: (text: string) => void,
  timeoutMs = 30_000
): Promise<string> {
  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), timeoutMs);

  try {
    const stream = await anthropic.messages.stream(
      {
        model: "claude-haiku-4-5-20251001",
        max_tokens: 1024,
        messages: [{ role: "user", content: prompt }]
      },
      { signal: controller.signal }
    );

    let fullText = "";
    for await (const chunk of stream) {
      if (chunk.type === "content_block_delta" && chunk.delta.type === "text_delta") {
        onChunk(chunk.delta.text);
        fullText += chunk.delta.text;
      }
    }
    return fullText;
  } catch (err) {
    if (err.name === "AbortError") {
      throw new TimeoutError(`LLM stream exceeded ${timeoutMs}ms`);
    }
    throw err;
  } finally {
    clearTimeout(timeout);
  }
}
```

---

## Estratégias de Redução de Custo

```
1. Prompt Caching (Anthropic/OpenAI)
   → System prompt longo + few-shot examples = cache 90% do input
   → Redução de 75–90% no custo de tokens repetitivos

2. Semantic Cache
   → Hit rate 30–50% em FAQ e suporte
   → Redução proporcional ao hit rate

3. Cascade Pattern
   → 60–80% das queries no modelo barato
   → Redução de 40–60% no custo total

4. Context Compression
   → Sumarizar histórico antes de injetar
   → Redução de 50–70% em conversas longas

5. Batch API
   → 50% de desconto em workloads assíncronos
   → Ideal para ETL, evals offline, análise bulk

6. Model Downgrade por Tarefa
   → Usar Haiku/Flash para classificação, extração
   → Reservar Sonnet/GPT-4o para raciocínio complexo
```

**Impacto composto — aplicando todas as estratégias:**
```
Baseline:         $1.000/mês
+ Prompt Caching: $400/mês  (−60%)
+ Semantic Cache: $280/mês  (−30%)
+ Cascade:        $168/mês  (−40%)
+ Batch API:      $140/mês  (−17%)
Total:            86% de redução
```

---

## Intent Routing — Roteamento por Intenção

```python
INTENT_ROUTING = {
    "greeting":      "gemini-2.0-flash",      # ultra-barato, latência zero
    "faq":           "gemini-2.0-flash",      # resposta curta, determinística
    "analysis":      "claude-haiku-4-5",      # raciocínio médio
    "code_review":   "claude-sonnet-4-6",     # qualidade crítica
    "planning":      "claude-sonnet-4-6",     # raciocínio complexo
    "unknown":       "claude-haiku-4-5"       # fallback seguro
}

async def route_by_intent(query: str) -> str:
    intent = await classify_intent(query)
    model = INTENT_ROUTING.get(intent, INTENT_ROUTING["unknown"])
    return await call_model(model, query)
```

---

## Quando Usar Cada Estratégia

| Situação | Estratégia |
|---|---|
| Volume alto, queries repetitivas (FAQ, suporte) | Semantic Cache + Prompt Caching |
| Tasks heterogêneas com qualidade variável | Cascade Pattern |
| Análise de documentos em bulk, sem urgência | Batch API |
| Multi-provider, precisa de fallback | LiteLLM ou Portkey |
| Budget por tenant com alertas | FinOps middleware + Redis |
| Controle total + self-host | LiteLLM open source |
| Managed, zero infra, observabilidade nativa | Portkey |

---

## Conceitos Relacionados

[[evals-sistematicas]] · [[llmops-observabilidade]] · [[context-engineering]] · [[fine-tuning]] · [[rag-retrieval]]

---
*Fonte: tech-mentor skill · tech-mentor-ai · 2026-04-08*
