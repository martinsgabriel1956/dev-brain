---
date: 2026-04-08
tags: [tech-mentor, ia, fine-tuning, lora, qlora, peft, instruction-tuning, catastrophic-forgetting, rlhf, dpo, grpo, synthetic-data, knowledge-distillation, raft]
skill: tech-mentor-ai/references/ai/finetuning.md
level: avançado
---

# Fine-tuning & Especialização

## Contexto

Fine-tuning é quando prompt engineering e RAG não são suficientes para estilo, formato ou comportamento consistente. Não substitui RAG para conhecimento atualizado — fine-tuning não "memoriza" fatos de forma confiável. Serve para ensinar ao modelo *como* se comportar, não *o que saber*.

---

## Quando Usar Fine-tuning

```
Precisa de conhecimento atualizado?                    → RAG (não fine-tuning)
Precisa de formato específico que few-shot não resolve? → Fine-tuning
Precisa de comportamento/persona consistente em escala? → Fine-tuning
Prompt engineering + few-shot já funciona bem?         → Ficou com Prompt Engineering ✓
Precisa de conhecimento E comportamento?               → RAG + Fine-tuning
```

**Fine-tuning RESOLVE:**
- ✅ Formato de output muito específico e consistente (JSON com schema fixo, relatórios no padrão da empresa)
- ✅ Reduzir tokens de instrução — comportamento frequente vira "instinto" do modelo
- ✅ Vocabulário e estilo específico do domínio
- ✅ Instruction-following mais preciso quando o modelo base ignora constraints

**Fine-tuning NÃO resolve:**
- ❌ Fatos atualizados — modelo não memoriza fatos de forma confiável
- ❌ Base de conhecimento grande — use RAG
- ❌ Raciocínio em novos domínios — raciocina com capacidades do treino base

---

## Por que Full Fine-tuning é Inviável

Treinar todos os parâmetros requer VRAM equivalente a ~4× o tamanho do modelo em float32. Llama 3 8B completo = >80GB de VRAM para treinar. Impraticável fora de data centers.

**Solução:** PEFT (Parameter-Efficient Fine-Tuning) — treina <1% dos parâmetros e atinge 90%+ da qualidade do fine-tuning completo.

---

## LoRA — Low-Rank Adaptation

Em vez de modificar os pesos originais W (matriz grande), aprende duas matrizes pequenas A e B tal que ΔW = A × B. Com rank r, reduz parâmetros de d×d para 2×d×r onde r << d.

```
W_original (frozen)    → não muda durante treino
      +
A (d × r) × B (r × d)  → só esses ~0.1% dos parâmetros são treinados
```

```python
from peft import LoraConfig, get_peft_model, TaskType
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model = AutoModelForCausalLM.from_pretrained(
    "meta-llama/Llama-3.1-8B-Instruct",
    torch_dtype=torch.float16,
    device_map="auto"
)

lora_config = LoraConfig(
    task_type=TaskType.CAUSAL_LM,
    r=16,               # rank — controla capacidade de adaptação
    lora_alpha=32,      # escala: geralmente 2× o rank
    lora_dropout=0.1,   # regularização
    target_modules=[
        "q_proj", "k_proj", "v_proj", "o_proj",   # attention
        "gate_proj", "up_proj", "down_proj"         # MLP
    ],
    bias="none"
)

peft_model = get_peft_model(model, lora_config)
peft_model.print_trainable_parameters()
# trainable params: 6,815,744 || all params: 8,036,352,000 || trainable%: 0.085
```

**rank r:** r=4 conservador, r=16 padrão, r=64 agressivo. Começa com r=16.

---

## QLoRA — Fine-tuning em GPU Consumer

QLoRA = LoRA + quantização 4-bit do modelo base. Permite treinar Llama 3 8B em uma GPU de 24GB (RTX 3090/4090).

```python
from transformers import BitsAndBytesConfig
from peft import prepare_model_for_kbit_training

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",            # NF4: melhor qualidade que int4 padrão
    bnb_4bit_compute_dtype=torch.bfloat16,
    bnb_4bit_use_double_quant=True         # dupla quantização: economiza mais memória
)

model = AutoModelForCausalLM.from_pretrained(
    "meta-llama/Llama-3.1-8B-Instruct",
    quantization_config=bnb_config,
    device_map="auto"
)

model = prepare_model_for_kbit_training(model)
peft_model = get_peft_model(model, lora_config)
```

**Requisitos de memória (treino, batch size 1):**

| Modelo | Full FT | LoRA (fp16) | QLoRA (4-bit) |
|---|---|---|---|
| 7–8B | >80GB | ~30GB | ~10GB |
| 13B | >120GB | ~50GB | ~16GB |
| 70B | >640GB | ~200GB | ~48GB |

---

## Instruction Tuning — Dataset

Fine-tuning de qualidade exige dataset de qualidade. Quantidade importa menos que diversidade e correção.

**Formato Alpaca-style:**
```jsonl
{"instruction": "Classifique o sentimento.", "input": "A bateria dura muito pouco, decepcionante.", "output": "NEGATIVO"}
{"instruction": "Classifique o sentimento.", "input": "Superou minhas expectativas!", "output": "POSITIVO"}
```

**Formato conversacional ChatML (para modelos de chat):**
```jsonl
{"messages": [
  {"role": "system", "content": "Você extrai entidades de texto jurídico em JSON."},
  {"role": "user", "content": "Contrato entre ACME LTDA (CNPJ 12.345.678/0001-00) e João Silva"},
  {"role": "assistant", "content": "{\"partes\": [{\"tipo\": \"empresa\", \"nome\": \"ACME LTDA\"}]}"}
]}
```

**Tamanho mínimo por objetivo:**

| Objetivo | Exemplos mínimos | Sweet spot |
|---|---|---|
| Formato de saída específico | 100 | 500–1k |
| Novo domínio / vocabulário | 500 | 2k–5k |
| Estilo de escrita | 200 | 1k–3k |
| Instruction-following geral | 1k | 5k–50k |

---

## Synthetic Data Generation

Quando dados reais são escassos, use LLM para gerar exemplos de treino. Valide sempre.

```python
import anthropic
import json

client = anthropic.Anthropic()

async def generate_training_examples(
    task_description: str,
    few_shot_examples: list[dict],
    n_examples = 100
) -> list[dict]:
    prompt = f"""Generate {n_examples} diverse training examples for this task:
{task_description}

Format: JSON array of {{"instruction": "...", "input": "...", "output": "..."}}
Each example should have different vocabulary, length, and complexity.
Ensure outputs are always correct and consistent.

Real examples to match the style:
{json.dumps(few_shot_examples, indent=2)}

Generate only the JSON array, no explanation."""

    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=8192,
        messages=[{"role": "user", "content": prompt}]
    )

    return json.loads(message.content[0].text)

# IMPORTANTE: validar manualmente ~10% dos exemplos gerados
# LLMs cometem erros — dados ruins degradam o fine-tuning
```

---

## Treino com TRL

```python
from trl import SFTTrainer, SFTConfig
from datasets import load_dataset

dataset = load_dataset("json", data_files="training_data.jsonl", split="train")

training_config = SFTConfig(
    output_dir="./output",
    num_train_epochs=3,
    per_device_train_batch_size=2,
    gradient_accumulation_steps=4,   # batch efetivo = 2 × 4 = 8
    learning_rate=2e-4,
    warmup_ratio=0.03,
    lr_scheduler_type="cosine",
    save_strategy="epoch",
    fp16=True,
    max_seq_length=2048,
    packing=True,   # empacota múltiplos exemplos curtos — aumenta eficiência
)

trainer = SFTTrainer(
    model=peft_model,
    args=training_config,
    train_dataset=dataset,
    tokenizer=tokenizer
)

trainer.train()

# Salvar apenas os pesos LoRA (alguns MB — não o modelo base inteiro)
peft_model.save_pretrained("./lora-adapters")
```

**Inferência com adapter:**
```python
from peft import PeftModel

base_model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16)
model = PeftModel.from_pretrained(base_model, "./lora-adapters")

# Merge para inferência mais rápida (remove overhead PEFT)
merged = model.merge_and_unload()
merged.save_pretrained("./merged-model")
# vllm serve ./merged-model --tensor-parallel-size 2
```

---

## Catastrophic Forgetting

O modelo esquece capacidades gerais ao aprender o novo domínio. Mitigações:

- **LoRA** já mitiga naturalmente — pesos base ficam congelados
- **Data mixing:** incluir ~10–20% de dados gerais no dataset de fine-tuning
- **Model merging:** combinar o modelo fine-tunado com o base via SLERP/TIES
- **EWC (Elastic Weight Consolidation):** penaliza mudanças em parâmetros críticos para capacidades gerais

---

## RLHF, DPO, GRPO — Alinhamento por Preferências

### RLHF (Reinforcement Learning from Human Feedback)

Como modelos como GPT-4 e Claude são alinhados. Pipeline em 3 etapas:

```
1. SFT (Supervised Fine-Tuning)
   Base model → fine-tune em exemplos de alta qualidade

2. Reward Model Training
   Humanos rankeiam pares de respostas (A vs B)
   Reward model aprende a prever preferência humana

3. PPO (Proximal Policy Optimization)
   LLM gera respostas → Reward model pontua
   PPO atualiza LLM para maximizar reward
   KL divergence penalty evita desvio excessivo do SFT
```

### DPO — Direct Preference Optimization

Alternativa ao PPO mais simples — sem reward model separado. Treina diretamente em pares `(chosen, rejected)`.

```python
from trl import DPOTrainer, DPOConfig

trainer = DPOTrainer(
    model=model,
    ref_model=ref_model,  # modelo de referência (não atualizado)
    args=DPOConfig(
        beta=0.1,          # força da penalidade KL
        learning_rate=1e-6,
        per_device_train_batch_size=4,
        max_length=1024,
        max_prompt_length=512
    ),
    train_dataset=dataset["train"],  # {prompt, chosen, rejected}
    tokenizer=tokenizer
)
trainer.train()
```

**DPO vs PPO:**

| | PPO | DPO |
|---|---|---|
| Reward model separado | Sim | Não |
| Complexidade | Alta | Baixa |
| Estabilidade | Menor (RL instável) | Maior |
| Uso em produção | GPT-4, Claude | Llama 3, Mistral instruct |

**GRPO (Group Relative Policy Optimization)** — usado no DeepSeek R1: elimina o reward model, usa comparação relativa de múltiplos outputs gerados pelo próprio modelo. Mais eficiente que PPO.

---

## Knowledge Distillation — Teacher-Student

Usa um modelo grande (teacher) para gerar dados de treino para um modelo menor (student). O student aprende não só a resposta certa, mas o raciocínio do teacher.

```python
# 1. Teacher (GPT-4o ou Claude Sonnet) gera respostas com chain-of-thought
teacher_outputs = await generate_with_cot(
    teacher_llm, training_prompts,
    system="Think step by step and show your reasoning before the answer."
)

# 2. Student (Llama 3 8B) treina nessas respostas
# O student aprende o raciocínio, não só o output
dataset = [
    {
        "instruction": prompt,
        "output": f"{cot_reasoning}\n\n{final_answer}"  # raciocínio + resposta
    }
    for prompt, (cot_reasoning, final_answer) in zip(training_prompts, teacher_outputs)
]
```

**Rational Distillation:** distila o raciocínio do teacher, não só o output final. DeepSeek R1 e Qwen foram treinados com essa técnica via GPT-4.

---

## RAFT — Retrieval-Augmented Fine-Tuning

Combina RAG + fine-tuning: treina o modelo para responder usando documentos recuperados, distinguindo documentos relevantes de "distractors".

```python
# Dataset RAFT: para cada pergunta, inclui documentos oracle + distractors
raft_dataset = [{
    "instruction": "Answer based on the documents. Cite the relevant passage.",
    "input": f"""Question: {question}

Documents:
[D1] {oracle_doc}       ← documento que contém a resposta
[D2] {distractor_1}     ← documento irrelevante (model deve ignorar)
[D3] {distractor_2}     ← documento irrelevante""",
    "output": f"Based on [D1]: {answer}. The relevant passage is: '{key_quote}'"
}]
```

**Por que funciona:** o modelo aprende a ler contexto RAG, identificar o documento relevante e ignorar noise — habilidade que modelos base não têm por padrão.

---

## Model Merging — SLERP, TIES, DARE

Combinar pesos de modelos fine-tunados sem retreinar.

```python
from mergekit import merge, MergeConfiguration

# SLERP — interpolação esférica entre dois modelos
config_slerp = MergeConfiguration(
    merge_method="slerp",
    models=[
        {"model": "base-model", "parameters": {"t": 0}},
        {"model": "finetuned-domain", "parameters": {"t": 0.5}}
    ],
    base_model="base-model",
    dtype="bfloat16"
)

# TIES — resolve conflitos entre múltiplos modelos fine-tunados
config_ties = MergeConfiguration(
    merge_method="ties",
    models=[
        {"model": "finetuned-code",      "parameters": {"density": 0.7, "weight": 1.0}},
        {"model": "finetuned-math",      "parameters": {"density": 0.7, "weight": 1.0}},
        {"model": "finetuned-reasoning", "parameters": {"density": 0.7, "weight": 1.0}}
    ],
    base_model="base-model"
)

merge(config_ties, out_path="merged-model/")
```

**Quando usar:** combinar especialistas sem retreinar; evitar catastrophic forgetting; criar modelos com capacidades complementares.

---

## Custo e ROI

| Abordagem | Setup | Por 1k queries |
|---|---|---|
| Prompt engineering | $0 | $0.05–0.50 (tokens extras) |
| RAG (pgvector) | $50–200 (infra) | $0.02–0.10 |
| Fine-tuning OpenAI | $10–500 (treino) | $0.01–0.05 (modelo menor) |
| QLoRA self-hosted | $50–200 (GPU time) | $0.001 (infra própria) |

**Break-even:** fine-tuning começa a valer quando volume > ~100k queries/mês com prompts longos. ROI adicional: latência menor, privacidade, qualidade superior em tarefas narrow.

---

## Quando Usar / Quando Evitar

**Use fine-tuning quando:** formato de output muito específico que few-shot não resolve em escala, redução de latência via modelo menor, restrições de privacidade (self-hosted), domínio muito específico onde modelo base falha.

**Não use fine-tuning quando:** precisa de conhecimento atualizado (→ RAG), está na fase de prototipagem (→ prompt engineering primeiro), equipe não tem experiência com treino de modelos.

**RAFT quando:** já usa RAG e quer que o modelo seja melhor em usar o contexto recuperado — é o melhor dos dois mundos.

---

## Conceitos Relacionados

[[evals-sistematicas]] · [[rag-retrieval]] · [[prompt-engineering]] · [[reasoning-models]] · [[llmops-observabilidade]]

---
*Fonte: tech-mentor skill · tech-mentor-ai · 2026-04-08*
