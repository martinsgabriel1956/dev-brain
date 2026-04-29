---
date: 2026-04-08
tags: [tech-mentor, ia, reasoning-models, extended-thinking, o1, o3, deepseek-r1, gemini-thinking, thinking-budget, swe-bench, long-context, computer-use, coding-agents]
skill: tech-mentor-ai/references/ai/reasoning-models-2025.md
level: avançado
---

# Reasoning Models & Long Context

## Contexto

Reasoning models "pensam antes de responder" — geram um scratchpad interno (thinking tokens) de raciocínio antes da resposta final. Diferente de adicionar CoT no prompt: o processo acontece dentro do modelo, com tokens ocultos ou visíveis dependendo do provider. A consequência é qualidade superior em problemas de múltiplos passos interdependentes, com custo e latência proporcionalmente maiores.

---

## Como Funciona

```
Modelo padrão:
  input → resposta

Reasoning model:
  input → [thinking tokens: 1k–16k tokens internos] → resposta final

Thinking tokens não aparecem na resposta ao usuário (OpenAI o1/o3).
Claude Extended Thinking expõe o raciocínio como bloco separado.
DeepSeek R1 expõe reasoning_content explicitamente.
```

---

## Claude Extended Thinking

```typescript
const response = await anthropic.messages.create({
  model: "claude-opus-4-6",
  max_tokens: 16000,
  thinking: {
    type: "enabled",
    budget_tokens: 10000   // tokens máximos para o raciocínio interno
  },
  messages: [{ role: "user", content: complexProblem }]
});

// Resposta contém blocos thinking + text separados
for (const block of response.content) {
  if (block.type === "thinking") {
    console.log("Raciocínio:", block.thinking);  // chain-of-thought visível
  }
  if (block.type === "text") {
    console.log("Resposta:", block.text);
  }
}
```

**Heurística de budget_tokens:**

| Tipo de problema | budget_tokens |
|---|---|
| Prova matemática, lógica formal | 8000–16000 |
| Análise de código complexo, arquitetura | 4000–8000 |
| Debugging, trade-offs | 1000–2000 |
| Classificação, extração, FAQ | `thinking: disabled` |

---

## OpenAI o1 / o3

```typescript
const response = await openai.chat.completions.create({
  model: "o3-mini",
  messages: [{ role: "user", content: problem }],
  reasoning_effort: "medium",   // "low" | "medium" | "high"
  max_completion_tokens: 8000
});

// Reasoning tokens consumidos mas NÃO expostos na API
console.log(response.usage.completion_tokens_details.reasoning_tokens);
```

**o1 vs o3-mini:**

| | o1 | o3-mini | o3 |
|---|---|---|---|
| Custo (output) | Alto | ~5–10× menor que o1 | Muito alto |
| Qualidade geral | Alta | Próxima ao o1 em coding/math | Máxima |
| Reasoning visível | Não | Não | Não |
| Melhor para | Balanced | Cost-sensitive reasoning | Máxima qualidade |

---

## DeepSeek R1 — Reasoning Open-Weight

Primeiro modelo de reasoning open-weight competitivo com o1. Custo de API 10–20× menor.

```python
from openai import AsyncOpenAI

# API DeepSeek é compatível com SDK OpenAI
client = AsyncOpenAI(
    api_key=os.environ["DEEPSEEK_API_KEY"],
    base_url="https://api.deepseek.com"
)

response = await client.chat.completions.create(
    model="deepseek-reasoner",
    messages=[{"role": "user", "content": "Prove que sqrt(2) é irracional"}]
)

# Reasoning visível (diferencial vs o1/o3)
thinking = response.choices[0].message.reasoning_content
answer = response.choices[0].message.content
```

**Self-hosted:**
```bash
ollama pull deepseek-r1:70b   # ~40GB VRAM
ollama run deepseek-r1:70b
```

**Por que importa para arquitetos:** performance comparável ao o1 em math/coding, self-hostável (privacidade), reasoning trace visível para debugging e evals.

---

## Gemini 3.1 Pro — Reasoning + Long Context

Líder em ARC-AGI-2 (77.1%) e GPQA Diamond (94.3%). Janela de contexto de 2M tokens com `thinkingBudget` configurável.

```python
import google.generativeai as genai

model = genai.GenerativeModel("gemini-3-1-pro")
response = model.generate_content(
    contents=[{"role": "user", "parts": [{"text": complex_problem}]}],
    generation_config={"thinking_config": {"thinkingBudget": 8000}}
)

for part in response.candidates[0].content.parts:
    if part.thought:
        print("Thinking:", part.text)
    else:
        print("Answer:", part.text)
```

**Diferencial:** 2M context + melhor reasoning novel (ARC-AGI-2) + multimodal vídeo 60fps. Escolha prioritária quando o problema exige raciocínio genuinamente novo, não memorizável.

---

## Prompt Engineering para Reasoning Models

```
❌ Modelo padrão: adicionar CoT manualmente é necessário
   "Pense passo a passo e resolva este problema..."

✅ Reasoning model: instrução direta sem CoT manual
   "Analyze the trade-offs between microservices and monolith for: [context]"

Reasoning models fazem o "pense passo a passo" internamente.
Adicionar CoT explícito pode PREJUDICAR a qualidade — interfere no processo interno.
```

**Anti-padrões específicos:**

| Anti-padrão | Por quê é ruim |
|---|---|
| "Mostre seu trabalho passo a passo" | Thinking já faz isso — duplica raciocínio |
| Few-shot examples extensivos | Prejudica raciocínio autônomo |
| Contexto excessivo e irrelevante | O modelo usa tokens para pensar — lixo entra, lixo sai |
| Pedir JSON estruturado de problema complexo | Mistura raciocínio com formatação — separe as etapas |

---

## Benchmarks e Performance Real

**SWE-Bench Verified** (500 GitHub issues reais, Python) — Q1 2026:

```
Claude Opus 4.6:     80.8% ← líder atual
MiniMax M2.5:        80.2%
Gemini 3.1 Pro:      78.8%
GPT-5.4:             78.2%
Claude Sonnet 4.5:   77.2%
DeepSeek R1:         ~49%   (open-weight)
Engenheiro humano:   ~86%   ← referência

→ Frontier models chegaram perto do humano em tarefas de coding bem definidas.
  A diferença real está em raciocínio de domínio e julgamento de design.
```

**ARC-AGI-2** (raciocínio de senso comum visual — resistente a contamination):
- Gemini 3.1 Pro: 77.1% ← líder (mais que dobro do Gemini 3.0)
- GPT-5.4: ~60%
- Humanos: ~98%

> Um salto de 2× no ARC-AGI-2 é evidência de melhoria arquitetural real — não apenas scale ou mais dados. É o benchmark mais confiável para raciocínio genuíno em 2026.

---

## METR Task Length Metric — Termômetro de Maturidade de Agentes

A organização METR mede quantas horas de tarefa humana um agente resolve com 50% de success rate:

```
2024 Q1: ~15 minutos
2024 Q3: ~30 minutos  (dobrou em ~7 meses)
2025 Q4: ~5 horas     (Claude Opus 4.5)
2026:    projeção crescente — aceleração contínua

Implicações práticas:
  Tasks < 1 hora  → agente já resolve com confiabilidade útil
  Tasks 1–5 horas → zona de maturação, requer HITL e checkpoints
  Tasks > 5 horas → ainda experimental, supervisão próxima necessária
```

---

## Quando Usar vs Quando Evitar

**Use reasoning models quando:**
- Problemas de múltiplos passos interdependentes (matemática, lógica, planejamento)
- Análise de trade-offs com muitas variáveis
- Debugging de sistemas complexos onde "primeiro instinto" costuma errar
- Code review / arquitetura onde encadeamento de inferências importa

**NÃO use reasoning models quando:**

| Caso | Por quê não | Alternativa |
|---|---|---|
| Extração JSON estruturada | Overhead desnecessário | Structured outputs + modelo barato |
| RAG simples | Raciocínio não melhora retrieval | Haiku + bom chunking |
| Streaming real-time | Thinking tokens adicionam 5–10s de TTFB | Modelo padrão |
| FAQ / respostas curtas | P95 latência > 5s inaceitável em UI | Haiku ou Flash |
| > 100 req/s | Custo 5–10× destruiria margem | Routing por complexidade |

**Regra:** use reasoning apenas quando o problema requer múltiplos passos de dedução onde a cadeia de raciocínio muda a resposta. Se um modelo padrão acerta 90% das vezes, reasoning provavelmente não vale o custo.

---

## Long Context — Estratégias para 200K–1M Tokens

### Lost in the Middle

LLMs tendem a ignorar informação no meio de contextos longos:

```
Atenção típica em contexto longo:
  [INÍCIO: alta atenção] [MEIO: atenção degradada] [FIM: alta atenção]

Estratégia: coloque informação crítica no início E no fim.
Repetir a tarefa ao final do contexto é eficaz.
```

### Contexto Longo vs RAG

| | Contexto Longo | RAG |
|---|---|---|
| Volume | 100s de páginas | Milhões de docs |
| Raciocínio cross-doc | Nativo | Difícil |
| Latência | Alta (processa tudo) | Baixa |
| Custo | Alto (tokens) | Baixo |
| Consistência | Alta | Depende do retrieval |

**Use contexto longo quando:** análise holística de codebase, docs que precisam ser lidos em conjunto, raciocínio que requer múltiplas partes simultaneamente.

**Use RAG quando:** volume impraticável, latência crítica, base de conhecimento muda frequentemente.

### Estruturação de Documentos para Contexto Longo

```
1. Instrução/tarefa crítica NO INÍCIO
2. Headers claros (## Section) para navegação do modelo
3. Delimitadores explícitos entre documentos:

<document id="1" title="Architecture Spec">
...conteúdo...
</document>

<document id="2" title="Current Implementation">
...conteúdo...
</document>

<task>
Identifique discrepâncias entre a spec e a implementação atual.
</task>

4. Repita a tarefa ao FINAL (mitigação de lost-in-the-middle)
```

### Prompt Cache para Contexto Longo

```typescript
// Anthropic: cache_control para reutilizar prefixo caro
const response = await anthropic.messages.create({
  model: "claude-opus-4-6",
  max_tokens: 1024,
  system: [
    {
      type: "text",
      text: "You are an expert analyst.",
      cache_control: { type: "ephemeral" }
    },
    {
      type: "text",
      text: largeDocument,   // 100K tokens — cacheado após primeiro call
      cache_control: { type: "ephemeral" }
    }
  ],
  messages: [{ role: "user", content: question }]
});

// Primeiro call: paga tokens completos
// Calls seguintes (mesma hora): 90% desconto no prefixo cacheado
// Análise de codebase com múltiplas perguntas → economia de ~80%
```

---

## Computer Use — Agentes que Controlam a GUI

Capacidade do modelo de ver a tela, clicar, digitar — automação de qualquer interface sem API.

```python
import anthropic
import base64
from PIL import ImageGrab
import io

client = anthropic.Anthropic()

def take_screenshot() -> str:
    img = ImageGrab.grab()
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    return base64.b64encode(buf.getvalue()).decode()

def computer_use_loop(task: str) -> str:
    messages = [{"role": "user", "content": task}]

    while True:
        response = client.beta.messages.create(
            model="claude-opus-4-6",
            max_tokens=4096,
            tools=[{
                "type": "computer_20241022",
                "name": "computer",
                "display_width_px": 1920,
                "display_height_px": 1080,
                "display_number": 1
            }],
            messages=messages,
            betas=["computer-use-2024-10-22"]
        )

        has_tool_use = any(b.type == "tool_use" for b in response.content)
        if not has_tool_use:
            return next(b.text for b in response.content if b.type == "text")

        tool_results = []
        for block in response.content:
            if block.type == "tool_use" and block.name == "computer":
                execute_computer_action(block.input)
                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": [{
                        "type": "image",
                        "source": {"type": "base64", "media_type": "image/png", "data": take_screenshot()}
                    }]
                })

        messages.append({"role": "assistant", "content": response.content})
        messages.append({"role": "user", "content": tool_results})
```

**Casos de uso:** automação de SaaS sem API, portais legados, testes E2E sem seletores frágeis.

**Riscos:** Computer Use tem acesso total ao sistema. Obrigatório: VM isolada, sem credenciais de produção, HITL para ações destrutivas, timeout agressivo.

---

## Coding Agents — Padrões de Implementação

```python
class CodingAgent:
    def __init__(self, repo_path: str):
        self.repo = RepoContext(repo_path)

    def solve_issue(self, issue: str) -> str:
        # 1. Encontra arquivos relevantes via embedding search
        relevant_files = self.repo.semantic_search(issue, top_k=10)
        type_context = self.repo.get_type_definitions(relevant_files)

        # 2. Planeja mudanças necessárias
        plan = reasoning_llm(
            system="You are a senior developer. Plan the changes needed.",
            context=[issue, relevant_files, type_context]
        )

        # 3. Executa cada passo do plano
        for step in plan.steps:
            file_content = self.repo.read_file(step.file)
            patch = llm(
                system="Apply this change to the file.",
                context=[step.description, file_content]
            )
            self.repo.apply_patch(step.file, patch)

        # 4. Valida — itera se falhar
        test_result = self.repo.run_tests()
        if not test_result.passed:
            return self.debug_and_fix(test_result)

        return "Issue resolved"


# Guardrails para coding agents
SAFE_OPERATIONS = {"read_file", "list_files", "search_code", "run_tests", "run_linter"}
REQUIRES_APPROVAL = {"write_file", "delete_file", "execute_command", "git_commit", "create_pr"}

async def validate_tool_call(tool: str, args: dict, approved: bool = False) -> bool:
    if tool in SAFE_OPERATIONS:
        return True
    if tool in REQUIRES_APPROVAL:
        if not approved:
            raise RequiresApprovalError(f"Tool '{tool}' requires human approval")
        return True
    raise UnknownToolError(tool)
```

---

## Trade-offs — Escolhendo o Modelo Certo

| Dimensão | Modelo padrão | Reasoning model |
|---|---|---|
| Latência (TTFT) | < 500ms | 5–60s |
| Custo | Baseline | 5–20× maior |
| Qualidade em tasks simples | Igual | Igual ou pior |
| Qualidade em raciocínio complexo | Boa | Superior |
| Streaming | Fluido | Atraso no thinking |
| Interpretabilidade | Baixa | Alta (thinking visível) |

---

## Conceitos Relacionados

[[prompt-engineering]] · [[context-engineering]] · [[agentes-core]] · [[evals-sistematicas]] · [[ai-gateway-token-economics]]

---
*Fonte: tech-mentor skill · tech-mentor-ai · 2026-04-08*
