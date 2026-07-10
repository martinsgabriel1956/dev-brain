---
type: concept
title: "Good First Issue"
aliases: ["boa primeira issue", "ponto de entrada na codebase", "first task"]
date_created: 2026-06-20
date_updated: 2026-07-10
source_count: 2
tags: [onboarding, codebase, open-source, contribuicao, carreira]
skill: tech-mentor-leadership
status: stable
---

# Good First Issue

Tarefa de entrada deliberadamente escolhida para que um dev aprenda a codebase enquanto contribui de verdade — não uma tarefa trivial de limpeza, mas uma que toca componentes centrais do sistema.

## Critério de seleção

Uma boa primeira issue para aprender a codebase deve:
- Tocar funcionalidade **core** do produto (não periférica)
- Ter **escopo claro** e impacto real
- Forçar o dev a entender um **fluxo completo** (evento → estado → render)
- Ser pequena o suficiente para completar em dias, não semanas

**Não confundir com:** tarefas de estilo, TODOs antigos, renomeações — essas ensinam pouco sobre o sistema.

## Exemplo prático

No Excalidraw: "adicionar opção de retângulo com bordas arredondadas" força entender como formas são criadas, adicionadas ao estado e renderizadas — um caminho completo pelo core do sistema.

## Quando não há time para sugerir uma tarefa

Invente uma com o critério acima. Pergunte: "Qual feature pequena toca o coração da aplicação e me força a entender o fluxo principal?"

## Perspectiva do tech lead

Do lado de quem faz onboarding de outros, sempre manter 2-3 issues marcadas como `good-first-issue` no backlog. Ver [[wiki/concepts/onboarding-de-codebase]] para o protocolo completo.

## Perspectiva de quem contribui de fora

Além do uso interno de onboarding em times, `good first issue`/`good first fix` também funciona como ponto de entrada padrão no GitHub para quem quer [[wiki/concepts/contribuir-open-source|contribuir com open source]] em projetos de terceiros que já usa no dia a dia — mesmo critério de escopo pequeno e core do produto, aplicado de fora para dentro em vez de dentro de um time.

## Key sources

- [[wiki/sources/como-aprender-novas-codebases]]
- [[wiki/sources/5-recursos-para-ser-um-desenvolvedor-melhor]]
