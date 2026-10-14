---
type: concept
title: "Análise de Impacto da Correção"
aliases: ["impacto colateral", "quem consome este método", "mudança de entrada e saída"]
date_created: 2026-10-14
date_updated: 2026-10-14
source_count: 1
tags: [bugs, regressao, refatoracao, testes, acoplamento]
skill: tech-mentor-testing
status: draft
---

# Análise de Impacto da Correção

Depois de [[wiki/concepts/provar-que-corrigiu|provar a correção]] (ordem: primeiro corrige, depois procura impactos), [[wiki/entities/andre-casciotti]] sugere olhar o que a mudança pode quebrar em outro lugar:

1. O trecho alterado é **reutilizado**? Procurar referências/consumidores (find references, busca em arquivos).
2. A mudança alterou **entrada ou saída** (o contrato)? Ex.: antes retornava sempre 1, agora pode ser 0 ou nulo, o que pode quebrar consumidores. Mudança só interna tem impacto menor.
3. **Teste unitário** detecta a mudança de contrato e já mapeia os consumos; faltando teste, criar para os consumidores.

Funciona porque o passo 1 já deu a visão macro do fluxo; olhar só a linha é a causa de "corrige aqui, quebra ali". [skill: tech-mentor-testing] é a mesma ideia de testes de regressão e *characterization tests* para código legado (`test-strategy-risk-architecture.md`). Ver [[wiki/concepts/tres-passos-para-lidar-com-bug]], [[wiki/concepts/causa-raiz]].

## Key Sources

- [[wiki/sources/como-sair-do-ciclo-de-bugs-e-retrabalho-andre-casciotti]]
