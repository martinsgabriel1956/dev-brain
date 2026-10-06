---
type: concept
title: "Harness: Componente por Capacidade (De-Para de Trivedy)"
aliases: ["de-para harness", "harness capability map", "modelo vs harness"]
date_created: 2026-10-06
date_updated: 2026-10-06
source_count: 1
tags: [harness, langchain, sandbox, memoria, compactacao, mcp, loop, harness-engineering]
skill: tech-mentor-ai
status: draft
---

# Harness: Componente por Capacidade

Mapa de [[wiki/entities/vivek-trivedy]] ([[wiki/entities/langchain]]), relatado em [[wiki/sources/harness-engineering-dicionario-do-programador-guias-sensores]]: o modelo sozinho não faz X; o harness adiciona Y.

| Comportamento desejado | Componente de harness | Páginas |
|---|---|---|
| Dados reais, persistentes | File system + Git | [[wiki/concepts/harness]] |
| Escrever/executar código | Bash + ambiente de execução | [[wiki/concepts/tool-call]] |
| Execução segura, tools padrão | Sandbox + tooling | [[wiki/concepts/agent-containment]] |
| Lembrar/acessar conhecimento novo | Arquivos de memória + web search + MCPs | [[wiki/concepts/agent-memory-tres-camadas]], [[wiki/concepts/model-context-protocol]] |
| Desempenho em contexto longo | Compactação + tool-offloading + skills | [[wiki/concepts/context-compaction]], [[wiki/concepts/skills-agente]] |
| Trabalho de longo prazo | Loops + planejamento + verificação | [[wiki/concepts/loop-engineering]], [[wiki/concepts/ralph-loop]] |

Lista explicitamente não exaustiva. Compare com os "doze componentes" em [[wiki/concepts/harness]].

## Key Sources

- [[wiki/sources/harness-engineering-dicionario-do-programador-guias-sensores]] — relato do áudio; texto original de Trivedy não verificado `[external]`; "loops" da última linha é leitura incerta do ASR.
