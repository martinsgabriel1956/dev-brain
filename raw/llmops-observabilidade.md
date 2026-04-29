---
date: 2026-04-08
tags: [tech-mentor, ia, llmops, observabilidade, traces, spans, ttft, cost-attribution, langfuse, langsmith, arize, helicone, opentelemetry, prompt-versioning, slo, evals-online]
skill: tech-mentor-ai/references/ai/llm-observability.md
level: avançado
---

# LLMOps & Observabilidade

## Contexto

Sem observabilidade, você não sabe o que está gastando nem por quê as respostas estão ruins. Observabilidade de LLMs vai além de métricas de infra (CPU, latência p99) — o que importa é entender o que o modelo está fazendo, por quê, quanto custa por feature e onde falha. Sem isso você está voando cego em produção.

---

## Como Funciona

### Estrutura hierárquica de traces LLM

LLM traces têm estrutura diferente de traces HTTP convencionais — spans aninhados com custo, tokens e qualidade por nível:

```
Trace (request do usuário)
└── Span: LLM call (input_tokens=1200, output_tokens=340, latência=1.2s)
    ├── Span: Tool call — search(query="...")
    │   └── Span: LLM call (summarize results)
    └── Span: Tool call — code_exec(code="...")
```

**Métricas por span:**

| Métrica | O que mede | SLO típico |
|---|---|---|
| **TTFT** | Time to First Token — latência percebida | < 500ms (p95) |
| **TPS** | Tokens per second — throughput | Depende do modelo |
| **Input/output tokens** | Custo direto | — |
| **Latência total** | SLA end-to-end | < 5s (p95) |
| **Score de qualidade** | Evals online | > 0.75 |

---

## Ferramentas

### Langfuse — open source, self-hostável

Mais popular para LLM tracing em produção. Zero lock-in — self-hostável com Docker.

```python
from langfuse import Langfuse
from langfuse.decorators import observe, langfuse_context

langfuse = Langfuse()

@observe()
def process_query(user_id: str, query: str) -> str:
    # Associar trace a usuário e feature para cost attribution
    langfuse_context.update_current_trace(
        user_id=user_id,
        metadata={"feature": "document_search", "team": "product", "user_tier": "enterprise"}
    )

    response = llm.invoke(query)

    # Score inline (LLM-as-judge assíncrono)
    langfuse_context.score_current_observation(name="relevance", value=0.9)

    return response
```

**Features principais:**
- Traces e spans com SDK para Python, JS/TS, LangChain, LlamaIndex
- Prompt management — versioning de prompts linkado a traces
- Cost tracking por modelo, usuário, feature
- Evals online com score automático ou humano por trace
- Exporta métricas para Prometheus/Grafana via `/metrics`

---

### LangSmith — integrado ao LangChain/LangGraph

Diferencial: trace automático de chains e agentes LangGraph sem código extra. Dataset management para salvar traces como exemplos de eval.

```python
from langfuse.callback import CallbackHandler

handler = CallbackHandler(
    public_key="pk-...",
    secret_key="sk-...",
    session_id=session_id,
    user_id=user_id,
    tags=["production", "agent-v2"]
)

agent.invoke(input, config={"callbacks": [handler]})
```

---

### Arize Phoenix — debugging e drift

Foco em análise de qualidade. Detecta drift de distribuição de inputs via visualização de embeddings.

**Diferencial:** span-level evals — roda métricas de toxicidade, relevância, alucinação sobre cada span individualmente. Integração nativa com OpenTelemetry.

---

### Helicone — zero código, proxy reverso

```python
# Zero mudança no código — só troca a base URL
from openai import OpenAI

client = OpenAI(
    base_url="https://oai.helicone.ai/v1",
    default_headers={"Helicone-Auth": f"Bearer {HELICONE_KEY}"}
)
# Captura automaticamente todos os calls — latência, tokens, custo, erros
```

**Quando usar:** protótipos, quando não quer instrumentar código, time sem OTel.

---

## Instrumentação com OpenTelemetry GenAI

Padrão oficial para observabilidade de LLMs — qualquer APM (Datadog, Grafana, Honeycomb) entende spans com esses atributos.

```python
from opentelemetry.instrumentation.openai import OpenAIInstrumentor

# Instrumentação automática — todos os calls OpenAI viram spans OTel
OpenAIInstrumentor().instrument()

# Atributos semânticos padronizados (OpenTelemetry GenAI SIG 2025)
# gen_ai.system             → "openai" | "anthropic" | "google_vertex_ai"
# gen_ai.operation.name     → "chat" | "text_completion" | "embeddings"
# gen_ai.request.model      → "gpt-4o"
# gen_ai.usage.input_tokens → 1200
# gen_ai.usage.output_tokens → 340
```

**Instrumentação manual quando precisa de controle:**
```python
from opentelemetry import trace
from opentelemetry.semconv._incubating.attributes import gen_ai_attributes as GenAI

tracer = trace.get_tracer("my-ai-app")

async def traced_complete(prompt: str) -> str:
    with tracer.start_as_current_span("llm.chat") as span:
        span.set_attribute(GenAI.GEN_AI_SYSTEM, "anthropic")
        span.set_attribute(GenAI.GEN_AI_REQUEST_MODEL, "claude-3-5-haiku-20241022")

        response = await anthropic_client.messages.create(
            model="claude-3-5-haiku-20241022",
            max_tokens=1024,
            messages=[{"role": "user", "content": prompt}]
        )

        span.set_attribute(GenAI.GEN_AI_USAGE_INPUT_TOKENS, response.usage.input_tokens)
        span.set_attribute(GenAI.GEN_AI_USAGE_OUTPUT_TOKENS, response.usage.output_tokens)

        return response.content[0].text
```

---

## Cost Attribution — por usuário, feature e modelo

O padrão é passar metadata nos traces para segmentar custo. Permite queries como "qual feature gasta mais tokens?" ou "qual plano de usuário tem maior custo de LLM?".

```python
# Middleware de atribuição de custo — registra em banco e Prometheus
class CostAttributionMiddleware:
    async def __call__(self, request: LLMRequest) -> LLMResponse:
        response = await self.next(request)

        cost = calculate_cost(
            model=response.model,
            input_tokens=response.usage.input_tokens,
            output_tokens=response.usage.output_tokens
        )

        await db.execute("""
            INSERT INTO ai_cost_ledger
            (tenant_id, user_id, feature, model, input_tokens, output_tokens, cost_usd, ts)
            VALUES ($1, $2, $3, $4, $5, $6, $7, NOW())
        """, request.tenant_id, request.user_id, request.feature,
            response.model, response.usage.input_tokens,
            response.usage.output_tokens, cost)

        ai_cost_counter.labels(
            tenant=request.tenant_id,
            feature=request.feature,
            model=response.model
        ).inc(cost)

        return response
```

---

## Evals Online — qualidade em tráfego real

Diferente de evals offline (batch sobre dataset), evals online rodam sobre tráfego real para detectar degradação de qualidade antes que usuários reclamem.

```python
@observe()
def answer_question(question: str) -> str:
    answer = llm.invoke(question)

    # Avaliação assíncrona — não bloqueia a resposta ao usuário
    asyncio.create_task(score_answer(question, answer))

    return answer

async def score_answer(question: str, answer: str):
    score = await judge_llm.invoke(
        f"Rate relevance 0.0-1.0: Question={question} Answer={answer}\nReturn only a number."
    )
    langfuse_context.score_current_observation(name="relevance", value=float(score))
```

**Sampling estratégico** — não avalie 100% dos traces (caro):
- 5–10% aleatório do tráfego
- 100% dos traces com latência > P95
- 100% dos traces com feedback negativo do usuário
- 100% dos primeiros 10 calls de usuários novos

---

## Prompt Versioning — gerenciar como código

Cada versão de prompt deve ser rastreável, linkada aos traces que ela gerou e comparável com versões anteriores.

```python
# Langfuse Prompt Management
from langfuse import Langfuse

langfuse = Langfuse()

# Criar versão de prompt
prompt = langfuse.create_prompt(
    name="support-agent-system",
    prompt="You are a support agent for Acme Corp. {context}",
    labels=["production"],  # tag de deployment
    config={"model": "gpt-4o", "temperature": 0}
)

# Usar versão específica em produção
production_prompt = langfuse.get_prompt("support-agent-system", label="production")
compiled = production_prompt.compile(context=customer_context)

# Traces são automaticamente linkados ao prompt + versão
# → você sabe exatamente qual versão gerou qual output
```

---

## A/B Testing de Prompts

```python
import random

async def ab_test_prompt(user_id: str, query: str) -> str:
    # Bucket determinístico por user_id — mesmo usuário sempre vê mesma variante
    variant = "A" if int(hashlib.md5(user_id.encode()).hexdigest(), 16) % 2 == 0 else "B"

    prompt = PROMPT_A if variant == "A" else PROMPT_B

    with langfuse.trace(name="ab_test", metadata={"variant": variant, "user_id": user_id}):
        response = await llm.complete(prompt.format(query=query))
        return response

# Comparar métricas por variante no Langfuse:
# - Score médio de relevância (A vs B)
# - Latência média (A vs B)
# - Custo médio por request (A vs B)
# - Taxa de feedback negativo (A vs B)
```

---

## SLOs para LLM — definir e monitorar

```python
# Definição de SLOs por feature
LLM_SLOs = {
    "chat": {
        "ttft_p95_ms": 500,       # 95% das respostas com primeiro token em < 500ms
        "latency_p95_ms": 5000,   # 95% das respostas completas em < 5s
        "error_rate_pct": 1.0,    # < 1% de erros
        "quality_score_min": 0.75  # score médio de relevância > 0.75
    },
    "document_analysis": {
        "ttft_p95_ms": 2000,      # mais permissivo — task mais pesada
        "latency_p95_ms": 30000,
        "error_rate_pct": 0.5,
        "quality_score_min": 0.80
    }
}

# Alertas
ALERT_THRESHOLDS = {
    "ttft_ms": 1000,           # > 1s por 5 minutos
    "latency_ms": 10000,       # > 10s por 5 minutos
    "error_rate_pct": 2.0,     # > 2% por 10 minutos
    "cost_deviation_pct": 50,  # desvio > 50% do baseline em 1h
    "quality_score": 0.6       # score médio < 0.6 por 30 minutos
}
```

---

## Prompt Drift Detection

Detecta quando a qualidade de um prompt degrada silenciosamente (geralmente por atualização silenciosa do modelo pelo provider).

```python
class PromptDriftMonitor:
    def __init__(self, golden_dataset: list[dict], threshold = 0.85):
        self.golden = golden_dataset  # [{input, expected_output, score_fn}]
        self.threshold = threshold

    async def check_drift(self, prompt_version: str) -> DriftReport:
        scores = []
        for sample in self.golden:
            output = await llm.complete(sample["input"])
            score = sample["score_fn"](output, sample["expected_output"])
            scores.append(score)

        avg_score = sum(scores) / len(scores)
        return DriftReport(
            prompt_version=prompt_version,
            score=avg_score,
            drifted=avg_score < self.threshold,
            failures=[s for s, sc in zip(self.golden, scores) if sc < 0.7]
        )

# Rodar diariamente via cron — detecta degradações antes dos usuários reportarem
monitor = PromptDriftMonitor(golden_dataset=load_golden_set())
report = await monitor.check_drift("v1.3.2")
if report.drifted:
    alert_team(report)
```

---

## Session Replay de Agentes

Para debugar por que um agente tomou uma decisão errada:

```python
@dataclass
class AgentEvent:
    session_id: str
    step: int
    event_type: str  # "tool_call" | "llm_response" | "decision" | "error"
    timestamp: datetime
    payload: dict    # args, response, reasoning

async def instrumented_agent_loop(task: str) -> str:
    session_id = str(uuid4())
    events = []

    messages = [{"role": "user", "content": task}]
    for step in range(max_steps):
        response = await llm.complete(messages=messages, tools=tools)
        events.append(AgentEvent(session_id, step, "llm_response",
                                 datetime.now(), {"content": response.content}))

        for tool_call in get_tool_calls(response):
            result = await execute_tool(tool_call)
            events.append(AgentEvent(session_id, step, "tool_call",
                                     datetime.now(), {
                                         "tool": tool_call.name,
                                         "args": tool_call.input,
                                         "result": result
                                     }))

    # Persistir para replay posterior
    await event_store.save_session(session_id, events)
    return extract_final_response(response)
```

---

## Trade-offs das Ferramentas

| Ferramenta | Self-host | Integração LangChain | Custo | Melhor para |
|---|---|---|---|---|
| Langfuse | ✅ | ✅ | Grátis (self-host) | Produção, controle total |
| LangSmith | ❌ | ✅✅ nativo | Pago | Times usando LangGraph |
| Arize Phoenix | ✅ | ✅ | Grátis (OSS) | Debugging de qualidade, drift |
| Helicone | ❌ | ✅ | Freemium | PoC, zero instrumentação |

---

## Quando Usar / Quando Evitar

**Instrumentação com OTel sempre:** é o padrão da indústria, não acopla a uma ferramenta específica.

**Langfuse em produção:** self-host para dados sensíveis, custo controlado, prompt versioning.

**Evals online:** sempre que a qualidade é crítica e não pode esperar por feedback de usuários. Sampling de 5–10% já é suficiente para detectar regressões.

**A/B testing de prompts:** antes de fazer rollout de qualquer mudança de prompt significativa em produção.

---

## Conceitos Relacionados

[[production-evals]] · [[agentes-orquestracao]] · [[token-economics]] · [[ai-safety-engineering]] · [[rag-retrieval]]

---
*Fonte: tech-mentor skill · tech-mentor-ai · 2026-04-08*
