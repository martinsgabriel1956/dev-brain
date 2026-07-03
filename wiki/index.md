---
type: index
date_updated: 2026-07-03


---

# Wiki Index

## Sources

| Página | TL;DR |
|---|---|
| [[wiki/sources/3-dicas-colocar-conhecimento-em-pratica]] | André Casciotti: não peça permissão, separe mudanças em partes coesas, use automações pessoais como veículo de prática de baixo risco |
| [[wiki/sources/como-nao-ser-humilhado-no-primeiro-code-review]] | 5 passos para reduzir a fricção do primeiro code review: regra de negócio antes de estilo, revisar com IA sem virar dependência, testar em ambiente externo, não levar comentários pro pessoal, validar em produção |
| [[wiki/sources/pare-de-terceirizar-suas-decisoes]] | Akita: pare de terceirizar decisões de carreira para influencers e de parar de cargo-cultar stack de big tech — skin in the game, antifragilidade e custo afundado |
| [[wiki/sources/3-soft-skills-que-poucos-programadores-dominam]] | Renato Augusto: comunicação persuasiva (gatilhos de urgência/ganância), imagem profissional mesmo em home office, e habilidade de lidar com pessoas (Dale Carnegie) como as soft skills que a IA não substitui |
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
| [[wiki/sources/iso-27001-dicionario-programador]] | SGSI organizado em torno da tríade CIA; Anexo A 2022 com 93 controles em 4 temas; controles A.8.28/A.5.15/A.5.8/A.8.25/A.5.3 relevantes para devs; Policy as Code (OPA/Gatekeeper) como implementação; ISO 42001 para governança de IA |
| [[wiki/sources/escalabilidade-horizontal-load-balancer-algoritmos]] | Tipos de load balancer (hardware/software/cloud), por que AWS/Azure separam LB de camada 4 e 7, e algoritmos de balanceamento (Round Robin, Weighted, Least Connections, Least Time, Sticky) com demo prática em Nginx |
| [[wiki/sources/operador-de-crud-vs-engenheiro-repertorio]] | "Operador de CRUD" vs. engenheiro — o mundo debaixo do CRUD (redes, Bluetooth, streams, mobile, banco de dados); IA entrega o fácil, não o simples; repertório é a cola que a IA não substitui |

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
| [[wiki/concepts/gaming-de-testes-por-ia]] | IA deleta ou enfraquece testes que falham em vez de corrigir o código — proibir explicitamente |

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

### Processo de Desenvolvimento com IA

| Página | Hook |
|---|---|
| [[wiki/concepts/niveis-adocao-ia-l0-l4]] | L0 (hater) → L4 (fábrica); a maioria dos devs está no L2; salto de produtividade real ocorre no L3 |
| [[wiki/concepts/spec-driven-development]] | Planning-first: spec antes de executar; LLM executa autônoma; dev revisa resultado, não linha a linha |
| [[wiki/concepts/worktree-paralelismo]] | Git worktrees isolam tarefas paralelas; base do trabalho L3 — múltiplas specs rodando simultaneamente |
| [[wiki/concepts/subagentes]] | Paralelismo a nível de contexto — subtarefas convergem numa única PR; model/tools customizáveis por agente |
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
| [[wiki/concepts/syscall]] | Única ponte autorizada user mode → kernel — open/read/write/fork; custo de ~100–300ns por context switch |
| [[wiki/concepts/kernel]] | Núcleo do SO com acesso total ao hardware — kernel mode vs user mode; kernel panic é fatal porque não há fundação embaixo |

### Fundamentos de CS

| Página | Hook |
|---|---|
| [[wiki/concepts/logica-booleana]] | AND, OR, NOT — as três operações que constroem qualquer circuito a partir de 0s e 1s |
| [[wiki/concepts/big-o]] | Notação que descreve como o tempo cresce com os dados — O(log n) com 1B elementos = 30 comparações |
| [[wiki/concepts/recursao]] | Função que chama ela mesma — caso base (para) + caso recursivo (divide) |
| [[wiki/concepts/lista-encadeada]] | Nós encadeados por ponteiros — inserção O(1) no meio, acesso O(n) por posição |
| [[wiki/concepts/concorrencia]] | Gerenciar múltiplas tarefas — race condition é o risco central quando threads compartilham estado |
| [[wiki/concepts/paralelismo]] | Executar múltiplas tarefas ao mesmo tempo — requer múltiplos cores; oposto de concorrência |
| [[wiki/concepts/compilador]] | Traduz código-fonte em código de máquina via lexer → parser → AST → otimizador |
| [[wiki/concepts/protocolo-de-rede]] | Regras de comunicação em camadas — HTTP diz o quê, TCP garante entrega, IP define rota |
| [[wiki/concepts/criptografia]] | Hashing irreversível, simétrica (mesma chave) e assimétrica (par público/privado) — base do HTTPS |
| [[wiki/concepts/bluetooth-le]] | Advertising → scan → pair → GATT — o "handshake" do Bluetooth Low Energy; gerenciar mal o ciclo gera conexão fantasma e dreno de bateria |

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
| [[wiki/concepts/string]] | Slice de bytes + charset + encoding — imutável porque alterar bytes quebra UTF-8 silenciosamente |
| [[wiki/concepts/charset]] | Mapeamento valor numérico → caractere; distinto de encoding (que é o algoritmo de serialização) |
| [[wiki/concepts/ascii]] | 128 caracteres em 7 bits; charset e encoding ao mesmo tempo; subconjunto de UTF-8 |
| [[wiki/concepts/unicode]] | Charset universal com >1M codepoints; não é encoding — precisa de UTF-8 para ser serializado |
| [[wiki/concepts/utf-8]] | Encoding de largura variável para Unicode; criado por Ken Thompson e Rob Pike; padrão da web |

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
| [[wiki/concepts/complexidade-como-estrategia]] | Três estágios: inconsciente → aparência → sabotagem — criar código incompreensível para se tornar insubstituível |
| [[wiki/concepts/ciclo-da-desgraca-software]] | Espiral reescrita→mesmo problema→dois sistemas; alternativa: refatoração incremental com strangler fig |
| [[wiki/concepts/pitfalls-de-linguagem]] | Armadilhas que existem na linguagem mas não devem ser usadas — descobertas pelo uso, não pelo estudo teórico |
| [[wiki/concepts/dizer-sim-para-tudo]] | Dizer sim para tudo fragmenta foco e inibe surgimento de líderes — promessa é dívida, tempo estoura |
| [[wiki/concepts/definicao-de-pronto]] | Código que só funciona não está pronto — legível + testado + documentado + revisado por regra de negócio |
| [[wiki/concepts/testar-proprio-codigo]] | Testar só o caminho feliz é concordar com a própria opinião — testes automatizados cobrem erro e happy path |
| [[wiki/concepts/atomic-commits]] | Commit atômico = alteração + teste que a valida juntos — unidade funcional, não diário de mudanças |

### Segurança de APIs & Arquitetura

| Página | Hook |
|---|---|
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

### Frontend & Design Engineering

| Página | Hook |
|---|---|
| [[wiki/concepts/design-first]] | Layout no Figma antes do código — padrão em times grandes com designers dedicados; Figma fica desatualizado em times pequenos |
| [[wiki/concepts/code-first]] | Codar com component libraries sem layout prévio — velocidade alta, risco de Frankenstein visual |
| [[wiki/concepts/design-engineer]] | Cargo do meio: conhecimentos de design aplicados diretamente no código — experimentações no código, Figma como referência |
| [[wiki/concepts/component-library]] | Shadcn, Radix, Headless UI — componentes pré-prontos; headless dá controle total, estilizadas são mais rápidas |
| [[wiki/concepts/fake-delay]] | Delay mínimo intencional (300ms) para garantir feedback visual perceptível — performance percebida é design |
| [[wiki/concepts/design-como-interacao]] | Design se manifesta na interação, não na primeira impressão — micro-interações, onboarding, feedback, linguagem |

### Padrões e Design

| Página | Hook |
|---|---|
| [[wiki/concepts/pattern-recognition]] | Capacidade humana de detectar repetições — base do aprendizado por exposição |
| [[wiki/concepts/design-patterns]] | Catálogo de soluções nomeadas — útil só depois de já ter visto os padrões na prática |
| [[wiki/concepts/anti-pattern]] | Repetição que parece solução mas cria problemas — frequência não implica qualidade |
| [[wiki/concepts/over-engineering]] | "Verde neném" — aplicar patterns sem base; pular etapas da progressão produz complexidade sem valor |
| [[wiki/concepts/otimizacao-prematura]] | Raiz de todo mal (Knuth) — otimizar antes de ter projeto bom torna o código rígido e difícil |
| [[wiki/concepts/modelagem-orientada-a-objetos]] | Pré-requisito obrigatório para design patterns — classes, atributos, relacionamentos antes de GoF |

## Entities

| Página | Hook |
|---|---|
| [[wiki/entities/bernardo-lobato]] | Desenvolvedor e criador de conteúdo brasileiro — arquitetura de software e padrões avançados |
| [[wiki/entities/linuxtips]] | Plataforma brasileira de educação em tecnologia — DevOps, Cloud, Kubernetes, podcast Papinho Tech Solo |
| [[wiki/entities/renato-augusto]] | Desenvolvedor e criador de conteúdo brasileiro — padrões de projeto GoF e orientação a objetos, carreira e soft skills |
| [[wiki/entities/dale-carnegie]] | Autor de "Como Fazer Amigos e Influenciar Pessoas" (1936) — confiança e influência genuína como base da habilidade interpessoal |
| [[wiki/entities/eduarda-rocket-city]] | Engenheira de software internacional, criadora de conteúdo no canal Rocket City |
| [[wiki/entities/openai]] | Organização responsável pelo GPT-3/4 — formalizou in-context learning e scaling laws; criadora do tokenizer tiktoken |
| [[wiki/entities/google]] | Criadora do Gemini e do harness AntiGravity — concorrente de Anthropic e OpenAI, tokenizer próprio |
| [[wiki/entities/matt-pocock]] | Educador de TypeScript/AI (AI Hero) — fundamentos de LLM explicados via código TypeScript |
| [[wiki/entities/vercel-ai-sdk]] | SDK TypeScript da Vercel para chamar múltiplos provedores de LLM com API unificada |
| [[wiki/entities/jason-wei]] | Pesquisador Google Brain — lead author do paper de chain-of-thought prompting e do paper de emergent abilities |
| [[wiki/entities/fabio-akita]] | Programador brasileiro, autodidata desde 1991, criador do canal Akita On Rails |
| [[wiki/entities/lucas-badico]] | Programador e professor brasileiro, criador de conteúdo sobre Golang e carreira; defende a ponte fullstack como caminho de entrada ao backend |
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
| [[wiki/entities/lucas-montano]] | Criador de conteúdo brasileiro — argumenta que o pânico de "atrofia cognitiva" por IA mede o tipo errado de habilidade (sintaxe, não conhecimento perene) |
| [[wiki/entities/mercado-livre]] | Maior e-commerce/fintech da América Latina — combina ISO 27001 + PCI-DSS + Zero Trust; adotante consolidado de Go em produção |
| [[wiki/entities/andre-casciotti]] | Criador de conteúdo brasileiro, canal Próximo Nível — carreira dev, granularidade de mudança, automações pessoais como prática |

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
