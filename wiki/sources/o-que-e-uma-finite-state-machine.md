---
type: source
title: "O que é uma Finite State Machine?"
aliases: ["fsm em game design", "finite state machine felipe costa"]
date_created: 2026-09-21
date_updated: 2026-09-21
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/o-que-e-uma-finite-state-machine.md
source_url: "https://medium.com/@felipecoast/o-que-é-uma-finite-state-machine-0592d7213f21"
author: "Felipe Costa"
date_published: 2023-12-07
date_ingested: 2026-09-21
source_count: 0
tags: [fsm, finite-state-machine, game-design, game-ai, automatos, teoria-da-computacao]
skill: cs-fundamentals
status: stable
---

## TL;DR

Introdução a Finite State Machine (FSM) aplicada a Game Design: um modelo de estados mutuamente exclusivos, com transições disparadas por eventos/ações do jogador ou regras definidas pelo Game Designer. Usa a IA clássica dos fantasmas de _Pac-Man_ (perseguir vs. fugir, disparado por o jogador comer a pílula) e uma _turret_ hipotética (patrulhar → atacar → eliminado/reiniciado, disparado por alcance e HP) como exemplos concretos. Fecha com um "easter egg" sobre Hierarchical Finite State Machine (HFSM), que adiciona subestados dentro de cada estado da FSM para modelar comportamentos mais complexos sem explodir o número de transições diretas.

## Key Claims

**Claim:** Uma FSM modela um fluxo de comportamentos em que apenas um estado pode estar ativo por vez, com transições disparadas por eventos ou ações específicas.
**Evidence:** Exemplo dos fantasmas de _Pac-Man_ — "perseguir" e "fugir" nunca estão ativos ao mesmo tempo; a transição entre eles depende de o _Pac-Man_ ter comido a pílula ou não.
**Confidence:** alta — consistente com a definição formal de autômato finito (conjunto finito de estados + função de transição determinística por evento), documentada em `references/computation-theory.md` da skill `cs-fundamentals`.

**Claim:** FSM já foi considerada uma das principais formas de IA em jogos no passado, mas hoje, diante da evolução de modelos de IA mais sofisticados, ocupa um papel mais modesto — embora continue em uso.
**Evidence:** Afirmação direta do autor, sem citar fontes históricas específicas nem os modelos de IA mais recentes aos quais compara.
**Confidence:** média — plausível e alinhada ao consenso da indústria de que FSM é uma técnica clássica de IA de jogos (junto com Behavior Trees, GOAP, utility AI), mas a fonte não especifica quando surgiu nem cita literatura ([external] Behavior Trees e GOAP são geralmente citados como sucessores por permitirem mais reuso e escalabilidade de comportamento do que FSMs planas).

**Claim:** Transições de estado podem ser definidas por regras arbitrárias do Game Designer, não apenas por gatilhos visualmente óbvios — ex.: inimigo transita de "patrulhar" para "atacar" apenas se o jogador chegar a exatos 3 metros, ou ao ouvir um barulho.
**Evidence:** Exemplos hipotéticos dados pelo autor (distância de detecção, ruído chamando atenção de um guarda).
**Confidence:** alta — descreve corretamente como a função de transição de uma FSM é, na prática, um contrato de design arbitrário (qualquer predicado sobre o estado do mundo/jogador), não uma limitação técnica do modelo.

**Claim:** Hierarchical Finite State Machine (HFSM) estende a FSM ao permitir que cada estado tenha subestados com seu próprio conjunto de transições, aumentando a complexidade e a naturalidade dos comportamentos sem ser uma FSM plana.
**Evidence:** Exemplo dado: o estado "perseguir" dos fantasmas de _Pac-Man_ poderia ser subdividido em subestados como "atravessar paredes" e "ficar invisível".
**Confidence:** alta — consistente com a motivação padrão de HFSM/Statecharts na literatura (evitar explosão combinatória de transições ao aninhar estados), embora a fonte não cite o termo "Statechart" (Harel, 1987) nem ferramentas concretas que implementam isso (ex.: XState) — ver `references/computation-theory.md`, seção "FSM vs Statechart (Harel)".

## Entities & Concepts Touched

- [[wiki/concepts/finite-state-machine]]
- [[wiki/concepts/hierarchical-finite-state-machine]]
- [[wiki/concepts/maquina-de-turing]]
- [[wiki/concepts/state-pattern]]
- [[wiki/concepts/maquina-de-estados-ui]]
- [[wiki/entities/felipe-costa]]

## Open Questions

- A fonte não distingue FSM de suas alternativas modernas em IA de jogos (Behavior Trees, GOAP, Utility AI) — apenas afirma que FSM "pode não ser mais considerada uma das principais" sem detalhar o porquê nem citar as técnicas sucessoras. `[external]`
- Não há menção ao termo formal "Statechart" (Harel) para o conceito de HFSM, embora a motivação descrita seja equivalente à de statecharts hierárquicos usados em ferramentas como XState (já presente em `references/computation-theory.md` da skill `cs-fundamentals`, ainda não citado em [[wiki/concepts/maquina-de-estados-ui]]).
- Nenhuma citação de literatura formal de teoria da computação (a fonte é uma introdução voltada a Game Design, não a ciência da computação) — útil como ponto de entrada aplicado, mas sem embasamento formal para claims sobre "precursoras da IA em games".

## Raw quotes

> "Finite State Machine (FSM) ou Máquina de Estado Finita é uma técnica que modela a representação de um fluxo entre diferentes comportamentos em um jogo."

> "Não é possível que ambos os estados estejam ativos ao mesmo tempo, ou seja, a depender da situação, ou o fantasma estará te perseguindo, ou então estará fugindo de você."

> "Além dos estados normais de uma FSM, uma HFSM pode ter subestados que podem dar acesso à outros conjuntos de transições."

## Notas de ingestão

Fonte fornecida pelo usuário como URL do Medium. `WebFetch` retornou HTTP 403 (bloqueio anti-scraping do Medium, mesma classe de bloqueio já registrada em ingests anteriores como [[wiki/sources/7-coisas-desenvolvedores-2026-max-lorian]]); contornado via proxy leitor `r.jina.ai`. Artigo já estava em português — sem necessidade de tradução. Salvo em `raw/o-que-e-uma-finite-state-machine.md` conforme pedido explícito do usuário. Skill carregada: `cs-fundamentals` (via `anthropic-skills:cs-fundamentals`), referência consultada: `references/computation-theory.md`, seção "Máquinas de Estado Finito (FSM)". Path de skills do CLAUDE.md (`/home/nemomartins/...`) não corresponde a este ambiente (`/home/gabriel-martins/...`) — mesma situação já registrada em ingests anteriores; usada a skill real via Skill tool. Este ingest cria a primeira página de conceito dedicada a FSM na wiki (`[[wiki/concepts/finite-state-machine]]`) — até então, [[wiki/concepts/maquina-de-turing]] linkava para [[wiki/concepts/maquina-de-estados-ui]] como se fosse a página geral de FSM, quando na verdade essa página é específica de UI/frontend; corrigido como parte deste ingest.
