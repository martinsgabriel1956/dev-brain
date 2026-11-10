---
type: concept
title: "Paralelismo de Tarefas Ia"
aliases: []
date_created: 2026-09-22
date_updated: 2026-11-10
source_count: 5
tags: [paralelismo-de-tarefas-ia]
skill: tech-mentor-ai
status: draft
---

# Paralelismo de Tarefas Ia

Stub criado durante sweep de lint (links quebrados) a partir de referências em 2 página(s) da wiki — conteúdo completo pendente de ingest dedicado.

## Contexto das citações

- Em [[wiki/sources/formacao-ia-devs-aula-01-abertura]]: [[wiki/concepts/paralelismo-de-tarefas-ia]] — rodar múltiplas tasks simultâneas via worktree + spec
- Em [[wiki/sources/formacao-ia-devs-aula-02-mercado-perfil-profissional]]: [[wiki/concepts/paralelismo-de-tarefas-ia]]

## Pendências

Promovida de stub a draft com [[wiki/sources/claude-code-dicas-worktrees-paralelismo-rotinas-sessoes-remotas-output-estruturado]]; ainda sem ingest dedicado só ao tema.

## Modalidades de Paralelismo no Claude Code

As cinco formas de paralelizar no [[wiki/entities/claude-code]] (vários terminais, subagentes, Agents View, Agent Teams, workflows customizados) e as ressalvas de custo (~2x tokens) e de atenção humana estão em [[wiki/concepts/modalidades-de-paralelismo-claude-code]]. Ideia central da fonte: paralelizar aumenta o custo rápido e você continua sendo uma pessoa, então há um teto prático.

## Quando Ainda Não Dá Para Paralelizar

[[wiki/sources/fluxo-completo-feature-com-ia-design-doc-worktrees-valdemar-neto]] dá um critério: sem a infraestrutura base, "um vai tentar criar coisa do outro". Primeiro vem o setup; depois, tarefas independentes. O autor pede ao agente para apontar o paralelizável, mas descarta uma sugestão que dependia de um client inexistente. Ele também reconhece o custo de trocar de contexto.

## Key sources

- [[wiki/sources/fluxo-completo-feature-com-ia-design-doc-worktrees-valdemar-neto]] — infraestrutura base antes de paralelizar; sugestões do agente exigem revisão
- [[wiki/sources/pilares-desenvolvimento-com-ia-contrato-de-revisao-waves]] — conceito de waves e specs por tarefa para rodar 4, 7 e 12 em paralelo — ver [[wiki/concepts/waves-de-desenvolvimento]]
- [[wiki/sources/formacao-ia-devs-aula-01-abertura]]
- [[wiki/sources/formacao-ia-devs-aula-02-mercado-perfil-profissional]]
- [[wiki/sources/claude-code-dicas-worktrees-paralelismo-rotinas-sessoes-remotas-output-estruturado]] — modalidades de paralelismo, custo ~2x, limite de atenção
