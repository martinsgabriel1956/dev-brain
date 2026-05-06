# Log de Ingest

Registro cronológico de todas as operações no wiki.

## [2026-05-06] ingest | IAM Introduction — Users, Groups, Policies

- **Source:** [[sources/iam-introduction-users-groups-policies]]
- **Skill:** tech-mentor-infra (referência: `references/cloud/aws.md`)
- **Páginas criadas:**
  - `sources/iam-introduction-users-groups-policies.md`
  - `concepts/aws-iam.md`
  - `concepts/principio-menor-privilegio.md`
- **Páginas atualizadas:**
  - `entities/amazon-web-services.md` — adicionada seção IAM
  - `wiki/index.md` — nova entrada IAM
- **Notas:** Aula 01 de módulo IAM. Conceitos fundamentais: usuários, grupos (não aninhados), policies JSON, princípio do menor privilégio. Questões em aberto: diferença IAM Roles vs Users para workloads, integração com AWS Organizations, SCPs.

## [2026-05-06] ingest | Infraestrutura Global da AWS

- **Source:** [[sources/aws-infraestrutura-global]]
- **Skill:** tech-mentor-infra (referência: `references/cloud/aws.md`)
- **Páginas criadas:**
  - `sources/aws-infraestrutura-global.md`
  - `concepts/regiao-aws.md`
  - `concepts/zona-de-disponibilidade.md`
  - `concepts/zona-local-aws.md`
  - `concepts/aws-wavelength.md`
  - `concepts/aws-outposts.md`
  - `concepts/zona-local-dedicada.md`
  - `concepts/aws-cloudfront.md`
  - `concepts/backbone-de-rede-aws.md`
  - `concepts/soberania-digital.md`
  - `concepts/alta-disponibilidade.md`
  - `entities/amazon-web-services.md`
- **Notas:** Primeira ingest de infraestrutura de cloud. Números-chave: 39 regiões, 123 AZs, 750+ POPs CloudFront, backbone de 9M km de fibra. Questões em aberto: SLA por região, conformidade LGPD certificada, latência backbone AWS vs internet pública Brasil→EUA.

## [2026-05-05] ingest | Compliance — Fundamentos para Engenheiros

**Source:** [[sources/compliance]]
**Raw file:** `raw/compliance.md`
**Skill:** `tech-mentor-security`

**Páginas criadas (sources):**
- `wiki/sources/compliance.md`

**Páginas criadas (concepts):**
- `wiki/concepts/compliance.md` — stable; compliance vs security, 5 frameworks, 3 cenários de engenharia (data residency, audit log, DSAR)
- `wiki/concepts/audit-log.md` — stable; schema mínimo, satisfaz SOC2/PCI/ISO27001/LGPD simultaneamente
- `wiki/concepts/data-residency.md` — stub; restrição geográfica de dados → muda topologia multi-region
- `wiki/concepts/dsar.md` — stub; deleção em cascata em DB + Redis + S3 + backups

**Páginas atualizadas (backlink adicionado):**
- `wiki/sources/lgpd-gdpr.md` — backlink para [[sources/compliance]]
- `wiki/sources/compliance-soc2-pci.md` — backlink para [[sources/compliance]]

**Notas:** Fonte interna (tech-mentor skill). Distinção central: compliance = prova documentada ≠ segurança = estado real. Do ponto de vista de engenharia, compliance vira problema arquitetural em 3 cenários concretos: data residency (muda topologia), audit log (muda schema/fluxo de escrita), DSAR (exige mapa de todos os stores de dados do usuário). Audit log estruturado é evidência reutilizável para múltiplos frameworks — uma única tabela satisfaz SOC2 CC7.2, PCI-DSS Req 10, ISO 27001 A.12.4 e LGPD Art. 37.

**Questões em aberto:**
- Como implementar data residency em multi-tenant SaaS sem multiplicar custo de infra?
- Qual a estratégia de backup que satisfaz LGPD sem impossibilitar restore?

---

## [2026-05-05] ingest | Clusters — Fundamentos

**Source:** [[sources/clusters]]
**Raw file:** `raw/clusters.md`
**Skill:** `tech-mentor-infra`

**Páginas criadas (sources):**
- `wiki/sources/clusters.md`

**Páginas criadas (concepts):**
- `wiki/concepts/cluster.md` — stable; tipo principal de fundamento de sistemas distribuídos; cobre 4 tipos (compute, database, cache, search) com trade-offs
- `wiki/concepts/control-plane.md` — stub; coordinator central; contrasta K8s (centralizado) vs Redis Cluster (gossip, descentralizado)
- `wiki/concepts/redis-cluster.md` — stub; 16.384 hash slots, gossip protocol, limitações de multi-key ops

**Páginas atualizadas (backlink adicionado):**
- `wiki/concepts/load-balancer.md` — source_count 1→2; LB é entry point do cluster
- `wiki/concepts/db-sharding.md` — source_count 1→2; consistent hashing é base do Redis Cluster

**Notas:** Fonte interna (tech-mentor skill). Conceito chave: cada tipo de cluster tem estratégia própria de distribuição de estado — pods por scheduler (K8s), primary/replica (databases), hash slots (Redis), shards (Elasticsearch). O trade-off central é sempre complexidade operacional de estado distribuído vs ganho de capacidade/disponibilidade. `cap-theorem` referenciado mas ainda sem página — candidato para próxima ingestão.

**Questões em aberto:**
- Como funciona resharding em Redis Cluster sem downtime?
- Custo operacional de Postgres + Patroni vs RDS Multi-AZ na prática?

---

## [2026-05-05] ingest | Observer — Padrão de Projeto Comportamental (Refactoring Guru)

**Source:** [[sources/design-pattern-observer]]
**Raw file:** `raw/design-pattern-observer.md`
**URL:** https://refactoring.guru/pt-br/design-patterns/observer
**Skill:** `tech-mentor-backend` — ref `design-patterns.md`

**Páginas criadas (sources):**
- `wiki/sources/design-pattern-observer.md`

**Páginas criadas (concepts):**
- `wiki/concepts/chain-of-responsibility-pattern.md` — stub; base do padrão de middleware HTTP; contraponto ao Observer (sequencial vs broadcast)
- `wiki/concepts/pub-sub.md` — stable; distinção crítica com Observer formalizada (direto vs broker)

**Páginas atualizadas (backlink adicionado):**
- `wiki/concepts/observer-pattern.md` — source_count 1→2
- `wiki/concepts/behavioral-patterns.md` — source_count 2→3
- `wiki/concepts/mediator-pattern.md` — distinção Mediator vs Observer aprofundada; source_count 1→2
- `wiki/concepts/command-pattern.md` — source_count 1→2
- `wiki/concepts/mensageria.md` — Observer vs Pub/Sub como contexto; source_count 1→2

**Notas:** Fonte canônica do Refactoring Guru (PT-BR). Dois insights que faltavam na wiki: (1) distinção formal Observer vs Pub/Sub — Observer é in-process e direto, Pub/Sub usa broker intermediário e permite cross-service; (2) distinção Mediator vs Observer é "bem obscura" segundo o próprio artigo — podem ser usados simultaneamente, e Observer pode implementar Mediator dinamicamente. Ponto prático importante: assinantes são notificados em **ordem aleatória** — se a ordem importa, Observer não é a ferramenta certa sem camada adicional. `pub-sub` criado como stable porque a distinção com Observer é o conceito mais importante e recorrente no contexto de mensageria.

**Questões em aberto:**
- Como garantir ordem de notificação quando ela importa?
- Memory leaks por assinantes não removidos — como gerenciar ciclo de vida?
- Quando usar Observer in-process vs mensageria externa (Kafka, SNS)?

---

## [2026-05-05] ingest | Strategy — Padrão de Projeto Comportamental (Refactoring Guru)

**Source:** [[sources/design-pattern-strategy]]
**Raw file:** `raw/design-pattern-strategy.md`
**URL:** https://refactoring.guru/pt-br/design-patterns/strategy
**Skill:** `tech-mentor-backend` — ref `design-patterns.md`

**Páginas criadas (sources):**
- `wiki/sources/design-pattern-strategy.md`

**Páginas criadas (concepts):**
- `wiki/concepts/template-method-pattern.md` — stub; contraponto direto ao Strategy (herança vs composição)
- `wiki/concepts/state-pattern.md` — stub; estrutura idêntica ao Strategy, intenção diferente
- `wiki/concepts/command-pattern.md` — stub; ambos parametrizam com ação, propósitos distintos
- `wiki/concepts/bridge-pattern.md` — stub; estrutura similar (composição), propósito estrutural

**Páginas atualizadas (backlink adicionado):**
- `wiki/concepts/strategy-pattern.md` — source_count 1→2
- `wiki/concepts/open-closed-principle.md` — source_count 2→3
- `wiki/concepts/behavioral-patterns.md` — source_count 1→2
- `wiki/concepts/decorator-pattern.md` — distinção Decorator vs Strategy; source_count 1→2

**Notas:** Fonte canônica do Refactoring Guru (PT-BR). Insights que faltavam na wiki: (1) o **contexto não sabe qual estratégia está usando** — trabalha apenas pela interface; (2) distinção precisa Strategy vs Template Method: mesmo propósito, mecanismo oposto — herança estática vs composição dinâmica; (3) distinção Strategy vs State: estrutura idêntica, mas State gerencia transições automáticas enquanto Strategy é trocada explicitamente pelo cliente; (4) em linguagens com funções de primeira classe, funções anônimas podem substituir as classes ConcreteStrategy.

**Questões em aberto:**
- Em TypeScript/JS, quando usar classes ConcreteStrategy vs funções de primeira classe?
- Como testar Contexto quando a estratégia tem efeitos colaterais (I/O, rede)?

---

## [2026-05-05] ingest | Facade — Padrão de Projeto Estrutural (Refactoring Guru)

**Source:** [[sources/design-pattern-facade]]
**Raw file:** `raw/design-pattern-facade.md`
**URL:** https://refactoring.guru/pt-br/design-patterns/facade
**Skill:** `tech-mentor-backend` — ref `design-patterns.md`

**Páginas criadas (sources):**
- `wiki/sources/design-pattern-facade.md`

**Páginas criadas (concepts):**
- `wiki/concepts/mediator-pattern.md` — stub; distinção central com Facade documentada
- `wiki/concepts/flyweight-pattern.md` — stub; distinção com Facade (muitos objetos vs um objeto)
- `wiki/concepts/god-object.md` — anti-pattern; risco explícito quando Facade acumula lógica
- `wiki/concepts/abstract-factory.md` — stub; alternativa ao Facade quando a preocupação é criação de objetos

**Páginas atualizadas (backlink adicionado):**
- `wiki/concepts/facade-pattern.md` — source_count 2→3
- `wiki/concepts/adapter-pattern.md` — distinção Facade vs Adapter formalizada; source_count 2→3
- `wiki/concepts/proxy-pattern.md` — relação Facade vs Proxy documentada; source_count 1→2
- `wiki/concepts/singleton-pattern.md` — Facade frequentemente vira Singleton; source_count 1→2

**Notas:** Fonte canônica do Refactoring Guru (PT-BR). Adiciona rigor à definição do Facade — especialmente dois pontos que faltavam na wiki: (1) o subsistema **não está ciente** da fachada, objetos internos se comunicam diretamente entre si; (2) **Fachada Adicional** como solução para evitar que a fachada principal vire God Object. Distinções formalizadas: Facade ≠ Adapter, Facade ≠ Mediator, Facade ≠ Proxy. `god-object` criado como anti-pattern estável — era referenciado em dois sources mas nunca tinha página própria.

**Questões em aberto:**
- Quando faz sentido ter Fachada Adicional vs dividir em múltiplas classes de serviço?
- Como testar uma fachada que inicializa o subsistema internamente (sem DI)?

---

## [2026-05-05] ingest | Sete Padrões de Design de Software

**Source:** [[sources/sete-padroes-de-design-de-software]]
**Raw file:** `raw/sete-padroes-de-design-de-software.md`
**Skill:** `tech-mentor-backend` — ref `design-patterns.md`

**Páginas criadas (sources):**
- `wiki/sources/sete-padroes-de-design-de-software.md`

**Páginas criadas (concepts):**
- `wiki/concepts/singleton-pattern.md`
- `wiki/concepts/builder-pattern.md`
- `wiki/concepts/factory-pattern.md`
- `wiki/concepts/strategy-pattern.md`
- `wiki/concepts/observer-pattern.md`
- `wiki/concepts/gang-of-four.md` (em concepts/ — entity equivalente já existe em entities/)
- `wiki/concepts/creational-patterns.md`
- `wiki/concepts/behavioral-patterns.md`

**Páginas atualizadas (stub → stable):**
- `wiki/concepts/facade-pattern.md` — enriquecido com código, trade-offs, exemplos; source_count 1→2
- `wiki/concepts/adapter-pattern.md` — enriquecido com código, trade-offs, distinção Proxy; source_count 1→2
- `wiki/concepts/open-closed-principle.md` — enriquecido com exemplo Strategy, limitações; source_count 1→2
- `wiki/concepts/structural-patterns.md` — tabela completa dos 7 padrões, distinção de criacionais; source_count 1→2

**Notas:** Transcrição de vídeo EN (canal Forest, YouTube), traduzida e estruturada. Cobre 7 dos 23 padrões GoF com exemplos TypeScript práticos. Claim mais importante: Strategy Pattern como aplicação direta do Open/Closed Principle — a classe consumidora fica intocada, nova estratégia = nova classe. Segundo insight relevante: Singleton é essencialmente uma variável global glorificada — usar apenas quando unicidade é genuinamente necessária. Facade e Observer já existiam como stubs do ingest de Proxy (2026-05-01) — promovidos a stable com conteúdo rico.

**Questões abertas:**
- O source não cobre Decorator, Proxy, Command, Template Method, Chain of Responsibility — todos relevantes segundo a ref `design-patterns.md`.
- Singleton em multi-thread exige double-checked locking — não coberto no vídeo.

---

## [2026-05-04] ingest | Ports and Adapters — Codebase Preparada para IA

**Source:** [[wiki/sources/ports-and-adapters-codebase-para-ia]]
**Raw file:** `raw/ports-and-adapters-codebase-para-ia.md`
**Skill:** `tech-mentor-backend` — ref `architecture-foundations.md`

**Páginas criadas (sources):**
- `wiki/sources/ports-and-adapters-codebase-para-ia.md`

**Páginas criadas (concepts):**
- `wiki/concepts/hexagonal-architecture.md` — resolveu órfão: era referenciado por `sources/hexagonal-architecture.md` desde 2026-04-23 mas nunca criado
- `wiki/concepts/codebase-legibilidade-ia.md` — insight central: legibilidade humana = legibilidade para agentes

**Páginas atualizadas:**
- `wiki/sources/hexagonal-architecture.md` — backlink para novo source
- `wiki/concepts/acoplamento.md` — backlink + source_count implícito

**Notas:** Vídeo PT-BR (autor: Galego). Ângulo principal: a qualidade da codebase importa mais do que o prompt ou o modelo — é o claim mais direto sobre o tema que o wiki tem até agora. O exemplo antes/depois (god class 238 linhas → ports and adapters modular) concretiza o que Navigation Paradox e Addy Osmani descrevem abstratamente. Conceito novo importante: `codebase-legibilidade-ia` como síntese do princípio. Bonus: criado `hexagonal-architecture` concept page que estava faltando desde o batch ingest de 2026-04-23 (era referenciado como wikilink mas nunca escrito).

**Questões abertas:**
- Existe tamanho de módulo "ideal" para agente trabalhar sem abrir outros módulos?
- Como medir ROI do refactor em termos de qualidade de resposta do agente?

---

## [2026-05-04] ingest | Erros do Workflow RPI + Context Engineering Avançado para Coding Agents

**Sources:**
- [[wiki/sources/erros-workflow-research-plan-implement]]
- [[wiki/sources/context-engineering-avancado-para-coding-agents]]

**Raw files:**
- `raw/erros-workflow-research-plan-implement.md`
- `raw/context-engineering-avancado-para-coding-agents.md`

**Skill:** `tech-mentor-ai` — refs `context-engineering.md` + `reasoning-models-2025.md`

**Páginas criadas (sources):**
- `wiki/sources/erros-workflow-research-plan-implement.md`
- `wiki/sources/context-engineering-avancado-para-coding-agents.md`

**Páginas criadas (concepts):**
- `wiki/concepts/rpi-workflow.md`
- `wiki/concepts/instruction-budget.md`
- `wiki/concepts/dumb-zone.md`
- `wiki/concepts/compaction-intencional.md`
- `wiki/concepts/plano-vertical.md`
- `wiki/concepts/design-discussion.md`
- `wiki/concepts/separacao-de-contextos.md`
- `wiki/concepts/mental-alignment.md`

**Páginas atualizadas:**
- `wiki/concepts/vertical-slice-architecture.md` — backlinks + source_count 1→3
- `wiki/concepts/comprehension-debt.md` — backlinks + source_count 1→3

**Notas:** Dois sources complementares sobre o mesmo tema — um em PT-BR (análise dos erros do RPI), outro traduzido do EN (talk do Dex na AI Engineer). Conceito mais importante: **instruction budget** — a maioria dos devs nunca contou quantas instruções o agente está recebendo no total (system prompt + CLAUDE.md + MCPs). O threshold empírico de ~150–200 é fácil de ultrapassar sem perceber. Segundo insight crítico: **dumb zone** a partir de ~40% da context window — MCPs verbosos empurram o agente para essa zona permanentemente. Conexão forte com conceitos já existentes: vertical-slice-architecture (plano vertical é VSA aplicado a workflow), comprehension-debt (não ler o código durante research é o caminho direto para ele).

**Questões abertas:**
- Instruction budget de 150–200 é por conversa ou por turn?
- O threshold de 40% vale para modelos com context window de 1M+ tokens?
- Compaction intencional tem custo de tokens de escrita — qual o break-even?

---

## [2026-05-02] ingest | Como Múltiplas Linguagens Vivem Num Único Binário

**Source:** [[wiki/sources/como-multiplas-linguagens-vivem-num-unico-binario]]
**Raw file:** `raw/como-multiplas-linguagens-vivem-num-unico-binario.md`
**URL:** null (vídeo do canal Core Dumped — George)
**Skill:** `lang-systems` — refs `compiladores-interpretadores.md` + `polyglot-wasm-comparative.md`

**Páginas criadas (sources):**
- `wiki/sources/como-multiplas-linguagens-vivem-num-unico-binario.md`

**Páginas criadas (concepts):**
- `wiki/concepts/pipeline-de-compilacao.md`
- `wiki/concepts/object-file.md`
- `wiki/concepts/static-linking.md`
- `wiki/concepts/dynamic-linking.md`
- `wiki/concepts/toolchain.md`
- `wiki/concepts/abi.md`
- `wiki/concepts/calling-convention.md`
- `wiki/concepts/ffi.md`

**Notas:** Transcrição de vídeo PT-BR (traduzida de EN). Fonte de altíssima qualidade para entender a cadeia compilação→linking→interop. Insight central: o linker é o ponto de encontro entre linguagens — object files são o formato neutro. Dois pontos contra-intuitivos bem explicados: (1) compiladores não geram código de máquina diretamente — passam por assembly; (2) ABI compatibility é necessária além de ter um linker em comum. Conecta com skill `compiladores-interpretadores.md` (pipeline, LLVM IR) e `polyglot-wasm-comparative.md` (interop entre linguagens em produção). Não há contradições com o wiki existente.

**Questões abertas:**
- Próxima parte do vídeo cobre linguagens compiladas + interpretadas — qual é o mecanismo equivalente ao linker nesse caso?
- Como o LLVM IR se encaixa nesse modelo? Seria uma forma de pular a fase de object file?

---

## [2026-05-01] ingest | Pensamento Estruturado para Resolução de Problemas

**Source:** [[wiki/sources/pensamento-estruturado-resolucao-de-problemas]]
**Raw file:** `raw/pensamento-estruturado-resolucao-de-problemas.md`
**URL:** null
**Skill:** `tech-mentor-leadership` (skills path indisponível — ingest sem calibração de referência)

**Páginas criadas (sources):**
- `wiki/sources/pensamento-estruturado-resolucao-de-problemas.md`

**Páginas criadas (concepts):**
- `wiki/concepts/pensamento-estruturado.md`
- `wiki/concepts/arvore-de-decomposicao.md`
- `wiki/concepts/pensamento-regressivo.md`
- `wiki/concepts/causa-raiz.md`
- `wiki/concepts/hipotese-e-validacao.md`

**Páginas atualizadas:**
- `wiki/concepts/decomposicao-de-problemas.md` — backlink + source_count 1→2
- `wiki/concepts/pensamento-sistemico.md` — backlink + source_count 1→2

**Notas:** Transcrição de vídeo PT-BR (canal Faculdade Rocket City, autor não identificado). O método de 5 passos é agnóstico de linguagem e aplicável além de problemas técnicos. Insight central: em nenhum momento você precisa mexer no código para chegar à causa raiz — a decomposição acontece antes. Conexão relevante com IA: pensamento estruturado é o que transforma a IA de geradora de ruído em ferramenta de precisão. Complementa cluster existente de carreira/aprendizado ([[decomposicao-de-problemas]], [[pensamento-sistemico]], [[dados-vs-intuicao]], [[principio-da-inversao]]).

**Questões abertas:**
- Como aplicar a árvore de decomposição em problemas de produto (não só técnicos)?
- Existe um limite de profundidade útil para a decomposição antes de virar análise infinita?

---

## [2026-05-01] ingest | Padrão de Projeto: Proxy

**Source:** [[wiki/sources/design-pattern-proxy]]
**Raw file:** `raw/design-pattern-proxy.md`
**URL:** https://refactoring.guru/pt-br/design-patterns/proxy
**Skill:** `tech-mentor-backend` (skills path indisponível — ingest sem calibração de referência)

**Páginas criadas (sources):**
- `wiki/sources/design-pattern-proxy.md`

**Páginas criadas (concepts):**
- `wiki/concepts/proxy-pattern.md`
- `wiki/concepts/structural-patterns.md`
- `wiki/concepts/cache-layer.md`
- `wiki/concepts/open-closed-principle.md`
- `wiki/concepts/single-responsibility-principle.md`
- `wiki/concepts/liskov-substitution-principle.md`
- `wiki/concepts/decorator-pattern.md`
- `wiki/concepts/facade-pattern.md`
- `wiki/concepts/adapter-pattern.md`
- `wiki/concepts/repository-pattern.md`
- `wiki/concepts/lazy-initialization.md`

**Páginas criadas (entities):**
- `wiki/entities/gang-of-four.md`
- `wiki/entities/refactoring-guru.md`

**Notas:** Transcrição de vídeo PT-BR (autor: Renato Augusto). Padrão mais versátil da categoria estrutural — casos de uso cobrem cache, controle de acesso, log, lazy init, validação. Conceito central: o proxy e o objeto real devem implementar a mesma interface (LSP) para o cliente ser agnóstico. Distinção de Decorator documentada: motivação diferente (controle de acesso vs extensão de comportamento). Princípios SOLID 3 (SRP, OCP, LSP) ancorados com exemplos concretos do mesmo caso prático.

**Questões abertas:**
- Em que momento o Proxy vira over-engineering vs. quando é a solução certa?
- Como testar unitariamente um proxy com cache sem precisar de infra real?

---

## [2026-04-29] ingest | 4 Habits That Make You an Inefficient Developer

**Source:** [[wiki/sources/4-habitos-programador-ineficiente]]  
**Raw file:** `raw/4-habitos-programador-ineficiente.md`  
**URL:** https://medium.com/better-programming/4-habits-that-make-you-an-inefficient-developer-f4384c4b9df5  
**Skill:** tech-mentor-leadership  

**Páginas tocadas:**
- Criada: `wiki/sources/4-habitos-programador-ineficiente.md`
- Atualizada: `wiki/concepts/dizer-sim-para-tudo.md` (source_count 1→2)
- Atualizada: `wiki/concepts/definicao-de-pronto.md` (source_count 1→2)
- Atualizada: `wiki/concepts/testar-proprio-codigo.md` (source_count 2→3)
- Atualizada: `wiki/concepts/atomic-commits.md` (source_count 1→2)

**Notas:** Source complementa ingest anterior (`habitos-ruins-de-programador`, 2026-04-22) — agora com URL primária do artigo original e conteúdo traduzido para EN. Os 4 conceitos centrais já existiam na wiki com backlinks; este ingest reforça a cobertura dessas páginas com a fonte canônica.

---

## [2026-04-29] ingest | Encoding vs Hashing vs Encryption

**Source:** `wiki/sources/encoding-hashing-encryption.md`
**Raw:** `raw/encoding-hashing-encryption.md`
**Skill:** `tech-mentor-security`

**Páginas criadas (sources):**
- `wiki/sources/encoding-hashing-encryption.md`

**Páginas criadas (concepts):**
- `wiki/concepts/encoding.md`
- `wiki/concepts/hashing.md`
- `wiki/concepts/encryption.md`
- `wiki/concepts/caesar-cipher.md`

**Notas:** Source introdutório/didático. Cobre fundamentos com exemplos concretos (URL encoding, WhatsApp E2E, Caesar Cipher). Open question: diferença entre hash de senha (bcrypt/argon2 com salt) vs hash de integridade (SHA-256) não é endereçada pelo source — possível expansão em `hashing.md`.

---

## [2026-04-29] ingest | Over-Engineering: Quando o Código Bonito Vira um Problema

**Source:** `wiki/sources/overengineering-carol-ate-quinta.md`
**Raw:** `raw/overengineering-carol-ate-quinta.md`
**Skill:** `tech-mentor-backend`

**Páginas criadas (sources):**
- `wiki/sources/overengineering-carol-ate-quinta.md`

**Páginas criadas (concepts):**
- `wiki/concepts/over-engineering.md`
- `wiki/concepts/kiss.md`
- `wiki/concepts/ego-driven-development.md`

**Páginas atualizadas (concepts):**
- `wiki/concepts/accidental-complexity.md` — backlink + source_count 1→2
- `wiki/concepts/abstraction-bloat.md` — backlink + source_count 3→4
- `wiki/concepts/abstraction-illusion.md` — backlink + source_count 2→3

**Notas:** Source de vídeo/transcrição PT-BR. Vetor humano (ego + experiência) do mesmo fenômeno que abstraction-bloat documenta para IA. Converge com listen-notes-good-enough-engineering. Tensão produtiva com clean-architecture e solid — padrões corretos, aplicação errada é a fonte do problema.

---

## [2026-04-29] ingest | A Ciência por Trás de Projetos Inacabados

**Source:** `wiki/sources/por-que-devs-nao-terminam-projetos.md`
**Raw:** `raw/por-que-devs-nao-terminam-projetos.md`
**Skill:** `tech-mentor-leadership`

**Páginas criadas (sources):**
- `wiki/sources/por-que-devs-nao-terminam-projetos.md`

**Páginas criadas (concepts):**
- `wiki/concepts/dopamina-e-projetos.md`
- `wiki/concepts/planning-fallacy.md`
- `wiki/concepts/scope-creep.md`
- `wiki/concepts/mvp.md`
- `wiki/concepts/perfeccionismo-em-devs.md`
- `wiki/concepts/paralisia-por-analise.md`
- `wiki/concepts/goal-gradient-effect.md`
- `wiki/concepts/aprendizado-por-luta.md`

**Páginas atualizadas:**
- `wiki/concepts/vibe-coding.md` — backlink + relação com aprendizado-por-luta
- `wiki/concepts/aprendizado-deliberado.md` — backlink + Kolb

**Notas:** Fonte de psicologia aplicada a devs. Conceitos técnicos ausentes no wiki — 8 novos. Open question relevante: onde está a linha entre "bom o suficiente" e tech debt intencional em side projects.

---

## [2026-04-29] ingest | Roadmap Dev Sênior 2026 — 5 Pilares Fundamentais

**Source:** `wiki/sources/roadmap-dev-senior-2026.md`
**Raw:** `raw/roadmap-dev-senior-2026.md`
**Skill:** `tech-mentor-leadership` (skills path indisponível — ingest sem calibração de referência)

**Páginas criadas (sources):**
- `wiki/sources/roadmap-dev-senior-2026.md`

**Páginas criadas (concepts):**
- `wiki/concepts/vocabulario-tecnico.md`
- `wiki/concepts/pensamento-sistemico.md`
- `wiki/concepts/ia-ciclo-dependencia.md`

**Páginas atualizadas:**
- `wiki/concepts/abstracao.md`
- `wiki/concepts/decomposicao-de-problemas.md`
- `wiki/concepts/observabilidade.md`
- `wiki/concepts/vibe-coding.md`
- `wiki/concepts/piramide-de-testes.md`

**Conceitos cobertos:** 5 pilares (pensar antes de codar, execução real, pensamento sistêmico, sistemas em produção, IA sem dependência), ciclo de degradação por IA, vocabulário técnico como base

**Open questions:** velocidade real do ciclo de degradação de competência; como medir qualidade de julgamento técnico vs geração de código

---

## [2026-04-29] ingest | A Natureza Trimodal da Compensação em Tech

**Source:** `wiki/sources/trimodal-compensacao-tech.md`
**Raw:** `raw/trimodal-compensacao-tech.md`
**Skill:** `tech-mentor-leadership` (referência: `career-progression.md`)

**Páginas criadas (sources):**
- `wiki/sources/trimodal-compensacao-tech.md`

**Páginas criadas (concepts):**
- `wiki/concepts/modelo-trimodal-compensacao.md`
- `wiki/concepts/equity-como-diferencial.md`
- `wiki/concepts/tier-de-empresas-tech.md`

**Conceitos cobertos:** modelo trimodal, 3 tiers de empresas, por que benchmarks públicos erram, equity como diferencial invisível, decisão de empresa > decisão de cargo, aplicabilidade global

**Conexões:** [[ia-salario-ou-carga-de-trabalho]], [[comparacao-na-carreira-dev]], [[desenvolvedor-acima-da-media-10-itens]]

---

## [2026-04-29] ingest | 5 Princípios Que Vão Mudar Você Como Programador

**Source:** `wiki/sources/5-principios-programador.md`
**Raw:** `raw/5-principles-that-changed-me-as-a-programmer.md`
**Skill:** `tech-mentor-leadership` (referência: `software-craftsmanship.md`)

**Páginas criadas (sources):**
- `wiki/sources/5-principios-programador.md`

**Páginas criadas (concepts):**
- `wiki/concepts/logs-em-producao.md`
- `wiki/concepts/usuarios-como-agentes-do-caos.md`

**Páginas atualizadas (concepts):**
- `wiki/concepts/tech-debt-como-ferramenta.md` — source_count 1→2
- `wiki/concepts/naming.md` — source_count 1→2
- `wiki/concepts/paridade-local-producao.md` — source_count 1→2

**Nota:** `tech-debt-como-ferramenta`, `naming` e `paridade-local-producao` já existiam de sessão anterior com `[[sources/5-principios-programador]]` como source — confirmando que o ingest original foi parcialmente executado (concepts criados, source page não).

**Conexões:** [[habitos-ruins-de-programador]], [[9-habitos-programador-junior]], [[conceitos-que-ninguem-ensina]], [[observabilidade]], [[estilo-de-codigo-convencoes]]

---

## [2026-04-29] ingest | Apagão de Sêniors e Vibe Coding

**Source:** `wiki/sources/apagao-de-seniors-vibe-coding.md`
**Raw:** `raw/apagao-de-seniors-vibe-coding.md`
**Skill:** `tech-mentor-ai`

**Páginas criadas (sources):**
- `wiki/sources/apagao-de-seniors-vibe-coding.md`

**Páginas criadas (concepts):**
- `wiki/concepts/property-based-testing.md`
- `wiki/concepts/n-plus-um-detector.md`

**Páginas atualizadas (concepts):**
- `wiki/concepts/vibe-coding.md` — adicionada seção de risco de qualidade + backlink

**Conceitos cobertos:** vibe coding, apagão de sêniors, N+1 detector, property-based testing, memory leak profiling, supply chain security, tradeoffs de arquitetura, adaptive thinking

**Conexões:** [[banco-de-dados]], [[async-io-memory-management]], [[supply-chain-security]], [[devsecops-pipeline]], [[piramide-de-testes]], [[tdd]]

---

## [2026-04-29] ingest | Convenções de Estilo de Código

**Source:** `wiki/sources/estilo-de-codigo-convencoes.md`
**Raw:** `raw/estilo-de-codigo-convencoes.md`
**Skill:** `tech-mentor-leadership` (referência: `software-craftsmanship.md`)

**Páginas criadas (sources):**
- `wiki/sources/estilo-de-codigo-convencoes.md`

**Páginas criadas (concepts):**
- `wiki/concepts/indentacao-como-aviso.md`
- `wiki/concepts/comentarios-o-que-nao-o-como.md`
- `wiki/concepts/comprimento-de-funcao.md`
- `wiki/concepts/strings-de-log-integras.md`

**Conceitos cobertos:** indentação 8 chars como aviso de aninhamento, strings de log íntegras para grep, tamanho de função inversamente proporcional à complexidade, comentários explicam o quê não o como

**Conexões:** [[anti-patterns]], [[conceitos-que-ninguem-ensina]], [[clean-architecture]]

---

## [2026-04-29] ingest | Como Aprender um Codebase Novo

**Source:** `wiki/sources/como-aprender-um-codebase-novo.md`
**Raw:** `raw/como-aprender-um-codebase-novo.md`
**Skill:** `tech-mentor-leadership` (referência: `onboarding-tecnico.md`)

**Páginas criadas (sources):**
- `wiki/sources/como-aprender-um-codebase-novo.md`

**Páginas criadas (concepts):**
- `wiki/concepts/aprendizado-por-impressoes.md`
- `wiki/concepts/exploracao-com-intencao.md`
- `wiki/concepts/aprender-ensinando.md`
- `wiki/concepts/entendimento-do-dominio.md`

**Conceitos cobertos:** onboarding técnico, aprendizado por impressões repetidas, exploração com intenção, modelo mental de fluxo de dados, pair programming como transferência de conhecimento, aprender ensinando, good first issue, entendimento de domínio

**Conexões:** [[habitos-ruins-de-programador]], [[9-habitos-programador-junior]], [[conceitos-que-ninguem-ensina]]

---

## [2026-04-29] sync | Correção de órfãos e ingest do raw de compilação

**Ações:**
- Criado `wiki/sources/listen-notes-one-person-startup.md` — source page para o raw de compilação PT-BR da trilogia Listen Notes
- Atualizado `source_file` em `listen-notes-boring-tech-one-person-company.md`, `listen-notes-good-enough-engineering.md` e `listen-notes-podcasts-nova-wikipedia.md` apontando para o raw
- Deletado `wiki/sources/5-principios-programador.md` — source page criada sem raw correspondente, violando a invariante. Raw nunca existiu. Quando o raw for dropado em `raw/`, reingerir.

**Skill:** `tech-mentor-backend`

---

## [2026-04-26] ingest | Listen Notes — Trilogy (Wenbin Fang)

**Sources:**
- `wiki/sources/listen-notes-boring-tech-one-person-company.md`
- `wiki/sources/listen-notes-good-enough-engineering.md`
- `wiki/sources/listen-notes-podcasts-nova-wikipedia.md`

**Skill:** `tech-mentor-backend` (artigos 1 e 2) · `tech-mentor-leadership` (artigo 3)

**Raw criado:** `raw/listen-notes-one-person-startup.md` — resumo completo do vídeo em PT-BR

**Conceitos cobertos:** one-person-company, boring-technology, good-enough-engineering, over-engineering, processamento-assíncrono, monorepo, aprendizado-informal, podcasts como mídia de conhecimento

**Nota:** Trilogia de artigos de Wenbin Fang sobre como construiu e opera o Listen Notes sozinho. Inclui infraestrutura detalhada (20 servidores AWS), tech stack completa e mentalidade anti-over-engineering.

---

## [2026-04-26] ingest | IA Aumenta Salário ou Carga de Trabalho?

**Source:** `wiki/sources/ia-salario-ou-carga-de-trabalho.md`
**Skill:** `tech-mentor-leadership` (referência: `ai-strategy-engineering.md`)

**Páginas criadas (sources):**
- `wiki/sources/ia-salario-ou-carga-de-trabalho.md`

**Páginas criadas (concepts):**
- `wiki/concepts/compute-como-compensacao.md`
- `wiki/concepts/ia-como-chicote-de-produtividade.md`

**Páginas tocadas:**
- `wiki/concepts/divida-cognitiva.md` — seção "Burnout voluntário com autonomia" + backlink, source_count 1→2
- `wiki/concepts/vibe-coding.md` — seção "O paradoxo do engenheiro autônomo" + backlink, source_count 1→2

**Notas:** Source complementa [[sources/divida-cognitiva-ai-brainfry]] adicionando a dimensão econômica (compute como compensação) e organizacional (autonomia vs. imposição). Sem contradições com o wiki existente.

---

## [2026-04-26] ingest | 5 Princípios Que Vão Mudar Você Como Programador

**Source:** `wiki/sources/5-principios-programador.md`
**Skill:** `tech-mentor-leadership` (referências: `tech-debt-management.md`, `software-craftsmanship.md`)

**Páginas criadas (sources):**
- `wiki/sources/5-principios-programador.md`

**Páginas criadas (concepts):**
- `wiki/concepts/tech-debt-como-ferramenta.md`
- `wiki/concepts/naming.md`
- `wiki/concepts/paridade-local-producao.md`

**Páginas tocadas:**
- `wiki/concepts/observabilidade.md` — backlink adicionado, source_count 1→2
- `wiki/concepts/testar-proprio-codigo.md` — seção "Usuários como agentes do caos" adicionada, source_count 1→2

**Notas:** Transcrição de vídeo YouTube (autor desconhecido). Tech debt deliberado alinha com Quadrante de Fowler já em `tech-debt-management.md`. Naming é conceito novo no wiki — complementa o cluster de software design.

---

## [2026-04-25] ingest | Diferenciais de Portfólio para Dev Backend Júnior

**Source:** `wiki/sources/diferenciais-portfolio-backend-junior.md`
**Skill:** `tech-mentor-leadership`

**Páginas criadas (sources):**
- `wiki/sources/diferenciais-portfolio-backend-junior.md`

**Páginas criadas (concepts):**
- `wiki/concepts/portfolio-backend-junior.md`
- `wiki/concepts/testes-integracao-banco-real.md`
- `wiki/concepts/docker-portfolio.md`
- `wiki/concepts/documentacao-api-swagger.md`
- `wiki/concepts/error-handling-estruturado.md`
- `wiki/concepts/sql-alem-do-basico.md`

**Páginas atualizadas:**
- `wiki/concepts/observabilidade.md` — backlink adicionado
- `wiki/concepts/curriculo-vs-portfolio.md` — backlink adicionado

**Notas:** Source cobre 7 diferenciais concretos + lista do que NÃO focar. Nova seção `### Carreira & Portfólio` criada no index. Sem contradições com wiki existente. `docker-portfolio`, `documentacao-api-swagger` e `sql-alem-do-basico` criados como stubs — candidatos a sources dedicados com mais profundidade técnica.

**Questões abertas:** Nenhuma.

---

## [2026-04-25] ingest | Acoplamento, Abstração e Estado — Lentes para Enxergar Código

**Source:** `wiki/sources/acoplamento-abstracao-estado.md`
**Skill:** `tech-mentor-backend` → `references/software-craftsmanship.md`

**Páginas criadas (sources):**
- `wiki/sources/acoplamento-abstracao-estado.md`

**Páginas criadas (concepts):**
- `wiki/concepts/lentes-de-codigo.md`
- `wiki/concepts/acoplamento.md`
- `wiki/concepts/abstracao.md`
- `wiki/concepts/estado-compartilhado.md`
- `wiki/concepts/imutabilidade.md`
- `wiki/concepts/efeito-colateral.md`
- `wiki/concepts/coesao.md`
- `wiki/concepts/single-responsibility.md`

**Páginas atualizadas:**
- `wiki/concepts/idempotencia.md` — backlink adicionado

**Notas:** Source cobre os três termos como "lentes" (não decoreba), com exemplos TypeScript concretos de antes/depois. Todos os conceitos interligados entre si. `imutabilidade`, `efeito-colateral`, `coesao` e `single-responsibility` criados como stubs — candidatos a sources dedicados. Sem contradições com o wiki existente.

**Questões abertas:** Nenhuma.

---

## [2026-04-23] ingest | Clean Architecture na Era da IA + 4 referências

**Sources (5):**
- [[sources/clean-architecture-ia-custo-real]] — transcrição de vídeo PT-BR
- [[sources/navigation-paradox-2026]] — paper arxiv (Tarakanath Paipuru, fev 2026)
- [[sources/addy-osmani-80-problem-agentic-coding]] — artigo Addy Osmani, Google
- [[sources/super-productivity-ai-architecture-guide]] — artigo Super Productivity Blog
- [[sources/go-is-not-java]] — blog vertigrated.com (fetch 429 — nota baseada no vídeo)

**Skills:** `tech-mentor-backend` (vídeo, super-productivity, go) · `tech-mentor-ai` (navigation paradox, addy osmani)

**Conceitos criados (6):**
- `wiki/concepts/yagni.md`
- `wiki/concepts/abstraction-bloat.md`
- `wiki/concepts/comprehension-debt.md`
- `wiki/concepts/abstraction-illusion.md`
- `wiki/concepts/navigation-paradox.md`
- `wiki/concepts/vertical-slice-architecture.md`

**Páginas atualizadas:**
- `wiki/concepts/divida-cognitiva.md` → backlink comprehension-debt + addy osmani

**Notas:** Cluster temático coeso: Clean Architecture ritualística tem custo mensurável em tokens e erros de agentes. O Navigation Paradox (paper) quantifica: 76.2% ACS em deps escondidas via DI containers. Addy Osmani nomeia o problema de geração: abstraction bloat. Super Productivity nomeia o problema de decisão: abstraction illusion. Go exemplifica que os princípios sobrevivem sem a cerimônia. YAGNI de 1999 (Kent Beck) continua sendo o princípio central — a IA apenas escalou o custo de ignorá-lo.

**Questões abertas:**
- É possível medir ACS em projetos Go vs TypeScript Clean Architecture para validar a hipótese empiricamente?
- Existe um número de arquivos por feature que serve como threshold objetivo para questionar a arquitetura?

---

## [2026-04-23] ingest | Platform Engineering Mobile — Shared SDK, Módulos Nativos, DX da Equipe

**Source:** [[sources/mobile-platform-engineering]]
**Skill:** `tech-mentor-mobile` → `references/react-mobile-desktop.md`

**Páginas criadas:**
- `wiki/sources/mobile-platform-engineering.md`
- `wiki/concepts/shared-sdk.md`
- `wiki/concepts/adapter-pattern-analytics.md`
- `wiki/concepts/native-module.md`
- `wiki/concepts/monorepo-mobile.md`

**Páginas atualizadas:**
- `wiki/concepts/analytics-pipeline.md` → adicionado contexto mobile + backlink

**Notas:** Source cobre a camada de platform engineering mobile — não apps, mas a infraestrutura que suporta múltiplos apps. Padrão central: Adapter Pattern para analytics (evita acoplamento a providers em 200 call sites). Native Modules custom apenas quando não há lib matura. Monorepo com Turborepo + pnpm como estrutura recomendada.

**Questões abertas levantadas:**
- `ApiClient` singleton com `useAuthStore.getState()` cria acoplamento oculto ao estado global — como isolar para testes?
- Qual limite de tamanho justifica split de SDK em pacotes com versionamento independente?

---

## [2026-04-23] ingest | Dívida Cognitiva e AI Brainfry

- **Source:** [[sources/divida-cognitiva-ai-brainfry]]
- **Skill:** tech-mentor-ai
- **URLs:** [HBR — When Using AI Leads to Brain Fry](https://hbr.org/2026/03/when-using-ai-leads-to-brain-fry) · [Margaret Storey — Cognitive Debt](https://margaretstorey.com/blog/2026/02/09/cognitive-debt/)
- **Páginas criadas:** `sources/divida-cognitiva-ai-brainfry`, `concepts/divida-cognitiva`, `concepts/ai-brainfry`, `concepts/vibe-coding`, `entities/margaret-storey`
- **Notas:** Claim mais importante: a forma mais desgastante de interação com IA não é gerar código — é supervisionar. O dev não "descansa" enquanto o agente trabalha; processa o próximo item simultaneamente. A digitação do código pode ter sido o refresco cognitivo que os devs não sabiam que tinham. Distinção útil: AI Brainfry pode acontecer com alta sensação de produtividade — é possível gerar 200 commits/dia e estar exausto cognitivamente. O gargalo real não é produtividade; é coerência, foco, finalização e julgamento.

---

## [2026-04-23] ingest | Conceitos que Ninguém Ensina em Curso

- **Source:** [[sources/conceitos-que-ninguem-ensina]]
- **Skill:** tech-mentor-system-design (`references/architecture-foundations.md`)
- **Páginas criadas:** `sources/conceitos-que-ninguem-ensina`, `concepts/back-pressure`, `concepts/temporal-coupling`, `concepts/accidental-complexity`, `concepts/essential-complexity`, `concepts/cache-stampede`, `entities/fred-brooks`
- **Páginas atualizadas:** `concepts/thundering-herd` (backlink + source_count 1→2)
- **Notas:** Quatro conceitos fundamentais raramente ensinados explicitamente. Insight mais importante: temporal coupling — o erro resultante de chamar fora de ordem não diz "chamou errado", diz NullPointerException. A solução não é documentar melhor, é tornar a chamada incorreta impossível pelo design. Distinção de Fred Brooks (1986) entre complexidade acidental e essencial é o modelo mental mais útil para priorizar tech debt.

---

## [2026-04-23] ingest | Batch Completo — 121 fontes (AI/LLM, Backend, Infra, Security, Data, Messaging, System Design)

- **Sources criadas:** 121 source pages em `wiki/sources/`
- **Skills utilizadas:** `tech-mentor-ai` (18) · `tech-mentor-backend` (25) · `tech-mentor-infra` (6) · `tech-mentor-security` (34) · `tech-mentor-data` (4) · `tech-mentor-system-design` (28) · `tech-mentor-networking` (1) · `cs-fundamentals` (1) · `lang-dynamic` (2) · `lang-systems` (1) · `tech-mentor-leadership` (1)
- **Domínios cobertos:**
  - AI/LLM: agentes-core, agentes-em-producao, agentes-orquestracao, agent-memory, ai-gateway-token-economics, ai-llm-security, ai-safety-guardrails, como-llms-funcionam, context-engineering, evals-sistematicas, fine-tuning, llmops-observabilidade, mcp, open-weight-deployment, prompt-engineering, rag-retrieval, reasoning-models, structured-outputs-function-calling
  - Backend: adr, anti-patterns, api-contracts-versioning, background-jobs, clean-architecture, conways-law, ddd-cqrs, ddd-strategic, ddd-tactical, dependency-injection, design-patterns-gof, event-driven-architecture, event-ordering-long-running, event-versioning, graphql, grpc, hexagonal-architecture, integration-patterns-eip, microsservicos, monolito-modular, tolerant-reader, temporal, webhook, websocket-sse-realtime, api-gateway-bff
  - Infra: kubernetes-core, k8s-autoscaling, k8s-networking, gitops-argocd, terraform, platform-engineering-devex
  - Data: postgresql-avancado, postgresql-extensions, redis-avancado, mongodb
  - Security: owasp-top10, oauth2-oidc-jwt, zero-trust, api-security, autenticacao-segura, secrets-management, threat-modeling, tls-mtls-vpn, rbac-abac-rebac, criptografia-fundamentos, browser-security, bug-bounty, cloud-security, compliance-soc2-pci, container-hardening, data-privacy, devsecops-pipeline, federated-identity, hipaa-sox, identidade-avancada, identity-iam-avancado, incident-response, input-validation-output-encoding, kubernetes-security, lgpd-gdpr, mobile-security, passkeys-webauthn, pentest-redteam, policy-as-code, post-quantum-crypto, runtime-security, secret-scanning, secure-design-patterns, supply-chain-security
  - Messaging: kafka, rabbitmq, nats-jetstream, sqs-sns, saga-pattern, outbox-pattern, dlq-event-patterns, schema-registry
  - System Design: architecture-fitness-functions, bancos-especializados, c4-model, cdc-debezium, cell-based-architecture, checklist-solutions-architect, dynamodb, elasticsearch-opensearch, evolutionary-architecture, expand-contract, fase-1-fundamentos-infraestrutura, flame-graph-profiling, fraud-abuse, micro-kernel, migrations-schema-evolution, otel-collector-sampling, otel-sdk, pagination, performance-methods, presenters, reactive-architecture, rest-openapi, rfc, serialization-protocols, sessions, solid, space-based-architecture, wardley-maps
  - Networking: http-tcp-quic
  - CS Fundamentals: two-sum-explicacao
  - Lang: typescript-avancado, go-core, async-io-memory-management
- **Notas:** Maior batch de ingest do wiki. Cobertura completa de infraestrutura técnica para nível Solutions Architect. Cada source segue o formato canônico com TL;DR, Key Claims (Claim/Evidence/Confidence), Entities & Concepts Touched e Open Questions. Index.md atualizado com todos os 121 novos sources.

---

## [2026-04-23] ingest | O Problema de Usar UUID como Primary Key no MySQL

- **Source:** [[sources/uuid-primary-key-mysql]]
- **Skill:** tech-mentor-data
- **URL:** https://planetscale.com/blog/the-problem-with-using-a-uuid-primary-key-in-mysql
- **Páginas criadas:** `sources/uuid-primary-key-mysql`, `concepts/uuid`, `concepts/page-splitting`
- **Páginas atualizadas:** `concepts/database-index` (backlink), `concepts/snowflake-id` (backlink)
- **Notas:** Insight central — page splitting com UUIDv4 deixa páginas com ~50% de utilização vs ~94% com sequenciais. UUIDv7 resolve o problema mantendo distribuição sem coordenação. Open question registrada: suporte nativo de UUIDv7 no PostgreSQL 17+.

---

## [2026-04-23] ingest | Batch de 16 fontes — Sistemas Distribuídos, Infra e Backend

- **Sources:** `crdt-colaboracao-tempo-real`, `db-sharding`, `distributed-locks`, `distributed-locks-raft`, `distributed-tracing`, `feature-flags`, `finops-cost-aware-architecture`, `fintech-system-design`, `graceful-degradation`, `idempotencia`, `load-balancer`, `mensageria`, `presence-system`, `raft-leader-election`, `rate-limiting`, `read-replicas-connection-pooling`
- **Skills:** `tech-mentor-system-design` (11 fontes) · `tech-mentor-backend` (3) · `tech-mentor-infra` (2) · `tech-mentor-data` (1)
- **Páginas de source criadas:** 16
- **Concepts criados:** `crdt`, `operational-transformation`, `db-sharding`, `distributed-tracing`, `rate-limiting`, `load-balancer`, `mensageria`, `finops`, `ledger-dupla-entrada`
- **Entities criadas:** `martin-kleppmann`, `yjs`
- **Conceitos já existentes tocados (backlink):** `graceful-degradation`, `feature-flags`, `idempotencia`, `distributed-lock`, `fencing-token`, `skip-locked`, `raft-paxos`, `presenca-online`, `read-replicas`, `connection-pooling`, `read-your-writes`, `retry-backoff`, `circuit-breaker`, `saga-pattern`, `outbox-pattern`, `consistent-hashing`, `storage-tiering`, `canary-release`
- **Notas:** Kleppmann 2016 sobre Redlock documentado com nuance — Antirez respondeu que Redlock é adequado para locks de "eficiência", não "correção". Distinção Queue vs Stream é o conceito mais importante de mensageria para entrevistas. Ledger de dupla entrada é invariante matemático: soma de débitos = soma de créditos.

---

## [2026-04-23] ingest | Três Características para Ser o Melhor Candidato

- **Source:** [[sources/tres-caracteristicas-melhor-candidato]]
- **Skill:** tech-mentor-leadership (`references/career-progression.md`)
- **Páginas criadas:** `sources/tres-caracteristicas-melhor-candidato`, `concepts/profundidade-e-maestria`, `concepts/abrangencia-profissional`, `concepts/comunicacao-tecnica`, `concepts/curriculo-vs-portfolio`, `entities/randy-nelson`
- **Páginas atualizadas:** `concepts/maturidade-tecnica` (backlink + source_count)
- **Notas:** Transcrição com ruído de voz — conteúdo reconstruído por contexto (ex: "pizza" → Pixar, "mais 7" → maestria). Insight forte: falhar e se recuperar como filtro de contratação para inovação, documentado no exemplo da NASA. Distinção currículo vs portfólio complementa comparacao-na-carreira.

---

## [2026-04-22] ingest | Circuit Breaker

- **Source:** [[sources/circuit-breaker]]
- **Skill:** tech-mentor-system-design (`references/graceful-degradation.md`)
- **Páginas criadas:** `sources/circuit-breaker`, `concepts/falha-em-cascata`
- **Páginas atualizadas:** `concepts/circuit-breaker` (stub → stable, enriquecido com diagrama de estados, Opossum, retry order, métricas, parâmetros por criticidade)
- **Notas:** Detalhe crítico documentado — retry deve ficar dentro do circuit breaker, não fora. Conceito falha-em-cascata criado pois estava faltando apesar de ser referenciado.

---

## [2026-04-22] ingest | CI/CD Pipeline

- **Source:** [[sources/cicd-pipeline]]
- **Skill:** tech-mentor-infra (`references/devops/ci-cd-strategies.md` + `references/devops/progressive-delivery.md`)
- **Páginas criadas:** `sources/cicd-pipeline`, `concepts/ci-cd`, `concepts/pipeline-de-ci`, `concepts/github-actions`, `concepts/argo-rollouts`
- **Notas:** Source bem estruturado com código de referência completo. Backlinks adicionados para canary-release, blue-green-deploy, feature-flags, zero-downtime-deploy e observabilidade. Open questions sobre Argo vs Flagger e monorepo pipelines registradas na source page.

---

## [2026-04-22] ingest | Sistema Operacional: O Que Acontece Por Baixo dos Panos

- **Source:** [[sources/sistema-operacional-por-baixo-dos-panos]]
- **Skill:** cs-fundamentals (`references/os-fundamentals.md`)
- **Páginas criadas:** `sources/sistema-operacional-por-baixo-dos-panos`, `concepts/processo`, `concepts/thread`, `concepts/deadlock`, `concepts/mutex`, `concepts/escalonador`, `concepts/context-switch`, `concepts/interrupcao-de-hardware`, `concepts/memoria-virtual`, `concepts/swap`, `concepts/sistema-de-arquivos`, `concepts/syscall`, `concepts/kernel`
- **Notas:** Transcrição com ruído de voz — nomes técnicos reconstruídos (ex: "trad" → thread, "miltex" → mutex, "contex sutch" → context switch). Cobertura ampla mas superficial — bom ponto de entrada para cada conceito. Open questions registradas na source page.

---

## [2026-04-22] ingest | Princípio da Inversão: Como Ser um Programador Melhor

- **Source:** [[sources/principio-da-inversao-programador]]
- **Skill:** tech-mentor-leadership
- **Páginas criadas:** `sources/principio-da-inversao-programador`, `concepts/principio-da-inversao`, `concepts/ciclo-da-desgraca-software`, `concepts/tutorial-hell`, `concepts/dados-vs-intuicao`, `concepts/complexidade-como-estrategia`, `concepts/maturidade-tecnica`, `concepts/atualizacao-tecnologica`, `concepts/pitfalls-de-linguagem`, `entities/charlie-munger`, `entities/george-hotz`, `entities/karl-gustav-jakob-jacobi`
- **Páginas atualizadas:** `concepts/aprendizado-deliberado` (backlink + source_count)
- **Notas:** Transcrição com ruído de voz — conceitos reconstruídos por inferência. Caso Amazon de recomendações no checkout é forte evidência para dados-vs-intuicao. Questão aberta: tutorial-hell e aprendizado-deliberado se sobrepõem — verificar se merecem consolidação futura.

---

## [2026-04-22] ingest | Lógica de Programação Sem Ser Gênio da Matemática

- **Source:** [[sources/logica-programacao-sem-matematica]]
- **Skill:** tech-mentor-leadership
- **Created:** `sources/logica-programacao-sem-matematica.md`, `concepts/decomposicao-de-problemas.md`
- **Updated:** `concepts/aprendizado-deliberado.md` (source_count 1→2), `concepts/postura-de-programador.md` (source_count 1→2), `index.md`, `log.md`
- **Notes:** Exercício do caixa eletrônico em Java demonstra decomposição + SRP em métodos; matemática exigida é apenas divisão inteira e módulo.

---

## [2026-04-22] ingest | Case: YouTube / Video Streaming

**Source:** [[sources/case-youtube-streaming]]
**Skill:** `tech-mentor-system-design` → `references/system-design-cases`

**Páginas criadas:**
- `wiki/sources/case-youtube-streaming.md`
- `wiki/concepts/video-transcoding.md`
- `wiki/concepts/adaptive-bitrate-streaming.md`
- `wiki/concepts/cdn-strategy.md`
- `wiki/concepts/storage-tiering.md`

**Páginas existentes referenciadas (backlink via source):**
- `wiki/concepts/media-upload-pattern.md` — presigned URL reusado do case WhatsApp
- `wiki/concepts/estimativas-back-of-envelope.md` — scale numbers do YouTube

**Questões abertas levantadas:**
- DRM: key rotation sem interromper streams ativos?
- Break-even de custo H.264 vs AV1 (encoding mais caro vs economia de CDN)?

**Notas:** Único case com problema de storage em escala de exabyte. Conceito mais subestimado: imutabilidade dos segmentos como fundação do CDN agressivo. media-upload-pattern reusado do WhatsApp — não duplicado.

---

## [2026-04-22] ingest | Case: WhatsApp

**Source:** [[sources/case-whatsapp]]
**Skill:** `tech-mentor-system-design` → `references/system-design-cases`

**Páginas criadas:**
- `wiki/sources/case-whatsapp.md`
- `wiki/concepts/websocket-vs-polling.md`
- `wiki/concepts/chat-distribuido.md`
- `wiki/concepts/ack-triplo.md`
- `wiki/concepts/presenca-online.md`
- `wiki/concepts/cassandra-schema.md`
- `wiki/concepts/media-upload-pattern.md`

**Questões abertas levantadas:**
- Signal Protocol: como ACK de leitura funciona sem o servidor ler o conteúdo?
- Fan-out grupos 256 — threshold para trocar Redis Pub-Sub por Kafka?

**Notas:** Case mais rico em padrões de baixo nível desta batch. Conceito mais subestimado: presença online — escala do problema é contra-intuitiva. Cassandra schema modelado por padrão de acesso, não por domínio.

---

## [2026-04-22] ingest | Case: URL Shortener

**Source:** [[sources/case-url-shortener]]
**Skill:** `tech-mentor-system-design` → `references/system-design-cases`

**Páginas criadas:**
- `wiki/sources/case-url-shortener.md`
- `wiki/concepts/snowflake-id.md`
- `wiki/concepts/http-redirect-301-302.md`
- `wiki/concepts/cache-hot-path.md`
- `wiki/concepts/analytics-pipeline.md` (stub)

**Questões abertas levantadas:**
- Rate limiting por IP no redirect — como evitar falsos positivos em NATs compartilhados?
- ClickHouse vs DynamoDB para analytics em escala de 10B events/dia?

**Notas:** Case clássico de entrevista. Conceito mais subestimado: 301 vs 302 tem trade-off real de analytics vs cache de browser. Power law justifica estratégia de cache em camadas.

---

## [2026-04-22] ingest | Case: Ride-sharing (Uber)

**Source:** [[sources/case-uber]]
**Skill:** `tech-mentor-system-design` → `references/system-design-cases`

**Páginas atualizadas:**
- `wiki/sources/case-uber.md` — stub existente substituído por source completa

**Páginas criadas:**
- `wiki/concepts/geohash.md`
- `wiki/concepts/redis-geo.md`
- `wiki/concepts/ride-matching-pipeline.md`
- `wiki/concepts/distributed-lock.md`
- `wiki/concepts/surge-pricing.md`
- `wiki/concepts/realtime-tracking.md` (stub)
- `wiki/concepts/estimativas-back-of-envelope.md` (stub)

**Questões abertas levantadas:**
- Como coordenar canary de algoritmo de matching sem afetar SLA de <1s?
- Geohash boundary problem em fronteiras de países — impacto operacional?

**Notas:** Source existia como stub (source_count: 0). Substituída por versão completa. Nova seção "System Design Cases" criada no index. Distributed lock referencia a controvérsia Kleppmann vs antirez sobre Redlock.

---

## [2026-04-22] ingest | Modelos de Consistência

**Source:** [[sources/modelos-de-consistencia]]
**Skill:** `tech-mentor-system-design` → `references/distributed-systems`

**Páginas criadas:**
- `wiki/sources/modelos-de-consistencia.md`
- `wiki/concepts/consistency-models.md`

**Páginas atualizadas:**
- `wiki/concepts/read-your-writes.md` — backlink para novo source + consistency-models, source_count 1→2

**Questões abertas levantadas:**
- PACELC como extensão do CAP — vale source próprio?
- CRDTs como alternativa a vector clocks — quando usar?
- Cassandra tunable consistency (ONE/QUORUM/ALL) — mapeamento para os modelos?

**Notas:** `read-your-writes` já existia do ingest de banco-de-dados — atualizado com backlink em vez de duplicado. Conceito mais subestimado: **armadilha de modelo errado por domínio** — eventual para inventário = overselling (bug financeiro), linearizable para view count = gargalo de escala sem necessidade.

---

## [2026-04-22] ingest | Multi-tenancy Patterns

**Source:** [[sources/multi-tenancy]]
**Skill:** `tech-mentor-system-design` → `references/multi-tenancy`

**Páginas criadas:**
- `wiki/sources/multi-tenancy.md`
- `wiki/concepts/multi-tenancy.md`
- `wiki/concepts/tenant-context.md`

**Questões abertas levantadas:**
- Schema-per-tenant vs DB-per-tenant em compliance enterprise — quando schema é suficiente?
- `pg_stat_statements` por tenant_id para identificar noisy neighbor — overhead aceitável?
- TenantConfig com `dataResidency` — como rotear para região certa sem aumentar latência?

**Notas:** Source mais densa até agora — cobre modelo de dados, migrations, rate limiting, GDPR e offboarding. TenantContext separado como conceito próprio — AsyncLocalStorage aparece em outros contextos (request context, tracing). Conceito mais subestimado: **RLS é segunda linha de defesa, não a primeira** — a primeira são testes automatizados que verificam explicitamente que tenant A não acessa dados de tenant B.

---

## [2026-04-22] ingest | Notification System Design

**Source:** [[sources/notification-system]]
**Skill:** `tech-mentor-system-design` → `references/design-cases`

**Páginas criadas:**
- `wiki/sources/notification-system.md`
- `wiki/concepts/notification-system.md`
- `wiki/concepts/fanout-pattern.md`

**Questões abertas levantadas:**
- Fan-out híbrido — threshold exato (1000? 10000 seguidores)?
- Notification batching — como modelar no schema?
- Timezone-aware quiet hours em escala global?

**Notas:** Fan-out separado como conceito próprio — aparece em notificações, feed de posts e chat distribuído. Conceito mais subestimado: **email bounce handling** — ignorar bounces é o caminho mais rápido para o domínio de email da empresa ir para blacklist e perder deliverability em todos os emails, não só notificações.

---

## [2026-04-22] ingest | Observabilidade

**Source:** [[sources/observabilidade]]
**Skill:** `tech-mentor-system-design` → `references/performance-profiling.md`

**Páginas criadas:**
- `wiki/sources/observabilidade.md`
- `wiki/concepts/observabilidade.md`
- `wiki/concepts/red-method.md`

**Questões abertas levantadas:**
- OpenTelemetry auto-instrumentation vs manual — quando overhead de configuração vale?
- Alert fatigue em times com muitos serviços — como calibrar thresholds sem perder sinal?
- Custo de storage de métricas/logs em escala — quando Datadog supera self-hosted?

**Notas:** Complementa as ingests de SRE (sli/slo/sla + incidents). RED Method separado como conceito próprio — aparece em SLI, observabilidade e service mesh. Conceito mais subestimado: **prioridade de implementação** — distributed tracing é o mais "sexy" mas o último a implementar. Logs estruturados com trace ID entregam 80% do valor com 10% do esforço.

---

## [2026-04-22] ingest | Pirâmide de Testes (re-ingest — upgrade)

**Source:** [[sources/piramide-de-testes]]
**Skill:** `tech-mentor-testing` → `references/test-strategy.md`

**Páginas atualizadas:**
- `wiki/sources/piramide-de-testes.md` — claims expandidos com evidence, path corrigido (nemomartins → gabriel-martins), backlinks corrigidos, open questions adicionadas
- `wiki/concepts/piramide-de-testes.md` — exemplos de código adicionados (unitário, integração, E2E/Playwright), backlink corrigido

**Notas:** Source existia do batch ingest de testing mas estava incompleta — sem código, path incorreto, backlinks com prefixo `wiki/`. Promovido para padrão atual. Conceito mais subestimado: E2E não bloqueia PR — bloqueia release. Colocar E2E no gate de PR é o caminho mais rápido para destruir a cultura de testes do time.

---

## [2026-04-22] ingest | Retry com Backoff Exponencial

**Source:** [[sources/retry-backoff]]
**Skill:** `tech-mentor-system-design` → `references/graceful-degradation.md`

**Páginas criadas:**
- `wiki/sources/retry-backoff.md`
- `wiki/concepts/retry-backoff.md`
- `wiki/concepts/thundering-herd.md`
- `wiki/concepts/idempotencia.md`

**Questões abertas levantadas:**
- Retry com backoff em streaming (SSE, WebSocket) — padrão de reconnect?
- Como expor retry count em métricas sem aumentar cardinalidade do Prometheus?
- Jitter full vs decorrelated jitter — diferença prática em alta concorrência?

**Notas:** Conceito mais subestimado: **jitter é obrigatório, não opcional** — backoff exponencial sem jitter ainda cria thundering herd, apenas deslocado no tempo. Idempotency key separado como conceito próprio — aparece em retry, mensageria e pagamentos.

---

## [2026-04-22] ingest | Service Discovery

**Source:** [[sources/service-discovery]]
**Skill:** `tech-mentor-system-design` → `references/distributed-systems`

**Páginas criadas:**
- `wiki/sources/service-discovery.md`
- `wiki/concepts/service-discovery.md`

**Questões abertas levantadas:**
- Consul vs etcd para service discovery em multi-cloud — quando cada um?
- DNS negative caching no K8s — como evitar que falhas de lookup sejam cacheadas?
- Service discovery para workers assíncronos (sem HTTP) — qual o padrão?

**Notas:** Source focada — um conceito central com quatro variantes. DNS-based K8s é o padrão zero-config; Consul para fora do K8s. Conceito mais subestimado: `deregisterCriticalServiceAfter` no Consul — sem isso, instâncias mortas ficam no registry e recebem tráfego indefinidamente.

---

## [2026-04-22] ingest | Service Mesh (Istio, Linkerd, mTLS)

**Source:** [[sources/service-mesh]]
**Skill:** `tech-mentor-system-design` → `references/service-mesh`

**Páginas criadas:**
- `wiki/sources/service-mesh.md`
- `wiki/concepts/service-mesh.md`
- `wiki/concepts/sidecar-pattern.md`
- `wiki/concepts/mtls.md`
- `wiki/concepts/fault-injection.md`
- `wiki/concepts/ambient-mesh.md`

**Questões abertas levantadas:**
- Ambient mesh em produção já é estável para workloads críticos (2026)?
- Como debugar quando o problema está no proxy Envoy e não na aplicação?
- Service mesh vale para sistemas com SLA interno relaxado (< 99.9%)?

**Notas:** Primeira ingest do domínio Service Mesh. Nova seção criada no index. Conceito mais subestimado: **AuthorizationPolicy com SPIFFE** — pod comprometido dentro do cluster não consegue chamar serviços não autorizados, mesmo sem firewall externo. Fault injection via VirtualService é a forma mais segura de fazer chaos engineering: declarativo, reversível, sem matar pods.

---

## [2026-04-22] ingest | SKIP LOCKED e Fencing Token

**Source:** [[sources/skip-locked-fencing-token]]
**Skill:** `tech-mentor-system-design` → `references/distributed-systems`

**Páginas criadas:**
- `wiki/sources/skip-locked-fencing-token.md`
- `wiki/concepts/skip-locked.md`
- `wiki/concepts/fencing-token.md`

**Páginas atualizadas:**
- `wiki/concepts/distributed-lock.md` — seção de lock fantasma, fencing token e SKIP LOCKED adicionadas; backlink

**Questões abertas levantadas:**
- Dead Letter Queue com SKIP LOCKED — melhor abordagem para jobs que falham repetidamente?
- SKIP LOCKED com tabela particionada no PostgreSQL — semântica de lock preservada?
- Fencing token com múltiplos storage backends — quem mantém o `lastToken`?

**Notas:** Dois padrões complementares de concorrência distribuída. Conceito mais subestimado: **o storage protegido — não o cliente — é responsável por validar o fencing token**. Redlock sem fencing token é citado explicitamente como insuficiente para recursos onde corretude > disponibilidade.

---

## [2026-04-22] ingest | SRE — Error Budget, Incident Lifecycle, Post-mortem e Runbook

**Source:** [[sources/sre-error-budget-incidents]]
**Skill:** `tech-mentor-infra` → `references/sre`

**Páginas criadas:**
- `wiki/sources/sre-error-budget-incidents.md`
- `wiki/concepts/incident-lifecycle.md`
- `wiki/concepts/incident-severity.md`
- `wiki/concepts/incident-roles.md`
- `wiki/concepts/runbook.md`
- `wiki/concepts/game-day.md`

**Páginas atualizadas:**
- `wiki/concepts/error-budget.md` — backlink adicionado
- `wiki/concepts/error-budget-policy.md` — backlink adicionado
- `wiki/concepts/blameless-post-mortem.md` — template completo adicionado (seção "O que Funcionou Bem", tabela de ações corretivas), backlink

**Questões abertas levantadas:**
- Game Day em sistemas multi-squad — como coordenar sem criar dependências de agenda?
- Runbook no mesmo repo vs wiki — trade-off de atualização?
- SEV-1 com múltiplos sistemas afetados — dois on-calls simultâneos, quem é o IC?

**Notas:** Segunda ingest do domínio SRE. Burn rate alerting desta source usa métrica de 5xx (erros reais) vs anterior que usava ausência de 2xx — abordagens complementares. Conceito mais subestimado: separação IC/TL — quando a mesma pessoa coordena e investiga, o MTTR aumenta significativamente.

---

## [2026-04-22] ingest | SRE — SLI, SLO, SLA e Error Budget

**Source:** [[sources/sre-sli-slo-sla]]
**Skill:** `tech-mentor-infra` → `references/sre`

**Páginas criadas:**
- `wiki/sources/sre-sli-slo-sla.md`
- `wiki/concepts/sre.md`
- `wiki/concepts/sli.md`
- `wiki/concepts/slo.md`
- `wiki/concepts/sla.md`
- `wiki/concepts/error-budget.md`
- `wiki/concepts/error-budget-policy.md`
- `wiki/concepts/blameless-post-mortem.md`

**Questões abertas levantadas:**
- SLO para sistemas batch/async — como medir freshness de forma equivalente a disponibilidade?
- Error Budget compartilhado entre múltiplos serviços — quem "paga" o incidente?
- SLOs em sistemas internos sem SLA contratual — vale o overhead?

**Notas:** Primeira ingest do domínio SRE. Nova seção "SRE & Observabilidade" criada no index. Conceito mais subestimado: burn rate alerting — detecta esgotamento do budget antecipadamente, threshold absoluto é tarde demais. Error Budget Policy é o que transforma SLO de métrica em ferramenta de decisão.

---

## [2026-04-22] ingest | Zero-Downtime Deploy

**Source:** [[sources/zero-downtime-deploy]]
**Skill:** `tech-mentor-system-design` → `references/zero-downtime-deployments.md`

**Páginas criadas:**
- `wiki/sources/zero-downtime-deploy.md`

**Páginas atualizadas:**
- `wiki/concepts/zero-downtime-deploy.md` — stub → stable; tabela de estratégias, Expand-Contract SQL, graceful shutdown TypeScript + YAML, checklist

**Questões abertas levantadas:**
- Canary com múltiplos serviços dependentes — como coordenar percentual sem drift?
- Expand-Contract em tabelas com bilhões de rows — backfill sem impacto de I/O?

**Notas:** Stub existia via ingest do blue-green-canary-rolling. Promovido a stable com código concreto (Kubernetes YAML, TypeScript SIGTERM handler, SQL Expand-Contract). Conceito mais subestimado: preStop sleep — sem ele, LB continua roteando para pod em shutdown.

---

## [2026-04-22] ingest | Blue/Green, Canary e Rolling Deploy

**Source:** [[sources/blue-green-canary-rolling]]
**Skill:** `tech-mentor-infra` → `references/cicd`

**Páginas criadas:**
- `wiki/sources/blue-green-canary-rolling.md`
- `wiki/concepts/blue-green-deploy.md`
- `wiki/concepts/canary-release.md`
- `wiki/concepts/rolling-update.md`
- `wiki/concepts/expand-contract.md`
- `wiki/concepts/deploy-strategies.md`
- `wiki/concepts/feature-flags.md` (stub)
- `wiki/concepts/zero-downtime-deploy.md` (stub)

**Questões abertas levantadas:**
- Canary com múltiplos serviços dependentes — como coordenar percentual entre eles?
- Expand-Contract em tabelas com bilhões de rows — backfill sem lock longo?

**Notas:** Primeira ingest do domínio de infra/deploy. Nova seção "Deploy & CI/CD" criada no index. Expand-Contract é o conceito mais subestimado da source — crítico para qualquer deploy sem downtime.

---

## [2026-04-22] ingest | 2PC — Two-Phase Commit

**Source:** [[sources/two-phase-commit]]
**Skill:** `tech-mentor-system-design` → `references/distributed-systems`

**Páginas criadas:**
- `wiki/sources/two-phase-commit.md`

**Páginas atualizadas:**
- `wiki/concepts/two-phase-commit.md` — stub → stable; XA code example adicionado, seções quando usar/evitar, backlinks completos

**Questões abertas levantadas:**
- Em quais bancos modernos (CockroachDB, Spanner) 2PC ainda é usado internamente?
- Saga orquestrado vs coreografado — quando cada um?
- JTA/XA em stacks modernas ainda é viável?

**Notas:** Source primária do conceito de 2PC no wiki. Anterior stub `two-phase-commit.md` criado via ingest do 3PC; agora promovido a stable com XA SQL, comparativo 2PC vs Saga e critérios claros de uso. Skill: `tech-mentor-system-design`.

---

## [2026-04-22] ingest | 3PC — Three-Phase Commit

**Source:** [[sources/3pc]]
**Skill:** `tech-mentor-system-design` → `references/distributed-systems`

**Páginas criadas:**
- `wiki/sources/3pc.md`
- `wiki/concepts/three-phase-commit.md`
- `wiki/concepts/two-phase-commit.md` (stub)
- `wiki/concepts/split-brain.md` (stub)
- `wiki/concepts/raft-paxos.md` (stub)
- `wiki/concepts/saga-pattern.md` (stub)
- `wiki/concepts/outbox-pattern.md` (stub)
- `wiki/concepts/distributed-transactions.md` (stub)

**Questões abertas levantadas:**
- Em quais bancos relacionais o 2PC ainda é usado em produção hoje?
- Saga orquestrado vs coreografado — quando cada um?

**Notas:** Primeira ingest do domínio de sistemas distribuídos. 3PC é principalmente acadêmico — stubs criados para as alternativas reais (Saga, Outbox, Raft). Nova seção "Sistemas Distribuídos" criada no index.

---

## [2026-04-22] ingest | Como Aprender Programação — 3 Dicas + Bônus

**Source:** [[sources/como-aprender-programacao-3-dicas]]
**Skill:** `tech-mentor-leadership`

**Páginas criadas:**
- `wiki/sources/como-aprender-programacao-3-dicas.md`
- `wiki/concepts/neuroplasticidade.md`
- `wiki/concepts/spaced-repetition.md`
- `wiki/concepts/tempo-variavel-capacidade-fixa.md`
- `wiki/concepts/aprendizado-deliberado.md`
- `wiki/concepts/postura-de-programador.md`

**Páginas existentes atualizadas (backlinks):**
- `wiki/concepts/comparacao-na-carreira.md`
- `wiki/concepts/familiaridade-vs-capacidade.md`

**Questões abertas levantadas:**
- Intervalo ideal de espaçamento para spaced repetition em código (horas? dias?)?
- "Avalanche sem entender" tem nome na literatura cognitiva? (parece priming/incubação)
- Postura de sobrevivência pode ser cultivada ou precisa ser descoberta?

**Notas:** Transcrição de vídeo PT-BR (speaker não identificado, canal brasileiro). Conceito mais subestimado: a pausa após saturação é parte ativa do aprendizado, não sinal de fraqueza — é quando a neuroplasticidade reorganiza os circuitos. Regra mais contraintuitiva: nunca copiar/colar código, nem nome de variável — redigitar tudo manualmente.

---

## [2026-04-22] ingest | 9 Hábitos que eu gostaria de ter aprendido sendo Programador Júnior

**Source:** [[sources/9-habitos-programador-junior]]
**Skill:** `tech-mentor-leadership`

**Páginas criadas:**
- `wiki/sources/9-habitos-programador-junior.md`
- `wiki/concepts/voluntariar-para-desconhecido.md`
- `wiki/concepts/comunicar-progresso.md`
- `wiki/concepts/escrever-para-aprender.md`
- `wiki/concepts/bloqueio-de-agenda.md`
- `wiki/concepts/pausa-estrategica.md`
- `wiki/concepts/fazer-por-voce.md`
- `wiki/concepts/pair-programming.md` (stub)
- `wiki/concepts/pomodoro.md` (stub)
- `wiki/concepts/documentar-conquistas.md` (stub)
- `wiki/concepts/sem-balas-de-prata.md`

**Páginas existentes atualizadas (backlinks):**
- `wiki/concepts/dizer-sim-para-tudo.md`
- `wiki/concepts/log-de-aprendizado.md`

**Questões abertas levantadas:**
- Habit stacking com Pomodoro funciona para devs em ambiente de muitas reuniões?
- Escrever blog em PT-BR vs EN — trade-off de alcance vs naturalidade?

**Notas:** Fonte dupla — artigo técnico de Tom Hombergs + transcrição de vídeo PT-BR (speaker não identificado, 2013–2015). Nova seção "Hábitos & Produtividade" criada no index.

---

## [2026-04-22] ingest | Bulkhead

**Source:** [[sources/bulkhead]]
**Skill:** `tech-mentor-system-design` → `references/graceful-degradation.md`

**Páginas criadas:**
- `wiki/sources/bulkhead.md`
- `wiki/concepts/bulkhead.md`
- `wiki/concepts/circuit-breaker.md` (stub)
- `wiki/concepts/blast-radius.md` (stub)
- `wiki/concepts/fail-fast.md` (stub)
- `wiki/concepts/littles-law.md` (stub)
- `wiki/concepts/graceful-degradation.md` (stub)

**Questões abertas levantadas:**
- Overhead de gerenciar N pools em serviços com 20+ downstreams?
- Bulkhead de semáforo vs pool de threads — quando cada um?

**Notas:** Primeira ingest do domínio de resiliência. Analogia naval como fio condutor. Conceitos circuit-breaker, blast-radius, fail-fast, graceful-degradation criados como stubs — precisam de sources próprias.

---

## [2026-04-22] ingest | Banco de Dados

**Source:** [[sources/banco-de-dados]]
**Skill:** `tech-mentor-system-design` → `references/read-replicas-pooling.md`

**Páginas criadas:**
- `wiki/sources/banco-de-dados.md`
- `wiki/concepts/acid.md`
- `wiki/concepts/nosql.md`
- `wiki/concepts/database-index.md`
- `wiki/concepts/database-transactions.md`
- `wiki/concepts/read-replicas.md`
- `wiki/concepts/read-your-writes.md`
- `wiki/concepts/connection-pooling.md`
- `wiki/concepts/n-plus-one.md`
- `wiki/concepts/postgresql.md`
- `wiki/concepts/relational-vs-nosql.md`

**Questões abertas levantadas:**
- Quando pg_vector compete com Pinecone/Weaviate em produção?
- Qual threshold de read/write justifica read replica vs escalar vertical?

**Notas:** Primeira ingest do domínio de banco de dados. Source é material do tech-mentor skill — fundamentos pragmáticos com código de referência em SQL + TypeScript/Prisma.

---

## [2026-04-22] ingest | React — Tudo que você precisa saber

**Source:** [[sources/react-tudo-que-voce-precisa-saber]]
**Skill:** `tech-mentor-frontend` → `references/frameworks/react-core.md`

**Páginas criadas:**
- `wiki/sources/react-tudo-que-voce-precisa-saber.md`
- `wiki/entities/react.md`
- `wiki/concepts/jsx.md`
- `wiki/concepts/useState.md`
- `wiki/concepts/useEffect.md`
- `wiki/concepts/useRef.md`
- `wiki/concepts/useReducer.md`
- `wiki/concepts/useMemo.md`
- `wiki/concepts/useCallback.md`
- `wiki/concepts/context-api.md`
- `wiki/concepts/custom-hooks.md`
- `wiki/concepts/error-boundary.md`
- `wiki/concepts/compound-components.md`
- `wiki/concepts/container-presenter.md`
- `wiki/concepts/concurrent-mode.md`
- `wiki/concepts/feature-sliced-architecture.md`

**Questões abertas levantadas:**
- Quando o React Compiler sair de beta, `useMemo`/`useCallback` tornam-se anti-padrão?
- Como integrar Error Boundaries com frameworks de logging (Sentry, Datadog)?

**Notas:** Primeira ingest do wiki. Estrutura de diretórios criada do zero.

---

## [2026-04-22] ingest | TanStack Query — Tudo que você precisa saber

**Source:** [[sources/tanstack-query-tudo-que-voce-precisa-saber]]
**Skill:** `tech-mentor-frontend` → `references/frameworks/react-state.md`

**Páginas criadas:**
- `wiki/sources/tanstack-query-tudo-que-voce-precisa-saber.md`
- `wiki/entities/tanstack.md`
- `wiki/concepts/tanstack-query.md`
- `wiki/concepts/server-state.md`
- `wiki/concepts/query-key.md`
- `wiki/concepts/optimistic-updates.md`
- `wiki/concepts/infinite-query.md`
- `wiki/concepts/swr.md`

**Páginas existentes tocadas (backlinks adicionados via source page):**
- `wiki/concepts/error-boundary.md` — referenciado via integração com QueryErrorResetBoundary
- `wiki/concepts/useEffect.md` — referenciado como anti-padrão substituído pelo TQ
- `wiki/entities/react.md` — TanStack Query adicionado ao ecossistema

**Questões abertas levantadas:**
- Com RSC no Next.js, qual o papel do TanStack Query no cliente em apps 100% Server Components?
- `useSuspenseQuery` + Streaming SSR — como funciona o handoff servidor→cliente?

---

## [2026-04-22] ingest | Design First vs Code First — Abordagens e Referências de Design

**Source:** [[sources/design-first-vs-code-first-referencias]]
**Skill:** `tech-mentor-frontend` → `references/mobile-frontend/design-systems.md`

**Páginas criadas:**
- `wiki/sources/design-first-vs-code-first-referencias.md`
- `wiki/concepts/design-first.md`
- `wiki/concepts/code-first.md`
- `wiki/concepts/design-engineer.md`
- `wiki/concepts/fake-delay.md`
- `wiki/entities/linear-app.md`
- `wiki/entities/figma.md`
- `wiki/entities/dribbble.md`
- `wiki/entities/lovable.md`

**Notas:** Fonte é transcrição de vídeo/aula — speaker não identificado. Linguagem coloquial preservada na source page. Conceito de fake delay tem implementação técnica concreta (Promise.all + setTimeout) adicionada pelo skill.

**Questões abertas levantadas:**
- Paper (o "Figma para devs") estabilizou? Vale adotar?
- Qual o threshold certo de fake delay por tipo de ação?

---

## [2026-04-22] ingest | useEffect — Problemas, Armadilhas e Soluções

**Source:** [[sources/useeffect-problemas-e-solucoes]]
**Skill:** `tech-mentor-frontend` → `references/frameworks/react-core.md`

**Páginas criadas:**
- `wiki/sources/useeffect-problemas-e-solucoes.md`
- `wiki/concepts/derived-state.md`
- `wiki/concepts/stale-closure.md`
- `wiki/concepts/race-condition.md`

**Páginas existentes atualizadas:**
- `wiki/concepts/useEffect.md` — seção de anti-padrões adicionada, backlink, regra de ouro
- `wiki/concepts/useMemo.md` — backlink para derived-state

**Questões abertas levantadas:**
- Existe caso legítimo de effect encadeado que não pode ser colapsado em cálculo direto?
- Qual o limite de complexidade na renderização antes de ser obrigatório usar `useMemo`?

---

## [2026-04-22] ingest | Desenvolvedor Acima da Média — 10 Itens para se Destacar

**Source:** [[sources/desenvolvedor-acima-da-media-10-itens]]
**Skill:** `tech-mentor-leadership` → `career-progression.md`, `technical-mentoring.md`, `engineering-hiring.md`

**Páginas criadas:**
- `wiki/sources/desenvolvedor-acima-da-media-10-itens.md`
- `wiki/concepts/dev-e-negocio.md`
- `wiki/concepts/ownership-proativo.md`
- `wiki/concepts/contratacao-barra-alta.md`
- `wiki/concepts/mentoria-tecnica.md`
- `wiki/concepts/one-on-one.md`
- `wiki/concepts/prova-de-conceito.md`
- `wiki/concepts/flexibilidade-tecnica.md`
- `wiki/concepts/extreme-ownership.md`
- `wiki/concepts/problema-com-solucao.md`

**Notas:** Primeira ingest de domínio de liderança/carreira — skill trocada de `tech-mentor-frontend` para `tech-mentor-leadership`. Source é transcrição de vídeo com speaker "Felipe" (sobrenome não identificado). Lista original tem 60 itens; apenas 10 foram abordados.

**Questões abertas levantadas:**
- A lista completa do "Liro Boy" (60 itens) vale ser ingerida?
- Como equilibrar ownership proativo (item 2) com flexibilidade técnica (item 7) quando você é o único com contexto?

---

## [2026-04-22] ingest | 4 Hábitos Ruins de Programador

**Source:** [[sources/habitos-ruins-de-programador]]
**Skill:** `tech-mentor-leadership` → `references/software-craftsmanship.md`

**Páginas criadas:**
- `wiki/sources/habitos-ruins-de-programador.md`
- `wiki/concepts/dizer-sim-para-tudo.md`
- `wiki/concepts/definicao-de-pronto.md`
- `wiki/concepts/testar-proprio-codigo.md`
- `wiki/concepts/atomic-commits.md`

**Páginas existentes atualizadas:**
- `wiki/concepts/mentoria-tecnica.md` — backlink adicionado

**Questões abertas:**
- Tamanho ideal de PR em linhas — existe referência empírica?
- Como dizer não sem parecer não-colaborativo em cultura de "sempre ajudar"?

---

## [2026-04-22] ingest batch | Testing — 6 fontes (Pirâmide, TDD, Test Doubles, BDD, Contract Testing, Living Documentation)

**Skill:** `tech-mentor-testing` → `references/test-patterns.md`

**Páginas criadas:**
- `wiki/sources/piramide-de-testes.md`
- `wiki/sources/tdd.md`
- `wiki/sources/test-doubles.md`
- `wiki/sources/bdd.md`
- `wiki/sources/contract-testing.md`
- `wiki/sources/living-documentation.md`
- `wiki/concepts/piramide-de-testes.md`
- `wiki/concepts/tdd.md`
- `wiki/concepts/test-doubles.md`
- `wiki/concepts/bdd.md`
- `wiki/concepts/contract-testing.md`
- `wiki/concepts/living-documentation.md`

**Notas:** Primeira ingest do domínio de testes — skill trocada para `tech-mentor-testing`. 6 arquivos estruturados do raw/ ingeridos em batch. Conceitos cobrem toda a estratégia: da pirâmide ao contrato de serviços. Living Documentation fecha o ciclo BDD → output navegável.

**Questões abertas levantadas:**
- Mutation testing (Stryker) vale um source próprio? Não coberto nesta batch.
- Chaos engineering como extensão de E2E — quando faz sentido introduzir?

---

## [2026-04-22] ingest | Comparação na Carreira Dev — Como Não Desistir Antes de Tentar

**Source:** [[sources/comparacao-na-carreira-dev]]
**Skill:** `tech-mentor-leadership` → `references/career-progression.md`

**Páginas criadas:**
- `wiki/sources/comparacao-na-carreira-dev.md`
- `wiki/concepts/comparacao-na-carreira.md`
- `wiki/concepts/familiaridade-vs-capacidade.md`
- `wiki/concepts/log-de-aprendizado.md`
- `wiki/concepts/linha-de-largada.md`

**Notas:** Transcrição de vídeo PT-BR por speaker feminina (nome não identificado). Foco em mentalidade de iniciante — comparação, síndrome do impostor, ferramentas práticas para medir evolução. Primeira source sobre mentalidade de aprendizado (vs carreira sênior/liderança das ingests anteriores).

**Questões abertas levantadas:**
- Quando a comparação deixa de ser nociva e vira benchmark útil? (ex: trilha de carreira da empresa)
- Como manter o log de aprendizado sem virar overhead burocrático?

## [2026-04-24] ingest batch | Go — 8 fontes (Fundamentos, Concorrência, Arquitetura, Avançado, Ecossistema, OOP/Composição, Produção, Stdlib)

**Skill:** `lang-systems`

**Páginas criadas:**
- `wiki/sources/go-fundamentos.md`
- `wiki/sources/go-concorrencia.md`
- `wiki/sources/go-arquitetura.md`
- `wiki/sources/go-avancado.md`
- `wiki/sources/go-ecossistema.md`
- `wiki/sources/go-oop-composicao.md`
- `wiki/sources/go-producao.md`
- `wiki/sources/go-stdlib.md`
- `wiki/concepts/go-fundamentos.md`
- `wiki/concepts/go-concorrencia.md`
- `wiki/concepts/go-arquitetura.md`
- `wiki/concepts/go-avancado.md`
- `wiki/concepts/go-ecossistema.md`
- `wiki/concepts/go-oop-composicao.md`
- `wiki/concepts/go-producao.md`
- `wiki/concepts/go-stdlib.md`

**Notas:** Primeira ingest do domínio Go. 8 arquivos raw ingeridos cobrindo a linguagem do zero ao prod: tipos/slices/maps, concorrência CSP, clean architecture sem DI framework, generics/reflection/cgo, ecossistema Chi+sqlc, OOP via composição, observabilidade com Prometheus/OTel/pprof, stdlib essencial. Todos os conceitos interligados com [[backlinks]] entre si e com conceitos existentes (clean-architecture, hexagonal-architecture, observabilidade, zero-downtime-deploy, distributed-locks).

**Questões abertas levantadas:**
- go-is-not-java (já existente) pode ser refatorado para linkar com os novos conceitos.
- go-core (raw/go-core.md) ainda não tem source page — o conteúdo sobrepõe com go-concorrencia e go-oop-composicao.

## [2026-04-24] ingest batch | Mobile — 27 fontes

**Skill:** `tech-mentor-mobile`

**Páginas criadas (sources):**
- `wiki/sources/mobile-animacoes-performaticas.md`
- `wiki/sources/mobile-armazenamento-local.md`
- `wiki/sources/mobile-baseline-profiles.md`
- `wiki/sources/mobile-biometria.md`
- `wiki/sources/mobile-chamadas-http.md`
- `wiki/sources/mobile-cicd.md`
- `wiki/sources/mobile-cross-platform-decision.md`
- `wiki/sources/mobile-deep-links.md`
- `wiki/sources/mobile-design-system.md`
- `wiki/sources/mobile-feature-flags.md`
- `wiki/sources/mobile-kmp.md`
- `wiki/sources/mobile-layouts-responsivos.md`
- `wiki/sources/mobile-metricas-criticas.md`
- `wiki/sources/mobile-monetizacao.md`
- `wiki/sources/mobile-monitoramento.md`
- `wiki/sources/mobile-navegacao.md`
- `wiki/sources/mobile-offline-first-avancado.md`
- `wiki/sources/mobile-offline-first-basico.md`
- `wiki/sources/mobile-on-device-ai.md`
- `wiki/sources/mobile-performance-listas.md`
- `wiki/sources/mobile-permissoes.md`
- `wiki/sources/mobile-profiling.md`
- `wiki/sources/mobile-publicacao-aso.md`
- `wiki/sources/mobile-push-notifications.md`
- `wiki/sources/mobile-seguranca.md`
- `wiki/sources/mobile-state-management-global.md`
- `wiki/sources/mobile-state-management-local.md`
- `wiki/sources/mobile-testes.md`

**Páginas criadas (concepts):** 27 conceitos espelhando os sources acima, com código de exemplo e backlinks cruzados.

**Notas:** Cobertura completa do domínio mobile — do nível básico (layouts, navegação, state local) ao avançado (KMP, on-device AI, offline sync com CRDT, baseline profiles). Todos os conceitos interligados entre si e com conceitos existentes (feature-flags, cicd-pipeline, observabilidade, crdt-colaboracao-tempo-real, piramide-de-testes, autenticacao-segura).

**Questões abertas levantadas:**
- mobile-security (source já existente de outra batch) e mobile-seguranca (novo) cobrem temas sobrepostos — candidato a merge/lint.
- mobile-platform-engineering (já existente) referencia shared-sdk/adapter-pattern que agora têm mais contexto nos novos concepts.
