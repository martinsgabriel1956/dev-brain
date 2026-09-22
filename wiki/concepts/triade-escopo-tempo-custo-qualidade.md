---
type: concept
title: "Tríade Escopo-Tempo-Custo e a Quarta Variável Invisível"
aliases: ["iron triangle", "triângulo de ferro de projetos", "quarta variável qualidade"]
date_created: 2026-09-22
date_updated: 2026-09-22
source_count: 1
tags: [gestao-de-projetos, escopo, qualidade, engineering-management]
skill: tech-mentor-leadership
status: stub
---

# Tríade Escopo-Tempo-Custo e a Quarta Variável Invisível

**TL;DR:** Todo projeto é limitado pela tríade escopo, tempo e custo — é impossível maximizar escopo minimizando tempo e custo ao mesmo tempo. Segundo [[wiki/entities/fabio-akita]], existe uma quarta variável que a tríade clássica não nomeia explicitamente: qualidade. Quando tempo e custo são fixados como restrições externas e o escopo não cede junto (porque ninguém quer cortar features), quem cede de forma invisível é a qualidade — e o custo disso é empurrado para a fase de operação.

## O mecanismo

Tempo e custo costumam ser os fatores fixos de um projeto (prazo definido pelo negócio, orçamento aprovado). Isso deveria forçar o escopo a se ajustar — mas escopo é sempre mal definido no início e os objetivos reais só ficam claros ao longo do projeto, então a pressão para manter o escopo "combinado" persiste mesmo quando não deveria. Quando as três variáveis visíveis (escopo, tempo, custo) são mantidas fixas sob pressão, a variável que absorve a diferença é a qualidade — código com atalhos, testes pulados, dívida técnica não documentada. O problema é que qualidade é mais difícil de medir em dólares e horas do que as outras três, então essa degradação passa despercebida até virar bug em produção.

## Sequência recomendada

1. Estabeleça a data final.
2. Estabeleça o orçamento.
3. Liste os objetivos em ordem de prioridade.
4. Trate qualidade como restrição explícita, não como variável livre.
5. Só então acomode o escopo que cabe dentro dessas restrições — normalmente não cabe tudo, e cortar é parte do trabalho, não uma falha do processo.

## Ver também

- [[wiki/concepts/gestao-de-riscos-e-controle-ilusorio]] — decisão sob incerteza como núcleo do trabalho de gestão
- [[wiki/concepts/estimativas-de-software]] — por que a variável "tempo" já chega distorcida antes mesmo de discutir qualidade
- [[wiki/concepts/tech-debt-como-ferramenta]] — a forma concreta que a "queda de qualidade" assume no código

## Key Sources

- [[wiki/sources/sobre-ser-gerente-fabio-akita]]
