---
date: 2026-04-07
tags: [tech-mentor, ia, structured-outputs, function-calling, tool-use, pydantic, zod, json-schema]
skill: tech-mentor-ai/references/ai/structured-outputs-function-calling.md
level: intermediário
---

# Structured Outputs & Function Calling

## Contexto

Sem outputs estruturados confiáveis, seu pipeline vai quebrar em produção. LLMs retornam texto livre — um mesmo prompt pode gerar `"Nome: João"`, `{"nome": "João"}` ou `"O nome é João"` em requests diferentes. Structured outputs e function calling resolvem isso com garantia de schema.

---

## Como Funciona

### O problema sem estrutura

```python
response = llm.generate("Extraia nome e email do texto: João Silva, joao@email.com")
# Pode retornar qualquer um dos formatos abaixo:
# "Nome: João Silva, Email: joao@email.com"
# '{"nome": "João Silva", "email": "joao@email.com"}'
# "O nome é João Silva e o email é joao@email.com"
```

Sem garantia de schema, o parsing falha silenciosamente em produção.

---

### JSON Mode vs Structured Outputs

**JSON Mode** — garante JSON válido, mas **não garante o schema**:
```python
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Extraia nome e email de: João Silva, joao@email.com"}],
    response_format={"type": "json_object"},
)
# Retorna JSON válido, mas pode ter campos diferentes do esperado
```

**Structured Outputs (OpenAI)** — garante JSON válido **e o schema exato**:
```python
from pydantic import BaseModel
from openai import OpenAI

client = OpenAI()

class ContactInfo(BaseModel):
    name: str
    email: str
    phone: str | None = None

completion = client.beta.chat.completions.parse(
    model="gpt-4o-2024-08-06",  # requer modelo compatível
    messages=[{"role": "user", "content": "Extraia: João Silva, joao@email.com, (11) 99999-9999"}],
    response_format=ContactInfo,
)

contact = completion.choices[0].message.parsed  # typed como ContactInfo
print(contact.name)   # "João Silva"
print(contact.email)  # "joao@email.com"
# Nunca falha de parsing — OpenAI garante o schema
```

---

### Claude — Tool Use como extração estruturada

Para Claude, a abordagem mais confiável é usar `tool_use` em vez de pedir JSON no prompt. Definir uma tool com schema e forçar seu uso (`tool_choice: {type: "tool", name: "..."}`) é mais robusto que instrução no system prompt.

```typescript
import Anthropic from "@anthropic-ai/sdk";
import { z } from "zod";

const InvoiceSchema = z.object({
  vendor_name: z.string(),
  total_amount: z.number().positive(),
  currency: z.enum(["BRL", "USD", "EUR"]),
  line_items: z.array(z.object({
    description: z.string(),
    quantity: z.number(),
    unit_price: z.number()
  })),
  due_date: z.string().regex(/^\d{4}-\d{2}-\d{2}$/)
});

type Invoice = z.infer<typeof InvoiceSchema>;

async function extractInvoice(imageBase64: string): Promise<Invoice> {
  const client = new Anthropic();

  const response = await client.messages.create({
    model: "claude-sonnet-4-20250514",
    max_tokens: 1000,
    tools: [{
      name: "extract_invoice",
      description: "Extract structured data from an invoice",
      input_schema: {
        type: "object",
        properties: {
          vendor_name: { type: "string" },
          total_amount: { type: "number" },
          currency: { type: "string", enum: ["BRL", "USD", "EUR"] },
          line_items: {
            type: "array",
            items: {
              type: "object",
              properties: {
                description: { type: "string" },
                quantity: { type: "number" },
                unit_price: { type: "number" }
              },
              required: ["description", "quantity", "unit_price"]
            }
          },
          due_date: { type: "string", description: "ISO 8601: YYYY-MM-DD" }
        },
        required: ["vendor_name", "total_amount", "currency", "line_items"]
      }
    }],
    tool_choice: { type: "tool", name: "extract_invoice" },  // força a tool — sem ambiguidade
    messages: [{
      role: "user",
      content: [
        { type: "image", source: { type: "base64", media_type: "image/jpeg", data: imageBase64 } },
        { type: "text", text: "Extract all invoice data from this image." }
      ]
    }]
  });

  const toolUse = response.content.find(b => b.type === "tool_use");
  if (!toolUse || toolUse.type !== "tool_use") throw new Error("No tool use in response");

  // Validação com Zod — lança se o LLM retornou algo fora do schema
  return InvoiceSchema.parse(toolUse.input);
}
```

---

## Function Calling — Tools para Agentes

### O conceito

O LLM decide **quando** e **com quais argumentos** chamar uma função. Você executa a função e devolve o resultado para o LLM continuar o raciocínio.

```
User: "Qual a previsão do tempo em São Paulo amanhã?"
  ↓
LLM: "Preciso chamar get_weather(location='São Paulo', date='tomorrow')"
  ↓
App: executa get_weather() → {"temp": 28, "condition": "sunny"}
  ↓
LLM: "A previsão para São Paulo amanhã é 28°C e ensolarado."
```

### Loop de agente — OpenAI

```python
import json
from openai import OpenAI

client = OpenAI()

tools = [{
    "type": "function",
    "function": {
        "name": "get_order_status",
        "description": "Get the current status and details of a customer order",
        "parameters": {
            "type": "object",
            "properties": {
                "order_id": {"type": "string", "description": "The order ID to look up"}
            },
            "required": ["order_id"],
            "additionalProperties": False  # strict mode — sem campos extras
        },
        "strict": True
    }
}]

messages = [{"role": "user", "content": "Qual o status do pedido #12345?"}]

while True:
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        tools=tools,
        tool_choice="auto"
    )

    choice = response.choices[0]
    messages.append(choice.message)

    if choice.finish_reason == "stop":
        print(choice.message.content)
        break

    if choice.finish_reason == "tool_calls":
        for tool_call in choice.message.tool_calls:
            args = json.loads(tool_call.function.arguments)
            result = get_order_status(args["order_id"])

            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": json.dumps(result)
            })
```

### Loop de agente — Claude

```python
import anthropic
import json

client = anthropic.Anthropic()

tools = [{
    "name": "search_products",
    "description": "Search for products in the catalog by name or category",
    "input_schema": {
        "type": "object",
        "properties": {
            "query": {"type": "string", "description": "Search query"},
            "category": {"type": "string", "enum": ["electronics", "clothing", "food"]},
            "max_results": {"type": "integer", "default": 5}
        },
        "required": ["query"]
    }
}]

messages = [{"role": "user", "content": "Mostre notebooks disponíveis"}]

while True:
    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        tools=tools,
        messages=messages
    )

    if response.stop_reason == "end_turn":
        for block in response.content:
            if hasattr(block, "text"):
                print(block.text)
        break

    if response.stop_reason == "tool_use":
        messages.append({"role": "assistant", "content": response.content})

        tool_results = []
        for block in response.content:
            if block.type == "tool_use":
                result = search_products(**block.input)
                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": json.dumps(result)
                })

        messages.append({"role": "user", "content": tool_results})
```

---

## Padrões de Produção

### Retry com validação de schema

Quando structured outputs não estão disponíveis (modelos menores, providers sem suporte), use retry com o erro como contexto:

```python
from pydantic import BaseModel, ValidationError
import json

def call_with_structured_output(prompt: str, schema: type[BaseModel], max_retries = 3):
    for attempt in range(max_retries):
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": f"Return valid JSON matching: {schema.model_json_schema()}"},
                {"role": "user", "content": prompt}
            ],
            response_format={"type": "json_object"}
        )

        try:
            data = json.loads(response.choices[0].message.content)
            return schema(**data)
        except (json.JSONDecodeError, ValidationError) as e:
            if attempt == max_retries - 1:
                raise
            # Adiciona o erro ao contexto — LLM tenta corrigir
            prompt = f"{prompt}\n\nPrevious attempt failed: {e}\nPlease fix and try again."
```

### Parallel Tool Calls

GPT-4o pode retornar múltiplos tool_calls no mesmo response — execute em paralelo:

```typescript
import { Promise } from "bluebird";

async function executeParallelTools(toolCalls: ToolCall[]) {
  const results = await Promise.all(
    toolCalls.map(async tc => {
      const fn = toolRegistry[tc.function.name];
      const args = JSON.parse(tc.function.arguments);
      const result = await fn(args);
      return { tool_call_id: tc.id, content: JSON.stringify(result) };
    })
  );
  return results;
}
```

### Idempotência das tools

Tools chamadas por agentes devem ser idempotentes — o agente pode chamá-las múltiplas vezes com os mesmos args.

```typescript
// ✅ Idempotente — GET é sempre seguro
async function getOrderStatus(orderId: string) {
  return await db.orders.findUnique({ where: { id: orderId } });
}

// ⚠️ Não idempotente — use idempotency key
async function chargeCard(amount: number, idempotencyKey: string) {
  return await stripe.charges.create(
    { amount, currency: "brl" },
    { idempotencyKey }  // Stripe não cobra duas vezes com a mesma key
  );
}
```

---

## Decision Tree

```
Extração simples, modelo moderno (OpenAI)   → Structured Outputs (parse) com Pydantic
Extração com Claude                          → Tool use com tool_choice forçado + Zod/Pydantic
Schema crítico, múltiplos providers          → Instructor library (abstração sobre qualquer LLM)
Múltiplas ações sequenciais                 → Function calling com loop de agente
Alta throughput, latência crítica            → Constrained decoding (Outlines)
Modelo menor sem structured outputs         → JSON mode + retry com validação
```

---

## Erros Comuns em Produção

| Problema | Causa | Solução |
|---|---|---|
| LLM inventa campos inexistentes | Schema permissivo | `additionalProperties: false` + `strict: true` |
| LLM chama tool que não existe | Nome de tool errado no response | Valide `fn_name` antes de executar |
| Loop infinito de tool calls | Sem limite de iterações | `max_turns=10`, lance erro ao atingir |
| Timeout na tool | Função externa lenta | Timeout por tool + fallback sem tools |
| JSON inválido em produção | Modelo antigo ou prompt ambíguo | Use Structured Outputs (OpenAI) ou tool_use nativo (Claude) |
| Double charge em pagamento | Tool não idempotente | Idempotency key em toda operação com efeito colateral |

---

## Trade-offs

| Abordagem | Garantia de schema | Custo | Latência | Flexibilidade |
|---|---|---|---|---|
| JSON mode | JSON válido, schema variável | 1× | 1× | Alta |
| Structured Outputs (OpenAI) | Schema garantido | 1× | 1× | Limitado (gpt-4o+) |
| Tool use forçado (Claude) | Schema garantido | 1× | 1× | Qualquer tool |
| Instructor | Schema via retry | 1.1–1.3× | 1.1× | Qualquer LLM |
| Constrained decoding (Outlines) | Schema garantido | Infra própria | Muito baixa | Self-hosted |

---

## Quando Usar / Quando Evitar

**Structured Outputs sempre que:** o output vai alimentar código que processa campos específicos — nunca confie em parsing ad-hoc de texto livre em produção.

**Function calling quando:** o agente precisa executar ações no mundo real (buscar dados, escrever, chamar APIs). Não use para extração pura — Structured Outputs são mais simples.

**Constrained decoding quando:** alta throughput, latência crítica, self-hosted. O modelo fisicamente não pode gerar tokens fora do schema.

**Retry com validação quando:** provider sem suporte a structured outputs, ou modelo pequeno/local que não suporta o modo structured.

---

## Conceitos Relacionados

[[prompt-engineering]] · [[agentes-core]] · [[rag-retrieval]] · [[context-engineering]]