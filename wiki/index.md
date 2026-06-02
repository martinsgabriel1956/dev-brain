---
type: index
date_updated: 2026-06-02
---

# Wiki Index

## Sources

| Página | TL;DR |
|---|---|
| [[wiki/sources/chain-of-thought-prompting]] | CoT prompting (Wei et al., 2022) — passos intermediários como exemplares few-shot é uma capacidade emergente de ~100B+ parâmetros; supera GPT-3 fine-tuned no GSM8K via prompting apenas |
| [[wiki/sources/microsoft-prompt-engineering-guide]] | Quatro padrões de prompt engineering (Tell/Show/Describe/Remind) + Software 3.0 — guia prático da Microsoft para obter boas completions do Codex/GPT |
| [[wiki/sources/gpt3-language-models-are-few-shot-learners]] | GPT-3 (175B) formaliza in-context learning — aprender tarefas via exemplos no prompt sem atualizar pesos; few-shot rivaliza com fine-tuned SOTA em vários benchmarks |
| [[wiki/sources/logica-de-programacao-quatro-passos]] | Quatro passos para transformar qualquer problema em código: entender, decompor, criar fluxo, traduzir |
| [[wiki/sources/logica-de-programacao-o-que-e-de-verdade]] | Os 5 pilares reais: decomposição, pesquisa, repertório, projetos e intuição — e por que DSA é só parte do todo |
| [[wiki/sources/let-it-crash-nodejs-asynclocalstorage]] | Let it Crash em Node.js sem try/catch — graceful shutdown + AsyncLocalStorage para rastrear contexto por cliente |
| [[wiki/sources/agents-md-vale-a-pena-paper-zurique]] | Paper de Zurique: arquivo de contexto custa +19–20%, mas sem ele alucinação aumenta — manter enxuto com links |
| [[wiki/sources/context-engineering-codebases-grandes-rpi]] | Progressive disclosure + on-demand loading + RPI com memória de longo prazo para refatorações grandes |
| [[wiki/sources/escala-niveis-uso-ia-engenheiros]] | 7 níveis de uso de IA: do negacionista ao arquiteto — o que muda é o modelo mental, não a ferramenta |
| [[wiki/sources/estruturas-de-dados-pratica-array-hashmap-fila-pilha-arvore]] | Array, Hashmap, Fila, Pilha e Árvore — três perguntas para escolher a estrutura certa |
| [[wiki/sources/akita-como-aprender-programacao]] | Autodidatas avançam independente do material; copie código por centenas de horas; DSA é a fundação inegociável; Design Patterns são para depois |
| [[wiki/sources/soft-skills-carreira-tecnologia-eduarda]] | As 6 soft skills que separam quem executa tarefas de quem resolve problemas e cresce na carreira |
| [[wiki/sources/token-anxiety-agentes-ia-comportamento-devs]] | Como agentes de IA com janelas de token estão mudando comportamento e rotina de devs |
| [[wiki/sources/trd-technical-requirements-document]] | TRD traduz PRD em especificação técnica — contratos, NFRs, segurança; distinto de RFC (proposta aberta) e ADR (decisão registrada) |
| [[wiki/sources/architecture-decision-record]] | ADR captura decisões arquiteturais — imutável, datado, versionado com o código; RFC propõe, ADR registra |
| [[wiki/sources/request-for-comments]] | RFC propõe mudanças grandes demais para decidir em silêncio — coleta objeções antes de implementar; RFC aceito gera ADR |
| [[wiki/sources/prd]] | PRD é o artefato de alinhamento estratégico — "por quê" e "o quê" sem entrar em implementação; antecede FRD e TRD |
| [[wiki/sources/frd]] | FRD detalha fluxos funcionais e regras de negócio — derivado do PRD, base para QA e engenharia |
| [[wiki/sources/user-stories]] | User Stories são a unidade mínima de valor em contextos ágeis — Como/Quero/Para + critérios Given/When/Then |
| [[wiki/sources/high-level-design]] | HLD alinha times sobre direção do sistema antes do código — serviços, integrações e fluxo de dados |
| [[wiki/sources/low-level-design]] | LLD remove ambiguidade antes de codificar — schemas, contratos de API, estrutura de classes, sequência de chamadas |
| [[wiki/sources/runbook]] | Runbook é procedimento linear para operações repetíveis — elimina variação humana, reduz MTTR |
| [[wiki/sources/playbook]] | Playbook é árvore de decisão para incidentes com causa desconhecida — guia investigação sob pressão |
| [[wiki/sources/post-mortem]] | Post-mortem blameless analisa incidentes após resolução — 5 Porquês até causa sistêmica, action items com dono e prazo |
| [[wiki/sources/nubank-clojure-datomic-event-sourcing]] | Por que o Nubank escolheu Clojure + Datomic — imutabilidade, event sourcing e DDD como fundação para 100M clientes |
| [[wiki/sources/claude-code-guia-pratico-full-cycle]] | Claude Code na prática — CLAUDE.md, MCP, hooks, plan mode, commands, gestão de contexto e armadilhas de custo |
| [[wiki/sources/ia-e-aprendizado-programacao-iniciantes]] | Como usar IA sem parar de aprender — dois perfis, dois extremos, dependência disfarçada e o papel do esforço produtivo |
| [[wiki/sources/profissional-do-futuro-ia-identidade-aprendizado]] | Nexialista, crença de alta eficácia e observador tercerático — o profissional do futuro é o mais adaptável, não o mais atualizado |
| [[wiki/sources/ia-custo-roi-bolha-ou-realidade]] | Custo real da IA com dados — 71% sem ROI, paradoxo de Jevons, AI Washing e por que não é bolha mas curva de adoção |
| [[wiki/sources/conteudo-tecnico-ia-robustez-sistemas]] | CRUD está resolvido, sênior é escasso — o diferencial agora é harness de qualidade e sistemas robustos |
| [[wiki/sources/conteudo-tecnico-ia-hype-sistemas-robustos]] | Hype de IA é produto deliberado do ciclo VC→IPO; FOMO é estratégia; open source garante que a mudança é permanente |
| [[wiki/sources/formacao-ia-devs-aula-01-abertura]] | Abertura do Módulo 1 — LLM, Harness, Spec-Driven, Subagents; instrutores Rodrigo Branas e Pedro Nauke |
| [[wiki/sources/formacao-ia-devs-aula-01-context-harness-engineering]] | Arquitetura do harness: guias vs sensores, system prompt, memória curto/longo prazo, loop agentico como brute-force |
| [[wiki/sources/formacao-ia-devs-aula-02-rules]] | Rules = guardrails sempre no system prompt; agents.md padrão de mercado; CLAUDE.md é o outlier Anthropic; <300 linhas |
| [[wiki/sources/formacao-ia-devs-aula-03-skills]] | Skills = pastas lazy-loaded; só front-matter no system prompt; skills.sh com 100k skills; design.md padrão Google |
| [[wiki/sources/formacao-ia-devs-aula-04-qa]] | Q&A: scaffolding via CLI, refactoring legado por spec-driven, caveman tokens não resolve, mapa de navegabilidade |
| [[wiki/sources/5-dicas-performance-javascript]] | Erick Wendel: Web Streams, evitar Sync, arquitetura assíncrona, OpenTelemetry, Playwright + Artillery |
| [[wiki/sources/formacao-ia-devs-aula-02-mercado-perfil-profissional]] | L0–L4 adoption levels, token maxing, novo perfil dev, pressão de CEOs, paralelismo via worktrees |
| [[wiki/sources/formacao-ia-devs-aula-03-llm]] | LLM = gerador de tokens probabilístico; degradação >400k tokens; reasoning levels; frontier vs open-weight 2026 |
| [[wiki/sources/formacao-ia-devs-aula-04-harness]] | Harness = tudo ao redor do LLM; tool calls; 1 prompt → 40+ ciclos; contexto explícito = menos custo |
| [[wiki/sources/formacao-ia-devs-aula-05-hands-on]] | XML+Markdown template vs prompt vago; meta-prompting; plan mode manual; 3 harnesses comparados |
| [[wiki/sources/formacao-ia-devs-aula-06-qa]] | Q&A: revisão de código com IA, arquitetura importa, legado, juniores, Go como linguagem AI-friendly |
| [[wiki/sources/formacao-ia-devs-aula-01-mcp-parte1]] | MCP arquitetura: host/client/server, JSON-RPC, primitivas tools/resources/prompts — antes não havia padronização |
| [[wiki/sources/formacao-ia-devs-aula-02-mcp-parte2]] | MCPs como sensores do harness; CLI economiza contexto; file system é o padrão de mercado para contexto IA |
| [[wiki/sources/formacao-ia-devs-aula-03-plan-mode]] | Plan Mode: salvar plano em arquivo, guideline de granularidade (1 arquivo → direto, 2-3 → Plan Mode, multi-domínio → SDD) |
| [[wiki/sources/formacao-ia-devs-aula-04-agentes-planejamento]] | SDD completo: Agente PRD → Tech Spec → Tarefas isoladas; PRD é para a IA, não para a empresa |
| [[wiki/sources/formacao-ia-devs-aula-05-qa]] | Q&A: Resume retoma onde parou, padrões de arquitetura ficam em rules, SDD funciona para refactoring e migrações |
| [[wiki/sources/5-principles-that-changed-me-as-a-programmer]] | Logs estruturados são infraestrutura crítica; tech debt Prudente+Deliberado é válido; naming é custo cognitivo permanente |

## Concepts

### Carreira & Soft Skills

| Página | Hook |
|---|---|
| [[wiki/concepts/soft-skills]] | Habilidades humanas que potencializam o técnico — o multiplicador da carreira |
| [[wiki/concepts/comunicacao-tecnica]] | Ser entendido, não apenas falar — acelerador de time |
| [[wiki/concepts/colaboracao-times]] | Construir junto; empatia de papel e gestão de conflito |
| [[wiki/concepts/autonomia-responsabilidade]] | Liberdade + maturidade para alinhar expectativas antes de executar |
| [[wiki/concepts/pensamento-critico]] | Causa raiz antes do código — executor vs. solucionador |
| [[wiki/concepts/aprendizado-continuo]] | Saber aprender, não acumular cursos; mantém a carreira viva |
| [[wiki/concepts/adaptabilidade]] | Continuar performando quando o contexto muda |
| [[wiki/concepts/inteligencia-emocional]] | Operar sob pressão, crítica e conflito sem perder equilíbrio |

### Qualidade de Software com IA

| Página | Hook |
|---|---|
| [[wiki/concepts/robustez-de-sistemas]] | Palavra do ano — escalabilidade, abstrações, boundaries, testes, segurança; o que a IA não garante sozinha |
| [[wiki/concepts/let-it-crash]] | Projetar para quebrar controladamente — orquestrador recria instâncias limpas em vez de recuperar estado corrompido |
| [[wiki/concepts/graceful-shutdown]] | Sequência controlada de encerramento: responde cliente → para conexões → libera recursos → process.exit |
| [[wiki/concepts/asynclocalstorage]] | API do Node.js para rastrear contexto assíncrono por cliente sem passar parâmetros pela call stack |
| [[wiki/concepts/excecao-vs-erro]] | Erro de domínio é previsível (trata com resposta); exceção é imprevisível (Let it Crash) |
| [[wiki/concepts/progressive-disclosure-ia]] | Arquivos de contexto por diretório/responsabilidade — agente carrega só o que é relevante para a tarefa |
| [[wiki/concepts/memoria-de-longo-prazo-ia]] | Salvar output do research como .md para conectar sessões em refatorações grandes sem re-explorar o codebase |
| [[wiki/concepts/escala-maturidade-ia-dev]] | Framework de 7 níveis: o que muda não é a ferramenta, é o modelo mental — gargalo crítico no nível 2→4 |
| [[wiki/concepts/array]] | Acesso O(1) por índice; inserção/remoção no meio é O(n) — use quando a posição importa |
| [[wiki/concepts/hashmap]] | Acesso O(1) por chave; busca por identificador independente do tamanho da coleção |
| [[wiki/concepts/fila]] | FIFO — primeiro a entrar, primeiro a sair; filas de jobs, mensageria, BFS |
| [[wiki/concepts/pilha]] | LIFO — último a entrar, primeiro a sair; undo, call stack, DFS |
| [[wiki/concepts/arvore]] | O(log n) por busca; hierarquia natural; base dos índices de banco de dados |
| [[wiki/concepts/crud-resolvido]] | CRUD simples automatizado pela IA; porta de entrada do júnior fechada; sênior em escassez |
| [[wiki/concepts/harness-de-qualidade]] | Ferramental que força padrões de código bom de forma determinística ao redor da IA |
| [[wiki/concepts/pipeline-de-qualidade]] | Lint → testes → coverage → mutation → segurança → E2E; passa ou não passa |
| [[wiki/concepts/teste-de-mutacao]] | Valida que os testes realmente testam comportamento — não só executam sem quebrar |

### IA em Organizações — Custo, ROI e Adoção

| Página | Hook |
|---|---|
| [[wiki/concepts/roi-de-ia]] | Ganho individual existe (9h/semana); ROI organizacional trava por falta de processo e cultura |
| [[wiki/concepts/ai-washing]] | Usar IA como narrativa para cortes que iriam acontecer de qualquer jeito — sem correlação com ROI |
| [[wiki/concepts/paradoxo-de-jevons]] | Token mais barato → consumo cresce mais → conta maior; o paradoxo central da era agêntica |
| [[wiki/concepts/era-agentica]] | Agentes fazem tarefas inteiras; modelo de custo muda de sugestão para funcionalidade |
| [[wiki/concepts/learning-gap-organizacional]] | O gap entre qualidade do modelo e ROI capturado — só 5% (MIT) fecham esse gap |

### Agentes & LLMOps

| Página | Hook |
|---|---|
| [[wiki/concepts/agente-ia]] | Sistema baseado em LLM que executa tarefas autonomamente com loop de ação |
| [[wiki/concepts/janela-de-contexto]] | Limite de tokens por sessão; o reset é gatilho para token anxiety |
| [[wiki/concepts/context-compaction]] | Compactação automática do histórico quando a janela enche — perda de nuances inevitável |
| [[wiki/concepts/llmops]] | Práticas e cultura para operar LLMs e agentes em produção |
| [[wiki/concepts/token-anxiety]] | Ansiedade de não desperdiçar a janela de tokens — fenômeno social emergente |
| [[wiki/concepts/fomo-tecnologico]] | FOMO amplificado por releases de modelos; paradoxo: mais capacidade = mais ansiedade |
| [[wiki/concepts/burnout-dev]] | Esgotamento em dev; linha mais tênue que nunca com agentes disponíveis para todos |
| [[wiki/concepts/dopamina-produtividade]] | Loop de recompensa que torna difícil parar mesmo quando o descanso seria melhor |
| [[wiki/concepts/harness]] | Tudo ao redor do LLM: tool calls, contexto, memória, MCP, subagentes — o que dá ao modelo "olhos e mãos" |
| [[wiki/concepts/tool-call]] | Mecanismo (2023, OpenAI) que permite ao LLM requisitar execução de funções externas — game changer |
| [[wiki/concepts/ciclo-agente]] | Loop prompt → tool calls → contexto → resposta; 1 prompt pode gerar 40+ ciclos internos |
| [[wiki/concepts/degradacao-de-contexto]] | Qualidade cai após ~400k tokens; solução: auto-compact; nunca encher a janela por encher |
| [[wiki/concepts/reasoning-level]] | Low/Medium/High/Extra-High — controla tokens internos de raciocínio; extra-high ≠ sempre melhor |
| [[wiki/concepts/modelo-frontier]] | Modelos mais capazes: Opus 4.7, GPT-5.5, Gemini 3.1, Kimi K2.6, GLM 5.1 — tabela de preços 2026 |
| [[wiki/concepts/mixture-of-experts]] | Arquitetura MoE: por que modelos open source chineses são 10x mais baratos que frontier densos |
| [[wiki/concepts/token-maxing]] | Consumo compulsivo de tokens como sinal de produtividade — fenômeno do Vale do Silício, 2026 |

### Processo de Desenvolvimento com IA

| Página | Hook |
|---|---|
| [[wiki/concepts/niveis-adocao-ia-l0-l4]] | L0 (hater) → L4 (fábrica); a maioria dos devs está no L2; salto de produtividade real ocorre no L3 |
| [[wiki/concepts/spec-driven-development]] | Planning-first: spec antes de executar; LLM executa autônoma; dev revisa resultado, não linha a linha |
| [[wiki/concepts/worktree-paralelismo]] | Git worktrees isolam tarefas paralelas; base do trabalho L3 — múltiplas specs rodando simultaneamente |
| [[wiki/concepts/context-engineering-harness]] | Rules + skills + MCPs formam o "mapa" do projeto — fator decisivo de qualidade acima do modelo escolhido |
| [[wiki/concepts/rules-agente]] | Guardrails sempre no system prompt — agents.md/CLAUDE.md; onboarding digital do projeto |
| [[wiki/concepts/skills-agente]] | Pastas lazy-loaded: só front-matter no system prompt; corpo sob demanda — substitui 80% das rules |
| [[wiki/concepts/sensores-vs-guias]] | Guias direcionam antes; sensores corrigem durante — qualidade dos sensores determina autocorreção |
| [[wiki/concepts/system-prompt-arquitetura]] | O prompt escondido: rules + skills front-matter + MCPs schemas, sempre antes do prompt do usuário |
| [[wiki/concepts/memoria-curto-longo-prazo-ia]] | Short-term = context window (apagada); long-term = system prompt (sempre reinjetado) |
| [[wiki/concepts/design-md-padrao]] | Padrão Google 2026: spec de design em .md para UIs visualmente consistentes com identidade de marca |
| [[wiki/concepts/novo-perfil-dev-ia]] | Dev 2026 = tech lead/analista de sistemas; foco em planejamento e design, não em codificação linha a linha |
| [[wiki/concepts/xml-markdown-prompts]] | Tags XML + Markdown: padrão de estruturação de prompts recomendado por Anthropic e OpenAI |
| [[wiki/concepts/meta-prompting]] | Placeholders descritivos no template guiam o LLM a raciocinar ativamente sobre o que preencher |
| [[wiki/concepts/codigo-legado-ia]] | IA funciona melhor em legado que greenfield quando há referências ricas; desafio é técnica, não capacidade |
| [[wiki/concepts/model-context-protocol]] | Protocolo padrão Anthropic para integrar LLMs a ferramentas externas — "USB-C das integrações de IA" |
| [[wiki/concepts/mcp-arquitetura]] | Host/Client/Server + transportes stdio/SSE/Streamable HTTP — server deve ficar em pé, não subir e cair |
| [[wiki/concepts/cli-vs-mcp]] | CLI usa treinamento da LLM e economiza contexto; MCP expõe tools delimitadas — critério de decisão |
| [[wiki/concepts/tech-spec]] | Segundo artefato do SDD: traduz o PRD em decisões técnicas (contratos, schemas, arquitetura) |
| [[wiki/concepts/human-in-the-loop]] | HITL em três granularidades: por tool call, por plan, por etapa SDD — Plan Mode é a forma leve |
| [[wiki/concepts/task-looper]] | Executor automático de tarefas SDD — itera pela lista aprovada com critérios de aceite, sem intervenção |
| [[wiki/concepts/agente-prd]] | Agente interativo que refina requisitos com perguntas e gera o PRD para consumo do agente de Tech Spec |

### JavaScript / Node.js Performance

| Página | Hook |
|---|---|
| [[wiki/concepts/event-loop-performance-js]] | Single-thread JS: qualquer Sync bloqueia todos os clientes — Web Streams e arquitetura assíncrona como solução |

### Claude Code — Recursos e Padrões

| Página | Hook |
|---|---|
| [[wiki/concepts/claude-md]] | Arquivo de memória e regras persistentes do Claude Code — lido em toda sessão |
| [[wiki/concepts/plan-mode]] | Modo de planejamento antes de executar (Shift+Tab) — alinha antes de gastar tokens |
| [[wiki/concepts/slash-commands-agente]] | Commands customizados em .claude/commands/*.md — workflows em Markdown reutilizáveis |
| [[wiki/concepts/hooks-agente]] | Automação garantida em eventos do agente — diferente de CLAUDE.md, não pode ser ignorado |
| [[wiki/concepts/mcp-server]] | Configuração de servidores MCP no Claude Code — CLI, global vs local, permissões |

### LLMs e IA

| Página | Hook |
|---|---|
| [[wiki/concepts/prompt-engineering]] | Construção sistemática de prompts para elicitar outputs de LLMs — primeira alavanca, barata e iterável |
| [[wiki/concepts/completion]] | Texto gerado pelo modelo em resposta a um prompt — gerado token a token por modelo autoregressivo |
| [[wiki/concepts/zero-shot-learning]] | Prompt sem exemplos — só instrução; ponto de partida antes de escalar para few-shot |
| [[wiki/concepts/chain-of-thought]] | Forçar raciocínio passo a passo no prompt — melhora performance em tarefas de lógica e matemática |
| [[wiki/concepts/context-window]] | Limite máximo de tokens (prompt + completion) por chamada — restrição central de prompt engineering |
| [[wiki/concepts/hyperparameters-llm]] | Temperature, max_tokens, stop sequence — controlam como o modelo amostra tokens durante a geração |
| [[wiki/concepts/software-3]] | Terceira geração de programação (Karpathy) — lógica especificada em linguagem natural via prompts |
| [[wiki/concepts/in-context-learning]] | Aprender tarefas via exemplos no prompt, sem gradient descent — capacidade emergente de LLMs grandes |
| [[wiki/concepts/few-shot-learning]] | Variante de ICL com 10–100 exemplos; sweet spot prático é 3–5; supera fine-tuned SOTA em vários benchmarks |
| [[wiki/concepts/scaling-laws]] | Performance de LLMs segue power law em parâmetros, dados e compute — previsível e smooth |
| [[wiki/concepts/data-contamination]] | Sobreposição entre dados de treino e benchmarks de teste — problema crescente em modelos treinados em web-scale data |
| [[wiki/concepts/foundation-model]] | Modelo pré-treinado em larga escala que serve de base para downstream tasks via ICL, fine-tuning ou prompting |
| [[wiki/concepts/autoregressive-language-model]] | Arquitetura decoder-only que gera token a token — base do GPT-3 e da maioria dos LLMs modernos |
| [[wiki/concepts/fine-tuning]] | Continuar treinamento num dataset específico de tarefa — alternativa mais custosa ao ICL |
| [[wiki/concepts/emergent-ability]] | Capacidade que não existe em modelos pequenos e aparece abruptamente acima de certo limiar de escala — CoT é o exemplo canônico |

### Fundamentos de Lógica e Programação

| Página | Hook |
|---|---|
| [[wiki/concepts/logica-de-programacao]] | Raciocínio por trás das decisões que o sistema precisa tomar |
| [[wiki/concepts/decomposicao-de-problemas]] | Quebrar problemas complexos em subproblemas menores e independentes |
| [[wiki/concepts/separacao-de-responsabilidades]] | Cada módulo cuida de uma coisa só |
| [[wiki/concepts/fluxo-logico]] | Mapa de decisões desenhado antes de abrir o editor |
| [[wiki/concepts/fluxo-de-controle]] | if/while/for — materialização do fluxo lógico em código |
| [[wiki/concepts/traducao-logica-para-codigo]] | Código como tradução de decisões já tomadas, não criação |
| [[wiki/concepts/estado]] | O que o sistema precisa lembrar para tomar decisões |
| [[wiki/concepts/caminho-feliz]] | Fluxo ideal em que tudo ocorre conforme esperado |
| [[wiki/concepts/edge-case]] | Cenários fora do fluxo principal que precisam ser tratados explicitamente |
| [[wiki/concepts/algoritmos-e-estruturas-de-dados]] | A fundação que separa amadores de profissionais — DSA antes de qualquer framework |
| [[wiki/concepts/repertorio]] | Acúmulo de experiência prática que gera reconhecimento de padrões e intuição — o terceiro pilar da competência |

### Aprendizado e Mentalidade

| Página | Hook |
|---|---|
| [[wiki/concepts/autodidata]] | Quem investiga o porquê quando o procedimento falha, em vez de travar |
| [[wiki/concepts/hacker-mindset]] | Curiosidade ativa — não só faz a pergunta, mas procura a resposta |
| [[wiki/concepts/aprendizado-por-exposicao]] | Copiar código sem objetivo por centenas de horas para formar fluência |
| [[wiki/concepts/memoria-muscular]] | Familiaridade instintiva com código formada pela repetição, pré-analítica |
| [[wiki/concepts/fluencia-vs-perfeicao]] | Fluência é operar mesmo errando — perfeição no início bloqueia o aprendizado |
| [[wiki/concepts/foco-profundo]] | Estado de concentração ininterrupta incompatível com redes sociais |
| [[wiki/concepts/fundacao-tecnica]] | Multiplicador de aprendizado — torna qualquer nova tecnologia simples |
| [[wiki/concepts/aprendizado-passivo]] | Copiar código sem entender — ilusão de progresso que impede construção de raciocínio |
| [[wiki/concepts/dependencia-ia]] | Ciclo preguiçoso de prompts disfarçado de produtividade — antônimo de autonomia |
| [[wiki/concepts/autonomia-tecnica]] | Entender, explicar, modificar e sustentar código independentemente — o diferencial real |
| [[wiki/concepts/esforco-produtivo]] | O intervalo entre o problema e a ajuda; onde o aprendizado de verdade acontece |
| [[wiki/concepts/aprender-a-aprender]] | Metacognição aplicada — o superpoder do profissional do futuro; mais duradouro que qualquer ferramenta |
| [[wiki/concepts/crenca-de-alta-eficacia]] | Crença na própria capacidade de aprender — preditor de adaptação; quem não tem pode de fato ser substituído |
| [[wiki/concepts/zona-de-desconforto-da-aprendizagem]] | ZDA: aprender é biologicamente desconfortável; abraçar o caos é o mecanismo do crescimento |
| [[wiki/concepts/nexialista]] | Profissional que conecta múltiplas áreas criando soluções que especialistas isolados não conseguem |
| [[wiki/concepts/observador-tercerático]] | Conceito de Luiz Tibiriçá: co-criar novos conceitos operando cérebro orgânico e IA em paralelo |

### Arquitetura Backend & Event-Driven

| Página | Hook |
|---|---|
| [[wiki/concepts/event-sourcing]] | Persistir eventos imutáveis em vez de estado — replay para calcular estado atual; auditoria nativa |
| [[wiki/concepts/cqrs]] | Separar modelos de escrita e leitura — write emite eventos, read mantém projeções otimizadas |
| [[wiki/concepts/ddd]] | Domínio no centro, adapters na borda — aggregates, domain events, bounded context |
| [[wiki/concepts/datomic]] | Banco de dados imutável com time-travel — append-only, datoms, snapshots; fundação do Nubank |
| [[wiki/concepts/ledger-imutavel]] | Saldo = soma de transações; nunca UPDATE em entradas financeiras — padrão fintech obrigatório |
| [[wiki/concepts/programacao-funcional]] | Imutabilidade + funções puras + efeitos explícitos — paradigma que elimina complexidade acidental |
| [[wiki/concepts/imutabilidade]] | Valores que não mudam após criados — elimina bugs de estado compartilhado |
| [[wiki/concepts/efeitos-colaterais]] | Tudo que uma função faz além de retornar valor — devem ser explícitos e isolados nas periferias |
| [[wiki/concepts/complexidade-acidental]] | Complexidade que vem de implementação, não do problema — Out of the Tar Pit; mutabilidade é a maior fonte |

### Boas Práticas de Engenharia

| Página | Hook |
|---|---|
| [[wiki/concepts/logging-estruturado]] | Logs com contexto (user_id, trace_id, error) — a diferença entre "vejo o problema" e "3h chutando" |
| [[wiki/concepts/quadrante-de-fowler]] | Dois eixos: Deliberado/Inadvertido × Prudente/Imprudente; só Prudente+Deliberado é aceitável |

### Padrões e Design

| Página | Hook |
|---|---|
| [[wiki/concepts/pattern-recognition]] | Capacidade humana de detectar repetições — base do aprendizado por exposição |
| [[wiki/concepts/design-patterns]] | Catálogo de soluções nomeadas — útil só depois de já ter visto os padrões na prática |
| [[wiki/concepts/anti-pattern]] | Repetição que parece solução mas cria problemas — frequência não implica qualidade |

## Entities

| Página | Hook |
|---|---|
| [[wiki/entities/eduarda-rocket-city]] | Engenheira de software internacional, criadora de conteúdo no canal Rocket City |
| [[wiki/entities/openai]] | Organização responsável pelo GPT-3/4 — formalizou in-context learning e scaling laws |
| [[wiki/entities/jason-wei]] | Pesquisador Google Brain — lead author do paper de chain-of-thought prompting e do paper de emergent abilities |
| [[wiki/entities/fabio-akita]] | Programador brasileiro, autodidata desde 1991, criador do canal Akita On Rails |
| [[wiki/entities/john-romero]] | Co-criador de Doom — "programação é criatividade baseada em lógica" |
| [[wiki/entities/edsger-dijkstra]] | Cientista da computação holandês — programação formal, crítica à linguagem natural em código |
| [[wiki/entities/eric-lenda]] | Criador de conteúdo brasileiro — JavaScript/Node.js avançado |
| [[wiki/entities/valdemar-neto]] | Cofundador da Tech Leads Club — arquitetura, IA aplicada, conteúdo avançado |
| [[wiki/entities/steve-ex-google-amazon]] | Criador da escala de 7 níveis de uso de IA (sobrenome não identificado na fonte) |
| [[wiki/entities/christopher-alexander]] | Arquiteto que criou a linguagem de patterns original — inspiração para o GoF |
| [[wiki/entities/nikon-cotaro]] | Autor do artigo Token Anxiety (fev/2025) |
| [[wiki/entities/claude-code]] | CLI da Anthropic com agentes e janela de contexto com reset |
| [[wiki/entities/luiz-tibirica]] | Growth hacker, 42 anos, Citybank/Bradesco/Itaú — criador do conceito Observador Tercerático |
| [[wiki/entities/nubank]] | Maior banco digital da América Latina (100M clientes) — escolheu Clojure + Datomic + Event Sourcing |
| [[wiki/entities/clojure]] | Dialeto Lisp funcional na JVM — imutabilidade por default, linguagem principal do Nubank |
| [[wiki/entities/rich-hickey]] | Criador do Clojure e do Datomic — defensor de imutabilidade e design simples |
| [[wiki/entities/rodrigo-branas]] | Instrutor brasileiro, 25 anos de dev — co-criador da Formação IA para Devs; foco em harness e spec-driven |
| [[wiki/entities/pedro-nauke]] | Instrutor brasileiro, 22 anos de dev — criador do Compose; especialista em spec-driven e paralelismo de tarefas |
| [[wiki/entities/anthropic]] | Criadora do Claude e do Claude Code — definiu specs de rules/skills/MCP que viraram padrão de mercado |
| [[wiki/entities/codex-openai]] | Harness de codificação da OpenAI baseado em GPT-5.x — par do Claude Code em 2026 |

### Documentação de Arquitetura

| Página | Hook |
|---|---|
| [[wiki/concepts/trd-technical-requirements-document]] | Especificação técnica completa — o "como" entre PRD e código |
| [[wiki/concepts/prd-product-requirements-document]] | O "o quê" do produto — antecede o TRD |
| [[wiki/concepts/brd-business-requirements-document]] | O "o quê" do negócio — antecede o PRD |
| [[wiki/concepts/rfc-request-for-comments]] | Proposta aberta buscando feedback antes da decisão |
| [[wiki/concepts/adr-architecture-decision-record]] | Registro histórico de decisão arquitetural já tomada |
| [[wiki/concepts/frd-functional-requirements-document]] | Contrato funcional entre produto e engenharia — fluxos, regras de negócio, tratamento de erro |
| [[wiki/concepts/user-stories]] | Unidade mínima de valor ágil — Como/Quero/Para + critérios Given/When/Then |
| [[wiki/concepts/high-level-design]] | Primeira camada de documentação arquitetural — serviços, integrações, fluxo de dados |
| [[wiki/concepts/low-level-design]] | Zoom dentro de um componente — schemas, contratos, estrutura de classes, sequência de chamadas |

### Documentação Operacional

| Página | Hook |
|---|---|
| [[wiki/concepts/runbook]] | Passos lineares para operações repetíveis — elimina variação humana, reduz MTTR |
| [[wiki/concepts/playbook]] | Árvore de decisão para incidentes com causa desconhecida |
| [[wiki/concepts/post-mortem]] | Análise retrospectiva blameless — 5 Porquês até causa sistêmica, action items com dono e prazo |

## Questions

_(vazio)_
