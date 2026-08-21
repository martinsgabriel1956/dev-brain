---
type: concept
title: "Paradoxo da Aceleração"
aliases: ["acceleration paradox", "paradoxo da aceleracao", "velocidade individual atrito sistemico"]
date_created: 2026-08-10
date_updated: 2026-08-20
source_count: 2
tags: [ia-produtividade, engineering-metrics, code-review, faros-ai, gargalo]
skill: tech-mentor-leadership
status: draft
---

# Paradoxo da Aceleração

**TL;DR:** Termo da [[wiki/entities/faros-ai]] para o descompasso entre **velocidade individual** (que sobe muito com IA) e **throughput do sistema** (que quase não sobe, ou piora). A IA acelera a etapa errada — a escrita — enquanto o gargalo real migra para a revisão, que não escala junto.

## O mecanismo

```
IA acelera a escrita de código
    ↓
Devs fazem 21% mais tarefas, ~2x mais PRs (individualmente)
    ↓
Mas a revisão exige julgamento humano e não escala igual
    ↓
Tempo de code review sobe 91% → fila de PRs
    ↓
Ganho individual não vira ganho de time (empresa: só +10%)
```

Antes da IA havia equilíbrio: um dev escrevia, outro revisava, mergeava — ritmos compatíveis. A IA rompe esse equilíbrio acelerando só a produção. O gargalo deixa de ser a escrita e passa a ser a **revisão** — uma tarefa que exige atenção, contexto do sistema e julgamento, que a IA não resolve e ainda **alimenta com mais código para revisar**.

## Por que a revisão não escala

Código gerado por IA **não é mais simples de revisar** — às vezes é mais difícil: é tecnicamente válido (segue padrões) mas pode ser arquiteturalmente errado, passar nos testes e quebrar a lógica de negócio. Ver [[wiki/concepts/gaming-de-testes-por-ia]] e [[wiki/concepts/ia-como-amplificador]].

## Os números (Faros AI)

| Métrica | Valor |
|---|---|
| Adoção de IA entre devs | 93% |
| Ganho de produtividade da empresa | 10% |
| Tarefas por dev | +21% |
| PRs mergeados por dev | ~2x |
| Tempo de code review | +91% |
| Devs que já bateram limites de uso | 30% |

> Números da fonte primária Faros AI reportados via transcrição — ver ressalva em [[wiki/sources/paradoxo-da-aceleracao-ia-produtividade-metricas]].

## Evolução vs. Revolução: Tratar a IA Como Otimização de Etapa É a Causa

[[wiki/sources/engenharia-de-contexto-vs-prompt-engineering-gargalo-real-times-ia]] chega ao mesmo fenômeno por um caminho diferente do dado quantitativo da Faros AI: raciocínio de ciclo completo. Se o fluxo de entrega vai de refinamento a deploy (refinamento → dev → revisão → teste → homologação → aprovação → deploy) e a IA só acelera a etapa "escrever código", o ganho no ciclo total fica limitado ao peso que essa etapa representa — as demais etapas (entre elas a revisão, o gargalo identificado pela Faros AI) continuam do mesmo tamanho.

A fonte nomeia a causa raiz como uma escolha, não um destino inevitável: tratar a IA como **evolução** — "plugar a ferramenta no processo que já existe e esperar o ganho aparecer" — versus como **revolução** — redesenhar o processo, o tamanho de tarefa e quem responde pela entrega em função do gargalo que migrou. Nessa leitura, o paradoxo da aceleração não é um limite físico da IA, é o resultado padrão de tratá-la como evolução: acelerar a escrita sem redesenhar a revisão (ou qualquer outra etapa que virou o novo gargalo) ao redor dela.

Recorte explícito da fonte: para um MVP sem legado, compliance ou revisão pesada, código mais rápido *é* uma vantagem real — o paradoxo aparece especificamente em projetos onde as etapas downstream (revisão, teste, homologação) já eram o gargalo estrutural antes da IA.

## Relação com outros paradoxos

Estrutura análoga ao [[wiki/concepts/roi-de-ia]] (ganho individual que não sobe para a empresa) e ao [[wiki/concepts/paradoxo-de-jevons]] (mais eficiência → mais consumo). A raiz comum é medir a etapa errada — ver [[wiki/concepts/output-vs-outcome]] e [[wiki/concepts/goodharts-law]].

## Conceitos Relacionados

[[wiki/concepts/ia-como-amplificador]] · [[wiki/concepts/output-vs-outcome]] · [[wiki/concepts/code-review]] · [[wiki/concepts/roi-de-ia]] · [[wiki/concepts/dora-metrics]]

## Key Sources

- [[wiki/sources/paradoxo-da-aceleracao-ia-produtividade-metricas]]
- [[wiki/sources/engenharia-de-contexto-vs-prompt-engineering-gargalo-real-times-ia]] — mesma dinâmica via raciocínio de ciclo completo (refinamento→deploy); distinção evolução (plugar IA no processo existente) vs. revolução (redesenhar processo) como causa raiz
