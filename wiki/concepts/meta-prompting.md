---
type: concept
title: "Meta-Prompting"
aliases: ["meta prompting", "prompt template", "placeholder prompting"]
date_created: 2026-06-02
date_updated: 2026-06-02
source_count: 2
tags: [prompt-engineering, meta-prompting, template, xml-markdown]
skill: tech-mentor-ai
status: draft
---

# Meta-Prompting

Técnica de estruturação de prompts onde **placeholders descritivos** indicam ao LLM o que deve ser preenchido em cada seção — em vez de passar o valor final diretamente. O prompt descreve *como* preencher, não o conteúdo. Frequentemente combinado com [[wiki/concepts/xml-markdown-prompts|XML+Markdown]].

## Conceito

```
# Sem meta-prompting
Requisitos: o usuário deve ver temperatura, umidade e vento

# Com meta-prompting
## Requirements
[placeholder: liste os requisitos funcionais da <task>, incluindo campos de dados exibidos, 
ações do usuário e comportamentos esperados]
```

No segundo caso, o LLM usa a instrução do placeholder para **raciocinar ativamente** sobre o que preencher, em vez de simplesmente aceitar o valor passado. Isso elicita output mais completo e mais alinhado.

## Por Que Funciona

O modelo trata cada placeholder como uma subtarefa de raciocínio. Em vez de apenas registrar "temperatura, umidade, vento", ele vai inferir: "o que mais pertence a 'requisitos funcionais' de um painel de clima?" → sugere 7 dias de previsão, geolocalização, responsividade, etc.

É equivalente a dar ao modelo um **briefing criativo** em vez de uma lista fechada.

## Sintaxe Típica

```
[placeholder: <instrução do que preencher aqui>]
[constraint: <instrução de restrição a ser aplicada>]
[note: <aviso ou boa prática a considerar>]
```

## Combinação com XML+Markdown

O padrão mais eficaz combina:
1. **Tags XML** para separar seções e criar referências reutilizáveis (`<task>`, `<context>`)
2. **Markdown** para estrutura visual e hierarquia
3. **Meta-prompting** dentro das seções para elicitar conteúdo inteligente

Ver [[wiki/concepts/xml-markdown-prompts]] para o padrão combinado completo.

## Aplicação ao Plan Mode

No [[wiki/concepts/plan-mode|plan mode]], o meta-prompting é usado para construir specs iterativamente: o LLM preenche os placeholders, o dev revisa, adiciona restrições, e itera. O template garante que nenhuma seção importante seja omitida.

## Key Sources

- [[wiki/sources/formacao-ia-devs-aula-05-hands-on]]
- [[wiki/sources/formacao-ia-devs-aula-04-harness]]
