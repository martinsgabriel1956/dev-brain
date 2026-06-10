---
type: concept
title: "Worktree e Paralelismo de Tarefas"
aliases: ["worktree parallelism", "git worktree IA", "paralelismo de tarefas ia"]
date_created: 2026-06-02
date_updated: 2026-06-09
source_count: 4
tags: [worktree, paralelismo, git, spec-driven, produtividade]
skill: tech-mentor-ai
status: stable
---

# Worktree e Paralelismo de Tarefas

Estratégia de trabalho que usa `git worktree` para criar ambientes de desenvolvimento isolados, permitindo que múltiplas tarefas rodem em paralelo — cada uma num contexto separado — enquanto o dev planeja a próxima ou descansa.

## O Problema que Resolve

No modelo L2 (babysitting), o dev aprova cada passo da IA e só começa a próxima tarefa quando a anterior termina. Com tarefas que levam 30–90 minutos cada, o idle é imenso. O worktree quebra essa serialização.

## Como Funciona

Um `git worktree` cria um segundo checkout do mesmo repositório em outro diretório, apontando para um branch diferente. É como fazer `git clone projeto projeto_2` — o mesmo histórico, mas working directory isolado.

```bash
git worktree add ../projeto-feature-a feature/checkout
git worktree add ../projeto-feature-b feature/notificacoes
```

Cada worktree pode ter um agente IA rodando independentemente, sem afetar o outro.

## Workflow do L3

1. Escrever spec da tarefa A → iniciar execução no worktree A → escrever spec da tarefa B → iniciar execução no worktree B → revisar resultado de A enquanto B roda → etc.
2. Resultado: tasks rodando em paralelo em ambientes isolados. "Não quer dizer que tudo acontece ao mesmo tempo, no mesmo lugar. As coisas estão acontecendo em batches diferentes."

## Limitações

- **Banco de dados compartilhado**: se as duas worktrees tocam no mesmo schema, uma migração aplicada numa worktree não está na outra. Requer disciplina ou ambientes Docker isolados.
- **Não é paralelismo de etapas da mesma tarefa**: funciona para tarefas independentes. Não faz sentido paralelizar "implemente" e "teste" da mesma feature — uma depende da outra.
- **Carga mental**: gerir múltiplas worktrees exige organização. Ferramentas como Compose (Pedro Nauke) ajudam a orquestrar.

## Paralelismo Extremo (Pedro Nauke)

Pedro chegou a rodar 6 contas simultâneas (3 Codex + 3 Claude Code) para desenvolver o Compose, cujo ciclo de test/verify é muito intenso. Hoje com sandboxes isoladas (Daytona, a2b) isso fica mais seguro e controlado.

## Relação com Ferramentas

- **Compose** (Nauke): orquestrador spec-driven que gerencia worktrees e integra com Code Rabbit
- **Sandboxes** (Daytona, a2b): ambientes virtualizados que resolvem o problema do banco compartilhado
- **Devin**: usa VM completa por task — a versão comercial/cara do mesmo conceito

## Paralelismo Real no Cursor (2026)

Confirmação de campo: cada feature full stack no Cursor dispara ~5 Claude agents simultâneos + 1 agente de code review + a engenheira validando. O tech lead do Databricks usa os intervalos entre reuniões para disparar 2–3 agents e revisar PRs nos blocos livres. Esses padrões confirmam que o paralelismo não é teórico — é o fluxo diário de [[product-engineer|product engineers]] em empresas de ponta.

## Key Sources

- [[wiki/sources/formacao-ia-devs-aula-02-mercado-perfil-profissional]]
- [[wiki/sources/formacao-ia-devs-aula-04-harness]]
- [[wiki/sources/formacao-ia-devs-aula-06-qa]]
- [[wiki/sources/product-engineer-vale-do-silicio-2026]]
