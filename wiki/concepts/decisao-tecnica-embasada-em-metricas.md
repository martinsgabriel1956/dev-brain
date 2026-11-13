---
type: concept
title: "Decisão Técnica Embasada em Métricas"
aliases: ["decisão embasada em números", "justificar adoção com números", "decisão baseada em dados"]
date_created: 2026-11-03
date_updated: 2026-11-13
source_count: 2
tags: [decisao-arquitetural, metricas, prova-de-conceito, over-engineering, comunicacao]
skill: tech-mentor-backend
status: stub
---

# Decisão Técnica Embasada em Métricas

Sustentar a adoção de framework, componente ou padrão com números de testes e [[wiki/concepts/prova-de-conceito|provas de conceito]] no cenário real do projeto, em vez de um ganho imaginado.

## O que a justificativa deve responder

Segundo [[wiki/sources/como-evitar-overengineering-kiss-yagni-decisoes-embasadas-abordagem-evolutiva]]:

- O que isso resolve?
- Qual métrica melhora, com base nos testes feitos?
- Quais são as vantagens em termos concretos?

Os exemplos da fonte são ilustrativos, não medições: sair de 5 para 1.000 usuários, ou reduzir uma requisição de 10 s para 1 s.

## Dois usos

1. **Para quem decide:** o número ajuda a perceber se a mudança é [[wiki/concepts/over-engineering]].
2. **Para o gestor:** o número traduz um custo adicional em resultado esperado.

## Limites

- PoC em escala irreal não vale como evidência ([[wiki/concepts/prova-de-conceito]], via [[wiki/sources/ciclo-de-mudanca-de-arquitetura]]).
- Os exemplos da fonte cobrem capacidade e latência. Ela não diz como justificar ganhos de manutenção, que são mais difíceis de medir.

## Ver também

- [[wiki/concepts/diagnostico-antes-de-reestruturar]] — entender o gargalo antes de mudar a arquitetura
- [[wiki/concepts/tradeoff-arquitetural]] — ganhos sempre avaliados contra custos
- [[wiki/concepts/empresa-como-laboratorio-de-testes]] — o que acontece sem esse critério
- [[wiki/concepts/abordagem-evolutiva]] — dados de uso orientando a evolução do produto
- [[wiki/concepts/porque-das-decisoes-de-design]] — o paralelo em design: cada escolha visual precisa de razão defensável diante do cliente

## Key Sources

- [[wiki/sources/como-evitar-overengineering-kiss-yagni-decisoes-embasadas-abordagem-evolutiva]]
- [[wiki/sources/cpu-profiling-nodejs-inspector-autocannon-erick-wendel]]: cada linha alterada medida no mesmo teste de carga (2000, 11.000, 13.000) e uma rodada repetida para separar ruído de ganho
