---
type: concept
title: "IA na Esteira (CI/CD): Gerar vs. Executar"
aliases: ["ia no pipeline", "llm na esteira", "ia no ci/cd", "esteira determinística", "verificação periódica de llm"]
date_created: 2026-09-29
date_updated: 2026-09-29
source_count: 1
tags: [ci-cd, ia, llm, determinismo, drift, evals, custo, pipeline]
skill: tech-mentor-ai
status: draft
---

# IA na Esteira (CI/CD): Gerar vs. Executar

## TL;DR

Distinção operacional proposta em [[wiki/sources/dev-na-era-da-ia-qualidade-esteira-e-novas-preocupacoes]]: usar IA para **construir** a esteira (testes, quality gate, linters, configuração de ferramentas) é ótimo; fazer a **execução** da esteira depender de uma LLM (ex.: agente que lê o log a cada build e aponta o erro) o autor considera ainda inadequado — a LLM é não determinística, custa tokens e deixa o build mais lento.

## Regras da fonte

1. **Gerar ≠ executar.** Código de teste, gate e linter pode ser gerado com IA (com acompanhamento e conhecimento de regra de negócio), mas depois de pronto roda como código comum. Isso preserva o determinismo exigido de um gate — ver [[wiki/concepts/determinismo-vs-probabilismo-em-ia]] e [[wiki/concepts/quality-gate]].
2. **Esteira de um sistema comum = 100% determinística.** Sem LLM no caminho crítico do build.
3. **Produto que chama LLM (chatbot, integração, automação):** o build continua determinístico. Além dele, há uma verificação **de comportamento**: fazer perguntas à LLM para detectar *behavior drift* e vazamento de informação/segurança. Essa verificação **não roda a cada commit**: roda **periodicamente** (exemplo do autor: a cada 2 semanas) e **quando o prompt muda**, possivelmente desacoplada do disparo do CI/CD.
4. **Usar a IA para aprender a esteira:** ao configurar ferramentas desconhecidas (GitHub etc.), fazer junto com a IA, passo a passo, em vez de delegar o entendimento.

## Por que faz sentido

- **Custo e latência:** cada execução com LLM consome tokens e tempo; uma esteira roda dezenas de vezes por dia.
- **Confiabilidade do gate:** um gate que decide por probabilidade pode aprovar/reprovar de forma inconsistente entre execuções (caso em [[wiki/concepts/determinismo-vs-probabilismo-em-ia]]).
- **Momento certo do eval:** o comportamento de uma LLM só muda quando muda o modelo, o prompt ou os dados — não a cada commit de código não relacionado. [skill: tech-mentor-ai, `production-evals.md`/`llm-testing.md`] cobre a mesma ideia de separar evals rápidos (pré-deploy/CI) de monitoramento contínuo e usa modelo mais barato para evals de CI e mais preciso para execuções noturnas.

## Relação com o restante da wiki

- Agentes que monitoram o PR/CI e corrigem ("babysit") existem em [[wiki/concepts/skills-agente]] e [[wiki/concepts/quality-gate]]; a fonte não os condena explicitamente, mas rejeita o agente **como executor** do gate. A diferença é onde a LLM está: depois do gate determinístico (assistindo) vs. no lugar dele (decidindo).
- Evals de comportamento de LLM: [[wiki/concepts/llm-evals-testing]].
- Sentido de "drift" aqui: [[wiki/concepts/drift-detection]] (seção *behavior drift*).
- Estrutura geral de pipeline: [[wiki/concepts/pipeline-de-ci]], [[wiki/concepts/ci-cd]].

## Ressalvas

- Posição de **opinião** de um único autor, sem métricas. A cadência "a cada 2 semanas" é um exemplo, não uma regra. `[external]` Práticas de mercado variam (muitas equipes rodam evals leves em todo PR que toca prompt).

## Key Sources

- [[wiki/sources/dev-na-era-da-ia-qualidade-esteira-e-novas-preocupacoes]]
