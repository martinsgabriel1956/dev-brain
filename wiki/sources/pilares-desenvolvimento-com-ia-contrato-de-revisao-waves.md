---
type: source
title: "Pilares do Desenvolvimento com IA: Harness, Contrato de Revisão e Waves"
aliases: ["pilares do desenvolvimento com ia", "contrato de revisão auditável", "waves e contrato de revisão"]
date_created: 2026-09-29
date_updated: 2026-09-29
source_count: 0
tags: [tech-mentor-ai, harness, spec-driven-development, contrato-de-revisao, revisao-por-ia, waves, paralelismo, quality-gate, fitness-functions, memory-rot, skills, mcp, claude-code, produtividade]
skill: tech-mentor-ai
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/pilares-desenvolvimento-com-ia-contrato-de-revisao-waves.md
source_url: ""
author: "desconhecido (aula/vídeo PT-BR; possivelmente [[wiki/entities/wesley-willians]] / MBA [[wiki/entities/full-cycle]] — não confirmado)"
date_published: ""
date_ingested: 2026-09-29
---

# Pilares do Desenvolvimento com IA: Harness, Contrato de Revisão e Waves

## TL;DR

O instrutor lista os **pilares** que um dev precisa dominar para trabalhar melhor com IA — ferramentas/[[wiki/concepts/harness]], agentes especializados, escolha de modelo, documentação, [[wiki/concepts/agent-memory-tres-camadas|memória]] (com o risco de [[wiki/concepts/memory-rot]]), local de execução, [[wiki/concepts/skills-agente|skills]] e [[wiki/concepts/model-context-protocol|MCPs]] em quantidade adequada ([[wiki/concepts/pilares-de-desenvolvimento-com-ia]]). Depois demonstra ao vivo o **workflow básico** (spec → IA implementa → revisão) num Kanban feito "no go horse" e aponta quatro falhas: sem harness, tempo parado olhando a IA, sem mecanismo de revisão e ciclo manual de correção de bugs. A alternativa que defende é um **contrato de revisão auditável** ([[wiki/concepts/contrato-de-revisao]]) — com pré-requisitos de ambiente, estado inicial de teste, *quality gates* e rastreabilidade por critério de aceitação — lido por um **revisor independente** do implementador ([[wiki/concepts/revisao-por-agente-independente]]), e a organização do trabalho em **waves** paralelas ([[wiki/concepts/waves-de-desenvolvimento]]) para que dez tarefas andem sem conversa constante com a IA.

## Key Claims

1. **Sete pilares** (ferramentas/harness, modelos, documentação/artefatos, memória, local de execução, skills, MCPs) determinam a clareza ao desenvolver com IA; dominá-los torna o dev "mais intencional". Evidência: enumeração na abertura; sem dados quantitativos. → [[wiki/concepts/pilares-de-desenvolvimento-com-ia]]
2. **IDEs e CLIs são o harness; agentes podem ser especializados** (definir os próprios agentes dá intenção quanto ao domínio do problema). → [[wiki/concepts/harness]], [[wiki/concepts/subagentes]], [[wiki/entities/claude-code]]
3. **Memória evita repetição do mesmo erro, mas envelhece** ("memory rot": deixa de refletir o estado do software). → [[wiki/concepts/memory-rot]], [[wiki/concepts/agent-memory-tres-camadas]]
4. **Skills:** a diferença entre uma boa e uma ruim é grande, e há **falsa sensação de saber criar uma skill decente**, gerando frustração. → [[wiki/concepts/skills-agente]]
5. **MCPs:** poucos e adequados, porque inicializar muitos servidores consome janela de contexto. → [[wiki/concepts/model-context-protocol]], [[wiki/concepts/context-window]]
6. **O workflow básico funciona, mas produz problemas de qualidade/segurança** que só aparecem depois. Evidência: demo do Kanban (Next.js + Tailwind + SQLite + Prisma) com Sonnet/effort high, sem CLAUDE.md nem plano; o próprio autor chama de "go horse". → [[wiki/concepts/spec-driven-development]], [[wiki/concepts/vibe-coding]]
7. **Ficar parado olhando a IA programar gera ansiedade e dúvida sobre produtividade real**; paralelizar com git/worktree ajuda mas não elimina a sensação. → [[wiki/concepts/token-anxiety]], [[wiki/concepts/ativo-vs-produtivo]], [[wiki/concepts/worktree-paralelismo]]
8. **O agente que implementou não deve ser o que revisa** ("orgulho ferido"); a IA revisora costuma declarar "pronto para produção". Revisão por IA funciona **com processo completo**; revisar algo que não está claro para ser revisado não é revisão completa (afirmado como experiência do autor com múltiplos workflows/ferramentas). → [[wiki/concepts/revisao-por-agente-independente]], [[wiki/concepts/code-review]]
9. **Contrato de revisão auditável:** implementador cumpre, revisor verifica; contém tudo para revisar **sem contexto do projeto** — runtime, estado inicial (usuários/arquivos), browser real via Playwright CLI, gates, critérios de aceitação e superfícies (HTTP, UI, protocolos). Ferramentas de SDD, segundo o autor, não trazem contrato de revisão. → [[wiki/concepts/contrato-de-revisao]], [[wiki/concepts/spec-driven-development]]
10. **Gates de qualidade** são onde "o harness entra forte": script de linter/dependências/arquitetura/camadas (regra de negócio no controller falha), Knip para código slop, dependência circular e organização de arquivos = [[wiki/concepts/fitness-functions]]. → [[wiki/concepts/quality-gate]], [[wiki/concepts/harness-de-qualidade]]
11. **Waves:** quebrar por features/histórias, gerar spec por tarefa e rodar em paralelo (ex.: tarefas 4, 7 e 12), cada uma gerando PR e agentes que se autorrevisam; dá clareza de paralelismo, spec decente e contrato claro. O plano é dividido em **etapas, não lista de tarefas**. → [[wiki/concepts/waves-de-desenvolvimento]], [[wiki/concepts/paralelismo-de-tarefas-ia]]
12. **Mudança de mentalidade:** a IA é tão rápida que o multitarefa mental não acompanha; é preciso desenhar um fluxo onde ~10 tarefas andem sem conversa constante. → [[wiki/concepts/ativo-vs-produtivo]]

## Entidades Mencionadas

- [[wiki/entities/claude-code]] — CLI usada na demo (Sonnet, effort high, `/clear`).
- [[wiki/entities/full-cycle]] / [[wiki/entities/wesley-willians]] — possível origem (referência a "o MBA" e o nome "Wesley" na fala); **não confirmado**.
- [[wiki/entities/github]] — pipeline de CD e remote control citados como locais de execução.
- Next.js, Tailwind, SQLite, Prisma, Playwright CLI, Knip, Trello — stack/ferramentas citadas; sem página própria.

## Conceitos Tocados

Criados: [[wiki/concepts/pilares-de-desenvolvimento-com-ia]], [[wiki/concepts/contrato-de-revisao]], [[wiki/concepts/revisao-por-agente-independente]], [[wiki/concepts/waves-de-desenvolvimento]], [[wiki/concepts/memory-rot]].

Atualizados: [[wiki/concepts/harness]], [[wiki/concepts/spec-driven-development]], [[wiki/concepts/worktree-paralelismo]], [[wiki/concepts/code-review]], [[wiki/concepts/fitness-functions]], [[wiki/concepts/quality-gate]], [[wiki/concepts/agent-memory-tres-camadas]], [[wiki/concepts/skills-agente]], [[wiki/concepts/ativo-vs-produtivo]], [[wiki/concepts/model-context-protocol]], [[wiki/concepts/subagentes]], [[wiki/concepts/token-anxiety]], [[wiki/concepts/paralelismo-de-tarefas-ia]], [[wiki/concepts/harness-de-qualidade]], [[wiki/concepts/vibe-coding]].

## Open Questions

- **Transcrição truncada** no fim (frase cortada em "…da forma que eu gostaria h"): o fecho da aula, incluindo eventual resultado da execução da feature 04, não está disponível.
- **Inconsistência do exemplo:** a stack anunciada é SQLite + Prisma, mas o contrato mostrado cita PostgreSQL e uma plataforma de vídeo (MP4/thumbnail) — provavelmente é um contrato de outro projeto usado como ilustração. Interpretação minha (inferência).
- **Sem evidência empírica** de que o contrato + waves supera o workflow básico (nem tempo, custo ou taxa de bugs); a autoridade é a experiência do autor com "múltiplos workflows e ferramentas".
- A afirmação de que ferramentas de SDD "não têm contrato de revisão" é genérica e não verificada; [[wiki/concepts/criterios-de-uma-boa-spec]] e [[wiki/concepts/spec-driven-development]] podem já cobrir parte disso — comparar em lint.
- O argumento do "orgulho ferido" antropomorfiza o agente; o mecanismo mais plausível (viés de confirmação do mesmo contexto/janela) não é discutido na fonte [skill: tech-mentor-ai — inferência]. Ver [[wiki/concepts/separacao-de-contextos]].
- Em [skill: tech-mentor-ai] `references/ai/agent-harness-engineering.md`, a recomendação de 2026 é **simplificar** harness/scaffolding para modelos modernos; a fonte prega mais gates e scripts. Não é contradição (gates de verificação ≠ scaffolding de raciocínio), mas vale medir o custo de manutenção dos gates.
- Não é dito **como mitigar o memory rot** (a fonte só nomeia o problema); ver [[wiki/concepts/memory-rot]].
- Nenhuma métrica de custo/tokens das waves; ver [[wiki/sources/agent-waves-custo-modelos-fortes-fracos-kimi]] para o outro uso do termo "waves".

## Raw Quotes

> "O mesmo agente que programou não vai ser o mesmo agente que revisou, porque o cara que programou vai ficar com orgulho ferido e vai falar que o que ele fez foi bem."

> "Revisar algo que não está claro para ser revisado não é uma revisão completa."

> "O contrato vai ter tudo que precisa para que esse cara revise sem entender nada do contexto do projeto."

> "A gente sempre foi acostumado a fazer uma tarefa de cada vez. Agora eu posso fazer 10 de cada vez, então a nossa cabeça tem que mudar e pensar como organizar um fluxo onde consigo fazer essas 10 tarefas sem ter que ficar o tempo inteiro falando com a IA."

> "O que a gente está fazendo agora é um processo improdutivo que não tem consistência para funcionar ao longo do tempo."
