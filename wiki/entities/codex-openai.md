---
type: entity
title: "Codex (OpenAI)"
aliases: ["Codex", "OpenAI Codex", "codex app"]
date_created: 2026-06-02
date_updated: 2026-07-31
source_count: 4
tags: [codex, openai, harness, ia-para-devs]
skill: tech-mentor-ai
status: stable
---

# Codex (OpenAI)

Harness de codificação da OpenAI, baseado nos modelos GPT-5.x. Considerado par do Claude Code no ranking dos melhores harnesses de codificação em 2026. Tem plano com reset a cada 5 horas, tornando-o competitivo em custo para uso intenso.

## Características

- **Modelo base**: GPT-5.5 / GPT-5.4 (escolhível pelo usuário)
- **Reset**: a cada 5 horas — limite semanal mas com reset frequente
- **Sem Auto Mode** (conforme demo de Nauke na Aula 05)
- **Reasoning levels**: Extra High, High, Medium, Low (selecionável)
- **Preferência de Nauke**: melhor para backend complexo e tarefas novas; reasoning mais denso que o Opus para código

## Contexto Histórico

A OpenAI não tinha harness de codificação próprio até ~2025 (apenas participação no GitHub Copilot como acionista). A virada veio com o GPT-5.1, que revelou que os modelos O-series (alta density reasoning, fine-tuned para código) eram excelentes para desenvolvimento. O Codex consolidou essa posição.

## Comparação com Claude Code

| Aspecto | Codex | Claude Code |
|---|---|---|
| Modelo | GPT-5.x | Claude (Opus/Sonnet) |
| Inovação de harness | Alta | Referência do mercado |
| Custo | Reset 5h | Reset 5h |
| Preferência | Backend complexo (Nauke) | Frontend/design (Nauke) |

## Suporte Nativo a Worktree (App)

Segundo [[wiki/sources/git-worktree-paralelismo-ia-codex-claude-abacus]], o app do Codex (não a CLI) oferece suporte nativo a `git worktree`: opções "new worktree" e "create permanent worktree" no painel do projeto. Ao contrário do [[wiki/entities/claude-code]], que guarda a worktree em `.claude/worktrees/` dentro do repositório, o Codex guarda a sua fora da pasta do repositório — local exato não confirmado, o próprio autor da fonte se corrige ao vivo sobre onde exatamente ela fica. Ver [[wiki/concepts/worktree-paralelismo]].

## Key Sources

- [[wiki/sources/formacao-ia-devs-aula-04-harness]]
- [[wiki/sources/formacao-ia-devs-aula-05-hands-on]]
- [[wiki/sources/formacao-ia-devs-aula-03-llm]]
- [[wiki/sources/git-worktree-paralelismo-ia-codex-claude-abacus]] — suporte nativo a worktree no app ("new worktree" / "create permanent worktree")
