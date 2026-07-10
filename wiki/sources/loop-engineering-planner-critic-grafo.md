---
type: source
title: "Loop Engineering: Por Que Você Deveria Estar Desenhando Loops, Não Prompts"
aliases: ["loop engineering", "harness com planner critic", "grafo como abstração de agentes"]
date_created: 2026-07-10
date_updated: 2026-07-10
source_count: 0
tags: [tech-mentor-ai, loop-engineering, harness, planner-executor-critic, rubrica, langgraph, grafo, subagentes]
skill: tech-mentor-ai
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/loop-engineering-planner-critic-grafo.md
source_url:
author: "Hulk (canal de vídeo — self-identificação na transcrição, não confirmada externamente)"
date_published:
date_ingested: 2026-07-10
---

# Loop Engineering: Por Que Você Deveria Estar Desenhando Loops, Não Prompts

## TL;DR

Vídeo opinativo que propõe uma progressão de abstração — prompt engineering → context engineering → harness engineering → **loop engineering** — e demonstra na prática um sistema onde um Planner (LLM) gera dinamicamente prompts e rúbricas para subagentes, um Verificador (outra LLM, para evitar bias) aprova ou devolve follow-ups contra essa rúbrica, e o grafo (nós = computação/LLM, arestas = condição de fluxo determinística) é o nível de abstração que amarra tudo. Tese central: "você não escreve mais o prompt, você desenha o sistema que escreve o prompt."

## Key Claims

1. **Loop engineering é o próximo degrau depois de harness engineering** — prompt engineering melhora uma chamada, context engineering melhora o contexto de uma chamada, harness engineering melhora o ambiente ao redor do modelo (como um todo), loop engineering melhora o ciclo completo — da primeira chamada até a resposta final — tornando-o repetível e disparável automaticamente (não só por prompt do usuário, mas por schedule ou evento).
2. **Quem constrói harness vira melhor vibe coder** — entender os padrões por trás de uma harness (como o modelo chama ferramentas, limites de contexto, compactação, skills) permite reconhecer e reaproveitar harnesses de terceiros (Claude, Codex) em vez de reinventá-los; harness engineering é maior que vibe coding, apesar de a internet tratar os dois como sinônimos.
3. **Planner gera prompt E rúbrica dinamicamente** — em vez de o humano escrever prompts para cada subtarefa, uma LLM "planner" (o autor usou GPT-5.5 — modelo mais forte, por ser tarefa que exige mais raciocínio) decompõe a entrada em até ~160 subtarefas simultâneas, cada uma com objetivo, papel, resultado esperado e fontes sugeridas — e define a **rúbrica**: os critérios que tornam a subtarefa "cumprida".
4. **Verificador é sempre um modelo diferente do executor** — para evitar que o mesmo viés (bias) do modelo que gerou a resposta também a valide, uma segunda LLM (outro modelo, não outra chamada do mesmo modelo) recebe a rúbrica e a saída do subagente executor, e decide aprovar ou gerar um follow-up específico (ex.: "reescreva o relatório incluindo uma tabela markdown com colunas"). No exemplo demonstrado, o loop rodou 3 tentativas de follow-up antes de não aprovar — o critério de parada (número de tentativas, o que fazer ao esgotá-las) é decisão de quem desenha o sistema, não do modelo.
5. **Isso não é o AutoGPT/"AFF Loop" de novo** — loops autônomos sem verificação (AutoGPT-like) não emplacaram porque viravam "monstrinhos" rodando sem controle. A diferença aqui é a dupla executor/verificador com rúbrica explícita e critério de decisão definido pelo autor do sistema, não pela LLM.
6. **Trade-off token/qualidade determina onde usar** — para quem não tem tokens ilimitados e preza qualidade de codebase, ainda é necessário um engenheiro por perto nos momentos de decisão. Para trabalho corporativo, pesquisa interna e entendimento de cliente (knowledge work / colarinho branco), o padrão é descrito como "maravilhoso" — sem dependência de nenhum provider específico, desde que haja conhecimento técnico para desenhá-lo.
7. **O grafo é o nível de abstração central, independente de framework** — G = (V, E): nós são onde computação acontece (frequentemente uma chamada de LLM, com custo computacional), arestas são condições de fluxo determinísticas definidas por quem constrói o sistema. A tese: não se deve deixar a LLM decidir tudo — decisões determinísticas (roteamento, critério de aprovação, número de tentativas) ficam nas arestas; a LLM resolve o que ela resolve bem (raciocínio, síntese) nos nós. LangGraph é citado como a ferramenta escolhida pelo autor, mas o grafo em si "não depende de framework" — pode ser desenhado no papel ou como estrutura matemática.
8. **A mudança de nível de abstração é de "resolver um problema" para "resolver uma categoria de problemas"** — em vez de escrever código para resolver um caso específico, o sistema (planner + subagentes + verificador + grafo) resolve qualquer instância de um tipo de problema, inclusive disparado por evento (ex.: verificar toda meia-noite se vendas caíram e, se sim, montar a harness necessária dinamicamente).
9. **Contexto de origem** — a citação do criador do OpenCode ("desenhar loops que fazem prompts") e do criador do Claude Code ("eu não faço mais prompts, tenho loops que descobrem o que precisa ser feito") serve de gancho: ambos trabalham em empresas que vendem tokens (viés a favor de uso intensivo), e ambos falam de "criar soluções" de forma agnóstica de domínio — o vídeo generaliza esse discurso para qualquer prática de engenharia de software/produto.

## Entidades Mencionadas

- [[wiki/entities/anthropic]] — empregador do criador do Claude Code citado na abertura
- [[wiki/entities/openai]] — empregador do criador do OpenCode citado na abertura
- [[wiki/entities/claude-code]] — citado como harness cujos padrões podem ser reaproveitados
- OpenCode — harness citado (sem entidade dedicada no wiki; já referenciado na tabela de [[wiki/concepts/harness]])

## Conceitos Tocados

- [[wiki/concepts/loop-engineering]]
- [[wiki/concepts/planner-executor-critic]]
- [[wiki/concepts/rubrica-de-verificacao]]
- [[wiki/concepts/grafo-como-abstracao-de-agentes]]
- [[wiki/concepts/langgraph]]
- [[wiki/concepts/harness]]
- [[wiki/concepts/ciclo-agente]]
- [[wiki/concepts/subagentes]]
- [[wiki/concepts/vibe-coding]]
- [[wiki/concepts/prompt-engineering]]
- [[wiki/concepts/context-engineering-harness]]

## Contradições / Reforços com o Resto da Wiki

**Reforço direto:** [[wiki/sources/agentes-orquestracao]] já descrevia o padrão Planner-Executor-Critic e LangGraph ("nodes são passos, edges são transições condicionais") em termos quase idênticos, mas os conceitos `[[concepts/planner-executor-critic]]` e `[[concepts/langgraph]]` citados naquela fonte nunca haviam sido criados (link quebrado — drift pré-existente, corrigido nesta ingestão). Esta fonte fornece o exemplo concreto e a demonstração em vídeo que faltava para essas páginas.

**Reforço:** [[wiki/concepts/ciclo-agente]] já documentava "É um brute-force até funcionar" (Branas) — esta fonte adiciona a camada de que o brute-force pode ser tornado sistemático via rúbrica + verificador com modelo distinto, reduzindo (sem eliminar) a natureza cega da iteração.

**Sem contradição, mas tensão explícita:** o vídeo reconhece a mesma ressalva que [[wiki/sources/vibe-coding-limites-maturidade-profissional]] já registrava — automação agêntica ilimitada não substitui julgamento humano quando token não é infinito e qualidade do codebase importa; loops autônomos são posicionados para trabalho corporativo/pesquisa, não para produção de codebase crítico sem supervisão.

**Observação de escopo (não contradição):** o vídeo não detalha custo de tokens do padrão (rúbrica + verificador dobra o número de chamadas de LLM por subtarefa) — nenhuma página do wiki cobre esse ângulo de custo específico do padrão PEC ainda; ponto em aberto.
