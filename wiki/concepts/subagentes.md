---
type: concept
title: "Subagentes"
aliases: ["subagents", "sub-agentes", "Task tool", ".claude/agents"]
date_created: 2026-07-03
date_updated: 2026-09-03
source_count: 7
tags: [subagentes, claude-code, multi-agent, paralelismo, context-engineering, harness, list-agents, mensagens-cruzadas]
skill: tech-mentor-ai
status: draft
---

# Subagentes

Padrão de paralelismo **a nível de janela de contexto**: o agente principal ([[wiki/concepts/ciclo-agente|chat pai]]) delega uma tarefa a uma instância separada do modelo, que roda numa janela de contexto própria, executa sua tarefa isoladamente e retorna **apenas o resultado final** — o raciocínio intermediário e os tool calls do subagente não entram no contexto do agente pai.

No [[wiki/entities/claude-code]], isso é implementado pela tool `Task`/`Agent`: cada subagente é, na prática, um processo separado sendo lançado pelo processo pai.

## Diferença Central para Worktrees

| | Subagentes | [[wiki/concepts/worktree-paralelismo|Worktrees]] |
|---|---|---|
| Nível de paralelismo | Contexto (mesma janela do Claude) | File system (cópia física do repo) |
| Resultado final | Convergido numa única síntese/PR | Branches e PRs separadas |
| Uso típico | Pesquisa, decisão, feature única dividida em partes (back+front+doc+teste) | Tarefas independentes que vão virar entregas separadas |
| Economia | De janela de contexto do agente pai | De conflito de arquivos entre agentes |

## Como Declarar um Subagente Customizado

Arquivo Markdown em `.claude/agents/*.md` (nível de projeto) ou equivalente a nível de usuário — mesma hierarquia de [[wiki/concepts/skills-agente|skills]] (usuário → projeto → diretório). Front-matter com nome, descrição (usada pelo Claude para decidir quando acionar) e cor; corpo com a instrução de comportamento.

Diferente de uma skill pura, um subagente pode fixar:

- **`model`** — ex.: Opus para um agente de Product Manager (decisões de maior peso), Sonnet para implementação, Haiku para documentação.
- **`tools`** — lista restrita de [[wiki/concepts/tool-call|tools]] disponíveis. Um subagente "code reviewer" só precisa de `Read`, `Grep`, `Glob`, `Bash` — sem `Write`/`Edit`, porque ele não escreve código, só analisa. Restringir tools reduz o system prompt do subagente e, por consequência, o custo em tokens.

## Padrão Orquestrador

Um subagente "CTO"/tech lead pode atuar como despachante de um time de subagentes especializados (backend, frontend, infra, product manager), cada um recebendo apenas as tarefas do seu domínio. Ver também o padrão Supervisor/Orchestrator em `references/ai/agents-orchestration.md` (skill `tech-mentor-ai`).

## Duas Formas de Disparo

1. **Automático** — o próprio modelo reconhece que uma tarefa é paralelizável (ex.: pesquisar 3 provedores de webhook ao mesmo tempo) e despacha subagentes via tool call, sem o usuário precisar nomear nenhum agente customizado.
2. **Explícito/customizado** — usuário ou prompt referencia diretamente o subagente pelo nome (ex.: "use o agente CTO"), garantindo que o roteamento não dependa da heurística automática do modelo.

**Risco observado:** com muitas skills e subagentes sobrepostos no mesmo projeto/usuário, o roteamento automático fica ambíguo — o modelo pode acionar uma skill genérica em vez do subagente customizado esperado, mesmo quando a descrição do subagente parecia cobrir o caso.

## Relação com Effort/Reasoning

Reasoning effort baixo pode impedir o reconhecimento de que uma tarefa é paralelizável — ver [[wiki/concepts/reasoning-level]]. O mesmo prompt disparou paralelismo automático só depois de subir o effort de low para high.

## Subagentes Como Executores num Loop Planner-Executor-Critic

Em vez de o usuário disparar cada subagente manualmente, um [[wiki/concepts/planner-executor-critic|Planner]] pode gerar dinamicamente o prompt de cada subagente (até dezenas em paralelo) junto com uma [[wiki/concepts/rubrica-de-verificacao|rúbrica]] de aceite, e um verificador (modelo distinto do executor) julga o resultado de cada subagente contra essa rúbrica antes de aceitar. Isso desloca o papel do subagente de "executor de tarefa nomeada pelo usuário" para "executor de tarefa gerada pelo sistema" — ver [[wiki/concepts/loop-engineering]].

## Disparo a Partir do Breakdown de Tasks de um Spec-Driven

Um caso concreto de disparo automático (não nomeado pelo usuário): ao executar um breakdown de tasks gerado por [[wiki/concepts/spec-driven-development|Spec-Driven Development]], o agente principal identifica quais tasks não têm dependência entre si e despacha um subagente por grupo paralelizável. Exemplo de campo: projeto de ~40 tasks executado com 4 subagentes rodando em paralelo, cada um cobrindo um subconjunto de tasks. Ver [[wiki/sources/spec-driven-development-otimizando-contexto-agentes]].

## Mensagens Cruzadas Entre Subagentes ("list agents")

Novidade documentada em [[wiki/sources/ia-2026-nao-e-so-prompt-nem-so-agente-codigo-fonte-tv]]: no [[wiki/entities/claude-code]], um subagente já não fica limitado a devolver resultado só ao agente pai — ele pode "promptar" diretamente outro agente disponível no mesmo contexto. O mecanismo descrito é um recurso de **listagem de agentes** que enumera todos os agentes endereçáveis naquele contexto; um subagente identifica qual é o mais adequado para resolver uma subtarefa, dispara mensagem para ele, e a execução pode continuar em paralelo (retomando depois) ou de forma sequencial.

Isso desloca o modelo de comunicação de "só o agente pai orquestra" para uma malha onde qualquer agente pode endereçar qualquer outro — mais próximo de comunicação peer-to-peer do que da hierarquia estrita "pai despacha, filho retorna resultado" descrita no restante desta página. A fonte não detalha o mecanismo de roteamento (como um agente decide qual outro é "o melhor" para a subtarefa) nem limites de profundidade de encadeamento (um agente B disparado por A pode disparar C?) — candidato a expansão se uma fonte técnica (changelog oficial, documentação) detalhar o comportamento exato.

## Padrão Organizador → Researchers → Builders → Reviewers

[[wiki/sources/graph-engineering-matematica-do-erro-composto]] descreve uma organização típica de subagentes num grafo: um **organizador** decompõe a tarefa, **researchers** rodam a pesquisa em paralelo, **builders** implementam, **reviewers** verificam o que foi feito — as arestas do grafo decidem quem espera por quem. Mesma ideia estrutural já registrada em [[wiki/sources/spec-driven-development-otimizando-contexto-agentes]] (4 subagentes em paralelo a partir do breakdown de tasks), com nomes de papel mais explícitos.

## Quanto Granular é Granular Demais: Um Benchmark de Campo

[[wiki/sources/subagentes-quando-vale-a-pena-custo-velocidade-tlc-spec-driven]] testa diretamente a pergunta "quantos subagentes uso?" com a mesma spec de 17 tasks (integração Stripe via TLC Spec Driven) rodada em quatro configurações:

| Cenário | Tempo | Tokens | Nota | Janela final do principal |
|---|---|---|---|---|
| Sem subagentes | ~15-19 min | ~9M | 0,93 | 74% |
| 1 subagente por task (17) | 43 min | 25M (+150%) | 0,81 | — |
| Agrupado por fases | 35 min | 15M | 0,90 | 32% |
| 3 subagentes (sweet spot) | 18 min | 10M | 0,95 | 26% |

**Achado central: granularidade excessiva não é um trade-off (mais caro, porém melhor) — é estritamente pior nos três eixos** (tempo, custo, qualidade) frente ao baseline sem subagente nenhum. A causa é a mesma já descrita acima em "Diferença Central para Worktrees" e no padrão orquestrador: cada subagente inicia sem contexto e recarrega arquivos do zero — com 17 tasks, isso é 17 recargas de contexto — e a fragmentação em tasks pequenas demais faz o subagente perder a noção do todo, derrubando a qualidade da implementação.

Já um agrupamento coeso em poucos subagentes (3, neste caso, agrupando ~6 tasks relacionadas por subagente) iguala ou supera o desempenho de um único agente em tempo, custo e qualidade, com o benefício adicional de terminar com a janela do agente principal muito mais livre (26% vs. 74%) — margem que importa para correções pós-implementação sem risco de degradação por janela cheia. O número "3" não é uma constante — é específico dessa spec de 17 tasks; a fonte recomenda replicar a metodologia (comparar granularidade do framework usado, agrupar de forma similar) em vez de aplicar literalmente esse número a qualquer projeto.

**Poluição da janela do principal escala com o número de subagentes, não com o volume de trabalho por subagente:** cada subagente retorna um output ao pai; mais subagentes (mesmo com menos trabalho cada) acumulam mais outputs na janela do principal.

### Duas Visões Divergentes da Indústria, Ambas Compatíveis com o Benchmark

- **Anthropic** (citada de segunda mão, sem link direto na fonte): multi-agente custa até 15× mais, mas acerta melhor em 90% dos casos — lógica de que um agente único rodando por muito tempo degrada. Esse número de custo não bate diretamente com o benchmark acima (onde o cenário mais caro teve a *pior* nota, não uma nota melhor); o autor da fonte especula, sem verificar, que a pesquisa da Anthropic não teria agrupado tasks de forma coesa — tratado como open question, não como fato reconciliado.
- **Cognition** (Devin, ver [[wiki/entities/devin-ai]]): subagentes são perigosos porque fragmentam contexto — toda ação de um agente carrega uma decisão que fica registrada na janela; um subagente novo não herda essas decisões. Batido diretamente pelo Cenário 2 do benchmark acima (granularidade excessiva fragmenta o contexto e derruba a qualidade).

### Modelo Mental de Decisão

1. **Research/varredura de codebase** → sempre vale subagente; não polui a janela do principal.
2. **Tarefas longas com muitas tasks** → considerar subagentes, mas evitar granularidade excessiva.
3. **Tarefas pequenas e fortemente acopladas** → manter na mesma janela, monitorando o quanto ela enche.
4. **Trabalho paralelizável** → subagentes ganham velocidade, mas de novo sem fragmentar demais.

## Key Sources

- [[wiki/sources/graph-engineering-matematica-do-erro-composto]] — organização típica organizador/researchers/builders/reviewers, arestas decidindo dependência entre subagentes
- [[wiki/sources/multiplos-agentes-worktrees-subagentes-claude-code]]
- [[wiki/sources/ia-2026-nao-e-so-prompt-nem-so-agente-codigo-fonte-tv]] — mensagens cruzadas entre subagentes via "list agents": um subagente pode disparar outro diretamente, sem depender do agente pai como intermediário
- [[wiki/sources/loop-engineering-planner-critic-grafo]] — subagentes como executores num loop Planner-Executor-Critic, com prompt e rúbrica gerados dinamicamente
- [[wiki/sources/spec-driven-development-otimizando-contexto-agentes]] — 4 subagentes em paralelo despachados a partir do breakdown de tasks de uma spec
- [[wiki/sources/graph-engineering-do-loop-ao-grafo]] — gestão de projeto (épico → história → tarefa → subtarefa com dependências cruzadas) como exemplo de como decidir quantos subagentes podem rodar em paralelo sem se bloquear, mesmo antes de qualquer agente de IA entrar no processo
- [[wiki/sources/subagentes-quando-vale-a-pena-custo-velocidade-tlc-spec-driven]] — benchmark de campo com 4 cenários de granularidade (sem subagente, 1 por task, agrupado por fase, sweet spot de 3): granularidade excessiva piora tempo, custo e qualidade ao mesmo tempo; agrupamento coeso iguala ou supera 1 agente único com janela final muito mais livre
