---
date: 2026-04-08
tags: [tech-mentor, ia, evals, llm-as-judge, golden-dataset, ragas, deepeval, g-eval, promptfoo, evalite, ci-evals, prompt-regression]
skill: tech-mentor-ai/references/ai/production-evals.md
level: avançado
---

# Avaliação Sistemática (Evals)

## Contexto

Sem evals, você está voando cego. Cada mudança de prompt pode quebrar casos que funcionavam — e você só vai saber quando um usuário reclamar. Evals sistemáticas são o que diferencia um sistema LLM de produção de um protótipo funcional.

---

## Como Funciona

### O problema central

LLMs são não-determinísticos e seu output é difícil de avaliar programaticamente. A solução é um pipeline de avaliação em três níveis:

```
Offline (pré-deploy)   → Golden dataset + métricas automáticas
Online (produção)      → Sampling de tráfego real + LLM-as-judge
CI (a cada PR)         → Evals bloqueantes que impedem regressão
```

---

## LLM-as-Judge — avaliação escalável

Usar um modelo mais forte como árbitro para avaliar outputs. Escala onde avaliação humana não consegue.

```typescript
async function evaluateResponse(question: string, answer: string): Promise<number> {
  const response = await openai.chat.completions.create({
    model: "gpt-4o",
    messages: [{
      role: "user",
      content: `Rate the following answer to the question on a scale of 1-5.
Question: ${question}
Answer: ${answer}
Return only JSON: {"score": <1-5>, "reason": "<brief explanation>"}`
    }],
    response_format: { type: "json_object" },
    temperature: 0
  });

  return JSON.parse(response.choices[0].message.content).score;
}
```

**Bias do LLM-as-Judge — como calibrar:**
- **Preferência por respostas longas:** penalize verbosidade explicitamente no prompt do juiz
- **Posição bias:** em comparações A/B, rode com ordem invertida e faça média
- **Auto-preferência:** modelo OpenAI tende a preferir outputs OpenAI — use Anthropic como juiz para outputs de todos os providers
- **Calibração:** rode 5–10% dos casos com avaliação humana e compare com o juiz para medir concordância (correlação de Spearman > 0.7 é aceitável)

---

## Golden Dataset — a base de tudo

Conjunto curado de `(input, expected_output)` que define o comportamento correto do sistema. Toda mudança de prompt ou modelo é avaliada contra ele antes de ir a produção.

```
eval-suite/
├── golden/
│   ├── qa-basic.jsonl           ← casos de Q&A simples
│   ├── qa-edge-cases.jsonl      ← casos difíceis, ambíguos
│   └── regression/
│       └── 2025-03-incident.jsonl  ← bugs que chegaram a prod → testes permanentes
├── prompts/
│   └── system-v3.txt            ← prompt versionado
└── results/
    └── 2026-04-08-claude.json   ← snapshot de resultado por data+modelo
```

```jsonl
{"id": "qa-001", "input": "Quanto custa o plano Pro?", "expected": "R$ 99/mês", "tags": ["pricing"]}
{"id": "qa-002", "input": "Como cancelo minha conta?", "expected_contains": ["cancelar", "conta"], "tags": ["support"]}
{"id": "qa-003", "input": "Qual é o prazo de entrega?", "expected": "5 dias úteis", "tags": ["shipping"]}
```

**Regras de curadoria:**
- Adicionar ao golden dataset **toda vez** que um bug de LLM chegar a produção
- Nunca deletar casos — marcar como `deprecated: true` no máximo
- 50–200 casos é o range útil; mais vira slow test suite
- Distribuição de tags deve refletir o tráfego real

---

## Eval Harness Customizado

```typescript
type EvalCase = {
  id: string;
  input: string;
  expected?: string;
  expectedContains?: string[];
  tags?: string[];
};

type EvalResult = {
  id: string;
  passed: boolean;
  score: number;    // 0–1
  actual: string;
  latency: number;
};

async function runEvals(goldenPath: string): Promise<void> {
  const cases: EvalCase[] = loadJsonl(goldenPath);
  const results: EvalResult[] = [];

  for (const testCase of cases) {
    const start = Date.now();
    const actual = await callLLM(testCase.input);
    const latency = Date.now() - start;

    const passed = checkExpectation(actual, testCase);
    results.push({ id: testCase.id, passed, score: passed ? 1 : 0, actual, latency });
  }

  const passRate = results.filter(r => r.passed).length / results.length;
  const avgLatency = results.reduce((s, r) => s + r.latency, 0) / results.length;

  console.log({ passRate, avgLatency, total: results.length });

  // Falha CI se pass rate abaixo do threshold
  if (passRate < 0.85) process.exit(1);
}

function checkExpectation(actual: string, testCase: EvalCase): boolean {
  if (testCase.expected) {
    return actual.toLowerCase().includes(testCase.expected.toLowerCase());
  }
  if (testCase.expectedContains) {
    return testCase.expectedContains.every(term => actual.toLowerCase().includes(term));
  }
  return true;  // sem expectativa → smoke test (não crashou)
}
```

---

## RAGAS — métricas específicas para RAG

Quatro métricas fundamentais para avaliar pipelines RAG:

```python
from ragas import evaluate
from ragas.metrics import faithfulness, answer_relevancy, context_precision, context_recall

dataset = Dataset.from_list([{
    "question": "Qual o prazo de devolução?",
    "answer": llm_answer,
    "contexts": retrieved_chunks,
    "ground_truth": "O cliente tem até 7 dias corridos para solicitar devolução."
}])

results = evaluate(dataset, metrics=[faithfulness, answer_relevancy, context_precision, context_recall])
# {"faithfulness": 0.85, "answer_relevancy": 0.92, "context_precision": 0.78, "context_recall": 0.71}
```

**O que cada métrica sinaliza:**

| Métrica | < threshold | Causa provável | Solução |
|---|---|---|---|
| `faithfulness` < 0.8 | LLM alucina além do contexto | Prompt mais restritivo, temperatura 0 |
| `context_precision` < 0.7 | Retrieval trazendo ruído | Re-ranking, threshold de relevância |
| `context_recall` < 0.7 | Chunks relevantes não recuperados | Hybrid search, HyDE, query expansion |
| `answer_relevancy` < 0.8 | Resposta desviou do ponto | CoT no prompt, foco explícito |

---

## DeepEval — framework de evals com múltiplas métricas

```python
from deepeval import evaluate
from deepeval.metrics import (
    AnswerRelevancyMetric,
    FaithfulnessMetric,
    HallucinationMetric,
    ContextualPrecisionMetric,
    BiasMetric,
    ToxicityMetric
)
from deepeval.test_case import LLMTestCase

test_case = LLMTestCase(
    input="O que é RAG?",
    actual_output=llm_response,
    expected_output="Retrieval-Augmented Generation é...",
    retrieval_context=retrieved_chunks
)

metrics = [
    AnswerRelevancyMetric(threshold=0.7, model="gpt-4o-mini"),
    FaithfulnessMetric(threshold=0.8, model="gpt-4o-mini"),
    HallucinationMetric(threshold=0.1, model="gpt-4o-mini")
]

evaluate([test_case], metrics)
# Gera relatório com pass/fail por métrica e motivo do LLM judge

# Integração com pytest
import pytest
from deepeval import assert_test

@pytest.mark.parametrize("test_case", load_test_cases("golden-dataset.json"))
def test_rag_pipeline(test_case: LLMTestCase):
    test_case.actual_output = run_pipeline(test_case.input)
    assert_test(test_case, [AnswerRelevancyMetric(threshold=0.7)])
```

---

## G-Eval — avaliação com critérios customizados

G-Eval usa CoT interno para avaliar com critérios em linguagem natural. Flexível para domínios específicos onde métricas genéricas não capturam o que importa.

```python
from deepeval.metrics import GEval
from deepeval.test_case import LLMTestCaseParams

# Critério para tom de suporte ao cliente
tone_metric = GEval(
    name="Professional Tone",
    criteria="""
    The response should be:
    1. Professional and empathetic
    2. Free of jargon the customer wouldn't understand
    3. Actionable — provides concrete next steps
    """,
    evaluation_params=[LLMTestCaseParams.INPUT, LLMTestCaseParams.ACTUAL_OUTPUT],
    threshold=0.8,
    model="gpt-4o"
)

# Critério de corretude factual para domínio jurídico
correctness_metric = GEval(
    name="Legal Accuracy",
    criteria="The response must cite the correct article of Brazilian law and not generalize.",
    evaluation_params=[
        LLMTestCaseParams.INPUT,
        LLMTestCaseParams.ACTUAL_OUTPUT,
        LLMTestCaseParams.EXPECTED_OUTPUT
    ],
    threshold=0.85
)
```

---

## promptfoo — testes de prompt em CI/CD

Open source, roda via CLI, integra com qualquer CI.

```yaml
# promptfooconfig.yaml
prompts:
  - prompts/system-v3.txt

providers:
  - openai:gpt-4o-mini
  - anthropic:claude-3-haiku-20240307

tests:
  - description: "Resposta sobre prazo de devolução"
    vars:
      question: "Qual é o prazo para devolução?"
    assert:
      - type: contains
        value: "7 dias"
      - type: llm-rubric
        value: "The response is professional and mentions the return policy clearly"
        threshold: 0.8

  - description: "Não responde sobre concorrentes"
    vars:
      question: "Como a Acme se compara com a Competitor Corp?"
    assert:
      - type: not-contains
        value: "Competitor Corp"
      - type: latency
        threshold: 3000  # ms

defaultTest:
  assert:
    - type: latency
      threshold: 5000
```

```bash
# Rodar no CI
npx promptfoo eval --config promptfooconfig.yaml --output results.json
npx promptfoo view  # dashboard de comparação A/B
```

---

## evalite — TypeScript, lightweight

Para projetos TypeScript que não querem adicionar um framework pesado.

```typescript
import { evalite } from "evalite";
import { Levenshtein } from "autoevals";

evalite("RAG Pipeline Evals", {
  data: async () => [
    { input: "Qual o prazo de entrega?", expected: "5 dias úteis" },
    { input: "Como faço devolução?", expected: "Em até 7 dias corridos" }
  ],
  task: async input => {
    const { answer } = await ragPipeline(input);
    return answer;
  },
  scorers: [
    Levenshtein,  // similaridade de string
    // ou LLM-as-judge customizado
    async ({ input, output, expected }) => ({
      name: "Relevance",
      score: await scoreRelevance(input, output, expected)
    })
  ]
});
```

---

## Evals em CI — integração no pipeline de deploy

```yaml
# .github/workflows/evals.yml
name: LLM Eval Suite

on:
  pull_request:
    paths:
      - "prompts/**"
      - "src/ai/**"

jobs:
  evals:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Run eval suite
        run: npx tsx scripts/run-evals.ts
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          BASELINE_PASS_RATE: "0.85"

      - name: Upload eval results
        uses: actions/upload-artifact@v4
        with:
          name: eval-results
          path: results/

      - name: Comment results on PR
        uses: actions/github-script@v7
        with:
          script: |
            const results = require('./results/latest.json');
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              body: `## Eval Results\nPass rate: ${results.passRate}\nAvg latency: ${results.avgLatency}ms`
            });
```

**Regra:** evals bloqueiam o merge se `passRate < baseline - 2%`. Isso previne regressões silenciosas.

---

## Benchmarking Interno — comparar providers

```typescript
async function benchmarkProviders(cases: EvalCase[]) {
  const providers = ["gpt-4o-mini", "claude-3-haiku-20240307", "gemini-1.5-flash"];

  for (const model of providers) {
    const start = Date.now();
    const results = await Promise.all(cases.map(c => callModel(model, c.input)));
    const elapsed = Date.now() - start;

    const passRate = computePassRate(results, cases);
    const totalCost = computeCost(results, model);
    const avgLatency = elapsed / cases.length;

    console.log({ model, passRate, avgLatencyMs: avgLatency, totalCostUsd: totalCost });
  }
}

// Saída típica:
// { model: "gpt-4o-mini",          passRate: 0.88, avgLatencyMs: 320, totalCostUsd: 0.002 }
// { model: "claude-3-haiku-...",   passRate: 0.91, avgLatencyMs: 280, totalCostUsd: 0.003 }
// { model: "gemini-1.5-flash",     passRate: 0.85, avgLatencyMs: 410, totalCostUsd: 0.001 }
```

**Decisão baseada em benchmark interno:**
- Qualidade crítica → escolha pelo passRate
- Custo prioritário → `custo / passRate` (eficiência)
- Latência prioritária → avgLatencyMs com passRate mínimo aceitável

---

## Prompt Versioning como Código

```
Prompts são código — versionados no Git, revisados em PR, testados antes do merge.

prompts/
  system-prompt.txt   ← versão corrente
  CHANGELOG.md        ← "v3: adicionado contexto de idioma; melhorou Q&A multilíngue"

Workflow:
  1. Edita system-prompt.txt em branch
  2. Roda eval suite: npm run evals
  3. Compara scores com baseline (main branch)
  4. PR aprovado apenas se passRate >= baseline − 2%
```

```typescript
// CI: comparar prompt novo vs baseline
async function comparePrompts() {
  const baselineScore = parseFloat(process.env.BASELINE_PASS_RATE ?? "0.90");
  const currentScore = await runEvalsAndGetScore("prompts/system-prompt.txt");

  if (currentScore < baselineScore - 0.02) {
    console.error({ message: "Prompt regression detected", baseline: baselineScore, current: currentScore });
    process.exit(1);
  }
}
```

---

## Quando Usar / Quando Evitar

**Golden dataset obrigatório quando:** qualquer sistema LLM que vai para produção. Sem ele você não tem baseline para medir regressão.

**RAGAS quando:** pipeline RAG. As métricas são específicas para esse caso — faithfulness e context_recall não fazem sentido fora de RAG.

**DeepEval quando:** quer um framework com múltiplas métricas pre-built e integração com pytest.

**G-Eval quando:** métricas genéricas não capturam o que importa no seu domínio. Jurídico, médico, atendimento ao cliente têm critérios que RAGAS não mede.

**promptfoo quando:** time faz muitas iterações de prompt e quer comparação side-by-side de variantes e modelos.

**LLM-as-judge quando:** volume é alto demais para avaliação humana. Calibre sempre com um subconjunto humano.

---

## Conceitos Relacionados

[[llmops-observabilidade]] · [[rag-retrieval]] · [[prompt-engineering]] · [[fine-tuning]]

---
*Fonte: tech-mentor skill · tech-mentor-ai · 2026-04-08*
