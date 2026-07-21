---
type: source
title: "Hermes Agent: o Novo Open Claw? Learning Loop, Skill Auto-Gerada e o Bug de Detecção que Torrou 200 Dólares no Claude Max 20"
aliases: ["hermes agent", "closed-loop skill learning system", "hermes.md bug anthropic"]
date_created: 2026-07-21
date_updated: 2026-07-21
source_count: 0
tags: [tech-mentor-ai, hermes-agent, open-claw, agent-memory, learning-loop, skills-agente, hooks-agente, mcp, claude-code, anthropic, messaging-gateway]
skill: tech-mentor-ai
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/hermes-agent-open-claw-learning-loop.md
source_url:
author: "canal de vídeo não identificado explicitamente na transcrição (autor menciona ter feito conteúdo com OpenAI 'há muito tempo' e ironiza a Anthropic 'nos convencer a usar HTML' — sem nome próprio citado no texto)"
date_published:
date_ingested: 2026-07-21
---

# Hermes Agent: o Novo Open Claw? Learning Loop, Skill Auto-Gerada e o Bug de Detecção que Torrou 200 Dólares no Claude Max 20

## TL;DR

Vídeo sobre o **Hermes Agent**, um agente open source (MIT) comparado ao Open Claw, cuja proposta central é um **closed-loop skill learning system** de 5 etapas (task completion → pattern extraction → skill creation → skill refinement → periodic audit a cada ~15 tarefas) rodando sobre memória persistente em três camadas (sessão, persistente, skill) indexada via FTS5 do SQLite, com um messaging gateway multi-plataforma (Telegram/Discord/Slack/WhatsApp). O vídeo usa como gancho um incidente real: um usuário do Claude Max 20 (US$200/mês) teve o uso extra consumido por um bug de detecção de ferramentas de terceiros que disparava ao encontrar a string "hermes" (convenção real de nomeação `hermes.md` para specs de prompt de sistema) no Git history — a Anthropic confirmou o bug e ofereceu reembolso.

## Key Claims

1. **O bug do Claude Max 20 foi real e confirmado pela Anthropic** — um usuário relatou publicamente ter tido o uso extra do Claude Max 20 (US$200/mês) consumido/encerrado por causa da string "hermes" presente em commits do Git, associada à convenção `hermes.md` (arquivo de especificação de prompt de sistema usado em projetos de agentes de IA, não um caso obscuro isolado). Um representante da Anthropic (citado como "Tarik" na transcrição, sem confirmação externa do nome/cargo nesta ingestão) respondeu publicamente admitindo bug "na detecção de ferramentas de terceiros e na forma como incluímos o status do Git no prompt do sistema", com pedido de desculpas e oferta de reembolso aos afetados.
2. **O Hermes Agent implementa um "closed-loop skill learning system" de ~5-6 etapas** — task completion (fim de uma tarefa) → pattern extraction (identificar o que se repete entre tarefas parecidas, via hooks que alimentam uma IA geradora de padrões) → skill creation (etapa já manual em várias empresas, automatizada no Hermes) → skill refinement (mesclar/simplificar skills parecidas — o autor relata fazer isso manualmente e achar difícil de escalar) → periodic audit a cada ~15 tarefas (autoavaliação de o que persistir e por quanto tempo, citando um TTL configurado, documentado no `agents.md` do projeto).
3. **Memória em três camadas é o padrão arquitetural, não exclusividade do Hermes** — (1) memória de sessão (equivalente à conversa atual do Claude Code/Codex), (2) persistent memory (`memory.md` curado entre agentes/sessões — já presente em quem usa orquestração de agentes), (3) skill memory (padrões extraídos e indexados por skill, com um `.md` de índice). Ver [[wiki/concepts/agent-memory-tres-camadas]].
4. **FTS5 (SQLite) é o mecanismo de indexação citado para a memória persistente** — usado para busca full-text sobre a sumarização feita por LLM quando o contexto cresce; citado no vídeo como escolha técnica específica do Hermes, sem detalhamento de schema ou benchmark.
5. **Ganho de skill auto-gerada é estritamente específico de domínio, não generaliza** — uma skill gerada para "sumarizar uma PR do GitHub" não se aplica a algo como "planejar migração de banco de dados conforme os últimos PRs"; tentar generalizar comprometeria o projeto. Delimita o caso de uso para os ~80% do trabalho repetitivo, não para decisões arquiteturais.
6. **Messaging gateway multi-plataforma é onde a comparação com Open Claw se intensifica, mas mistura dois problemas distintos** — usar IA para acelerar desenvolvimento de software vs. usar IA como assistente pessoal de vida (tipo "Jarvis"). A fonte cita como evidência da segunda tendência o app da Anthropic oferecendo integração com Apple Health.
7. **Arquitetura de referência sugerida pelo autor para um gateway próprio**: múltiplos canais de origem → gateway/middleware único → sessão isolada por chat → controllers que escrevem nas três camadas de memória. Avaliado pelo autor como "não muito complexo" no código-fonte, com a dificuldade concentrada na organização, não na implementação.
8. **Hermes Agent liderou o ranking global de uso de tokens do OpenRouter na semana anterior ao vídeo**, superando Open Claw, Kilo Code, Claude Code e Descript — citado como sinal de tração, com ressalva explícita do autor contra tratar isso como validação de qualidade ("não quero vir aqui alimentar hype").
9. **Trade-off lock-in**: depender do "Dreaming in Claude" (feature anunciada pela Anthropic dias antes do vídeo, para revisar sessões passadas de agentes Claude e curar memórias/padrões ao longo do tempo) prende o usuário a um único provedor; hospedar um fork do Hermes (ou construir algo equivalente) permite trocar entre GPT, Claude, Gemini etc.
10. **Documentação desatualizada é pior que ausência de documentação** — tese já defendida anteriormente pelo autor, reforçada aqui no contexto de tudo virar `.md` gerido por agente (memória, skill, regras) em vez de docs estáticos mantidos manualmente.

## Entidades Mencionadas

- [[wiki/entities/anthropic]] — bug de billing no Claude Max 20; lançamento do Dreaming in Claude; integração com Apple Health citada como evidência da estratégia "Jarvis"
- [[wiki/entities/claude-code]] — comparado ao Hermes ("Hermes não é Claude Code com mais memória"); citado no ranking de tokens do OpenRouter
- [[wiki/entities/openai]] — citada de passagem (aquisição do time por trás do Open Claw)
- [[wiki/entities/hermes-agent]] (nova, stub)
- [[wiki/entities/open-claw]] (nova, stub)
- [[wiki/entities/hostinger]] (nova, stub) — bloco patrocinado, VPS
- OpenRouter, Kilo Code, Descript — citados apenas no ranking de tokens, sem página dedicada nesta ingestão (menção pontual, sem conteúdo técnico substancial para justificar stub)

## Conceitos Tocados

- [[wiki/concepts/agent-memory-tres-camadas]] (novo)
- [[wiki/concepts/closed-loop-skill-learning]] (novo)
- [[wiki/concepts/skills-agente]] — caso de skill auto-gerada via learning loop
- [[wiki/concepts/hooks-agente]] — hooks usados para pattern extraction manual, precursor do que o Hermes automatiza
- [[wiki/concepts/harness]] — comparação Hermes vs. Claude Code vs. Open Claw como harnesses concorrentes
- [[wiki/concepts/memoria-de-longo-prazo-ia]] — conceito irmão, mas de escopo diferente (RPI/refactoring plans vs. skill learning loop)
- [[wiki/concepts/mcp-arquitetura]] — mencionado indiretamente como padrão de agente conectado a ferramentas externas
- [[wiki/concepts/token-anxiety-agentes-ia-comportamento-devs]] — tema relacionado ao billing bug (ansiedade com consumo de token/orçamento)

## Contradições / Reforços com o Resto da Wiki

**Reforço direto:** [[wiki/concepts/memoria-de-longo-prazo-ia]] já documentava um padrão de memória persistida via `.md` entre sessões (fase de research → subplanos), mas com escopo específico de refatoração RPI. Esta fonte generaliza o conceito para memória de sessão/persistente/skill como arquitetura de três camadas aplicável a qualquer agente de propósito geral — tratado como conceito relacionado, não substituto, e linkado como tal.

**Reforço direto:** [[wiki/concepts/hooks-agente]] já descrevia hooks como mecanismo garantido de automação (`PostToolUse`, `Stop`, etc.). Esta fonte mostra um uso concreto adicional — hook de fim de sessão alimentando uma IA que gera padrões reutilizáveis — que não estava explicitamente coberto na página; adicionado como novo caso de uso.

**Reforço direto:** [[wiki/entities/anthropic]] já registrava o custo elevado e comportamento inesperado de billing em ferramentas da Anthropic (crash do Ultra Review consumindo saldo sem entregar resultado, relatado em [[wiki/sources/quality-gate-ratchet-multiplos-agentes-ia]]). O bug do Claude Max 20 relatado nesta fonte é um segundo incidente de billing na mesma linha — adicionado à mesma seção da entidade.

**Sem contradição encontrada** entre esta fonte e [[wiki/concepts/skills-agente]]: o padrão de skill curta e específica de domínio (não generalizável) já estava implícito no caso "workforce multiagente com skills curtas" documentado naquela página; esta fonte reforça explicitamente essa limitação.

## Open Questions

- O nome/cargo exato do representante da Anthropic citado como "Tarik" na transcrição não foi verificado externamente — tratado como não confirmado.
- Não há link ou repositório GitHub citado explicitamente na transcrição para o Hermes Agent — impossível verificar detalhes de implementação (schema FTS5, linguagem, versão) além do que foi narrado.
- O nome/identidade do autor do vídeo não é declarado explicitamente na transcrição (diferente de outras fontes já ingeridas, como Erick Wendel ou Fábio Akita, que se autoidentificam) — página de fonte não cria entidade de autor por falta de confirmação.
- "Dreaming in Claude" (feature da Anthropic) não tem página própria na wiki ainda — candidato a stub se surgir uma fonte dedicada a ela.

## Raw Quotes

> "Se o Claude encontrasse um arquivo hermes.md dentro do seu Git History, ele ia torrar os 200 dólares do plano Claude Max 20."

> "Isso não é prompt engineering, e não é o agente 'ficando mais inteligente' magicamente — é o agente reescrevendo a própria base de conhecimento dele, sempre com a permissão do usuário."

> "Documentação desatualizada é pior do que ausência de documentação."
