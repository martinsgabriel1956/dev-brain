---
type: concept
title: "Closed-Loop Skill Learning System"
aliases: ["learning loop de agente", "skill learning loop", "auto-geração de skills"]
date_created: 2026-07-21
date_updated: 2026-07-21
source_count: 1
tags: [tech-mentor-ai, learning-loop, skills-agente, hooks-agente, hermes-agent, pattern-extraction]
skill: tech-mentor-ai
status: draft
---

# Closed-Loop Skill Learning System

Ciclo de aprendizado usado pelo Hermes Agent (ver [[wiki/sources/hermes-agent-open-claw-learning-loop]]) para transformar o histórico de tarefas de um agente em skills reutilizáveis, sem intervenção manual do desenvolvedor a cada padrão identificado. Não é [[wiki/concepts/prompt-engineering|prompt engineering]] nem "o modelo ficando mais inteligente" — é o agente reescrevendo sua própria base de conhecimento persistida, sempre sob permissão do usuário.

## As Cinco (ou Seis) Etapas

1. **Task completion** — dispara ao fim de cada tarefa; é o gatilho do loop.
2. **Pattern extraction** — analisa os passos dados na tarefa e identifica o que se repete em tarefas parecidas. Implementável hoje, de forma manual, com [[wiki/concepts/hooks-agente|hooks]] de fim de sessão que alimentam uma chamada de LLM geradora de padrões.
3. **Skill creation** — converte o padrão identificado em uma nova skill (ver [[wiki/concepts/skills-agente]]). Etapa que várias empresas já fazem manualmente hoje; automatizada no Hermes.
4. **Skill refinement** — mescla, simplifica ou descarta skills sobrepostas/redundantes conforme o banco de skills cresce. Apontado como o passo mais difícil de escalar manualmente (mencionado explicitamente como dor pessoal do autor da fonte).
5. **Periodic audit** — a cada ~15 tarefas, o agente se autoavalia e decide o que persistir e por quanto tempo (citando um TTL configurável), documentado no `agents.md` do projeto.

## Por que Isso Importa

Resolve o problema descrito no gancho da fonte: repetir manualmente, a cada nova sessão/janela de contexto, as mesmas instruções de projeto (ex.: "usamos PNPM, não NPM"; "nunca rode Prisma Migrate sem X"). Em vez de crescer indefinidamente um `CLAUDE.md`/`AGENTS.md` estático, o loop gera e cura esse conhecimento incrementalmente.

## Limite: Ganho Estritamente Específico de Domínio

Skills geradas por este loop nascem **super específicas** — ex.: "sumarizar uma PR do GitHub". Não generalizam para tarefas de julgamento maior, como planejar uma migração de banco de dados a partir do histórico de PRs. Útil para os ~80% de trabalho repetitivo do dia a dia; não substitui decisão arquitetural.

## Relação com Outros Conceitos

- [[wiki/concepts/agent-memory-tres-camadas]] — este loop popula especificamente a camada de skill memory
- [[wiki/concepts/skills-agente]] — skill como unidade de saída do loop; ver especialmente a seção "Caso: Skill como Contexto Pessoal Persistente" para outro exemplo de skill gerada/curada fora de codificação pura
- [[wiki/concepts/hooks-agente]] — mecanismo hoje disponível para implementar manualmente as etapas 2–4 antes de existir automação dedicada
- [[wiki/concepts/harness]] — o loop é um recurso de harness, comparável a "dream consolidation" já citado em [[wiki/entities/claude-code]]

## Key sources

- [[wiki/sources/hermes-agent-open-claw-learning-loop]]
