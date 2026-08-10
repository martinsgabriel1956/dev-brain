---
type: concept
title: "Folga de Capacidade (Slack)"
aliases: ["slack", "folga de fluxo", "nunca alocar 100%", "regra dos 20%", "capacity buffer"]
date_created: 2026-08-10
date_updated: 2026-08-10
source_count: 1
tags: [engineering-management, planejamento, tech-debt, capacidade, fluxo]
skill: tech-mentor-leadership
status: stub
---

# Folga de Capacidade (Slack)

Prática de **nunca alocar 100% da capacidade da equipe** a trabalho planejado, deixando deliberadamente uma folga (tipicamente ~20%) para absorver o imprevisto — bugs críticos, deploy que falha, casos não previstos. Sem essa folga, a única forma de responder a um imprevisto é a gambiarra rápida, ou seja, **emitir [[wiki/concepts/tech-debt-como-ferramenta|dívida técnica]]**.

## Por que funciona

É a intuição da teoria de filas aplicada a times: à medida que a utilização de um recurso se aproxima de 100%, o tempo de espera na fila dispara de forma não-linear. Um time 100% alocado não tem onde encaixar o trabalho não-planejado, então ele vira dívida ou atraso. A folga é o amortecedor que mantém o fluxo previsível.

[[wiki/sources/por-que-code-bases-degradam-estrategias-code-rot]] atribui a ideia ao livro *Principles of Product Development Flow* (ver [[wiki/entities/principles-of-product-development-flow]]) e propõe o modelo prático de **~80% features / ~20% bug fixes e refatoração**.

## Relação com outras práticas

- É a contraparte *organizacional* da [[wiki/concepts/boy-scout-rule]] (que age no nível do PR): a folga garante o *tempo* para que a limpeza contínua aconteça.
- Conecta com a [[wiki/concepts/planning-fallacy]]: como a subestimação é sistemática, planejar a 100% garante estouro; a folga é o reconhecimento estrutural desse erro.
- Distinta de [[wiki/concepts/feature-freeze]] (parada pontual concentrada) — slack é folga *contínua* embutida em toda sprint.

## Key Sources

- [[wiki/sources/por-que-code-bases-degradam-estrategias-code-rot]] — a "regra dos 20%" como principal contramedida organizacional contra code rot
