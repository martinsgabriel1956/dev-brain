---
date: 2026-04-07
tags: [tech-mentor, ia, llms, fundamentos, transformers, tokenizacao, attention]
skill: tech-mentor-ai/references/ai/fundamentals.md
level: fundamento
---

# Como LLMs Funcionam

## Contexto

LLMs (Large Language Models) são o motor de toda IA generativa moderna. Sem entender o que acontece internamente, cada decisão arquitetural — escolha de modelo, tamanho de contexto, custo por request — fica no escuro. Esse é o fundamento sobre o qual RAG, agentes, fine-tuning e tudo mais é construído.

---

## Como Funciona

### A tarefa central: prever o próximo token

Um LLM faz uma coisa: dado um contexto, estima a probabilidade de cada token possível ser o próximo. O texto é gerado token a token, de forma auto-regressiva.

```
"A capital do Brasil" → P(token seguinte)
  "é"       → 0.82
  "foi"     → 0.07
  ","       → 0.04
  ...
```

Tudo o mais — raciocínio, código, respostas coerentes — emerge desse processo repetido.

---

### Arquitetura Transformer

```
Input tokens → Embeddings + Positional Encoding
             → N × [Multi-Head Attention → Add & Norm → FFN → Add & Norm]
             → Logits → Softmax → Próximo token
```

**Multi-Head Attention** — cada token "olha" para todos os outros e decide o quanto prestar atenção:

```python
def attention(Q, K, V, mask=None):
    d_k = Q.size(-1)
    scores = torch.matmul(Q, K.transpose(-2, -1)) / d_k**0.5
    if mask is not None:
        scores = scores.masked_fill(mask == 0, float('-inf'))
    weights = F.softmax(scores, dim=-1)  # distribuição de atenção
    return torch.matmul(weights, V)      # média ponderada dos Values
```

- **Q (Query):** o que este token está procurando?
- **K (Key):** o que cada token oferece?
- **V (Value):** o conteúdo a ser agregado

"Multi-head" = roda esse processo H vezes em subespaços diferentes. Cada head aprende relações distintas: sintaxe, semântica, co-referência, etc.

**FFN (Feed-Forward Network):** aplicado por token após o attention. 2 camadas lineares com ativação GELU. É aqui que reside boa parte do "conhecimento factual" do modelo.

**Positional Encoding:** o Transformer não tem noção de ordem por si só — a atenção é invariante à posição. Encodings (sinusoidais ou aprendidos) injetam informação de onde cada token está na sequência.

---

### Tokenização — tokens ≠ palavras

Os modelos não processam caracteres nem palavras — processam **tokens**, unidades aprendidas pelo algoritmo BPE (Byte Pair Encoding).

```python
import tiktoken

enc = tiktoken.encoding_for_model("gpt-4")
enc.encode("Hello, world!")         # → [9906, 11, 1917, 0]  — 4 tokens
enc.encode("Hello")                 # → [9906]                — 1 token
```

**Regras de thumb:**

| Contexto     | Chars/token                      |
| ------------ | -------------------------------- |
| Inglês       | ~4 chars/token                   |
| Código       | ~3 chars/token (muitos símbolos) |
| Português    | ~3.5 chars/token                 |
| Chinês/Árabe | 1–2 chars/token → mais caro      |

**Implicações arquiteturais:**
- Custo é por token (input + output separadamente)
- Palavras raras e nomes próprios = mais tokens = mais caro
- Código é tokenizado de forma diferente de prosa

---

### Context Window

A quantidade de tokens que o modelo processa de uma vez. Tudo além desse limite é simplesmente ignorado.

| Modelo               | Context Window |
| -------------------- | -------------- |
| Llama 4 Scout        | 10M tokens     |
| Gemini 3.1 Pro/Flash | 1M–2M tokens   |
| GPT-5.4              | 1M tokens      |
| Claude Opus 4.6      | 200k tokens    |
| Qwen3.5 27B          | 32k tokens     |
| Gemma 4 31B          | 128k tokens    |

**1M tokens ≈ 750k palavras ≈ 1.500 páginas.**

Atenção é O(n²) — dobrar o contexto quadruplica o custo computacional. Contexto grande = latência maior e custo maior.

---

### Temperatura e controles de aleatoriedade

**Temperatura** controla o quão "achatada" ou "afiada" é a distribuição de probabilidade sobre os tokens.

```
Temperatura = 0   → sempre escolhe o token mais provável (determinístico)
Temperatura = 0.7 → criativo, mas coerente
Temperatura > 1   → aleatório, surpreendente, potencialmente incoerente
```

**Top-p (nucleus sampling):** considera apenas os tokens cuja probabilidade acumulada atinge p. `top_p = 0.9` filtra tokens muito improváveis antes de amostrar.

**Decisão prática:**
```
Extração de dados estruturados → temperature: 0
Geração de conteúdo criativo   → temperature: 0.7–1.0
Código                         → temperature: 0.2–0.4
```

---

### Custo por token — input vs output

Input e output têm preços diferentes. Output costuma ser 3–5× mais caro por token porque exige computação auto-regressiva.

**Estratégia de modelo pequeno/grande (Cascade Pattern):**
```
Request chega → modelo pequeno (haiku, mini) tenta resolver
             ↓ se confiança baixa ou task complexa
             → modelo grande (sonnet, gpt-4o)
```

Isso reduz custo em 60–80% em cargas de trabalho mistas.

---

### Latência vs qualidade — quando streaming importa

- **TTFT (Time to First Token):** latência percebida pelo usuário. Streaming reduz TTFT — o usuário vê a resposta chegando progressivamente.
- **Modelos grandes** têm TTFT maior. Para aplicações interativas, considere modelos menores ou streaming obrigatório.
- **Batch API:** para processamento offline, aceita latência maior em troca de 50% de desconto (OpenAI, Anthropic).

---

### Mixture of Experts (MoE)

Substitui o FFN único por N "especialistas", ativando apenas k deles por token via um router.

```
Dense:  Token → Attention → FFN (sempre ativo) → Output
MoE:    Token → Attention → Router → Exp1, Exp3 (k=2 de N) → Output ponderado
```

**Por que importa:**
```
Mixtral 8x7B: 46B parâmetros totais, 12.9B ativos por token
  → Qualidade próxima a Llama 70B, custo computacional de 13B
```

- Mais parâmetros com o mesmo custo de inferência
- Mais memória necessária (todos os experts precisam estar em VRAM)
- **Expert collapse** é o problema principal: router envia tudo para os mesmos 2 experts

---

### State Space Models — Mamba e alternativas O(n)

Alternativas ao Transformer para sequências muito longas. Atenção padrão é O(n²) — 100k tokens = 10B operações.

```
Mamba (SSM seletivo): O(n) linear
  h(t) = A·h(t-1) + B·x(t)   ← estado atualizado
  y(t) = C·h(t) + D·x(t)     ← output
  A, B, C variam com o input  ← "seletividade" (diferencial do Mamba)
```

| | Transformer | Mamba | Linear Attention |
|---|---|---|---|
| Complexidade | O(n²) | O(n) | O(n) |
| Qualidade (seq. longa) | ✅ | ✅ | ⚠️ Degrada |
| KV Cache | Cresce com n | Fixo | Fixo |
| Hardware maturo | ✅ | ⚠️ Kernel custom | ⚠️ |

**Status 2026:** modelos híbridos (Transformer + SSM intercalados) são o estado da arte para contexto longo — ex: Jamba, Zamba.

---

### Text Diffusion Models — Alternativa Não-Autoregressiva

Enquanto Transformers geram token a token (sequencial), modelos de difusão para texto geram em paralelo removendo ruído progressivamente.

```
Autoregressive (padrão):
  Token 1 → Token 2 → Token 3 → Token N   (latência ∝ N)

Text Diffusion (Mercury, Inception Labs — fev/2025):
  Ruído → denoising paralelo → todos os tokens   (latência sublinear)
```

**Estado atual:** Mercury (primeiro relevante para código) tem latência 5–10× menor que modelos AR comparáveis, mas qualidade ~10–15% abaixo de Claude Sonnet 4.5 em SWE-Bench. Relevante quando latência < 200ms é requerida e qualidade pode ser menor.

---

### FlashAttention 2/3 — IO-aware attention

Mesmo resultado matemático do attention padrão, radicalmente mais eficiente em memória.

**Problema do attention padrão:** materializa a matriz N×N inteira na HBM (memória lenta da GPU).
Para 10k tokens: 10k × 10k × 4 bytes = 400MB por camada.

**FlashAttention:** divide a matriz em blocos que cabem na SRAM (on-chip, rápida). Nunca materializa N×N.
- 2–4× mais rápido, 5–20× menos memória HBM
- FA2: otimizado para A100 (72% de MFU)
- FA3: específico para H100, FP8 nativo, ~2× mais rápido que FA2

```python
# PyTorch 2.0+ — usa FlashAttention automaticamente
import torch.nn.functional as F

output = F.scaled_dot_product_attention(
    query, key, value,
    attn_mask=None,
    dropout_p=0.0,
    is_causal=True
)
```

---

## Trade-offs de Modelos (Q1-Q2 2026)

| Modelo | SWE-Bench | Contexto | Input/1M | Melhor para |
|---|---|---|---|---|
| Claude Opus 4.6 | 80.8% | 200k | $15 | Coding agents, tool use, auditabilidade |
| Gemini 3.1 Pro | 78.8% | 2M | $1.25 | ARC-AGI-2 (77.1%), reasoning novel, multimodal |
| GPT-5.4 | 78.2% | 1M | $2.50 | Generalista, computer use nativo |
| Claude Sonnet 4.5 | 77.2% | 200k (beta 1M) | $3 | Equilíbrio custo/qualidade |
| DeepSeek V4 | ~75% | 128k | $0.28 | Alto volume, 1/50 do preço dos frontier |
| Gemini 3.1 Flash | — | 1M | $0.07 | Long context barato, alta throughput |
| Gemini Flash Lite | — | 1M | $0.025 | Volume extremo, tarefas simples |
| Qwen3.5 27B (self-hosted) | ~72% | 32k | ~$0.30 | Apache 2.0, privacidade, custo fixo |
| Gemma 4 31B (self-hosted) | — | 128k | ~$0.10 | Edge, Apache 2.0, math/coding |

---

## Quando Usar / Quando Evitar

**Modelo frontier (Claude Opus 4.6, Gemini 3.1 Pro, GPT-5.4):**
- ✅ Coding agents, raciocínio multi-passo, tool use crítico
- ✅ Tasks onde erros têm impacto no negócio
- ❌ Alto volume com orçamento limitado — cascade para modelo menor

**Modelo mid-tier (Claude Sonnet 4.5, Gemini Flash):**
- ✅ Equilíbrio qualidade/custo, maioria dos produtos
- ✅ Long context a custo razoável

**Modelo econômico (Gemini Flash Lite, DeepSeek V4):**
- ✅ Classificação, extração, alto volume, RAG retrieval
- ❌ Raciocínio complexo, código difícil

**Self-hosted (Qwen3.5, Gemma 4 via vLLM/SGLang):**
- ✅ LGPD/GDPR estrito, dados sensíveis, Apache 2.0 sem fricção jurídica
- ✅ Volume > ~800/mês em API já compensa em 2026 (vs ~$3k em 2025)
- ❌ MVP, equipe sem capacidade de MLOps

---

## Conceitos Relacionados

[[prompt-engineering]] · [[rag-retrieval]] · [[context-engineering]] · [[fine-tuning]] · [[reasoning-models]]

