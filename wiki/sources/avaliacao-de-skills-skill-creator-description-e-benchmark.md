---
type: source
title: "Avaliação de Skills com o Skill Creator: Description e Benchmark com/sem Skill"
aliases: ["avaliação de skills", "skill-creator evals", "benchmark com e sem skill"]
date_created: 2026-09-29
date_updated: 2026-09-29
source_count: 0
tags: [tech-mentor-ai, skills, evals, skill-creator, description-optimization, benchmark, haiku, opus, claude-code, portabilidade-de-harness]
skill: tech-mentor-ai
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/avaliacao-de-skills-skill-creator-description-e-benchmark.md
source_url: ""
author: "desconhecido (vídeo/aula PT-BR)"
date_published: ""
date_ingested: 2026-09-29
---

# Avaliação de Skills com o Skill Creator: Description e Benchmark com/sem Skill

## TL;DR

O apresentador mostra a anatomia de uma skill (`SKILL.md` com front matter + corpo, mais `references/` e `scripts/`) e usa a skill **skill-creator** da Anthropic ([[wiki/entities/skill-creator]]) para dois tipos de avaliação: (1) **otimização de description** — um loop iterativo com queries *should trigger / should not trigger* que recuperou uma description propositalmente capada ([[wiki/concepts/otimizacao-de-descricao-de-skill]]); (2) **benchmark com skill vs. sem skill** rodado em paralelo com Haiku e Opus, com relatório de *grades* por asserção. Resultado relatado: com Opus 100/100 com ou sem skill (a skill é dispensável); com Haiku ~90% com skill vs. ~50% sem (delta de ~40 pontos) ([[wiki/concepts/benchmark-com-e-sem-skill]]). Tese final: skills são a base de workflows estruturados e precisam funcionar em vários modelos/harnesses para que o time tenha experiência parecida ([[wiki/concepts/avaliacao-de-skills]]).

## Key Claims

1. **Estrutura de skill:** pasta em `.claude/skills/` (ou `.agents/skills/`), `SKILL.md` com front matter (`name`, `description`) + corpo de instruções, opcionalmente referências (ex.: catálogo de antipadrões de performance SQL) e scripts. Evidência: demo de skills SQL do autor. → [[wiki/concepts/skills-agente]]
2. **A skill-creator é uma skill da Anthropic para testar skills**, com scripts determinísticos, referências e arquivos de apoio; roda o processo de evaluation. → [[wiki/entities/skill-creator]], [[wiki/entities/anthropic]]
3. **Loop de description:** com a description capada pela metade, o loop (`run_loop.py`) gera descriptions em iterações distintas, testa contra queries *should trigger* e devolve a melhor; a skill passou de "não funciona bem" para acionada corretamente. Evidência: histórico rodado e log na pasta `workspace/description-optimization`; **sem números** de taxa de acionamento na fala. → [[wiki/concepts/otimizacao-de-descricao-de-skill]]
4. **A avaliação qualitativa varia por N eixos:** client, modelo, provedor, dataset. → [[wiki/concepts/avaliacao-de-skills]], [[wiki/concepts/llm-evals-testing]]
5. **Haiku vs. Opus, com vs. sem skill:** Haiku ~90% com skill / ~50% sem (delta 40 pts); Opus 100/100 nos dois casos. Evidência: uma skill de migração de banco de dados, prompts e resultados esperados do autor; **amostra e tamanho do conjunto de prompts não informados**. → [[wiki/concepts/benchmark-com-e-sem-skill]], [[wiki/concepts/modelo-por-leverage-tarefa]]
6. **O eval indica se a skill deve existir:** se o modelo forte resolve sozinho, a skill não se justifica naquele projeto; modelos avançados absorvem o que antes exigia skill. → [[wiki/concepts/benchmark-com-e-sem-skill]]
7. **Execução por subagentes encadeados** (iterações por modelo, pastas com/sem skill, benchmark consolidado). → [[wiki/concepts/subagentes]]
8. **Relatório item a item (grades):** mostra resposta, asserções passadas/falhas (ex.: 5/5 vs. 2/5) e o porquê da falha, permitindo melhorar a skill progressivamente. → [[wiki/concepts/avaliacao-de-skills]]
9. **Portabilidade:** o time usa harnesses diferentes (Claude Code, Codex, OpenCode); o workflow (skills) deve dar experiência minimamente parecida em todos. → [[wiki/entities/claude-code]], [[wiki/entities/codex-openai]], [[wiki/entities/opencode]], [[wiki/concepts/harness]]

## Entidades Mencionadas

- [[wiki/entities/skill-creator]] — skill oficial da Anthropic para criar/avaliar skills.
- [[wiki/entities/anthropic]] — autora da skill-creator; modelos Haiku e Opus.
- [[wiki/entities/claude-code]], [[wiki/entities/codex-openai]], [[wiki/entities/opencode]] — harnesses citados como preferências do time.

## Conceitos Tocados

Criados: [[wiki/concepts/avaliacao-de-skills]], [[wiki/concepts/otimizacao-de-descricao-de-skill]], [[wiki/concepts/benchmark-com-e-sem-skill]].

Atualizados: [[wiki/concepts/skills-agente]], [[wiki/concepts/llm-evals-testing]], [[wiki/concepts/evals-llm]], [[wiki/concepts/closed-loop-skill-learning]], [[wiki/concepts/modelo-por-leverage-tarefa]], [[wiki/concepts/roteamento-automatico-de-modelo]], [[wiki/concepts/harness]], [[wiki/concepts/harness-de-qualidade]], [[wiki/concepts/subagentes]], [[wiki/concepts/progressive-disclosure-ia]], [[wiki/concepts/pilares-de-desenvolvimento-com-ia]].

## Open Questions

- **Transcrição truncada** no fim ("…para todos os as pessoas do meu Sim").
- **Sem números de amostra:** não se sabe quantos prompts/asserções compõem o benchmark, nem a variância entre execuções; 90% vs. 50% e o "delta de 40 pontos" são reportados de forma verbal.
- **Inconsistência aparente:** "delta de 40 pontos" bate com 90% vs. 50%, mas a soma de falhas citadas (3+3+4+2 itens) não é acompanhada do total de asserções — não dá para reconciliar (inferência).
- **Validade da skill fora do modelo testado:** o autor testou só Haiku e Opus (Anthropic); a alegação de portabilidade entre Claude Code/Codex/OpenCode não foi demonstrada.
- **Nome da skill "query optimizer"** e sua identidade exata incertos por corrupção da transcrição.
- [skill: tech-mentor-ai] `references/ai/production-evals.md` recomenda golden dataset + evals em CI; a fonte roda o loop manualmente, sem CI — lacuna a explorar.
- **Viés de mesmo modelo:** quem gera as descriptions e quem julga é o mesmo ecossistema de modelos; risco de otimizar para o próprio juiz (inferência [skill: tech-mentor-ai]).

## Raw Quotes

> "Se eu utilizo o modelo um pouco menos inteligente, olha a diferença: com skill eu tenho 90% de assertividade, sem skill eu tenho 50%." (redação limpa da transcrição)

> "Sem ela, processos de workflow mais estruturados se tornam impossíveis atualmente."
