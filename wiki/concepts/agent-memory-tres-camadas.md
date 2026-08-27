---
type: concept
title: "Memória de Agente em Três Camadas (Sessão / Persistente / Skill)"
aliases: ["three-layer agent memory", "memória de três camadas", "session/persistent/skill memory"]
date_created: 2026-07-21
date_updated: 2026-08-27
source_count: 4
tags: [tech-mentor-ai, agent-memory, learning-loop, sqlite, fts5, hermes-agent, claude-md, memory-layers]
skill: tech-mentor-ai
status: draft
---

# Memória de Agente em Três Camadas (Sessão / Persistente / Skill)

Padrão arquitetural para agentes de propósito geral que precisam reter contexto entre conversas, não só dentro de uma única sessão. Descrito em [[wiki/sources/hermes-agent-open-claw-learning-loop]] como base do Hermes Agent, mas apresentado como padrão comum a "quem já usa alguma orquestração de agentes" — não uma invenção exclusiva.

## As Três Camadas

1. **Memória de sessão** — a conversa atual. Equivalente à working memory in-context do Claude Code ou Codex: rápida, mas perdida ao fim da sessão.
2. **Persistent memory** — um `memory.md` (ou equivalente) que armazena e cura dados entre agentes e sessões diferentes. É o que sobrevive ao fechar a janela de contexto atual.
3. **Skill memory** — padrões extraídos de tarefas passadas, convertidos em skills reutilizáveis (ver [[wiki/concepts/closed-loop-skill-learning]]), indexadas por um arquivo `.md` próprio.

## Indexação via FTS5 (SQLite)

O caso descrito usa **FTS5** (full-text search do SQLite) para buscar sobre a sumarização LLM da memória persistente quando o contexto cresce — em vez de (ou além de) um vector store dedicado. Diferença prática frente às opções listadas em [[wiki/concepts/gerenciamento-de-memoria]]/`agent-memory.md`: FTS5 é busca lexical/full-text, não busca por similaridade semântica via embeddings — mais barato de rodar localmente (SQLite embutido, sem serviço externo), mas sem os mesmos ganhos de recall semântico de um vector store como Qdrant ou pgvector.

## Resultado Prático

O efeito observado, segundo a fonte: o agente passa a lembrar preferências implícitas do usuário (ex.: "você odeia NPM") depois de poucas sessões, sem que isso precise ser reescrito manualmente em um arquivo de regras a cada nova janela de contexto.

## Relação com Outros Conceitos

- [[wiki/concepts/closed-loop-skill-learning]] — o loop que alimenta a camada de skill memory
- [[wiki/concepts/memoria-de-longo-prazo-ia]] — padrão irmão, mas de escopo mais estreito (memória de research/refactoring plan entre sessões de uma única tarefa grande, não memória geral de preferências do usuário)
- [[wiki/concepts/skills-agente]] — skill memory é, na prática, um caso de skills geradas automaticamente em vez de escritas à mão
- [[wiki/concepts/hooks-agente]] — hooks são o mecanismo citado para popular a persistent/skill memory ao fim de uma sessão

## Variante: Distinção da Própria Anthropic (Contexto de Trabalho / Memória Futura / Artefato Revisado)

[[wiki/sources/ia-2026-nao-e-so-prompt-nem-so-agente-codigo-fonte-tv]] atribui à [[wiki/entities/anthropic|Anthropic]] (transcrição foneticamente incerta na fonte, possível erro de ASR para "a própria Anthropic") uma distinção de três partes semelhante em espírito às três camadas acima, mas nomeada de forma diferente: **contexto de trabalho** (equivalente à memória de sessão), **memória para execuções futuras** (equivalente à persistent memory) e **artefatos revisados que servem como fonte confiável** — uma categoria adicional que não mapeia diretamente para nenhuma das três camadas originais, mais próxima da ideia de um golden dataset curado do que de skill memory. A mesma fonte trata a hierarquia do [[wiki/concepts/claude-md|`CLAUDE.md`]] (máquina → usuário → projeto → pasta) explicitamente como uma forma de memória, e não só como configuração de regras — enquadramento novo frente ao resto da wiki, que até esta ingestão tratava a hierarquia de rules separadamente de memory layers.

A fonte também documenta uma prática de campo (não formalizada como spec ou loop): pedir ao agente para gerar documentação numa pasta `docs/` do próprio projeto ao final de cada tarefa, para servir de contexto consultável nas sessões seguintes — mesmo padrão funcional do artefato de "estado" já coberto em [[wiki/concepts/spec-driven-development#Estado: Registro de Decisões Pós-Planejamento]], mas descrito aqui como hábito informal, fora do fluxo formal de spec-driven.

## Variante: Memória Multiplayer por Canal (Claude Tag)

[[wiki/sources/claude-tag-slack-terceiro-paradigma-llm]] descreve uma variante ainda sem página própria na wiki: memória compartilhada não por usuário/sessão, mas por **canal/equipe inteira** — um agente por canal do Slack (Claude Tag, da [[wiki/entities/anthropic]]) que aprende com as mensagens de todos os membros e une pedidos feitos por pessoas diferentes num mesmo contexto contínuo. As três camadas acima (sessão/persistente/skill) seguem se aplicando, mas a "sessão" deixa de ser de um usuário e passa a ser do canal como um todo — candidata a virar concept própria (`memoria-multiplayer-agente.md`) se surgir mais de uma fonte técnica detalhando o mecanismo.

## Variante: User / Episodic / Semantic / Procedural Memory (Assemble de Contexto)

[[wiki/sources/harness-anatomia-tecnica-alem-do-claude-md]] descreve uma quarta nomenclatura para o mesmo domínio, no contexto do assemble de contexto de um agent run genérico (não específico de um harness com learning loop): **user memory** (fatos duráveis sobre o usuário), **episodic memory** (linha do tempo de descobertas já feitas na conversa atual — mapeia perto de "memória de sessão" acima, mas enfatizada como histórico cronológico de achados, não só janela ativa), **semantic memory** (fatos gerais de usuário/projeto, mais perto de persistent memory) e **procedural memory** (os arquivos markdown/playbooks — equivalente direto à camada procedural já usada nesta página). Diferença central frente às três camadas e à distinção da Anthropic acima: esta fonte separa explicitamente episodic de semantic, onde as outras duas nomenclaturas tratam esse par como uma única camada de "persistent/memória futura". A fonte também nota que nem toda ferramenta implementa todas as quatro camadas — algumas exigem configuração manual, outras não têm nenhuma forma de aprendizado contínuo sobre o usuário.

## Key sources

- [[wiki/sources/harness-anatomia-tecnica-alem-do-claude-md]] — quarta nomenclatura (user/episodic/semantic/procedural memory) no contexto de assemble de contexto de um agent run; separa episodic de semantic explicitamente
- [[wiki/sources/hermes-agent-open-claw-learning-loop]]
- [[wiki/sources/claude-tag-slack-terceiro-paradigma-llm]] — variante de memória multiplayer por canal (não por usuário individual)
- [[wiki/sources/ia-2026-nao-e-so-prompt-nem-so-agente-codigo-fonte-tv]] — distinção de três partes atribuída à Anthropic (contexto de trabalho / memória futura / artefatos revisados); hierarquia do CLAUDE.md enquadrada como memory layer; prática de campo de gerar docs em `docs/` ao fim de cada tarefa
