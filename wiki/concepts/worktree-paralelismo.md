---
type: concept
title: "Worktree e Paralelismo de Tarefas"
aliases: ["worktree parallelism", "git worktree IA", "paralelismo de tarefas ia"]
date_created: 2026-06-02
date_updated: 2026-07-31
source_count: 9
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

## `claude --worktree`: Wrapper Nativo no Claude Code

O [[wiki/entities/claude-code]] embutiu o fluxo como comando de primeira classe: `claude --worktree <nome>` cria a cópia do repositório automaticamente em `.claude/worktrees/<nome>`, sem precisar rodar `git worktree add` manualmente. Cada sessão do Claude aberta numa worktree diferente trabalha em cópias físicas dos arquivos — dois agentes podem editar o "mesmo" arquivo lógico (mesmo path) sem gerar conflito, porque fisicamente são arquivos distintos.

Boa prática documentada no `CLAUDE.md`: instruir o agente a **encerrar a worktree** ao finalizar as alterações (commit → encerrar worktree → abrir PR) — caso contrário, os arquivos da cópia podem acabar sendo commitados junto ao repositório principal se não estiverem no `.gitignore`.

## Worktree vs. Subagente

Worktree é paralelismo a nível de **file system** (cópias físicas, PRs separadas). Ver [[wiki/concepts/subagentes]] para o paralelismo equivalente a nível de **janela de contexto** (resultado convergido numa única PR). Regra prática: tarefas independentes que virarão entregas separadas → worktree; uma tarefa grande dividida em partes que convergem para uma única entrega → subagente.

## Paralelismo Real no Cursor (2026)

Confirmação de campo: cada feature full stack no Cursor dispara ~5 Claude agents simultâneos + 1 agente de code review + a engenheira validando. O tech lead do Databricks usa os intervalos entre reuniões para disparar 2–3 agents e revisar PRs nos blocos livres. Esses padrões confirmam que o paralelismo não é teórico — é o fluxo diário de [[product-engineer|product engineers]] em empresas de ponta.

## Demonstração Manual Completa: `add` / `list` / `remove -f`

[[wiki/sources/git-worktree-paralelismo-ia-codex-claude-abacus]] demonstra ao vivo o ciclo de vida completo de uma worktree criada manualmente:

```bash
git worktree add ../feature-a -b feature-a   # cria fora do repositório, um nível acima
git worktree list                             # lista todas as worktrees ativas
git worktree remove <caminho>                 # recusa/avisa se há mudanças não commitadas
git worktree remove -f <caminho>              # força remoção, descartando mudanças pendentes
```

Recomendação registrada na fonte: criar a pasta da worktree **fora** do repositório (`../feature-a`) é a abordagem mais simples; a alternativa é uma pasta ignorada pelo Git dentro do próprio repositório — que é justamente o que o [[wiki/entities/claude-code]] faz nativamente (`.claude/worktrees/`).

## Codex: App Nativo vs. Claude Code — Onde Cada Um Guarda a Worktree

A mesma fonte compara lado a lado o suporte nativo de duas ferramentas:

| Ferramenta | Comando/UI | Onde guarda |
|---|---|---|
| [[wiki/entities/codex-openai]] (app) | "new worktree" / "create permanent worktree" | Fora da pasta do repositório — local exato não confirmado, o próprio autor se contradiz ao vivo sobre isso `[transcrição incerta]` |
| [[wiki/entities/claude-code]] | `claude --worktree <nome>` | `.claude/worktrees/<nome>`, dentro do repositório |

Ao encerrar a sessão (`/quit`), o Claude Code pergunta explicitamente se o usuário quer manter a worktree — confirmação direta do comportamento já registrado na seção anterior sobre encerramento explícito.

## Worktree Cross-Repo em Microfrontends

[[wiki/sources/impacto-ia-mercado-frontend]] descreve uma variante do problema em arquiteturas de microfrontends/múltiplos repositórios: como o worktree isola uma cópia de working directory mas não o contexto de outro repositório, o dev precisa linkar manualmente o worktree/PR do backend ao worktree/PR do frontend para sinalizar a interface entre eles — trabalho de coordenação que um monorepo não exige, porque ali o mesmo contexto já contém os dois lados. Ver [[wiki/concepts/monorepo-vs-microfrontends-ia]].

## Key Sources

- [[wiki/sources/formacao-ia-devs-aula-02-mercado-perfil-profissional]]
- [[wiki/sources/formacao-ia-devs-aula-04-harness]]
- [[wiki/sources/formacao-ia-devs-aula-06-qa]]
- [[wiki/sources/product-engineer-vale-do-silicio-2026]]
- [[wiki/sources/multiplos-agentes-worktrees-subagentes-claude-code]]
- [[wiki/sources/impacto-ia-mercado-frontend]]
- [[wiki/sources/system-design-simulador-hotel-booking-replit]] — [[wiki/entities/replit|Replit]] expõe esse padrão na UI como "workers": uma sessão principal roda uma tarefa maior enquanto subtarefas paralelas de colaboradores rodam isoladas, com merge automático de volta e resolução de conflitos pelo próprio harness — hipótese do autor de que é `git worktree` por baixo dos panos, mas sem confirmação técnica
- [[wiki/sources/git-worktree-paralelismo-ia-codex-claude-abacus]] — demonstração completa de `git worktree add`/`list`/`remove -f` no terminal; comparação lado a lado de onde Codex (app) e Claude Code guardam a worktree criada nativamente
- [[wiki/sources/spec-driven-development-otimizando-contexto-agentes]] — o artefato de "estado" de um projeto spec-driven permite fatiar o trabalho em múltiplos pull requests sem perder rastreabilidade das decisões já tomadas
