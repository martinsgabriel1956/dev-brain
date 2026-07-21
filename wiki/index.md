---
type: index
date_updated: 2026-07-21
---





# Wiki Index

## Sources

| Página | TL;DR |
|---|---|
| [[wiki/sources/5-cuidados-antes-de-comecar-a-programar]] | Autoria inferida (Filipe Deschamps): 5 armadilhas de mentalidade ao aprender a programar — bomba de efeito moral (choque de complexidade que paralisa), relação criador-criatura (pedestal técnico), programar sem mirar impacto real, escolher o projeto (com "adrenalina") antes da tecnologia, e desligar autocomplete para não sabotar a spaced repetition |
| [[wiki/sources/kimi-k3-china-mercado-ia-open-source]] | Kimi K3 (Moonshot, 2,8T parâmetros, MoE 896/16 experts, até 75% economia de KV Cache) como estudo de caso: sanções de exportação de chips forçam inovação arquitetural que, ao virar open source, espalha conhecimento de inferência barata — tese central: a camada de aplicação importa mais que o modelo, lock-in em um único provedor não faz sentido |
| [[wiki/sources/8-sistemas-operacionais-explicados]] | Panorama dos 8 SOs mais conhecidos: Windows, macOS, Linux, Chrome OS, Android, iOS, Unix e BSD — propósito, mercado, vantagens e desvantagens de cada um |
| [[wiki/sources/5-dicas-entrevistas-lousa-branca-system-design]] | Full Cycle (Wesley Willians): 5 dicas para entrevista de system design/lousa branca — gerenciar tempo, requisitos core antes de desenhar, plano de capacidade, modelagem de dados/API, e só então o desenho; nunca citar tecnologia que não domina |
| [[wiki/sources/ai-jail-sandbox-para-agentes-de-ia-akita]] | AI Jail (Fábio Akita): sandbox via Bubblewrap para conter agentes de codificação de IA contra supply chain attacks (ex.: npm postinstall malicioso); modelo de 3 camadas — sessão/AI Jail, código/Git, SO imutável; comparação com o opt-out do sandbox nativo do Claude Code |
| [[wiki/sources/pos-graduacao-arquitetura-software-vale-a-pena]] | Renato Augusto: "vale a pena" sem objetivo definido não tem resposta; pós-graduação em arquitetura ensina teoria, não prática, nem em instituições renomadas; vantagens reais são networking, acesso a vagas com exigência de diploma e visão de negócio (churn, CAC, LTV) |
| [[wiki/sources/leetcode-como-se-preparar-entrevistas-coding-anthony-mays]] | Anthony D. Mays (ex-entrevistador big tech): memorize o padrão, não o problema; resposta certa não basta, processo de raciocínio importa mais; ficar travado é esperado; fazer perguntas de esclarecimento é trabalho do candidato, não do entrevistador |
| [[wiki/sources/kiss-yagni-entrega-rapida-qualidade]] | Everton Oliveira: KISS (origem Marinha dos EUA) e YAGNI como os dois princípios que resolvem o dilema velocidade vs. qualidade — exemplo de refactor de validação de status e de repositório com métodos CRUD implementados por precaução |
| [[wiki/sources/analise-curriculos-programador-junior-dicas-ats]] | Reação a currículos reais de candidatos júnior: repetição da stack-alvo para passar no ATS, ausência de GitHub como motivo de descarte explícito, formatação/legibilidade e discurso de "pensar produto" como diferenciais |
| [[wiki/sources/8-tipos-de-javascript]] | Os 8 tipos de JS (`null`, `undefined`, `boolean`, `number`, `bigint`, `string`, `symbol`, `object`); `typeof` vs. `Object.prototype.toString.call()`; `==` vs `===`; default de parâmetro (`undefined`) vs. fallback `\|\|` (qualquer falsy) |
| [[wiki/sources/filosofia-do-design-de-software-introducao]] | Tradução do cap. 1 de *A Philosophy of Software Design*: complexidade como maior limitação real ao escrever software; eliminar vs. encapsular; por que waterfall falha e design incremental funciona; red flags via code review |
| [[wiki/sources/ssh-chaves-como-funcionam]] | Chave SSH é par assimétrico (privada nunca sai da origem, pública vai pro `authorized_keys` do destino) e é unidirecional por par — `sshd_config.d` com `PubkeyAuthentication yes` + senha desativada é o padrão de indústria; `~/.ssh/config` cria aliases com `IdentitiesOnly` |
| [[wiki/sources/loop-engineering-planner-critic-grafo]] | "Você não faz o prompt, você desenha o sistema que faz o prompt" — Planner gera prompt+rúbrica dinamicamente para subagentes, Verificador (outro modelo) aprova/rejeita, grafo (nós=LLM, arestas=determinístico) é o nível de abstração |
| [[wiki/sources/teste-unitario-integracao-e2e-opiniao]] | Vídeo opinativo: teste nunca previne bug 100%, só regressão; pirâmide de testes é problema de alocação de recursos; sweet spot é teste de integração validando regra de negócio ponta a ponta |
| [[wiki/sources/9-habitos-programador-junior]] | Tom Hombergs + vídeo PT-BR: voluntariar para o desconhecido, comunicar progresso continuamente, escrever para aprender, bloquear agenda, começar do zero após pausa, e fazer tudo por você — não pelo chefe |
| [[wiki/sources/double-spend-double-submit]] | Double spend/double submit são o mesmo problema — camadas complementares: frontend desabilita botão, redirect após POST (PRG), Idempotency Key (hash gerado no servidor + storage compartilhado), e Unique Constraint no banco quando há campo genuinamente único |
| [[wiki/sources/html-vs-markdown-para-agentes-de-ia]] | HTML vs. Markdown como formato de saída de agentes — maior densidade de informação vs. ~20x mais tokens; mais um quality gate real de CI para qualidade de transcrição (Whisper local) |
| [[wiki/sources/como-vender-um-saas-sem-audiencia]] | Build in public já era: viralizar sketch sem parecer propaganda, feature vendível desde o dia zero, conhecer LTV antes do CAC, ser usuário do próprio produto |
| [[wiki/sources/pensamento-estruturado-resolucao-de-problemas]] | Resolver problemas é saber pensar, não experiência ou talento — árvore de decomposição, pensar de trás pra frente, testar hipóteses antes de agir, documentar o que se descobriu |
| [[wiki/sources/3-dicas-colocar-conhecimento-em-pratica]] | André Casciotti: não peça permissão, separe mudanças em partes coesas, use automações pessoais como veículo de prática de baixo risco |
| [[wiki/sources/como-nao-ser-humilhado-no-primeiro-code-review]] | 5 passos para reduzir a fricção do primeiro code review: regra de negócio antes de estilo, revisar com IA sem virar dependência, testar em ambiente externo, não levar comentários pro pessoal, validar em produção |
| [[wiki/sources/pare-de-terceirizar-suas-decisoes]] | Akita: pare de terceirizar decisões de carreira para influencers e de parar de cargo-cultar stack de big tech — skin in the game, antifragilidade e custo afundado |
| [[wiki/sources/3-soft-skills-que-poucos-programadores-dominam]] | Renato Augusto: comunicação persuasiva (gatilhos de urgência/ganância), imagem profissional mesmo em home office, e habilidade de lidar com pessoas (Dale Carnegie) como as soft skills que a IA não substitui |
| [[wiki/sources/tres-caracteristicas-melhor-candidato]] | Randy Nelson (ex-Pixar/Apple): profundidade via maestria em qualquer assunto (não anos de experiência), abrangência (ser interessado, não interessante) e comunicação (tradução na ponta de quem emite) |
| [[wiki/sources/acid-vs-base-garantias-bancos-de-dados]] | ACID (atomicidade, consistência, isolamento, durabilidade) vs. BASE (basically available, soft state, eventual consistency) — o tradeoff corretude/performance vs. disponibilidade/escala, e quando usar cada um |
| [[wiki/sources/vibe-coding-limites-maturidade-profissional]] | Vibe coding brilha em MVPs, protótipos, docs e testes; sistemas sustentáveis e seguros ainda exigem arquitetura, contexto de negócio e julgamento humano — vendê-los como prontos sem isso é ilusão e desonestidade |
| [[wiki/sources/sql-nao-e-banco-de-dados-uncle-bob]] | SQL é linguagem, não banco de dados — a confusão do Twitter na thread de Uncle Bob, e o que um banco relacional faz por baixo (B-tree, WAL, parser, planner) |
| [[wiki/sources/orm-sql-organizacao-regras-negocio-bancos-dados]] | Q&A: ORM inviável com relacionamentos profundos/chaves compostas força SQL direto; stored procedure com moderação; relatório sempre bate em réplica; relacional vs. não relacional depende da necessidade de junções múltiplas |
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
| [[wiki/sources/estruturas-de-dados-algoritmos-big-o-como-escolher]] | Continuação sobre Big O: escolha por operação, estrutura vs. algoritmo, quatro curvas essenciais, trade-off tempo/memória, melhor/pior/caso médio |
| [[wiki/sources/akita-como-aprender-programacao]] | Autodidatas avançam independente do material; copie código por centenas de horas; DSA é a fundação inegociável; Design Patterns são para depois |
| [[wiki/sources/quanto-tempo-aprender-programacao]] | 800–1.000 horas para júnior; cérebro aprende padrões, não sintaxe; o vale do desespero é estrutural — troque prazo por quilometragem |
| [[wiki/sources/como-strings-realmente-funcionam]] | String é slice de bytes + charset + encoding; imutabilidade existe para proteger UTF-8 de corrupção por indexação |
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
| [[wiki/sources/5-principios-que-mudaram-como-programador]] | Boy Scout Rule, evitar otimização prematura, código para o mantenedor, YAGNI e "faça a coisa mais simples que poderia funcionar" (XP) |
| [[wiki/sources/cinco-praticas-seguranca-pragmatic-programmer]] | 5 práticas do Pragmatic Programmer: superfície de ataque, menor privilégio, defaults seguros, criptografia, updates — e nunca credencial no código |
| [[wiki/sources/padroes-arquiteturais-seguranca-gatekeeper-valet-key-token-relay]] | Gatekeeper centraliza entrada, Valet Key emite credenciais temporárias, Token Relay propaga identidade — segurança nasce no design da arquitetura |
| [[wiki/sources/papinho-tech-solo-aprender-a-aprender]] | Entender ≠ aprender — EAD cria ilusão de fluência; autoconsciência de como você aprende é a variável que o professor não controla |
| [[wiki/sources/design-pattern-proxy]] | Proxy intercepta comunicação entre cliente e objeto real — cache, auth, log sem tocar na classe original nem no Controller |
| [[wiki/sources/custo-tokens-portugues-vs-ingles]] | Português custa 62% mais tokens que inglês no Anthropic — BPE treinado em corpus inglês é a causa; impacto direto no CLAUDE.md e specs |
| [[wiki/sources/product-engineer-vale-do-silicio-2026]] | Relato do Vale do Silício: o Product Engineer constrói a coisa que constrói a coisa — duas faces (senso de produto + harness), 40-50% dos usuários do Cursor não são devs |
| [[wiki/sources/aprender-antes-de-aplicar-fundamentos-e-otimizacao-prematura]] | Progressão incremental de aprendizado em 3 estágios; over-engineering ("verde neném"); otimização prematura é a raiz de todo mal (Knuth) |
| [[wiki/sources/principio-da-inversao-programador]] | 7 conselhos do pior programador invertidos via Munger/Jacobi — revela o que um bom programador deve ser; geohot: não há substituto para construir |
| [[wiki/sources/design-first-vs-code-first-referencias]] | Design First vs Code First, Design Engineer como cargo do meio, fake delay, Linear como referência máxima — design é interação, não só visual |
| [[wiki/sources/como-aprender-novas-codebases]] | Método iterativo de 10 etapas para absorver qualquer codebase — leitura como primer, exploração com intenção, tarefas core, pair programming e ciclo de revisita |
| [[wiki/sources/habitos-ruins-de-programador]] | 4 hábitos ruins que derrubam qualidade e produtividade — dizer sim para tudo, definição fraca de pronto, não testar o próprio código, PRs gigantescos |
| [[wiki/sources/como-sistemas-operacionais-funcionam]] | Do clique duplo à primeira tela: processos, threads, escalonador, memória virtual, sistema de arquivos e syscalls — tudo em milissegundos |
| [[wiki/sources/como-arquitetar-com-cache-e-redis]] | Redis como solução de cache: o que é, pontos fortes e fracos, e três padrões arquiteturais — Feature Flags, Cache-Aside e CQRS com Redis como read layer |
| [[wiki/sources/10-conceitos-fundamentais-computacao]] | Os 10 conceitos base de toda computação — do binário à abstração; a fundação que não muda mesmo quando linguagens e frameworks mudam |
| [[wiki/sources/9-algoritmos-que-todo-programador-deveria-saber]] | Nove algoritmos em três categorias — ordenação (Bubble, Insertion, Merge), busca (Linear, Binary) e grafo (DFS, BFS, Dijkstra, A*) |
| [[wiki/sources/escalabilidade-vertical-horizontal-system-design]] | Vertical vs horizontal, Load Balancer, stateless, CDN, auto scaling, sharding, replicação — quando e como escalar cada camada |
| [[wiki/sources/the-comparison-trap-in-programming-careers]] | Bastidor vs palco + familiaridade vs capacidade — as duas formas de comparação que destroem iniciantes; quatro estratégias para medir evolução contra si mesmo |
| [[wiki/sources/tokens-llm-fundamentos-typescript]] | Tokens em LLMs explicados via TypeScript — encode/decode, treino de tokenizer, trade-off de vocabulário, palavras raras custam mais tokens |
| [[wiki/sources/akita-oferta-procura-matematica-carreira]] | Lei de oferta e procura em ciclos de mercado tech; raciocínio matemático básico (juros compostos) como diferencial de carreira; apego a ferramentas como estagnação |
| [[wiki/sources/engenheiro-vs-programador-mercado-ia]] | Programador executa, engenheiro governa — o paradoxo da IA (mais código gerado = mais demanda por quem governa) e o roadmap de fundamentos em dois eixos, técnico e humano |
| [[wiki/sources/server-sent-events-sse-tempo-real]] | SSE na prática: formato `data`/`event`, polling disfarçado como erro comum, Redis Pub/Sub entre microsserviços, Singleton na conexão, auth via JWT em query string |
| [[wiki/sources/multiplos-agentes-worktrees-subagentes-claude-code]] | Worktrees (paralelismo de file system, `claude --worktree`) vs. subagentes (paralelismo de contexto, `.claude/agents/`) — quando usar cada um e o risco de excesso de skills/agentes sobrepostos |
| [[wiki/sources/golang-mercado-trabalho-frontend-para-backend]] | Go não é passageiro — cloud native por design, já consolidado em Mercado Livre/Mercado Pago/Stone; estratégia para frontend migrar: mirar pleno e usar fullstack como ponte |
| [[wiki/sources/updates-tempo-real-polling-sse-websocket]] | Polling, SSE e WebSocket sob a lente de entrevista — quando polling simples é a resposta certa, LB L4 vs L7, tópico por usuário no Redis Pub/Sub, tabela de mensagens pendentes para offline |
| [[wiki/sources/atrofia-cognitiva-ia-programacao]] | Sintaxe já era irrelevante antes da IA (autocomplete + Google); conhecimento perene (401/500, debugging de produção) é o que importa; fundação sólida torna atrofia reversível, mas quem aprendeu já com IA não tem o que recuperar |
| [[wiki/sources/tdd-sdd-bdd-era-ia]] | TDD (red-green-refactor), SDD (contrato de boundary — OpenAPI/Protobuf/GraphQL) e BDD (Gherkin) como práticas com viés comportamental que também funcionam impostas sobre IA; proibir a IA de deletar testes que falham |
| [[wiki/sources/shopify-redis-para-mysql-skip-locked-black-friday]] | Shopify substituiu reserva de estoque Redis+MySQL por MySQL puro com SKIP LOCKED; corrigiu gap locking e PK mal desenhada; gargalo real era conexão segurada pelo checkout legado, não a query de reserva; -50% leituras, -33% transações, US$ 5,1M/min na Black Friday 2025 |
| [[wiki/sources/lean-startup-para-devs-mano-deivin]] | Dev desmotivado quer largar tudo e construir seu próprio produto — Lean Startup (Eric Ries) como antídoto: validar a dor antes de codar, MVP de funcionalidade única, ciclo construir-medir-aprender, teste A/B, e apaixonar-se pelo problema, não pela solução |
| [[wiki/sources/indistraivel-nir-eyal-mano-deivin]] | Resumo de *Indistraível* (Nir Eyal): dominar gatilhos internos (anotar em vez de agir), time boxing, hackear gatilhos externos (notificações) e pactos anti-distração (esforço, preço, público) — o antídoto do autor ao próprio *Hooked* |
| [[wiki/sources/5-ou-6-dicas-para-projetos-novos]] | Checklist do primeiro dia de um projeto novo: escolha de stack (aprender vs. monetizar), estrutura documentada antes de codar, deploy imediato do boilerplate com CD automático, ORM mínima com migrations desde o dia 1, testes na pipeline antes de features, README + AGENTS.md |
| [[wiki/sources/akita-discurso-howard-roark-a-nascente-ayn-rand]] | Akita lê o discurso de Howard Roark (*A Nascente*, Ayn Rand): criador vs. parasita, independência como necessidade básica de quem cria, crítica ao altruísmo como doutrina coercitiva |
| [[wiki/sources/useeffect-problemas-e-solucoes]] | Três anti-padrões de `useEffect`: estado derivado sincronizado via effects encadeados, stale closure em contadores, fetch sem AbortController — "o melhor effect é o que você deleta" |
| [[wiki/sources/integration-test-martin-fowler]] | Martin Fowler desambigua "integration test": estreito (double + contract test, rápido) vs. amplo (serviços reais, lento); confusão irmã com unit test solitário/sociável |
| [[wiki/sources/test-double-martin-fowler]] | Fonte primária do termo "Test Double" (bliki, 2006): Dummy/Fake/Stub/Spy/Mock — taxonomia de Gerard Meszaros, relatada e divulgada por Fowler, não inventada por ele |
| [[wiki/sources/xunit-martin-fowler]] | Fonte primária da história do JUnit (bliki, 2006): do framework caseiro de Kent Beck em Smalltalk ao voo com Erich Gamma na OOPSLA 1997 até a proliferação de ports que virou a família "Xunit" |
| [[wiki/sources/gate-de-qualidade-definicoes-formais]] | Três definições formais de Quality Gate da literatura (checklist/aprovação por gate, milestone com critérios pré-definidos, ponto de verificação de Schneider) e suas características estruturais: critérios de entrada/saída, disparo por critério (não data), resultado binário, gates em paralelo |
| [[wiki/sources/quality-gate-ratchet-multiplos-agentes-ia]] | Quality gate com padrão ratchet (baseline congelada só pode melhorar/empatar) no projeto Strawberry; babysitting de PR pelo próprio agente de IA; pipeline de CI real (npm audit em dois níveis, jscpd para duplicação); comentários no código como contexto recuperável por agentes via grep |
| [[wiki/sources/iso-27001-dicionario-programador]] | SGSI organizado em torno da tríade CIA; Anexo A 2022 com 93 controles em 4 temas; controles A.8.28/A.5.15/A.5.8/A.8.25/A.5.3 relevantes para devs; Policy as Code (OPA/Gatekeeper) como implementação; ISO 42001 para governança de IA |
| [[wiki/sources/escalabilidade-horizontal-load-balancer-algoritmos]] | Tipos de load balancer (hardware/software/cloud), por que AWS/Azure separam LB de camada 4 e 7, e algoritmos de balanceamento (Round Robin, Weighted, Least Connections, Least Time, Sticky) com demo prática em Nginx |
| [[wiki/sources/operador-de-crud-vs-engenheiro-repertorio]] | "Operador de CRUD" vs. engenheiro — o mundo debaixo do CRUD (redes, Bluetooth, streams, mobile, banco de dados); IA entrega o fácil, não o simples; repertório é a cola que a IA não substitui |
| [[wiki/sources/vulnerabilidades-comuns-seguranca-apps]] | Vulnerabilidades comuns de app/SaaS além dos grandes CVEs: webhook sem validação de assinatura, IDOR/BOLA, exposição excessiva de dados, falta de rate limiting, mass assignment, TOCTOU e o anti-padrão raiz de confiar no frontend para regras de negócio |
| [[wiki/sources/produtividade-falsa-vs-verdadeira]] | Ativo vs. produtivo, Pareto 80/20, eficácia antes de eficiência, e a técnica da "pergunta do ataque cardíaco" (Tim Ferriss) para achar as poucas tarefas de real impacto |
| [[wiki/sources/apagao-de-seniors-vibe-coding]] | Vibe coding pode gerar um apagão de sêniors; kit de sobrevivência técnico contra os 4 pilares que a IA ignora — N+1 detector, property-based testing para race conditions, memory profiling, dependency/secret scanning |
| [[wiki/sources/react-19-memoization-sem-usememo-usecallback]] | React Compiler (React 19) automatiza a memoização que antes exigia useMemo/useCallback manuais; hooks manuais sobrevivem só em casos de borda (libs de terceiros, código fora das Rules of Hooks) |
| [[wiki/sources/como-criar-uma-linguagem-de-programacao]] | As 7 decisões encadeadas para criar uma linguagem: propósito → gramática/EBNF → lexer/parser/AST → sistema de tipos → modelo de execução (interpretador/nativo/bytecode+VM+JIT) → gerenciamento de memória → stdlib/ecossistema/LSP; Crafting Interpreters como recurso prático |
| [[wiki/sources/como-eu-investiria-como-programador-ate-50000]] | Lucas Montano: finanças pessoais por faixa salarial de dev (até R$ 50.000) — abaixo de R$ 5.000 investir em si mesmo bate qualquer renda fixa; reserva de emergência, dolarização via bonds, tributação de PJ e diversificação de RSU nas faixas mais altas |
| [[wiki/sources/10-conceitos-fundamentais-backend]] | As 10 ideias que sustentam qualquer backend profissional, em ordem crescente de importância: requisição/resposta → contrato de API → validação → autenticação/autorização → modelagem de dados → transações → cache → filas/workers → escala/disponibilidade → observabilidade (o meta-conceito que amarra todos) |
| [[wiki/sources/como-identificar-o-proximo-hype-tecnologico]] | Filipe Deschamps (TabNews): a tríade retorno-risco-liquidez dos investimentos aplicada a hype tecnológico — caso real Node.js no Pagar.me vs. C# na Stone, e a postura de nunca entrar num hype buscando só retorno financeiro |
| [[wiki/sources/sistemas-de-arquivos-explicados]] | Panorama cronológico de sistemas de arquivos: FAT12→FAT16→FAT32→exFAT (Microsoft), HFS→HFS+→APFS (Apple), ext2→ext3→ext4 (Linux) e ZFS — cada geração resolve o limite de tamanho ou a falta de journaling/checksum da anterior |
| [[wiki/sources/fundamentos-de-software-importam-mais-que-nunca-na-era-da-ia]] | Matt Pocock: "código não é barato" — specs to code sem inspeção degenera em vibe coding; design concept compartilhado, linguagem ubíqua, TDD e módulos profundos como antídoto |
| [[wiki/sources/tipos-de-deploy]] | Deploy vs. release, deploy manual vs. automático (a diferença é o gatilho), e seis estratégias: Recreate, Rolling, Blue/Green, Canary, A/B e Shadow deployment |
| [[wiki/sources/desenvolvedor-acima-da-media-10-itens]] | 10 itens do checklist "Liro Boy" (60 itens) para se destacar como sênior: entender o negócio, ownership proativo, contratação com barra alta, mentoria, 1:1s, PoC antes de produção, flexibilidade técnica, Extreme Ownership, trazer solução junto do problema |
| [[wiki/sources/como-um-compilador-transforma-codigo-em-instrucoes-de-maquina]] | Pipeline de 6 estágios de um compilador — lexing, parsing (AST), análise semântica (tabela de símbolos), IR, otimização (constant folding, DCE, loop unrolling, inlining) e geração de código (alocação de registradores); compilador vs. interpretador vs. JIT |
| [[wiki/sources/pub-sub-message-queue-bullmq-na-pratica]] | Pub/Sub publica um fato, message queue publica um trabalho — distinção pelo modelo de dependência (quem depende de quem); quickstart de BullMQ com producer/worker sobre Redis |
| [[wiki/sources/como-evitar-over-engineering-david-farley]] | Refuta o "triângulo de ferro" com dados DORA/Accelerate; maior problema da indústria é under-engineering, não over-engineering; walking skeleton do LMAX como antídoto contra resolver requisitos não-funcionais cedo demais |
| [[wiki/sources/diferenciais-portfolio-backend-junior]] | Para a primeira vaga de backend, o diferencial não é arquitetura sofisticada — é profissionalismo nas bases: testes de integração com banco real, Docker/deploy real, SQL além do CRUD, documentação Swagger, error handling estruturado e observabilidade |
| [[wiki/sources/acoplamento-abstracao-estado]] | Acoplamento, abstração e estado como lentes para ler código, não termos para decorar — função god acoplada vs. separação por responsabilidade, interface como abstração, estado isolado (recebe/retorna) vs. estado global mutado |
| [[wiki/sources/5-recursos-para-ser-um-desenvolvedor-melhor]] | Augusto Galego: documentação oficial, roadmap.sh, CS50, livros com custo-benefício (Refactoring sim, Clean Code com reserva), cursos até R$30 e contribuir com open source — nada substitui escrever muito código |
| [[wiki/sources/golang-mercado-salarios-pesquisa-2024]] | Go paga acima de Java em todos os níveis (maior gap no Sênior, ~R$6.000/mês); Go Developer Survey confirma 93% de satisfação; 27,7% dos devs Go no Brasil atuam remoto para o exterior contra 12% em Java |
| [[wiki/sources/hmac-integridade-mensagem-local-first-entrevista]] | Pergunta de entrevista de system design sobre integridade de mensagem: carrinho local-first sem storage no servidor — por que criptografar quebra a exibição, chave assimétrica é cara demais, e HMAC (ipad/opad derivados do mesmo segredo, duas etapas de hash) é a resposta certa contra ataque de extensão de mensagem |
| [[wiki/sources/mappers-conversao-entre-camadas]] | A mesma entidade (`Notification`) é representada de forma diferente em cada camada de uma arquitetura em camadas — mapper estático por camada (`PrismaNotificationMapper.toPrisma()`) converte entre formatos e isola o acoplamento à tecnologia, não ao domínio |
| [[wiki/sources/portas-de-rede-como-funcionam]] | Porta é um número virtual (0–65.535) que, com o IP, roteia dados ao serviço certo — faixas IANA (well-known, registered, dynamic), portas dinâmicas por conexão de saída, estados listening/established/closed, netstat na prática |
| [[wiki/sources/design-pattern-adapter]] | Renato Augusto: classe de negócio acoplada via `new` a uma lib externa de PDF (DomPDF) fere SRP e é intestável — Adapter extrai uma interface própria do domínio, e trocar de lib (DomPDF → TCPDF) passa a exigir só um novo adaptador |
| [[wiki/sources/observabilidade-ponta-a-ponta-opentelemetry-ia-amsterdam]] | Palestra em Amsterdã: OpenTelemetry como padrão vendor-neutral roteado por um Collector central; agente de IA via Grafana MCP correlaciona métricas/logs/traces sozinho e acha causa raiz em código — "o ouro está nos dados, não na IA" |
| [[wiki/sources/o-que-e-refatoracao-quando-usar]] | Bernardo Lobato: refatoração é mudar estrutura interna sem alterar comportamento externo — dois chapéus de Kent Beck, God Class nascendo sprint a sprint sob prazo, testes na base da pirâmide como rede de segurança, passos pequenos, refatoração oportunista vs. planejada |
| [[wiki/sources/rust-por-que-tanto-hype-ownership-borrowing-lifetimes]] | Ownership (um dono por valor), borrowing (`&`/`&mut` — N leitores OU 1 escritor) e lifetimes (referência nunca outlive o valor) eliminam use-after-free, double-free e data races em compile-time, sem GC — trade-off: aprendizado e compilação mais lentos |
| [[wiki/sources/cognitive-debt-margaret-storey]] | Fonte primária de "cognitive debt": dívida técnica mora no código, dívida cognitiva mora na cabeça do time — fundamentada na teoria de Peter Naur (1985) de que um programa é uma teoria, não o código-fonte |
| [[wiki/sources/custo-real-ia-tokens-produtividade-demissoes]] | Episódio CDF Café: produtividade com IA é real mas custo sobe (caso Uber), Gartner projeta custo de codificação superando salário médio até 2028, 59% das empresas usam IA como bode expiatório para demissões, Meta admite erro de reestruturação, capital de tokens (Nadella) |
| [[wiki/sources/rfcs-grill-me-e-o-risco-da-preguica-no-vibe-coding]] | Episódio CDF Café: RFC como source of truth anti-alucinação (80/20 planejamento/execução), especificações agnósticas à linguagem (Fabrício Arcanjo), skill Grill Me (Matt Pocock) invertendo quem revisa quem, quality gates forçando modularização |
| [[wiki/sources/underengineering-overengineering-mario-souto]] | Mário Souto (DevSoutinho): under-engineering é mais comum que over-engineering — não reinventar libs maduras (React Hook Form, Tailwind), variável de ambiente em vez de hardcode na Vercel, acoplamento login/criar conta, CI mínimo de ~31 linhas (lint+teste) com branch protection |
| [[wiki/sources/sistema-produtividade-ia-adapta]] | Sistema pessoal de produtividade em 3 pilares (planejamento/priorização/execução): dump mental + regra dos 5 minutos, matriz de Eisenhower + tarefa principal do dia, execução via Adapta (skills de contexto pessoal + roteamento automático de modelo) |
| [[wiki/sources/deploy-blue-green-na-pratica-vps-nginx]] | Demo prática de blue/green numa VPS única: Nginx como reverse proxy trocando entre duas portas via script, sem Kubernetes; deploy 100% manual via SSH como etapa antes de automatizar |
| [[wiki/sources/application-boundary-martin-fowler]] | Martin Fowler (bliki, 2003): aplicações são construções sociais — devs, negócio e financiadores enxergam "unidade única" de formas diferentes; fronteiras são traçadas por política, não por critério técnico; contra a previsão de que SOA extinguiria aplicações |

## Concepts

### Onboarding & Aprendizado de Codebase

| Página | Hook |
|---|---|
| [[wiki/concepts/onboarding-de-codebase]] | Método iterativo para absorver qualquer codebase — 10 etapas que se aprofundam a cada volta |
| [[wiki/concepts/exploracao-com-intencao]] | Seguir o fio de uma feature real no código em vez de navegar aleatoriamente |
| [[wiki/concepts/modelo-mental-de-fluxo-de-dados]] | Representação interna de como dados fluem na codebase — o objetivo final do onboarding |
| [[wiki/concepts/aprendizado-por-impressoes]] | Cada exposição ao mesmo conceito aprofunda a compreensão — spaced exposure em codebases |
| [[wiki/concepts/pair-programming]] | Programação em par como acelerador de aprendizado — observe antes de participar |
| [[wiki/concepts/aprender-ensinando]] | Explicar para ser testado revela exatamente onde estão os gaps de compreensão |
| [[wiki/concepts/good-first-issue]] | Tarefa de entrada que toca o core do sistema — contribui e aprende ao mesmo tempo |
| [[wiki/concepts/entendimento-de-dominio]] | Saber para quê e para quem o software existe — fundação de decisões arquiteturais boas |
| [[wiki/concepts/testes-como-aprendizado]] | Escrever testes força compreensão do comportamento esperado — valida entendimento com feedback |
| [[wiki/concepts/ciclo-de-revisita]] | Repetir as etapas do onboarding com profundidade crescente a cada volta |

### Carreira & Soft Skills

| Página | Hook |
|---|---|
| [[wiki/concepts/soft-skills]] | Habilidades humanas que potencializam o técnico — o multiplicador da carreira |
| [[wiki/concepts/code-review]] | Regra de negócio antes de estilo — e por que o primeiro review de um júnior costuma vir cheio de comentários |
| [[wiki/concepts/sindrome-do-impostor]] | Confundir "código reprovado" com "eu fui reprovado" — o gatilho mais comum no primeiro emprego |
| [[wiki/concepts/comunicacao-tecnica]] | Ser entendido, não apenas falar — acelerador de time |
| [[wiki/concepts/colaboracao-times]] | Construir junto; empatia de papel e gestão de conflito |
| [[wiki/concepts/autonomia-responsabilidade]] | Liberdade + maturidade para alinhar expectativas antes de executar |
| [[wiki/concepts/pensamento-critico]] | Causa raiz antes do código — executor vs. solucionador |
| [[wiki/concepts/aprendizado-continuo]] | Saber aprender, não acumular cursos; mantém a carreira viva |
| [[wiki/concepts/adaptabilidade]] | Continuar performando quando o contexto muda |
| [[wiki/concepts/inteligencia-emocional]] | Operar sob pressão, crítica e conflito sem perder equilíbrio |
| [[wiki/concepts/dados-vs-intuicao]] | Dados superam intuição especialmente em ideias inovadoras — quanto menos dados, mais fortes e perigosas são as opiniões |
| [[wiki/concepts/maturidade-tecnica]] | Capacidade de extrair aprendizado de qualquer situação, incluindo as adversas |
| [[wiki/concepts/profundidade-e-maestria]] | Maestria em qualquer assunto (mesmo fora da área técnica) é prognóstico de sucesso em qualquer outro problema — o "hardware mental" se transfere |
| [[wiki/concepts/abrangencia-profissional]] | Ser interessado, não apenas interessante — sinal é se curvar para frente ao ouvir um problema, não chegar com a solução pronta |
| [[wiki/concepts/entrevista-tecnica-coding]] | Memorize o padrão, não o problema — processo de raciocínio e perguntas de esclarecimento importam mais que a resposta certa |
| [[wiki/concepts/entrevista-system-design]] | Whiteboard interview: requisitos core antes de desenhar, plano de capacidade, modelagem de dados/API, e só então o high-level design |
| [[wiki/concepts/networking-de-carreira]] | Mercado invisível de indicações — quanto mais sênior o cargo, mais a vaga é preenchida por "você conhece alguém?" em vez de vaga aberta |
| [[wiki/concepts/credencialismo-formacao-formal]] | Diploma como proxy de disciplina, não de competência técnica — "tecnologia se ensina, disciplina não" |
| [[wiki/concepts/definicao-de-objetivo-antes-de-decisao]] | "Vale a pena" sem objetivo definido é como perguntar se um avião vale a pena sem saber o destino |

### Recursos de Aprendizado

| Página | Hook |
|---|---|
| [[wiki/concepts/roadmap-sh]] | Mapa ordenado de tópicos por área (284k stars no GitHub) — direcionamento, não profundidade |
| [[wiki/concepts/documentacao-oficial-como-recurso]] | Ler a doc do próprio framework — recurso óbvio e mais negligenciado |
| [[wiki/concepts/cs50]] | Curso gratuito de Harvard como base de fundamentos para quem não fez faculdade |
| [[wiki/concepts/livros-recomendados-programador]] | Refactoring com endosso pleno, Clean Code com reserva explícita — custo-benefício como critério |
| [[wiki/concepts/contribuir-open-source]] | Contribuir com o que você já usa — good first issue como ponto de entrada |
| [[wiki/concepts/custo-beneficio-cursos-online]] | R$20-30 compensa, R$5-10 mil para uma tecnologia pontual não |
| [[wiki/concepts/aprendizado-multimodal]] | Curso + documentação + projeto ao mesmo tempo, não em sequência |
| [[wiki/concepts/atualizacao-tecnologica]] | Custo de ficar estagnado vs. fadiga de perseguir novidades — empresa que não evoluiu na stack também não evoluiu na cultura |
| [[wiki/concepts/comparacao-na-carreira]] | Medir seu primeiro degrau pela régua de quem está no meio da escada — o erro que leva à desistência prematura |
| [[wiki/concepts/familiaridade-vs-capacidade]] | Velocidade inicial ≠ talento — é histórico acumulado de vida; linha de largada explica tudo |
| [[wiki/concepts/linha-de-largada]] | Ponto de partida determinado por exposição anterior, não aptidão — invalida comparações de velocidade |
| [[wiki/concepts/log-de-aprendizado]] | Registro semanal de aprendizado que torna visível a evolução sub-perceptível no dia a dia |
| [[wiki/concepts/disciplina-vs-talento]] | Disciplina consistente supera talento no longo prazo — a única competição válida é com o eu do passado |
| [[wiki/concepts/ciclo-de-mercado-tech]] | Mercado tech segue ciclos de abundância e depressão por oferta e procura — ciclo de abundância atual está terminando |
| [[wiki/concepts/apego-a-ferramentas]] | Prender-se à primeira ferramenta aprendida é sinal de estagnação, não de expertise — martelo e chave de fenda |
| [[wiki/concepts/engenheiro-vs-programador]] | Programador executa dentro de um espaço definido; engenheiro questiona a formulação do problema e governa a complexidade — mentalidade, não título |
| [[wiki/concepts/governanca-de-codigo-gerado-por-ia]] | Quanto mais IA gera código, mais se precisa de engenheiros para governá-lo — metralhadora para quem não sabe mirar |
| [[wiki/concepts/pensamento-em-producao]] | Código escrito é 10% do trabalho; os outros 90% são o sistema rodando em produção com usuários reais |
| [[wiki/concepts/arquitetura-de-software]] | Não existe arquitetura boa para tudo — existe arquitetura certa para o contexto certo |
| [[wiki/concepts/contexto-organizacional-para-arquitetura]] | Maturidade de plataforma, processo e know-how da empresa como restrição real de arquitetura — não só a tecnologia "certa" em abstrato |
| [[wiki/concepts/confidencialidade-de-dados-em-prompts-ia]] | Não jogar código ou dado corporativo sigiloso em ferramentas de IA de terceiros fora do perímetro da empresa |
| [[wiki/concepts/ponte-fullstack-para-especializacao]] | Migrar de frontend para backend numa stack de nicho (Go): mirar pleno, não júnior, e usar vaga fullstack como ponte de entrada |
| [[wiki/concepts/sintaxe-vs-conhecimento-perene]] | Memorizar sintaxe já era irrelevante antes da IA — o que não se atrofia é o julgamento sobre causa/efeito (erros HTTP, debugging de produção) |
| [[wiki/concepts/ativo-vs-produtivo]] | Terminar tarefas no prazo mas preencher o resto do tempo com atividade de aparência produtiva não é ser produtivo — é procrastinação sofisticada |
| [[wiki/concepts/principio-de-pareto]] | 80% dos resultados vêm de 20% do esforço — fazer bem feito ou gastar muito tempo numa tarefa não a torna importante |
| [[wiki/concepts/eficacia-vs-eficiencia]] | Eficácia é fazer a coisa certa; eficiência é fazer qualquer coisa de forma econômica — otimizar a execução antes de validar a tarefa é o erro padrão |
| [[wiki/concepts/tecnica-do-ataque-cardiaco]] | "Se você só pudesse trabalhar 2h/dia, no que trabalharia?" — técnica de Tim Ferriss para achar as tarefas de real impacto |
| [[wiki/concepts/sobrecarga-de-informacao]] | Riqueza de informação cria pobreza de atenção (Herbert Simon) — consumir conteúdo sem aplicação é desperdício disfarçado de aprendizado |
| [[wiki/concepts/decisao-terceirizada]] | Pedir para influencer/palestrante decidir sua carreira por você — falha porque ninguém tem contexto da sua história nem skin in the game |
| [[wiki/concepts/skin-in-the-game]] | Só vale ouvir com propriedade quem arca com o prejuízo se o próprio conselho der errado |
| [[wiki/concepts/antifragilidade]] | Antifrágil não é prejuízo zero, é pouco prejuízo — apostar em várias tecnologias/décadas em vez de tentar acertar 100% |
| [[wiki/concepts/cargo-cult-tecnologico]] | Copiar a stack de Netflix/Google/Facebook sem ter a escala deles — compare-se com o dia um delas, não com a versão madura |
| [[wiki/concepts/falacia-do-custo-afundado]] | Continuar um livro/curso ruim só porque já investiu tempo nele só aumenta o prejuízo |
| [[wiki/concepts/curva-de-adocao-tecnologica]] | Toda tecnologia segue uma curva em S — início devagar, crescimento exponencial, desaceleração; nada dura para sempre |
| [[wiki/concepts/granularidade-de-mudanca]] | Mudança grande gera barreira grande — separe em partes pequenas e coesas que ainda gerem valor real |
| [[wiki/concepts/automacao-pessoal-para-aprender]] | Automações pessoais fora do pipeline da empresa como veículo de prática deliberada de baixo risco |
| [[wiki/concepts/comunicacao-persuasiva]] | Vender decisão técnica (refatoração) com gatilhos de urgência/ganância em linguagem de negócio, não em jargão técnico |
| [[wiki/concepts/imagem-profissional]] | Aparência mesmo em home office afeta autopercepção e percepção alheia de liderança — evidência citada é fraca/não rastreável |
| [[wiki/concepts/habilidade-de-lidar-com-pessoas]] | Confiança e influência interpessoal (Dale Carnegie) como maior alavanca de sucesso profissional segundo Renato Augusto — estatística 85/15 sem fonte primária rastreável |
| [[wiki/concepts/reserva-de-emergencia]] | Colchão de liquidez de ~3 meses via Tesouro Selic — não maximiza retorno, existe para permitir assumir riscos de carreira sem risco de ruína |
| [[wiki/concepts/freelance-como-alavanca-de-renda]] | Um freela de R$ 500 aumenta renda mensal em 1/3 quando a base é baixa — retorno que nenhuma renda fixa entrega no mesmo prazo |
| [[wiki/concepts/dolarizacao-de-renda]] | Diluir risco político/cambial via bonds corporativos em dólar (nota de crédito externo) sem precisar de conta no exterior |
| [[wiki/concepts/holding-patrimonial]] | Estrutura societária para múltiplas PJs/fontes de renda em faturamento alto — estratégias de tributação impossíveis via CPF pessoa física |
| [[wiki/concepts/dev-e-negocio]] | Dev acima da média entende o que gera receita (ou economiza custo) e opera nessa camada de negócio, não só na técnica |
| [[wiki/concepts/ownership-proativo]] | Puxar responsabilidade por um projeto de alto impacto antes que caia no colo — com clareza prévia do que é sucesso |
| [[wiki/concepts/contratacao-barra-alta]] | Envolver-se no processo de contratação e filtrar pela pessoa que mais faz bem à empresa — decide o jogo de longo prazo do time |
| [[wiki/concepts/mentoria-tecnica]] | Sênior que replica conhecimento para júniors acelera o crescimento deles e preserva a cultura técnica ao longo do tempo |
| [[wiki/concepts/one-on-one]] | Reunião individual cara a cara em sala fechada — mecanismo principal para descobrir o que reuniões de status não revelam |
| [[wiki/concepts/prova-de-conceito]] | Testar tecnologia emergente em protótipo pequeno antes de arriscar produto consolidado — mata a ansiedade sem colocar valor em risco |
| [[wiki/concepts/flexibilidade-tecnica]] | Aceitar múltiplas visões e soluções válidas — inflexibilidade trava inovação e tira espaço de crescimento de outros |
| [[wiki/concepts/extreme-ownership]] | Jocko Willink/Leif Babin: o líder é responsável por tudo que acontece no time — sem desculpas, sem terceirizar culpa |
| [[wiki/concepts/problema-com-solucao]] | Trazer problema ao gestor sempre com uma sugestão de solução — distingue quem quer resolver de quem só reclama |
| [[wiki/concepts/dump-mental]] | Capturar tudo que está na cabeça num único lugar antes de organizar — elimina o custo mental de tentar lembrar tudo |
| [[wiki/concepts/regra-dos-5-minutos]] | Se leva menos de 5 minutos, faça na hora em vez de anotar para depois |
| [[wiki/concepts/matriz-de-eisenhower]] | Quatro quadrantes (urgente × importante) para parar de tratar tudo como prioridade |
| [[wiki/concepts/tarefa-principal-do-dia]] | Eleger uma única tarefa que, se cumprida, já torna o dia bem-sucedido — MIT |
| [[wiki/concepts/gatilho-interno-vs-externo]] | Gatilho externo vem de fora (notificação); interno vem de dentro (uma lembrança no meio de outra tarefa) — o segundo é o mais negligenciado, e o antídoto é anotar em vez de agir na hora |
| [[wiki/concepts/time-boxing]] | Alocar intervalo fixo para cada bloco de trabalho — agrupa tarefas simples, protege blocos complexos, dá vazão a gatilhos internos sem quebrar o foco atual |
| [[wiki/concepts/pactos-anti-distracao]] | Pacto de esforço (fricção física), de preço (aposta cobrada por terceiro) e público (declaração social) — deslocam a decisão de resistir à distração para antes do momento de tentação |

### Produto & Lean Startup

| Página | Hook |
|---|---|
| [[wiki/concepts/lean-startup]] | Metodologia de Eric Ries para validar produtos antes de construir — visão, construir-medir-aprender, aprendizagem validada, contabilização de inovação, crescimento sustentável, pivô ou persevere |
| [[wiki/concepts/build-measure-learn]] | Ciclo iterativo central do Lean Startup — MVP de funcionalidade única, funil medido com estranhos, aprendizado por conversa direta com usuários |
| [[wiki/concepts/validacao-de-problema]] | Confirmar que a dor é real e compartilhada antes de pensar em solução — a concorrência real costuma ser uma solução informal já em uso (WhatsApp, planilha) |
| [[wiki/concepts/aprendizagem-validada]] | Teste A/B para decidir entre hipóteses de produto com dados, não achismo |
| [[wiki/concepts/contabilizacao-de-inovacao]] | Consolidar faturamento, retenção e monetização depois que o produto já está validado |
| [[wiki/concepts/pivotar-ou-perseverar]] | Decisão entre mudar de direção ou dobrar a aposta — possível sem trauma porque a paixão é pelo problema, não pela solução |
| [[wiki/concepts/inovacao-continua]] | Manter a essência validada e adicionar novas frentes sem perdê-la — Uber e iFood como exemplos |
| [[wiki/concepts/produto-vendivel-desde-o-dia-zero]] | Primeira feature já deve ser vendível — não lançar grátis esperando apego para converter depois |
| [[wiki/concepts/ltv-cac]] | Não investir em aquisição sem saber o LTV — tráfego "orgânico sintético" também tem custo |
| [[wiki/concepts/marketing-organico-viral]] | Sketch de produto que viraliza sem parecer propaganda — build in public deixou de ser pré-requisito |

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
| [[wiki/concepts/pub-sub]] | Publisher/subscriber — publica um fato para quem estiver ouvindo; fan-out, desacoplamento total via broker |
| [[wiki/concepts/mensageria]] | Comunicação assíncrona via broker — queue (consumo único) vs. stream (replay); Kafka, SQS, RabbitMQ |
| [[wiki/concepts/bullmq]] | Lib de filas para Node.js/Bun sobre Redis — producer/worker como processos independentes, sem chamada de função direta |
| [[wiki/concepts/pilha]] | LIFO — último a entrar, primeiro a sair; undo, call stack, DFS |
| [[wiki/concepts/arvore]] | O(log n) por busca; hierarquia natural; base dos índices de banco de dados |
| [[wiki/concepts/crud-resolvido]] | CRUD simples automatizado pela IA; porta de entrada do júnior fechada; sênior em escassez |
| [[wiki/concepts/harness-de-qualidade]] | Ferramental que força padrões de código bom de forma determinística ao redor da IA |
| [[wiki/concepts/pipeline-de-qualidade]] | Lint → testes → coverage → mutation → segurança → E2E; passa ou não passa |
| [[wiki/concepts/teste-de-mutacao]] | Valida que os testes realmente testam comportamento — não só executam sem quebrar |
| [[wiki/concepts/gaming-de-testes-por-ia]] | IA deleta ou enfraquece testes que falham em vez de corrigir o código — proibir explicitamente |
| [[wiki/concepts/apagao-de-seniors]] | Risco de escassez de sêniors se vibe coding virar padrão: menos gente aprende fundamentos, mais gente só orquestra prompts |
| [[wiki/concepts/n-plus-um-detector]] | Middleware que conta queries por request e alerta quando ultrapassa threshold — detecta N+1 antes de produção |
| [[wiki/concepts/property-based-testing]] | Bombardeia função com inputs aleatórios/concorrentes e verifica invariante — eficaz contra race conditions geradas por IA |
| [[wiki/concepts/adaptive-thinking]] | Modelo decide sozinho quanto "pensar"; hipótese de que remove controle do usuário para gerenciar custo de inferência |

### Perfil Profissional & Product Engineering

| Página | Hook |
|---|---|
| [[wiki/concepts/product-engineer]] | Constrói a coisa que constrói a coisa — senso de produto + harness; o cargo do dev em 2026 |
| [[wiki/concepts/taste-dev]] | Julgamento estético e de qualidade sem regra explícita — o diferencial do Product Engineer |

### IA em Organizações — Custo, ROI e Adoção

| Página | Hook |
|---|---|
| [[wiki/concepts/roi-de-ia]] | Ganho individual existe (9h/semana); ROI organizacional trava por falta de processo e cultura |
| [[wiki/concepts/ai-washing]] | Usar IA como narrativa para cortes que iriam acontecer de qualquer jeito — sem correlação com ROI |
| [[wiki/concepts/paradoxo-de-jevons]] | Token mais barato → consumo cresce mais → conta maior; o paradoxo central da era agêntica |
| [[wiki/concepts/era-agentica]] | Agentes fazem tarefas inteiras; modelo de custo muda de sugestão para funcionalidade |
| [[wiki/concepts/learning-gap-organizacional]] | O gap entre qualidade do modelo e ROI capturado — só 5% (MIT) fecham esse gap |
| [[wiki/concepts/capital-de-tokens]] | Nadella: consumo de tokens como novo capital organizacional, análogo ao capital humano |

### Token Economics & Custo

| Página | Hook |
|---|---|
| [[wiki/concepts/token-tax-multilingual]] | Português paga 62% mais tokens que inglês — BPE favorece idiomas com mais dados de treinamento |
| [[wiki/concepts/byte-pair-encoding]] | Algoritmo que transforma texto em tokens — otimizado para inglês, penaliza idiomas não-ingleses |
| [[wiki/concepts/tokenizacao]] | O que é um token, pipeline encode/decode, e por que o tamanho do vocabulário é o trade-off central |

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
| [[wiki/concepts/loop-engineering]] | Degrau seguinte a harness engineering: desenhar o ciclo completo como estrutura repetível, disparável por prompt, schedule ou evento |
| [[wiki/concepts/planner-executor-critic]] | Planner gera prompt+rúbrica para subagentes; Critic (modelo distinto do executor) aprova ou devolve follow-up |
| [[wiki/concepts/rubrica-de-verificacao]] | Critérios explícitos de aceite gerados junto com o prompt — contrato entre Planner e Verificador |
| [[wiki/concepts/langgraph]] | Framework que representa estado de agente como grafo — nodes são passos, edges são transições condicionais |
| [[wiki/concepts/grafo-como-abstracao-de-agentes]] | G=(V,E): nós são computação/LLM, arestas são condição de fluxo determinística — abstração independente de framework |
| [[wiki/concepts/roteamento-automatico-de-modelo]] | Camada que escolhe automaticamente qual LLM responde cada prompt (complexity/cascade/intent-based) — caso comercial: Adapta ONE |
| [[wiki/concepts/kv-cache]] | Cache de chaves/valores de atenção — evita reprocessar contexto a cada token; Kimi K3 promete até 75% de economia |
| [[wiki/concepts/export-controls-chips-ia]] | Sanções de exportação de chips NVIDIA para a China — pressão de fundo por trás de inovação arquitetural em MoE/KV Cache |
| [[wiki/concepts/corrida-preco-qualidade-llm]] | Concorrência entre frontier fechado e open source empurra preço para baixo e qualidade para cima simultaneamente |
| [[wiki/concepts/camada-de-aplicacao-vs-modelo]] | Com modelos cada vez mais equivalentes, a vantagem competitiva migra do modelo para a camada de aplicação |

### Dívida Cognitiva & Teoria do Programa

| Página | Hook |
|---|---|
| [[wiki/concepts/divida-cognitiva]] | Dívida técnica mora no código; dívida cognitiva mora na cabeça do time — IA acelera a segunda sem reduzir a primeira |
| [[wiki/concepts/comprehension-debt]] | Erosão progressiva e individual da capacidade de entender o próprio código aprovado — "mais 5 minutos de prompt" vira 5 horas |
| [[wiki/concepts/teoria-do-programa-naur]] | Peter Naur (1985): um programa é uma teoria na mente de quem o construiu, não o código-fonte — base teórica de "cognitive debt" |

### Processo de Desenvolvimento com IA

| Página | Hook |
|---|---|
| [[wiki/concepts/niveis-adocao-ia-l0-l4]] | L0 (hater) → L4 (fábrica); a maioria dos devs está no L2; salto de produtividade real ocorre no L3 |
| [[wiki/concepts/spec-driven-development]] | Planning-first: spec antes de executar; LLM executa autônoma; dev revisa resultado, não linha a linha |
| [[wiki/concepts/worktree-paralelismo]] | Git worktrees isolam tarefas paralelas; base do trabalho L3 — múltiplas specs rodando simultaneamente |
| [[wiki/concepts/subagentes]] | Paralelismo a nível de contexto — subtarefas convergem numa única PR; model/tools customizáveis por agente |
| [[wiki/concepts/context-engineering-harness]] | Rules + skills + MCPs formam o "mapa" do projeto — fator decisivo de qualidade acima do modelo escolhido |
| [[wiki/concepts/rules-agente]] | Guardrails sempre no system prompt — agents.md/CLAUDE.md; onboarding digital do projeto |
| [[wiki/concepts/skills-agente]] | Pastas lazy-loaded: só front-matter no system prompt; corpo sob demanda — substitui 80% das rules; skill Grill Me inverte quem revisa quem |
| [[wiki/concepts/quality-gate]] | Ponto de verificação com critérios de entrada/saída, resultado binário e disparo por critério (não data); na prática, limites estruturais (tamanho de função/arquivo, duplicação) em CI forçam a IA a modularizar o próprio código gerado |
| [[wiki/concepts/ratchet-baseline]] | "Catraca" de qualidade: baseline de métricas (lint, duplicação, cobertura, tamanho de arquivo) congelada em CI; nenhum PR pode piorá-la, só melhorar ou empatar |
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
| [[wiki/concepts/investigacao-de-incidentes-com-ia-e-mcp]] | Agente com Grafana MCP correlaciona métricas/logs/traces sozinho e acha causa raiz em código — semanas de investigação viram minutos, mas só se os dados já existirem |
| [[wiki/concepts/cli-vs-mcp]] | CLI usa treinamento da LLM e economiza contexto; MCP expõe tools delimitadas — critério de decisão |
| [[wiki/concepts/tech-spec]] | Segundo artefato do SDD: traduz o PRD em decisões técnicas (contratos, schemas, arquitetura) |
| [[wiki/concepts/human-in-the-loop]] | HITL em três granularidades: por tool call, por plan, por etapa SDD — Plan Mode é a forma leve |
| [[wiki/concepts/task-looper]] | Executor automático de tarefas SDD — itera pela lista aprovada com critérios de aceite, sem intervenção |
| [[wiki/concepts/agente-prd]] | Agente interativo que refina requisitos com perguntas e gera o PRD para consumo do agente de Tech Spec |

### JavaScript / Node.js Performance

| Página | Hook |
|---|---|
| [[wiki/concepts/event-loop-performance-js]] | Single-thread JS: qualquer Sync bloqueia todos os clientes — Web Streams e arquitetura assíncrona como solução |
| [[wiki/concepts/tipos-primitivos-javascript]] | Os 8 tipos de JS e por que `typeof null === "object"` — `Object.prototype.toString.call()` como checagem mais precisa |

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
| [[wiki/concepts/html-vs-markdown-formato-de-saida-agentes]] | HTML tem maior densidade de informação que Markdown para output de agentes (tabelas, diagramas, interações), ao custo de muito mais tokens — sem consenso ou benchmark formal |
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

### Fundamentos de Sistemas Operacionais

| Página | Hook |
|---|---|
| [[wiki/concepts/processo]] | Instância em execução de um programa — PID, ciclo de vida (new→ready→running→waiting→terminated), memória isolada |
| [[wiki/concepts/thread]] | Unidade de execução dentro de um processo — compartilha memória, mais barata que processo, risco de race condition |
| [[wiki/concepts/deadlock]] | Bloqueio mútuo eterno — duas threads esperam uma pela outra; prevenção via ordenação de locks ou timeout |
| [[wiki/concepts/mutex]] | Chave de porta para seções críticas — garante que só uma thread acessa o recurso compartilhado por vez |
| [[wiki/concepts/escalonador]] | Árbitro do processador — Round-Robin, filas de prioridade, aging; Linux usa CFS para processos normais |
| [[wiki/concepts/context-switch]] | Troca de processo no processador — salva/restaura estado completo; TLB flush é o custo extra entre processos |
| [[wiki/concepts/interrupcao-de-hardware]] | Sinal que para o processador e transfere controle ao SO — timer, teclado, disco; base do escalonador preemptivo |
| [[wiki/concepts/memoria-virtual]] | Cada processo crê ter toda a memória — page table traduz virtual→físico; page fault é o custo do miss |
| [[wiki/concepts/swap]] | Extensão da RAM no disco — páginas frias movidas para liberar RAM; uso excessivo causa thrashing |
| [[wiki/concepts/sistema-de-arquivos]] | Abstração sobre blocos do disco — nomes, hierarquia, tabela de blocos; deletar só remove a referência |
| [[wiki/concepts/journaling]] | Write-ahead log de disco — registra mudanças antes de aplicá-las; troca throughput por resiliência a queda de energia |
| [[wiki/concepts/fat32]] | FAT12→FAT16→FAT32: cada geração destrava um limite de tamanho; sobrevive hoje só por compatibilidade universal |
| [[wiki/concepts/exfat]] | Meio-termo Microsoft entre FAT32 e NTFS — limite de arquivo quase ilimitado, sem journaling; padrão de mídia portátil Win+Mac |
| [[wiki/concepts/ntfs]] | Sistema de arquivos padrão do Windows — journaling, permissões, criptografia, compressão; fraco fora do ecossistema Windows |
| [[wiki/concepts/apfs]] | HFS→HFS+→APFS: linhagem Apple, salto de HD para SSD/flash em 2017 — criptografia forte, snapshots |
| [[wiki/concepts/ext4]] | ext2→ext3→ext4: padrão do Linux, journaling desde o ext3, até 16 TB por arquivo e 1 exabyte por volume |
| [[wiki/concepts/zfs]] | Sun Microsystems, 2006 — checksums constantes e auto-reparo; prioriza integridade sobre simplicidade, usado em data centers |
| [[wiki/concepts/syscall]] | Única ponte autorizada user mode → kernel — open/read/write/fork; custo de ~100–300ns por context switch |
| [[wiki/concepts/kernel]] | Núcleo do SO com acesso total ao hardware — kernel mode vs user mode; kernel panic é fatal porque não há fundação embaixo |
| [[wiki/concepts/windows]] | Maior base instalada do mundo — ampla compatibilidade de hardware, maior alvo de malware, BSOD como kernel panic |
| [[wiki/concepts/macos]] | Exclusivo de hardware Apple — controle vertical rende estabilidade, forte em edição criativa, fraco para jogos |
| [[wiki/concepts/linux]] | Família de distros, não um SO único — leve, gratuito, domina servidores; barreira de entrada é a linha de comando |
| [[wiki/concepts/chrome-os]] | Leve e dependente de nuvem — Chromebooks de boot rápido, forte offline limitado e sem softwares desktop pesados |
| [[wiki/concepts/android]] | Mobile open source mais popular do mundo — alta personalização, mas fragmentação de updates e bloatware |
| [[wiki/concepts/ios]] | Mobile exclusivo Apple — estável e curado, mas altamente restritivo a customização e sideload |
| [[wiki/concepts/unix]] | Ancestral multiusuário/multitarefa dos anos 60 — domínio de bancos e centros de pesquisa, licenciamento caro |
| [[wiki/concepts/bsd]] | Família derivada do Unix de Berkeley — infra/embarcados, citado em PS4/PS5 e na CDN da Netflix |

### Fundamentos de CS

| Página | Hook |
|---|---|
| [[wiki/concepts/logica-booleana]] | AND, OR, NOT — as três operações que constroem qualquer circuito a partir de 0s e 1s |
| [[wiki/concepts/big-o]] | Notação que descreve como o tempo cresce com os dados — O(log n) com 1B elementos = 30 comparações |
| [[wiki/concepts/melhor-caso-pior-caso-caso-medio]] | A mesma busca pode ser O(1), O(n) ou "o que costuma acontecer" — "complexidade" sem qualificação numa entrevista é o pior caso |
| [[wiki/concepts/time-space-tradeoff]] | Gastar mais memória (índice) para economizar passos — Big O mais baixo nem sempre é a melhor escolha |
| [[wiki/concepts/recursao]] | Função que chama ela mesma — caso base (para) + caso recursivo (divide) |
| [[wiki/concepts/lista-encadeada]] | Nós encadeados por ponteiros — inserção O(1) no meio, acesso O(n) por posição |
| [[wiki/concepts/concorrencia]] | Gerenciar múltiplas tarefas — race condition é o risco central quando threads compartilham estado |
| [[wiki/concepts/paralelismo]] | Executar múltiplas tarefas ao mesmo tempo — requer múltiplos cores; oposto de concorrência |
| [[wiki/concepts/compilador]] | Traduz código-fonte em código de máquina via lexer → parser → AST → otimizador |
| [[wiki/concepts/protocolo-de-rede]] | Regras de comunicação em camadas — HTTP diz o quê, TCP garante entrega, IP define rota |
| [[wiki/concepts/porta-de-rede]] | Número virtual (0–65.535) que identifica serviço/processo num host — IANA organiza em well-known, registered e dynamic; SO atribui porta dinâmica por conexão de saída para demultiplexar respostas |
| [[wiki/concepts/criptografia]] | Hashing irreversível, simétrica (mesma chave) e assimétrica (par público/privado) — base do HTTPS |
| [[wiki/concepts/bluetooth-le]] | Advertising → scan → pair → GATT — o "handshake" do Bluetooth Low Energy; gerenciar mal o ciclo gera conexão fantasma e dreno de bateria |
| [[wiki/concepts/sistema-de-tipos]] | Estática vs. dinâmica vs. inferência — quando os erros de tipo são pegos: compilação ou runtime |
| [[wiki/concepts/gerenciamento-de-memoria]] | Manual, garbage collector ou ownership (Rust) — a decisão de runtime mais difícil de reverter numa linguagem |
| [[wiki/concepts/rust-ownership-borrowing-lifetimes]] | Um dono por valor, `&`/`&mut` com regra N leitores OU 1 escritor, e lifetime garantindo que referência não outlive o valor — tudo verificado em compile-time pelo borrow checker |
| [[wiki/concepts/rust-fundamentos]] | `Option`/`Result` sem `null` implícito, `match` exaustivo, traits com static dispatch, Cargo como toolchain unificada, e onde a adoção real de Rust compensa o custo de aprendizado |
| [[wiki/concepts/gramatica-formal-ebnf]] | EBNF define o que é sintaticamente válido; precedência e associatividade resolvem ambiguidade (`1 + 2 * 3`) |
| [[wiki/concepts/language-server-protocol]] | Protocolo da Microsoft que desacopla editor de linguagem — um servidor, N editores com autocomplete e erros inline |
| [[wiki/concepts/standard-library-e-ecossistema]] | Stdlib, package manager e tooling — o que faz uma linguagem tecnicamente boa sobreviver de fato |

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
| [[wiki/concepts/algoritmos-de-ordenacao]] | Bubble Sort O(n²), Insertion Sort O(n²)/O(n) melhor caso, Merge Sort O(n log n) estável — não há um melhor universal |
| [[wiki/concepts/algoritmos-de-busca]] | Linear Search O(n) vs Binary Search O(log n) — a busca binária exige dados já ordenados |
| [[wiki/concepts/algoritmos-de-grafo]] | DFS, BFS, Dijkstra e A* — do backtrack ingênuo ao roteamento com heurística do Google Maps |
| [[wiki/concepts/repertorio]] | Acúmulo de experiência prática que gera reconhecimento de padrões e intuição — o terceiro pilar da competência |
| [[wiki/concepts/string]] | Slice de bytes + charset + encoding — imutável porque alterar bytes quebra UTF-8 silenciosamente |
| [[wiki/concepts/charset]] | Mapeamento valor numérico → caractere; distinto de encoding (que é o algoritmo de serialização) |
| [[wiki/concepts/ascii]] | 128 caracteres em 7 bits; charset e encoding ao mesmo tempo; subconjunto de UTF-8 |
| [[wiki/concepts/unicode]] | Charset universal com >1M codepoints; não é encoding — precisa de UTF-8 para ser serializado |
| [[wiki/concepts/utf-8]] | Encoding de largura variável para Unicode; criado por Ken Thompson e Rob Pike; padrão da web |

### Resolução de Problemas & Debugging Estruturado

| Página | Hook |
|---|---|
| [[wiki/concepts/pensamento-estruturado]] | Resolver qualquer problema não é dom, é prática — saber como o próprio raciocínio funciona diante do desconhecido |
| [[wiki/concepts/arvore-de-decomposicao]] | Quebrar um problema vago ("sistema lento") em perguntas cada vez mais específicas até virar solução acionável |
| [[wiki/concepts/pensamento-regressivo]] | Partir do estado final desejado e mapear de trás pra frente, em vez de arriscar suposições para frente |
| [[wiki/concepts/causa-raiz]] | O ponto de origem real do problema — atuar no sintoma sem achá-la resolve só temporariamente |
| [[wiki/concepts/hipotese-e-validacao]] | "Pode ser" não é resposta — validar com dados antes de agir, ou arrisca dias resolvendo a coisa errada |
| [[wiki/concepts/pensamento-sistemico]] | Enxergar como as partes de um sistema se conectam, não só resolver o problema pontual |
| [[wiki/concepts/debugging]] | Aplicação direta do pensamento estruturado a um bug técnico concreto |

### Aprendizado e Mentalidade

| Página | Hook |
|---|---|
| [[wiki/concepts/entender-vs-aprender]] | Entender é cognitivo, aprender é habilidade — a ilusão de fluência surge quando se confunde os dois |
| [[wiki/concepts/autoconsciencia-de-aprendizado]] | Descobrir como você especificamente aprende — o núcleo do "aprender a aprender" |
| [[wiki/concepts/autodidata]] | Quem investiga o porquê quando o procedimento falha, em vez de travar |
| [[wiki/concepts/hacker-mindset]] | Curiosidade ativa — não só faz a pergunta, mas procura a resposta |
| [[wiki/concepts/aprendizado-por-exposicao]] | Copiar código sem objetivo por centenas de horas para formar fluência |
| [[wiki/concepts/memoria-muscular]] | Familiaridade instintiva com código formada pela repetição, pré-analítica |
| [[wiki/concepts/fluencia-vs-perfeicao]] | Fluência é operar mesmo errando — perfeição no início bloqueia o aprendizado |
| [[wiki/concepts/foco-profundo]] | Estado de concentração ininterrupta incompatível com redes sociais |
| [[wiki/concepts/fundacao-tecnica]] | Multiplicador de aprendizado — torna qualquer nova tecnologia simples |
| [[wiki/concepts/raciocinio-matematico-aplicado]] | Pensamento matemático (não decorado) como fundação que não envelhece — testado com exemplo de juros compostos |
| [[wiki/concepts/aprendizado-passivo]] | Copiar código sem entender — ilusão de progresso que impede construção de raciocínio |
| [[wiki/concepts/dependencia-ia]] | Ciclo preguiçoso de prompts disfarçado de produtividade — antônimo de autonomia |
| [[wiki/concepts/autonomia-tecnica]] | Entender, explicar, modificar e sustentar código independentemente — o diferencial real |
| [[wiki/concepts/esforco-produtivo]] | O intervalo entre o problema e a ajuda; onde o aprendizado de verdade acontece |
| [[wiki/concepts/aprender-a-aprender]] | Metacognição aplicada — o superpoder do profissional do futuro; mais duradouro que qualquer ferramenta |
| [[wiki/concepts/crenca-de-alta-eficacia]] | Crença na própria capacidade de aprender — preditor de adaptação; quem não tem pode de fato ser substituído |
| [[wiki/concepts/zona-de-desconforto-da-aprendizagem]] | ZDA: aprender é biologicamente desconfortável; abraçar o caos é o mecanismo do crescimento |
| [[wiki/concepts/nexialista]] | Profissional que conecta múltiplas áreas criando soluções que especialistas isolados não conseguem |
| [[wiki/concepts/observador-tercerático]] | Conceito de Luiz Tibiriçá: co-criar novos conceitos operando cérebro orgânico e IA em paralelo |
| [[wiki/concepts/vale-do-desespero]] | O ponto em que o aprendiz entende cada peça mas não consegue arquitetar — etapa estrutural, não sinal de incapacidade |
| [[wiki/concepts/pratica-deliberada]] | 800–1.000 horas para júnior; prática no limite da competência atual, com feedback — não repetição mecânica |
| [[wiki/concepts/reconhecimento-de-padroes]] | O que separa mestre de amador (xadrez e programação): repertório de padrões, não inteligência ou sintaxe |
| [[wiki/concepts/principio-da-inversao]] | Inverter o problema para revelar a solução — Jacobi/Munger; lista o pior caso para encontrar o melhor |
| [[wiki/concepts/tutorial-hell]] | Espiral de consumo passivo de conteúdo — quanto mais você estuda, mais descobre que precisa estudar; saída: construir algo |
| [[wiki/concepts/aprendizado-deliberado]] | Prática com intenção, feedback e dificuldade progressiva — antídoto ao tutorial hell |
| [[wiki/concepts/bomba-de-efeito-moral]] | Choque de complexidade que paralisa pelo susto, não pela dificuldade real — some numa segunda leitura sem o susto |
| [[wiki/concepts/relacao-criador-criatura]] | Colocar programador admirado num pedestal e se tratar como inferior — bloqueia o próprio potencial |
| [[wiki/concepts/maximizar-pontos-fortes]] | Objetivo de programar não é ser bom em programar, é aumentar área de impacto — aproxime a técnica do seu forte real |
| [[wiki/concepts/projeto-com-adrenalina]] | Escolher o projeto real (pelo interesse genuíno) antes da tecnologia — a stack vem depois, em função do projeto |

### Filosofia do Criador (Objetivismo)

| Página | Hook |
|---|---|
| [[wiki/concepts/objetivismo]] | Sistema filosófico de Ayn Rand — razão, egoísmo racional e capitalismo laissez-faire |
| [[wiki/concepts/criador-vs-parasita]] | Criador enfrenta a natureza sozinho e precisa de independência; parasita enfrenta através de outras pessoas e precisa de dependência |
| [[wiki/concepts/altruismo-coercitivo]] | Crítica ao altruísmo como doutrina moral obrigatória — dependência tratada como virtude |
| [[wiki/concepts/independencia-como-motor-criativo]] | Independência total em função e motivo como necessidade básica de quem cria |

### Escalabilidade & System Design

| Página | Hook |
|---|---|
| [[wiki/concepts/escalabilidade-vertical]] | Scale up — simples mas com teto físico e single point of failure |
| [[wiki/concepts/escalabilidade-horizontal]] | Scale out — sem teto teórico, requer stateless e load balancer |
| [[wiki/concepts/stateless]] | Servidor sem estado — pré-requisito da escalabilidade horizontal |
| [[wiki/concepts/sticky-session]] | Afinidade de sessão — solução paliativa que adia o problema real |
| [[wiki/concepts/cdn]] | Rede de edge servers geográficos — cache global da camada web |
| [[wiki/concepts/auto-scaling]] | Adição/remoção automática de instâncias por regras de métricas |
| [[wiki/concepts/sharding]] | Divisão de banco em múltiplos shards — escala writes e armazenamento |
| [[wiki/concepts/replicacao-de-banco]] | Cópias do banco para leitura — escala reads e aumenta disponibilidade |
| [[wiki/concepts/gargalo]] | Ponto mais lento da cadeia — identificar antes de escalar qualquer coisa |
| [[wiki/concepts/cap-theorem]] | Consistência vs Disponibilidade vs Partição — o trade-off central de sistemas distribuídos |

### Fundamentos de Backend (Request/Response ao Deploy)

| Página | Hook |
|---|---|
| [[wiki/concepts/requisicao-resposta]] | O idioma básico do backend — método, rota, headers, body de um lado; status code do outro |
| [[wiki/concepts/contrato-de-api]] | API como contrato entre cliente e servidor — permite mudar o backend por dentro sem quebrar quem consome |
| [[wiki/concepts/validacao-de-entrada]] | Nunca confiar no client — separação em camadas (controller/service/banco) evita regra de negócio espalhada |
| [[wiki/concepts/autenticacao-e-autorizacao]] | Duas perguntas diferentes: quem é você (autenticação) vs. o que você pode fazer (autorização) |
| [[wiki/concepts/modelagem-de-dados]] | Como o mundo real vira estrutura no banco — tradeoff entre modelar pouco (confuso) e normalizar demais (joins) |
| [[wiki/concepts/filas-e-workers]] | Desacoplar pedido de processamento pesado — riscos: job falha, processa 2x, fila cresce mais que o consumo |
| [[wiki/concepts/load-balancer]] | Distribui tráfego entre instâncias — L4 (cego, rápido) vs L7 (inspeciona HTTP, roteia por path/header) |
| [[wiki/concepts/reverse-proxy]] | Fica na frente da aplicação e repassa a requisição — só vira load balancer quando escolhe entre múltiplos destinos equivalentes |
| [[wiki/concepts/alta-disponibilidade]] | Sistema continua operacional mesmo com falhas de componente — redundância, health check, deploy gradual |
| [[wiki/concepts/observabilidade]] | Entender o que acontece por dentro via logs (o quê), métricas (crescendo?) e traces (onde o tempo foi gasto) |

### Idempotência & Deduplicação de Requests

| Página | Hook |
|---|---|
| [[wiki/concepts/idempotencia]] | Mesmo resultado não importa quantas vezes a operação executa — pré-requisito para retry seguro; chave gerada pelo servidor (hash dos campos) é mais robusta contra abuso que chave enviada pelo cliente |
| [[wiki/concepts/post-redirect-get]] | Redirect 303 após POST evita reenvio acidental de formulário — não protege contra reenvio via script, só via navegador |

### Estratégias de Deploy

| Página | Hook |
|---|---|
| [[wiki/concepts/deploy-vs-release]] | Deploy é colocar o código na máquina; release é ligar o comportamento para o usuário — dois eventos separáveis via feature flag ou tráfego direcionado |
| [[wiki/concepts/deploy-strategies]] | Comparativo de todas as estratégias — Recreate, Rolling, Blue/Green, Canary, A/B, Shadow — rollback, custo e quando usar cada uma |
| [[wiki/concepts/recreate-deployment]] | Desliga a instância antiga e sobe a nova — mais simples, mas downtime inevitável na janela entre shutdown e start |
| [[wiki/concepts/rolling-update]] | Substituição gradual pod a pod — nativo no Kubernetes, tráfego misto exige compatibilidade de API e banco |
| [[wiki/concepts/blue-green-deploy]] | Dois ambientes em paralelo, troca atômica no load balancer — rollback instantâneo, custo 2x durante a transição |
| [[wiki/concepts/canary-release]] | Percentual pequeno de tráfego vai para a versão nova para reduzir risco técnico — requer observabilidade madura |
| [[wiki/concepts/ab-testing-deployment]] | Split de tráfego como o Canary, mas para validar hipótese de negócio (conversão, receita) em vez de risco técnico |
| [[wiki/concepts/shadow-deployment]] | Tráfego real duplicado para a v2 sem que nenhum usuário veja a resposta — valida com dados de produção, risco zero |
| [[wiki/concepts/zero-downtime-deploy]] | Estratégia de tráfego + migrations backward compatible via Expand-Contract — nunca migrar schema e código no mesmo deploy |
| [[wiki/concepts/feature-flags]] | Ativa/desativa funcionalidades em produção sem novo deploy — o mecanismo mais comum para separar deploy de release |
| [[wiki/concepts/systemd]] | Init system do Linux (PID 1) — mantém o processo da aplicação vivo entre trocas de tráfego, independente do roteamento |

### Realtime & Comunicação

| Página | Hook |
|---|---|
| [[wiki/concepts/server-sent-events]] | Conexão HTTP mantida aberta, servidor→cliente; formato `data`/`event`, Redis Pub/Sub para escalar, erro comum de polling disfarçado |
| [[wiki/concepts/websocket-vs-polling]] | Polling, long polling, SSE e WebSocket comparados — trade-offs de latência, overhead e bidirecionalidade |

### Cache & Redis

| Página | Hook |
|---|---|
| [[wiki/concepts/redis]] | Banco NoSQL in-memory chave-valor — sub-milissegundo, single CPU, escala horizontal via cluster |
| [[wiki/concepts/cache]] | Guardar dados em memória para resposta rápida — hierarquia L1→L4, padrões e quando não usar |
| [[wiki/concepts/cache-aside]] | Lazy Loading: tenta cache, em miss vai ao banco com TTL — análogo ao padrão Flyweight |
| [[wiki/concepts/feature-flag]] | Interruptores de funcionalidade em runtime — Redis é ideal pela latência mínima no fluxo de execução |
| [[wiki/concepts/banco-in-memory]] | Armazenamento primário em RAM — Redis, persistência RDB/AOF opcional |
| [[wiki/concepts/escalabilidade-horizontal]] | Mais máquinas ao invés de mais recursos na mesma — NoSQL e Redis cluster como caso principal |
| [[wiki/concepts/tradeoff-de-cache]] | Cache sempre adiciona complexidade — invalidação, sincronismo e consistência eventual como custos |

### Bancos de Dados & SQL

| Página | Hook |
|---|---|
| [[wiki/concepts/orm]] | ORM não elimina SQL, gera SQL por baixo dos panos — abstração, não substituição |
| [[wiki/concepts/domain-specific-language]] | DSL para banco de dados quase sempre é wrapper em cima de SQL; Datalog do Datomic é a exceção real |
| [[wiki/concepts/mysql]] | InnoDB, gap locking, estoque como linhas físicas vs coluna numérica, diagnóstico por tempo de conexão segurada |
| [[wiki/concepts/skip-locked]] | `SELECT FOR UPDATE SKIP LOCKED` — fila de jobs e reserva de estoque de alta concorrência sem broker externo |
| [[wiki/concepts/grande-rollback]] | Tendência de empresas em escala abandonando Redis/brokers por primitivas do banco relacional — Shopify e 37signals |
| [[wiki/concepts/solid-queue]] | Fila de background jobs da 37signals 100% sobre banco relacional, sem Redis nem Kafka |
| [[wiki/concepts/acid]] | Atomicidade, Consistência, Isolamento, Durabilidade — garantias fortes dos bancos relacionais |
| [[wiki/concepts/base-basically-available-soft-state-eventual]] | O contraponto de ACID — disponibilidade e escala em troca de consistência eventual |
| [[wiki/concepts/relational-vs-nosql]] | Não existe escolha universal; trade-offs de consistência, queries, escala e schema por tipo de banco |
| [[wiki/concepts/database-transactions]] | Mecanismo que garante atomicidade — `$transaction` como invocação do contrato ACID |
| [[wiki/concepts/database-index]] | Estrutura (B-tree/hash) que acelera queries e garante unicidade ao custo de overhead em escritas |
| [[wiki/concepts/consistency-models]] | Espectro de Linearizability a Eventual Consistency — o que um cliente pode observar após uma escrita |
| [[wiki/concepts/stored-procedure]] | Lógica armazenada e executada no banco — mover regra de negócio pra lá compensa em agregação de grande volume, mas com moderação |
| [[wiki/concepts/materialized-view]] | View com resultado persistido em disco — meio-termo entre SQL cru repetido e stored procedure |

### Arquitetura Backend & Event-Driven

| Página | Hook |
|---|---|
| [[wiki/concepts/event-sourcing]] | Persistir eventos imutáveis em vez de estado — replay para calcular estado atual; auditoria nativa |
| [[wiki/concepts/cqrs]] | Separar modelos de escrita e leitura — write emite eventos, read mantém projeções otimizadas |
| [[wiki/concepts/ddd]] | Domínio no centro, adapters na borda — aggregates, domain events, bounded context |
| [[wiki/concepts/application-boundary]] | Aplicações são construções sociais — devs, negócio e orçamento enxergam "uma unidade única" de formas diferentes; fronteira real é política, não técnica |
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
| [[wiki/concepts/boy-scout-rule]] | Deixe o código um pouco mais limpo a cada mudança — estratégia de pagamento contínuo de dívida técnica inadvertida |
| [[wiki/concepts/codigo-para-o-mantenedor]] | Escreva pensando em quem vai manter, inclusive você mesmo no futuro — vale também para código gerado por IA |
| [[wiki/concepts/fazer-a-coisa-mais-simples-que-poderia-funcionar]] | Princípio de XP: resolva com a solução mais simples válida agora, refatore depois se necessário |
| [[wiki/concepts/quadrante-de-fowler]] | Dois eixos: Deliberado/Inadvertido × Prudente/Imprudente; só Prudente+Deliberado é aceitável |
| [[wiki/concepts/complexidade-como-estrategia]] | Três estágios: inconsciente → aparência → sabotagem — criar código incompreensível para se tornar insubstituível |
| [[wiki/concepts/ciclo-da-desgraca-software]] | Espiral reescrita→mesmo problema→dois sistemas; alternativa: refatoração incremental com strangler fig |
| [[wiki/concepts/pitfalls-de-linguagem]] | Armadilhas que existem na linguagem mas não devem ser usadas — descobertas pelo uso, não pelo estudo teórico |
| [[wiki/concepts/dizer-sim-para-tudo]] | Dizer sim para tudo fragmenta foco e inibe surgimento de líderes — promessa é dívida, tempo estoura |
| [[wiki/concepts/definicao-de-pronto]] | Código que só funciona não está pronto — legível + testado + documentado + revisado por regra de negócio |
| [[wiki/concepts/testar-proprio-codigo]] | Testar só o caminho feliz é concordar com a própria opinião — testes automatizados cobrem erro e happy path |
| [[wiki/concepts/atomic-commits]] | Commit atômico = alteração + teste que a valida juntos — unidade funcional, não diário de mudanças |
| [[wiki/concepts/checklist-primeiro-dia-projeto]] | Seis etapas do dia 1 de uma codebase nova — deploy, ORM/migrations e testes resolvidos antes de qualquer feature, quando o custo de errar ainda é baixo |
| [[wiki/concepts/escolha-de-stack]] | Aprender vs. monetizar como eixo central da escolha de stack; framework batteries-included acelera SaaS solo |
| [[wiki/concepts/triade-retorno-risco-liquidez]] | Retorno, risco e liquidez nunca são bons ao mesmo tempo — modelo de investimentos generalizado para qualquer decisão da vida |
| [[wiki/concepts/avaliar-hype-tecnologico]] | Adotar tecnologia hype é risco alto + liquidez baixa; só compensa se o retorno for proporcionalmente alto — caso Node.js no Pagar.me vs. C# na Stone |
| [[wiki/concepts/modulo-profundo]] | Deep module (Ousterhout): poucos módulos grandes com interface simples escondendo complexidade — o oposto de muitos módulos rasos que a IA produz por padrão |
| [[wiki/concepts/modelo-cascata-vs-desenvolvimento-incremental]] | Waterfall falha para software porque é impossível visualizar o design inteiro antes de construir — design incremental corrige o design cedo, enquanto o sistema ainda é pequeno |
| [[wiki/concepts/red-flags-de-design]] | Sinal de que um trecho de código é mais complicado do que precisa — melhor exercitado no código de outra pessoa via code review, não no próprio |
| [[wiki/concepts/lentes-de-codigo]] | Acoplamento, abstração e estado não são termos para decorar — são lentes que revelam se o código é bom ou só funciona; central para avaliar código gerado por IA |
| [[wiki/concepts/acoplamento]] | Grau de dependência entre partes — quanto uma mudança em A força mudança em B; god function vs. funções separadas por responsabilidade |
| [[wiki/concepts/abstracao]] | Esconder o que não precisa ser visto atrás de um contrato — troca de implementação (banco → API) sem tocar no código consumidor |
| [[wiki/concepts/coesao]] | Quanto as responsabilidades dentro de uma unidade estão relacionadas entre si — alta coesão interna + baixo acoplamento externo é o alvo |
| [[wiki/concepts/single-responsibility]] | Uma unidade deve ter uma única razão para mudar — o critério é o ator que causa a mudança, não o número de linhas |
| [[wiki/concepts/efeito-colateral]] | O que uma função muda além do que retorna — o objetivo não é eliminar efeitos, é isolá-los e torná-los explícitos |
| [[wiki/concepts/estado-compartilhado]] | Múltiplas funções lendo/mutando o mesmo estado tornam debugging impossível em escala — solução: funções que recebem estado e retornam novo estado |

### Segurança de APIs & Arquitetura

| Página | Hook |
|---|---|
| [[wiki/concepts/ssh]] | Chave privada nunca sai da origem, pública vai pro `authorized_keys` do destino — acesso é unidirecional por par de chaves, `~/.ssh/config` cria aliases |
| [[wiki/concepts/hardening-de-servidor]] | Reduzir superfície de um host desativando o que não é necessário — presets escalonados (paranoico/equilibrado/básico) para SSH e afins |
| [[wiki/concepts/gatekeeper-pattern]] | Ponto único de entrada obrigatório — centraliza autenticação, rate limiting e logging, reduz superfície de ataque |
| [[wiki/concepts/valet-key-pattern]] | Credencial temporária de escopo mínimo — cliente acessa recurso diretamente sem a API virar proxy |
| [[wiki/concepts/token-relay-pattern]] | Identidade do usuário viaja por todos os saltos internos — autorização fina em cada serviço |
| [[wiki/concepts/attack-surface]] | Conjunto de pontos de entrada exploráveis — quanto menor, mais fácil de defender |
| [[wiki/concepts/defense-in-depth]] | Múltiplas camadas independentes — se uma falha, as outras contêm o dano |
| [[wiki/concepts/waf]] | Filtro de borda HTTP — bloqueia OWASP Top 10 e DDoS antes de chegar na aplicação |
| [[wiki/concepts/principio-do-menor-privilegio]] | Permissão exata e nada mais — limita o raio de explosão quando um componente é comprometido |
| [[wiki/concepts/secure-by-default]] | Estado padrão é o mais seguro — fail-secure, confirmação explícita para ações destrutivas |
| [[wiki/concepts/sql-injection]] | Input não sanitizado executado como SQL — Bobby Tables; prevenção: queries parametrizadas |
| [[wiki/concepts/xss]] | Injeção de JavaScript no browser da vítima — mesma classe do SQLi, contexto HTML/JS |
| [[wiki/concepts/timing-attack]] | Tempo de resposta como canal de informação — variação de latência revela segredos |
| [[wiki/concepts/sast]] | Análise estática de segurança no código — detecta padrões vulneráveis antes do deploy |
| [[wiki/concepts/secrets-management]] | Credenciais nunca no código — .env local, GitHub Secrets/AWS SM em produção |
| [[wiki/concepts/password-hashing]] | Armazenar senhas exige algoritmo lento + salt + pepper — plaintext e MD5/SHA são inseguros |
| [[wiki/concepts/salt]] | String aleatória por usuário concatenada à senha — invalida rainbow tables pré-computadas |
| [[wiki/concepts/pepper]] | Segredo do servidor concatenado à senha — defesa se só o banco vazar |
| [[wiki/concepts/bcrypt]] | CPU-hard clássico (fator de trabalho configurável) — superado por rigs de GPU sem memory-hard |
| [[wiki/concepts/argon2]] | Estado da arte: CPU-hard + memory-hard — gargalo de VRAM derrota paralelismo de GPU |
| [[wiki/concepts/cpu-hard]] | Algoritmo intencionalmente lento — cada tentativa de brute-force custa ciclos de CPU |
| [[wiki/concepts/memory-hard]] | Ocupa RAM por instância — limita paralelismo de GPU pelo gargalo de VRAM |
| [[wiki/concepts/rainbow-table]] | Tabela hash→senha pré-computada — reutilizável contra qualquer banco sem salt |
| [[wiki/concepts/ataque-pre-computacao]] | Trabalho feito uma vez, reutilizado em múltiplos vazamentos — salt invalida o reaproveitamento |
| [[wiki/concepts/iso-27001]] | Framework de gestão (SGSI) organizado em torno da tríade CIA — 93 controles do Anexo A em 4 temas, SoA justifica o que se aplica |
| [[wiki/concepts/sgsi-isms]] | O objeto central que a ISO 27001 exige: políticas + processos + tecnologia geridos como sistema, não ferramenta isolada |
| [[wiki/concepts/triade-cia]] | Confidencialidade, integridade, disponibilidade — o critério que justifica todo controle de segurança da informação |
| [[wiki/concepts/segregacao-de-funcoes]] | Quem desenvolve não deve poder fazer deploy sozinho — controle A.5.3, tenso em times pequenos |
| [[wiki/concepts/iso-42001]] | Governança de IA responsável — cobre a lacuna que a ISO 27001 deixa em aberto com LLMs |
| [[wiki/concepts/idor]] | IDOR/BOLA — acessar objeto por ID sem checar ownership; #1 do OWASP API Top 10 |
| [[wiki/concepts/mass-assignment]] | BOPLA — aceitar o body inteiro sem whitelist permite alterar campos como `role` |
| [[wiki/concepts/webhook-signature-validation]] | HMAC + `timingSafeEqual` + replay/idempotência — validar que o webhook veio da fonte certa |
| [[wiki/concepts/hmac]] | Chave interna e externa derivadas do mesmo segredo via padding (ipad `0x36`/opad `0x5C`) — integridade sem o custo de assinatura assimétrica, resistente a ataque de extensão de mensagem |
| [[wiki/concepts/local-first]] | Dado calculado no servidor vive só no cliente — HMAC garante integridade na volta sem pagar custo de storage/lookup |
| [[wiki/concepts/exposicao-excessiva-de-dados]] | Retornar a entidade inteira em vez de projetar campos vaza dados sensíveis mesmo sem exibi-los na UI |
| [[wiki/concepts/toctou]] | Intervalo entre check e use permite saque/estoque duplicado sob concorrência — corrigido com transactions atômicas |
| [[wiki/concepts/confiar-no-frontend]] | Anti-padrão raiz: regra de negócio só no cliente é sempre contornável — servidor deve revalidar tudo |
| [[wiki/concepts/agent-containment]] | Isolar o processo de um agente de IA (sandbox) para limitar dano se ele executar código malicioso vindo de uma dependência comprometida |
| [[wiki/concepts/supply-chain-security]] | SBOM, SLSA, Sigstore/Cosign contra dependências comprometidas; ataques via `postinstall` malicioso (ex.: npm) como vetor mais direto |
| [[wiki/concepts/sistema-operacional-imutavel]] | Root somente-leitura (NixOS/Fedora Silverblue) — dano ao sistema não sobrevive a um reboot |

### Frontend & Design Engineering

| Página | Hook |
|---|---|
| [[wiki/concepts/design-first]] | Layout no Figma antes do código — padrão em times grandes com designers dedicados; Figma fica desatualizado em times pequenos |
| [[wiki/concepts/code-first]] | Codar com component libraries sem layout prévio — velocidade alta, risco de Frankenstein visual |
| [[wiki/concepts/design-engineer]] | Cargo do meio: conhecimentos de design aplicados diretamente no código — experimentações no código, Figma como referência |
| [[wiki/concepts/component-library]] | Shadcn, Radix, Headless UI — componentes pré-prontos; headless dá controle total, estilizadas são mais rápidas |
| [[wiki/concepts/fake-delay]] | Delay mínimo intencional (300ms) para garantir feedback visual perceptível — performance percebida é design |
| [[wiki/concepts/design-como-interacao]] | Design se manifesta na interação, não na primeira impressão — micro-interações, onboarding, feedback, linguagem |
| [[wiki/concepts/react-compiler]] | Compilador do React 19 que memoiza valores e funções automaticamente em build time, reduzindo a necessidade de useMemo/useCallback manuais |
| [[wiki/concepts/useMemo]] | Hook que memoiza o resultado de um cálculo — só recalcula quando as dependências mudam; overhead supera ganho em cálculos triviais |
| [[wiki/concepts/useCallback]] | Hook que memoiza a referência de uma função entre renders — essencial para não quebrar `React.memo` em componentes filhos |
| [[wiki/concepts/concurrent-mode]] | Modelo de renderização do React 18+ que pausa/retoma/prioriza renders sem bloquear a UI — useTransition e useDeferredValue |

### React & Hooks

| Página | Hook |
|---|---|
| [[wiki/concepts/derived-state]] | Se dá para calcular a partir de estado/props existentes, não é estado — calcula na renderização em vez de sincronizar via `useEffect` |
| [[wiki/concepts/stale-closure]] | `useEffect` com array de dependências vazio congela variáveis da primeira renderização — closure captura variáveis, não valores |

### Testes & Qualidade

| Página | Hook |
|---|---|
| [[wiki/concepts/tdd]] | Red-Green-Refactor — o teste vem antes para sentir o acoplamento antes de criá-lo, não para cobertura |
| [[wiki/concepts/test-doubles]] | Dummy/Stub/Fake/Spy/Mock (Meszaros) — Fake robusto testa o contrato, Mock frágil testa o nome do método |
| [[wiki/concepts/seedwork]] | Framework mínimo que cada time reconstrói por conta própria em vez de compartilhar um só — origem do framework de testes de Kent Beck antes do JUnit |
| [[wiki/concepts/contract-testing]] | Consumer-Driven Contracts + Pact — valida que dois serviços concordam com o formato da comunicação sem rodar juntos |
| [[wiki/concepts/piramide-de-testes]] | Unitário → Integração → E2E; quanto mais alto, mais lento, caro e frágil |
| [[wiki/concepts/testes-integracao-banco-real]] | Nunca mockar o banco em testes de integração — o valor do teste está em validar a query real |
| [[wiki/concepts/teste-de-integracao-estreito-vs-amplo]] | Fowler separa "integration test" em estreito (double + contract test, rápido) e amplo (serviços reais, lento) |
| [[wiki/concepts/unit-test-solitario-vs-sociavel]] | Solitário mocka tudo (London), sociável usa colaboradores reais (Detroit) — confusão irmã do narrow/broad |
| [[wiki/concepts/criterios-de-bom-teste]] | Determinístico, conciso, relevante, compreensível, durável — e 100% de cobertura não garante ausência de bug |

### Padrões e Design

| Página | Hook |
|---|---|
| [[wiki/concepts/pattern-recognition]] | Capacidade humana de detectar repetições — base do aprendizado por exposição |
| [[wiki/concepts/design-patterns]] | Catálogo de soluções nomeadas — útil só depois de já ter visto os padrões na prática |
| [[wiki/concepts/mapper-pattern]] | Classe estática por camada que converte entidade de domínio para o formato de outra camada (Prisma, HTTP) — isola o acoplamento à tecnologia, não ao domínio |
| [[wiki/concepts/anti-pattern]] | Repetição que parece solução mas cria problemas — frequência não implica qualidade |
| [[wiki/concepts/over-engineering]] | "Verde neném" — aplicar patterns sem base; pular etapas da progressão produz complexidade sem valor; under-engineering é o problema mais comum |
| [[wiki/concepts/under-engineering]] | Fazer menos do que o projeto exige — acoplamento, hardcode, sem CI, copy-paste sem estrutura; mais comum que over-engineering, e o antídoto não exige nenhuma técnica sofisticada |
| [[wiki/concepts/otimizacao-prematura]] | Raiz de todo mal (Knuth) — otimizar antes de ter projeto bom torna o código rígido e difícil |
| [[wiki/concepts/modelagem-orientada-a-objetos]] | Pré-requisito obrigatório para design patterns — classes, atributos, relacionamentos antes de GoF |
| [[wiki/concepts/walking-skeleton]] | Fatia mínima da arquitetura fim-a-fim em produção cedo; caso LMAX — peça provisória isolada atrás de abstração trocável |
| [[wiki/concepts/dora-metrics]] | Deployment Frequency, Lead Time, Change Failure Rate, MTTR — velocidade e qualidade se correlacionam positivamente, refutando o "triângulo de ferro" |
| [[wiki/concepts/portfolio-backend-junior]] | Checklist do diferencial numa primeira vaga de backend — profissionalismo nos fundamentos, não arquitetura sofisticada |
| [[wiki/concepts/docker-portfolio]] | Docker Compose + Dockerfile multi-stage numa aplicação de portfólio demonstra as ferramentas que qualquer empresa de backend vai exigir |
| [[wiki/concepts/documentacao-api-swagger]] | Swagger/OpenAPI + Scalar como API reference — diferencial raro, ~1 em 10 devs se preocupa com documentação de portfólio |
| [[wiki/concepts/error-handling-estruturado]] | Classes de erro específicas + HTTP codes corretos por caso + error handler global para o inesperado |
| [[wiki/concepts/sql-alem-do-basico]] | JOINs, agregações e subqueries — sinal de que o dev saiu do CRUD básico e entende como o banco funciona de verdade |
| [[wiki/concepts/curriculo-vs-portfolio]] | Currículo é promessa de onde você esteve; portfólio é prova do que você produziu |
| [[wiki/concepts/otimizacao-ats-curriculo]] | Repetir a stack-alvo 2-3x no currículo para passar no filtro automático (ATS) antes de qualquer avaliação humana |
| [[wiki/concepts/refatoracao]] | Mudar estrutura interna sem alterar comportamento externo — dois chapéus de Kent Beck, passos pequenos, testes na base da pirâmide como rede de segurança, refatoração oportunista vs. planejada |
| [[wiki/concepts/dois-chapeus-kent-beck]] | Adicionar funcionalidade e refatorar são atividades mutuamente exclusivas no tempo — cada uma com sua própria disciplina de validação |

## Entities

| Página | Hook |
|---|---|
| [[wiki/entities/moonshot-ai]] | Lab chinês criador do Kimi — Kimi K3 (2,8T parâmetros, MoE 896/16 experts) publica método de inferência aberto para descentralizar conhecimento de servir modelos grandes |
| [[wiki/entities/deepseek]] | Lab chinês — DeepSeek V4 Pro, maior open source antes do Kimi K3; DeepSeek Flash V4 como referência de modelo barato para tarefas do dia a dia |
| [[wiki/entities/nvidia]] | Fabricante de GPUs — sujeita a sanções de exportação de chips para a China, pressão de fundo por trás de inovação em MoE/KV Cache |
| [[wiki/entities/bubblewrap]] | Binário de sandboxing do GNOME (usado pelo Flatpak) — base técnica do AI Jail e do sandbox nativo do Claude Code |
| [[wiki/entities/augusto-galego]] | Criador de conteúdo técnico brasileiro — demo prática de deploy blue/green com Nginx numa VPS |
| [[wiki/entities/hostgator]] | Provedora de hospedagem/VPS — patrocinadora da demo de deploy blue/green de Augusto Galego |
| [[wiki/entities/anthony-d-mays]] | Ex-entrevistador técnico big tech ("de Compton ao Google") — autor do conselho "memorize o padrão, não o problema" para entrevistas de coding |
| [[wiki/entities/wesley-willians]] | Apresentador do canal Full Cycle — conteúdo sobre arquitetura de software, system design e carreira |
| [[wiki/entities/full-cycle]] | Canal/comunidade brasileira de arquitetura de software e MBA em Arquitetura Full Cycle |
| [[wiki/entities/everton-oliveira]] | Engenheiro de software sênior e criador de conteúdo brasileiro — princípios de entrega rápida e com qualidade (KISS, YAGNI) |
| [[wiki/entities/mario-souto]] | Staff Software Engineer e criador de conteúdo brasileiro, canal DevSoutinho — under-engineering vs. over-engineering |
| [[wiki/entities/iana]] | Internet Assigned Numbers Authority — coordena globalmente endereços IP, nomes de domínio e números de porta |
| [[wiki/entities/margaret-storey]] | Professora, University of Victoria, Canada Research Chair — cunhou "cognitive debt" (2026) sobre a base teórica de Peter Naur |
| [[wiki/entities/peter-naur]] | Turing Award 2005 — Backus-Naur Form (gramática) e "Programming as Theory Building" (1985), base de "cognitive debt" |
| [[wiki/entities/bernardo-lobato]] | Desenvolvedor e criador de conteúdo brasileiro — arquitetura de software e padrões avançados |
| [[wiki/entities/linuxtips]] | Plataforma brasileira de educação em tecnologia — DevOps, Cloud, Kubernetes, podcast Papinho Tech Solo |
| [[wiki/entities/renato-augusto]] | Desenvolvedor e criador de conteúdo brasileiro — padrões de projeto GoF e orientação a objetos, carreira e soft skills |
| [[wiki/entities/dale-carnegie]] | Autor de "Como Fazer Amigos e Influenciar Pessoas" (1936) — confiança e influência genuína como base da habilidade interpessoal |
| [[wiki/entities/randy-nelson]] | Ex-Pixar, hoje Apple — educador; autor da palestra sobre as três características (profundidade, abrangência, comunicação) de um candidato excepcional |
| [[wiki/entities/eduarda-rocket-city]] | Engenheira de software internacional, criadora de conteúdo no canal Rocket City |
| [[wiki/entities/openai]] | Organização responsável pelo GPT-3/4 — formalizou in-context learning e scaling laws; criadora do tokenizer tiktoken |
| [[wiki/entities/google]] | Criadora do Gemini e do harness AntiGravity — concorrente de Anthropic e OpenAI, tokenizer próprio |
| [[wiki/entities/matt-pocock]] | Educador de TypeScript/AI (AI Hero) — fundamentos de LLM, e a tese de que fundamentos de software importam mais que nunca na era da IA |
| [[wiki/entities/fred-brooks]] | Mythical Man-Month, No Silver Bullet, e o conceito de "design concept" — teoria compartilhada e invisível do que está sendo construído |
| [[wiki/entities/john-ousterhout]] | A Philosophy of Software Design — define complexidade como estrutura difícil de mudar; cunhou "módulos profundos" |
| [[wiki/entities/kent-beck]] | Criador do TDD moderno e da XP — "invista no design do sistema todos os dias"; coautor do JUnit com Erich Gamma |
| [[wiki/entities/junit]] | Framework de testes criado por Kent Beck e Erich Gamma num voo para a OOPSLA 1997 — origem da família de frameworks Xunit |
| [[wiki/entities/c3-project]] | Chrysler Comprehensive Compensation — projeto de nascimento da Extreme Programming, onde o framework de testes de Kent Beck foi usado |
| [[wiki/entities/gang-of-four]] | Erich Gamma, Richard Helm, Ralph Johnson e John Vlissides — autores de *Design Patterns* (1994); Gamma também coautor do JUnit |
| [[wiki/entities/vercel-ai-sdk]] | SDK TypeScript da Vercel para chamar múltiplos provedores de LLM com API unificada |
| [[wiki/entities/jason-wei]] | Pesquisador Google Brain — lead author do paper de chain-of-thought prompting e do paper de emergent abilities |
| [[wiki/entities/fabio-akita]] | Programador brasileiro, autodidata desde 1991, criador do canal Akita On Rails |
| [[wiki/entities/lucas-badico]] | Programador e professor brasileiro, criador de conteúdo sobre Golang e carreira; defende a ponte fullstack como caminho de entrada ao backend |
| [[wiki/entities/codigo-fonte-tv]] | Canal brasileiro de YouTube com pesquisa salarial própria (pesquisa.codefonte.com.br); cruza dados com pesquisas oficiais de fabricantes de linguagem |
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
| [[wiki/entities/pascadev]] | Canal brasileiro de conteúdo sobre IA e Claude Code — série sobre eficiência com LLMs |
| [[wiki/entities/codex-openai]] | Harness de codificação da OpenAI baseado em GPT-5.x — par do Claude Code em 2026 |
| [[wiki/entities/rockyou]] | Empresa que vazou 32M senhas em plaintext em 2009 — originou a wordlist com bilhões de senhas reais |
| [[wiki/entities/pedro-duarte]] | Brasileiro, co-fundador Radix UI + Stitches (adquiridos WorkOS), hoje Raycast — referência em design de interação |
| [[wiki/entities/linear]] | Ferramenta de issues — referência máxima de design e performance frontend; todo dev deveria usar ao menos uma vez |
| [[wiki/entities/radix-ui]] | Biblioteca headless acessível — fundação do Shadcn/UI; co-criada por Pedro Duarte |
| [[wiki/entities/lovable]] | Principal ferramenta de vibe-coding 2025 — sucesso deve-se ao design de produto, não só à tecnologia |
| [[wiki/entities/charlie-munger]] | Sócio de Warren Buffett — popularizou o princípio da inversão como modelo mental; usou inversão para criar rotas aéreas seguras na 2ª Guerra |
| [[wiki/entities/karl-gustav-jakob-jacobi]] | Matemático alemão — originou o princípio "inverter, sempre invertar" |
| [[wiki/entities/george-hotz]] | Geohot — hacker do iPhone/PS3, carro autônomo open source; "não há substituto para sentar e construir algo" |
| [[wiki/entities/pedro-camaforte]] | Dev sênior, cria série de system design para entrevistas — foco no que separa resposta mediana de resposta de sênior |
| [[wiki/entities/uncle-bob]] | Robert C. Martin — associado a Clean Code/Clean Architecture/SOLID; citado em thread sobre SQL não ser feito para ser embutido em programas |
| [[wiki/entities/shopify]] | E-commerce que hospeda ~14% das lojas americanas — substituiu reserva de estoque Redis+MySQL por MySQL puro com SKIP LOCKED, segurando US$ 5,1M/minuto na Black Friday 2025 |
| [[wiki/entities/37signals]] | Empresa por trás do Basecamp e Rails — saiu do cloud para hardware próprio; criadora do Solid Queue, fila 100% sobre banco relacional |
| [[wiki/entities/lucas-montano]] | Criador de conteúdo brasileiro — argumenta que o pânico de "atrofia cognitiva" por IA mede o tipo errado de habilidade (sintaxe, não conhecimento perene) |
| [[wiki/entities/eric-ries]] | Autor de *A Startup Enxuta* — ex-programador que criou a metodologia Lean Startup depois de lançar um produto que ninguém queria |
| [[wiki/entities/mano-deivin]] | Canal brasileiro de YouTube sobre carreira e produto para devs |
| [[wiki/entities/nir-eyal]] | Autor de *Hooked* e *Indistraível* — escreveu o segundo livro como antídoto ao próprio primeiro |
| [[wiki/entities/ayn-rand]] | Escritora e filósofa russo-americana — criadora do Objetivismo; autora de *A Nascente* |
| [[wiki/entities/martin-fowler]] | Chief Scientist Thoughtworks, autor de *Refactoring* e *PoEAA* — mantém o bliki, referência em terminologia de testes e arquitetura |
| [[wiki/entities/gerard-meszaros]] | Autor de *xUnit Test Patterns* (2007) — criou a taxonomia de Test Doubles (Dummy/Fake/Stub/Spy/Mock) divulgada por Martin Fowler |
| [[wiki/entities/david-farley]] | Coautor de *Continuous Delivery* com Jez Humble; envolvido no LMAX; refuta o "triângulo de ferro" com dados DORA |
| [[wiki/entities/mercado-livre]] | Maior e-commerce/fintech da América Latina — combina ISO 27001 + PCI-DSS + Zero Trust; adotante consolidado de Go em produção |
| [[wiki/entities/andre-casciotti]] | Criador de conteúdo brasileiro, canal Próximo Nível — carreira dev, granularidade de mudança, automações pessoais como prática |
| [[wiki/entities/robert-nystrom]] | Autor de *Crafting Interpreters* — implementação passo a passo da linguagem Lox (interpretador Java + VM bytecode em C) |
| [[wiki/entities/llvm]] | Infraestrutura de compilador reutilizável — backend de otimização/codegen multi-arquitetura usado por Rust e Swift |
| [[wiki/entities/filipe-deschamps]] | Programador brasileiro, fundador do TabNews — quadro Request/Response; aplica a tríade retorno-risco-liquidez a decisões de carreira e adoção de hype |
| [[wiki/entities/tabnews]] | Comunidade brasileira de conteúdo técnico fundada por Filipe Deschamps — newsletter e formato Request/Response |
| [[wiki/entities/pagar-me]] | Fintech brasileira de pagamentos — adotou Node.js quando o modelo assíncrono ainda era hype, apostando em concorrência sem multi-threading complexo |
| [[wiki/entities/stone]] | Fintech brasileira, mesmo grupo do Pagar.me — stack C# mais madura, mas com mais dificuldade de contratação que o Pagar.me/Node.js na mesma época |
| [[wiki/entities/gartner]] | Consultoria de mercado — projeta custo de codificação com IA superando salário médio de dev até 2028 |
| [[wiki/entities/uber]] | Estourou orçamento anual de IA em 4 meses por token maxing sem limite de consumo |
| [[wiki/entities/microsoft]] | Primeira grande onda de demissões em massa; Satya Nadella cunhou "capital de tokens" |
| [[wiki/entities/meta]] | Zuckerberg admite em memorando que a reestruturação de equipes por IA foi antecipada demais |
| [[wiki/entities/palantir-technologies]] | CEO critica modelo de cobrança por token e levanta a questão de quem controla a economia de IA |
| [[wiki/entities/fabricio-arcanjo]] | Participante do Stubborn Club — defende especificações técnicas agnósticas à linguagem de programação, focadas em DDD e padrões |
| [[wiki/entities/adapta]] | Agregador brasileiro de modelos de IA (adapta.org) — skills de contexto pessoal + roteamento automático de modelo (ONE/ONE Pro) |

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
