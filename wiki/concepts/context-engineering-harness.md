---
type: concept
title: "Context Engineering (nível Harness)"
aliases: ["context engineering harness", "engenharia de contexto", "project knowledge ia"]
date_created: 2026-06-02
date_updated: 2026-06-02
source_count: 6
tags: [context-engineering, harness, rules, skills, project-knowledge]
skill: tech-mentor-ai
status: draft
---

# Context Engineering (nível Harness)

Prática de estruturar e disponibilizar o **conhecimento do projeto** para o agente de forma que ele precise fazer menos exploração e produza resultados mais alinhados. É a evolução do prompt engineering: em vez de instruções por prompt, o contexto relevante é persistente via rules, skills, CLAUDE.md e referências de arquivos.

## A Metáfora da Bússola

A LLM não conhece seu projeto. Sem context engineering, ela é um explorador no mato sem bússola: vai lendo arquivo por arquivo até encontrar o que precisa (7 tool calls para corrigir 1 bug). Com context engineering, ela tem um mapa: "tudo relacionado a desconto está em `src/domain/coupon.ts`; regras de negócio ficam no service; persistência no repository".

## Evolução

```
Prompt Engineering
       ↓
Context Engineering  ← você está aqui
       ↓
Harness Engineering
```

- **Prompt Engineering**: como estruturar um prompt individual
- **Context Engineering**: como gerenciar o que entra no contexto ao longo do tempo e das sessões
- **Harness Engineering**: como montar o ecossistema completo (tools, MCPs, subagents, CI/CD) ao redor do modelo

## Ferramentas de Context Engineering

### Rules (CLAUDE.md / .cursorrules)
Regras de projeto lidas em toda sessão. Ex: "componentes React devem ter no máximo 100 linhas", "regras de negócio ficam no domain model".

### Skills
Conjuntos de instruções para tarefas recorrentes. Ex: skill "criar slide" com todos os modelos de slide possíveis — cada novo slide inicia com contexto limpo mas carrega a skill. Evita repetir instruções em todo prompt.

### MCPs (Model Context Protocol)
Servidores que expõem tools/resources ao agente via protocolo padronizado. Ex: MCP do Figma para acessar designs; MCP do banco de dados para queries; 50+ tools da Adobe (liberadas em 2026).

### Progressive Disclosure
Ver [[wiki/concepts/progressive-disclosure-ia]] — arquivos de contexto por diretório.

### Memória de Longo Prazo
Ver [[wiki/concepts/memoria-de-longo-prazo-ia]] — salvar outputs de research como .md para reusar entre sessões.

## O Fator Decisivo de Qualidade

> "No fim das contas, o resultado vem de modelo, de harness, de técnica, e principalmente da formalização de conhecimento." — Rodrigo Branas

Usar Opus 4.7 ou GPT-5.5 sem context engineering produz resultados mediocres. Usar Kimi K2.6 com bom context engineering pode superar modelos mais caros. **A técnica e o contexto importam mais que o modelo.**

## Sensores vs Guias

O user harness divide-se em duas categorias (Branas, Aula 01 Parte 2):

- **Guias** — antecipam comportamento: rules, skills, MCPs, CLAUDE.md. Ver [[wiki/concepts/sensores-vs-guias]].
- **Sensores** — fornecem feedback: testes, linter, compilador, browser, banco, LLM de revisão.

> "Qualidade dos seus sensores faz a diferença no resultado." — Rodrigo Branas

## Rules vs Skills

| | Rules | Skills |
|---|---|---|
| Carregamento | Sempre inteira no system prompt | Só front-matter; corpo sob demanda |
| Escopo | Global e obrigatório | Contextual e sob demanda |
| Tamanho ideal | < 300 linhas | Sem limite |

Ver [[wiki/concepts/rules-agente]] e [[wiki/concepts/skills-agente]] para detalhes.

## Key Sources

- [[wiki/sources/formacao-ia-devs-aula-04-harness]]
- [[wiki/sources/formacao-ia-devs-aula-05-hands-on]]
- [[wiki/sources/context-engineering-codebases-grandes-rpi]]
- [[wiki/sources/formacao-ia-devs-aula-01-context-harness-engineering]]
- [[wiki/sources/formacao-ia-devs-aula-02-rules]]
- [[wiki/sources/formacao-ia-devs-aula-03-skills]]
