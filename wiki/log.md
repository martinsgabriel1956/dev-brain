# Wiki Log

---

## [2026-06-26] ingest | The Comparison Trap in Programming Careers

**Source:** [[wiki/sources/the-comparison-trap-in-programming-careers]]
**Skill:** `tech-mentor-leadership` (path `/home/nemomartins/...` não encontrado — skill aplicada por mapeamento de domínio)

**Páginas criadas:**
- `wiki/sources/the-comparison-trap-in-programming-careers.md`
- `wiki/concepts/disciplina-vs-talento.md`

**Páginas atualizadas (backlink + source_count):**
- `wiki/concepts/comparacao-na-carreira.md`
- `wiki/concepts/familiaridade-vs-capacidade.md`
- `wiki/concepts/linha-de-largada.md`
- `wiki/concepts/log-de-aprendizado.md`
- `wiki/concepts/repertorio.md`
- `wiki/concepts/fluencia-vs-perfeicao.md`
- `wiki/concepts/pratica-deliberada.md`

**Notas:** Transcrição de vídeo em português — traduzida e formatada em Markdown antes do ingest. Autora não identificada. Fonte confirma e reforça com narrativa em primeira pessoa conceitos já bem estabelecidos no wiki. Nenhuma contradição. Questão aberta: "vergonha de código antigo como evidência de crescimento" tem nome na literatura? Possível relação com efeito Dunning-Kruger invertido.

---

## [2026-06-26] ingest | 10 Conceitos Fundamentais da Computação

**Source:** [[wiki/sources/10-conceitos-fundamentais-computacao]]
**Skill:** `cs-fundamentals` | Referências: `algorithms-complexity.md`, `data-structures.md`, `compiler-fundamentals.md`, `network-fundamentals.md`, `cryptography-applied.md`, `os-fundamentals.md`, `database-theory.md`

**Páginas criadas:**
- `wiki/sources/10-conceitos-fundamentais-computacao.md`
- `wiki/concepts/logica-booleana.md`
- `wiki/concepts/big-o.md`
- `wiki/concepts/recursao.md`
- `wiki/concepts/concorrencia.md`
- `wiki/concepts/paralelismo.md`
- `wiki/concepts/compilador.md`
- `wiki/concepts/protocolo-de-rede.md`
- `wiki/concepts/criptografia.md`
- `wiki/concepts/lista-encadeada.md`

**Páginas atualizadas (backlink + source_count):**
- `array.md`, `hashmap.md`, `arvore.md`, `thread.md`, `deadlock.md`, `mutex.md`, `abstracao.md`, `acid.md`

**Notas:** Fonte didática sem referências acadêmicas formais. Cobre os 10 conceitos base da CS de forma superficial mas precisa — bom material de ancoragem para tópicos já existentes no wiki. Abstração como meta-conceito unificador é o insight central.

---

## [2026-06-26] ingest | Escalabilidade: Vertical vs Horizontal — System Design

**Source:** [[wiki/sources/escalabilidade-vertical-horizontal-system-design]]
**Skill:** `tech-mentor-system-design` | Referência: `references/system-design.md`

**Páginas criadas:**
- `wiki/sources/escalabilidade-vertical-horizontal-system-design.md`
- `wiki/concepts/escalabilidade-vertical.md`
- `wiki/concepts/stateless.md`
- `wiki/concepts/sticky-session.md`
- `wiki/concepts/cdn.md`
- `wiki/concepts/auto-scaling.md`
- `wiki/concepts/sharding.md`
- `wiki/concepts/replicacao-de-banco.md`
- `wiki/concepts/gargalo.md`
- `wiki/concepts/cap-theorem.md` (stub — necessita fonte dedicada)

**Páginas atualizadas (backlink + source_count):**
- `escalabilidade-horizontal.md`, `load-balancer.md`, `cache.md`

**Notas:** Fonte didática introdutória de System Design — boa para ancoragem de conceitos de escalabilidade. Sharding e CAP Theorem foram criados como stubs; o vídeo os menciona mas não os aprofunda. Open question: fonte dedicada de CAP/PACELC está em falta no wiki.

---

## [2026-06-26] ingest | Como Arquitetar com Cache e Redis

**Source:** [[wiki/sources/como-arquitetar-com-cache-e-redis]]
**Skill:** `tech-mentor-backend` | Referência: `references/redis-advanced.md`

**Páginas criadas:**
- `wiki/sources/como-arquitetar-com-cache-e-redis.md`
- `wiki/concepts/redis.md`
- `wiki/concepts/cache.md`
- `wiki/concepts/cache-aside.md`
- `wiki/concepts/feature-flag.md`
- `wiki/concepts/banco-in-memory.md`
- `wiki/concepts/escalabilidade-horizontal.md`
- `wiki/concepts/tradeoff-de-cache.md`

**Páginas atualizadas:**
- `wiki/concepts/cqrs.md` — seção "Redis como Read Layer" adicionada; source_count 1→2
- `wiki/concepts/nosql.md` — seção de escalabilidade horizontal adicionada; backlink para nova source; source_count 1→2

**Index:** source adicionada + nova seção "Cache & Redis" com 7 conceitos

**Notas:** Transcrição de vídeo em português sobre arquitetura com Redis. Conteúdo cobre fundamentos (NoSQL vs SQL, in-memory, chave-valor), pontos fortes/fracos e três arquiteturas práticas: Feature Flags com batch, Cache-Aside/Flyweight e CQRS com Redis como read layer. Referência `redis-advanced.md` confirmou e enriqueceu os padrões com exemplos de cache stampede, TTL design, write-through e write-behind — esses padrões avançados não estão na fonte, mas foram registrados nas páginas de conceito. **Questões em aberto:** (1) A fonte afirma "segurança limitada" do Redis, mas o Redis 6+ introduziu ACLs granulares — afirmação pode estar desatualizada; (2) A fonte não menciona Memcached como alternativa; (3) A fonte não distingue Cache-Aside do padrão Read-Through — são diferentes mas a fonte usa "Flyweight" como analogia para os dois.

---

## [2026-06-26] ingest | Como Sistemas Operacionais Funcionam por Baixo dos Panos

**Source:** [[wiki/sources/como-sistemas-operacionais-funcionam]]
**Skill:** `cs-fundamentals` | Referência: `references/os-fundamentals.md`

**Páginas criadas:**
- `wiki/sources/como-sistemas-operacionais-funcionam.md`

**Páginas atualizadas (backlink + source_count 1→2):**
- `wiki/concepts/processo.md`
- `wiki/concepts/thread.md`
- `wiki/concepts/deadlock.md`
- `wiki/concepts/mutex.md`
- `wiki/concepts/escalonador.md`
- `wiki/concepts/context-switch.md`
- `wiki/concepts/interrupcao-de-hardware.md`
- `wiki/concepts/memoria-virtual.md`
- `wiki/concepts/swap.md`
- `wiki/concepts/sistema-de-arquivos.md`
- `wiki/concepts/syscall.md`
- `wiki/concepts/kernel.md`

**Index:** source adicionada + nova seção "Fundamentos de Sistemas Operacionais" com 12 conceitos

**Notas:** Transcrição de vídeo em português sobre internals de SO. Os 12 conceitos já existiam no wiki desde 2026-04-22 com referência a `[[sources/sistema-operacional-por-baixo-dos-panos]]` — source que nunca foi criada (link quebrado pré-existente, não corrigido neste ingest). Esta ingest cria a source correta. Questões em aberto: overhead real de context switch com Spectre/Meltdown mitigations; como runtimes como Go e asyncio agendam goroutines/coroutines sobre threads do kernel; o vídeo não cobre io_uring (Linux 5.1+).

---

## [2026-06-20] ingest | 4 Hábitos Ruins de Programador

**Source:** [[wiki/sources/habitos-ruins-de-programador]]
**Skill:** `tech-mentor-leadership` | Referência: `references/software-craftsmanship.md`

**Páginas criadas (sessão anterior — 2026-04-22, sem registro):**
- `wiki/sources/habitos-ruins-de-programador.md`
- `wiki/concepts/dizer-sim-para-tudo.md`
- `wiki/concepts/definicao-de-pronto.md`
- `wiki/concepts/testar-proprio-codigo.md`
- `wiki/concepts/atomic-commits.md`

**Ações desta sessão:**
- `wiki/index.md` — source e 4 conceitos adicionados (seções Sources e Boas Práticas de Engenharia)
- `wiki/log.md` — ingest registrado retroativamente

**Notas:** Transcrição de vídeo comentando artigo "For Web Developers" de "Dano". Framing central: você não *é* um programador ruim, você pode *estar* com hábitos ruins — identidade vs. comportamento. Os 4 hábitos cobrem dimensões complementares: gestão de compromissos (dizer sim para tudo), qualidade de entrega (definição de pronto), robustez de código (testar além do happy path) e colaboração via git (commits atômicos). Questão em aberto: qual tamanho de PR é revisável numa sessão de foco? Como dizer não em culturas de "sempre ajudar"?

---

## [2026-06-20] ingest | Como Aprender Novas Codebases

**Source:** [[wiki/sources/como-aprender-novas-codebases]]
**Skill:** `tech-mentor-leadership` | Referência: `references/onboarding-tecnico.md`

**Páginas criadas:**
- `wiki/sources/como-aprender-novas-codebases.md`
- `wiki/concepts/onboarding-de-codebase.md`
- `wiki/concepts/modelo-mental-de-fluxo-de-dados.md`
- `wiki/concepts/good-first-issue.md`
- `wiki/concepts/entendimento-de-dominio.md`
- `wiki/concepts/testes-como-aprendizado.md`
- `wiki/concepts/ciclo-de-revisita.md`

**Páginas atualizadas (stubs → stable):**
- `wiki/concepts/exploracao-com-intencao.md`
- `wiki/concepts/aprendizado-por-impressoes.md`
- `wiki/concepts/pair-programming.md`
- `wiki/concepts/aprender-ensinando.md`

**Notas:** Transcrição de vídeo em inglês traduzida para PT-BR. Método central: ciclo iterativo de 10 etapas onde a compreensão aprofunda a cada volta. Alinha bem com material já no wiki sobre aprendizado (pratica-deliberada, esforco-produtivo, aprendizado-continuo). A distinção entre exploração com intenção e browse aleatório é o claim mais acionável. Questões abertas: tempo médio para atingir o "ver o código ao usar o app"; como adaptar para solo devs sem pair programming.

---

## [2026-06-11] ingest | Design First vs Code First — Abordagens e Referências de Design

**Source:** [[wiki/sources/design-first-vs-code-first-referencias]]
**Skill:** `tech-mentor-frontend` (skill não encontrado — ingest sem calibração de domínio; marcado para re-ingest quando skill estiver disponível)

**Nota:** Páginas core criadas em sessão anterior (2026-04-22) sem registro no log nem no index. Este entry fecha o ingest e adiciona as páginas que faltavam.

**Páginas criadas (sessão anterior):**
- `wiki/sources/design-first-vs-code-first-referencias.md`
- `wiki/concepts/design-engineer.md`
- `wiki/concepts/design-first.md`
- `wiki/concepts/code-first.md`
- `wiki/concepts/fake-delay.md`
- `wiki/entities/lovable.md`

**Páginas criadas (esta sessão):**
- `wiki/concepts/component-library.md`
- `wiki/concepts/design-como-interacao.md`
- `wiki/entities/pedro-duarte.md`
- `wiki/entities/linear.md`
- `wiki/entities/radix-ui.md`

**Notas:** Fonte é transcrição de vídeo do canal Rocket City. Argumento central: Design Engineer é o cargo que resolve a tensão entre Design First (Figma desatualiza) e Code First (risco de Frankenstein). Design não é estética — é interação, e o Linear é a referência máxima disso. Fake delay é exemplo concreto: 300ms mínimo para feedback visual mesmo em ações instantâneas. Questões abertas: quando o Figma deixa de fazer sentido completamente para um Design Engineer? Como medir qualidade de interação objetivamente?

---

## [2026-06-11] ingest | O Princípio da Inversão Aplicado à Programação

**Source:** [[wiki/sources/principio-da-inversao-programador]]
**Skill:** tech-mentor-leadership (`references/technical-mentoring.md`, `references/career-progression.md`)

**Nota:** Páginas criadas em sessão anterior (2026-04-22) sem registro no log nem no index. Este entry fecha o ingest.

**Páginas criadas (sessão anterior):**
- `wiki/sources/principio-da-inversao-programador.md`
- `wiki/concepts/principio-da-inversao.md`
- `wiki/concepts/dados-vs-intuicao.md`
- `wiki/concepts/complexidade-como-estrategia.md`
- `wiki/concepts/ciclo-da-desgraca-software.md`
- `wiki/concepts/pitfalls-de-linguagem.md`
- `wiki/concepts/maturidade-tecnica.md`
- `wiki/concepts/atualizacao-tecnologica.md`
- `wiki/concepts/tutorial-hell.md`
- `wiki/concepts/aprendizado-deliberado.md`
- `wiki/entities/charlie-munger.md`
- `wiki/entities/karl-gustav-jakob-jacobi.md`
- `wiki/entities/george-hotz.md`

**Notas:** Fonte aplica o modelo mental de inversão (Jacobi/Munger) a 7 hábitos do pior programador. Conclusão central: dados > intuição (HiPPO effect), complexidade intencional é sabotagem, reescrita do zero reproduce o ciclo, e geohot sintetiza o antídoto ao tutorial hell — não há substituto para construir algo. Questões abertas: equilíbrio entre questionar líderes e ser produtivo; como sair do ciclo da desgraça além de refatoração incremental.

---

## [2026-06-11] ingest | Segurança e Armazenamento de Senhas no Banco de Dados

**Source:** [[wiki/sources/seguranca-armazenamento-senhas-banco-de-dados]]
**Skill:** tech-mentor-security (`references/crypto.md`)

**Páginas criadas:**
- `wiki/sources/seguranca-armazenamento-senhas-banco-de-dados.md`
- `wiki/concepts/password-hashing.md`
- `wiki/concepts/argon2.md`
- `wiki/concepts/bcrypt.md`
- `wiki/concepts/salt.md`
- `wiki/concepts/pepper.md`
- `wiki/concepts/rainbow-table.md`
- `wiki/concepts/cpu-hard.md`
- `wiki/concepts/memory-hard.md`
- `wiki/concepts/ataque-pre-computacao.md`
- `wiki/entities/rockyou.md`

**Páginas atualizadas:**
- `wiki/concepts/hashing.md` — seção sobre velocidade como problema, backlinks para salt/rainbow-table/password-hashing
- `wiki/concepts/sql-injection.md` — seção sobre papel histórico no armazenamento de senhas + RockYou
- `wiki/concepts/timing-attack.md` — backlinks para bcrypt/argon2/password-hashing

**Notas:** Fonte é transcrição de vídeo de Renato Augusto cobrindo a evolução histórica do armazenamento de senhas (anos 90 → 2026). Argumento central: entender os fundamentos (paralelismo, núcleos, memória de GPU) é o que diferencia quem configura segurança corretamente de quem usa defaults sem saber se são seguros. Questões abertas: rotação de pepper sem invalidar senhas existentes; memory_cost mínimo recomendado em 2026; viabilidade de migração progressiva de bcrypt para Argon2id.

---

## [2026-06-10] ingest | Cinco Práticas de Segurança do Pragmatic Programmer

**Source:** [[wiki/sources/cinco-praticas-seguranca-pragmatic-programmer]]
**Skill:** tech-mentor-security (ref: secure-design-patterns.md + appsec-owasp.md)
**Páginas criadas:**
- `wiki/sources/cinco-praticas-seguranca-pragmatic-programmer.md`
- `wiki/concepts/principio-do-menor-privilegio.md`
- `wiki/concepts/secure-by-default.md`
- `wiki/concepts/timing-attack.md`
- `wiki/concepts/sql-injection.md`
- `wiki/concepts/sast.md`
- `wiki/concepts/secrets-management.md`
- `wiki/concepts/xss.md`

**Páginas atualizadas:**
- `wiki/concepts/attack-surface.md` — exemplos concretos: S3 público, IDs sequenciais, outputs como vetores (timing), backlink
- `wiki/concepts/defense-in-depth.md` — backlink
- `wiki/concepts/waf.md` — backlink + distinção SAST vs WAF

**Notas:** Vídeo de CTO (não identificado). Framing de dev, não de especialista em segurança. Argumento central: segurança é cultura, não feature — cada dev é responsável. Questão aberta: capítulo exato do Pragmatic Programmer que origina as 5 práticas não citado (provavelmente edição 20th anniversary). XSS criado como stub — mencionado brevemente na fonte.

---

## [2026-06-10] ingest | Como Strings Realmente Funcionam (por Baixo dos Panos)

**Source:** [[wiki/sources/como-strings-realmente-funcionam]]
**Skill:** cs-fundamentals (ref: regex-text-processing.md + number-systems-representation.md)
**Páginas criadas:**
- `wiki/sources/como-strings-realmente-funcionam.md`
- `wiki/concepts/string.md`
- `wiki/concepts/charset.md`
- `wiki/concepts/ascii.md`
- `wiki/concepts/unicode.md`
- `wiki/concepts/utf-8.md`

**Páginas atualizadas:**
- `wiki/concepts/imutabilidade.md` — seção nova sobre imutabilidade de strings (motivação técnica: proteger encoding UTF-8)
- `wiki/concepts/encoding.md` — distinção explícita entre encoding de texto (UTF-8) e encoding de transporte (Base64, URL)

**Notas:** Vídeo YouTube com exemplos em Go. Argumento central: string é slice de bytes; imutabilidade existe para proteger UTF-8 de corrupção por indexação direta. Questão aberta: como o algoritmo UTF-8 usa bits de prefixo para marcar largura do caractere — fonte sugere um vídeo separado sobre isso. Nota: `encoding.md` existente cobria ângulo de segurança (transport encoding); a distinção foi registrada explicitamente no verbete para evitar conflação.

---

## [2026-06-10] ingest | Quanto Tempo Leva para Aprender Programação?

**Source:** [[wiki/sources/quanto-tempo-aprender-programacao]]
**Skill:** tech-mentor-leadership (ref: technical-mentoring.md)
**Páginas criadas:**
- `wiki/sources/quanto-tempo-aprender-programacao.md`
- `wiki/concepts/vale-do-desespero.md`
- `wiki/concepts/pratica-deliberada.md`
- `wiki/concepts/reconhecimento-de-padroes.md`

**Páginas atualizadas:**
- `wiki/concepts/autoconsciencia-de-aprendizado.md` — backlink + ângulo do tempo de aprendizado
- `wiki/concepts/entender-vs-aprender.md` — backlink + vale do desespero como ponto de crise
- `wiki/concepts/fluencia-vs-perfeicao.md` — backlink + fluência como produto de exposição, não aceleração

**Notas:** Vídeo YouTube de autora não identificada. Argumento central: o cérebro aprende padrões (não sintaxe), e esse processo tem um tempo biológico — a única estratégia válida é trocar o foco de prazo para quilometragem. Questão aberta: referência exata da pesquisa com xadrezistas não citada (provável Chase & Simon 1973 ou Ericsson). Range de 800–1.000 horas para júnior sem fonte explícita.

---

## [2026-06-09] ingest | Aprenda antes de aplicar — Fundamentos e Otimização Prematura

**Source:** [[wiki/sources/aprender-antes-de-aplicar-fundamentos-e-otimizacao-prematura]]
**Skill:** tech-mentor-leadership (`references/software-craftsmanship.md`)

**Páginas criadas:**
- `wiki/sources/aprender-antes-de-aplicar-fundamentos-e-otimizacao-prematura.md`
- `wiki/concepts/otimizacao-prematura.md`
- `wiki/concepts/over-engineering.md`
- `wiki/concepts/modelagem-orientada-a-objetos.md`

**Páginas atualizadas:**
- `wiki/concepts/fundacao-tecnica.md` — tabela de progressão de 3 estágios adicionada; link para over-engineering e modelagem OO; source_count 1→2
- `wiki/concepts/design-patterns.md` — seção sobre pré-requisito de modelagem OO; link para over-engineering; source_count 1→2
- `wiki/concepts/logica-de-programacao.md` — referenciado como estágio 1 da progressão incremental; source_count 2→3
- `wiki/index.md` — três novos conceitos na seção "Padrões e Design" + source adicionada

**Notas:** Fonte é transcrição de vídeo de dev brasileiro não identificado. Dois argumentos centrais: (1) a progressão incremental de aprendizado tem 3 estágios que não podem ser pulados — programação/algoritmos → modelagem OO → design patterns/arquitetura; pular leva ao "verde neném" (over-engineering ingênuo); (2) otimização prematura é a raiz de todo mal (Knuth) — refatorar antes de otimizar é sempre a ordem correta. Conexão forte com wiki existente: `fundacao-tecnica` (reforçado com a progressão explícita), `design-patterns` (pré-requisito de modelagem OO era implícito, agora explicitado). Conceito novo mais relevante: `modelagem-orientada-a-objetos` preenchia uma lacuna — estava implícito em várias páginas mas não tinha página própria. Questão aberta: autor não identificado — vídeo parece anterior a 2022.

---

## [2026-06-09] ingest | Construir a coisa que constrói a coisa — O Product Engineer em 2026

**Source:** [[wiki/sources/product-engineer-vale-do-silicio-2026]]
**Skill:** tech-mentor-ai (`references/ai/agentic-patterns-2025.md`)

**Páginas criadas:**
- `wiki/sources/product-engineer-vale-do-silicio-2026.md`
- `wiki/concepts/product-engineer.md`
- `wiki/concepts/taste-dev.md`

**Páginas atualizadas:**
- `wiki/concepts/novo-perfil-dev-ia.md` — Product Engineer é a formalização do conceito; source_count 3→4
- `wiki/concepts/niveis-adocao-ia-l0-l4.md` — L3 na prática: tech lead Databricks + engenheira Cursor com 5 agents simultâneos; source_count 2→3
- `wiki/concepts/harness.md` — harness como trabalho central do Product Engineer; exemplos do Cursor em maturidade; source_count 5→6
- `wiki/concepts/worktree-paralelismo.md` — confirmação de campo: 5 agents simultâneos por feature; source_count 3→4
- `wiki/concepts/spec-driven-development.md` — critério de granularidade de task confirmado em campo; source_count 6→7
- `wiki/entities/valdemar-neto.md` — quarta fonte deste autor; source_count 3→4
- `wiki/index.md` — nova seção "Perfil Profissional & Product Engineering" + source adicionada

**Notas:** Fonte é relato de viagem do Valdemar Neto ao Vale do Silício — conversas com Cursor, Tray, Stripe, Databricks e outras empresas. Conceito central novo: Product Engineer (duas faces inseparáveis: senso de produto + harness). Conceito novo: taste (julgamento estético e de qualidade sem regra explícita). Dado de campo importante: 40–50% dos usuários do Cursor não são devs — builders entregando em produção. As quatro histórias concretas (Databricks, Cursor task decomposition, decisão por dados, incidente com Canvas) são evidências empíricas do L3 em operação que enriquecem diretamente `niveis-adocao-ia-l0-l4`, `spec-driven-development` e `worktree-paralelismo`. Conexão importante: `product-engineer` é a formalização do que `novo-perfil-dev-ia` descrevia de forma mais abstrata — os dois conceitos agora se linkam explicitamente. Questão aberta: o critério de granularidade de task ("menor trabalho que agente consegue fazer sem esbarrar em outro") é aplicável fora de ambientes com MCPs centrais e agents bem configurados?

---

## [2026-06-09] ingest | Você paga 62% a mais usando IA em português

**Source:** [[wiki/sources/custo-tokens-portugues-vs-ingles]]
**Skill:** tech-mentor-ai (`references/ai/token-economics.md`)

**Páginas criadas:**
- `wiki/sources/custo-tokens-portugues-vs-ingles.md`
- `wiki/concepts/token-tax-multilingual.md`
- `wiki/concepts/byte-pair-encoding.md`
- `wiki/entities/pascadev.md`

**Páginas atualizadas:**
- `wiki/concepts/janela-de-contexto.md` — seção sobre idioma afetando consumo da janela; source_count 1→2
- `wiki/concepts/claude-md.md` — seção sobre custo do CLAUDE.md em português; source_count 2→3
- `wiki/concepts/token-anxiety.md` — seção sobre token tax amplificando ansiedade de devs não-anglófonos; source_count 2→3
- `wiki/entities/anthropic.md` — seção sobre tokenizador BPE e token tax; source_count 4→5
- `wiki/index.md` — nova seção "Token Economics & Custo" + source e entity adicionadas

**Notas:** Fonte é transcrição de vídeo do canal PascaDev. Argumento central: a maioria dos devs brasileiros não sabe que escrever em português custa 62% mais tokens do que em inglês no Anthropic. A causa é técnica (BPE treinado em corpus inglês), não intencional. O impacto é concreto: `CLAUDE.md`, specs e prompts em português drenam o context budget 62% mais rápido por sessão. Três estratégias apresentadas — "tudo em inglês", "artefatos em inglês / conversas em português", "ignorar e aceitar". Conexão identificada com token-anxiety (token tax amplifica a ansiedade para devs não-anglófonos) e com claude-md (idioma do arquivo é variável de custo invisível). Questão aberta: o estudo específico citado não foi linkado na transcrição — números plausíveis mas verificar fonte primária antes de usar como referência em contexto formal.

---

## [2026-06-05] ingest | Padrão de Projeto: Proxy

**Source:** [[wiki/sources/design-pattern-proxy]]
**Skill:** tech-mentor-backend (`references/design-patterns.md`)

**Páginas criadas:**
- `wiki/sources/design-pattern-proxy.md` (enriquecimento de stub existente)
- `wiki/entities/renato-augusto.md`

**Páginas atualizadas:**
- `wiki/concepts/proxy-pattern.md` — exemplo concreto de cache proxy adicionado; source_count 1→2
- `wiki/concepts/cache-layer.md` — source adicionada com contexto; source_count 1→2
- `wiki/concepts/decorator-pattern.md` — source_count 1→2
- `wiki/concepts/lazy-initialization.md` — source_count 1→2
- `wiki/index.md` — source e entity adicionadas

**Notas:** Fonte é transcrição de vídeo de Renato Augusto sobre o padrão Proxy GoF. Argumento central: cache não é regra de negócio — pertence ao Proxy, não ao Controller nem à classe de serviço. A source page já existia como stub antecipado; foi enriquecida com Key Claims completas e fluxo de execução. Nenhuma contradição com wiki existente. Questões abertas: Proxy vs. Middleware em frameworks web; teste unitário de proxy com cache.

---

## [2026-06-05] ingest | Aprender a Aprender — Papinho Tech Solo

**Source:** [[wiki/sources/papinho-tech-solo-aprender-a-aprender]]
**Skill:** tech-mentor-leadership (`references/technical-mentoring.md`)

**Páginas criadas:**
- `wiki/sources/papinho-tech-solo-aprender-a-aprender.md`
- `wiki/concepts/entender-vs-aprender.md`
- `wiki/concepts/autoconsciencia-de-aprendizado.md`
- `wiki/entities/linuxtips.md`

**Páginas atualizadas:**
- `wiki/concepts/autodidata.md` — source adicionada; professor não controla aplicação, só o aluno controla
- `wiki/concepts/memoria-muscular.md` — analogias da bicicleta e do bebê adicionadas com link para `entender-vs-aprender`
- `wiki/concepts/aprendizado-passivo.md` — ângulo EAD adicionado; vídeo de qualidade técnica cria ilusão de aprendizado
- `wiki/index.md` — source e entity adicionadas; dois novos conceitos na seção Aprendizado e Mentalidade

**Notas:** Fonte é episódio de podcast gravado em Gramado durante o Gramado Summit. Argumento central: entender e aprender são processos distintos — vídeo produz entendimento, não aprendizado; o EAD amplifica essa confusão. Nenhuma contradição com wiki existente — reforça e complementa páginas já consolidadas como `autodidata`, `aprendizado-passivo` e `memoria-muscular`. Questão aberta: existe pesquisa formal sobre "ilusão de fluência" no EAD?

---

## [2026-06-05] ingest | Padrões Arquiteturais de Segurança: Gatekeeper, Valet Key e Token Relay

**Source:** [[wiki/sources/padroes-arquiteturais-seguranca-gatekeeper-valet-key-token-relay]]
**Skill:** tech-mentor-security (`references/security/secure-design-patterns.md`, `references/appsec-api.md`)

**Páginas criadas:**
- `wiki/sources/padroes-arquiteturais-seguranca-gatekeeper-valet-key-token-relay.md`
- `wiki/concepts/gatekeeper-pattern.md`
- `wiki/concepts/valet-key-pattern.md`
- `wiki/concepts/token-relay-pattern.md`
- `wiki/concepts/attack-surface.md`
- `wiki/concepts/defense-in-depth.md`
- `wiki/concepts/waf.md`
- `wiki/entities/bernardo-lobato.md`

**Páginas atualizadas:**
- `wiki/concepts/media-upload-pattern.md` — adicionado link para `valet-key-pattern` e source
- `wiki/concepts/rate-limiting.md` — adicionada dimensão de segurança e link para `gatekeeper-pattern`
- `wiki/index.md` — nova seção "Segurança de APIs & Arquitetura" + entry na source table + entity

**Notas:** Fonte é transcrição de vídeo do canal de Bernardo Lobato. Argumento central: segurança robusta nasce no design arquitetural, não no código — as três perguntas guias são "por que esse serviço está exposto?", "por que o cliente precisa falar com isso?" e "quem pode entrar por onde?". Conexão identificada com `media-upload-pattern` (presigned URL é implementação do Valet Key). Nenhuma contradição com wiki existente. Questões abertas: Token Relay com tokens opacos vs JWT em múltiplos saltos; Valet Key em cenários multi-tenant.

---

## [2026-06-02] ingest | Formação IA para Devs — MCPs, Plan Mode, Agentes de Planejamento + 5 Principles

**Skills:** `tech-mentor-ai` (aulas MCP, Plan Mode, SDD) · `tech-mentor-leadership` (5 Principles)

**Fontes ingeridas:**
- `raw/Aula 01 - MCPs - Parte 1.md` → [[wiki/sources/formacao-ia-devs-aula-01-mcp-parte1]]
- `raw/Aula 02 - MCPs - Parte 2.md` → [[wiki/sources/formacao-ia-devs-aula-02-mcp-parte2]]
- `raw/Aula 03 - Plan Mode.md` → [[wiki/sources/formacao-ia-devs-aula-03-plan-mode]]
- `raw/Aula 04 - Agentes de Planejamento.md` → [[wiki/sources/formacao-ia-devs-aula-04-agentes-planejamento]]
- `raw/Aula 05 - Q&A.md` → [[wiki/sources/formacao-ia-devs-aula-05-qa]]
- `raw/5-principles-that-changed-me-as-a-programmer.md` → [[wiki/sources/5-principles-that-changed-me-as-a-programmer]]

**Páginas criadas (novas):**

Concepts:
- [[wiki/concepts/model-context-protocol]]
- [[wiki/concepts/mcp-arquitetura]]
- [[wiki/concepts/cli-vs-mcp]]
- [[wiki/concepts/tech-spec]]
- [[wiki/concepts/human-in-the-loop]]
- [[wiki/concepts/task-looper]]
- [[wiki/concepts/agente-prd]]
- [[wiki/concepts/logging-estruturado]]
- [[wiki/concepts/quadrante-de-fowler]]

**Páginas atualizadas:**
- [[wiki/concepts/plan-mode]] — +1 fonte, +seção guideline de granularidade, +seção persistência do plano; source_count 1→2
- [[wiki/concepts/spec-driven-development]] — +2 fontes, +seção fluxo com agentes especializados, +seção onde ficam padrões de arquitetura, +seção quando usar SDD; source_count 4→6
- [[wiki/concepts/prd-product-requirements-document]] — +2 fontes, +seção PRD no contexto de IA; source_count 1→3; status stub→stable
- [[wiki/concepts/sensores-vs-guias]] — +1 fonte; source_count 1→2
- [[wiki/concepts/tech-debt-como-ferramenta]] — +1 fonte; source_count 2→3
- [[wiki/concepts/naming]] — +1 fonte; source_count 2→3

**Notas:** Seis fontes em dois clusters. (1) MCPs e SDD (5 aulas): MCP arquitetura host/client/server explicada em detalhe, decisão CLI vs MCP formalizada, fluxo completo do Spec Driven Development com agentes especializados (PRD→TechSpec→Tarefas), HITL obrigatório em cada etapa, task looper para automação em projetos grandes. Frase central: "PRD não é um documento para a empresa, é um documento para a IA." (2) 5 Principles: cinco lições práticas — logs com contexto, testar o impossível, tech debt deliberado, naming como custo cognitivo, paridade dev-prod. Sem contradições com wiki existente.

---

## [2026-06-02] ingest | Formação IA para Devs — Aulas 01–04 (Partes 2) + 5 Dicas JS

**Fontes:**
- [[wiki/sources/formacao-ia-devs-aula-01-context-harness-engineering]]
- [[wiki/sources/formacao-ia-devs-aula-02-rules]]
- [[wiki/sources/formacao-ia-devs-aula-03-skills]]
- [[wiki/sources/formacao-ia-devs-aula-04-qa]]
- [[wiki/sources/5-dicas-performance-javascript]]

**Skills usadas:** `tech-mentor-ai` (aulas 01–04), `lang-dynamic` (JS performance)

**Páginas criadas (novas):**

Concepts:
- [[wiki/concepts/system-prompt-arquitetura]]
- [[wiki/concepts/sensores-vs-guias]]
- [[wiki/concepts/memoria-curto-longo-prazo-ia]]
- [[wiki/concepts/rules-agente]]
- [[wiki/concepts/skills-agente]]
- [[wiki/concepts/design-md-padrao]]
- [[wiki/concepts/event-loop-performance-js]]

Sources:
- 5 páginas de source (listadas acima)

**Páginas atualizadas:**
- [[wiki/concepts/context-engineering-harness]] — seções de sensores vs guias + rules vs skills adicionadas; source_count 3→6
- [[wiki/concepts/harness]] — seção de duas camadas (provider vs user); source_count 4→5
- [[wiki/concepts/ciclo-agente]] — seção de sensores reduzindo iterações + citação brute-force; source_count 2→3

**Notas:** Aulas são partes 2 das mesmas sessões já ingerias (aula 01 abertura, aula 02 mercado, etc.). Conteúdo central das novas partes: (1) system design ao vivo do harness — guias vs sensores, system prompt architecture, memória curto/longo prazo; (2) rules pattern: agents.md, problema de rules excessivas, simlinks; (3) skills pattern: lazy-loading do front-matter, skills.sh, design.md do Google; (4) Q&A sobre scaffolding, legado e custos. Arquivo de JS performance é fonte independente de Erick Wendel sobre event loop e Web Streams. Contradições: nenhuma nova contra wiki existente.

---

## [2026-06-02] ingest | Formação IA para Devs — Módulo 1 (Aulas 01–06)

**Fontes:**
- [[wiki/sources/formacao-ia-devs-aula-01-abertura]]
- [[wiki/sources/formacao-ia-devs-aula-02-mercado-perfil-profissional]]
- [[wiki/sources/formacao-ia-devs-aula-03-llm]]
- [[wiki/sources/formacao-ia-devs-aula-04-harness]]
- [[wiki/sources/formacao-ia-devs-aula-05-hands-on]]
- [[wiki/sources/formacao-ia-devs-aula-06-qa]]

**Skill usada:** `tech-mentor-ai`

**Páginas criadas (novas):**

Concepts:
- [[wiki/concepts/harness]]
- [[wiki/concepts/niveis-adocao-ia-l0-l4]]
- [[wiki/concepts/tool-call]]
- [[wiki/concepts/degradacao-de-contexto]]
- [[wiki/concepts/reasoning-level]]
- [[wiki/concepts/worktree-paralelismo]]
- [[wiki/concepts/spec-driven-development]]
- [[wiki/concepts/ciclo-agente]]
- [[wiki/concepts/meta-prompting]]
- [[wiki/concepts/xml-markdown-prompts]]
- [[wiki/concepts/novo-perfil-dev-ia]]
- [[wiki/concepts/token-maxing]]
- [[wiki/concepts/modelo-frontier]]
- [[wiki/concepts/context-engineering-harness]]
- [[wiki/concepts/codigo-legado-ia]]
- [[wiki/concepts/mixture-of-experts]]

Entities:
- [[wiki/entities/rodrigo-branas]]
- [[wiki/entities/pedro-nauke]]
- [[wiki/entities/anthropic]]
- [[wiki/entities/codex-openai]]

**Notas:** Transcrições de 6 aulas ao vivo do Módulo 1 da Formação IA para Devs. Conteúdo central: o conceito de harness como evolução do "modelo sozinho", níveis L0–L4 de adoção, spec-driven como abordagem L3, degradação de contexto após 400k tokens, e a evolução prompt→context→harness engineering. Contradições com wiki existente: nenhuma. Contradições internas: Anthropic diz que Opus não degrada; Nauke discorda por experiência prática (flag para verificar com versões 4.x mais novas).

---

## [2026-06-01] ingest | Estruturas de Dados na Prática — Array, Hashmap, Fila, Pilha e Árvore

**Source:** [[wiki/sources/estruturas-de-dados-pratica-array-hashmap-fila-pilha-arvore]]
**Skill:** cs-fundamentals (`references/data-structures.md`)

**Páginas criadas:**
- `wiki/sources/estruturas-de-dados-pratica-array-hashmap-fila-pilha-arvore.md`
- `wiki/concepts/array.md`
- `wiki/concepts/hashmap.md`
- `wiki/concepts/fila.md`
- `wiki/concepts/pilha.md`
- `wiki/concepts/arvore.md`

**Páginas atualizadas:**
- `wiki/concepts/algoritmos-e-estruturas-de-dados.md` — source_count 2→3; seção adicionada com links para os cinco conceitos individuais

**Notas:** Fonte é transcrição de vídeo introdutório de canal parceiro da Rocket City. Argumento central: a escolha de estrutura de dados é uma decisão implícita que a maioria dos devs toma sem perceber — e a escolha errada em escala para o sistema. O ponto mais prático é o framework de três perguntas de decisão (posição vs. identificador / ordem / hierarquia) que cobre a maioria dos casos do dia a dia. As cinco páginas individuais foram criadas como stubs ricos em conteúdo — com complexidade Big-O, analogias, quando usar/não usar, e conexões com sistemas reais. Questão em aberto: o vídeo anuncia continuação sobre Big O notation — ingerir quando disponível para fechar o loop teórico das complexidades mencionadas.

---

## [2026-06-01] ingest | Os 7 Níveis de Como Engenheiros Usam IA

**Source:** [[wiki/sources/escala-niveis-uso-ia-engenheiros]]
**Skill:** tech-mentor-leadership (`references/technical-mentoring.md`, `references/career-progression.md`)

**Páginas criadas:**
- `wiki/sources/escala-niveis-uso-ia-engenheiros.md`
- `wiki/concepts/escala-maturidade-ia-dev.md`
- `wiki/entities/steve-ex-google-amazon.md`

**Páginas atualizadas:**
- `wiki/concepts/era-agentica.md` — seção adicionada conectando os níveis 5–7 como materialização individual da era agêntica
- `wiki/concepts/learning-gap-organizacional.md` — seção adicionada explicando por que estudos de 20–30% medem os níveis errados
- `wiki/concepts/autonomia-tecnica.md` — paradoxo do nível 4: mais delegação exige mais conhecimento de domínio
- `wiki/concepts/dependencia-ia.md` — source_count 1→2; níveis 0–2 como zona de estagnação e dependência
- `wiki/entities/valdemar-neto.md` — source_count 2→3; terceira fonte deste autor

**Notas:** Fonte é transcrição de vídeo do Valdemar Neto — terceira fonte deste autor no wiki. Conceito central criado: escala-maturidade-ia-dev (não existia). Conexão forte com wiki existente: a escala fecha o loop entre era-agentica (macro), learning-gap-organizacional (organizacional) e autonomia-tecnica/dependencia-ia (individual) — agora há um framework que mapeia onde cada dev está. Questão em aberto: o "Steve" que criou o framework não foi identificado pelo sobrenome na fonte — pode ser Steve Yegge (ex-Google, ex-Amazon, conhecido por ensaios sobre engenharia) mas não verificado. O paradoxo central ("mais nível = mais skill, não menos") é uma contradição direta com narrativas de "IA vai substituir devs" — conexão com crenca-de-alta-eficacia e dependencia-ia.

---

## [2026-06-01] ingest | Context Engineering para Codebases Grandes — Progressive Disclosure, On-Demand Loading e o Workflow RPI

**Source:** [[wiki/sources/context-engineering-codebases-grandes-rpi]]
**Skill:** tech-mentor-ai (`references/ai/context-engineering.md`, `references/ai/agents-core.md`)

**Páginas criadas:**
- `wiki/sources/context-engineering-codebases-grandes-rpi.md`
- `wiki/concepts/progressive-disclosure-ia.md`
- `wiki/concepts/memoria-de-longo-prazo-ia.md`

**Páginas atualizadas:**
- `wiki/concepts/rpi-workflow.md` — source_count 2→3; seções adicionadas sobre memória de longo prazo e progressive disclosure como complementos do RPI
- `wiki/concepts/separacao-de-contextos.md` — source_count 2→3; extensão com memória de longo prazo como ponte entre sessões separadas
- `wiki/concepts/codebase-legibilidade-ia.md` — source_count 2→3; MVC god class como anti-padrão específico; progressive disclosure como mitigação
- `wiki/entities/valdemar-neto.md` — source_count 1→2; segunda fonte deste autor

**Notas:** Fonte é transcrição de vídeo do Valdemar Neto — segunda fonte deste autor no wiki. O conceito de RPI já existia (rpi-workflow.md, separacao-de-contextos.md), então o ingest focou no que era genuinamente novo: progressive disclosure (arquivos por diretório), on-demand loading com Cursor Rules/Skills, e memória de longo prazo para refatorações grandes. Conexão importante: progressive-disclosure-ia + claude-md + instruction-budget formam agora um cluster coerente sobre gestão de contexto no CLAUDE.md — três conceitos que se reforçam mutuamente com dados empíricos (paper de Zurique) e exemplos práticos (este vídeo). O padrão de sub-planos com memória de longo prazo resolve o problema de refatorações que não cabem numa sessão sem estourar a context window.

---

## [2026-06-01] ingest | agents.md e CLAUDE.md Ainda Valem a Pena? O que o Paper de Zurique Realmente Diz

**Source:** [[wiki/sources/agents-md-vale-a-pena-paper-zurique]]
**Skill:** tech-mentor-ai (`references/ai/context-engineering.md`, `references/ai/agents-core.md`)

**Páginas criadas:**
- `wiki/sources/agents-md-vale-a-pena-paper-zurique.md`
- `wiki/entities/valdemar-neto.md`

**Páginas atualizadas:**
- `wiki/concepts/claude-md.md` — source_count 1→2; tabela com dados do paper de Zurique; seção de estratégia enxuto + links adicionada
- `wiki/concepts/instruction-budget.md` — source_count 2→3; evidência empírica do custo (+19–20%) adicionada como validação dos ~150 instruções máx.
- `wiki/concepts/llmops.md` — source_count 2→3; seção sobre gestão de arquivos de contexto como problema de LLMOps

**Notas:** Fonte é análise de vídeo do Valdemar Neto sobre paper da Universidade de Zurique. Argumento central: o paper é real e os números são válidos, mas a métrica usada (testes passaram?) não captura qualidade — então a conclusão "delete o agents.md" é precipitada. A estratégia correta é manter o arquivo mas mantê-lo enxuto com links para arquivos específicos. Conexão forte com wiki existente: instruction-budget (dado empírico agora confirmado por paper), claude-md (estratégia de links reforçada), llmops (custo de arquivos de contexto como trade-off explícito). Furo metodológico registrado: o paper assume que arquivos existentes nos repos foram escritos por humanos — podem ter sido gerados por LLM. Questão em aberto: não existe ainda paper que avalie qualidade de código (segurança, design) além de taxa de sucesso em testes — lacuna importante na literatura.

---

## [2026-06-01] ingest | Let It Crash — Graceful Shutdown com AsyncLocalStorage no Node.js

**Source:** [[wiki/sources/let-it-crash-nodejs-asynclocalstorage]]
**Skill:** tech-mentor-backend (`references/architecture-resilience-patterns.md`, `references/graceful-degradation.md`)

**Páginas criadas:**
- `wiki/sources/let-it-crash-nodejs-asynclocalstorage.md`
- `wiki/concepts/let-it-crash.md`
- `wiki/concepts/graceful-shutdown.md`
- `wiki/concepts/asynclocalstorage.md`
- `wiki/concepts/excecao-vs-erro.md`
- `wiki/entities/eric-lenda.md`

**Páginas atualizadas:**
- `wiki/concepts/robustez-de-sistemas.md` — source_count 1→2; seção adicionada sobre Let it Crash como estratégia de robustez complementar ao harness de qualidade

**Notas:** Fonte é transcrição de vídeo do canal de Eric Lenda sobre sistemas confiáveis em Node.js. Argumento central: exceções imprevisíveis (banco de dados fora, memória esgotada) não devem ser recuperadas — devem desencadear um graceful shutdown e o orquestrador recria instâncias limpas. A implementação sem `try/catch` usa `AsyncLocalStorage` para rastrear o `response` do cliente específico que causou a exceção. Conceitos novos: todos os quatro conceitos criados são novos no wiki. Conexão com wiki existente: robustez-de-sistemas (enriquecida — Let it Crash é a estratégia runtime que complementa o harness de qualidade, que é a estratégia de prevenção). Armadilha documentada: `async` na função de contexto do `AsyncLocalStorage.run()` quebra o rastreamento. Questão em aberto: como combinar Let it Crash com Circuit Breaker — são complementares mas a fonte não explora a interação.

---

## [2026-06-01] ingest | Lógica de Programação — O Que É de Verdade

**Source:** [[wiki/sources/logica-de-programacao-o-que-e-de-verdade]]
**Skill:** tech-mentor-leadership (`references/technical-mentoring.md`, `references/career-progression.md`) + cs-fundamentals (secundário)

**Páginas criadas:**
- `wiki/sources/logica-de-programacao-o-que-e-de-verdade.md`
- `wiki/concepts/repertorio.md`
- `wiki/entities/john-romero.md`
- `wiki/entities/edsger-dijkstra.md`

**Páginas atualizadas:**
- `wiki/concepts/logica-de-programacao.md` — source_count 1→2, status draft→stable; reescrita com os 5 pilares, crítica ao DSA como substituto, "programação = descrição inambígua" (Dijkstra)
- `wiki/concepts/decomposicao-de-problemas.md` — source_count 1→2; novo exemplo com clone de Netflix; conexão com repertório
- `wiki/concepts/algoritmos-e-estruturas-de-dados.md` — source_count 1→2; seção adicionada sobre DSA como parte — não o todo — da lógica
- `wiki/concepts/aprendizado-por-exposicao.md` — source_count 2→3; seção adicionada conectando exposição ativa com construção de repertório
- `wiki/concepts/software-3.md` — source_count 1→2; seção adicionada conectando Dijkstra ("descrever = programar") com o comportamento empírico de LLMs replicando ambiguidades do prompt

**Notas:** Fonte é transcrição de vídeo de canal brasileiro focado em DSA/LeetCode. Argumento central: a pergunta real por trás de "lógica de programação" é "como me torno competente?" e a resposta são 5 pilares — decomposição, pesquisa, repertório, projetos e intuição. Conceito novo central: [[repertorio]] (não existia no wiki). Conexão forte com fontes anteriores: converge com Akita (autodidata, prática) e com ia-e-aprendizado (dependência vs autonomia). Contradição potencial: Akita diz "DSA é a fundação inegociável"; esta fonte diz "DSA é parte pequena do todo" — ambas coexistem se entendidas como: DSA é fundação necessária mas não suficiente. Observação relevante: demonstração empírica com GPT-4.1 confirma argumento de Dijkstra — LLM replica ambiguidades da descrição em português, o que conecta diretamente com software-3.md.

---

## [2026-05-31] ingest | Conteúdo Técnico Não Rende Mais — O que Isso Significa para Devs

**Source:** [[wiki/sources/conteudo-tecnico-ia-robustez-sistemas]]
**Skill:** tech-mentor-backend (`references/software-craftsmanship.md`, `references/architecture-eda-patterns.md`)

**Páginas criadas:**
- `wiki/sources/conteudo-tecnico-ia-robustez-sistemas.md`
- `wiki/concepts/robustez-de-sistemas.md`
- `wiki/concepts/crud-resolvido.md`
- `wiki/concepts/harness-de-qualidade.md`
- `wiki/concepts/pipeline-de-qualidade.md`
- `wiki/concepts/teste-de-mutacao.md`

**Páginas atualizadas:**
- `wiki/concepts/era-agentica.md` — +1 fonte; seção adicionada sobre CRUD resolvido e escassez de sênior
- `wiki/concepts/n-plus-one.md` — +1 fonte; seção adicionada sobre N+1 como erro estrutural típico da IA e mitigação via harness
- `wiki/concepts/tdd.md` — +1 fonte; seção adicionada sobre TDD com IA (mais poderoso e mais necessário)

**Notas:** Fonte é vídeo de canal de tecnologia sobre o domínio de conteúdo de IA e o que isso significa para devs. Argumento central: CRUD está resolvido, porta de entrada do júnior fechou, o diferencial é harness de qualidade + robustez. Conexão forte com ingests anteriores: era-agentica (expandida), learning-gap-organizacional (harness é o que fecha o gap no nível técnico). O conceito de "harness de qualidade" como pipeline determinística (passa/não passa) é paralelo direto ao conceito de "hooks garantidos vs CLAUDE.md" do ingest do Claude Code — mesma lógica: ferramenta > intenção. Questão em aberto: projeção de "80% dos devs vencidos" em 2 anos — verificar.

---

## [2026-05-31] ingest | IA para Empresas — Custo, ROI e Por que Não é uma Bolha

**Source:** [[wiki/sources/ia-custo-roi-bolha-ou-realidade]]
**Skill:** tech-mentor-ai (`references/ai/token-economics.md`, `references/ai/llmops.md`, `references/ai/agents-core.md`)

**Páginas criadas:**
- `wiki/sources/ia-custo-roi-bolha-ou-realidade.md`
- `wiki/concepts/ai-washing.md`
- `wiki/concepts/paradoxo-de-jevons.md`
- `wiki/concepts/roi-de-ia.md`
- `wiki/concepts/era-agentica.md`
- `wiki/concepts/learning-gap-organizacional.md`

**Páginas atualizadas:**
- `wiki/concepts/token-anxiety.md` — source_count 1→2; seção adicionada sobre token anxiety no nível organizacional (Uber, Microsoft); conexão com paradoxo de Jevons e era agêntica
- `wiki/concepts/llmops.md` — source_count 1→2; seção adicionada conectando LLMOps a ROI organizacional, learning gap e AI washing
- `wiki/concepts/agente-ia.md` — tags atualizados (via era-agentica)

**Notas:** Fonte é transcrição de vídeo de análise crítica com dados sobre custo e ROI de IA em empresas. Tese central: não é bolha — é curva de adoção que a maioria está subindo errado. Três fontes independentes convergem (Writer 29%, MIT 5%, Mercer 27%) — cada uma com critério diferente, todas apontando o mesmo buraco. Conceito central novo: learning gap organizacional (MIT) como diagnóstico do problema. Conexão cruzada importante: o paradoxo de Jevons explica por que o custo por dev aumenta mesmo com tokens mais baratos; esse fenômeno agrava o token-anxiety existente no wiki. Questões em aberto: projeção de 24x de Goldman Sachs é estimativa — verificar dados reais em 2027/2028; a queda de ação do GitLab (8%) indica que o mercado está mudando de postura sobre AI washing — acompanhar.

---

## [2026-05-31] ingest | O Profissional do Futuro — IA, Identidade e Aprendizado

**Source:** [[wiki/sources/profissional-do-futuro-ia-identidade-aprendizado]]
**Skill:** tech-mentor-leadership (`references/technical-mentoring.md`, `references/career-progression.md`)

**Páginas criadas:**
- `wiki/sources/profissional-do-futuro-ia-identidade-aprendizado.md`
- `wiki/concepts/nexialista.md`
- `wiki/concepts/crenca-de-alta-eficacia.md`
- `wiki/concepts/aprender-a-aprender.md`
- `wiki/concepts/zona-de-desconforto-da-aprendizagem.md`
- `wiki/concepts/observador-tercerático.md`
- `wiki/entities/luiz-tibirica.md`

**Páginas atualizadas:**
- `wiki/concepts/adaptabilidade.md` — source_count 1→2; seção adicionada conectando nexialista, aprender-a-aprender e crença de alta eficácia
- `wiki/concepts/aprendizado-continuo.md` — source_count 1→2; distinção aprendizado contínuo vs. aprender-a-aprender
- `wiki/concepts/aprendizado-passivo.md` — source_count 1→2; estatística de queda de 17% (Anthropic); conexão com crença de alta eficácia

**Notas:** Fonte é transcrição de conversa/podcast entre Luiz Tibiriçá (growth hacker, 42 anos em bancos), Débora (educação/cognição) e Ronald (host). Teses centrais: (1) IA zerou o game de acesso — diferencial agora é aprender-a-aprender; (2) profissional que teme substituição tem baixa crença de eficácia e pode de fato ser substituído; (3) implementar IA sem organizar dados/processos primeiro é fracasso garantido. Conceito original de Luiz: Observador Tercerático (status draft — sem respaldo acadêmico ainda). Conexão forte com ingest anterior (ia-e-aprendizado-programacao-iniciantes): ambos convergem que o risco é o aprendizado passivo, não a IA em si. Questão em aberto: a queda de 17% citada (artigo Anthropic) não tem link — verificar antes de usar como referência.

---

## [2026-05-31] ingest | IA e Aprendizado de Programação — Como Usar sem Parar de Aprender

**Source:** [[wiki/sources/ia-e-aprendizado-programacao-iniciantes]]
**Skill:** tech-mentor-leadership (`references/technical-mentoring.md`, `references/career-progression.md`)

**Páginas criadas:**
- `wiki/sources/ia-e-aprendizado-programacao-iniciantes.md`
- `wiki/concepts/aprendizado-passivo.md`
- `wiki/concepts/dependencia-ia.md`
- `wiki/concepts/autonomia-tecnica.md`
- `wiki/concepts/esforco-produtivo.md`

**Páginas atualizadas:**
- `wiki/concepts/autodidata.md` — source_count 1→2; seção adicionada sobre relação com IA e dependência; conexão com autonomia-tecnica
- `wiki/concepts/aprendizado-por-exposicao.md` — source_count 1→2; distinção crítica entre exposição ativa e cópia passiva com IA
- `wiki/concepts/fluencia-vs-perfeicao.md` — +1 fonte; seção adicionada conectando esforço produtivo com busca prematura de perfeição via IA

**Notas:** Fonte é transcrição de vídeo de programadora brasileira sobre uso de IA por iniciantes. Argumento central: o risco não é a IA em si, é o aprendizado passivo que ela facilita. Dois perfis distintos (criador não-técnico vs. profissional de dev); dois extremos igualmente errados ("proibir IA" vs. "não precisa mais estudar"). A regra de ouro: se não consegue explicar o código, o conhecimento não é seu. Conexão forte com Akita (autodidata, exposição ativa, fluência) — os dois vídeos se reforçam: Akita diz "não fique copiando código de tutorial", este diz "não terceirize o raciocínio pra IA". Questão em aberto: onde está a linha entre esforço produtivo e bloqueio improdutivo? A fonte não define um critério objetivo de tempo.

---

## [2026-05-31] ingest | Claude Code — Guia Prático (Full Cycle)

**Source:** [[wiki/sources/claude-code-guia-pratico-full-cycle]]
**Skill:** tech-mentor-ai (`references/ai/mcp.md`, `references/ai/agents-core.md`, `references/ai/context-engineering.md`)

**Páginas criadas:**
- `wiki/sources/claude-code-guia-pratico-full-cycle.md`
- `wiki/concepts/claude-md.md`
- `wiki/concepts/hooks-agente.md`
- `wiki/concepts/plan-mode.md`
- `wiki/concepts/slash-commands-agente.md`
- `wiki/concepts/context-compaction.md`
- `wiki/concepts/mcp-server.md`

**Páginas atualizadas:**
- `wiki/entities/claude-code.md` — source_count 1→2, status stub→stable; reescrita com tabela de recursos, planos, comandos essenciais e integração IDE
- `wiki/concepts/context-window.md` — source_count 1→2; seção adicionada sobre gestão de contexto em agentes e compactação
- `wiki/concepts/agente-ia.md` — source_count 1→2; seção adicionada com Claude Code como exemplo concreto de agente

**Notas:** Fonte é transcrição de vídeo do canal Full Cycle sobre Claude Code CLI. Argumento central: Claude Code é um agente CLI que integra com IDEs via extensão; o diferencial está em dominar CLAUDE.md, hooks e commands para criar workflows reproduzíveis e consistentes. Distinção crítica documentada: CLAUDE.md é guideline (o LLM pode ignorar), hooks são garantidos pelo runtime. Armadilha de custo: usar API Key diretamente pode custar centenas de dólares — sempre usar plano de assinatura. Conexão com wiki existente: context-window (enriquecida com compactação), agente-ia (Claude Code como exemplo concreto), token-anxiety (compactação como catalisador). Questão em aberto: qual a combinação ideal de Plan Mode + Commands + Hooks para diferentes tipos de tarefa (features novas vs bug fixes vs refactoring)?

---

## [2026-05-31] ingest | Por que o Nubank Escolheu Clojure e Datomic

**Source:** [[wiki/sources/nubank-clojure-datomic-event-sourcing]]
**Skill:** tech-mentor-backend (`references/event-sourcing-cqrs.md`, `references/fintech.md`)

**Páginas criadas:**
- `wiki/sources/nubank-clojure-datomic-event-sourcing.md`
- `wiki/concepts/event-sourcing.md`
- `wiki/concepts/cqrs.md`
- `wiki/concepts/programacao-funcional.md`
- `wiki/concepts/efeitos-colaterais.md`
- `wiki/concepts/ddd.md`
- `wiki/concepts/complexidade-acidental.md`
- `wiki/concepts/datomic.md`
- `wiki/concepts/ledger-imutavel.md`
- `wiki/entities/nubank.md`
- `wiki/entities/clojure.md`
- `wiki/entities/rich-hickey.md`

**Páginas atualizadas:**
- `wiki/concepts/imutabilidade.md` — source_count 1→2, status stub→stable; seções adicionadas: sistemas financeiros, event sourcing, programação funcional, out of the tar pit

**Notas:** Fonte é transcrição de vídeo do canal Nova Devs analisando decisões técnicas fundacionais do Nubank. Argumento central: o CTO do Nubank baseou as escolhas de Clojure + Datomic + Event Sourcing no paper "Out of the Tar Pit" (Moseley & Marks), que identifica mutabilidade e efeitos colaterais como fontes principais de complexidade acidental em sistemas grandes. A combinação funcional + imutável + event-sourced permite que o codebase "envelheça como vinho" em vez de "leite". Conexão com wiki existente: imutabilidade (conceito já existia como stub, promovido para stable). Questões em aberto: como o Nubank faz onboarding de novos engenheiros para uma stack de Clojure/Event Sourcing de alta complexidade? Clojure é linguagem de nicho — como lidar com contratação em escala?

---

## [2026-05-19] ingest | Soft Skills que Realmente Fazem Diferença na Carreira em Tecnologia

**Source:** [[wiki/sources/soft-skills-carreira-tecnologia-eduarda]]
**Skill:** tech-mentor-leadership (`references/career-progression.md`)

**Páginas criadas:**
- `wiki/sources/soft-skills-carreira-tecnologia-eduarda.md`
- `wiki/concepts/soft-skills.md`
- `wiki/concepts/colaboracao-times.md`
- `wiki/concepts/autonomia-responsabilidade.md`
- `wiki/concepts/pensamento-critico.md`
- `wiki/concepts/aprendizado-continuo.md`
- `wiki/concepts/adaptabilidade.md`
- `wiki/concepts/inteligencia-emocional.md`
- `wiki/entities/eduarda-rocket-city.md`

**Páginas atualizadas:**
- `wiki/concepts/comunicacao-tecnica.md` — +1 fonte (página já existia de ingest anterior); backlink adicionado
- `wiki/concepts/burnout-dev.md` — +1 fonte; inteligência emocional como proteção contra burnout
- `wiki/concepts/autodidata.md` — +1 fonte; conexão com aprendizado-continuo

**Notas:** Fonte é transcrição de vídeo do canal Rocket City. Argumento central: hard skills são o piso mínimo, soft skills são o multiplicador. As seis alavancas — comunicação, colaboração, autonomia, pensamento crítico, aprendizado contínuo e inteligência emocional/adaptabilidade — separam executor de solucionador e determinam quem constrói cultura vs. quem apenas entrega código. Conexão importante com wiki existente: aprendizado contínuo é a versão carreira do autodidata (Akita); inteligência emocional é a defesa direta contra burnout (token anxiety). Questões em aberto: soft skills são treináveis deliberadamente? Como medi-las? Em contextos com agentes de IA, qual soft skill se torna mais crítica?

---

## [2026-05-18] ingest | Token Anxiety — Como os Agentes de IA Estão Mudando o Comportamento dos Devs

**Source:** [[wiki/sources/token-anxiety-agentes-ia-comportamento-devs]]
**Skill:** tech-mentor-ai (domínio: LLMs, agentes, LLMOps, comportamento)

**Páginas criadas:**
- `wiki/sources/token-anxiety-agentes-ia-comportamento-devs.md`
- `wiki/concepts/token-anxiety.md`
- `wiki/concepts/agente-ia.md`
- `wiki/concepts/janela-de-contexto.md`
- `wiki/concepts/fomo-tecnologico.md`
- `wiki/concepts/burnout-dev.md`
- `wiki/concepts/dopamina-produtividade.md`
- `wiki/concepts/llmops.md`
- `wiki/entities/nikon-cotaro.md`
- `wiki/entities/claude-code.md`

**Notas:** Fonte é transcrição de vídeo brasileiro comentando o artigo *Token Anxiety* de Nikon Cotaro (fev/2025). Argumento central: ferramentas de agentes com janela de tokens finita (ex.: Claude Code com reset 3–5h) estão criando um novo padrão de ansiedade que distorce comportamentos sociais, rotinas e prioridades de desenvolvedores. O fenômeno amplifica FOMO (mais capacidade = mais ansiedade, não menos) e torna a linha entre ownership saudável e burnout mais tênue para todos — não apenas seniores. Camada brasileira: dev que compete no mercado internacional sente urgência amplificada. Questões em aberto: o fenômeno chegou massivamente ao Brasil? Pricing diferenciado por horário é real? Como diferenciar operacionalmente ownership saudável de token anxiety patológica?

---

## [2026-05-17] ingest | Chain-of-Thought Prompting Elicits Reasoning in Large Language Models

**Source:** [[wiki/sources/chain-of-thought-prompting]]
**Skill:** tech-mentor-ai (`references/ai/prompt-engineering.md`)

**Páginas criadas:**
- `wiki/sources/chain-of-thought-prompting.md`
- `wiki/concepts/emergent-ability.md` (novo conceito)
- `wiki/entities/jason-wei.md` (nova entidade)

**Páginas atualizadas:**
- `wiki/concepts/chain-of-thought.md` — source_count 1→2, major update com resultados empíricos, ablações e condições de uso
- `wiki/concepts/few-shot-learning.md` — source_count 2→3, seção Few-Shot CoT adicionada
- `wiki/concepts/in-context-learning.md` — source_count 2→3, backlink adicionado
- `wiki/concepts/scaling-laws.md` — source_count 1→2, seção de limites expandida com emergent abilities
- `wiki/concepts/prompt-engineering.md` — source_count 1→2, backlink adicionado
- `wiki/concepts/fine-tuning.md` — source_count 2→3, seção CoT vs Fine-Tuning adicionada

**Notas:** Paper seminal de Wei et al. (Google Brain, 2022). Argumento central: fornecer exemplares few-shot com passos de raciocínio intermediários (chain-of-thought) desbloqueia capacidades de raciocínio complexo em LLMs grandes — sem fine-tuning. Resultado mais impactante: PaLM 540B com 8 exemplares supera GPT-3 fine-tuned com verificador no GSM8K (~57% vs ~35%). Chain-of-thought é uma propriedade emergente que só aparece em modelos ~100B+. Questões em aberto: (1) o que exatamente no pré-treino causa a emergência do CoT nessa escala? (2) reasoning models (o1/o3/Claude extended thinking) internalizam CoT no treinamento — qual a relação com CoT prompting explícito? (3) CoT pode ser destilado para modelos menores via rationale distillation?

---

## [2026-05-17] ingest | Microsoft Prompt Engineering Guide

**Source:** [[wiki/sources/microsoft-prompt-engineering-guide]]
**Skill:** tech-mentor-ai (`references/ai/prompt-engineering.md`)

**Páginas criadas:**
- `wiki/sources/microsoft-prompt-engineering-guide.md`
- `wiki/concepts/prompt-engineering.md`
- `wiki/concepts/completion.md`
- `wiki/concepts/zero-shot-learning.md`
- `wiki/concepts/chain-of-thought.md`
- `wiki/concepts/context-window.md`
- `wiki/concepts/hyperparameters-llm.md`
- `wiki/concepts/software-3.md`

**Páginas atualizadas:**
- `wiki/concepts/few-shot-learning.md` — source_count 1→2, backlink adicionado
- `wiki/concepts/fine-tuning.md` — source_count 1→2, backlink adicionado
- `wiki/concepts/in-context-learning.md` — source_count 1→2, backlink adicionado
- `wiki/entities/openai.md` — source_count 1→2, Codex adicionado, backlink adicionado

**Notas:** Guia prático da Microsoft (2022) sobre prompt engineering com Codex. Argumento central: a qualidade das completions depende diretamente da construção do prompt. Quatro padrões: Tell It (instrução de alto nível), Show It (few-shot), Describe It (APIs desconhecidas), Remind It (histórico conversacional). Karpathy cunha "Software 3.0" — prompts como a terceira geração de programação. Questões em aberto: o guia foi escrito pré-reasoning models (o1/o3/Claude extended thinking) — como esses paradigmas se relacionam com CoT explícito? Com LoRA/QLoRA, a hierarquia "few-shot antes de fine-tuning" ainda se sustenta da mesma forma?

---

## [2026-05-17] ingest | Language Models are Few-Shot Learners (GPT-3)

**Source:** [[wiki/sources/gpt3-language-models-are-few-shot-learners]]
**Skill:** tech-mentor-ai (`references/ai/prompt-engineering.md` + `references/ai/fundamentals.md`)

**Páginas criadas:**
- `wiki/sources/gpt3-language-models-are-few-shot-learners.md`
- `wiki/concepts/in-context-learning.md`
- `wiki/concepts/few-shot-learning.md`
- `wiki/concepts/scaling-laws.md`
- `wiki/concepts/data-contamination.md`
- `wiki/concepts/foundation-model.md`
- `wiki/concepts/autoregressive-language-model.md`
- `wiki/concepts/fine-tuning.md`
- `wiki/entities/openai.md`

**Notas:** Paper seminal do GPT-3 (Brown et al., 2020). Argumento central: modelos maiores são meta-aprendizes melhores — aprendem tarefas via exemplos no contexto sem atualizar pesos (in-context learning). Few-shot sem fine-tuning supera SOTA fine-tuned em TriviaQA e PIQA. Questões em aberto: ICL é aprendizado genuíno ou recuperação de padrões do pré-treino? Até onde as scaling laws se sustentam? Como medir data contamination em modelos que não publicam dados de treino?

---

## [2026-05-17] ingest | Batch — Documentação Técnica e Operacional (10 fontes)

**Skills:** tech-mentor-system-design · tech-mentor-infra · tech-mentor-leadership

**Fontes ingeridas:**
- `raw/architecture-decision-record.md` → [[wiki/sources/architecture-decision-record]]
- `raw/request-for-comments.md` → [[wiki/sources/request-for-comments]]
- `raw/high-level-design.md` → [[wiki/sources/high-level-design]]
- `raw/low-level-design.md` → [[wiki/sources/low-level-design]]
- `raw/prd.md` → [[wiki/sources/prd]]
- `raw/frd.md` → [[wiki/sources/frd]]
- `raw/user-stories.md` → [[wiki/sources/user-stories]]
- `raw/runbook.md` → [[wiki/sources/runbook]]
- `raw/playbook.md` → [[wiki/sources/playbook]]
- `raw/post-mortem.md` → [[wiki/sources/post-mortem]]

**Páginas criadas:**
- `wiki/concepts/frd-functional-requirements-document.md`
- `wiki/concepts/high-level-design.md`
- `wiki/concepts/low-level-design.md`
- `wiki/concepts/playbook.md`
- `wiki/concepts/post-mortem.md`
- `wiki/concepts/user-stories.md`
- `wiki/concepts/runbook.md` (atualizado — +1 fonte, +seção pré-requisitos/rollback)

**Notas:** Batch de notas próprias do tech-mentor. Dois clusters principais: (1) documentação arquitetural e de produto — hierarquia PRD→FRD→TRD, HLD→LLD, RFC→ADR com papéis distintos e complementares; (2) documentação operacional — tríade runbook (execução)/playbook (investigação)/post-mortem (retrospectiva). Questão aberta: como o LLD se relaciona com o FRD em projetos onde produto e engenharia fazem as duas coisas?

---

## [2026-05-17] ingest | TRD — Technical Requirements Document

**Source:** [[wiki/sources/trd-technical-requirements-document]]
**Skill:** tech-mentor-system-design (`references/c4-adr.md`)

**Páginas criadas:**
- `wiki/sources/trd-technical-requirements-document.md`
- `wiki/concepts/trd-technical-requirements-document.md`
- `wiki/concepts/prd-product-requirements-document.md` (stub)
- `wiki/concepts/brd-business-requirements-document.md` (stub)
- `wiki/concepts/rfc-request-for-comments.md` (stub)
- `wiki/concepts/adr-architecture-decision-record.md` (stub)

**Notas:** Fonte é nota própria sobre documentação técnica. Argumento central: TRD é o elo entre produto e implementação — responde "como" depois que PRD respondeu "o quê". Conceito chave: distinção TRD (especificação) vs RFC (proposta aberta) vs ADR (decisão registrada). Nenhuma contradição com wiki existente. Questão aberta: quando o TRD se sobrepõe funcionalmente com o ADR em times menores?

**Nota:** `raw/akita-como-aprender-programacao.md` estava listado como untracked pelo git mas já foi ingerido em 2026-05-16 — sem re-ingest necessário.

---

## [2026-05-16] ingest | Como Aprender Programação — Fábio Akita

**Source:** [[wiki/sources/akita-como-aprender-programacao]]
**Skill:** tech-mentor-leadership (`references/technical-mentoring.md`)

**Páginas criadas:**
- `wiki/sources/akita-como-aprender-programacao.md`
- `wiki/concepts/autodidata.md`
- `wiki/concepts/aprendizado-por-exposicao.md`
- `wiki/concepts/memoria-muscular.md`
- `wiki/concepts/pattern-recognition.md`
- `wiki/concepts/anti-pattern.md`
- `wiki/concepts/design-patterns.md`
- `wiki/concepts/algoritmos-e-estruturas-de-dados.md`
- `wiki/concepts/fundacao-tecnica.md`
- `wiki/concepts/fluencia-vs-perfeicao.md`
- `wiki/concepts/hacker-mindset.md`
- `wiki/concepts/foco-profundo.md`
- `wiki/entities/fabio-akita.md`
- `wiki/entities/christopher-alexander.md`

**Notas:** Fonte é transcrição de vídeo do canal Akita On Rails. Argumento central: autodidata vs. passivo é a variável que determina quem aprende, não a qualidade do curso. Contradição potencial com wiki existente: nenhuma. Questão aberta: é possível desenvolver a postura autodidata deliberadamente, ou ela é formada na infância?

---

## [2026-05-13] ingest | Lógica de Programação: Como Qualquer Problema Vira Código

**Source:** [[wiki/sources/logica-de-programacao-quatro-passos]]
**Skill:** cs-fundamentals
**Páginas criadas:**
- `wiki/sources/logica-de-programacao-quatro-passos.md`
- `wiki/concepts/logica-de-programacao.md`
- `wiki/concepts/decomposicao-de-problemas.md`
- `wiki/concepts/separacao-de-responsabilidades.md`
- `wiki/concepts/fluxo-logico.md`
- `wiki/concepts/fluxo-de-controle.md`
- `wiki/concepts/traducao-logica-para-codigo.md`
- `wiki/concepts/estado.md`
- `wiki/concepts/caminho-feliz.md`
- `wiki/concepts/edge-case.md`

**Notas:** Vídeo introdutório de lógica de programação usando caixa eletrônico como exemplo central. Anuncia próxima fonte sobre estruturas de dados. Nenhuma contradição (wiki iniciado neste ingest).
