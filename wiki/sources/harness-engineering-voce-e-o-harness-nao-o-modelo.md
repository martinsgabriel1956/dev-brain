---
type: source
title: "Harness Engineering — 'Você Não É Mais o Modelo, Você É o Harness'"
aliases: ["if you are not the model you are the harness", "erros compostos agente", "12 componentes do harness"]
date_created: 2026-07-28
date_updated: 2026-07-28
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/harness-engineering-voce-e-o-harness-nao-o-modelo.md
source_url: ""
author: "não identificado (autor se dirige ao público como 'mava dev')"
date_published: ""
date_ingested: 2026-07-28
source_count: 0
tags: [harness, loop-engineering, ralph-loop, verificacao, erros-compostos, tool-call, anthropic, vercel, claude-code]
skill: tech-mentor-ai
status: stable
---

## TL;DR

Vídeo organizando a frase viral de Peter Steinberger ("você não deveria mais promptar agentes, deveria desenhar loops que promptam seus agentes") em torno de dois eixos: por que agentes falham de forma composta (matemática de 99%ⁿ ao longo de N etapas) e quatro formas de atacar isso no harness (verificação, checkpoints, ferramentas corretas, contexto limpo). Traz dois estudos de caso concretos — Vercel removendo 80% das ferramentas de um agente e melhorando performance, e o criador do Claude Code documentando ganho de 2-3x em qualidade só com mecanismos de verificação — além da origem do Ralph Loop (Geoffrey Huntley, julho de 2025) e dos quatro níveis oficiais de loop do guia da Anthropic (turn-based, goal-based, time-based, proactive). Argumenta que quem já usa CLAUDE.md, spec-driven development e TDD já está fazendo harness engineering sem nomear.

## Key Claims

**Claim:** Erros em processos de múltiplas etapas se compõem multiplicativamente — um processo de 10 etapas com 99% de sucesso individual por etapa tem ~90,4% de chance de sucesso completo; com 20 etapas, ~81,8%; com 50 etapas, ~60%.
**Evidence:** Matemática direta (0,99ⁿ), apresentada pelo autor como conclusão de um artigo citado de ouvido como "Adios Money" (identificação não confirmada). Consistente com o anti-padrão "Loop Infinito"/necessidade de `LoopDetector` e com os `AgentErrorCategory` documentados em `references/ai/agents-runtime.md` da skill, que trata falhas de agente como categorizáveis e cumulativas, não binárias.
**Confidence:** alta como matemática (cálculo verificável); média quanto à fonte original citada, não verificada externamente.

**Claim:** Quatro mecanismos atacam a composição de erros: verificação do próprio trabalho antes de avançar, checkpoints com intervenção humana/automatizada, ferramentas corretas (menos ambiguidade), e contexto limpo (menos ruído).
**Evidence:** Framework proposto pelo autor. O item "checkpoints" é diretamente equivalente ao padrão HITL documentado em `references/ai/agents-runtime.md` (`HITLManager`, critérios de quando exigir aprovação humana) — ver [[wiki/concepts/human-in-the-loop]]. O item "ferramentas corretas" reflete o anti-padrão "Tool Overload" de `references/ai/agentic-patterns-2025.md`.
**Confidence:** alta — os quatro mecanismos têm contrapartida direta e nomeada na literatura de referência da skill, mesmo com terminologia diferente.

**Claim:** A Vercel removeu 80% das ferramentas disponíveis para um agente interno (que tinha muitas ferramentas e performance ruim) e a performance melhorou — porque cada etapa passou a exigir escolher entre menos opções.
**Evidence:** Relato de experiência da Vercel, sem link ou paper citado pelo autor. Alinhado ponto a ponto com o anti-padrão "God Agent / Tool Overload" (`references/ai/agentic-patterns-2025.md`: "Um agente com 40+ tools → Dividir em especialistas com handoff" / "Confusão na seleção de tools → Embedding-based selection") e com o Padrão 5 (Tool Selection via Embedding), que documenta que agentes com 50+ ferramentas ficam "confusos ou lentos".
**Confidence:** média-alta como caso relatado (sem dado quantitativo do "quanto" melhorou), mas o mecanismo por trás é bem documentado na literatura de referência da skill — não é afirmação isolada.

**Claim:** O criador do Claude Code documentou publicamente que dar ao modelo uma forma de verificar o próprio trabalho (rodar testes, checar existência de arquivo, verificar se o output faz sentido) melhora a qualidade do output de 2 a 3 vezes.
**Evidence:** Citação atribuída de ouvido a "Bshine" (provável Boris Cherny, criador do Claude Code — já entidade na wiki, ver [[wiki/entities/claude-code]]). Sem link direto para a declaração original nesta fonte.
**Confidence:** média — número específico (2-3x) citado sem link verificável nesta fonte; mecanismo em si (verificação embutida) já documentado como boa prática em [[wiki/sources/20-melhores-praticas-claude-code-segundo-anthropic]] (fonte anterior da wiki, atribuída à documentação oficial da Anthropic), que reforça de forma independente a importância de verificação embutida no prompt.

**Claim:** O Ralph Loop, técnica de rodar um mesmo prompt em loop simples de bash até a tarefa terminar, foi publicado por Geoffrey Huntley (engenheiro australiano) em julho de 2025, batizado em homenagem a Ralph Wiggum d'Os Simpsons por ser deliberadamente simples.
**Evidence:** Relato histórico do autor, sem link direto nesta fonte. Consistente com a datação já registrada em [[wiki/concepts/loop-engineering]], que situa a origem conceitual do loop agêntico no padrão ReAct (2022/2023) e o destravamento de loops longos especificamente em 2026 — o Ralph Loop (2025) encaixa como o ponto intermediário entre a ideia (ReAct) e a maturidade atual (guia oficial da Anthropic).
**Confidence:** média — nome próprio e data específicos, não verificados por fonte externa nesta ingestão.

**Claim:** O guia oficial da Anthropic ("Getting Started with Loops") define quatro níveis de loop, cada um entregando mais autonomia ao agente: turn-based (cada prompt é o próprio loop, humano dirige cada turno), goal-based (humano dá a condição de parada, ex. "roda até os testes passarem"), time-based (humano dá o gatilho/trigger, loop roda agendado sem presença humana), e proactive (humano dá só o prompt, sistema decide o quê e quando agir).
**Evidence:** Relato do autor sobre o guia, sem link direto nesta fonte. Complementar (não conflitante) à taxonomia de três níveis já registrada em [[wiki/concepts/loop-engineering]] (Loop React → Spec Driven → Humano no Loop, de [[wiki/sources/loop-engineering-niveis-dev-loop-jogo-mmo]]) — são frameworks de autores diferentes descrevendo a mesma progressão de autonomia crescente, com nomenclatura própria cada um.
**Confidence:** média — conteúdo de um guia oficial citado de segunda mão, sem link verificável nesta ingestão; a existência do guia é mencionada por mais de uma fonte já presente na wiki (padrão consistente).

**Claim:** O mesmo Claude Opus performa significativamente melhor dentro do harness do Claude Code do que em benchmark padrão sem harness — mesmo modelo, harness diferente, resultado diferente.
**Evidence:** Citado como "dado de benchmark" sem número específico nem link nesta fonte.
**Confidence:** baixa/qualitativa — afirmação sem cifra, tratada aqui como reforço direcional do argumento central do vídeo (harness importa mais que o modelo), não como dado verificado.

## Entities & Concepts Touched

- [[wiki/concepts/harness]]
- [[wiki/concepts/loop-engineering]]
- [[wiki/concepts/tool-call]]
- [[wiki/concepts/rubrica-de-verificacao]]
- [[wiki/concepts/human-in-the-loop]]
- [[wiki/concepts/hooks-agente]]
- [[wiki/concepts/spec-driven-development]]
- [[wiki/concepts/ciclo-agente]]
- [[wiki/concepts/ralph-loop]]
- [[wiki/entities/anthropic]]
- [[wiki/entities/claude-code]]
- [[wiki/entities/open-claw]]
- [[wiki/entities/geoffrey-huntley]]
- [[wiki/entities/peter-steinberger]]
- [[wiki/entities/vercel]]

## Open Questions

- Identidade de "Peter Steinberger, criador do OpenClaw" citada no vídeo não bate diretamente com o que a wiki já registrava sobre [[wiki/entities/open-claw]] (agente open source MIT, mensageria multi-plataforma, sem criador nomeado nas fontes anteriores) — mantido como claim não reconciliado; ver nota em [[wiki/entities/open-claw]].
- O "caso Lang Shen" (mesmo modelo/pesos, infraestrutura diferente, saiu do top 30 para o ranking 5 em benchmark) não foi possível identificar com confiança — nome citado de ouvido, sem sobrenome completo nem link. Registrado como não verificado; se uma fonte futura mencionar o mesmo caso com grafia diferente, reconciliar.
- Os "12 componentes do harness" citados pelo autor foram cobertos apenas 7 no vídeo (system prompt, ferramentas, gestão de contexto, mecanismos de verificação, memória, sandboxes, hooks) — os outros 5 não foram nomeados nesta fonte; candidato a completar se o autor publicar os componentes restantes.
- Nenhum link ou número de benchmark foi fornecido para o claim "Opus performa melhor dentro do harness do Claude Code do que em benchmark padrão" — vale cruzar com fonte primária da Anthropic se aparecer.

## Fontes Relacionadas

- [[wiki/sources/loop-engineering-harness-e-a-frase-que-viralizou]] — mesma correção central ("loop contém harness, não o substitui"), mesma origem no padrão ReAct; esta nova fonte adiciona a matemática de erros compostos, os quatro mecanismos de mitigação, os estudos de caso (Vercel, Claude Code) e a origem do Ralph Loop, que a fonte anterior não cobria.
- [[wiki/sources/loop-engineering-niveis-dev-loop-jogo-mmo]] — propôs os três níveis do dev loop (React/Spec Driven/Humano) mais loop engineering como quarta camada; esta fonte traz o framework paralelo e oficial da Anthropic (turn/goal/time/proactive) — mesma progressão de autonomia, nomenclatura e autor diferentes, sem contradição.
- [[wiki/sources/20-melhores-praticas-claude-code-segundo-anthropic]] — já registrava "verificação embutida no prompt" como boa prática atribuída à documentação oficial da Anthropic; esta fonte reforça de forma independente com o número específico (2-3x) atribuído ao criador do Claude Code.
