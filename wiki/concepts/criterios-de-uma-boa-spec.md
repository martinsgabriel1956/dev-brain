---
type: concept
title: "Critérios de uma Boa Spec"
aliases: ["7 critérios de spec", "falseabilidade de specs", "spec quality checklist"]
date_created: 2026-08-18
date_updated: 2026-08-18
source_count: 1
tags: [spec-driven, tech-spec, qualidade-de-spec, falseabilidade, context-engineering]
skill: tech-mentor-ai
status: draft
---

# Critérios de uma Boa Spec

## TL;DR

Framework de 7 critérios para avaliar se uma [[wiki/concepts/tech-spec|tech spec]] está pronta para guiar execução autônoma de um agente, proposto em [[wiki/sources/spec-writer-skill-criterios-de-boa-spec]] como o gate de validação (etapa 5 de 6) de uma skill pessoal de geração de specs ("Spec Writer"). Nenhuma fonte anterior na wiki detalhava um critério operacional para "spec boa o suficiente" — `tech-spec.md` documentava o que uma tech spec contém, mas não como testar sua qualidade.

## Os 7 Critérios

1. **Falseabilidade.** Toda afirmação deve ser verificável contra o output real. "O sistema deve ser performático" não é falseável; "P99 de latência < 200ms sob 1000 req/s" é.

2. **Comportamento, não implementação.** A spec diz o que é verdade, não como fazer. "Aplicar desconto sobre um valor proporcionado" é comportamento; "criar classe `X.Y.Z` com método `apply`" é implementação e não pertence à spec.

3. **Invariantes.** Regras que nunca podem ser violadas, nomeadas explicitamente — ex.: "o preço final nunca é negativo", "a soma dos créditos distribuídos nunca excede o crédito original numa transação".

4. **Edge cases nomeados.** Casos de borda (vazio, negativo, limite, concorrência/simultaneidade, inexistência) precisam estar listados individualmente, não implícitos. É citado como sinal de spec madura.

5. **Fronteira / escopo explícito.** O que está fora do escopo precisa ser dito, não apenas o que está dentro — ex.: "não trata moedas estrangeiras, só BRL"; "reembolso é um fluxo separado, fora desta spec".

6. **Entradas e restrições.** Como a feature espera receber os dados e sob quais restrições.

7. **Decisões de negócio.** As decisões de negócio que moldaram a spec precisam estar registradas, não só inferidas do contexto.

## Onde Isso se Encaixa no Fluxo SDD

```
PRD (alto nível, sem tecnologia)
  → Spec por feature (technical overview, componentes, decisões técnicas, contratos de API, migration, estratégia de teste)
      → validação contra os 7 critérios ← este framework
          → Execução
```

Os critérios 1–4 (falseabilidade, comportamento, invariantes, edge cases) atacam a **precisão** da spec — deixam menos espaço para o agente inferir errado. Os critérios 5–7 (fronteira, entradas/restrições, decisões de negócio) atacam o **escopo** — deixam explícito o que a spec conscientemente não cobre.

## Por Que Isso Importa: Contexto Insuficiente Vira Inferência Errada

A fonte ilustra o custo de pular esses critérios com um exemplo simples: pedir "implemente um login" sem especificar o comportamento pós-sucesso não dá ao agente informação suficiente para saber que deve redirecionar para o dashboard — ele "faz do jeito que achar que é bom". O framework existe para eliminar exatamente esse tipo de lacuna antes da execução, reforçando a tese central de [[wiki/concepts/context-engineering-harness]] de que a LLM é inferência pura e preenche qualquer vazio de contexto com a própria suposição.

## Relação com Outros Conceitos

- [[wiki/concepts/tech-spec]] — este framework é o critério de validação que falta no "O que Contém" / "O que NÃO Contém" já documentado ali
- [[wiki/concepts/spec-driven-development]] — os critérios operacionalizam a etapa de "Planejamento" do processo SDD
- [[wiki/concepts/quality-gate]] — a etapa 5 da skill Spec Writer funciona como um quality gate aplicado à spec, não ao código
- [[wiki/concepts/prd-product-requirements-document]] — o PRD é intencionalmente não-falseável/alto-nível; os critérios de falseabilidade só se aplicam a partir da spec por feature, um nível abaixo

## Key Sources

- [[wiki/sources/spec-writer-skill-criterios-de-boa-spec]] — origem do framework, demonstrado via skill "Spec Writer" (6 etapas: validar inputs, entrevista, sumarizar, gerar documento, validar contra os 7 critérios, escrever output)
