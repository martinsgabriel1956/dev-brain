---
date: 2026-04-08
tags: [tech-mentor, ia, open-weight, self-hosted, vllm, sglang, gemma4, qwen35, llama4, quantizacao, lora, licenciamento, finops]
skill: tech-mentor-ai/references/ai/open-weight-deployment-2026.md
level: avançado
---

# Open-Weight Deployment em Produção (2026)

## Contexto

Até 2024, self-hosting era nicho: modelos open-weight ficavam bem atrás dos fechados em qualidade e o breakeven só acontecia a ~$3k/mês em API. Em 2026, três mudanças tornam a decisão obrigatória para qualquer sistema de produção:

1. **Gap de qualidade fechou** — Qwen3.5 27B está a 3 pontos de SWE-Bench dos modelos fechados mid-tier
2. **Apache 2.0 como padrão** — Gemma 4 e Qwen3.5 eliminam a fricção jurídica do Llama 4
3. **Breakeven em ~$800/mês** — era $3k em 2025; a queda no custo de GPUs consumer tornou viável muito antes

---

## Famílias de Modelos 2026

### Apache 2.0 — Zero fricção jurídica

| Modelo | Params ativos | VRAM mínima | Destaque |
|---|---|---|---|
| Gemma 4 E2B | 2.3B | 4GB | Edge/mobile, audio, 128K context |
| Gemma 4 E4B | 4.5B | 8GB | Edge com mais capacidade |
| Gemma 4 MoE | 26B / 3.8B ativo | 20GB | Mais eficiente por parâmetro ativo |
| Gemma 4 31B Dense | 31B | 24GB | AIME 2026: 89.2%, #3 LMArena |
| Qwen3.5 27B | 27B | 24GB | Melhor coding open (~72% SWE-Bench) |
| Qwen3.5 235B MoE | 397B / 17B ativo | 4×H100 | Near-frontier, 119 idiomas |
| Qwen3.5-Omni | 27B | 24GB | Único open-weight com speech output real-time |
| GPT-oss-120b | 120B | 4×H100 | Primeiro open-weight OpenAI (ago/2025) |

### Llama 4 Community License (até 700M MAU)

| Modelo | Params ativos | Destaque |
|---|---|---|
| Llama 4 Scout | 109B / 17B MoE | 10M context — sem equivalente Apache 2.0 |
| Llama 4 Maverick | 400B / 17B MoE | Máxima capacidade Meta |

---

## Árvore de Decisão — Qual Família

```
Precisa de Apache 2.0 irrestrito?
├── SIM → Gemma 4 ou Qwen3.5
│         ├── Audio/speech nativo?      → Qwen3.5-Omni
│         ├── Foco em math/coding?      → Gemma 4 31B Dense
│         ├── VRAM limitada (<24GB)?    → Gemma 4 MoE (3.8B ativos)
│         └── Edge/mobile?             → Gemma 4 E2B ou E4B
└── NÃO (Llama 4 OK para < 700M MAU)
          ├── Contexto > 1M tokens?    → Llama 4 Scout (10M)
          └── Máxima capacidade?       → Llama 4 Maverick
```

---

## Inference Engines: vLLM vs SGLang

A maioria dos modelos relevantes de 2026 usa MoE. A escolha do engine impacta throughput e latência.

### vLLM — padrão histórico

```bash
vllm serve Qwen/Qwen3.5-27B-Instruct \
  --tensor-parallel-size 2 \
  --max-model-len 32768 \
  --enable-chunked-prefill \
  --dtype bfloat16
```

- **Pontos fortes:** PagedAttention maduro, ecossistema amplo, integração com KServe/SageMaker/Vertex AI
- **Use quando:** workloads genéricos, cloud providers, suporte de equipe menor

### SGLang — emergindo em 2026

```bash
python -m sglang.launch_server \
  --model-path Qwen/Qwen3.5-27B-Instruct \
  --tp 2 \
  --context-length 32768
```

- **Pontos fortes:** RadixAttention para caching de prefixo compartilhado; 20–40% mais throughput em workloads agentic com system prompts repetidos
- **Use quando:** multi-tenant com system prompts longos e fixos (chatbots, agentes com tool definitions fixas)

**Decisão prática:** SGLang para agentes/chatbots com system prompt grande compartilhado. vLLM para tudo o mais.

---

## Quantização para MoE

MoE tem comportamento diferente de modelos densos — a sparsidade já reduz compute, quantização adiciona redução de memória.

| Técnica | Qualidade (vs FP16) | Redução VRAM | Velocidade |
|---|---|---|---|
| FP8 (E4M3) | -0.5% benchmark | -50% | +30% throughput |
| INT8 (GPTQ) | -1.5% | -60% | +20% throughput |
| INT4 (AWQ) | -3% | -70% | +50% throughput |
| Q4_K_M (GGUF) | -2% | -70% | Consumer CPU viável |

**Para MoE em produção:** FP8 é o melhor trade-off. Para consumer GPU: Q4_K_M com llama.cpp/Ollama.

```python
# Qwen3.5 27B em FP8 — cabe em 1×RTX 4090 (~20GB VRAM)
from transformers import AutoModelForCausalLM
import torch

model = AutoModelForCausalLM.from_pretrained(
    "Qwen/Qwen3.5-27B-Instruct",
    torch_dtype=torch.float8_e4m3fn,
    device_map="auto",
)
```

---

## Custo Real: Self-hosted vs API (2026)

### Cenário: 10M tokens/dia (workload médio B2B SaaS)

```
Claude Sonnet 4.5 API (~$3/M input, $15/M output, mix 70/30):
  Input:  7M × $3/M  = $21/dia
  Output: 3M × $15/M = $45/dia
  Total:  $66/dia → ~$2.000/mês

Qwen3.5 27B self-hosted (RTX 4090, ~35 tok/s):
  GPU cloud (1× RTX 4090): $0.40/h = $9.60/dia
  Throughput: 3M tokens/dia por GPU → 4 GPUs para 10M tokens
  Total: 4 × $9.60 = $38/dia → ~$1.150/mês
  Economia: ~42%

Breakeven (volumes menores):
  Para 3M tokens/dia → 1 GPU basta → $9.60/dia vs $20/dia (API) → compensa
  Novo threshold de 2026: ~$800/mês em API já compensa
```

**Modelos grandes (235B+) ainda não compensam self-host a volumes médios** — requerem 4×H100 ($192/dia) e throughput não acompanha.

---

## Fine-tuning Open-Weight em Produção

### LoRA em Qwen3.5 27B — cabe em 1×A100

```python
from peft import LoraConfig, get_peft_model
from transformers import AutoModelForCausalLM
from trl import SFTTrainer

model = AutoModelForCausalLM.from_pretrained(
    "Qwen/Qwen3.5-27B-Instruct",
    torch_dtype="bfloat16",
    device_map="auto",
)

lora_config = LoraConfig(
    r=16,
    lora_alpha=32,
    target_modules=["q_proj", "v_proj", "k_proj", "o_proj"],
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM",
)

model = get_peft_model(model, lora_config)
# Treina apenas ~0.1% dos parâmetros — cabe em 1×A100 (80GB) ou 2×A100 (40GB)
```

**Quando fine-tuning compensar vs alternativas:**
```
Prompt engineering: < 1 semana, sem dados, sem infra
  → Use quando: comportamento padrão do modelo já está próximo

RAG: 1–2 semanas, pipeline, sem treinamento
  → Use quando: conhecimento factual atualizado, docs proprietários

Fine-tuning: 2–4 semanas, 500+ exemplos, GPU
  → Use quando: estilo/formato muito específico, latência crítica
    (system prompt longo aumenta TTFT), domain shift profundo
```

---

## Multi-tier Strategy — Padrão de Produção

```typescript
// Tier 1: triagem simples → modelo edge local (zero custo)
// Tier 2: tasks médias  → API econômica
// Tier 3: tasks complexas → frontier fechado

async function routeToModel(task: AITask): Promise<Response> {
  const complexity = await assessComplexity(task); // modelo leve local

  if (complexity < 0.3) {
    return await localModel.complete(task);   // Gemma 4 E4B, sub-50ms, grátis
  } else if (complexity < 0.7) {
    return await geminiFlash.complete(task);  // $0.025/M tokens
  } else {
    return await claudeOpus.complete(task);   // máxima qualidade, agentic
  }
}
```

---

## Licenciamento — Comparativo

| Aspecto | Apache 2.0 (Gemma 4, Qwen3.5) | Llama 4 Community | Proprietário (Claude, GPT) |
|---|---|---|---|
| Uso comercial | Irrestrito | Gratuito até 700M MAU | Via API terms |
| Fine-tuning | Livre | Livre | Limitado por API |
| Redistribuição | Livre | Livre + "Built with Llama" | Proibido |
| Enterprise adoption | Zero fricção jurídica | Risco acima de 700M MAU | Via contrato SLA |

**Decisão prática:** para novos projetos enterprise que querem open-weight, Gemma 4 ou Qwen3.5 com Apache 2.0 eliminam a revisão jurídica que o Llama 4 ainda exige.

---

## Quando Usar / Quando Evitar

**Use self-hosted quando:**
- LGPD, HIPAA, SOC2 não permitem saída de dados
- Volume previsível > ~800/mês em API (2026 threshold)
- Fine-tuning frequente por domínio
- Latência < 30ms (mesmo VPC ou mesmo host)
- Conformidade Apache 2.0 necessária

**Não use self-hosted quando:**
- MVP ou time-to-market crítico
- Volume imprevisível (picos de 100×)
- Equipe sem capacidade de MLOps
- Frontier capability necessária (80%+ SWE-Bench)

---

## Conceitos Relacionados

[[como-llms-funcionam]] · [[fine-tuning]] · [[ai-gateway-token-economics]] · [[agentes-em-producao]] · [[llmops-observabilidade]]

---
*Fonte: tech-mentor skill · tech-mentor-ai · 2026-04-08*
