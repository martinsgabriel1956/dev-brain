---
type: concept
title: "Progressive Disclosure para IA"
aliases: ["progressive disclosure", "entrega gradual de contexto", "context by directory"]
date_created: 2026-06-01
date_updated: 2026-08-20
source_count: 2
tags: [context-engineering, coding-agents, on-demand-loading, claude-md, cursor-rules]
skill: tech-mentor-ai
status: draft
---

# Progressive Disclosure para IA

Estratégia de organizar arquivos de contexto (guidelines, regras, documentação) de forma que o agente **descubra e carregue gradualmente** apenas o que é relevante para a tarefa atual — em vez de receber tudo de uma vez.

## O problema que resolve

Um `CLAUDE.md` ou `agents.md` monolítico na raiz carrega todas as regras do projeto em toda sessão. Isso viola o [[instruction-budget]] e empurra o agente para a [[dumb-zone]] antes mesmo de começar a trabalhar.

## Implementação: arquivos por responsabilidade e diretório

```
/                          ← raiz
├── CLAUDE.md              ← base mínima (sempre carregada)
├── .cursor/rules/
│   ├── architecture.mdc   ← always: true — carregada sempre
│   ├── feature-folders.mdc ← sob demanda: modificando módulos
│   └── ddd-strategic.mdc  ← sob demanda: dúvidas sobre design
├── billing/
│   └── GUIDELINES.md      ← carregada quando o agente toca billing/
├── identity/
│   └── GUIDELINES.md      ← carregada quando o agente toca identity/
└── content/
    └── GUIDELINES.md
```

O agente carrega o arquivo do módulo que está sendo alterado — não os de todos os módulos.

## On-Demand Loading com Cursor Rules e Claude Skills

Cursor Rules permitem configurar gatilhos de carregamento por arquivo:

```yaml
# Arquivo sempre ativo
alwaysApply: true

# Carregado quando o agente identifica a necessidade
alwaysApply: false
trigger: "criando ou modificando módulos / dúvidas sobre design patterns"

# Carregado apenas quando explicitamente invocado
alwaysApply: false
trigger: "quando o usuário pedir 'identify domains' no chat"
```

Claude Skills seguem a mesma lógica. `agents.md` padrão é menos flexível — não tem gatilhos configuráveis.

## Relação com [[instruction-budget]]

Progressive disclosure é a implementação prática do orçamento de instruções: manter o total de instruções ativas bem abaixo do limite (~150–200) carregando apenas o que a tarefa atual requer.

## Analogia: o Mapa Antes da Rua

[[wiki/sources/engenharia-de-contexto-vs-prompt-engineering-gargalo-real-times-ia]] descreve a mesma lógica com uma imagem simples: "mais contexto não é melhor contexto — se você despeja tudo na janela, o essencial acaba afogando no acessório". O modelo deve receber primeiro uma visão geral sempre presente (o mapa) e só depois os detalhes específicos da tarefa (a rua onde ele vai trabalhar de fato) — reafirmando, sem contradizer, a estrutura de arquivos por diretório/responsabilidade já descrita acima.

## Relação com outros conceitos

- [[claude-md]] — o arquivo principal é o ponto de entrada; progressive disclosure distribui o resto
- [[instruction-budget]] — progressive disclosure mantém o orçamento baixo
- [[on-demand-loading]] — o mecanismo técnico que viabiliza progressive disclosure em ferramentas modernas
- [[separacao-de-contextos]] — sessões separadas é o equivalente temporal; progressive disclosure é o equivalente espacial

## Key sources

- [[wiki/sources/context-engineering-codebases-grandes-rpi]] — demonstração prática com codebase de streaming; Cursor Rules com alwaysApply e gatilhos
- [[wiki/sources/agents-md-vale-a-pena-paper-zurique]] — links para arquivos específicos como estratégia de custo
- [[wiki/sources/engenharia-de-contexto-vs-prompt-engineering-gargalo-real-times-ia]] — analogia "mapa antes da rua" para dosagem de contexto
