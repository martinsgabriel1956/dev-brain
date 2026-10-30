---
type: concept
title: "REVIEW.md"
aliases: ["review.md", "colinha do revisor", "arquivo de instruções do revisor"]
date_created: 2026-10-26
date_updated: 2026-10-26
source_count: 2
tags: [code-review, claude-code, review-md, agentes, harness, context-engineering]
skill: tech-mentor-ai
status: draft
---

# REVIEW.md

Arquivo mantido pelo **dono do código** que diz ao agente revisor **o que importa** naquele repositório — a "colinha" do revisor, irmã do [[wiki/concepts/claude-md|CLAUDE.md]]: o CLAUDE.md ensina a *escrever*, o `REVIEW.md` ensina a *revisar*.

## O que contém (exemplos da Anthropic)

- Descreve o **smell**, não uma regra de código: em **documentação** a falha é *mentir* (README diz que a config vem ligada por padrão e não vem); em **configuração**, é *apontar para o lugar errado* (produção em vez de staging/dev).
- Exige **arquivo e linha como prova** em cada comentário.
- **Limita nitpicks** por PR.
- Registra **falsos positivos** recorrentes para o revisor parar de reclamar (ex.: ignorar formatação em tal tipo de arquivo).

## Ciclo de retroalimentação

Achado repetido em vários PRs → pergunta: é erro real? **Sim** → vira regra de lint, linha no CLAUDE.md ou skill (corrigir o harness, não o PR); **não (falso positivo)** → linha no `REVIEW.md`. Ver [[wiki/concepts/harness-de-qualidade]].

## Relações

- Origem anterior no wiki: [[wiki/concepts/claude-md]] (seção sobre `review.md`) e [[wiki/concepts/code-review]] (arquivo dedicado recomendado pela Anthropic).
- Destino do aprendizado da amostragem em [[wiki/concepts/matriz-risco-dificuldade-review-ia]].
- Usado pela camada 3 de [[wiki/concepts/revisao-em-camadas-queijo-suico]] e pelo [[wiki/concepts/consenso-multiagente-em-code-review]].

## Key sources

- [[wiki/sources/anthropic-code-review-por-agentes-sete-camadas]] — exemplos oficiais (doc mentindo, config no lugar errado) e o ciclo erro-repetido → regra
- [[wiki/sources/ninguem-mais-revisa-codigo-ia-migracao-review-galego]] — `review.md` como CLAUDE.md do revisor
