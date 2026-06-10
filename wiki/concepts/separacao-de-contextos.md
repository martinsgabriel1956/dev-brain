---
type: concept
title: "Separação de Contextos"
aliases: ["context separation", "context isolation", "sessões separadas"]
date_created: 2026-05-04
date_updated: 2026-06-01
source_count: 3
tags: [context-engineering, coding-agents, workflow]
skill: tech-mentor-ai
status: stable
---

# Separação de Contextos

Princípio de isolar fisicamente as fases de trabalho com coding agents em janelas de contexto distintas, impedindo que o estado de uma fase contamine a próxima.

## O Problema da Contaminação

Quando research e plan acontecem na **mesma sessão**, o modelo começa a misturar o que observou com o que acha que deveria ser construído. Decisões de arquitetura aparecem escondidas dentro da fase de observação — o modelo já está "planejando" enquanto deveria só estar "vendo".

Resultado: o plan está enviesado pelas decisões implícitas que o modelo tomou durante o research, sem que o dev tenha tido a chance de revisar ou redirecionar.

## Na Prática

```
Sessão 1 (research): explore o codebase, colete fatos, documente
   ↓ compactar o resultado em markdown
Sessão 2 (plan): recebe os fatos, decide o que construir
   ↓ aprovado pelo dev
Sessão 3 (implement): executa o plano
```

Cada sessão começa com uma context window limpa — sem o ruído acumulado das fases anteriores.

## Sub-agentes como Separação Automatizada

Sub-agentes são uma implementação técnica de separação de contextos:
- O agente pai não faz a exploração diretamente
- Ele dispara um sub-agente com uma nova context window
- O sub-agente faz toda a busca e leitura
- Retorna apenas uma mensagem sucinta: "o arquivo que você quer está aqui, linha X"
- O agente pai lê só aquele arquivo e vai direto ao trabalho

O pai nunca acumula o ruído da exploração — sua context window permanece limpa.

## Relação com Compaction

[[concepts/compaction-intencional]] e separação de contextos são complementares:
- Compaction: comprime o histórico de uma sessão para reutilizar em outra
- Separação: garante que certas informações nunca entrem em determinadas sessões

## Extensão: Memória de Longo Prazo entre Sessões

Separação de contextos garante que sessões não se contaminem. [[memoria-de-longo-prazo-ia]] conecta essas sessões via arquivo persistido: o output do research é salvo como `.md` e serve de input para sessões futuras — sem re-explorar o codebase.

## Key Sources

- [[sources/erros-workflow-research-plan-implement]]
- [[sources/context-engineering-avancado-para-coding-agents]]
- [[wiki/sources/context-engineering-codebases-grandes-rpi]] — memória de longo prazo como extensão natural da separação de contextos; sub-agentes como implementação técnica confirmada
