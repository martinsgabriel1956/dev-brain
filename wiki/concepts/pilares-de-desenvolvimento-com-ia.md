---
type: concept
title: "Pilares do Desenvolvimento com IA"
aliases: ["pilares da IA no desenvolvimento", "elementos de domínio para trabalhar com IA"]
date_created: 2026-09-29
date_updated: 2026-09-29
source_count: 2
tags: [harness, agentes, modelos, memoria, skills, mcp, documentacao, intencionalidade]
skill: tech-mentor-ai
status: draft
---

# Pilares do Desenvolvimento com IA

Lista de elementos que, dominados, aumentam a chance de minimizar os problemas ao desenvolver com IA ([[wiki/sources/pilares-desenvolvimento-com-ia-contrato-de-revisao-waves]]):

| Pilar | Ideia | Página |
|---|---|---|
| Ferramentas (IDEs/CLIs) | São o harness; agentes especializáveis | [[wiki/concepts/harness]], [[wiki/concepts/subagentes]] |
| Modelos | Modelo certo, momento certo, velocidade certa, menor custo | [[wiki/concepts/roteamento-automatico-de-modelo]] |
| Documentação/artefatos | Para o dev, o chefe e o novato entenderem o sistema | [[wiki/concepts/spec-driven-development]] |
| Memória | Evita repetir erros; sofre [[wiki/concepts/memory-rot]] | [[wiki/concepts/agent-memory-tres-camadas]] |
| Onde roda | Local, remoto, pipeline de CD, remote control no celular | — |
| Skills | Boa × ruim faz enorme diferença; ilusão de saber criar | [[wiki/concepts/skills-agente]] |
| MCPs | Poucos e adequados: consomem contexto | [[wiki/concepts/model-context-protocol]] |

Tese: entender cada item a fundo torna o dev **mais intencional**. A fonte lista os pilares sem hierarquia nem evidência empírica; o mesmo enquadramento aparece de outra forma em [[wiki/concepts/context-engineering-harness]].

## Key sources

- [[wiki/sources/pilares-desenvolvimento-com-ia-contrato-de-revisao-waves]]
- [[wiki/sources/avaliacao-de-skills-skill-creator-description-e-benchmark]] — como medir o pilar 'skills' (evals de description e com/sem skill), endereçando a 'falsa sensação' de saber criar skills
