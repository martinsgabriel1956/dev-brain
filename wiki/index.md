---
type: index
date_updated: 2026-08-10
---












# Wiki Index

## Sources

| Página | TL;DR |
|---|---|
| [[wiki/sources/potencial-programador-atitude-mindset]] | Lucas Montano "valida em código" o artigo de Gregor Ojstersek sobre potencial de engenheiros: atitude/mindset acima da tech skill, 3 traços (ownership, drive, team player), efeito multiplicador — mas conclui que na sua ponderação a tech skill segue dominante |
| [[wiki/sources/cache-vs-buffer-diferenca-conceitual]] | Bernardo Lobato: cache e buffer só têm em comum armazenar dados temporariamente — cache guarda cópias pela expectativa de **reutilização** (olha pro passado), buffer absorve **diferença de velocidade** produtor/consumidor e descarta após consumo (olha pro presente); mesma ideia do hardware (cache L1/L2/L3, buffer de I/O) à arquitetura distribuída (Redis, filas Kafka/SQS, streaming); buffer pool é cache apesar do nome |
| [[wiki/sources/escalar-para-um-milhao-de-usuarios]] | Augusto Galego (inferido): aula gratuita reconstruindo o capítulo "de zero a milhões de usuários" de Alex Xu — desenho incremental guiado por SPOF/gargalo (1 servidor → banco → cluster+LB → réplicas write/read → cache → CDN → stateless+NoSQL de sessões → filas/workers → tooling → multi-região) |
| [[wiki/sources/arquitetura-de-sacrificio]] | **Sacrificial Architecture** (Martin Fowler, 2014): jogar fora uma base de código **não é fracasso** — "o melhor código que você escreve hoje é o que vai descartar em alguns anos". Escolha *deliberadamente* uma arquitetura que será substituída (crescimento exponencial invalida decisões: eBay Perl→C++→Java; regra do "10×" do Google). Cedo priorize flexibilidade sobre performance; **não** abandone a qualidade interna (modularidade permite sacrificar módulos, não o sistema todo); cuidado com amortização contábil; **monolito** é melhor arquitetura de sacrifício que microsserviços (distribuição+assincronia = complexidade cedo demais), desmontado depois via strangler fig; quem escreveu o código é quem decide sacrificá-lo |
| [[wiki/sources/como-usar-ia-para-aprender-programacao-sem-atrofiar]] | Como usar IA no estudo de programação sem prejudicar o aprendizado: a **dificuldade desejável** (atrito/esforço) é o que cria conhecimento durável, então IA como *muleta* gera **atrofia cognitiva**, mas IA que *gera* dificuldade calibrada potencializa. Prós (personalização, democratização, multimodalidade) e contras (informações falsas, atrofia) do estudo com IA, e 4+1 dicas que preservam o esforço: questionários que acham gaps, apostilas de exercícios, questionar o *porquê* do código, desafios sem resposta e testes de borda sem apontar o erro |
| [[wiki/sources/monolito-modular-transicao-mvp-empresa-madura]] | Monolito modular como etapa entre o MVP simples e a empresa madura: microsserviços eliminam o código espaguete por impossibilidade estrutural (serviço não chama função de outro, só via rede/API), mas essa troca só compensa com razão real de hardware/escala; o monolito modular captura o isolamento sem o custo — um artefato, um banco, módulos que se comunicam por contratos/Ports & Adapters — e deixa a extração futura para microsserviço reduzida a trocar o transporte (função → gRPC) |
| [[wiki/sources/escalar-leituras-banco-de-dados-entrevista-tier-s]] | Vídeo 1 da série de System Design de Pedro Camaforte (base num artigo de Lucas Faria): como **escalar leituras** de banco em entrevistas Tier S, como uma escada de custo crescente que só se sobe quando o degrau anterior não basta — índices + connection pooling (~80% dos casos) → read replicas (200-300k+ req/s, tradeoff de replication lag) → cache (hotspots e queries caras, tradeoff de invalidação) → CDN (arquivos estáticos). O erro que elimina 90% dos candidatos: atacar arquitetura sem entender o contexto (volumetria, hotspots, criticidade). Caso canônico: encurtador de URL |
| [[wiki/sources/por-que-code-bases-degradam-estrategias-code-rot]] | Por que toda code base se degrada (code rot / entropia) e como conter: a degradação é o estado natural (requisitos sobre arquitetura estática, perda de contexto entre equipes, hotfix sob pressão, casos não previstos). Sinais: atraso crônico, testes flaky, "classes super-homem" (God Object) e "Devs Gandalf" (bus factor = 1). Contramedidas majoritariamente organizacionais: nunca alocar 100% da capacidade (~20% de folga — Reinertsen), regra do escoteiro no PR, medir o *erro* de estimativa, code owners, testes de integração como critério de aceitação; secundárias: feature freeze, análise estática com ressalva da Lei de Goodhart, ADRs. "Qualidade é uma prática, não uma feature" |
| [[wiki/sources/paradoxo-da-aceleracao-ia-produtividade-metricas]] | 93% dos devs usam IA mas a produtividade da empresa sobe só 10% (Faros AI): individualmente +21% de tarefas e ~2x PRs, mas o code review sobe 91% e vira o gargalo — o "paradoxo da aceleração". 95% se sentem mais produtivos produzindo código de qualidade menor; a IA amplifica sem julgamento (júnior +26–56%, sênior em legado zero/negativo — survey Pragmatic Engineer). Cura: medir outcome (bug rate, ciclo de review), não output |
| [[wiki/sources/seis-design-patterns-mais-usados-na-pratica]] | Os seis design patterns mais usados no mundo real segundo o autor, cada um com analogia do cotidiano: Observer (sino do YouTube), Factory (pedido de pizza), Singleton (elevador do prédio), Decorator (filtros do Instagram), Strategy (rotas do GPS) e Adapter (adaptador de tomada); nota como os patterns interagem entre si e alerta contra aplicar pattern sem problema real |
| [[wiki/sources/solid-principles-in-pictures-ugonna-thelma]] | Artigo original (Medium, 2020, Ugonna Thelma) por trás das ilustrações de robôs usadas no vídeo já ingerido — definições formais dos 5 princípios SOLID e o exemplo textual Coffee/Cappuccino/Water para LSP |
| [[wiki/sources/principios-solid-ilustrados]] | Vídeo que percorre os cinco princípios SOLID via ilustrações de robôs ("SOLID Principles in Pictures"), com exemplos de processador de pagamentos, ORM e extensões de navegador; propõe um "efeito dominó" entre os princípios e credita a Robert C. Martin (1996, não confirmado) a generalização de OCP+LSP em Dependency Inversion |
| [[wiki/sources/design-pattern-observer-codigo-fonte-tv]] | Código Fonte TV: Observer em TypeScript/Deno, dois exemplos — genérico (Subject/Observer com subscribe/notifyAll) e notificação de vídeo do YouTube com dois tipos de observer (Subscriber e Feed) reagindo ao mesmo evento |
| [[wiki/sources/uuid-quando-usar-pergunta-diogo]] | Resposta a uma pergunta de espectador sobre quando usar UUID: evita colisão de chave ao consolidar bases shardeadas/multi-origem, e dificulta ataques de enumeração de recursos (IDOR) em APIs REST; contra isso pesa espaço (16+ bytes), comparação manual difícil e performance; recomendação prática é híbrida — sequência interna (int) para joins + UUID/hash só nas tabelas expostas por rota, sem substituir autorização de verdade |
| [[wiki/sources/codigo-gerado-por-ia-mais-falhas-seguranca-degradacao-iterativa]] | Código gerado por IA tem ~2,77x mais falhas de segurança que código humano (CodeRabbit, Veracode); relatório Black Duck mostra 107% de aumento de vulnerabilidades por codebase em um ano; paper mostra que refinamento iterativo com IA piora a segurança (+37,6% de vulnerabilidades críticas após 5 rodadas), mesmo pedindo foco em segurança no prompt; propõe SAST no delta, limite de iterações, testes de segurança como contrato prévio e review em contexto limpo |
| [[wiki/sources/toolkit-aws-servicos-essenciais-para-aplicacoes-escalaveis]] | Tour do "80/20" da AWS sem abrir o console: EC2 (paga por tempo, não por uso) vs. Lambda (paga por execução, incluindo I/O ocioso) vs. Fargate; ECS e Elastic Beanstalk como camadas de orquestração/PaaS; ALB (L7) e API Gateway como roteamento; Step Functions como o caso mais extremo de vendor lock-in; RDS e DynamoDB; passagem rápida por SQS, SNS, CloudWatch, Secrets Manager, CloudFront e Amplify |
| [[wiki/sources/resolvendo-3-problemas-classicos-entrevista-coding-dsa]] | Três problemas clássicos de entrevista resolvidos do zero: Longest Consecutive Sequence (array + hash set, O(n) contra O(n log n) por ordenação), Top K Frequent Elements (hash map + bucket sort por frequência, O(n) contra O(n log n)), Reverse Only Letters (two pointers, O(n)) — ênfase em por que a explicação do raciocínio vale mais que a resposta |
| [[wiki/sources/binary-search-em-5-minutos]] | Vídeo curto: por que binary search exige array ordenado e chega em O(log n) contra O(n) da busca linear; implementação com two pointers em vez de recursão com recriação de array; resolvido ao vivo no LeetCode em menos de 5 minutos |
| [[wiki/sources/infraestrutura-como-codigo-cdk-aws]] | Por que configurar infraestrutura clicando no console AWS não é reproduzível nem documentado; panorama de ferramentas de IaC (Terraform/OpenTofu, CloudFormation, CDK, Pulumi); demo ao vivo de um bucket S3 + Lambda via AWS CDK em TypeScript (`cdk deploy`/`cdk destroy`) |
| [[wiki/sources/react-reconciliacao-memo-usememo-usecallback]] | Algoritmo de reconciliação demonstrado no React DevTools Profiler (renderizar ≠ tocar o DOM real); `React.memo` e as 4 situações onde compensa; igualdade referencial/shallow compare quebrando `memo` com funções e objetos recriados; `useCallback` com forma funcional de setState para remover dependências; `useMemo` para cálculo caro e para estabilizar referência de objetos |
| [[wiki/sources/sharding-charging-fragmentacao-banco-de-dados]] | Renato Augusto, continuação da playlist de System Design: sharding de banco de dados de ponta a ponta — escolha de shard key (com dois exemplos de má distribuição: `created_at` e faixas fixas de `user_id`), hash-based sharding com módulo passo a passo, consistent hashing, problema da celebridade, cross-shard operations resolvido com cache, transações distribuídas resolvidas com Saga, e a tese de que sharding pressupõe decomposição por DDD/microsserviços |
| [[wiki/sources/autenticacao-moderna-senha-sessao-jwt-oauth-mfa-passkeys]] | Vídeo de ponta a ponta sobre autenticação moderna: authn vs. authz, password hashing (work factor, salt), erros de login (mensagens genéricas, rate limiting, SQLi), sessões (session fixation, invalidação ao trocar senha, Redis), JWT (HMAC vs. RSA/ECDSA, rotação de refresh token), OAuth/PKCE (open redirect, state), OIDC (nonce, escopos), MFA (step-up authentication), passkeys e CORS mal configurado |
| [[wiki/sources/ha-vs-ft-alta-disponibilidade-tolerancia-a-falha]] | Aula curta: distinção entre HA (topologia ativo-passivo — banco primário/secundário com failover e janela de indisponibilidade durante o switch) e Tolerância a Falha (topologia ativo-ativo — nós idênticos já servindo tráfego em paralelo, sem janela perceptível); FT não é 100% de disponibilidade (retry após erro pontual já cai no lado saudável) e custa estruturalmente mais que HA |
| [[wiki/sources/rto-rpo-recovery-time-point-objective]] | Aula curta: RTO (tempo de recuperação) e RPO (dado tolerável de perda) como indicadores focados em desastre que devem ser definidos a partir do negócio antes da arquitetura — exemplo de custo de downtime ($1.000/minuto) e tolerância a RPO radicalmente diferente entre sistema financeiro, e-commerce e microsserviço de catálogo |
| [[wiki/sources/sre-capacidade-observabilidade-confiabilidade-custo]] | Aula introdutória: cinco pilares de "sucesso" na visão de um SRE — planejamento de capacidade (alimentado por observabilidade), observabilidade (traceability fim-a-fim), otimização de custo (às vezes gastar mais para perder menos), Release Engineering (estratégias de deploy) e segurança; fecha com confiabilidade como guarda-chuva (consistência, durabilidade, tolerância a falhas, previsibilidade, disponibilidade de recursos) |
| [[wiki/sources/cinco-escolas-programacao-com-ia]] | Mano Deivin: cinco "escolas" de programação com IA organizadas no "autonomy slider" de Karpathy — copiloto, delegação total/spec-driven, "na unha" (Peter Naur), loop sem supervisão (Ralph Loop); DHH e Antirez trocaram de "anti-agente raiz" para agent-first em ~6 meses; distinção de Antirez entre automatic programming e vibe coding |
| [[wiki/sources/codificacao-de-caracteres-ascii-iso-8859-1-unicode]] | Aula curta do professor Olibário: por que ASCII usa só 7 dos 8 bits (0–127), limitações sem acentos/alfabetos não latinos, ISO-8859-1/Latin-1 como extensão de 8 bits (0–255) idêntica a ASCII até 127, Unicode/UTF-8 como solução universal; fecha com exercício de decode ASCII (`66 69 67 65` → "BECA") |
| [[wiki/sources/testes-de-seguranca-pentest-com-claude-code-pulsar-saas]] | Vlog em primeira pessoa: dev sem background em segurança usa o Claude Code como "professor" para autopentest do Pulsar (SaaS pessoal) — nove perguntas cobrindo autenticação/logout, IDOR, CSRF, XSS/SQLi, abuso de regra de negócio via API, vazamento em mensagens de erro, rate limiting, dependências vulneráveis e segredos no histórico de git; método de seis passos para prompt de segurança eficaz |
| [[wiki/sources/vibe-coding-env-exposto-idor-account-takeover-rce-loja-ia]] | Pentester demonstra cadeia de ataque completa (lab controlado) contra loja fictícia construída via vibe coding (Cursor/Lovable/Claude Code): `.env` exposto (achado via dirsearch) → IDOR em pedidos → IDOR em perfil vazando chave de integração → account takeover sem senha → escalonamento a admin por enumeração de IDs no Burp Intruder → RCE via upload de plugin sem validação; menos de 10 minutos ponta a ponta |
| [[wiki/sources/ddos-sim-flood-servidor-find-my-saas]] | Post-mortem em primeira pessoa: SYN flood de 260 milhões de requests em um dia contra um SaaS pequeno atrás de Cloudflare — modo Under Attack desativado, proxy reverso (Traefik via Coolify) com bug de CPU/memory leak auto-atualizado durante o próprio incidente; servidor não recuperado, reconstruído do zero com firewall → Docker → proxy nessa ordem |
| [[wiki/sources/pkce-proof-key-code-exchange-spa-mobile]] | PKCE (RFC 7636) resolve o problema do client secret dinâmico em SPA/mobile — `code_verifier` gerado no cliente, hash (`code_challenge`) enviado na autorização, `code_verifier` original revelado só na troca do código por token; substitui o Implicit Flow (deprecated, token na URL) e é obrigatório no OAuth 2.1 para todos os clients |
| [[wiki/sources/rfc-7636-pkce-oauth-public-clients]] | Texto normativo completo do RFC 7636 (IETF, 2015), traduzido PT-BR — ABNF exata do `code_verifier` (43-128 chars), `S256` como MTI vs. `plain` desaconselhado, razão para não usar salting no `code_challenge`, e regras de retrocompatibilidade servidor/cliente |
| [[wiki/sources/microsservicos-do-zero-deadlock-2pc-saga-cqrs]] | Aula didática que constrói incrementalmente o percurso clássico de microsserviços: deadlock por banco compartilhado → banco por serviço → quebra de atomicidade → two-phase commit → gargalo de coordenação → Saga Pattern via fila (RabbitMQ)/event-driven → CQRS com read/write split e trade-off de replication lag |
| [[wiki/sources/clean-architecture-arquitetura-centrada-no-dominio]] | Vídeo (inglês, traduzido) comparando 3-tier vs. Clean Architecture via app de lembretes — explica por que Clean Architecture é "domain-centric": lógica de negócio dividida em Application (use cases) + Domain (entidades/regras), banco na infrastructure layer, Dependency Rule via interfaces definidas por dentro e implementadas por fora |
| [[wiki/sources/arquitetura-limpa-na-pratica]] | Livro completo (Otávio Lemos, 2022) ensinando Clean Architecture via estudo de caso TypeScript (theWisePad): genealogia DCI/BCE/Hexagonal, Regra de Dependência, Either monad para erros, Value Objects auto-validados, crítica a ORM/Active Record, e casos reais de adoção (Netflix, Uber, iFood) |
| [[wiki/sources/delay-tv-aberta-vs-youtube-live-latencia-streaming]] | Por que uma live de futebol no YouTube chega atrasada em relação à TV aberta — buffer de leitura antecipada como principal causador de latência (segundo doc. do YouTube), radiodifusão sem sessão individual por espectador na TV aberta, modos de latência do YouTube (normal/baixa <10s/ultra baixa <5s) |
| [[wiki/sources/email-address]] | Endereço de e-mail via RFC 5322/5321: `local-part@domain`, parte local case-sensitive na spec mas case-insensitive na prática, sub-addressing (`+tag`) formal via RFC 5233, domínio via regras LDH e resolução por registros MX; internacionalização (EAI/SMTPUTF8) permite UTF-8 completo; sintaxe válida não prova que a caixa existe |
| [[wiki/sources/14-habitos-desenvolvedores-altamente-produtivos]] | Zeno Rocha: 14 hábitos de dev produtivo em 5 categorias — JOMO contra FOMO tecnológico, ensinar como forma de aprender, consistência (jogo infinito) > intensidade, código para o "eu futuro", visão de negócio (problema XY), triagem de side project em 6 perguntas, Mario vs. Sonic (tempo de casa), ouvir para entender, 5 razões para subestimar tarefas, especialista vs. generalista, e a dicotomia estoica do controle |
| [[wiki/sources/full-text-search-mysql-postgresql]] | `LIKE '%termo%'` é a intuição errada de busca — falha em relevância (substring de caracteres, não palavras) e em performance (full table scan); Full-Text Search resolve os dois via índice invertido — `FULLTEXT INDEX`/`MATCH AGAINST` no MySQL, `tsvector`/`tsquery`/`GIN` no PostgreSQL (que ainda entende plural/singular e sinônimos via lexema/tesauro) |
| [[wiki/sources/indice-de-banco-de-dados]] | O que é um índice de banco de dados e por que existe — demonstração visual de B-tree se reordenando e busca em O(log n); B-tree (padrão, range) vs. hash (match exato, O(1)) vs. composto vs. único/não único vs. parcial vs. full-text vs. espacial; regra de ouro: índice é ditado pelo padrão de acesso |
| [[wiki/sources/como-um-banco-de-dados-funciona-por-dentro]] | Caminho completo de uma escrita num banco relacional via exemplo de Pix: páginas → buffer pool (buffer hit/miss, dirty pages) → WAL (commit responde antes da página final) → transação/atomicidade → locks + MVCC → isolation levels (Read Committed vs. Repeatable Read) → índice como dado com custo de manutenção → vacuum/compaction → checkpoint/recovery; fecha com "banco não é só um arquivo" |
| [[wiki/sources/rapid-release-at-massive-scale-facebook]] | Post do Facebook Engineering (2017): migração de ~700 cherry-picks manuais/dia para push quase-contínuo direto da master, com rollout escalonado (funcionários → 2% → 100%) e o feature-flag interno Gatekeeper desacoplando deploy de release; mobile reduziu ciclo de release de 4 para 1 semana escalando o time 15x sem perder qualidade |
| [[wiki/sources/problema-n-mais-1-graphql-orm-solucoes]] | N+1 em duas camadas — frontend↔backend (via API) e backend↔banco (via ORM lazy loading) — mesmas soluções estruturais (endpoint/query especializada, lista de IDs conhecida, ou JOIN/prefetch); origem do GraphQL na Meta como resposta genérica ao N+1/over-under-fetching entre múltiplos frontends; fecha com relational queries do Drizzle como syntax sugar inspirado no GraphQL |
| [[wiki/sources/aprenda-a-programar-do-jeito-dificil]] | Por que estudar linguagens e conceitos low level (mesmo sem retorno financeiro imediato) traz satisfação pessoal e benefício de carreira no longo prazo — caso pessoal do bot de Discord de Tibia otimizado com concorrência em Go, e da contribuição não remunerada à API TibiaData |
| [[wiki/sources/7-habitos-programador-altamente-eficaz]] | Sete hábitos de programador eficaz: buscar solução por conta própria antes de perguntar, escapar da paralisia do planejamento sem cair em over-engineering, ler código alheio, documentar de forma inteligente (testes como documentação viva), pensar primeiro em abstrações/limites (analogia dos órgãos), perder o medo de código, e bloquear a própria agenda para "entortar o tempo" |
| [[wiki/sources/pipeline-de-renderizacao-do-browser-url-ate-pixel]] | Seis etapas entre digitar a URL e o primeiro pixel: cache → DNS → TCP handshake → TLS → request HTTP → parsing HTML/CSS em DOM/CSSOM → render tree → layout → paint → composite; JavaScript síncrono bloqueia o parser, daí async/defer; cada otimização clássica (minificar, defer, CSS raso, transform/opacity) ataca uma etapa específica |
| [[wiki/sources/database-migrations-sql-cru-vs-orm-drizzle]] | Migrar banco na mão via SSH é considerado errado (não auditável/reproduzível); migrations devem ser versionadas em git e passar por PR/review; demonstração prática de migrate up/down com SQL cru (docker-compose + Postgres local) e com Drizzle ORM (fluxo invertido: schema declarado → migration derivada); mesmo com ORM, migration em tabela grande pode travar produção |
| [[wiki/sources/connection-pooling-pool-vs-polling-serverless]] | Desambiguação poll/pool; pool de conexões deve ser singleton instanciado fora do handler de rota; bug de `client.release()` esquecido vazando a pool aos poucos; connection pooling em serverless (Lambda sem memória compartilhada) via RDS Proxy, "attach database pool" da Vercel, suporte nativo de ORM, ou PgBouncer (com disclaimer de uso não testado pelo autor) |
| [[wiki/sources/anatomia-entrevista-system-design-bigtech]] | Pipeline bigtech de 5 etapas (RH → técnica/LeetCode → system design → fit) e o que cada etapa da sessão de system design (requisitos, BOE, API, esquema SQL+NoSQL, HLD, tradeoffs) está de fato avaliando — compreensão do problema exposta em voz alta, não caixinhas decoradas |
| [[wiki/sources/ia-nao-substitui-sistemas-corporativos-deterministicos]] | Curso de COBOL/mainframe: validador de tarefas via LLM falhou de forma inconsistente por 3 semanas — as 3 IAs (GPT, Claude, Gemini) diagnosticaram "ferramenta de análise semântica usada para análise determinística"; sistemas corporativos (juros, impostos, folha) exigem 100% previsibilidade, não "quase certo"; cortes de projetos de IA não são bolha, são erro de enquadramento (IA substituindo software em vez de interpretar para ele) |
| [[wiki/sources/historia-autenticacao-senha-mfa-oauth-jwt]] | Percurso de 70 anos da autenticação: user ID sem senha (time-sharing anos 60) → senha com hash+salt (Unix, 1976) → MFA (sei/tenho/sou) → segundo fator (RSA SecurID → HOTP/TOTP → U2F/WebAuthn) → biometria (3 gerações) → identidade federada (SSO → OAuth 2.0 → OpenID Connect) → JWT com Access/Refresh Token |
| [[wiki/sources/problemas-de-escopo-aberto-vs-fechado]] | Jogos e redes sociais treinam o cérebro para problemas de escopo fechado (objetivo + caminho previsível); vida real exige operacionalizar problemas de escopo aberto e trocar foco de resultado por ação; "burrice" costuma ser inexperiência, cuja cura é experimentar (base: playlist do Dr. Alok Kanojia) |
| [[wiki/sources/mitos-fable-5-bloqueio-governo-eua-cyberseguranca]] | Código Fonte TV: Mitos e Fable 5 (Anthropic) e GPT 5.6 (OpenAI) — modelos de IA capazes de achar vulnerabilidades de software em escala inédita (falhas de décadas em OpenBSD, FFmpeg, kernel Linux), restritos ao consórcio Glasswing e depois bloqueados pelo governo dos EUA após a NSA relatar sistemas confidenciais comprometidos em horas; jailbreak do Fable 5 documentado (702/7.828 tentativas); Japão (Sakana AI/Fugo) e China (360/Tulong Fang, Zhipu AI/GLM 5.2) já reivindicam capacidade equivalente |
| [[wiki/sources/vale-a-pena-estudar-microsservicos-mesmo-sem-usar]] | Bernardo Lobato: estudar microsserviços vale a pena mesmo sem usar em produção, porque funciona como eixo unificado de aprendizado (bounded context, circuit breaker, saga, observabilidade, mensageria, times autônomos); relato pessoal de retorno ao mercado após anos em monólitos legados; fundamentos como o que permite curar sugestões de IA |
| [[wiki/sources/loop-engineering-niveis-dev-loop-jogo-mmo]] | Três níveis do dev loop (React → spec driven → humano) e loop engineering como quarta camada; distinção loop fixo (sem side effect) vs. loop criador (roadmap iterativo, risco de perpetuar bugs); caso Ban→Rust e jogo MMO completo construído em um final de semana; quatro perguntas para decidir se vale usar loop |
| [[wiki/sources/loop-engineering-harness-e-a-frase-que-viralizou]] | Pedro Nauke (Compose): loop = 4 peças (objetivo checável, ação, feedback, condição de parada); origem no padrão ReAct (2022/2023); três fatores que destravaram loops longos em 2026 (modelo, harness, estado persistente); correção da frase viral "loop engineering matou harness engineering" — o loop contém o harness, não o substitui |
| [[wiki/sources/harness-engineering-voce-e-o-harness-nao-o-modelo]] | Frase viral de Peter Steinberger; matemática de erros compostos (0,99ⁿ) em processos de múltiplas etapas; quatro mitigações (verificação, checkpoints, ferramentas, contexto limpo); caso Vercel (remoção de 80% das ferramentas); Ralph Loop (Geoffrey Huntley, 2025); quatro níveis oficiais de loop da Anthropic (turn/goal/time/proactive); doze componentes do harness (sete documentados) |
| [[wiki/sources/jspace-cerebro-cloud-antropic]] | Lucas Montano reage à pesquisa "J-Space" da Anthropic: espaço interno de ativações do Claude vinculável a palavras nunca ditas, lido via Jacobian Lens; não é chain-of-thought; tese pessoal do autor de que isso vira base de cobrança/auditoria de agentes |
| [[wiki/sources/system-design-simulador-hotel-booking-replit]] | System design como a competência que a IA não substitui — construção de um simulador de system design via Replit e exercício prático de hotel booking (gargalo no banco → cache → load balancer → réplicas → fila Kafka, nota de IA 58/100) |
| [[wiki/sources/verdades-duras-programador-20-anos-pedro-nauck]] | Pedro Nauck: 5 verdades duras de 20+ anos de carreira — ego não discrimina por senioridade, side projects populares viram maldição de manutenção (caso Docz), reinventar a roda é remix com custo de manutenção, cultura brasileira do "hard worker" normalizou entrega mínima, e overthinking/over-engineering resolve problemas que ainda não existem |
| [[wiki/sources/api-gateway-padrao-essencial-arquiteturas-distribuidas]] | Bernardo Lobato: API Gateway como ponto único de entrada (roteamento, auth, mapeamento de payload, edge functions); API Composition/API Composer para orquestrar e agregar múltiplos endpoints; BFF como Gateway especializado por tipo de cliente; desafios centrais são single point of failure e Gateway virando gargalo por acúmulo de funções de borda |
| [[wiki/sources/como-lidar-com-tarefas-dificeis-sendo-junior]] | André Casciotti: tarefas difíceis parecem mais difíceis do que são — síndrome do impostor ataca em todo nível, tarefas complexas naturalmente vão para seniores; 3 técnicas: seguir o fluxo do código desde a ação do usuário, dividir tarefas até responder "seguro?"/"tenho prazo?", organizar trabalho com lista escrita e progresso visível |
| [[wiki/sources/os-3-estagios-de-maturidade-para-testar-codigo]] | Filipe Deschamps (autoria inferida): três estágios de maturidade para testar código — clicar manualmente na UI, Postman contra API-first/dogfooding no Pagar.me, e testes automatizados em modo watch (Jest); expectativa que quebra expõe vulnerabilidade real de autorização (403 vs 200) e o mesmo teste pega regressão futura sem verificação manual |
| [[wiki/sources/20-melhores-praticas-claude-code-segundo-anthropic]] | ~19 boas práticas de Claude Code atribuídas à documentação oficial da Anthropic: verificação embutida no prompt, descrever resultado e não passos, checkpoints/rewind, gerenciamento de sessões, `/go`, alocação de modelo por leverage, sandbox para loops não interrompidos, retenção de 30 dias |
| [[wiki/sources/3-pilares-testes-automatizados-produtividade]] | Erick Wendel: 3 pilares — entender a tarefa antes de codificar (loop de confirmação de entendimento), setup de live reload/debug/testes integrados (node --watch/--inspect/--test + launch.json), e decompor tarefa em entrada/processamento/saída + Given/When/Then antes de implementar (exemplo Rinha de Backend); tipagem forte via JSDoc sem TypeScript |
| [[wiki/sources/5-cuidados-antes-de-comecar-a-programar]] | Autoria inferida (Filipe Deschamps): 5 armadilhas de mentalidade ao aprender a programar — bomba de efeito moral (choque de complexidade que paralisa), relação criador-criatura (pedestal técnico), programar sem mirar impacto real, escolher o projeto (com "adrenalina") antes da tecnologia, e desligar autocomplete para não sabotar a spaced repetition |
| [[wiki/sources/kimi-k3-china-mercado-ia-open-source]] | Kimi K3 (Moonshot, 2,8T parâmetros, MoE 896/16 experts, até 75% economia de KV Cache) como estudo de caso: sanções de exportação de chips forçam inovação arquitetural que, ao virar open source, espalha conhecimento de inferência barata — tese central: a camada de aplicação importa mais que o modelo, lock-in em um único provedor não faz sentido |
| [[wiki/sources/8-sistemas-operacionais-explicados]] | Panorama dos 8 SOs mais conhecidos: Windows, macOS, Linux, Chrome OS, Android, iOS, Unix e BSD — propósito, mercado, vantagens e desvantagens de cada um |
| [[wiki/sources/5-dicas-entrevistas-lousa-branca-system-design]] | Full Cycle (Wesley Willians): 5 dicas para entrevista de system design/lousa branca — gerenciar tempo, requisitos core antes de desenhar, plano de capacidade, modelagem de dados/API, e só então o desenho; nunca citar tecnologia que não domina |
| [[wiki/sources/ai-jail-sandbox-para-agentes-de-ia-akita]] | AI Jail (Fábio Akita): sandbox via Bubblewrap para conter agentes de codificação de IA contra supply chain attacks (ex.: npm postinstall malicioso); modelo de 3 camadas — sessão/AI Jail, código/Git, SO imutável; comparação com o opt-out do sandbox nativo do Claude Code |
| [[wiki/sources/pos-graduacao-arquitetura-software-vale-a-pena]] | Renato Augusto: "vale a pena" sem objetivo definido não tem resposta; pós-graduação em arquitetura ensina teoria, não prática, nem em instituições renomadas; vantagens reais são networking, acesso a vagas com exigência de diploma e visão de negócio (churn, CAC, LTV) |
| [[wiki/sources/leetcode-como-se-preparar-entrevistas-coding-anthony-mays]] | Anthony D. Mays (ex-entrevistador big tech): memorize o padrão, não o problema; resposta certa não basta, processo de raciocínio importa mais; ficar travado é esperado; fazer perguntas de esclarecimento é trabalho do candidato, não do entrevistador |
| [[wiki/sources/como-praticar-leetcode-da-forma-certa-anthony-mays]] | Artigo original (2022) de Anthony D. Mays: entrevista é exercício colaborativo, não prova solo; framework "Os Seis Passos" como roteiro de dez etapas de mock interview — cronômetro real, ouvir o problema sem ler o enunciado, estimar Big-O antes de codar, implementar sem pseudocódigo, diário de progresso |
| [[wiki/sources/kiss-yagni-entrega-rapida-qualidade]] | Everton Oliveira: KISS (origem Marinha dos EUA) e YAGNI como os dois princípios que resolvem o dilema velocidade vs. qualidade — exemplo de refactor de validação de status e de repositório com métodos CRUD implementados por precaução |
| [[wiki/sources/analise-curriculos-programador-junior-dicas-ats]] | Reação a currículos reais de candidatos júnior: repetição da stack-alvo para passar no ATS, ausência de GitHub como motivo de descarte explícito, formatação/legibilidade e discurso de "pensar produto" como diferenciais |
| [[wiki/sources/8-tipos-de-javascript]] | Os 8 tipos de JS (`null`, `undefined`, `boolean`, `number`, `bigint`, `string`, `symbol`, `object`); `typeof` vs. `Object.prototype.toString.call()`; `==` vs `===`; default de parâmetro (`undefined`) vs. fallback `\|\|` (qualquer falsy) |
| [[wiki/sources/filosofia-do-design-de-software-introducao]] | Tradução do cap. 1 de *A Philosophy of Software Design*: complexidade como maior limitação real ao escrever software; eliminar vs. encapsular; por que waterfall falha e design incremental funciona; red flags via code review |
| [[wiki/sources/filosofia-do-design-de-software-livro-completo]] | Livro completo (22 caps.) de *A Philosophy of Software Design*: information hiding, módulos de propósito geral, camadas/pass-through, definir erros para fora da existência, projetar duas vezes, comentários como ferramenta de design, naming, consistência, tático vs. estratégico — com 3 discordâncias explícitas nomeadas contra Clean Code e o guia de estilo do Go |
| [[wiki/sources/git-rebase-na-pratica]] | Tutorial prático de `git rebase`: reposiciona a base de uma branch de feature na ponta atual da `main`, demonstração ponta a ponta com conflito real (mesmo arquivo alterado nos dois lados) resolvido no editor do VS Code; regra de ouro — rebase só em repositório local, nunca em branch pública/compartilhada |
| [[wiki/sources/ssh-chaves-como-funcionam]] | Chave SSH é par assimétrico (privada nunca sai da origem, pública vai pro `authorized_keys` do destino) e é unidirecional por par — `sshd_config.d` com `PubkeyAuthentication yes` + senha desativada é o padrão de indústria; `~/.ssh/config` cria aliases com `IdentitiesOnly` |
| [[wiki/sources/loop-engineering-planner-critic-grafo]] | "Você não faz o prompt, você desenha o sistema que faz o prompt" — Planner gera prompt+rúbrica dinamicamente para subagentes, Verificador (outro modelo) aprova/rejeita, grafo (nós=LLM, arestas=determinístico) é o nível de abstração |
| [[wiki/sources/graph-engineering-do-loop-ao-grafo]] | "Graph engineering" a partir de um tweet de Peter Steinberger: grafo ensinado do zero (nó/aresta/peso) com exemplos cotidianos (rotina matinal, rede social, funil tráfego→ativação→churn→LTV); "uma métrica nunca é suficiente" (CAC isolado pode subir churn e derrubar LTV); gestão de projeto (épico→história→tarefa) como grafo de dependências, não árvore; fecha com fundamentos como alavanca contra o FOMO de hype semanal |
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
| [[wiki/sources/objetos-vs-estruturas-de-dados-clean-architecture]] | Post de blog de Uncle Bob: objeto vs. estrutura de dados como conceitos opostos; por que "Object-Relational Mapper" é nome equivocado; fluxo completo de Clean Architecture numa aplicação web (Controller → Use Case → Entities → Presenter → View) |
| [[wiki/sources/orm-sql-organizacao-regras-negocio-bancos-dados]] | Q&A: ORM inviável com relacionamentos profundos/chaves compostas força SQL direto; stored procedure com moderação; relatório sempre bate em réplica; relacional vs. não relacional depende da necessidade de junções múltiplas |
| [[wiki/sources/chain-of-thought-prompting]] | CoT prompting (Wei et al., 2022) — passos intermediários como exemplares few-shot é uma capacidade emergente de ~100B+ parâmetros; supera GPT-3 fine-tuned no GSM8K via prompting apenas |
| [[wiki/sources/oracle-demite-milhares-anatomia-agente-dba-autonomo]] | Lucas Montano (inferido): layoff de 20-30 mil pessoas na Oracle (motivo alegado: agente de IA substituindo DBAs) usado como gancho para ensinar blueprint de agente autônomo de produção — 5 peças (planner, tool loop, observação, decisão, write-back) + 4 componentes (trigger, whitelist, loop de observação, escape hatch por limiar de confiança); fecha com a tese de que automação só demite quando a empresa não converte o tempo liberado em mais valor |
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
| [[wiki/sources/algoritmo-decode-utf8-com-tdd]] | Continuação prometida do vídeo de strings: implementa `DecodeRune` em Go via TDD (testes importados da stdlib), usando AND/OR/left shift; valida overlong encoding, surrogate pairs e codepoint máximo |
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
| [[wiki/sources/tres-estagios-de-acoplamento-observer-pattern-na-pratica]] | Três estágios de acoplamento via refatoração de um jogo em JS — tudo misturado → Factory com chamada estática → Observer sem conhecimento estático; heurística "de quem é essa linha?" |
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
| [[wiki/sources/conceitos-que-regem-a-computacao-bits-turing-complexidade]] | Da representação binária (bit/byte) à máquina de Turing, determinismo × não-determinismo e complexidade (Big O) — fechando em por que a criptografia é segura pela inviabilidade exponencial |
| [[wiki/sources/9-algoritmos-que-todo-programador-deveria-saber]] | Nove algoritmos em três categorias — ordenação (Bubble, Insertion, Merge), busca (Linear, Binary) e grafo (DFS, BFS, Dijkstra, A*) |
| [[wiki/sources/escalabilidade-vertical-horizontal-system-design]] | Vertical vs horizontal, Load Balancer, stateless, CDN, auto scaling, sharding, replicação — quando e como escalar cada camada |
| [[wiki/sources/the-comparison-trap-in-programming-careers]] | Bastidor vs palco + familiaridade vs capacidade — as duas formas de comparação que destroem iniciantes; quatro estratégias para medir evolução contra si mesmo |
| [[wiki/sources/tokens-llm-fundamentos-typescript]] | Tokens em LLMs explicados via TypeScript — encode/decode, treino de tokenizer, trade-off de vocabulário, palavras raras custam mais tokens |
| [[wiki/sources/akita-oferta-procura-matematica-carreira]] | Lei de oferta e procura em ciclos de mercado tech; raciocínio matemático básico (juros compostos) como diferencial de carreira; apego a ferramentas como estagnação |
| [[wiki/sources/engenheiro-vs-programador-mercado-ia]] | Programador executa, engenheiro governa — o paradoxo da IA (mais código gerado = mais demanda por quem governa) e o roadmap de fundamentos em dois eixos, técnico e humano |
| [[wiki/sources/server-sent-events-sse-tempo-real]] | SSE na prática: formato `data`/`event`, polling disfarçado como erro comum, Redis Pub/Sub entre microsserviços, Singleton na conexão, auth via JWT em query string |
| [[wiki/sources/multiplos-agentes-worktrees-subagentes-claude-code]] | Worktrees (paralelismo de file system, `claude --worktree`) vs. subagentes (paralelismo de contexto, `.claude/agents/`) — quando usar cada um e o risco de excesso de skills/agentes sobrepostos |
| [[wiki/sources/git-worktree-paralelismo-ia-codex-claude-abacus]] | Demonstração ao vivo de `git worktree add`/`list`/`remove -f`; suporte nativo comparado entre o app do Codex e `claude --worktree`; bloco patrocinado da Abacus.AI sobre Multi-Engine Agent Farm e CLI própria |
| [[wiki/sources/golang-mercado-trabalho-frontend-para-backend]] | Go não é passageiro — cloud native por design, já consolidado em Mercado Livre/Mercado Pago/Stone; estratégia para frontend migrar: mirar pleno e usar fullstack como ponte |
| [[wiki/sources/impacto-ia-mercado-frontend]] | IA comoditizou nichos de CRUD (agência, freelancer de landing page, consultoria pequena/média) e comprimiu salário de sênior remoto (14–18k → 11–14k); requisitos viraram spec-driven + harness próprio; monorepo favorece contexto de IA mais que microfrontends |
| [[wiki/sources/5-boas-praticas-uiux-ux-pilot]] | Comparação Cursor vs. UX Pilot na mesma landing page: hierarquia visual, lei da proximidade (Gestalt), affordance e interface como máquina de estados — os quatro conceitos de design que fazem prompts de geração de UI saírem de resultado genérico para profissional |
| [[wiki/sources/updates-tempo-real-polling-sse-websocket]] | Polling, SSE e WebSocket sob a lente de entrevista — quando polling simples é a resposta certa, LB L4 vs L7, tópico por usuário no Redis Pub/Sub, tabela de mensagens pendentes para offline |
| [[wiki/sources/atrofia-cognitiva-ia-programacao]] | Sintaxe já era irrelevante antes da IA (autocomplete + Google); conhecimento perene (401/500, debugging de produção) é o que importa; fundação sólida torna atrofia reversível, mas quem aprendeu já com IA não tem o que recuperar |
| [[wiki/sources/tdd-sdd-bdd-era-ia]] | TDD (red-green-refactor), SDD (contrato de boundary — OpenAPI/Protobuf/GraphQL) e BDD (Gherkin) como práticas com viés comportamental que também funcionam impostas sobre IA; proibir a IA de deletar testes que falham |
| [[wiki/sources/shopify-redis-para-mysql-skip-locked-black-friday]] | Shopify substituiu reserva de estoque Redis+MySQL por MySQL puro com SKIP LOCKED; corrigiu gap locking e PK mal desenhada; gargalo real era conexão segurada pelo checkout legado, não a query de reserva; -50% leituras, -33% transações, US$ 5,1M/min na Black Friday 2025 |
| [[wiki/sources/lean-startup-para-devs-mano-deivin]] | Dev desmotivado quer largar tudo e construir seu próprio produto — Lean Startup (Eric Ries) como antídoto: validar a dor antes de codar, MVP de funcionalidade única, ciclo construir-medir-aprender, teste A/B, e apaixonar-se pelo problema, não pela solução |
| [[wiki/sources/indistraivel-nir-eyal-mano-deivin]] | Resumo de *Indistraível* (Nir Eyal): dominar gatilhos internos (anotar em vez de agir), time boxing, hackear gatilhos externos (notificações) e pactos anti-distração (esforço, preço, público) — o antídoto do autor ao próprio *Hooked* |
| [[wiki/sources/5-ou-6-dicas-para-projetos-novos]] | Checklist do primeiro dia de um projeto novo: escolha de stack (aprender vs. monetizar), estrutura documentada antes de codar, deploy imediato do boilerplate com CD automático, ORM mínima com migrations desde o dia 1, testes na pipeline antes de features, README + AGENTS.md |
| [[wiki/sources/akita-discurso-howard-roark-a-nascente-ayn-rand]] | Akita lê o discurso de Howard Roark (*A Nascente*, Ayn Rand): criador vs. parasita, independência como necessidade básica de quem cria, crítica ao altruísmo como doutrina coercitiva |
| [[wiki/sources/useeffect-problemas-e-solucoes]] | Três anti-padrões de `useEffect`: estado derivado sincronizado via effects encadeados, stale closure em contadores, fetch sem AbortController — "o melhor effect é o que você deleta" |
| [[wiki/sources/contract-test-martin-fowler]] | Bliki de Fowler (2011): mantém testes contra um double + um segundo conjunto de contract tests que confere periodicamente se o double reflete o serviço real; recomenda SelfInitializingFake |
| [[wiki/sources/integration-test-martin-fowler]] | Martin Fowler desambigua "integration test": estreito (double + contract test, rápido) vs. amplo (serviços reais, lento); confusão irmã com unit test solitário/sociável |
| [[wiki/sources/test-double-martin-fowler]] | Fonte primária do termo "Test Double" (bliki, 2006): Dummy/Fake/Stub/Spy/Mock — taxonomia de Gerard Meszaros, relatada e divulgada por Fowler, não inventada por ele |
| [[wiki/sources/xunit-martin-fowler]] | Fonte primária da história do JUnit (bliki, 2006): do framework caseiro de Kent Beck em Smalltalk ao voo com Erich Gamma na OOPSLA 1997 até a proliferação de ports que virou a família "Xunit" |
| [[wiki/sources/consumer-driven-contracts-martin-fowler]] | Ian Robinson (2006), publicado no site de Fowler mas não escrito por ele: cunha Consumer-Driven Contracts — modelo de três camadas (Provider/Consumer/Consumer-Driven Contract) e o Must Ignore pattern de extensibilidade de schema |
| [[wiki/sources/gate-de-qualidade-definicoes-formais]] | Três definições formais de Quality Gate da literatura (checklist/aprovação por gate, milestone com critérios pré-definidos, ponto de verificação de Schneider) e suas características estruturais: critérios de entrada/saída, disparo por critério (não data), resultado binário, gates em paralelo |
| [[wiki/sources/quality-gate-ratchet-multiplos-agentes-ia]] | Quality gate com padrão ratchet (baseline congelada só pode melhorar/empatar) no projeto Strawberry; babysitting de PR pelo próprio agente de IA; pipeline de CI real (npm audit em dois níveis, jscpd para duplicação); comentários no código como contexto recuperável por agentes via grep |
| [[wiki/sources/uncle-bob-direito-de-nao-ler-codigo-agentes-ia]] | Uncle Bob não lê mais código de agentes: debate função-pequena vs. módulo-profundo com Ousterhout ganha dado empírico; grepability como razão real para quebrar funções; teto de ~1000 linhas por arquivo ligado ao tool call; harness (unit test, cobertura, mutation test, Gherkin, métrica) como o que sustenta não ler código |
| [[wiki/sources/quatro-tecnicas-ci-cd-gate-qualidade-codigo-ia-uncle-bob]] | Segundo vídeo de reação a Uncle Bob sobre não revisar código de agentes: quatro gates concretos de CI — complexidade ciclomática (CCN 1–20), cobertura + mutation testing com `mutmut` (400 mutações, 50 sobreviventes), limite de 300 linhas por arquivo, dependency structure analysis (import circular, camadas invertidas, módulo de API vs. implementação) |
| [[wiki/sources/ninguem-mais-revisa-codigo-ia-migracao-review-galego]] | Terceiro vídeo de reação a Uncle Bob (Augusto Galego): como *migrar* de "reviso 100%" para "não reviso" via matriz risco × dificuldade (merge automático / amostragem / revisão manual em pares); Boris (Claude Code) sobre `CLAUDE.md`/`review.md` como o novo trabalho; Quality Gate de Lucas Montano; ceticismo — nenhuma empresa multibilionária feita só com IA ainda |
| [[wiki/sources/iso-27001-dicionario-programador]] | SGSI organizado em torno da tríade CIA; Anexo A 2022 com 93 controles em 4 temas; controles A.8.28/A.5.15/A.5.8/A.8.25/A.5.3 relevantes para devs; Policy as Code (OPA/Gatekeeper) como implementação; ISO 42001 para governança de IA |
| [[wiki/sources/escalabilidade-horizontal-load-balancer-algoritmos]] | Tipos de load balancer (hardware/software/cloud), por que AWS/Azure separam LB de camada 4 e 7, e algoritmos de balanceamento (Round Robin, Weighted, Least Connections, Least Time, Sticky) com demo prática em Nginx |
| [[wiki/sources/reacao-artigo-visual-algoritmos-load-balancing]] | Simulação visual (bolinhas de requisição encolhendo) de Round Robin → fila → Weighted RR → Dynamic Weighted RR (peso por latência) → Least Connections → PEWMA; conclusão: sempre validar com benchmark da carga real |
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
| [[wiki/sources/golang-profissional-sem-grandes-frameworks]] | Lucas Badico: Go não é pra "código fofo" — sem framework dominante equivalente a Rails/Express, ~80% das dependências vêm da stdlib, e mesmo com generics a cultura prefere repetição estável a abstração grande e frágil |
| [[wiki/sources/hmac-integridade-mensagem-local-first-entrevista]] | Pergunta de entrevista de system design sobre integridade de mensagem: carrinho local-first sem storage no servidor — por que criptografar quebra a exibição, chave assimétrica é cara demais, e HMAC (ipad/opad derivados do mesmo segredo, duas etapas de hash) é a resposta certa contra ataque de extensão de mensagem |
| [[wiki/sources/mappers-conversao-entre-camadas]] | A mesma entidade (`Notification`) é representada de forma diferente em cada camada de uma arquitetura em camadas — mapper estático por camada (`PrismaNotificationMapper.toPrisma()`) converte entre formatos e isola o acoplamento à tecnologia, não ao domínio |
| [[wiki/sources/portas-de-rede-como-funcionam]] | Porta é um número virtual (0–65.535) que, com o IP, roteia dados ao serviço certo — faixas IANA (well-known, registered, dynamic), portas dinâmicas por conexão de saída, estados listening/established/closed, netstat na prática |
| [[wiki/sources/design-pattern-adapter]] | Renato Augusto: classe de negócio acoplada via `new` a uma lib externa de PDF (DomPDF) fere SRP e é intestável — Adapter extrai uma interface própria do domínio, e trocar de lib (DomPDF → TCPDF) passa a exigir só um novo adaptador |
| [[wiki/sources/observabilidade-ponta-a-ponta-opentelemetry-ia-amsterdam]] | Palestra em Amsterdã: OpenTelemetry como padrão vendor-neutral roteado por um Collector central; agente de IA via Grafana MCP correlaciona métricas/logs/traces sozinho e acha causa raiz em código — "o ouro está nos dados, não na IA" |
| [[wiki/sources/monitoramento-aplicacoes-ia-grafana-cloud-opentelemetry]] | Demo patrocinada do Grafana Cloud: assistente de IA embutido no chat web (sem custo de créditos do editor) correlaciona logs/métricas/traces de uma app de exemplo e acha um vazamento de conexão PostgreSQL na linha exata, oferecendo alerta, dashboard e PR de correção via GitHub |
| [[wiki/sources/o-que-e-refatoracao-quando-usar]] | Bernardo Lobato: refatoração é mudar estrutura interna sem alterar comportamento externo — dois chapéus de Kent Beck, God Class nascendo sprint a sprint sob prazo, testes na base da pirâmide como rede de segurança, passos pequenos, refatoração oportunista vs. planejada |
| [[wiki/sources/refatoracao-pragmatic-programmer-martin-fowler-2a-edicao]] | Motivos da 2ª edição de Refactoring 20 anos depois (Java datado → JS, locadora de vídeos → peças de teatro); analogia de jardinagem vs. construção civil; duas motivações de Fowler e seis situações do Pragmatic Programmer para refatorar |
| [[wiki/sources/rust-por-que-tanto-hype-ownership-borrowing-lifetimes]] | Ownership (um dono por valor), borrowing (`&`/`&mut` — N leitores OU 1 escritor) e lifetimes (referência nunca outlive o valor) eliminam use-after-free, double-free e data races em compile-time, sem GC — trade-off: aprendizado e compilação mais lentos |
| [[wiki/sources/ponteiros-cpp-go-csharp]] | Ponteiros em C++/Go/C#: mesma sintaxe (`&`/`*`) em C++ e Go, mas Go protege com escape analysis + GC e C# esconde tudo atrás de reference types; retornar endereço de variável local é undefined behavior em C++, resolvido automaticamente nas outras duas; RAII e `unique_ptr`/`std::move` eliminam a maior parte do `new`/`delete` manual em C++ moderno |
| [[wiki/sources/cognitive-debt-margaret-storey]] | Fonte primária de "cognitive debt": dívida técnica mora no código, dívida cognitiva mora na cabeça do time — fundamentada na teoria de Peter Naur (1985) de que um programa é uma teoria, não o código-fonte |
| [[wiki/sources/custo-real-ia-tokens-produtividade-demissoes]] | Episódio CDF Café: produtividade com IA é real mas custo sobe (caso Uber), Gartner projeta custo de codificação superando salário médio até 2028, 59% das empresas usam IA como bode expiatório para demissões, Meta admite erro de reestruturação, capital de tokens (Nadella) |
| [[wiki/sources/rfcs-grill-me-e-o-risco-da-preguica-no-vibe-coding]] | Episódio CDF Café: RFC como source of truth anti-alucinação (80/20 planejamento/execução), especificações agnósticas à linguagem (Fabrício Arcanjo), skill Grill Me (Matt Pocock) invertendo quem revisa quem, quality gates forçando modularização |
| [[wiki/sources/underengineering-overengineering-mario-souto]] | Mário Souto (DevSoutinho): under-engineering é mais comum que over-engineering — não reinventar libs maduras (React Hook Form, Tailwind), variável de ambiente em vez de hardcode na Vercel, acoplamento login/criar conta, CI mínimo de ~31 linhas (lint+teste) com branch protection |
| [[wiki/sources/sistema-produtividade-ia-adapta]] | Sistema pessoal de produtividade em 3 pilares (planejamento/priorização/execução): dump mental + regra dos 5 minutos, matriz de Eisenhower + tarefa principal do dia, execução via Adapta (skills de contexto pessoal + roteamento automático de modelo) |
| [[wiki/sources/deploy-blue-green-na-pratica-vps-nginx]] | Demo prática de blue/green numa VPS única: Nginx como reverse proxy trocando entre duas portas via script, sem Kubernetes; deploy 100% manual via SSH como etapa antes de automatizar |
| [[wiki/sources/application-boundary-martin-fowler]] | Martin Fowler (bliki, 2003): aplicações são construções sociais — devs, negócio e financiadores enxergam "unidade única" de formas diferentes; fronteiras são traçadas por política, não por critério técnico; contra a previsão de que SOA extinguiria aplicações
| [[wiki/sources/papinho-tech-solo-adaptabilidade]] | Vestimenta e comunicação são adaptação estratégica ao contexto, não perda de essência; recusa em se adaptar fecha portas; comunicação muda por nível hierárquico e por canal de conteúdo |
| [[wiki/sources/hermes-agent-open-claw-learning-loop]] | Hermes Agent (open source, MIT): closed-loop skill learning system de 5 etapas sobre memória em três camadas (sessão/persistente/skill) indexada via FTS5; gancho é o bug real de billing no Claude Max 20 disparado pela string "hermes" no Git history |
| [[wiki/sources/idempotencia-pagamentos-retry-sistemas-distribuidos]] | Timeout não distingue falha, processamento em andamento ou sucesso com resposta perdida; chave de idempotência nasce no cliente por intenção (não por conteúdo); corrida entre tentativas resolvida por INSERT atômico; idempotência ≠ transação (problemas complementares); Outbox/Inbox propaga a identidade entre fronteiras de serviço; identidades de negócio por produto (saque ID, emissão ID, crédito ID, client order ID) |
| [[wiki/sources/topicos-desenvolvimento-software-mudei-de-ideia-6-anos]] | Chris Kiehl, retrospectiva de 6 anos de carreira: tipagem estática ganha valor em time, arquitetura importa mais que quase tudo, "boas práticas" são contextuais, DRY é meio não fim, ordem de prioridade YAGNI/SOLID/DRY, entrevistas técnicas "completamente quebradas", monólitos bons na maioria dos casos |
| [[wiki/sources/por-que-letras-minusculas-economizam-dados]] | Lucas Montano: por que letras minúsculas comprimem melhor que maiúsculas — Huffman coding (árvore menor com menos variedade de caracteres) + LZSS/LZ77 (ponteiros para sequências repetidas) explicam o deflate/gzip; caso Hacker News (title case → sentence case) economiza 31 bytes/página; escovação de bits comparada a otimizar imagens/JS/cache, que economiza ordens de magnitude mais |
| [[wiki/sources/a-insanidade-de-ser-um-programador-hoje]] | Reação ao artigo de Vitor Sousa Pereira: Unix/`grep` nasceram como ferramenta privada de Ken Thompson depois compartilhada de graça; front-end/back-end como especialidades separadas é invenção de 2006-2007, não histórico; fullstack como corte de custo, não escolha técnica; curva de aprendizado descontínua (caso SMTP); área ficou mais complexa e menos especializada ao mesmo tempo |
| [[wiki/sources/system-design-por-nivel-junior-pleno-senior]] | Augusto Galego: entrevista de system design cobra compreensão do todo em todo nível, mas no trabalho real só sênior costuma precisar dela; júnior soluciona e demonstra fundação, pleno resolve com racional prático, sênior otimiza e lidera a conversa sobre CAP/sharding/cache/monolito-vs-microsserviços |
| [[wiki/sources/continuous-integration-delivery-deploy-vs-release]] | Os "dois CDs" (delivery vs. deployment) e deploy vs. release, com demo prática: GitHub Actions de 2 jobs (CI + deploy SSH para VPS), GitHub Secrets write-only, fluxo feature→dev/staging→main com clonagem anonimizada do banco para staging |
| [[wiki/sources/como-escolher-banco-de-dados-historia-acid-cap]] | TI das Antigas: história do modelo relacional (Codd, IBM 1970) até hoje; ACID e CAP como decisão de negócio, não hype; números reais de instância única (conexões, volume, latência) para MySQL, PostgreSQL, Oracle, SQL Server, SQLite, Redis e MongoDB, com guia direto por cenário |
| [[wiki/sources/sgbd-conceitos-fundamentais-questoes-concurso]] | Aula de concurso público: SGBD, SGBDR vs. SGBD NoSQL, visão (view), quatro modelos NoSQL (chave-valor, documento, colunas, grafos), ACID, Teorema CAP com classificação CA/CP/AP por produto, e bloco de questões reais de bancas (CESPE, NC-UFPR, KIAC, IBADE, AOCP) com gabaritos |
| [[wiki/sources/design-pattern-facade-renato-augusto]] | Renato Augusto: Facade via exemplo de e-commerce (OrderController → OrderFacade) — Controller não deve carregar fluxo/regra de negócio; defesa de que Facade não fere o SRP porque opera num nível de abstração diferente das classes que orquestra |
| [[wiki/sources/arquitetura-frontend-microfrontends-monolito-modular-vertical-slice]] | Cinco níveis de arquitetura frontend (camadas → modular → vertical slice → microfrontend baseado em rotas → microfrontends parciais distribuídos); demo prática Shell + React/Angular/Solid.js via Custom Events expõe o custo real de microfrontends parciais (performance, CI/CD fragmentado, versionamento, governança); tese central: a maioria das decisões saudáveis fica entre monolito modular e microfrontend baseado em rotas, não nos extremos |
| [[wiki/sources/microsservicos-martin-fowler-james-lewis]] | James Lewis e Martin Fowler (25 mar 2014): artigo original que cunhou a definição de microsserviços — nove características comuns, "smart endpoints and dumb pipes" contra ESBs, Lei de Conway como razão para decompor por capacidade de negócio, Polyglot Persistence, Design for Failure (Simian Army, Circuit Breaker); os próprios autores recusam declarar microsserviços "o futuro" sem ressalvas |
| [[wiki/sources/criptografia-cesar-vigenere-rsa-aes-hashing-quantica]] | Linha do tempo da criptografia — cítala espartana e cifra de César (criatividade, não matemática) → Vigenère (polialfabética, "indecifrável" por 300 anos) → Enigma (quebrada por reuso de chave) → AES/RSA modernos (key distribution problem resolvido por par público/privado) → IND-CPA como modelo formal (César falha, preserva padrão de repetição) → ameaça quântica (Shor quebra RSA, Grover só acelera busca) → password hashing (salt, pepper, BCrypt EKS-Blowfish limitado a 72 chars, Argon2id em três fases) |
| [[wiki/sources/story-points-po-forcando-30-40-pontos-por-sprint]] | Lucas Badico: pergunta de mentorado sobre PO exigindo 30-40 story points/sprint por pessoa vira discussão sobre o papel do Scrum Master e do PO — story points medem complexidade relativa (não tempo), forçar uma meta de cima para baixo corrompe a métrica (Lei de Goodhart), reduz colaboração e reproduz Waterfall com verniz de cerimônias ágeis |
| [[wiki/sources/tech-debt-guia-completo-gestao-metricas]] | Guia introdutório de dívida técnica: revisita Quadrante de Fowler e analogia com dívida financeira; acrescenta debt ratio/SQALE (`remediation/development cost`, faixas <5%/5-10%/10-20%/>20%), hotspot analysis (complexidade ciclomática × code churn), framework PAID, matriz refatorar-vs-reescrever (valor×risco), regra dos 20% vs. regra dos 25% do Shopify, TDD/pair programming/CI-CD como prevenção, template de business case para stakeholders, caso Knight Capital |
| [[wiki/sources/historia-dos-formatos-de-imagem]] | Cronologia dos formatos de imagem (TGA 1984 → PDF): canal alfa e RLE nos formatos raster antigos, JPEG (compressão com perdas em blocos 8x8) vs. PNG (sem perdas, criado como resposta livre-de-patente ao GIF), SVG como único formato vetorial, e WebP/HEIC/AVIF como geração mais recente — HEIC e AVIF reaproveitam literalmente codecs de vídeo (HEVC, AV1) para comprimir uma imagem única |
| [[wiki/sources/modelo-openai-escapa-sandbox-benchmark-cyberseguranca]] | Benchmark interno de cybersegurança da OpenAI (GPT 5.6 + modelos não públicos, guardrails removidos) explora zero-day no proxy de egress e escapa do sandbox de rede; invade servidor da Hugging Face via credencial vazada (~17.000 linhas de eventos); modelos com guardrail padrão se recusam a ajudar a investigar o próprio incidente, obrigando a hospedar o GLM 5.2 (Zhipu AI) internamente sem guardrails |
| [[wiki/sources/papinho-tech-solo-comunidade]] | Comunidade técnica como ciclo de recebimento e retribuição — quem foi ajudado por um meetup/palestra deve retribuir ajudando outra pessoa; caso de interiorização de tecnologia em São José do Alegre (MG) com o Instituto Aaron Schwartz; preguiça de sair de casa, não falta de eventos, é o maior obstáculo à participação |
| [[wiki/sources/porque-nunca-confiar-em-llm-alucinacao]] | Alucinação de LLM é fenômeno mensurável (94% humano vs 58% LLM em benchmark citado; melhor modelo errou 48%); paper da OpenAI aponta causa raiz — treinamento recompensa palpite em vez de reconhecer incerteza, precisão nunca chega a 100%; caso Air Canada como precedente de risco jurídico; 205 mil pacotes de código alucinados num corpus de 576 mil gerações; RAG e LLM-as-judge (faithfulness) reduzem mas não eliminam o problema |
| [[wiki/sources/devsecops-origem-cultura-manifesto]] | Origem do DevSecOps: cunhado pela Gartner em 2012, três anos após Patrick Debois formalizar o DevOps (2009, inspirado pela palestra da Flickr na Velocity); Manifesto DevSecOps propõe atacar o próprio produto como um invasor externo faria em vez de confiar só em scanners; shift-left testing mapeado por fase do ciclo (planejamento → build → deploy → operação); segurança como cultura de pessoas, não só ferramental |
| [[wiki/sources/system-design-entrevista-cinema-draw-io]] | Rocket City (João): entrevista de system design simulada ao vivo no draw.io para "reserva de ingressos de cinema" — follow-up questions, load balancer, MySQL vs. não-relacional, APIs externas de seatmap/pagamento, Redis com TTL como reserva de 15 min; autor expõe abertamente um bug de consistência não resolvido no próprio desenho |
| [[wiki/sources/injecao-sql-aula-modulo-seguranca]] | Aula prática (Express + `pg`, sem ORM) de SQL Injection ao vivo: bypass via `' OR '1'='1'` em query string e via `1 OR 1=1` em parâmetro de rota, retornando todos os usuários; correção via placeholders parametrizados (`$1`/`$2`); camada extra de validação de schema com Celebrate + Joi rejeitando o ataque antes da query rodar |
| [[wiki/sources/claude-tag-slack-terceiro-paradigma-llm]] | Lucas Montano (atribuição provável) reage ao Claude Tag (Claude no Slack) da Anthropic e à tese de Andrej Karpathy de "terceira reformulação da interface de LLM" (site → app → agente autônomo assíncrono organizacional); memória multiplayer por canal, modo ambient proativo; contraponto de Gergely Orosz — o breakthrough é integração confiável com sistemas internos, não a interface; Anthropic ultrapassa OpenAI no gasto em cartão corporativo em abril; alerta de vendor lock-in de memória organizacional |
| [[wiki/sources/arquitetura-frontend-dash-fornecedores-vs-microfrontends-super-roupas]] | Estudo de caso fictício "Super Roupas": 4 sistemas de fornecedor sem visibilidade unificada de status/atraso; solução "vendida" de microfrontends parciais unifica a experiência (sintoma errado, 3+ meses, alto atrito entre times); solução enxuta é dashboard read-only + BFF agregador (causa raiz, <2 meses, time de 4); eixo sênior (produto) vs. staff (vertical) e reflexão sobre "escalável para quê" |
| [[wiki/sources/tres-projetos-para-aprender-programar]] | Três projetos escolhidos pela habilidade que ensinam, não pelo portfólio: Snake (gerenciamento de estado), simulador de supermercado (modelagem de domínio) e Pathfinding (algoritmos como estratégia) — "software é argila, não Lego" |
| [[wiki/sources/gestao-de-custo-velocidade-modelos-de-ia-fable-sol]] | Fable (Anthropic) e Sol/GPT 5.6 (OpenAI) são os mais inteligentes no Artificial Analysis mas ~70× mais caros por tarefa que o DeepSeek V4; roteamento manual → skill/subagentes no Claude Code → Custom Router (Abacus.AI) como as três camadas de automação da escolha de modelo por inteligência/velocidade/custo |
| [[wiki/sources/palantir-ceo-token-tax-nvidia-scam-ia]] | Reação à entrevista de Alex Karp (CEO da Palantir) à CNBC sobre deal com a Nvidia que virou crítica ao modelo de cobrança por token da OpenAI/Anthropic — três argumentos (wealth tax, roubo de propriedade intelectual, preço deveria ser sobre valor); harness como multiplicador oculto de custo; quatro dicas de FinOps para IA |
| [[wiki/sources/marco-bruno-3-dicas-vaga-junior]] | Marco Bruno (Cohab Code): 3 dicas para conseguir a primeira vaga júnior — aplicar amplamente e investir em comunidade em vez de se autofiltrar, tratar toda entrevista como ensaio ("nunca aposte o que não pode perder"), e preparo mental para receber feedback sem se defender + persistência (perguntar quando tentar de novo) + transparência sobre prazos; observa vagas júnior exigindo pleno no mercado brasileiro |
| [[wiki/sources/large-scale-vs-complex-architecture]] | Large scale (capacidade/escala, dividir-para-conquistar, control plane) e complexidade (interdependência, legado poliglota tipo mainframe→AS/400→Linux→Windows) são eixos independentes; over-engineering vs. over-thinking como anti-patterns espelho; autor admite não ter métrica objetiva para "complexidade" |
| [[wiki/sources/10-conceitos-internos-frameworks-frontend]] | Short em português listando 10 mecanismos internos que React/Vue/Angular resolvem por baixo dos panos, em ordem decrescente: estado (prop drilling, derived state) → batching → tree shaking/code splitting → ciclo de vida → compilação → roteamento client-side (History API) → hydration/ilhas → reatividade (Virtual DOM vs. signals) → reconciliação (keys) → DOM; fecha com a tese de que frameworks existem para minimizar toques no DOM e aumentar produtividade |
| [[wiki/sources/ciclo-de-mudanca-de-arquitetura]] | Aula curta: ciclo operacional de uma mudança de arquitetura — avaliar 100% o AS-IS (tecnologia + regras de negócio) → desenhar o TO-BE → validar com POC testada na escala real esperada (não numa fração dela) → migrar em coexistência com o legado via padrões de transição → migração concluída vira o novo AS-IS, reiniciando o ciclo; tese central é que assertividade importa porque descobrir tarde que o caminho está errado é retrabalho caro |
| [[wiki/sources/escalabilidade-horizontal-vertical-custo-grafico]] | Aula curta e introdutória: diferença horizontal/vertical via analogias visuais (horizonte vs. imagem esticada) e exemplo gráfico de custo — horizontal permite adicionar exatamente a capacidade necessária (um servidor a mais), vertical em cloud providers costuma forçar dobrar o tier da instância, gerando capacidade ociosa; mais réplicas menores aumentam resiliência |
| [[wiki/sources/sre-sli-slo-sla]] | SRE trata confiabilidade como problema de engenharia: SLI mede, SLO define meta interna, SLA é contrato externo com margem de segurança, Error Budget governa velocidade vs. estabilidade; inclui alerting por burn rate e template de blameless post-mortem |
| [[wiki/sources/slo-sli-sla-exemplo-ecommerce]] | Aula curta e didática: a diferença entre SLO e SLA não está no número prometido, mas em quem são as partes do acordo — mesma promessa de disponibilidade é SLO entre times da mesma empresa e vira SLA quando o acordo cruza a fronteira entre empresas distintas, com consequência contratual |
| [[wiki/sources/recriando-zustand-javascript-puro-sem-provider]] | Transcrição de vídeo: recria o mecanismo central do Zustand (Observer + Map + useState/useEffect) em ~43 linhas de JS puro, sem Provider, demonstrado com color picker sincronizado em 3 pontos da árvore |
| [[wiki/sources/spec-driven-development-otimizando-contexto-agentes]] | RPI + Spec-Driven amarrados como resposta ao mesmo problema (janela ocupada = mais alucinação); breakdown de tasks executado com 4 subagentes em paralelo; artefato de "estado" pós-implementação para continuidade entre janelas |
| [[wiki/sources/tecnologias-hype-passado-soap-xml-esb-jquery-cobol]] | Bernardo Lobato: cinco tecnologias fora do mainstream de hype que ainda sustentam sistemas críticos — SOAP (WSDL, contratos rígidos, NF-e), XML (auge corporativo pré-JSON), ESB (barramento central pré-microsserviços, "Erroneous Spaghetti Box"), jQuery ("write less, do more", ainda mantido em 2026) e COBOL (1959, sistema financeiro mundial, Pix, padrão atualizado em 2023); tese central: o ciclo de hype da comunidade não acompanha o ritmo real de obsolescência |
| [[wiki/sources/rotacao-de-contas-free-tier-llm-router-hostinger]] | Vídeo "boteco de tecnologia": AI Gateway self-hosted ("Nine Router", nome não confirmado) via deploy de um clique na Hostinger — mapeia o modelo que o Claude Code "acha" que usa para qualquer outro provider (GLM, MiMo) e rotaciona múltiplas contas free tier quando uma esgota; teste ao vivo mostra "Token Saver" piorando consumo (705k → 2,2M tokens de input) num caso Ruby on Rails; autor reconhece risco de banimento por detecção de abuso em contas free tier |
| [[wiki/sources/15-dias-depois-lancar-sas-numeros-ataques-vulnerabilidades]] | Mano Davin, 15 dias após lançar o Find My SaaS: 12 mil usuários e 646 SaaS cadastrados via Google Analytics, R$ 4.819 de faturamento orgânico (boost pago, sem tráfego pago), 230 mil+ requisições numa VPS de 1 vCPU/4GB sem Kubernetes nem microsserviços, 157 tentativas maliciosas bloqueadas pelo Cloudflare, pentest voluntário encontra 12 vulnerabilidades incl. escopo OAuth aceito sem validação via URL; cronologicamente anterior ao incidente de SYN flood em [[wiki/sources/ddos-sim-flood-servidor-find-my-saas]] |

## Concepts

### Autenticação & Identidade

| Página | Hook |
|---|---|
| [[wiki/concepts/pkce]] | Client secret dinâmico e descartável para SPA/mobile — `code_verifier`/`code_challenge` via hash, resolve a falta de prova de posse do Implicit Flow, obrigatório no OAuth 2.1 |
| [[wiki/concepts/mfa-multifator-autenticacao]] | Três categorias de fator (sabe/tem/é) — dois fatores da mesma categoria não valem como MFA de verdade |
| [[wiki/concepts/otp-hotp-totp]] | Código de 6 dígitos a partir de seed + relógio ou contador — RSA SecurID proprietário até HOTP/TOTP padronizado pela IETF |
| [[wiki/concepts/webauthn-fido2-u2f]] | Criptografia assimétrica em vez de segredo compartilhado — chave privada nunca sai do dispositivo, phishing-resistant por design |
| [[wiki/concepts/jwt]] | Token stateless com header.payload.signature — Access Token curto + Refresh Token revogável resolve o dilema revogação vs. escala |
| [[wiki/concepts/oauth2]] | Framework de autorização (não autenticação) — delegação de acesso com escopo limitado sem compartilhar senha |
| [[wiki/concepts/openid-connect]] | Camada de autenticação sobre OAuth 2.0 — ID Token (JWT) verificável via JWKS, base do "Entrar com Google" |
| [[wiki/concepts/sso-single-sign-on]] | Autenticar uma vez num Identity Provider, todos os sistemas confiam — SAML legado vs. OIDC moderno |
| [[wiki/concepts/sessoes-http-cookies]] | Sessão stateful com armazenamento central (Redis) — dependência única que o JWT stateless elimina |
| [[wiki/concepts/session-fixation]] | Atacante planta um session ID conhecido antes do login; regenerar o ID pós-login é a defesa |
| [[wiki/concepts/open-redirect]] | Validação frouxa da `redirect_uri` no OAuth permite ao atacante desviar o `authorization_code` para domínio próprio |
| [[wiki/concepts/step-up-authentication]] | MFA só no login não protege ações sensíveis pós-sessão — reautenticar o segundo fator antes de ações de alto risco |

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
| [[wiki/concepts/atitude-mindset-vs-tech-skill]] | Potencial (aposta no futuro, onde atitude/mindset dominam) vs. performance atual (onde a tech skill pesa hoje) — e por que "20% melhor" é immensurável |
| [[wiki/concepts/mentalidade-de-dar-primeiro]] | Give-first: oferecer ajuda antes de precisar; o "efeito magnético" de os outros gostarem de trabalhar com você |
| [[wiki/concepts/efeito-multiplicador]] | Elevar 5 pessoas em 20% agrega 100% de valor vs. os 20% de melhorar só a si mesmo — com a ressalva do custo de tempo do lead |
| [[wiki/concepts/code-review]] | Regra de negócio antes de estilo — e por que o primeiro review de um júnior costuma vir cheio de comentários |
| [[wiki/concepts/matriz-risco-dificuldade-review-ia]] | Framework de transição para migrar de "reviso tudo" para "não reviso": classifica cada PR por risco × dificuldade e aplica merge automático (baixo risco, com teste), amostragem (risco médio) ou revisão manual em pares (alto risco: auth, pagamentos, migração de banco) |
| [[wiki/concepts/sindrome-do-impostor]] | Confundir "código reprovado" com "eu fui reprovado" — o gatilho mais comum no primeiro emprego |
| [[wiki/concepts/problema-de-escopo-aberto]] | Escopo fechado (jogo, objetivo + caminho previsível) vs. escopo aberto (vida real, sem limites definidos) — operacionalizar o problema em pedaços fechados e trocar foco de resultado por ação |
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
| [[wiki/concepts/seis-passos-mock-interview]] | Roteiro de dez etapas para transformar prática solo de LeetCode em simulação fiel de entrevista real — cronômetro, sem ler o enunciado, Big-O antes de codar |
| [[wiki/concepts/entrevista-system-design]] | Whiteboard interview: requisitos core antes de desenhar, plano de capacidade, modelagem de dados/API, e só então o high-level design |
| [[wiki/concepts/networking-de-carreira]] | Mercado invisível de indicações — quanto mais sênior o cargo, mais a vaga é preenchida por "você conhece alguém?" em vez de vaga aberta |
| [[wiki/concepts/comunidade-tecnica]] | Ciclo de recebimento e retribuição em meetups/eventos — quem foi ajudado deve retribuir, sob risco de o ciclo se fechar quando alguém "vira celebridade" e some dos eventos pequenos |
| [[wiki/concepts/credencialismo-formacao-formal]] | Diploma como proxy de disciplina, não de competência técnica — "tecnologia se ensina, disciplina não" |
| [[wiki/concepts/divisao-de-tarefas-em-partes-menores]] | Divida até responder "tenho segurança?" e "consigo dar prazo?" — pare quando não der mais para dividir entre duas pessoas |
| [[wiki/concepts/organizacao-pessoal-do-trabalho]] | Anotar em papel, listar subtarefas, riscar progresso — fecha os "loops abertos" que ficam martelando na cabeça |
| [[wiki/concepts/estimativa-como-habilidade-treinavel]] | Dar prazo mesmo sem pressão e comparar depois — treina o orçamento antes de precisar sob cobrança real |
| [[wiki/concepts/definicao-de-objetivo-antes-de-decisao]] | "Vale a pena" sem objetivo definido é como perguntar se um avião vale a pena sem saber o destino |
| [[wiki/concepts/nichos-frontend-automatizados-ia]] | Agência, freelancer de landing page e consultoria de CRUD foram os nichos de frontend mais comoditizados pela IA — arquitetura e observabilidade blindaram quem já operava nessa maturidade |
| [[wiki/concepts/nunca-aposte-o-que-nao-pode-perder]] | Ensaie entrevistas mesmo sem urgência real — sem medo de perder, só existe lado positivo: aprender ou conseguir a vaga |
| [[wiki/concepts/persistencia-em-processo-seletivo]] | Pergunte quando pode tentar de novo após reprovação — quem não persiste na entrevista dificilmente persiste nos problemas maiores do dia a dia |
| [[wiki/concepts/transparencia-sobre-prazos]] | Avisar e negociar atraso de teste técnico pesa mais na avaliação do que simplesmente atrasar sem avisar |
| [[wiki/concepts/vaga-junior-vira-pleno]] | Padrão observado no Brasil: vaga rotulada "júnior" exigindo nível pleno na prática — sem fronteira clara entre as duas categorias |
| [[wiki/concepts/monorepo-vs-microfrontends-ia]] | Monorepo junta contexto para o agente numa alteração vertical; microfrontends fragmentam a mesma mudança em várias tarefas cross-repo, exigindo linkar worktree/PR manualmente |
| [[wiki/concepts/side-project-como-armadilha]] | Side project popular vira manutenção obrigatória — pode ser mais maldição do que bênção sem cronograma dedicado |
| [[wiki/concepts/reinventar-a-roda]] | Reinventar raramente é inovação genuína — é remix, e o custo real está na manutenção extra desnecessária |
| [[wiki/concepts/cultura-do-trabalhador-esforcado]] | "Hard worker" como padrão mínimo obrigatório em vez de diferencial — esforço aparente mascarando entrega inconsistente |
| [[wiki/concepts/curva-de-aprendizado]] | Conhecimento não cresce linear com o que você consegue criar — cada objetivo esconde uma cadeia de pré-requisitos não óbvios (caso SMTP) |
| [[wiki/concepts/debugar-antes-de-perguntar]] | Buscar solução por conta própria antes de perguntar — quem só pergunta vira um "proxy super conectado", sem gerar raciocínio próprio |
| [[wiki/concepts/ler-codigo-de-terceiros]] | Ler código de outras pessoas ensina o que dificulta legibilidade e é fonte direta de aprendizado — "projeto funcionando é melhor que documentação" |
| [[wiki/concepts/medo-de-codigo]] | A sensação de que o código "julga" está inteiramente na cabeça — reformulação: é o código quem precisa de você, não o contrário |
| [[wiki/concepts/jogo-finito-vs-infinito]] | Carse/Sinek aplicado à carreira: intensidade é jogo finito (vencer um pico), disciplina é jogo infinito (continuar jogando) — programação é jogo infinito mesmo quando age como finito |
| [[wiki/concepts/codigo-para-o-futuro-eu]] | Código é escrito para o "eu atual" com todo contexto na cabeça, mas deveria ser escrito para o "eu futuro" que não vai lembrar de nada |
| [[wiki/concepts/estimativas-de-software]] | 5 razões comportamentais para subestimar tarefas (impressionar, esquecer que não é só código, falta de foco, achar todos iguais, pressão) — não é falta de técnica |
| [[wiki/concepts/visao-de-negocio-do-desenvolvedor]] | O "problema XY": perguntar como implementar X quando o problema real era Y — visão de negócio economiza tempo, evita complexidade e prioriza melhor |
| [[wiki/concepts/permanencia-vs-troca-de-emprego]] | Mario (troca a cada 6 meses, evita desconforto) vs. Sonic (busca desafio, aprofunda) — impacto de carreira de longo prazo exige tempo investido no mesmo lugar |
| [[wiki/concepts/controle-do-que-e-controlavel]] | Dicotomia estoica aplicada à carreira: pare de gastar energia em variáveis incontroláveis (economia, opinião alheia), foque nas controláveis (hábitos, tempo, dinheiro) |
| [[wiki/concepts/senior-vs-staff-visao-arquitetural]] | Sênior olha para o escopo do próprio produto, staff olha para a vertical inteira — armadilha comum aos dois: confundir solução mais complexa com solução mais madura |

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
| [[wiki/concepts/especialista-de-powerpoint]] | Quem nunca lançou nada dando conselho de escala e feature — filtrar feedback de quem não tem execução real por trás |

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
| [[wiki/concepts/determinismo-vs-probabilismo-em-ia]] | LLM tokeniza e responde por probabilidade, não lê linha a linha; tarefas que exigem mesmo output sempre (juros, impostos, folha) precisam de software determinístico, não julgamento de modelo |
| [[wiki/concepts/codigo-grepavel]] | Nomear funções para serem achadas por busca textual, não só lidas em sequência — a razão real por trás de -35% tokens ao quebrar código denso |
| [[wiki/concepts/complexidade-ciclomatica]] | CCN: conta caminhos de execução dentro de uma função; LLMs geram funções com muitos `if`s aninhados; gate de CI com limite bloqueante (ex.: 1–20), medido via SonarQube |
| [[wiki/concepts/codebase-legibilidade-ia]] | Código bom para humano é bom para IA; navigation paradox, teto prático de linhas por arquivo ligado ao tool call |
| [[wiki/concepts/navigation-paradox]] | Contexto maior não elimina navegação estrutural — desloca a falha de "não cabe" para "não foi notado"; DI containers como pior caso |

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
| [[wiki/concepts/paradoxo-da-aceleracao]] | Faros AI: velocidade individual sobe muito com IA, throughput do sistema quase não muda — o gargalo migra da escrita para a revisão (+91% no code review) |
| [[wiki/concepts/ia-como-amplificador]] | A IA amplifica o contexto e o critério existentes, sem julgamento próprio: júnior em tarefa simples +26–56%, sênior em legado zero/negativo |
| [[wiki/concepts/output-vs-outcome]] | Métricas de output (volume, PRs) são infladas pela IA independente de qualidade; só outcome (bug rate, ciclo de review) revela a verdade |

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
| [[wiki/concepts/dopamina-e-projetos]] | Antecipação da recompensa gera mais dopamina que a construção real — ciclo de iniciar projetos sem terminar nenhum |
| [[wiki/concepts/harness]] | Tudo ao redor do LLM: tool calls, contexto, memória, MCP, subagentes — o que dá ao modelo "olhos e mãos" |
| [[wiki/concepts/tool-call]] | Mecanismo (2023, OpenAI) que permite ao LLM requisitar execução de funções externas — game changer |
| [[wiki/concepts/ciclo-agente]] | Loop prompt → tool calls → contexto → resposta; 1 prompt pode gerar 40+ ciclos internos |
| [[wiki/concepts/degradacao-de-contexto]] | Qualidade cai após ~400k tokens; solução: auto-compact; nunca encher a janela por encher |
| [[wiki/concepts/reasoning-level]] | Low/Medium/High/Extra-High — controla tokens internos de raciocínio; extra-high ≠ sempre melhor |
| [[wiki/concepts/modelo-frontier]] | Modelos mais capazes: Opus 4.7, GPT-5.5, Gemini 3.1, Kimi K2.6, GLM 5.1 — tabela de preços 2026 |
| [[wiki/concepts/mixture-of-experts]] | Arquitetura MoE: por que modelos open source chineses são 10x mais baratos que frontier densos |
| [[wiki/concepts/token-maxing]] | Consumo compulsivo de tokens como sinal de produtividade — fenômeno do Vale do Silício, 2026 |
| [[wiki/concepts/loop-engineering]] | Degrau seguinte a harness engineering: desenhar o ciclo completo como estrutura repetível, disparável por prompt, schedule ou evento |
| [[wiki/concepts/ralph-loop]] | Loop agêntico de uma linha de bash (Geoffrey Huntley, 2025), batizado por Ralph Wiggum — deliberadamente simples, precursor histórico do guia oficial de loop da Anthropic |
| [[wiki/concepts/planner-executor-critic]] | Planner gera prompt+rúbrica para subagentes; Critic (modelo distinto do executor) aprova ou devolve follow-up |
| [[wiki/concepts/rubrica-de-verificacao]] | Critérios explícitos de aceite gerados junto com o prompt — contrato entre Planner e Verificador |
| [[wiki/concepts/langgraph]] | Framework que representa estado de agente como grafo — nodes são passos, edges são transições condicionais |
| [[wiki/concepts/grafo-como-abstracao-de-agentes]] | G=(V,E): nós são computação/LLM, arestas são condição de fluxo determinística — abstração independente de framework |
| [[wiki/concepts/roteamento-automatico-de-modelo]] | Camada que escolhe automaticamente qual LLM responde cada prompt (complexity/cascade/intent-based) — caso comercial: Adapta ONE |
| [[wiki/concepts/kv-cache]] | Cache de chaves/valores de atenção — evita reprocessar contexto a cada token; Kimi K3 promete até 75% de economia |
| [[wiki/concepts/export-controls-chips-ia]] | Sanções de exportação de chips NVIDIA para a China — pressão de fundo por trás de inovação arquitetural em MoE/KV Cache |
| [[wiki/concepts/corrida-preco-qualidade-llm]] | Concorrência entre frontier fechado e open source empurra preço para baixo e qualidade para cima simultaneamente |
| [[wiki/concepts/camada-de-aplicacao-vs-modelo]] | Com modelos cada vez mais equivalentes, a vantagem competitiva migra do modelo para a camada de aplicação |
| [[wiki/concepts/agent-memory-tres-camadas]] | Memória de sessão + persistente (`memory.md`) + skill, indexada via FTS5 do SQLite — padrão comum a orquestradores de agente, não exclusivo de um projeto |
| [[wiki/concepts/closed-loop-skill-learning]] | Loop de 5 etapas (task completion → pattern extraction → skill creation → refinement → periodic audit) que gera e refina skills automaticamente a partir do histórico de tarefas |
| [[wiki/concepts/paradigmas-interface-llm]] | Karpathy: três reformulações de interface de LLM — site → app local → entidade autônoma, persistente e assíncrona a serviço de toda a organização (Claude Tag) |
| [[wiki/concepts/lock-in-vendor-ia]] | Meses de memória organizacional acumulada num agente de fornecedor único (ex.: Claude Tag) tornam a migração cara — mitigação sugerida: paralelo de engenharia própria |
| [[wiki/concepts/autonomy-slider]] | Karpathy: controle deslizante contínuo (volume de rádio) do quanto de autonomia se delega a um agente — do "só sugestão" ao "faz o que você quiser" |
| [[wiki/concepts/escolas-de-programacao-com-ia]] | Taxonomia de 5 posições sobre programar com IA (copiloto, delegação total/spec-driven, "na unha", loop); DHH e Antirez migraram de "na unha" para delegação em <12 meses |
| [[wiki/concepts/ai-gateway-llm-router]] | Proxy self-hosted que expõe API compatível com Anthropic/OpenAI para redirecionar chamadas a qualquer provider real por trás — drop-in replacement via troca de `base_url` |
| [[wiki/concepts/rotacao-de-contas-free-tier]] | Cadastrar múltiplas contas free tier do mesmo provider e rotacionar entre elas via gateway quando uma esgota a cota — eixo de credencial, não de qualidade de modelo; risco de banimento por detecção de abuso |

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
| [[wiki/concepts/rewind-checkpoints-claude-code]] | Checkpoints e `rewind` no Claude Code — voltar a um ponto anterior da conversa sem depender só de commits Git |
| [[wiki/concepts/gerenciamento-de-sessoes-claude-code]] | Renomear/retomar sessões locais do Claude Code; `/go` para objetivos verificáveis de longo prazo; retenção de 30 dias |
| [[wiki/concepts/modelo-por-leverage-tarefa]] | Modelo mais forte para planejamento/arquitetura, mais leve para execução rotineira — alocação por alavancagem da tarefa |
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
| [[wiki/concepts/investigacao-de-incidentes-com-ia-e-mcp]] | Agente com Grafana MCP correlaciona métricas/logs/traces sozinho e acha causa raiz em código — semanas de investigação viram minutos, mas só se os dados já existirem; guardrails podem recusar investigar um ataque real por não distinguir defesa de ofensa |
| [[wiki/concepts/cli-vs-mcp]] | CLI usa treinamento da LLM e economiza contexto; MCP expõe tools delimitadas — critério de decisão |
| [[wiki/concepts/tech-spec]] | Segundo artefato do SDD: traduz o PRD em decisões técnicas (contratos, schemas, arquitetura) |
| [[wiki/concepts/human-in-the-loop]] | HITL em três granularidades: por tool call, por plan, por etapa SDD — Plan Mode é a forma leve |
| [[wiki/concepts/task-looper]] | Executor automático de tarefas SDD — itera pela lista aprovada com critérios de aceite, sem intervenção |
| [[wiki/concepts/agente-prd]] | Agente interativo que refina requisitos com perguntas e gera o PRD para consumo do agente de Tech Spec |
| [[wiki/concepts/degradacao-de-seguranca-iterativa-ia]] | Refinar código com IA repetidamente piora a segurança, não melhora — +37,6% de vulnerabilidades críticas após 5 rodadas, mesmo pedindo foco em segurança no prompt |

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
| [[wiki/concepts/j-space-interpretabilidade]] | Espaço interno de ativações do Claude vinculável a palavras nunca verbalizadas no output, lido via Jacobian Lens (Anthropic) — distinto de chain-of-thought, que é texto observável |
| [[wiki/concepts/alucinacao-llm]] | LLM inventa fatos, código e referências com confiança — causa raiz (OpenAI): treinamento recompensa palpite sobre reconhecimento de incerteza; RAG e LLM-as-judge (faithfulness) mitigam mas nunca eliminam; risco jurídico real (caso Air Canada) |

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
| [[wiki/concepts/sistema-binario-bit-byte]] | Bit (binary digit, 2 estados via transistor) → byte (8 bits, um caractere) → palavra → documento; toda informação é binária |
| [[wiki/concepts/maquina-de-turing]] | Fita infinita + cabeça de leitura/escrita + tabela de transição (Turing, 1936) — o modelo que define o que é computável |
| [[wiki/concepts/determinismo-vs-nao-determinismo]] | Uma ação por (estado, símbolo) vs. várias — a distinção que origina P vs NP; associação com quântico é simplificação, não equivalência |
| [[wiki/concepts/complexidade-computacional]] | Eficiência de algoritmos em tempo e espaço (finitos) — Big O como comportamento assintótico; base da segurança criptográfica |
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
| [[wiki/concepts/ponteiros-cpp-stack-heap-raii]] | Ponteiro é variável que guarda um endereço — stack vs. heap muda quem libera; retornar endereço de variável local é undefined behavior em C++, mas escape analysis (Go) e reference types em heap (C#) tornam o mesmo código seguro; RAII/`unique_ptr` como solução de C++ moderno |
| [[wiki/concepts/gramatica-formal-ebnf]] | EBNF define o que é sintaticamente válido; precedência e associatividade resolvem ambiguidade (`1 + 2 * 3`) |
| [[wiki/concepts/language-server-protocol]] | Protocolo da Microsoft que desacopla editor de linguagem — um servidor, N editores com autocomplete e erros inline |
| [[wiki/concepts/standard-library-e-ecossistema]] | Stdlib, package manager e tooling — o que faz uma linguagem tecnicamente boa sobreviver de fato |
| [[wiki/concepts/compactacao-de-texto]] | Huffman coding (código curto para caractere frequente, árvore encolhe com menos variedade de caixa) + LZSS/LZ77 (ponteiro para sequência repetida) = deflate/gzip; por isso maiúsculas custam mais depois de compactar mesmo custando o mesmo antes |

### Formatos de Imagem & Compressão

| Página | Hook |
|---|---|
| [[wiki/concepts/compressao-com-perdas-vs-sem-perdas]] | JPEG descarta informação de propósito (DCT em blocos 8x8 + quantização), PNG não descarta nada — a escolha é fidelidade vs. tamanho, não "qual é melhor" |
| [[wiki/concepts/formato-jpeg]] | Compressão com perdas em blocos 8x8 — resalvar o mesmo arquivo repetidamente degrada a imagem de forma cumulativa |
| [[wiki/concepts/formato-png]] | Nasceu como resposta livre-de-patente ao licenciamento cobrado sobre o LZW do GIF — compressão sem perdas + transparência verdadeira |
| [[wiki/concepts/formato-gif]] | Paleta de 256 cores, LZW patenteado — o formato cuja cobrança de royalties gerou o PNG |
| [[wiki/concepts/formato-svg]] | Único formato vetorial da lista — armazena instruções matemáticas, não pixels, por isso escala infinitamente sem perder nitidez |
| [[wiki/concepts/formato-webp]] | Google (2010) unificou JPEG+PNG+GIF num único contêiner — 20-30% menor com qualidade comparável |
| [[wiki/concepts/formato-heic-avif]] | HEIC e AVIF não inventam compressão própria — reaproveitam codecs de vídeo (HEVC, AV1) para comprimir um frame único |
| [[wiki/concepts/formato-raw-fotografia]] | RAW não é imagem pronta — é o dado bruto do sensor antes de qualquer processamento; TIFF é o irmão "revelado" de fidelidade total |
| [[wiki/concepts/exif-metadados]] | Metadados embutidos em JPEG podem incluir coordenadas GPS da foto — privacidade vaza sem que o usuário perceba |

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
| [[wiki/concepts/bucket-sort]] | Ordenar sem comparar: distribuir elementos em "baldes" indexados por um valor com teto conhecido (ex.: frequência ≤ n) — O(n) em vez de O(n log n) |
| [[wiki/concepts/two-pointer]] | Dois índices móveis sobre a mesma estrutura em vez de recriar sub-arrays a cada chamada recursiva — implementação real de binary search |
| [[wiki/concepts/algoritmos-de-grafo]] | DFS, BFS, Dijkstra e A* — do backtrack ingênuo ao roteamento com heurística do Google Maps |
| [[wiki/concepts/repertorio]] | Acúmulo de experiência prática que gera reconhecimento de padrões e intuição — o terceiro pilar da competência |
| [[wiki/concepts/string]] | Slice de bytes + charset + encoding — imutável porque alterar bytes quebra UTF-8 silenciosamente |
| [[wiki/concepts/charset]] | Mapeamento valor numérico → caractere; distinto de encoding (que é o algoritmo de serialização) |
| [[wiki/concepts/ascii]] | 128 caracteres em 7 bits; charset e encoding ao mesmo tempo; subconjunto de UTF-8 |
| [[wiki/concepts/unicode]] | Charset universal com >1M codepoints; não é encoding — precisa de UTF-8 para ser serializado |
| [[wiki/concepts/iso-8859-1-latin-1]] | Charset regional de 8 bits (0–255), idêntico a ASCII até 127, acrescenta acentos — usado no Brasil antes do Unicode dominar |
| [[wiki/concepts/utf-8]] | Encoding de largura variável para Unicode; criado por Ken Thompson e Rob Pike; padrão da web |
| [[wiki/concepts/bitwise-operations]] | AND extrai/zera bits, OR mescla, left shift abre espaço — o trio por trás de todo parsing binário |
| [[wiki/concepts/overlong-encoding]] | Codificar UTF-8 com mais bytes do que o mínimo necessário — sintaticamente válido, mas proibido pelo padrão |

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
| [[wiki/concepts/dificuldade-desejavel]] | Atrito e esforço calibrados criam conexões neurais duráveis (Bjork) — removê-los remove o aprendizado; a lente que separa uso bom e ruim de IA |
| [[wiki/concepts/atrofia-cognitiva]] | Delegar toda dificuldade à IA enfraquece raciocínio e pensamento crítico — reversível se há base, ausência de base se não há |
| [[wiki/concepts/active-recall]] | Recuperação ativa (testing effect): puxar a resposta da memória, não reconsumir — IA gerando questionários que expõem gaps |
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
| [[wiki/concepts/projetos-fundamentais-para-aprender-a-programar]] | Snake ensina estado, supermercado ensina modelagem, Pathfinding ensina algoritmos — três projetos, três habilidades ortogonais |

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
| [[wiki/concepts/single-point-of-failure]] | Componente cuja falha derruba o sistema inteiro — o fio condutor por trás de toda redundância (múltiplos servidores, réplicas, LB em par) |
| [[wiki/concepts/escalabilidade-vertical]] | Scale up — simples mas com teto físico e single point of failure |
| [[wiki/concepts/escalabilidade-horizontal]] | Scale out — sem teto teórico, requer stateless e load balancer |
| [[wiki/concepts/stateless]] | Servidor sem estado — pré-requisito da escalabilidade horizontal |
| [[wiki/concepts/sticky-session]] | Afinidade de sessão — solução paliativa que adia o problema real |
| [[wiki/concepts/cdn]] | Rede de edge servers geográficos — cache global da camada web |
| [[wiki/concepts/auto-scaling]] | Adição/remoção automática de instâncias por regras de métricas |
| [[wiki/concepts/sharding]] | Divisão de banco em múltiplos shards — escala writes e armazenamento |
| [[wiki/concepts/consistent-hashing]] | Anel virtual de shards — minimiza dados movidos ao adicionar/remover nós, evitando o rebalanceamento total do hash-based sharding simples |
| [[wiki/concepts/replicacao-de-banco]] | Cópias do banco para leitura — escala reads e aumenta disponibilidade |
| [[wiki/concepts/gargalo]] | Ponto mais lento da cadeia — identificar antes de escalar qualquer coisa |
| [[wiki/concepts/cap-theorem]] | Consistência vs Disponibilidade vs Partição — o trade-off central de sistemas distribuídos |
| [[wiki/concepts/simulador-de-system-design]] | Playground que roda tráfego simulado sobre o diagrama e pontua o desenho com IA — não é só desenhar, é testar |
| [[wiki/concepts/niveis-de-senioridade-system-design]] | Júnior soluciona e demonstra fundação, pleno resolve com racional prático, sênior otimiza e lidera a conversa — entrevista cobra o todo em qualquer nível, trabalho real só exige isso a partir de sênior |
| [[wiki/concepts/latencia-streaming-ao-vivo]] | Delay entre captura e exibição em live streaming — buffer de leitura antecipada como principal causador; TV aberta (radiodifusão, sem sessão individual) tem latência estruturalmente menor que streaming via internet |
| [[wiki/concepts/large-scale-architecture]] | Escala e complexidade são eixos independentes de uma arquitetura — large scale foca em capacidade/dividir-para-conquistar, não necessariamente em interdependência |
| [[wiki/concepts/arquitetura-complexa]] | Interdependência e poliglotismo, típico de legado enterprise que convive com o passado (mainframe → AS/400 → Linux → Windows) — sem métrica objetiva de classificação |
| [[wiki/concepts/planejamento-de-capacidade]] | Estimar recursos futuros a partir dos dados da observabilidade — inclui o contra-intuitivo "gastar mais para perder menos" e disponibilidade como capacidade de recurso, não só uptime |

### AWS & Cloud

| Página | Hook |
|---|---|
| [[wiki/concepts/ec2]] | Building block básico de compute da AWS — paga por tempo de máquina alocada, não por computação realizada |
| [[wiki/concepts/amazon-s3]] | Object storage barato e quase ilimitado em volume, mas caro se acessado com muita frequência — não é banco de dados |
| [[wiki/concepts/ecs]] | Orquestração de containers/EC2 em cluster — simplifica escalar por demanda, mas escala custo junto |
| [[wiki/concepts/aws-fargate]] | Containers serverless — sem gerenciar EC2 diretamente, custo escala com uso mas pode ficar caro por workload |
| [[wiki/concepts/elastic-beanstalk]] | PaaS da AWS — configuração mais simples e custo mais atrativo que ECS manual para apps web simples, lock-in forte |
| [[wiki/concepts/aws-lambda]] | Menor unidade serverless — paga pelo tempo total de execução, incluindo espera ociosa por I/O, não só CPU |
| [[wiki/concepts/step-functions]] | Coordenação de workflow como máquina de estados — maior vendor lock-in entre os serviços do toolkit essencial |
| [[wiki/concepts/rds]] | Banco relacional gerenciado da AWS — só SQL, não cobre NoSQL |
| [[wiki/concepts/dynamodb]] | NoSQL key-value da AWS — hash key + sort key, latência muito baixa, Global Tables para escala mundial |
| [[wiki/concepts/vendor-lock-in-cloud]] | Quanto mais serviços proprietários de um provedor um sistema usa, mais caro migrar depois — gradiente de EC2 (baixo) a Step Functions (extremo) |
| [[wiki/concepts/infraestrutura-como-codigo]] | Tratar infra como código versionado/revisável em vez de clicar no console — versionamento, revisão, replicabilidade, automação |
| [[wiki/concepts/aws-cdk]] | TypeScript (ou outra linguagem geral) que sintetiza para CloudFormation — permite lógica condicional real na definição de infra |
| [[wiki/concepts/aws-cloudformation]] | Formato declarativo nativo AWS (YAML/JSON) agrupado em "stack" — artefato de fato aplicado por trás do CDK |

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
| [[wiki/concepts/tolerancia-a-falha]] | Topologia ativo-ativo — nós idênticos já servindo tráfego em paralelo, sem janela de failover perceptível; mais forte e mais cara que HA (ativo-passivo) |
| [[wiki/concepts/observabilidade]] | Entender o que acontece por dentro via logs (o quê), métricas (crescendo?) e traces (onde o tempo foi gasto) |
| [[wiki/concepts/sli]] | A métrica concreta (0–1 ou %) que mede qualidade do serviço — entrada do SLO |
| [[wiki/concepts/slo]] | Meta interna de confiabilidade sobre o SLI — fonte da verdade para decisões operacionais, não o SLA |
| [[wiki/concepts/sla]] | Contrato externo com penalidade — mesma promessa do SLO, mas entre empresas distintas, com consequência contratual |
| [[wiki/concepts/rto]] | Tempo de recuperação após desastre — imposto pela arquitetura escolhida, deve ser confrontado com custo de downtime do negócio |
| [[wiki/concepts/rpo]] | Dado tolerável de perda, medido pela distância até o último backup válido — tolerância varia radicalmente por domínio (financeiro vs. e-commerce vs. catálogo) |

### Idempotência & Deduplicação de Requests

| Página | Hook |
|---|---|
| [[wiki/concepts/idempotencia]] | Mesmo resultado não importa quantas vezes a operação executa — pré-requisito para retry seguro; chave gerada pelo servidor (hash dos campos) é mais robusta contra abuso que chave enviada pelo cliente; corrida entre tentativas concorrentes resolvida por INSERT atômico, não SELECT+INSERT |
| [[wiki/concepts/post-redirect-get]] | Redirect 303 após POST evita reenvio acidental de formulário — não protege contra reenvio via script, só via navegador |
| [[wiki/concepts/inbox-pattern]] | Complementar ao Outbox do lado de quem consome — tabela `inbox_events` com unique constraint por `provedor + event_id` impede reaplicar o efeito de um webhook ou evento reentregue |

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
| [[wiki/concepts/coolify]] | PaaS self-hosted sobre Docker/Traefik — auto-update semanal do proxy é conveniente até uma versão bugada derrubar tudo sozinha |

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
| [[wiki/concepts/cache-vs-buffer]] | Cache (reutilização, olha pro passado) vs. buffer (diferença de velocidade produtor/consumidor, olha pro presente) — mesma implementação, motivos opostos; buffer pool é cache apesar do nome |
| [[wiki/concepts/buffer]] | Área temporária que absorve diferença de velocidade produtor/consumidor — I/O de hardware, filas de mensagem, buffer de streaming; dado é descartado após consumo, não reutilizado |
| [[wiki/concepts/cache-aside]] | Lazy Loading: tenta cache, em miss vai ao banco com TTL — análogo ao padrão Flyweight |
| [[wiki/concepts/feature-flag]] | Interruptores de funcionalidade em runtime — Redis é ideal pela latência mínima no fluxo de execução |
| [[wiki/concepts/banco-in-memory]] | Armazenamento primário em RAM — Redis, persistência RDB/AOF opcional |
| [[wiki/concepts/escalabilidade-horizontal]] | Mais máquinas ao invés de mais recursos na mesma — NoSQL e Redis cluster como caso principal |
| [[wiki/concepts/tradeoff-de-cache]] | Cache sempre adiciona complexidade — invalidação, sincronismo e consistência eventual como custos |

### Bancos de Dados & SQL

| Página | Hook |
|---|---|
| [[wiki/concepts/orm]] | ORM não elimina SQL, gera SQL por baixo dos panos — abstração, não substituição |
| [[wiki/concepts/database-migration]] | Migrate up/down versionado sequencialmente — via SQL cru ou derivado do estado final do schema por uma ORM |
| [[wiki/concepts/drizzle-orm]] | ORM mínima TypeScript próxima de SQL puro — schema declarado gera migration automaticamente via `drizzle-kit generate`; relational queries (`with:`) inspiradas em GraphQL |
| [[wiki/concepts/n-plus-one]] | 1 query para uma lista + N queries adicionais, uma por item — entre backend↔banco (lazy loading de ORM) e entre frontend↔backend (via API); mesma solução: JOIN/prefetch ou pedir a estrutura de uma vez |
| [[wiki/concepts/domain-specific-language]] | DSL para banco de dados quase sempre é wrapper em cima de SQL; Datalog do Datomic é a exceção real |
| [[wiki/concepts/mysql]] | InnoDB, gap locking, estoque como linhas físicas vs coluna numérica, diagnóstico por tempo de conexão segurada |
| [[wiki/concepts/skip-locked]] | `SELECT FOR UPDATE SKIP LOCKED` — fila de jobs e reserva de estoque de alta concorrência sem broker externo |
| [[wiki/concepts/grande-rollback]] | Tendência de empresas em escala abandonando Redis/brokers por primitivas do banco relacional — Shopify e 37signals |
| [[wiki/concepts/solid-queue]] | Fila de background jobs da 37signals 100% sobre banco relacional, sem Redis nem Kafka |
| [[wiki/concepts/acid]] | Atomicidade, Consistência, Isolamento, Durabilidade — garantias fortes dos bancos relacionais |
| [[wiki/concepts/base-basically-available-soft-state-eventual]] | O contraponto de ACID — disponibilidade e escala em troca de consistência eventual |
| [[wiki/concepts/relational-vs-nosql]] | Não existe escolha universal; trade-offs de consistência, queries, escala e schema por tipo de banco |
| [[wiki/concepts/database-transactions]] | Mecanismo que garante atomicidade — `$transaction` como invocação do contrato ACID |
| [[wiki/concepts/database-index]] | Estrutura (B-tree/hash/GIN/espacial) que acelera queries e garante unicidade ao custo de overhead em escritas |
| [[wiki/concepts/consistency-models]] | Espectro de Linearizability a Eventual Consistency — o que um cliente pode observar após uma escrita |
| [[wiki/concepts/stored-procedure]] | Lógica armazenada e executada no banco — mover regra de negócio pra lá compensa em agregação de grande volume, mas com moderação |
| [[wiki/concepts/materialized-view]] | View com resultado persistido em disco — meio-termo entre SQL cru repetido e stored procedure |
| [[wiki/concepts/postgresql]] | Processo por conexão (não thread) + PgBouncer obrigatório; até 50% mais rápido que MySQL em cargas analíticas |
| [[wiki/concepts/oracle-database]] | RAC multiplica sessões horizontalmente; Flashback Query, licenciamento por núcleo custa milhões/ano |
| [[wiki/concepts/sql-server]] | Escolha operacional (não técnica) quando a empresa já vive no ecossistema Windows/.NET/Power BI |
| [[wiki/concepts/sqlite]] | Biblioteca embarcada, arquivo único, lock global de escrita — não substituto de banco cliente-servidor |
| [[wiki/concepts/mongodb]] | Documento BSON sem esquema fixo; sem JOIN nativo; complementa o relacional, não substitui |
| [[wiki/concepts/full-text-search]] | Índice invertido dedicado (`FULLTEXT`/`MATCH AGAINST` no MySQL, `tsvector`/`GIN` no Postgres) — resolve relevância e performance onde `LIKE '%termo%'` falha nos dois eixos |
| [[wiki/concepts/indice-invertido]] | Palavra → lista de IDs onde ela ocorre; estrutura por baixo de todo Full-Text Search, de `FULLTEXT INDEX` a Lucene |
| [[wiki/concepts/like-wildcard]] | `LIKE '%termo%'` — antipattern de busca: substring de caracteres em vez de palavra, e full table scan em vez de índice |
| [[wiki/concepts/buffer-pool]] | Cache de páginas em memória do banco — buffer hit/miss e dirty pages que aguardam persistência assíncrona |
| [[wiki/concepts/write-ahead-log]] | WAL: log escrito antes da página final — commit responde assim que o log é gravado, não quando o disco é atualizado |
| [[wiki/concepts/mvcc]] | Múltiplas versões de uma linha em paralelo — leitura e escrita concorrentes sem lock mútuo |
| [[wiki/concepts/isolation-levels]] | Read Committed vs. Repeatable Read vs. Serializable — qual versão dos dados uma transação enxerga |
| [[wiki/concepts/database-recovery]] | Checkpoint limita o WAL a reler; recovery reaplica confirmadas e descarta incompletas após uma queda |

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
| [[wiki/concepts/api-gateway]] | Ponto único de entrada externo — roteamento, auth de borda, mapeamento de payload entre protocolos; single point of failure por natureza, mitigado com escala horizontal e observabilidade |
| [[wiki/concepts/bff-pattern]] | API Gateway especializado por tipo de cliente — resolve over-fetching/under-fetching agregando dados exatamente no formato que aquele frontend precisa |
| [[wiki/concepts/api-composition]] | API Composer orquestra múltiplas chamadas em paralelo (fan-out) e devolve um único resultado lapidado — técnica central por trás de BFFs e agregação de endpoints |
| [[wiki/concepts/graphql]] | Cliente pede a estrutura de dados exata que quer numa única query — criado pela Meta para resolver N+1/over-under-fetching entre múltiplos frontends; sempre POST por limite de tamanho de URL |
| [[wiki/concepts/microsservicos]] | Decomposição por bounded context, não por camada técnica; monolito modular é o ponto de partida correto para ~90% dos casos; estudar o estilo funciona como eixo de aprendizado que amarra circuit breaker, saga, observabilidade e mensageria |
| [[wiki/concepts/monolito-modular]] | Um artefato/banco/runtime dividido em módulos de fronteira explícita que se comunicam por contratos (Ports & Adapters), não por chamadas de função — captura o isolamento dos microsserviços sem o custo de rede; etapa entre MVP e empresa madura que facilita a extração tardia |
| [[wiki/concepts/arquitetura-de-sacrificio]] | Escolher *deliberadamente* uma arquitetura que você vai descartar quando o produto crescer (Fowler): descartar código não é fracasso; priorize flexibilidade cedo, preserve qualidade interna/modularidade, prefira monolito a microsserviços como sacrifício e deixe quem escreveu decidir a hora de sacrificar |
| [[wiki/concepts/monolito]] | Aplicação de artefato único, deploy único — simples e suficiente para MVPs (e muito além), mas degenera em código espaguete sem disciplina de fronteiras |
| [[wiki/concepts/code-espaguete]] | Código acoplado em cadeia sem fronteiras claras; microsserviços o impedem por impossibilidade estrutural, monolito modular por contratos entre módulos |
| [[wiki/concepts/separation-of-concerns]] | Cada parte cuida de uma responsabilidade distinta com interação explícita — o que os contratos entre módulos garantem |
| [[wiki/concepts/encapsulamento]] | Esconder internals e expor só uma interface controlada (analogia getters/setters) — como um módulo do monolito modular se protege |
| [[wiki/concepts/database-per-service]] | Banco isolado por microsserviço resolve deadlock de banco compartilhado, mas cria problema de atomicidade entre serviços — motiva 2PC/Saga |
| [[wiki/concepts/event-driven-architecture]] | Comunicação via eventos publicados/reagidos em vez de chamadas síncronas — base do Saga coreografado e da propagação write→read em CQRS |
| [[wiki/concepts/soap]] | Protocolo XML de 1998 com contrato rígido via WSDL; sobrevive em bancos, seguradoras e NF-e mesmo após REST+JSON dominar APIs novas |
| [[wiki/concepts/xml-extensible-markup-language]] | Formato de dados estruturado de 1998, espinha dorsal da tecnologia corporativa pré-JSON; ainda essencial em Office, Java, config e NF-e |
| [[wiki/concepts/esb-enterprise-service-bus]] | Barramento central de integração pré-microsserviços — "smart endpoints, dumb pipes" nasceu como reação a ele; ainda essencial em empresas com grande legado |
| [[wiki/concepts/jquery]] | Biblioteca JS de 2006 que unificou DOM/eventos entre navegadores; raramente escolhida hoje mas ainda mantida ativamente em 2026 |
| [[wiki/concepts/cobol]] | Linguagem de 1959 que sustenta o sistema financeiro mundial (Pix incluso); modernização se dá pela borda (API/filas), não por reescrita |

### Boas Práticas de Engenharia

| Página | Hook |
|---|---|
| [[wiki/concepts/logging-estruturado]] | Logs com contexto (user_id, trace_id, error) — a diferença entre "vejo o problema" e "3h chutando" |
| [[wiki/concepts/boy-scout-rule]] | Deixe o código um pouco mais limpo a cada mudança — estratégia de pagamento contínuo de dívida técnica inadvertida |
| [[wiki/concepts/codigo-para-o-mantenedor]] | Escreva pensando em quem vai manter, inclusive você mesmo no futuro — vale também para código gerado por IA |
| [[wiki/concepts/fazer-a-coisa-mais-simples-que-poderia-funcionar]] | Princípio de XP: resolva com a solução mais simples válida agora, refatore depois se necessário |
| [[wiki/concepts/quadrante-de-fowler]] | Dois eixos: Deliberado/Inadvertido × Prudente/Imprudente; só Prudente+Deliberado é aceitável |
| [[wiki/concepts/debt-ratio-sqale]] | `remediation cost / development cost` — fórmula SQALE por trás do percentual de dívida técnica reportado por ferramentas como SonarQube |
| [[wiki/concepts/hotspot-analysis]] | Complexidade ciclomática × code churn — hotspot real é a interseção, não cada métrica isolada; 80% da dor vem de 20% dos arquivos |
| [[wiki/concepts/paid-framework]] | Performance/Architectural/Integration/Dependency — mnemônico rápido de priorização de dívida técnica sem ferramenta de análise |
| [[wiki/concepts/refactor-vs-rewrite-matrix]] | Valor de negócio × risco técnico decide entre refatorar, reescrever, conviver ou depreciar um item de dívida técnica |
| [[wiki/concepts/ciclo-de-mudanca-de-arquitetura]] | AS-IS → TO-BE → POC (testada na escala real) → coexistência com o legado → novo AS-IS — pular etapa é a causa mais comum de retrabalho caro numa mudança de arquitetura |
| [[wiki/concepts/strangler-fig-pattern]] | Transform/Coexist/Eliminate: substitui sistema legado incrementalmente via proxy de roteamento, sem reescrita big bang; CDC para dados compartilhados durante a transição |
| [[wiki/concepts/complexidade-como-estrategia]] | Três estágios: inconsciente → aparência → sabotagem — criar código incompreensível para se tornar insubstituível |
| [[wiki/concepts/ciclo-da-desgraca-software]] | Espiral reescrita→mesmo problema→dois sistemas; alternativa: refatoração incremental com strangler fig |
| [[wiki/concepts/folga-de-capacidade-slack]] | Nunca alocar 100% da capacidade — ~20% de folga absorve o imprevisto sem forçar emissão de dívida técnica (Reinertsen, teoria de filas) |
| [[wiki/concepts/feature-freeze]] | Semana sem features novas para repaginar arquitetura, pagar dívida e consertar testes flaky — respiro pontual vs. code freeze (só testar) |
| [[wiki/concepts/bus-factor]] | Quantas pessoas precisariam sair para o conhecimento crítico se perder; o "Dev Gandalf" (bus factor = 1) é sintoma de código não-modificável, não solução |
| [[wiki/concepts/pitfalls-de-linguagem]] | Armadilhas que existem na linguagem mas não devem ser usadas — descobertas pelo uso, não pelo estudo teórico |
| [[wiki/concepts/dizer-sim-para-tudo]] | Dizer sim para tudo fragmenta foco e inibe surgimento de líderes — promessa é dívida, tempo estoura |
| [[wiki/concepts/definicao-de-pronto]] | Código que só funciona não está pronto — legível + testado + documentado + revisado por regra de negócio |
| [[wiki/concepts/testar-proprio-codigo]] | Testar só o caminho feliz é concordar com a própria opinião — testes automatizados cobrem erro e happy path |
| [[wiki/concepts/atomic-commits]] | Commit atômico = alteração + teste que a valida juntos — unidade funcional, não diário de mudanças |
| [[wiki/concepts/rebase-vs-merge]] | Rebase reescreve SHAs para um histórico linear (ótimo para bisect/blame, perigoso em branch compartilhada); merge preserva o histórico real com um commit de dois pais — regra prática: rebase local antes do PR, merge para integrar |
| [[wiki/concepts/checklist-primeiro-dia-projeto]] | Seis etapas do dia 1 de uma codebase nova — deploy, ORM/migrations e testes resolvidos antes de qualquer feature, quando o custo de errar ainda é baixo |
| [[wiki/concepts/escolha-de-stack]] | Aprender vs. monetizar como eixo central da escolha de stack; framework batteries-included acelera SaaS solo |
| [[wiki/concepts/triade-retorno-risco-liquidez]] | Retorno, risco e liquidez nunca são bons ao mesmo tempo — modelo de investimentos generalizado para qualquer decisão da vida |
| [[wiki/concepts/avaliar-hype-tecnologico]] | Adotar tecnologia hype é risco alto + liquidez baixa; só compensa se o retorno for proporcionalmente alto — caso Node.js no Pagar.me vs. C# na Stone |
| [[wiki/concepts/modulo-profundo]] | Deep module (Ousterhout): poucos módulos grandes com interface simples escondendo complexidade — o oposto de muitos módulos rasos que a IA produz por padrão |
| [[wiki/concepts/modelo-cascata-vs-desenvolvimento-incremental]] | Waterfall falha para software porque é impossível visualizar o design inteiro antes de construir — design incremental corrige o design cedo, enquanto o sistema ainda é pequeno |
| [[wiki/concepts/red-flags-de-design]] | Sinal de que um trecho de código é mais complicado do que precisa — melhor exercitado no código de outra pessoa via code review, não no próprio; catálogo completo dos 14 red flags do livro |
| [[wiki/concepts/ocultamento-de-informacao]] | Information hiding (Parnas): esconder decisões de design dentro de um módulo; vazamento via decomposição temporal é a causa mais comum quando o código segue a ordem de execução em vez do conhecimento necessário |
| [[wiki/concepts/definir-erros-para-fora-da-existencia]] | Redesenhar a semântica de uma operação para que a condição de erro deixe de existir — Tcl `unset`, deleção de arquivo Unix vs. Windows, `substring` do Java; +mascarar, agregar, travar |
| [[wiki/concepts/comentarios-como-ferramenta-de-design]] | Escrever o comentário de interface antes do código expõe cedo se a abstração é boa; discordância explícita de Ousterhout com Clean Code ("comments are always failures") |
| [[wiki/concepts/projetar-duas-vezes]] | Comparar ao menos duas alternativas radicalmente diferentes antes de escolher — mesmo quando a primeira parece óbvia; hábito difícil para quem sempre acertou de primeira |
| [[wiki/concepts/decidir-o-que-importa]] | Separar o que importa do que não importa e estruturar o sistema em torno disso — alavancagem, prominência, repetição, centralidade; "bom gosto" como habilidade central de design |
| [[wiki/concepts/lentes-de-codigo]] | Acoplamento, abstração e estado não são termos para decorar — são lentes que revelam se o código é bom ou só funciona; central para avaliar código gerado por IA |
| [[wiki/concepts/acoplamento]] | Grau de dependência entre partes — quanto uma mudança em A força mudança em B; god function vs. funções separadas por responsabilidade |
| [[wiki/concepts/abstracao]] | Esconder o que não precisa ser visto atrás de um contrato — troca de implementação (banco → API) sem tocar no código consumidor |
| [[wiki/concepts/coesao]] | Quanto as responsabilidades dentro de uma unidade estão relacionadas entre si — alta coesão interna + baixo acoplamento externo é o alvo |
| [[wiki/concepts/single-responsibility]] | Uma unidade deve ter uma única razão para mudar — o critério é o ator que causa a mudança, não o número de linhas |
| [[wiki/concepts/single-responsibility-principle]] | SRP com a analogia da máquina de lavar: um componente no lugar errado "mancha" o comportamento de todos os outros |
| [[wiki/concepts/open-closed-principle]] | Aberto para extensão, fechado para modificação — exemplo do processador de pagamentos e do ORM |
| [[wiki/concepts/liskov-substitution-principle]] | Subclasse deve substituir a base sem quebrar o esperado — exemplo Ave/Pica-pau/Pinguim mostra abstração no nível errado |
| [[wiki/concepts/interface-segregation-principle]] | Não force o cliente a depender de método que não usa — segregar em interfaces menores |
| [[wiki/concepts/dependency-inversion-principle]] | Depender de abstração (soquete/interface), não de implementação concreta fundida ao objeto |
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
| [[wiki/concepts/ddos-syn-flood]] | Handshake TCP nunca completado em massa esgota recursos do servidor — SYN cookies adiam alocação de memória, Under Attack Mode é a camada que falta mesmo com CDN configurado |
| [[wiki/concepts/principio-do-menor-privilegio]] | Permissão exata e nada mais — limita o raio de explosão quando um componente é comprometido |
| [[wiki/concepts/secure-by-default]] | Estado padrão é o mais seguro — fail-secure, confirmação explícita para ações destrutivas |
| [[wiki/concepts/sql-injection]] | Input não sanitizado executado como SQL — Bobby Tables; prevenção: queries parametrizadas |
| [[wiki/concepts/xss]] | Injeção de JavaScript no browser da vítima — mesma classe do SQLi, contexto HTML/JS |
| [[wiki/concepts/cors-misconfiguration]] | `Access-Control-Allow-Origin: *` + `Allow-Credentials: true` permite requisições autenticadas de qualquer site na internet |
| [[wiki/concepts/timing-attack]] | Tempo de resposta como canal de informação — variação de latência revela segredos |
| [[wiki/concepts/sast]] | Análise estática de segurança no código — detecta padrões vulneráveis antes do deploy |
| [[wiki/concepts/secrets-management]] | Credenciais nunca no código — .env local, GitHub Secrets/AWS SM em produção; caso real de agente de IA autônomo encontrando e explorando credencial vazada sem intervenção humana; `.env` publicamente servido como ponto de entrada de um pentest real |
| [[wiki/concepts/idor]] | Recurso acessado por ID sem checar ownership — #1 do OWASP API Top 10 (BOLA); pode escalar até account takeover quando o dado vazado é uma credencial |
| [[wiki/concepts/multitenancy]] | Múltiplos clientes compartilhando as mesmas tabelas — amplia a superfície de IDOR se a checagem de tenant falhar em alguma query |
| [[wiki/concepts/account-takeover]] | Autenticar-se como outro usuário sem senha/MFA — nesta wiki, via chave de API vazada por IDOR e aceita sozinha como credencial de login |
| [[wiki/concepts/upload-arbitrario-rce]] | Upload de arquivo sem validar MIME/extensão/execução — vira RCE quando o servidor trata o arquivo enviado como código |
| [[wiki/concepts/autenticacao-e-autorizacao]] | "Quem é você" vs. "o que você pode fazer" — teste de logout, e caso de credencial de fator único aceita sem segundo fator |
| [[wiki/concepts/password-hashing]] | Armazenar senhas exige algoritmo lento + salt + pepper — plaintext e MD5/SHA são inseguros |
| [[wiki/concepts/salt]] | String aleatória por usuário concatenada à senha — invalida rainbow tables pré-computadas |
| [[wiki/concepts/pepper]] | Segredo do servidor concatenado à senha — defesa se só o banco vazar |
| [[wiki/concepts/bcrypt]] | CPU-hard clássico (fator de trabalho configurável) — superado por rigs de GPU sem memory-hard |
| [[wiki/concepts/argon2]] | Estado da arte: CPU-hard + memory-hard — gargalo de VRAM derrota paralelismo de GPU; três fases (hash inicial, preenchimento de matriz, mistura final) |
| [[wiki/concepts/caesar-cipher]] | Substituição monoalfabética fixa — não é IND-CPA segura, preserva padrão de repetição de caracteres |
| [[wiki/concepts/scytale]] | Cítala espartana — transposição via bastão de diâmetro específico, anterior à cifra de César |
| [[wiki/concepts/vigenere-cipher]] | Substituição polialfabética via chave repetida — "cifra indecifrável" por 300 anos, primeiro exemplo histórico de criptografia simétrica |
| [[wiki/concepts/enigma-machine]] | Máquina de rotores da Alemanha na 2ª Guerra — quebrada por reuso operacional de chave |
| [[wiki/concepts/aes]] | Criptografia simétrica por blocos, 128-256 bits — padrão de dados em repouso, sem vulnerabilidade conhecida quando usado corretamente |
| [[wiki/concepts/rsa]] | Criptografia assimétrica baseada na dificuldade de fatorar primos grandes — resolve o key distribution problem |
| [[wiki/concepts/key-distribution-problem]] | Como compartilhar chave simétrica secreta com segurança — motivou a criação da criptografia de chave pública |
| [[wiki/concepts/ind-cpa-security]] | Modelo formal de segurança — atacante não deve distinguir qual de duas mensagens escolhidas gerou uma cifra dada |
| [[wiki/concepts/shor-algorithm]] | Algoritmo quântico que fatora inteiros em tempo polinomial — quebra RSA por completo |
| [[wiki/concepts/grover-algorithm]] | Aceleração quântica quadrática de busca — reduz AES-256 a ~128 bits efetivos, ainda seguro |
| [[wiki/concepts/post-quantum-cryptography]] | Algoritmos NIST (ML-KEM, ML-DSA) resistentes a Shor/Grover — resposta ao risco "colha agora, decifre depois" |
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
| [[wiki/concepts/agent-containment]] | Isolar o processo de um agente de IA (sandbox) para limitar dano se ele executar código malicioso vindo de uma dependência comprometida — mesmo um proxy de egress dedicado pode ser contornado via zero-day, como em [[wiki/sources/modelo-openai-escapa-sandbox-benchmark-cyberseguranca]] |
| [[wiki/concepts/zero-day]] | Falha desconhecida do fornecedor até o momento da exploração — caso real: agente de IA achou e explorou zero-day no próprio proxy de rede que o continha |
| [[wiki/concepts/supply-chain-security]] | SBOM, SLSA, Sigstore/Cosign contra dependências comprometidas; ataques via `postinstall` malicioso (ex.: npm) como vetor mais direto |
| [[wiki/concepts/sistema-operacional-imutavel]] | Root somente-leitura (NixOS/Fedora Silverblue) — dano ao sistema não sobrevive a um reboot |
| [[wiki/concepts/soberania-digital]] | Controle sobre dados/infra dentro de fronteiras jurisdicionais — estendido a controle sobre o próprio modelo de IA quando guardrails de terceiros recusam ajudar numa investigação de incidente |
| [[wiki/concepts/devsecops]] | Segurança como responsabilidade compartilhada em todo o ciclo de vida do software, não setor isolado no fim do pipeline — cunhado pela Gartner em 2012 a partir do DevOps |
| [[wiki/concepts/shift-left-testing]] | Mover testes de segurança para o início do ciclo (planejamento, código) em vez de só no fim — secret scanning, SCA, SAST, IAST cobrindo cada fase |

### Frontend & Design Engineering

| Página | Hook |
|---|---|
| [[wiki/concepts/design-first]] | Layout no Figma antes do código — padrão em times grandes com designers dedicados; Figma fica desatualizado em times pequenos |
| [[wiki/concepts/code-first]] | Codar com component libraries sem layout prévio — velocidade alta, risco de Frankenstein visual |
| [[wiki/concepts/design-engineer]] | Cargo do meio: conhecimentos de design aplicados diretamente no código — experimentações no código, Figma como referência |
| [[wiki/concepts/component-library]] | Shadcn, Radix, Headless UI — componentes pré-prontos; headless dá controle total, estilizadas são mais rápidas |
| [[wiki/concepts/fake-delay]] | Delay mínimo intencional (300ms) para garantir feedback visual perceptível — performance percebida é design |
| [[wiki/concepts/design-como-interacao]] | Design se manifesta na interação, não na primeira impressão — micro-interações, onboarding, feedback, linguagem |
| [[wiki/concepts/hierarquia-visual]] | Dois CTAs com o mesmo peso visual competem pela atenção — o mais fácil de clicar rouba conversão do que importa |
| [[wiki/concepts/lei-da-proximidade-gestalt]] | Elementos próximos são lidos como um grupo único (Gestalt) — o logo da Unilever forma um U só quando os ícones estão juntos |
| [[wiki/concepts/affordance]] | Propriedade visual que sugere como usar um elemento sem curva de aprendizado — botões sem cursor pointer ou hover confundem o usuário |
| [[wiki/concepts/maquina-de-estados-ui]] | Componente sem estado de loading mapeado é o sintoma mais comum de não pensar a UI como máquina de estados |
| [[wiki/concepts/react-compiler]] | Compilador do React 19 que memoiza valores e funções automaticamente em build time, reduzindo a necessidade de useMemo/useCallback manuais |
| [[wiki/concepts/useMemo]] | Hook que memoiza o resultado de um cálculo — só recalcula quando as dependências mudam; overhead supera ganho em cálculos triviais |
| [[wiki/concepts/useCallback]] | Hook que memoiza a referência de uma função entre renders — essencial para não quebrar `React.memo` em componentes filhos |
| [[wiki/concepts/concurrent-mode]] | Modelo de renderização do React 18+ que pausa/retoma/prioriza renders sem bloquear a UI — useTransition e useDeferredValue |
| [[wiki/concepts/monolito-modular-frontend]] | Fronteiras por domínio dentro de um único build — ponto de partida correto antes de cogitar builds separados ou microfrontends |
| [[wiki/concepts/microfrontend-baseado-em-rotas]] | Proxy reverso + builds separados por módulo via libs de monorepo — maior parte dos benefícios de desacoplamento com a menor complexidade adicionada |
| [[wiki/concepts/microfrontends-parciais]] | Múltiplos frameworks coexistindo na mesma tela via Shadow DOM/eventos — desacoplamento alto vendido, custo real em performance/CI-CD/versionamento/governança |
| [[wiki/concepts/monorepo-frontend]] | Apps consomem libs/packages compartilhados como dependências instaláveis — dependência flui numa via só, apps nunca são importadas por packages |
| [[wiki/concepts/zustand]] | Estado global sem Provider — módulo fora da árvore + Hook de sincronização; o mecanismo central é um Observer recriável em ~40 linhas de JS puro |

### Pipeline de Renderização do Browser

| Página | Hook |
|---|---|
| [[wiki/concepts/critical-rendering-path]] | Sequência completa da URL ao pixel — cache, DNS, TCP, TLS, HTTP, DOM/CSSOM, render tree, layout, paint, composite |
| [[wiki/concepts/dom]] | Árvore construída incrementalmente e com tolerância a erros pelo parser de HTML — nunca falha o parsing |
| [[wiki/concepts/cssom]] | Árvore de estilos em cascata, render-blocking — nada é pintado até o CSSOM estar completo |
| [[wiki/concepts/render-tree]] | DOM + CSSOM combinados, só nós visíveis — `display:none` fica de fora, `visibility:hidden` entra (ocupa espaço) |
| [[wiki/concepts/reflow-layout]] | Cálculo recursivo de geometria via box model — unidades relativas viram pixels absolutos |
| [[wiki/concepts/paint-composite]] | Pintura em camadas + composição na GPU — `transform`/`opacity` pulam layout e paint |
| [[wiki/concepts/script-async-defer]] | Parser para em `<script>` síncrono porque não sabe se ele muta o DOM — `defer` executa após DOM pronto, na ordem do documento |
| [[wiki/concepts/layout-thrashing]] | Ler geometria e escrever estilo alternadamente em loop força reflow síncrono repetido |
| [[wiki/concepts/box-model]] | Content, padding, border, margin — camadas que definem o tamanho final de cada caixa |
| [[wiki/concepts/tcp-three-way-handshake]] | SYN → SYN-ACK → ACK — abre a conexão antes do TLS e do request HTTP |
| [[wiki/concepts/tls-handshake]] | Negociação de certificados/chaves em HTTPS — round trips extras antes do primeiro byte |
| [[wiki/concepts/http-caching]] | Cache válido pula toda a navegação de rede — fonte não distingue cache HTTP comum de bfcache |

### React & Hooks

| Página | Hook |
|---|---|
| [[wiki/concepts/derived-state]] | Se dá para calcular a partir de estado/props existentes, não é estado — calcula na renderização em vez de sincronizar via `useEffect` |
| [[wiki/concepts/stale-closure]] | `useEffect` com array de dependências vazio congela variáveis da primeira renderização — closure captura variáveis, não valores |
| [[wiki/concepts/react-memo]] | Bloqueia a entrada no fluxo de renderização antes mesmo de gerar Virtual DOM — só compensa em componente puro, que renderiza muito, com props estáveis, e de porte médio/grande |
| [[wiki/concepts/shallow-compare]] | `{} === {}` é `false` — objeto/array/função recriados no corpo do componente quebram `memo` mesmo com conteúdo idêntico, porque a comparação é por referência, não por valor |

### Internals de Frameworks Frontend (React/Vue/Angular)

| Página | Hook |
|---|---|
| [[wiki/concepts/virtual-dom]] | Cópia da árvore de componentes em memória — diff contra a anterior decide o que tocar no DOM real |
| [[wiki/concepts/reconciliacao]] | Algoritmo de diffing — trocar tipo de elemento recria do zero; `key` errada (índice em lista dinâmica) faz inputs perderem texto e estado vazar entre itens |
| [[wiki/concepts/signals]] | Reatividade fine-grained — liga variável direto ao nó de DOM, sem diff nem árvore; vence Virtual DOM em listas gigantes/animações pesadas |
| [[wiki/concepts/batching]] | Agrupa múltiplas mudanças de estado numa única atualização de DOM — ler o DOM logo após mudar estado ainda mostra o valor antigo |
| [[wiki/concepts/hydration]] | HTML do SSR chega estático e inerte — JS conecta listeners/estado; arquitetura de ilhas hidrata só o que é interativo |
| [[wiki/concepts/client-side-routing]] | `pushState`/`popstate` trocam URL e conteúdo sem requisição — acesso direto a rota profunda quebra sem fallback de servidor para `index.html` |
| [[wiki/concepts/tree-shaking]] | Bundler remove código nunca importado — importar função específica em vez de biblioteca inteira reduz drasticamente o bundle |
| [[wiki/concepts/code-splitting]] | Bundle dividido em chunks carregados sob demanda (`lazy`) — cada página baixa só o JS que precisa |
| [[wiki/concepts/component-lifecycle]] | Montar/atualizar/desmontar universal a todo framework — esquecer cleanup no desmonte (WebSocket, timers, listeners) vaza memória |

### Testes & Qualidade

| Página | Hook |
|---|---|
| [[wiki/concepts/tdd]] | Red-Green-Refactor — o teste vem antes para sentir o acoplamento antes de criá-lo, não para cobertura |
| [[wiki/concepts/test-doubles]] | Dummy/Stub/Fake/Spy/Mock (Meszaros) — Fake robusto testa o contrato, Mock frágil testa o nome do método |
| [[wiki/concepts/seedwork]] | Framework mínimo que cada time reconstrói por conta própria em vez de compartilhar um só — origem do framework de testes de Kent Beck antes do JUnit |
| [[wiki/concepts/contract-testing]] | Consumer-Driven Contracts + Pact — valida que dois serviços concordam com o formato da comunicação sem rodar juntos |
| [[wiki/concepts/self-initializing-fake]] | Fake que se autovalida contra o serviço real e vira snapshot local — técnica de Fowler para doubles usados em contract testing |
| [[wiki/concepts/must-ignore-pattern]] | Ponto de extensão de schema que um consumidor pode ignorar com segurança — origem do padrão Consumer-Driven Contracts (Ian Robinson, 2006) |
| [[wiki/concepts/piramide-de-testes]] | Unitário → Integração → E2E; quanto mais alto, mais lento, caro e frágil |
| [[wiki/concepts/testes-integracao-banco-real]] | Nunca mockar o banco em testes de integração — o valor do teste está em validar a query real |
| [[wiki/concepts/teste-de-integracao-estreito-vs-amplo]] | Fowler separa "integration test" em estreito (double + contract test, rápido) e amplo (serviços reais, lento) |
| [[wiki/concepts/unit-test-solitario-vs-sociavel]] | Solitário mocka tudo (London), sociável usa colaboradores reais (Detroit) — confusão irmã do narrow/broad |
| [[wiki/concepts/criterios-de-bom-teste]] | Determinístico, conciso, relevante, compreensível, durável — e 100% de cobertura não garante ausência de bug |
| [[wiki/concepts/mapear-entrada-processamento-saida]] | Decompor tarefa em entrada/processamento/saída + Given/When/Then antes de implementar — cada linha vira um teste anotado antes do primeiro código |
| [[wiki/concepts/loop-de-confirmacao-de-entendimento]] | Ouvir a explicação inteira sem interromper, depois dizer de volta "o que eu entendi foi X" — antes de cair para implementação |
| [[wiki/concepts/setup-live-reload-debug-testes]] | Live reload + `--inspect` + `node --test` integrados via `launch.json` — testes e debugger rodam a cada Ctrl+S, sem sair do editor |
| [[wiki/concepts/tipagem-com-jsdoc]] | `@typedef`/`@param`/`@returns` dão autocomplete e validação de tipo em JavaScript puro, sem TypeScript |
| [[wiki/concepts/tres-estagios-maturidade-testes]] | UI manual → Postman/API-first → Jest em modo watch — o que muda não é o cliente HTTP, é se a verificação vira especificação permanente ou checagem descartável |

### Padrões e Design

| Página | Hook |
|---|---|
| [[wiki/concepts/pattern-recognition]] | Capacidade humana de detectar repetições — base do aprendizado por exposição |
| [[wiki/concepts/design-patterns]] | Catálogo de soluções nomeadas — útil só depois de já ter visto os padrões na prática |
| [[wiki/concepts/observer-pattern]] | Dependência um-para-muitos com notificação automática — terceiro estágio de desacoplamento, componentes que não se conhecem nem estaticamente |
| [[wiki/concepts/factory-pattern]] | Centraliza a criação de objetos — segundo estágio de desacoplamento, isola implementação mas mantém chamada estática explícita |
| [[wiki/concepts/abstract-factory]] | Cria famílias de objetos relacionados, não só um tipo — variante do Factory Method |
| [[wiki/concepts/dependency-injection]] | Dependência recebida de fora em vez de criada internamente — torna acoplamento flexível/testável sem eliminá-lo |
| [[wiki/concepts/mapper-pattern]] | Classe estática por camada que converte entidade de domínio para o formato de outra camada (Prisma, HTTP) — isola o acoplamento à tecnologia, não ao domínio |
| [[wiki/concepts/objeto-vs-estrutura-de-dados]] | Uncle Bob: objeto = funções sobre dados implícitos/encapsulados; estrutura de dados = dados expostos operados por funções externas — conceitos literalmente opostos, não sobrepostos |
| [[wiki/concepts/clean-architecture]] | Regra de dependência apontando para dentro; fluxo de aplicação web camada a camada — Controller empacota Input Data, Use Case orquestra Entities, Presenter reempacota em ViewModel |
| [[wiki/concepts/dci-e-bce]] | Data-Context-Interaction (Reenskaug/Coplien) e Boundary-Control-Entity (Jacobson) — as duas arquiteturas, junto com Hexagonal, que Robert Martin sintetizou na Clean Architecture |
| [[wiki/concepts/template-method-pattern]] | Esqueleto de algoritmo com etapas variáveis — variação via composição (não herança) usada num WebController de API REST |
| [[wiki/concepts/arquitetura-em-3-camadas]] | Presentation → Business → Data Access com dependência direta e transitiva; contraponto usado para explicar por que Clean Architecture é "domain-centric" |
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
| [[wiki/concepts/refatoracao]] | Mudar estrutura interna sem alterar comportamento externo — dois chapéus de Kent Beck, passos pequenos, testes na base da pirâmide como rede de segurança, refatoração oportunista vs. planejada, analogia de jardinagem, seis situações do Pragmatic Programmer |
| [[wiki/concepts/dois-chapeus-kent-beck]] | Adicionar funcionalidade e refatorar são atividades mutuamente exclusivas no tempo — cada uma com sua própria disciplina de validação |
| [[wiki/concepts/entropia-de-software]] | Tendência natural de um sistema degradar com o tempo mesmo sem erro deliberado — refatoração como poda contínua de um jardim, não construção pontual de um prédio |
| [[wiki/concepts/finops-para-ia]] | Quatro práticas de governança de custo de token: budget/limite por dev-ferramenta, métricas de valor em vez de dashboard de volume, classificação de dados para self-hosted, ownership evitando lock-in de provedor |

## Entities

| Página | Hook |
|---|---|
| [[wiki/entities/gregor-ojstersek]] | Autor da newsletter Engineering Leadership (Substack) e do livro *The Multiplier Mindset* — tese de que o potencial de engenheiros se reconhece por atitude/mindset, não tech skill atual |
| [[wiki/entities/lucas-faria]] | Autor do artigo "sete conceitos que mais caem em entrevistas de System Design Tier S" — base da série de vídeos de System Design de Pedro Camaforte (identidade/URL não confirmadas na fonte) |
| [[wiki/entities/principles-of-product-development-flow]] | Livro (Reinertsen, atribuição externa) que aplica teoria de filas ao desenvolvimento — origem da regra de nunca alocar 100% da capacidade |
| [[wiki/entities/faros-ai]] | Plataforma de engineering intelligence (dados de produção, não satisfação) que cunhou o "paradoxo da aceleração" — velocidade individual sobe com IA, throughput do sistema não |
| [[wiki/entities/amazon-web-services]] | Maior provedor de cloud do mundo — infraestrutura global, toolkit essencial de compute/deploy/dados (EC2, Lambda, ECS, RDS, DynamoDB...) e tema recorrente de vendor lock-in quanto mais serviços proprietários um sistema adota |
| [[wiki/entities/w3c]] | Padronizou SOAP e tornou XML recomendação oficial em 1998 |
| [[wiki/entities/john-resig]] | Criador do jQuery (2006) — resolveu a fragmentação de DOM/JavaScript entre navegadores |
| [[wiki/entities/pulsar-saas]] | SaaS pessoal ligado a um desafio de estudos gratuito de 100 dias no Instagram — caso real de autopentest guiado por IA |
| [[wiki/entities/geraldo-alcantara]] | Pentester e criador de conteúdo — demonstrações de exploração em ambiente controlado, incluindo cadeia completa contra loja construída via vibe coding |
| [[wiki/entities/the-primeagen]] | Engenheiro de software sênior na Netflix, criador de conteúdo (YouTube, em inglês) — reagiu a um vídeo de Theodor defendendo programar "do jeito difícil" |
| [[wiki/entities/theodor]] | Dev/criador de conteúdo construindo jogo indie do zero sem engine — identidade exata não confirmada na fonte |
| [[wiki/entities/oracle]] | Empresa de software corporativo (~400bi de market cap) — demitiu 20-30 mil pessoas via e-mail automático, motivo alegado é substituição de DBAs por agente de IA piloto há 8+ meses |
| [[wiki/entities/otavio-lemos]] | Professor (UNIFESP/USP/UCI) e criador de conteúdo — autor de *Arquitetura Limpa na Prática*, tutorial de Clean Architecture com estudo de caso completo em TypeScript |
| [[wiki/entities/knight-capital]] | Trading de alta frequência: código morto reativado por engano num deploy (2012) causou perda de ~$440-460 milhões em 45 minutos — caso extremo de custo de não seguir a Boy Scout Rule |
| [[wiki/entities/edgar-codd]] | IBM, 1970: paper do modelo relacional e independência de dados — fundamento de tudo que veio depois |
| [[wiki/entities/rabbitmq]] | Message broker AMQP — fila que viabiliza Saga Pattern coreografado sem gargalo de coordenação síncrona |
| [[wiki/entities/rsa-security]] | Criadora do SecurID — token de hardware que popularizou o segundo fator de autenticação nos anos 90 |
| [[wiki/entities/leetcode]] | Plataforma de prática de algoritmos e formato de referência para entrevistas técnicas de coding |
| [[wiki/entities/ietf]] | Padronizou HOTP (RFC 4226) e TOTP (RFC 6238), tirando a autenticação por OTP das mãos de fornecedores proprietários |
| [[wiki/entities/sakana-ai]] | Empresa japonesa de IA — Fugo, pool de modelos que superou Fable 5 e alguns benchmarks do Mitos preview em cybersegurança |
| [[wiki/entities/alan-turing]] | Matemático britânico — propôs a máquina de Turing (1936), o modelo teórico que define o que é computável |
| [[wiki/entities/alok-kanojia]] | Psiquiatra formado em Harvard (canal HealthyGamer/"Dr. K") — fonte primária citada sobre o impacto de jogos no cérebro e problemas de escopo aberto vs. fechado |
| [[wiki/entities/erick-wendel]] | Criador de conteúdo brasileiro sobre Node.js e testes automatizados — método de 3 pilares para produtividade com testes; possível duplicata não confirmada de [[wiki/entities/eric-lenda]] |
| [[wiki/entities/grafana-labs]] | Empresa por trás do Grafana/Grafana Cloud e da stack LGTM (Loki, Tempo, Mimir) — assistente de IA embutido no chat web correlaciona telemetria sem consumir créditos do editor do usuário |
| [[wiki/entities/rinha-de-backend]] | Desafio open source de backend (transações crédito/débito) — usado como exemplo de decomposição de tarefa em casos de teste |
| [[wiki/entities/ux-pilot]] | Ferramenta de geração de UI/UX por IA (telas completas ou wireframes) que exporta pro Figma, de onde o MCP conecta a uma IA de código |
| [[wiki/entities/moonshot-ai]] | Lab chinês criador do Kimi — Kimi K3 (2,8T parâmetros, MoE 896/16 experts) publica método de inferência aberto para descentralizar conhecimento de servir modelos grandes |
| [[wiki/entities/instituto-aaron-schwartz]] | ONG brasileira que leva conhecimento de tecnologia a adolescentes de cidades pequenas sem acesso prévio a essa informação |
| [[wiki/entities/deepseek]] | Lab chinês — DeepSeek V4 Pro, maior open source antes do Kimi K3; DeepSeek Flash V4 como referência de modelo barato para tarefas do dia a dia |
| [[wiki/entities/nvidia]] | Fabricante de GPUs — sujeita a sanções de exportação de chips para a China, pressão de fundo por trás de inovação em MoE/KV Cache |
| [[wiki/entities/bubblewrap]] | Binário de sandboxing do GNOME (usado pelo Flatpak) — base técnica do AI Jail e do sandbox nativo do Claude Code |
| [[wiki/entities/hermes-agent]] | Agente open source (MIT) com closed-loop skill learning system e memória em três camadas — liderou ranking de tokens do OpenRouter |
| [[wiki/entities/open-claw]] | Agente open source (MIT), referência de mercado que motivou Hermes Agent e o "Dreaming in Claude" da Anthropic |
| [[wiki/entities/geoffrey-huntley]] | Engenheiro australiano, publicou o Ralph Loop em julho de 2025 — loop agêntico de uma linha de bash batizado por Ralph Wiggum |
| [[wiki/entities/peter-steinberger]] | Autor da frase viral "if you are not the model, you are the harness" (6,5M views) e, numa segunda fonte independente, do tweet "loop ou grafo?" que disparou o termo graph engineering; citado (não reconciliado) como criador do OpenClaw |
| [[wiki/entities/hotmart]] | Maior plataforma de produtos digitais do mundo (25M+ compradores, R$50bi em vendas) — afiliado como exemplo de "aresta" conectando produto a consumidor num grafo |
| [[wiki/entities/hostinger]] | Provedora de VPS (menção patrocinada) — servidor virtual livre, físico gerenciado (DDoS, firewall IA, backups semanais) |
| [[wiki/entities/mano-davin]] | Criador do Find My SaaS — 15 dias após lançamento: R$ 4.819 faturados, 646 SaaS cadastrados, VPS mínima sob 230mil+ requisições; depois, SYN flood de 260M requests/dia derruba o servidor, reconstruído do zero |
| [[wiki/entities/replit]] | Plataforma de agentes de IA — workers paralelos (possível `git worktree`), taskboard multiplayer, testes end-to-end automáticos do próprio agente |
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
| [[wiki/entities/joao-rocket-city]] | Engenheiro de software pra gringa (3 anos), apresentador de série semanal de system design no canal Rocket City |
| [[wiki/entities/openai]] | Organização responsável pelo GPT-3/4 — formalizou in-context learning e scaling laws; criadora do tokenizer tiktoken; benchmark interno de cybersegurança sem guardrails resultou em zero-day explorado e ataque real via credencial vazada |
| [[wiki/entities/hugging-face]] | Hub de modelos, datasets e benchmarks de IA — alvo de um ataque real via credencial de servidor vazada e publicamente indexada, explorado por um agente de IA autônomo |
| [[wiki/entities/google]] | Criadora do Gemini e do harness AntiGravity — concorrente de Anthropic e OpenAI, tokenizer próprio |
| [[wiki/entities/openrouter]] | Gateway/agregador de acesso a múltiplos modelos de LLM (incluindo modelos chineses como GLM) por trás de uma única API |
| [[wiki/entities/matt-pocock]] | Educador de TypeScript/AI (AI Hero) — fundamentos de LLM, e a tese de que fundamentos de software importam mais que nunca na era da IA |
| [[wiki/entities/fred-brooks]] | Mythical Man-Month, No Silver Bullet, e o conceito de "design concept" — teoria compartilhada e invisível do que está sendo construído |
| [[wiki/entities/john-ousterhout]] | A Philosophy of Software Design — define complexidade como estrutura difícil de mudar; cunhou "módulos profundos" |
| [[wiki/entities/kent-beck]] | Criador do TDD moderno e da XP — "invista no design do sistema todos os dias"; coautor do JUnit com Erich Gamma |
| [[wiki/entities/junit]] | Framework de testes criado por Kent Beck e Erich Gamma num voo para a OOPSLA 1997 — origem da família de frameworks Xunit |
| [[wiki/entities/c3-project]] | Chrysler Comprehensive Compensation — projeto de nascimento da Extreme Programming, onde o framework de testes de Kent Beck foi usado |
| [[wiki/entities/gang-of-four]] | Erich Gamma, Richard Helm, Ralph Johnson e John Vlissides — autores de *Design Patterns* (1994); Gamma também coautor do JUnit |
| [[wiki/entities/vercel-ai-sdk]] | SDK TypeScript da Vercel para chamar múltiplos provedores de LLM com API unificada |
| [[wiki/entities/vercel]] | Plataforma de deploy — caso interno de remover 80% das ferramentas de um agente para melhorar performance |
| [[wiki/entities/jason-wei]] | Pesquisador Google Brain — lead author do paper de chain-of-thought prompting e do paper de emergent abilities |
| [[wiki/entities/fabio-akita]] | Programador brasileiro, autodidata desde 1991, criador do canal Akita On Rails |
| [[wiki/entities/lucas-badico]] | Programador e professor brasileiro, criador de conteúdo sobre Golang e carreira; defende a ponte fullstack como caminho de entrada ao backend |
| [[wiki/entities/codigo-fonte-tv]] | Canal brasileiro de YouTube com pesquisa salarial própria (pesquisa.codefonte.com.br) e série de design patterns em TypeScript/Deno; cruza dados com pesquisas oficiais de fabricantes de linguagem |
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
| [[wiki/entities/boris]] | Criador do Claude Code (Anthropic) — argumenta que escrever `CLAUDE.md`/`review.md`/skills/docs para agentes é o novo trabalho de engenharia, barateado pela automação |
| [[wiki/entities/paulo-tarso]] | Autor brasileiro de artigo bilíngue que detalha na prática como implementar as métricas de Uncle Bob (cobertura, CCN, tamanho de módulo, mutation testing) |
| [[wiki/entities/ugonna-thelma]] | Autora de "The S.O.L.I.D Principles in Pictures" (Medium, 2020) — identidade resolvida a partir de um nome deformado por transcrição automática de áudio num vídeo ingerido antes do artigo original |
| [[wiki/entities/shopify]] | E-commerce que hospeda ~14% das lojas americanas — substituiu reserva de estoque Redis+MySQL por MySQL puro com SKIP LOCKED, segurando US$ 5,1M/minuto na Black Friday 2025 |
| [[wiki/entities/37signals]] | Empresa por trás do Basecamp e Rails — saiu do cloud para hardware próprio; criadora do Solid Queue, fila 100% sobre banco relacional |
| [[wiki/entities/lucas-montano]] | Criador de conteúdo brasileiro — argumenta que o pânico de "atrofia cognitiva" por IA mede o tipo errado de habilidade (sintaxe, não conhecimento perene) |
| [[wiki/entities/eric-ries]] | Autor de *A Startup Enxuta* — ex-programador que criou a metodologia Lean Startup depois de lançar um produto que ninguém queria |
| [[wiki/entities/mano-deivin]] | Canal brasileiro de YouTube sobre carreira e produto para devs |
| [[wiki/entities/nir-eyal]] | Autor de *Hooked* e *Indistraível* — escreveu o segundo livro como antídoto ao próprio primeiro |
| [[wiki/entities/ayn-rand]] | Escritora e filósofa russo-americana — criadora do Objetivismo; autora de *A Nascente* |
| [[wiki/entities/martin-fowler]] | Chief Scientist Thoughtworks, autor de *Refactoring* e *PoEAA* — mantém o bliki, referência em terminologia de testes e arquitetura |
| [[wiki/entities/gerard-meszaros]] | Autor de *xUnit Test Patterns* (2007) — criou a taxonomia de Test Doubles (Dummy/Fake/Stub/Spy/Mock) divulgada por Martin Fowler |
| [[wiki/entities/thoughtworks]] | Consultoria de software onde Martin Fowler é Chief Scientist — fundada por Roy Singham, não por Fowler (contradição sinalizada contra fonte que afirma o contrário) |
| [[wiki/entities/ian-robinson]] | Principal Consultant na Thoughtworks — autor do artigo de 2006 que cunha o padrão Consumer-Driven Contracts, hospedado no site de Martin Fowler mas não escrito por ele |
| [[wiki/entities/james-lewis]] | Principal Consultant na Thoughtworks — coautor com Martin Fowler do artigo de 2014 que cunhou a definição de microsserviços |
| [[wiki/entities/david-farley]] | Coautor de *Continuous Delivery* com Jez Humble; envolvido no LMAX; refuta o "triângulo de ferro" com dados DORA |
| [[wiki/entities/mercado-livre]] | Maior e-commerce/fintech da América Latina — combina ISO 27001 + PCI-DSS + Zero Trust; adotante consolidado de Go em produção |
| [[wiki/entities/andre-casciotti]] | Criador de conteúdo brasileiro, canal Próximo Nível — carreira dev, granularidade de mudança, síndrome do impostor em todo nível de carreira, decomposição de tarefas |
| [[wiki/entities/marco-bruno]] | Educador, comunidade Cohab Code — 3 dicas para vaga júnior (networking, ensaiar entrevistas, transparência); ensinar como multiplicador de impacto |
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
| [[wiki/entities/chris-kiehl]] | Autor do blog Blogomatano e de *Data-Oriented Programming in Java* — retrospectivas de carreira listando opiniões de engenharia que mudaram/permaneceram |
| [[wiki/entities/vitor-sousa-pereira]] | Autor do blog `0x1.pt` — escreveu "The Insanity of Being a Software Engineer" (2025), lista satírica da escalada de exigências técnicas esperadas de um único engenheiro |
| [[wiki/entities/ken-thompson]] | Criador do Unix e do `grep` na AT&T — Unix nasceu como subproduto de rodar melhor seu jogo *Space Travel*; `grep` era comando privado antes de virar público |
| [[wiki/entities/patrick-debois]] | "Padrinho" do termo DevOps — blog Jedi, movimento de infraestrutura ágil desde 2008, criador do primeiro DevOps Day (Gante, 2009) |
| [[wiki/entities/flickr]] | Palestra "10+ Deploys por Dia" na Velocity 2009 — catalisou o movimento DevOps ao demonstrar deploys frequentes via cooperação dev/ops |
| [[wiki/entities/andrej-karpathy]] | Ex-diretor de IA da Tesla, fundador da OpenAI — tese dos "três paradigmas de interface de LLM" (site → app → agente autônomo assíncrono organizacional), em reação ao Claude Tag |
| [[wiki/entities/gergely-orosz]] | Autor do Pragmatic Engineer — contraponto ao hype do Claude Tag: o breakthrough é integrar de forma confiável todos os sistemas internos de uma empresa, não a interface do Slack |
| [[wiki/entities/devin-ai]] | Cognition AI — precursor do padrão de agente na nuvem (cloud agent) via chat/Slack; usado (relato de segunda mão) pelo Nubank para refatoração |
| [[wiki/entities/abacus-ai]] | Plataforma de IA por assinatura — Custom Router configurável por categoria de tarefa (Frontier/Complexo/Velocidade/Balanceado/Fallback), chave de API conectável a outros harnesses |
| [[wiki/entities/artificial-analysis]] | Site de benchmarks independentes de LLM — índice de inteligência/coding, velocidade e custo por tarefa entre modelos frontier e alternativas mais baratas |
| [[wiki/entities/opencode]] | Harness de codificação agêntica em CLI, parecido com o Claude Code mas agnóstico de provider — conecta a qualquer endpoint via chave de API |
| [[wiki/entities/xai]] | Empresa de IA de Elon Musk (data centers e modelos próprios, família Grok) — teto mensal de uso de IA para engenheiros internos citado como sinal de escrutínio de custo mesmo com infra própria |
| [[wiki/entities/elon-musk]] | Fundador da xAI — citado por relato de segunda mão sobre limite de uso de IA imposto a engenheiros internos |
| [[wiki/entities/dhh]] | Criador do Ruby on Rails, cofundador da 37signals — trocou de "anti-agente raiz" (2025) para "agent first" (2026) em ~6 meses |
| [[wiki/entities/antirez]] | Criador do Redis — publicou "não use agente", reverteu e cunhou "automatic programming" vs. vibe coding |
| [[wiki/entities/thorsten-ball]] | Criador do agente AMP — "o agente escreve 70-80% do código, eu só faço commit" |
| [[wiki/entities/steve-yegge]] | Citado sobre o dev virar majoritariamente "babá de agente" na Escola 2 de programação com IA |
| [[wiki/entities/sean-grove]] | OpenAI — "a especificação é o artefato valioso, o código é só uma projeção dela" |
| [[wiki/entities/coderabbit]] | Ferramenta de code review por IA — fonte do dado de que código gerado por IA tem ~2,77x mais falhas de segurança que código humano (análise de PRs reais) |
| [[wiki/entities/veracode]] | Empresa de AppSec — relatório 2025 testando 100+ modelos corrobora o mesmo múltiplo (~2,77x) de falhas de segurança do CodeRabbit |
| [[wiki/entities/black-duck]] | Empresa de segurança open source — relatório sobre 947 codebases: +107% de vulnerabilidades/codebase em um ano, só 24% das empresas avaliam código de IA por completo |

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

### Agile & Estimativa

| Página | Hook |
|---|---|
| [[wiki/concepts/story-points]] | Estimativa relativa de complexidade, não tempo — forçar uma meta de pontos de cima para baixo corrompe a métrica |
| [[wiki/concepts/planning-poker]] | Cerimônia de estimativa em time — o valor real está na conversa sobre divergência, não na média |
| [[wiki/concepts/scrum-master]] | Facilita o processo e protege a saúde do time — vira "Agile industrializado" quando só fiscaliza números |
| [[wiki/concepts/goodharts-law]] | "Quando uma medida vira alvo, ela deixa de ser uma boa medida" — mecanismo por trás de métricas forçadas que perdem sentido |

### Documentação Operacional

| Página | Hook |
|---|---|
| [[wiki/concepts/runbook]] | Passos lineares para operações repetíveis — elimina variação humana, reduz MTTR |
| [[wiki/concepts/playbook]] | Árvore de decisão para incidentes com causa desconhecida |
| [[wiki/concepts/post-mortem]] | Análise retrospectiva blameless — 5 Porquês até causa sistêmica, action items com dono e prazo |

## Questions

_(vazio)_
