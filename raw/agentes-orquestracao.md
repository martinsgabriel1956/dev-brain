---
date: 2026-04-08
tags: [tech-mentor, ia, agentes, multi-agente, supervisor-pattern, handoff, langgraph, crewai, swarm, planner-executor-critic, checkpointing, error-boundaries, durable-execution]
skill: tech-mentor-ai/references/ai/agents-orchestration.md
level: avançado
---

# Orquestração Multi-agente

## Contexto

Tarefas complexas precisam de múltiplos agentes com papéis diferentes — um único agente acumulando todas as responsabilidades vira um God Agent: contexto gigante, sem especialização, difícil de testar e debugar. Orquestração distribui a complexidade.

---

## Como Funciona

### Quando multi-agente faz sentido

```
Agente único resolve quando:
  - Task de domínio único
  - Contexto cabe no context window
  - Steps são sequenciais e simples

Multi-agente resolve quando:
  - Task requer especialização (pesquisa, escrita, revisão são habilidades distintas)
  - Paralelismo real — sub-tasks independentes rodando ao mesmo tempo
  - Contexto de um agente único cresceria além do limite
  - Diferentes partes da task precisam de modelos diferentes
```

---

## Padrões de Arquitetura

### Supervisor Pattern — orquestrador delegando para sub-agentes

O agente orquestrador recebe a task, planeja e delega para especialistas. Sub-agentes não se comunicam diretamente.

```
User → Orchestrator
           ├→ Research Agent  → resultado
           ├→ Analysis Agent  → resultado
           └→ Writer Agent    → resultado final
```

```typescript
// Orchestrator tem tools que são os sub-agentes
const orchestratorTools = [
  tool({
    name: "delegate_research",
    description: "Delegate research tasks. Use when information needs to be gathered from external sources.",
    parameters: z.object({ task: z.string(), context: z.string() }),
    execute: async ({ task, context }) => researchAgent.run(task, context)
  }),
  tool({
    name: "delegate_analysis",
    description: "Delegate analysis tasks. Use when gathered data needs to be synthesized.",
    parameters: z.object({ data: z.string(), question: z.string() }),
    execute: async ({ data, question }) => analysisAgent.run(data, question)
  }),
  tool({
    name: "delegate_writing",
    description: "Delegate writing tasks. Use to produce final formatted output.",
    parameters: z.object({ content: z.string(), format: z.string() }),
    execute: async ({ content, format }) => writerAgent.run(content, format)
  })
];
```

**Vantagem:** controle centralizado, rastreabilidade. O orchestrator é o single point of truth sobre o estado da task.

---

### Handoff Pattern — transferência de contexto entre agentes

Um agente completa sua parte e passa o contexto adiante para o próximo. Útil para pipelines onde cada etapa produz input para a próxima.

```
Agent A → [output + context] → Agent B → [output + context] → Agent C → Resposta
```

```typescript
type HandoffContext = {
  taskId: string;
  originalTask: string;
  completedSteps: Array<{ agent: string; output: unknown; timestamp: Date }>;
  nextStep: string;
};

async function handoffPipeline(task: string): Promise<string> {
  const context: HandoffContext = {
    taskId: crypto.randomUUID(),
    originalTask: task,
    completedSteps: [],
    nextStep: "research"
  };

  // Pesquisa
  const researchOutput = await researchAgent.run(task);
  context.completedSteps.push({ agent: "research", output: researchOutput, timestamp: new Date() });
  context.nextStep = "analysis";

  // Análise com contexto acumulado
  const analysisOutput = await analysisAgent.run({ ...context, input: researchOutput });
  context.completedSteps.push({ agent: "analysis", output: analysisOutput, timestamp: new Date() });
  context.nextStep = "writing";

  // Escrita com contexto completo
  return await writerAgent.run(context);
}
```

---

### Swarm Pattern — agentes paralelos com resultado agregado

Sub-agentes rodam em paralelo em partes independentes da task. Resultado é agregado ao final.

```
                 ┌→ Agent A (parte 1) ─┐
User → Router   ├→ Agent B (parte 2) ──→ Aggregator → Resposta
                 └→ Agent C (parte 3) ─┘
```

```typescript
async function swarmSearch(query: string): Promise<string> {
  // Divide a task em sub-tasks independentes
  const subTasks = await decompose(query);  // LLM quebra a task em partes

  // Executa todos em paralelo
  const results = await Promise.all(
    subTasks.map(subTask => specialistAgent.run(subTask))
  );

  // Agrega resultados
  return await aggregatorAgent.synthesize(query, results);
}
```

**Quando usar:** análise de múltiplos documentos independentes, busca em múltiplas fontes, tarefas com paralelismo real.

---

### Planner-Executor-Critic — loop de planejamento e reflexão

O agente Planner cria um plano, Executor executa, Critic avalia. Se a qualidade não atingir o threshold, o ciclo se repete.

```
[Planner] → plano → [Executor] → resultado → [Critic] → score
     ↑                                                      |
     └────────────── feedback (se score < threshold) ───────┘
```

```typescript
async function plannerExecutorCritic(task: string, maxCycles = 3): Promise<string> {
  let plan: string;
  let result: string;
  let feedback = "";

  for (let cycle = 0; cycle < maxCycles; cycle++) {
    // Planner
    plan = await plannerAgent.createPlan(task, feedback);

    // Executor
    result = await executorAgent.execute(plan);

    // Critic
    const evaluation = await criticAgent.evaluate({ task, plan, result });

    if (evaluation.score >= 0.85) return result;  // qualidade suficiente

    feedback = evaluation.feedback;  // passa feedback para o próximo ciclo
  }

  return result;  // retorna melhor resultado mesmo sem atingir threshold
}
```

**Custo:** cada ciclo = 3 LLM calls + tools. Use apenas quando qualidade é crítica e latência não é.

---

## LangGraph — Grafos de Estado

LangGraph representa fluxos de agentes como grafos dirigidos, com estado compartilhado e suporte a ciclos (reflexão, correção de erros).

```typescript
import { StateGraph, END } from "@langchain/langgraph";

type AgentState = {
  messages: Message[];
  plan: string | null;
  result: string | null;
  attempts: number;
};

const workflow = new StateGraph<AgentState>({
  channels: {
    messages: { value: (x, y) => x.concat(y), default: () => [] },
    plan: { value: (_, y) => y, default: () => null },
    result: { value: (_, y) => y, default: () => null },
    attempts: { value: (x, y) => x + y, default: () => 0 }
  }
})
  .addNode("planner", async state => ({ plan: await planSteps(state.messages) }))
  .addNode("executor", async state => ({ result: await executeStep(state.plan!), attempts: 1 }))
  .addNode("reviewer", async state => ({
    messages: state.result
      ? [...state.messages, { role: "assistant", content: state.result }]
      : state.messages
  }))
  .addEdge("planner", "executor")
  .addConditionalEdges("reviewer", state => {
    if (state.attempts >= 3) return END;
    if (isGoodResult(state.result)) return END;
    return "planner";  // ciclo de reflexão
  })
  .setEntryPoint("planner");

const app = workflow.compile();
```

**Quando usar LangGraph:** fluxos com ciclos de reflexão, agentes stateful que precisam de checkpointing, pipelines complexos com condicionais.

---

## Long-Running Agents — Resiliência

Agentes que executam por horas precisam de padrões específicos de resiliência.

### Async Task com Polling

```typescript
// 1. Iniciar — retorna imediatamente
// POST /agents/tasks → { taskId: "task_abc", status: "queued" }

// 2. Executar em background (worker queue)

// 3. Status endpoint
// GET /agents/tasks/:id
// { taskId, status: "running", progress: { step: "234/1000", percent: 23 } }
```

### Checkpointing — retomar após falha

```typescript
type AgentCheckpoint = {
  taskId: string;
  stepIndex: number;
  stepName: string;
  state: {
    memorySnapshot: string;
    toolResults: Record<string, unknown>;
    partialOutput: unknown;
  };
  timestamp: Date;
};

class CheckpointedAgent {
  async executeWithCheckpoints(task: AgentTask): Promise<AgentResult> {
    const checkpoints = await this.loadCheckpoints(task.id);
    const startStep = checkpoints.length;  // retoma de onde parou

    for (let step = startStep; step < task.steps.length; step++) {
      const result = await this.executeStep(task.steps[step], this.state);
      this.state = { ...this.state, ...result };

      // Salva checkpoint após cada step bem-sucedido
      await this.saveCheckpoint({
        taskId: task.id,
        stepIndex: step,
        stepName: task.steps[step].name,
        state: this.state,
        timestamp: new Date()
      });
    }

    return this.state.output;
  }
}
```

---

## Error Boundaries — contenção de falhas em loops longos

Agentes falham de formas imprevisíveis. Categorize os erros e tenha estratégia distinta para cada um.

```typescript
type AgentErrorCategory =
  | "tool_error"       // API externa down — retry com backoff
  | "parsing_error"    // LLM não seguiu o formato — retry com instrução mais explícita
  | "context_overflow" // comprimir contexto e retry
  | "infinite_loop"    // pausar e pedir human review
  | "budget_exceeded"  // parar — não retry
  | "safety_violation" // parar e logar — não retry

async function executeWithErrorBoundary(step: AgentStep, state: AgentState): Promise<StepResult> {
  for (let attempt = 0; attempt < 3; attempt++) {
    try {
      return await executeStep(step, state);
    } catch (error) {
      const category = categorizeError(error);

      switch (category) {
        case "tool_error":
          await exponentialBackoff(attempt);
          continue;

        case "parsing_error":
          step.prompt = addParsingInstructions(step.prompt, error);
          if (attempt < 2) continue;
          throw new NonRetryableError("Model unable to follow format");

        case "context_overflow":
          state = await compressContext(state);
          if (attempt < 1) continue;
          throw new NonRetryableError("Context too large even after compression");

        case "infinite_loop":
          await requestHumanReview(state, "Agent stuck in loop");
          return { status: "paused_for_review", state };

        case "budget_exceeded":
        case "safety_violation":
          throw new NonRetryableError(`${category} — stopping agent`);
      }
    }
  }

  throw new Error("Step failed after max retries");
}
```

**Detecção de loop infinito:**
```typescript
function detectInfiniteLoop(stepHistory: AgentStep[]): boolean {
  if (stepHistory.length < 6) return false;

  const recent = stepHistory.slice(-6);
  const toolCalls = recent.map(s => s.toolCall?.name + JSON.stringify(s.toolCall?.args));
  const unique = new Set(toolCalls);

  // Mesmos 2 tool calls repetidos nos últimos 6 steps = loop
  return unique.size <= 2 && stepHistory.length > 10;
}
```

---

## Durable Execution — Temporal e Inngest

Para agentes de longa duração onde checkpointing manual é insuficiente, use durable execution frameworks.

**Temporal:** workflow engine com histórico persistente, retry automático e determinismo garantido.
**Inngest:** mais simples, serverless-friendly, ideal para agentes no stack Node.js.

```typescript
// Inngest — agente com durable execution
import { inngest } from "./inngest";

export const analyzeRepositoryAgent = inngest.createFunction(
  { id: "analyze-repository", retries: 3 },
  { event: "agent/analyze.requested" },
  async ({ event, step }) => {
    // Cada step.run é durável — se o processo morrer, retoma aqui
    const issues = await step.run("fetch-issues", async () => {
      return await github.listIssues(event.data.repo);
    });

    const categories = await step.run("categorize-issues", async () => {
      return await llm.categorize(issues);  // pode levar minutos — sem timeout
    });

    // Sleep durável — suspende o processo, retoma após o intervalo
    await step.sleep("wait-for-review", "24h");

    return await step.run("generate-report", async () => {
      return await reportAgent.generate(categories);
    });
  }
);
```

**Quando usar durable execution:** tasks que levam horas/dias, precisam de sleep durável, têm retry automático complexo, ou precisam de histórico completo de execução para auditoria.

---

## Avaliação de Agentes

**Métricas por tipo:**

| Métrica | Definição | Target |
|---|---|---|
| Task completion rate | % de tasks completadas com sucesso | > 90% |
| Tool precision | % de tool calls corretas vs desnecessárias | > 80% |
| Step efficiency | Steps usados vs mínimo teórico | < 1.5× |
| Hallucination rate | % de informações inventadas vs tool outputs | < 5% |
| Cost per task | Custo médio em tokens por task completada | Depende do SLA |

```python
# Casos de teste com tool calls esperadas
test_cases = [
    {
        "input": "Qual o saldo da conta 12345?",
        "expected_tool_calls": ["get_account_balance"],
        "expected_output_contains": "R$"
    }
]

# Avaliação automatizada com LangSmith ou Langfuse
from langfuse.callback import CallbackHandler

handler = CallbackHandler(
    public_key="pk-...", secret_key="sk-...",
    session_id=session_id, user_id=user_id,
    tags=["production", "agent-v2"]
)
agent.invoke(input, config={"callbacks": [handler]})
```

---

## Observabilidade Mínima em Produção

```typescript
import { trace } from "@opentelemetry/api";

const tracer = trace.getTracer("ai-agent");

async function tracedAgentStep(step: string, fn: () => Promise<unknown>) {
  return tracer.startActiveSpan(`agent.${step}`, async span => {
    span.setAttributes({ "ai.step": step });
    try {
      const result = await fn();
      span.setStatus({ code: SpanStatusCode.OK });
      return result;
    } catch (err) {
      span.recordException(err);
      span.setStatus({ code: SpanStatusCode.ERROR });
      throw err;
    } finally {
      span.end();
    }
  });
}
```

**Mínimo para produção:** trace de cada step, custo por agente run, tool calls (nome + args + resultado), erros com categoria.

---

## Trade-offs dos Padrões

| Padrão | Complexidade | Paralelismo | Controle | Quando usar |
|---|---|---|---|---|
| Single Agent | Baixa | Nenhum | Total | Tasks de domínio único |
| Supervisor | Média | Parcial | Alto | Task com especialistas distintos |
| Handoff | Baixa | Nenhum | Alto | Pipeline sequencial bem definido |
| Swarm | Média | Total | Baixo | Sub-tasks independentes |
| Planner-Executor-Critic | Alta | Nenhum | Médio | Qualidade > latência |
| LangGraph | Alta | Parcial | Muito alto | Fluxos com ciclos e estado |

---

## Problemas Comuns em Produção

| Problema | Causa | Solução |
|---|---|---|
| Loop infinito | Agente não reconhece que terminou | `maxSteps` + detecção de loop |
| Context overflow | Histórico crescendo sem limite | Sliding window + summarização |
| Tool call inválido | Description vaga | Melhorar descriptions, adicionar exemplos |
| Latência > 30s | Steps sequenciais evitáveis | Paralelizar tools independentes |
| Custo explosivo | Modelo grande em loop com bugs | Modelo pequeno para steps simples, budget por run |
| Sub-agente sem contexto suficiente | Handoff incompleto | Passar `completedSteps` no contexto de handoff |

---

## Conceitos Relacionados

[[agentes-core]] · [[agent-memory]] · [[mcp]] · [[context-engineering]] · [[llm-observability]]

---
*Fonte: tech-mentor skill · tech-mentor-ai · 2026-04-08*
