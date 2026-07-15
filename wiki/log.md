# Wiki Log

---

## [2026-07-15] ingest | O Que É Refatoração (e Quando Usar)

**Fonte:** [[wiki/sources/o-que-e-refatoracao-quando-usar]] — transcrição de fala corrida em português (sem necessidade de tradução), limpa e organizada em seções, salva em `raw/o-que-e-refatoracao-quando-usar.md`. Vídeo introdutório de [[wiki/entities/bernardo-lobato]] anunciando uma possível série sobre refatoração no canal.

**Skill carregada:** `tech-mentor-backend`, `references/software-craftsmanship.md` (seção "Technical Debt — Quadrantes e Estratégia de Pagamento", que já cobre Boy Scout Rule e o alerta contra "refactoring project" de 6 meses com feature freeze) — mesma skill já usada em [[wiki/sources/design-pattern-adapter]] e [[wiki/sources/design-pattern-facade]].

**Páginas criadas:**
- `wiki/sources/o-que-e-refatoracao-quando-usar.md`
- `wiki/concepts/refatoracao.md` — novo conceito central: refatoração como mudança de estrutura interna sem alterar comportamento externo, com pilares (dois chapéus, passos pequenos, testes como rede de segurança) e critérios de quando/quando não refatorar
- `wiki/concepts/dois-chapeus-kent-beck.md` — novo conceito: metáfora de Kent Beck para adicionar funcionalidade e refatorar como atividades mutuamente exclusivas no tempo

**Páginas atualizadas:**
- `wiki/concepts/god-object.md` — nova seção "Como uma God Class nasce sprint a sprint", exemplo narrativo de degradação incremental sob prazo; `source_count` 2 → 3
- `wiki/concepts/piramide-de-testes.md` — nova seção ligando a base da pirâmide ao pré-requisito de segurança para refatorar (E2E citado como caro/lento demais para esse ciclo); `source_count` 4 → 5
- `wiki/concepts/tech-debt-como-ferramenta.md` — nova seção "Quando refatoração vira débito técnico", critério prático (horas/dias de esforço) complementar ao Quadrante de Fowler; `source_count` 5 → 6
- `wiki/concepts/boy-scout-rule.md` — nota distinguindo Boy Scout Rule (micro-limpeza) de refatoração oportunista (reestruturação maior); `source_count` 1 → 2
- `wiki/entities/martin-fowler.md` — nova seção "Autor do livro-fonte de Refatoração" (política de bugs encontrados durante refatoração; gráficos de tempo de entrega); `source_count` 2 → 3
- `wiki/entities/kent-beck.md` — nova seção sobre a metáfora dos dois chapéus; `source_count` 1 → 2
- `wiki/entities/bernardo-lobato.md` — nova linha em Key Sources; `source_count` 1 → 2
- `wiki/index.md` — nova linha em Sources; duas novas linhas em Concepts (seção "Padrões e Design")

**Notas:** Fonte é uma introdução de série, propositalmente na superfície — o autor adia code smells, catálogo de técnicas de Fowler e "como refatorar com segurança usando testes" para vídeos futuros. A wiki já tinha material adjacente maduro ([[wiki/concepts/tech-debt-como-ferramenta]], [[wiki/concepts/boy-scout-rule]], [[wiki/concepts/god-object]], [[wiki/concepts/piramide-de-testes]]) mas nenhuma página dedicada ao conceito central de refatoração em si — daí a criação de [[wiki/concepts/refatoracao]] como página nova, não apenas mais uma seção espalhada. Reforça sem contradizer: a política de bugs durante refatoração (deixar bug conhecido, corrigir só bug novo com certeza absoluta) e a metáfora dos dois chapéus de Kent Beck são citações nomeadas e específicas, ambas consistentes com o material já presente sobre TDD (RED-GREEN-REFACTOR) e sobre o Quadrante de Fowler. Open questions registradas na fonte: não há heurística objetiva para o limiar "refatoração oportunista vs. vira débito técnico" além de bom senso; a citação atribuída ao livro de Fowler sobre bugs é paráfrase, não citação textual — vale confirmar numa ingestão futura do próprio livro.

---

## [2026-07-15] ingest | Análise de Currículos de Programador Júnior — Dicas de ATS e Portfólio

**Fonte:** [[wiki/sources/analise-curriculos-programador-junior-dicas-ats]] — transcrição de fala corrida em português (sem necessidade de tradução), limpa e organizada em seções por candidato, salva em `raw/analise-curriculos-programador-junior-dicas-ats.md`. Vídeo de reação a currículos enviados por espectadores de um curso/comunidade não identificada com confiança na transcrição.

**Skill carregada:** `tech-mentor-leadership` — carregado `SKILL.md` em `/home/gabriel-martins/Documentos/skills/tech-mentor-leadership/` (path real deste ambiente; o CLAUDE.md referencia `/home/nemomartins/...`, que não existe aqui). Consultado `references/leadership/engineering-hiring.md` para calibrar o vocabulário de triagem/processo seletivo.

**Páginas criadas:**
- `wiki/sources/analise-curriculos-programador-junior-dicas-ats.md`
- `wiki/concepts/otimizacao-ats-curriculo.md` — novo conceito: repetição de palavras-chave da stack-alvo no currículo para passar no filtro automático (ATS) antes da avaliação humana

**Páginas atualizadas:**
- `wiki/concepts/curriculo-vs-portfolio.md` — nova seção "Na prática de triagem: GitHub ativo como prova mínima" com caso real de descarte por ausência de link; `source_count` 2 → 3
- `wiki/concepts/portfolio-backend-junior.md` — nova seção "Antes do portfólio: passar na triagem" ligando o filtro de ATS/GitHub como etapa anterior ao portfólio técnico em si; `source_count` 2 → 3
- `wiki/index.md` — nova linha em Sources; nova linha em Concepts

**Notas:** Fonte de baixa densidade técnica mas alta especificidade prática — é uma reação ao vivo a currículos reais, não um artigo teórico, então grande parte do conteúdo é avaliação caso a caso (seis candidatos, a maioria rejeitada por falta de GitHub, formatação ruim ou cores/fonte problemáticas). O ponto novo o suficiente para virar página própria foi a mecânica de ATS (contagem de menções de palavra-chave), que a wiki já tocava de raspão em outras fontes de carreira mas nunca tinha detalhado como conceito — daí [[wiki/concepts/otimizacao-ats-curriculo]]. O restante do conteúdo (GitHub como prova, formatação, discurso de "pensar produto", conhecimento de IA aplicada no currículo) encaixou como reforço direto em [[wiki/concepts/curriculo-vs-portfolio]] e [[wiki/concepts/portfolio-backend-junior]], sem contradição com o que já existia. Nenhuma entidade nova foi criada: o apresentador não se identifica na transcrição, e os candidatos avaliados são pessoas privadas (nomes completos citados), não entidades de relevância pública para a wiki — decisão deliberada de não criar páginas de entidade para eles. Open question registrada na fonte: nome do canal/apresentador não identificado com confiança.

---

## [2026-07-15] ingest | Portas de Rede — Como Funcionam

**Source:** [[wiki/sources/portas-de-rede-como-funcionam]] — transcrição de vídeo em inglês (fala corrida, sem pontuação), traduzida para português e organizada em seções, salva em `raw/portas-de-rede-como-funcionam.md`.

**Skill:** `tech-mentor-networking` — carregado `SKILL.md` em `/home/gabriel-martins/Documentos/skills/tech-mentor-networking/` (path real deste ambiente; o CLAUDE.md referencia `/home/nemomartins/...`, que não existe aqui). Consultado `references/protocols-transport.md` para calibrar terminologia de estados de conexão (`LISTEN`/`ESTABLISHED`/`TIME_WAIT`/`CLOSE_WAIT`) e confirmar que `ss` é o substituto moderno de `netstat` no Linux — a fonte usa `netstat` (Windows), então essa diferença de ferramenta por plataforma foi registrada como nota, não como contradição.

**Páginas criadas:**
- `wiki/sources/portas-de-rede-como-funcionam.md`
- `wiki/concepts/porta-de-rede.md` — novo conceito central; nenhuma página existente descrevia porta como conceito próprio (apenas mencionada de passagem em `protocolo-de-rede`, `ssh`, `load-balancer`)
- `wiki/entities/iana.md` — nova entidade; autoridade citada como gestora de IPs, domínios e portas, sem página própria até então

**Páginas atualizadas:**
- `wiki/concepts/protocolo-de-rede.md` — nova seção "Porta: o endereçamento dentro do host", ligando `IP:porta` ao modelo em camadas já documentado; `source_count` 5 → 6
- `wiki/concepts/dns.md` — nota distinguindo resolução de nome (DNS) de resolução de serviço (porta), duas camadas de endereçamento complementares; `source_count` 1 → 2
- `wiki/concepts/ssh.md` — nova frase relacionando a porta 22 (well-known port do SSH) à diretiva `Port` já documentada em `~/.ssh/config`/`sshd_config`; `source_count` 1 → 2
- `wiki/concepts/load-balancer.md` — nova frase explicando que o roteamento "cego" do L4 é literalmente ler `IP:porta` sem abrir o payload; `source_count` 7 → 8
- `wiki/index.md` — nova linha em Sources; nova linha em Concepts (seção de fundamentos de rede); nova linha em Entities

**Notas:** Fonte introdutória/fundamentos (nível iniciante), mas preenchia uma lacuna real: o wiki já tinha várias páginas mencionando portas de passagem (443 em SSE/WebSocket, 22 em SSH, `IP:porta` em load balancer) sem nenhuma página que tratasse "porta" como conceito de primeira classe com suas três faixas IANA e a distinção servidor (well-known/registered) vs. cliente (dynamic/ephemeral). Essa distinção — portas dinâmicas existem para demultiplexar respostas no lado do cliente, não para identificar serviços — não estava formalizada em nenhuma página antes desta ingestão. Sem contradições com o resto do wiki; a única discrepância é de ferramenta (netstat vs. ss), documentada como nota de plataforma, não como erro da fonte. Open question registrada na fonte: ela não distingue portas TCP de portas UDP (o conceito de porta é agnóstico ao transporte, mas isso ficou implícito, não explícito, no vídeo original).

---

## [2026-07-10] ingest | HMAC: Integridade de Mensagem em Local-First (Entrevista de System Design)

**Source:** [[wiki/sources/hmac-integridade-mensagem-local-first-entrevista]] — transcrição bruta de ASR (fala em bloco único, sem pontuação) colada pelo usuário, já em português (sem necessidade de tradução), reescrita como markdown estruturado por etapa de raciocínio em `raw/hmac-integridade-mensagem-local-first-entrevista.md`.
**Skill:** tech-mentor-security — carregado `SKILL.md` e `references/crypto.md` em `/home/gabriel-martins/Documentos/skills/tech-mentor-security/` (path real deste ambiente; o CLAUDE.md referencia `/home/nemomartins/...`, que não existe aqui). A referência já cobre HMAC (seção "Assinaturas Digitais e HMAC", com a tabela HMAC vs. assinatura assimétrica) mas não detalha a construção interna ipad/opad — a fonte preenche exatamente essa lacuna de mecânica do algoritmo.

**Páginas criadas:**
- `wiki/sources/hmac-integridade-mensagem-local-first-entrevista.md`
- `wiki/concepts/hmac.md` — novo conceito; mecânica da construção HMAC (ipad `0x36`/opad `0x5C`, normalização de chave, duas etapas de hash) que não tinha página própria — `webhook-signature-validation.md` já usava HMAC como caixa-preta, sem explicar por que a construção é resistente a ataque de extensão de mensagem
- `wiki/concepts/local-first.md` — novo conceito; padrão de tratar dado do cliente como fidedigno para evitar custo de storage/lookup no servidor, com HMAC como mecanismo de integridade

**Páginas atualizadas:**
- `wiki/concepts/webhook-signature-validation.md` — `source_count` 1 → 2; nova seção "Como o HMAC é construído por baixo" linkando para o novo conceito
- `wiki/concepts/criptografia.md` — `source_count` 2 → 3; nova seção "HMAC: um meio-termo entre hash e assinatura assimétrica"
- `wiki/concepts/encryption.md` — `source_count` 2 → 3; nova seção "Integridade sem confidencialidade: quando encryption é a ferramenta errada"
- `wiki/index.md` — nova linha em Sources; duas novas linhas em Concepts na seção de Segurança

**Notas:** Nenhuma contradição com a wiki existente — a fonte converge com `references/crypto.md` da skill (mesma tabela HMAC vs. assinatura assimétrica, mesmo motivo de custo computacional) e complementa `webhook-signature-validation.md` com a camada de mecânica interna que faltava. Duas lacunas da fonte registradas como Open Questions em `wiki/sources/hmac-integridade-mensagem-local-first-entrevista.md`: (1) o esquema descrito não tem timestamp/nonce contra replay, ao contrário do padrão já documentado para webhooks; (2) não fecha qual algoritmo de hash de bloco de 64 bytes é usado na prática além de citar MD5/SHA-1 como exemplo de tamanho de bloco. Autor/canal não identificado na transcrição — nenhuma entidade nova.

---

## [2026-04-22] ingest | 9 Hábitos que eu gostaria de ter aprendido sendo Programador Júnior

**Source:** [[wiki/sources/9-habitos-programador-junior]] — transcrição de vídeo PT-BR (transcrição de fala corrida, sem pontuação) já em português, reescrita como markdown estruturado em `raw/9-habitos-programador-junior.md`, cruzada com o artigo original "9 Habits I Wish I Had as a Junior Developer" de Tom Hombergs.
**Skill:** tech-mentor-leadership.

**Páginas criadas:**
- `wiki/sources/9-habitos-programador-junior.md`
- `wiki/entities/tom-hombergs.md`
- `wiki/concepts/voluntariar-para-desconhecido.md`
- `wiki/concepts/comunicar-progresso.md`
- `wiki/concepts/escrever-para-aprender.md`
- `wiki/concepts/bloqueio-de-agenda.md`
- `wiki/concepts/pausa-estrategica.md`
- `wiki/concepts/fazer-por-voce.md`
- `wiki/concepts/pair-programming.md`
- `wiki/concepts/pomodoro.md`
- `wiki/concepts/documentar-conquistas.md`
- `wiki/concepts/sem-balas-de-prata.md`

**Notas:** Entrada registrada retroativamente — as páginas já existiam no repositório (ingest anterior a este log ter sido consultado), mas `wiki/index.md` e `wiki/log.md` não tinham o registro correspondente. Este commit fecha esse drift, sem alterar o conteúdo já ingerido.

---

## [2026-07-10] ingest | Testes Unitários, Integração e E2E — uma conversa opinativa

**Source:** [[wiki/sources/teste-unitario-integracao-e2e-opiniao]] — transcrição bruta de ASR (fala corrida, sem pontuação, com bloco publicitário no meio) colada pelo usuário, já em português (sem necessidade de tradução), reescrita como markdown estruturado em `raw/teste-unitario-integracao-e2e-opiniao.md`. O bloco de patrocínio (curso de investimentos) foi preservado por integridade da transcrição, mas isolado ao final, fora do corpo técnico.
**Skill:** tech-mentor-testing — carregado `SKILL.md` em `/home/gabriel-martins/Documentos/skills/tech-mentor-testing/` (path real do repo). O índice da skill mapeia pirâmide/estratégia de testes, TDD, mocks e test doubles para `references/test-strategy.md` e `references/test-patterns.md`; conteúdo da fonte é consistente com o material de referência, sem contradições — é essencialmente uma opinião pessoal sobre como *alocar* investimento entre as três camadas já bem documentadas na wiki, não uma reformulação técnica delas.

**Páginas criadas:**
- `wiki/sources/teste-unitario-integracao-e2e-opiniao.md`
- `wiki/concepts/criterios-de-bom-teste.md` — novo conceito; formaliza os cinco critérios (determinístico, conciso, relevante, compreensível, durável) que a fonte usa para avaliar testes de qualquer camada, e que não tinham página própria na wiki (apareciam espalhados/implícitos em `piramide-de-testes.md` e `gaming-de-testes-por-ia.md`)

**Páginas atualizadas:**
- `wiki/concepts/piramide-de-testes.md` — `source_count` 3 → 4; nova seção "Não é bem uma pirâmide — é alocação de recursos", com a tese central da fonte (custo de dev-time/infra como restrição real) e o achado de que E2E vale desproporcionalmente mais em código legado sem dono e desproporcionalmente menos em startups em pivot constante
- `wiki/concepts/tdd.md` — `source_count` 5 → 6; nova seção curta ligando "100% coverage ≠ ausência de bugs" a [[wiki/concepts/criterios-de-bom-teste]]
- `wiki/concepts/test-doubles.md` — `source_count` 2 → 3; nova seção sobre o limite do mock de banco (assertion de chamada não prova persistência)
- `wiki/concepts/testar-proprio-codigo.md` — `source_count` 3 → 4; nova seção reforçando que testar além do happy path não garante ausência de bug, só não-regressão do que já foi pensado
- `wiki/concepts/gaming-de-testes-por-ia.md` — `source_count` 1 → 2; nova seção ligando testes flaky/irrelevantes a serem terreno mais fácil para gaming (humano ou IA) — a fonte menciona explicitamente "vibe coding" mudando testes que falham em vez de corrigir o código, reforçando o padrão já documentado nesta página
- `wiki/concepts/testes-integracao-banco-real.md` — `source_count` 2 → 3; nova seção sobre mock de banco mal pensado "não integrar de verdade"
- `wiki/concepts/contract-testing.md` — `source_count` 2 → 3; nova seção sobre mockar as pontas de um fluxo (ex. PSP/fornecedor) como alternativa mais barata a ativar dependências reais
- `wiki/concepts/teste-de-integracao-estreito-vs-amplo.md` — `source_count` 1 → 2; linha adicional em Key Sources com o caso prático de "amplo" ambíguo em sistema com dependências externas
- `wiki/concepts/unit-test-solitario-vs-sociavel.md` — `source_count` 1 → 2; linha adicional em Key Sources com o exemplo da fonte (teste de `add` que socializa ao ganhar um `db.save` real)
- `wiki/index.md` — nova linha em Sources; nova linha em "Testes & Qualidade" para `criterios-de-bom-teste`

**Notas:** Nenhuma contradição encontrada com o que já estava documentado — a fonte é convergente com `piramide-de-testes.md`, `teste-de-integracao-estreito-vs-amplo.md` e `testes-integracao-banco-real.md`, mas adiciona uma camada de opinião/julgamento de custo-benefício que a wiki ainda não tinha explícita (a pirâmide como problema de alocação de recursos, não como hierarquia fixa). O autor/canal não se identifica na transcrição, então nenhuma entidade de autoria foi criada — registrado como open question na source. `raw/` contém a transcrição bruta original preservada (incluindo o trecho publicitário), sem edição de conteúdo.

---

## [2026-07-10] ingest | Estruturas de Dados, Algoritmos e Big O — Como Escolher

**Source:** [[wiki/sources/estruturas-de-dados-algoritmos-big-o-como-escolher]] — transcrição bruta de ASR (fala em bloco único, sem pontuação) colada pelo usuário, já em português (sem necessidade de tradução), reescrita como markdown estruturado em `raw/estruturas-de-dados-algoritmos-big-o-como-escolher.md`. É a continuação direta anunciada em [[wiki/sources/estruturas-de-dados-pratica-array-hashmap-fila-pilha-arvore]] ("o vídeo anuncia continuação sobre Big O" — open question já registrada naquela fonte).
**Skill:** cs-fundamentals — carregado `SKILL.md` em `/home/gabriel-martins/Documentos/skills/cs-fundamentals/` (path real do repo; o CLAUDE.md referencia um path antigo `/home/nemomartins/...` que não existe mais neste ambiente). Índice apontou para `references/algorithms-complexity.md`, consultado para validar a formalização O/Θ/Ω (limite superior/exato/inferior = pior/médio/melhor caso) e a análise amortizada — claims da fonte consistentes com a referência, sem contradições.

**Páginas criadas:**
- `wiki/sources/estruturas-de-dados-algoritmos-big-o-como-escolher.md`
- `wiki/concepts/melhor-caso-pior-caso-caso-medio.md` — novo conceito; formaliza a distinção que a fonte introduz via exemplo de busca linear
- `wiki/concepts/time-space-tradeoff.md` — novo conceito; também fecha um link quebrado: [[wiki/sources/two-sum-explicacao]] já referenciava `[[concepts/time-space-tradeoff]]` desde 2026-04-23 sem a página existir

**Páginas atualizadas:**
- `wiki/concepts/big-o.md` — `source_count` 2 → 3; nova seção "As quatro curvas essenciais para começar" (O(1)/O(n)/O(log n)/O(n²) como ponto de partida antes da tabela completa) e nova frase de abertura sobre por que medir em milissegundos engana
- `wiki/concepts/algoritmos-e-estruturas-de-dados.md` — `source_count` 6 → 7; nova seção "Como escolher a estrutura certa: operação primeiro" com o framework de quatro perguntas e a distinção estrutura de dados vs. algoritmo
- `wiki/concepts/array.md`, `wiki/concepts/hashmap.md`, `wiki/concepts/fila.md` — `source_count` +1 cada; linha em Key sources amarrando ao exemplo específico usado na fonte (array como ponto de partida didático; hashmap como exemplo do trade-off tempo/memória; fila como exemplo de "operação onde ordem de chegada importa")
- `wiki/concepts/algoritmos-de-busca.md` — `source_count` 1 → 2; busca linear agora documenta melhor caso O(1) além de pior/médio O(n); link para o novo conceito de melhor/pior/caso médio
- `wiki/index.md` — nova linha em Sources; duas novas linhas em "Fundamentos de CS" para os conceitos criados

**Notas:** Conteúdo não contradiz nada já registrado — é estritamente aditivo e formaliza o que a fonte anterior deixou como pergunta em aberto. Nenhuma entidade nova. `raw/` recebeu apenas o novo arquivo desta transcrição; nenhum arquivo existente foi tocado.

---

## [2026-07-09] ingest | Double Spend / Double Submit

**Source:** [[wiki/sources/double-spend-double-submit]] — transcrição bruta de ASR (fala em bloco único, sem pontuação, com propaganda de patrocinador intercalada) colada pelo usuário, já em português (sem necessidade de tradução), reescrita como markdown estruturado por camada de solução em `raw/double-spend-double-submit.md`
**Skill:** tech-mentor-backend — carregado `SKILL.md` em `/home/gabriel-martins/Documentos/skills/tech-mentor-backend/`; índice apontou para `references/idempotency-patterns.md` como referência específica do tópico (Idempotency, Idempotency Key, Dedup, Upsert, CAS), consultado para calibrar os claims e identificar duas lacunas que o vídeo deixa em aberto (lock de concorrência e TTL por domínio)

**Páginas criadas:**
- `wiki/sources/double-spend-double-submit.md`
- `wiki/concepts/post-redirect-get.md` (stub) — padrão PRG (303 após POST), citado no vídeo como camada que resolve reenvio acidental de formulário mas não abuso deliberado

**Páginas atualizadas:**
- `wiki/concepts/idempotencia.md` — `source_count` 2 → 3; nova seção "Double Spend / Double Submit — a Chave Gerada pelo Servidor" com a variante de gerar a Idempotency Key no servidor via hash dos campos (mais robusta contra abuso deliberado que chave enviada pelo cliente) e tabela comparando as 4 camadas de defesa por tipo de ameaça (duplo clique acidental vs. abuso deliberado)
- `wiki/index.md` — nova linha em Sources (topo da tabela); nova seção "Idempotência & Deduplicação de Requests" com `idempotencia` e `post-redirect-get` (fechando de passagem um drift antigo: nem `idempotencia` nem `retry-backoff` estavam indexados apesar de já existirem como páginas estáveis — `retry-backoff` permanece fora do índice por não ter sido tocado nesta ingestão)

**Notas:** Conteúdo não contradiz [[wiki/concepts/idempotencia]] — na verdade preenche uma lacuna real: a página existente só documentava a Idempotency Key enviada pelo cliente (padrão Stripe), sem discutir a variante mais robusta de gerá-la no servidor via hash determinístico dos campos, nem a distinção entre ameaça acidental (duplo clique) e deliberada (abuso/scripting), que é o eixo central deste vídeo. O vídeo é didático e evita alegações fortes sem qualificação — a maior parte do conteúdo é consistente com `references/idempotency-patterns.md` da skill. Duas lacunas do vídeo ficaram registradas como Open Questions na fonte: falta de discussão sobre lock de concorrência entre requests simultâneos com a mesma chave (a skill cobre isso com um lock key separado do cache key) e ausência de uma estratégia concreta de TTL por tipo de operação (a skill sugere valores diferenciados: pagamento 30 dias, pedido 7 dias). Entidades: nenhuma relevante — o patrocínio (Abacus AI) foi tratado como contexto tangencial, não como entidade da wiki.

---

## [2026-07-09] ingest | Build in Public Já Era: Como Vender um SaaS Sem Audiência

**Source:** [[wiki/sources/como-vender-um-saas-sem-audiencia]] — transcrição bruta de ASR (fala em bloco único, sem pontuação) colada pelo usuário, já em português (sem necessidade de tradução), reescrita como markdown estruturado por tópico em `raw/como-vender-um-saas-sem-audiencia.md`
**Skill:** tech-mentor-leadership — carregado `SKILL.md` em `/home/gabriel-martins/Documentos/skills/tech-mentor-leadership/`. Não há mapeamento exato para "growth/marketing de SaaS indie" na tabela de domínios do CLAUDE.md; usado o mesmo critério já aplicado a `como-eu-investiria-como-programador-ate-50000` (mesmo autor, conteúdo de carreira/negócio fora do escopo puramente técnico) — `references/engineering-brand.md` foi consultado mas cobre marca de engenharia B2B/hiring, não growth de produto consumer, então o conteúdo foi tratado com conhecimento geral de unit economics em vez de mapeado a uma referência específica da skill

**Páginas criadas:**
- `wiki/sources/como-vender-um-saas-sem-audiencia.md`
- `wiki/concepts/ltv-cac.md`
- `wiki/concepts/marketing-organico-viral.md`
- `wiki/concepts/produto-vendivel-desde-o-dia-zero.md`

**Páginas atualizadas:**
- `wiki/entities/lucas-montano.md` — `source_count` 2 → 3; novo parágrafo sobre o produto "Persoa/Pessoa" (pivô de feature, viralização via sketch, mudança do Stupid Button Club para anuidade)
- `wiki/concepts/comunicacao-persuasiva.md` — `source_count` 1 → 2; nova seção "Aplicação em marketing de produto" ligando o princípio de tradução de mensagem (interno, para decisores) ao princípio de sketch que não parece propaganda (externo, para consumidor)
- `wiki/index.md` — nova linha em Sources (topo da tabela); três novas linhas em Concepts na seção "Produto & Lean Startup"

**Notas:** Transcrição já em português — sem necessidade de tradução. Vídeo do mesmo autor de [[wiki/entities/lucas-montano]] (identificado por menções a "Stupid Button Club" e ao produto "Pessoa/Persoa", já presentes na entidade). Conteúdo é predominantemente de growth/marketing de produto (LTV, CAC, viralização orgânica), área não coberta por nenhuma página existente na wiki — as três novas páginas de conceito preenchem essa lacuna e conectam-se a `wiki/concepts/lean-startup.md` e afins na seção "Produto & Lean Startup". Nenhuma contradição encontrada contra conteúdo existente. Questões em aberto registradas na source: o vídeo não apresenta dados concretos de LTV antes/depois do pivô de feature (a causalidade é afirmada, não demonstrada); não fica claro como a sustentabilidade do "hack" de não citar a marca no vídeo se dá em plataformas com políticas anti-spam de comentários; e como a comissão de 10% por conversão é medida quando o tráfego é orgânico sem link rastreável.

---

## [2026-07-09] ingest | 10 Conceitos Fundamentais do Backend

**Source:** [[wiki/sources/10-conceitos-fundamentais-backend]] — canal de vídeo, transcrição bruta de ASR colada pelo usuário (já em português, sem necessidade de tradução), reescrita como markdown estruturado por seções em `raw/10-conceitos-fundamentais-backend.md`
**Skill:** tech-mentor-backend — desta vez a pasta de skills **foi encontrada** neste ambiente em `/home/gabriel-martins/Documentos/skills/tech-mentor-backend/` (caminho local diferente do `/home/nemomartins/...` citado no CLAUDE.md, que aponta para outra máquina); índice de `SKILL.md` consultado para confirmar cobertura de request/response, contratos de API, auth, banco, transações, cache, filas, escalabilidade e observabilidade antes do ingest

**Páginas criadas:**
- `wiki/sources/10-conceitos-fundamentais-backend.md`
- `wiki/concepts/requisicao-resposta.md` (stub)
- `wiki/concepts/contrato-de-api.md` (stub)
- `wiki/concepts/validacao-de-entrada.md` (stub)
- `wiki/concepts/autenticacao-e-autorizacao.md` (stub)
- `wiki/concepts/modelagem-de-dados.md` (stub)
- `wiki/concepts/filas-e-workers.md` (stub) — padrão arquitetural de processamento assíncrono, distinto de [[wiki/concepts/fila]] (estrutura de dados FIFO)

**Páginas atualizadas:**
- `wiki/concepts/cache.md` — nova key source, `source_count` 3→4
- `wiki/concepts/database-transactions.md` — nova key source (mesmo exemplo de transferência bancária), `source_count` 3→4
- `wiki/concepts/observabilidade.md` — nova key source como "meta-conceito nº1", `source_count` 2→5 (corrigido drift: já havia 4 fontes listadas mas frontmatter desatualizado)
- `wiki/concepts/stateless.md` — nova key source, `source_count` 1→2
- `wiki/concepts/alta-disponibilidade.md` — nova key source, `source_count` 1→2
- `wiki/concepts/escalabilidade-horizontal.md` — nova key source, `source_count` 4→5
- `wiki/concepts/escalabilidade-vertical.md` — nova key source, `source_count` 2→3
- `wiki/concepts/load-balancer.md` — nova key source, `source_count` 6→7
- `wiki/concepts/fila.md` — backlink adicionado para `filas-e-workers.md`
- `wiki/index.md` — nova linha em Sources; nova seção "Fundamentos de Backend (Request/Response ao Deploy)" com as 6 páginas novas + `load-balancer`, `alta-disponibilidade` e `observabilidade` (essas três já existiam como páginas estáveis mas nunca haviam entrado no índice — drift antigo fechado de passagem)

**Notas:** Fonte é uma visão geral didática e agnóstica de stack — nenhuma entidade nomeada (produto, empresa, framework específico) foi mencionada, então a seção "Entidades Mencionadas" da fonte ficou vazia. Conteúdo não contradiz nada já existente na wiki; principalmente reforça e conecta conceitos já estáveis (`database-transactions`, `cache`, `escalabilidade-*`, `load-balancer`, `observabilidade`) com uma narrativa de superfície que serve como bom ponto de entrada para quem está aprendendo — o exemplo de transferência bancária em transações é idêntico ao já registrado via [[wiki/sources/acid-vs-base-garantias-bancos-de-dados]]. Três lacunas abertas na própria fonte, registradas em Open Questions: falta de autoria/referências (mesmo padrão de [[wiki/sources/10-conceitos-fundamentais-computacao]]), ausência de detalhamento de estratégias de invalidação de cache e de retry/idempotência em filas, e nenhuma menção a isolation levels em transações.

---

## [2026-07-09] ingest | Como Eu Investiria Se Fosse um Programador Ganhando de R$ Até R$ 50.000

**Source:** [[wiki/sources/como-eu-investiria-como-programador-ate-50000]] — canal de Lucas Montano (YouTube)
**Skill:** tech-mentor-leadership (skill folder de referência não encontrado neste ambiente — `/home/nemomartins/Documentos/new/skills/` citado no CLAUDE.md aponta para outra máquina; ingest seguido sem carregar `SKILL.md`/`references/`, calibrado pelo conteúdo da própria fonte e pelas páginas de carreira/compensação já existentes na wiki)

**Páginas criadas:**
- `wiki/sources/como-eu-investiria-como-programador-ate-50000.md`
- `wiki/concepts/reserva-de-emergencia.md`
- `wiki/concepts/freelance-como-alavanca-de-renda.md`
- `wiki/concepts/dolarizacao-de-renda.md`
- `wiki/concepts/holding-patrimonial.md`

**Páginas atualizadas:**
- `wiki/entities/lucas-montano.md` — `source_count` 1 → 2; segundo vídeo do autor (agora coberto financeiro além de IA/carreira); tags +`financas-pessoais`
- `wiki/concepts/comparacao-na-carreira.md` — `source_count` 2 → 3; nova referência à "régua máxima" de R$ 5.000 do professor como mesmo padrão de comparação externa aplicado a dinheiro
- `wiki/concepts/equity-como-diferencial.md` — `source_count` 1 → 2; nova seção sobre a estratégia de vender 100% do RSU no vesting para diversificar risco de concentração
- `wiki/concepts/raciocinio-matematico-aplicado.md` — `source_count` 1 → 2; link para a aplicação prática da tese (juros compostos, tesouro pré-fixado, IPCA+) no dia a dia financeiro de um dev
- `wiki/index.md` — nova linha em Sources; 4 novas linhas em "Carreira & Soft Skills"

**Notas:** Fonte era transcrição bruta de ASR em português, sem pontuação — reescrita como markdown estruturado por faixa salarial em `raw/como-eu-investiria-como-programador-ate-50000.md`, sem necessidade de tradução. Autor identificado por correspondência de contexto com [[wiki/entities/lucas-montano]] (já existente na wiki desde o ingest de [[wiki/sources/atrofia-cognitiva-ia-programacao]]) — a fonte menciona a comunidade "Stupid Button Club", consistente com o mesmo criador de conteúdo. Conteúdo é o primeiro na wiki dedicado a finanças pessoais para devs; não havia página nenhuma sobre reserva de emergência, dolarização ou holding patrimonial antes desta ingestão, apesar de `wiki/concepts/modelo-trimodal-compensacao.md` e `wiki/concepts/equity-como-diferencial.md` já cobrirem compensação/equity de forma adjacente. Sem contradições encontradas com o restante da wiki. Três questões abertas registradas na própria fonte: números de limite de faturamento de ME e cobertura do FGC não verificados contra fonte primária (podem ter mudado desde a gravação), afirmação sobre justa causa por uso de equipamento da empresa é generalização sem citar cláusula/artigo específico, e detalhes operacionais de "nota de crédito externo" (ticket mínimo, corretoras, tributação exata) não foram dados pelo autor.

---

## [2026-07-09] ingest | Como Criar uma Linguagem de Programação

**Source:** [[wiki/sources/como-criar-uma-linguagem-de-programacao]]
**Skill:** cs-fundamentals (skill folder de referência não encontrado neste ambiente — `/home/nemomartins/Documentos/new/skills/` citado no CLAUDE.md aponta para outra máquina; ingest seguido sem carregar `SKILL.md`/`references/`, calibrado apenas pelo conteúdo da própria fonte e pelas páginas já existentes na wiki sobre o mesmo domínio)

**Páginas criadas:**
- `wiki/sources/como-criar-uma-linguagem-de-programacao.md`
- `wiki/concepts/sistema-de-tipos.md`
- `wiki/concepts/gerenciamento-de-memoria.md`
- `wiki/concepts/gramatica-formal-ebnf.md`
- `wiki/concepts/language-server-protocol.md`
- `wiki/concepts/standard-library-e-ecossistema.md`
- `wiki/entities/robert-nystrom.md`
- `wiki/entities/llvm.md`

**Páginas atualizadas:**
- `wiki/concepts/compilador.md` — `source_count` 1 → 2; nova seção "Decisões de design que antecedem o pipeline" linkando sistema de tipos, gerenciamento de memória e gramática; detalhe de JIT/hot path adicionado à seção de bytecode+VM
- `wiki/concepts/pipeline-de-compilacao.md` — `source_count` 1 → 2; nova seção "Backend plugável via LLVM"
- `wiki/concepts/concorrencia.md` — `source_count` 1 → 2; nova seção "Decisão de design em linguagens novas" ligando modelo de concorrência do runtime ao gerenciamento de memória
- `wiki/index.md` — nova linha em Sources; 5 novas linhas em "Fundamentos de CS"; 2 novas linhas em Entities

**Notas:** Fonte era transcrição bruta de ASR em português, sem pontuação — reescrita como markdown estruturado por seções em `raw/como-criar-uma-linguagem-de-programacao.md`, sem necessidade de tradução. Diversos erros óbvios de transcrição corrigidos por contexto ao reescrever (ex.: "AS"→AST, "My R"→IR, "Bite Code"→bytecode, "ser algo equivalente"→Rust, "locks"→Lox, "Newovin"→Neovim, "PIP ou V"→pip/uv, "Eureng"→Erlang). Autor/canal não identificado, sem URL de origem. Conteúdo complementa diretamente [[wiki/concepts/compilador]] e [[wiki/concepts/pipeline-de-compilacao]] (que já cobriam o mecanismo lexer→parser→AST→codegen) com a camada de decisões de design que antecede esse mecanismo — nenhuma contradição encontrada, ampliação do mesmo território conceitual. `skill:` cs-fundamentals foi atribuído por mapeamento de domínio (algoritmos/CS teórico) já que o diretório de skills do CLAUDE.md deste repo aponta para um caminho de outra máquina (`/home/nemomartins/...`) inexistente neste ambiente — flag para skill-drift caso um sweep de lint rode depois.

---

## [2026-07-07] ingest | Integration Test (Martin Fowler)

**Source:** [[wiki/sources/integration-test-martin-fowler]] — https://martinfowler.com/bliki/IntegrationTest.html
**Skill:** tech-mentor-testing (índice de `references/` consultado — `test-patterns.md` e `test-strategy.md` não continham a distinção narrow/broad nem solitary/sociable antes desta ingestão)

**Páginas criadas:**
- `raw/integration-test-martin-fowler.md` — resumo/paráfrase em PT-BR do artigo original (não tradução literal, por direitos autorais)
- `wiki/sources/integration-test-martin-fowler.md`
- `wiki/entities/martin-fowler.md`
- `wiki/concepts/teste-de-integracao-estreito-vs-amplo.md`
- `wiki/concepts/unit-test-solitario-vs-sociavel.md`

**Páginas atualizadas:**
- `wiki/concepts/contract-testing.md` — nova seção sobre o papel do contract testing na estratégia de narrow integration test de Fowler, +1 fonte
- `wiki/concepts/test-doubles.md` — nova seção sobre o termo TestDouble e seu uso em narrow integration tests, +1 fonte
- `wiki/concepts/piramide-de-testes.md` — nova seção sobre a camada "Integração" se dividir em estreita/ampla, +1 fonte
- `wiki/concepts/testes-integracao-banco-real.md` — nova seção reconciliando "nunca mockar o banco" com o narrow integration test de Fowler (banco próprio ≠ serviço externo), +1 fonte
- `wiki/concepts/tdd.md` — link entre escolas London/Detroit e unit test solitário/sociável, +1 fonte
- `wiki/concepts/ci-cd.md` — nota sobre o termo "Deployment Pipeline" (Fowler) e onde cada tipo de teste de integração roda no pipeline, +1 fonte
- `wiki/concepts/quadrante-de-fowler.md` — menção textual convertida em wikilink para a nova entidade
- `wiki/concepts/design-patterns.md` — menções a Repository/Active Record convertidas em wikilink para a nova entidade
- `wiki/index.md` — nova seção "Testes & Qualidade" (indexava as 5 páginas de teste pré-existentes que nunca tinham entrado no índice, + as 2 novas), entrada de fonte, entrada de entidade

**Notas:** Artigo do bliki de Fowler (jan/2018, revisado jun/2021) sobre a ambiguidade do termo "integration test". Conteúdo foi salvo em `raw/` como resumo/paráfrase estruturado, não tradução literal, para respeitar os direitos autorais do texto original — a URL fonte fica registrada em `source_url` para quem quiser o texto exato. Contradição identificada e documentada nas Open Questions da fonte: `testes-integracao-banco-real.md` recomenda nunca mockar o banco, o que à primeira vista tensiona com a defesa de Fowler por dublês em testes de integração — resolvido explicitando que banco de dados próprio da aplicação não se qualifica como o tipo de "serviço externo" que Fowler tem em mente (mantido por outro time, com seu próprio build/deploy). Gap identificado na skill `tech-mentor-testing`: os arquivos de referência de testes não cobriam a distinção narrow/broad nem solitary/sociable antes desta ingestão, apesar de serem vocabulário padrão da indústria — sinalizado como open question na fonte para eventual atualização da skill (fora do escopo desta ingestão, que não edita `skills/`).

---

## [2026-07-07] ingest | O Discurso de Howard Roark (A Nascente, Ayn Rand) — lido por Fábio Akita

**Source:** [[wiki/sources/akita-discurso-howard-roark-a-nascente-ayn-rand]]
**Skill:** tech-mentor-leadership (sem arquivo de referência específico para filosofia objetivista/individualismo no índice da skill — respondendo com conhecimento base do texto, seguindo o precedente de `akita-como-aprender-programacao.md` e `akita-oferta-procura-matematica-carreira.md`, já classificados sob esta skill como fontes de Fábio Akita sobre carreira/mentalidade)

**Páginas criadas:**
- `wiki/sources/akita-discurso-howard-roark-a-nascente-ayn-rand.md`
- `wiki/entities/ayn-rand.md`
- `wiki/concepts/objetivismo.md`
- `wiki/concepts/criador-vs-parasita.md`
- `wiki/concepts/altruismo-coercitivo.md`
- `wiki/concepts/independencia-como-motor-criativo.md`

**Páginas atualizadas:**
- `wiki/entities/fabio-akita.md` — nova seção "Raiz Filosófica", +1 fonte
- `wiki/concepts/autodidata.md` — nova seção "Raiz filosófica: independência como necessidade básica do criador", +1 fonte
- `wiki/concepts/hacker-mindset.md` — nova seção "Raiz filosófica: buscar a própria resposta como independência", +1 fonte
- `wiki/index.md`

**Notas:** Fonte é transcrição de vídeo (canal Akita On Rails) em que Fábio Akita lê na íntegra o discurso de defesa de Howard Roark no julgamento (livro *A Nascente*, de Ayn Rand), afirmando que tentou viver seguindo esses princípios e que o texto é origem de vários temas que já abordou sobre carreira e criação. Conteúdo é filosofia/ideologia (Objetivismo), não conhecimento técnico — primeira fonte puramente filosófica ingerida na wiki. Dicotomia central: criador (independência como necessidade básica, motivado pela própria verdade) vs. parasita (dependência da mente alheia, motivado por controlar relações); crítica ao altruísmo como doutrina moral obrigatória que inverteu os fundamentos éticos ao tratar dependência como virtude. Conexões tecidas com conceitos já estabelecidos de carreira/mentalidade ligados a Akita (autodidata, hacker mindset) como raiz filosófica comum, não como fonte técnica adicional. Contradição/tensão identificada e documentada nas Open Questions da fonte: o discurso trata a dicotomia altruísmo/egoísmo como total e mutuamente excludente, sem espaço para reciprocidade não-sacrificial (cuidado mútuo, colaboração comunitária) — e generaliza "os maiores horrores da história" ao altruísmo sem citar casos verificáveis, o que é retórica de ficção filosófica, não tese historiográfica. Marcado como leitura crítica em todas as páginas novas, não como fato estabelecido.

---

## [2026-07-07] ingest | 5 (ou 6) Dicas Para Projetos Novos

**Source:** [[wiki/sources/5-ou-6-dicas-para-projetos-novos]]
**Skill:** tech-mentor-leadership (sem arquivo de referência específico para "checklist de setup de projeto novo" no índice da skill — respondendo com conhecimento base do vídeo, seguindo o precedente de `habitos-ruins-de-programador.md`, `como-aprender-novas-codebases.md` e `por-que-devs-nao-terminam-projetos.md`, todos já classificados sob esta skill)

**Páginas criadas:**
- `wiki/sources/5-ou-6-dicas-para-projetos-novos.md`
- `wiki/concepts/checklist-primeiro-dia-projeto.md`
- `wiki/concepts/escolha-de-stack.md`

**Páginas atualizadas:**
- `wiki/concepts/orm.md` — nova seção "ORM Mínima: Migrations Automáticas Desde o Primeiro Deploy" (Drizzle), Key Sources
- `wiki/concepts/ci-cd.md` — nova seção "Deploy Imediato do Boilerplate (Antes de Qualquer Funcionalidade)", Key Sources
- `wiki/concepts/piramide-de-testes.md` — nova seção "Testes Desde o Dia 1 de um Projeto Novo" (Vitest + Cypress), Key Sources
- `wiki/concepts/rules-agente.md` — nova seção "AGENTS.md como Etapa do Setup Inicial de Projeto", Key Sources
- `wiki/concepts/mvp.md` — nova seção "Estrutura Inicial a Serviço do MVP", Ver Também, Key Sources
- `wiki/concepts/living-documentation.md` — nota cruzada em "Quando usar/evitar" (README manual é aceitável no contexto do checklist de projeto novo), Key Sources
- `wiki/sources/por-que-devs-nao-terminam-projetos.md` — nova entrada em Open Questions cruzando com o antídoto tático desta fonte
- `wiki/index.md`

**Notas:** Fonte é transcrição de vídeo (YouTube, canal não identificado — sem URL de origem, patrocínio HostGator) com um checklist tático para o primeiro dia de uma codebase nova: (1) escolha de stack por objetivo (aprender vs. monetizar) e framework batteries-included para SaaS solo; (2) documentar estrutura inicial rumo ao MVP antes de codar; (3) deploy imediato do boilerplate com CD automático a cada merge; (4) ORM mínima (Drizzle) com migrations automáticas desde o dia 1; (5) testes (Vitest + Cypress) na pipeline antes de qualquer feature; (6) documentação dupla — README para humanos, AGENTS.md para IA. Nenhuma contradição direta com a wiki existente; a fonte é essencialmente tática/prescritiva e se conecta bem com conceitos já estabelecidos (CI/CD, ORM, pirâmide de testes, rules-agente, MVP). Um ponto de nuance real foi identificado e documentado: a recomendação de README escrito manualmente parece à primeira vista tensionar com `living-documentation.md` (que trata README manual como anti-padrão), mas na verdade está alinhada com a própria seção "Quando evitar" daquele conceito (MVP/protótipo, time pequeno) — não é contradição, é o caso de uso correto da exceção já documentada. Autor/canal do vídeo não identificado nesta ingestão — sinalizado como questão aberta na fonte.

---

## [2026-07-07] ingest | Lean Startup para Devs: Por Que Você Não Deveria Sair Escrevendo Código Direto

**Source:** [[wiki/sources/lean-startup-para-devs-mano-deivin]]
**Skill:** tech-mentor-leadership (sem arquivo de referência específico para Lean Startup/metodologia de produto no índice da skill — respondendo com conhecimento base do vídeo, seguindo o precedente de `mvp.md` e `por-que-devs-nao-terminam-projetos.md`, ambos já classificados sob esta skill)

**Páginas criadas:**
- `wiki/sources/lean-startup-para-devs-mano-deivin.md`
- `wiki/concepts/lean-startup.md`
- `wiki/concepts/build-measure-learn.md`
- `wiki/concepts/validacao-de-problema.md`
- `wiki/concepts/aprendizagem-validada.md`
- `wiki/concepts/contabilizacao-de-inovacao.md`
- `wiki/concepts/pivotar-ou-perseverar.md`
- `wiki/concepts/inovacao-continua.md`
- `wiki/entities/eric-ries.md`
- `wiki/entities/mano-deivin.md`

**Páginas atualizadas:**
- `wiki/concepts/mvp.md` — nova seção "MVP como Unidade do Ciclo Lean Startup", ponto 4 em "Por Que Devs Falham no MVP" (automação prematura), Key Sources
- `wiki/concepts/dopamina-e-projetos.md` — nova seção "Padrão Análogo: o 'Dev Emocionado'", Key Sources
- `wiki/index.md`

**Notas:** Fonte é transcrição de vídeo do canal brasileiro Mano Deivin resumindo *A Startup Enxuta* (Eric Ries) para devs tentados a largar o emprego e construir produto próprio. O vídeo organiza o livro em "6 fases" (Visão, Construir-Medir-Aprender, Aprendizagem Validada, Contabilização de Inovação, Crescimento Sustentável, Pivô ou Persevere) mais Inovação Contínua — simplificação didática que difere da estrutura formal do livro (Visão / Direção / Aceleração em três partes). Sinalizado como questão aberta na página da fonte para eventual checagem contra o texto original. Forte sobreposição temática com fontes já existentes sobre MVP e ciclo de dopamina em projetos (`por-que-devs-nao-terminam-projetos`) — ambas atualizadas com backlink cruzado. Nenhuma contradição direta com a wiki existente; a fonte complementa o tema de "por que devs não terminam/lançam projetos" com o ângulo inverso (por que não validar antes de começar a construir). Conteúdo publicitário do vídeo (indicação de plataforma de pagamento patrocinada) foi mantido como nota isolada em `raw/`, fora do corpo técnico.

---

## [2026-07-07] ingest | Shopify Trocou Redis por MySQL e Segurou US$ 5,1 Milhões por Minuto na Black Friday

**Source:** [[wiki/sources/shopify-redis-para-mysql-skip-locked-black-friday]]
**Skill:** tech-mentor-backend (`references/distributed-locking.md`)

**Páginas criadas:**
- `wiki/sources/shopify-redis-para-mysql-skip-locked-black-friday.md`
- `wiki/concepts/mysql.md`
- `wiki/concepts/grande-rollback.md`
- `wiki/concepts/solid-queue.md`
- `wiki/entities/shopify.md`
- `wiki/entities/37signals.md`

**Páginas atualizadas:**
- `wiki/concepts/skip-locked.md` — nova seção "Além de Filas de Job: Reserva de Estoque" (caso Shopify), tag mysql, Key Sources
- `wiki/concepts/redis.md` — nova seção "Caso Real: Substituindo Redis por SQL Puro (Grande Rollback)", Key Sources
- `wiki/concepts/cache.md` — Key Sources com contraponto do case
- `wiki/concepts/distributed-lock.md` — Key Sources
- `wiki/concepts/deadlock.md` — nova seção "Deadlock em Banco de Dados: Gap Locking do MySQL", Key Sources
- `wiki/concepts/connection-pooling.md` — nova seção "Diagnóstico: Tempo de Conexão Segurada, Não Latência de Query", Key Sources
- `wiki/sources/uuid-primary-key-mysql.md` — link para novo `concepts/mysql`
- `wiki/sources/listen-notes-boring-tech-one-person-company.md` — link cruzado sobre "fonte única de verdade" e Grande Rollback
- `wiki/index.md`

**Notas:** Fonte é transcrição de vídeo (YouTube, canal de tecnologia brasileiro) analisando um artigo de engenharia da Shopify (não linkado na transcrição original — falta a URL primária). Núcleo técnico: reserva de estoque migrou de Redis+MySQL sincronizados por duas escritas não-atômicas para um modelo 100% MySQL com `SELECT FOR UPDATE SKIP LOCKED`, onde cada unidade de estoque é uma linha física (não uma coluna numérica). Precisaram corrigir três problemas clássicos de banco (PK mal desenhada, gap locking do InnoDB, ordem de execução divergente) antes de escalar. O achado mais interessante é o diagnóstico: mesmo com queries otimizadas, o sistema não escalava por gargalo de **tempo de conexão segurada por operação** (não latência de query) — e o gargalo real estava em código legado do checkout, não na reserva de estoque que parecia ser o problema. A fonte conecta o case a uma teoria recorrente do canal, o "Grande Rollback" (empresas em escala voltando de Redis/brokers para primitivas do banco relacional), citando a 37signals/Solid Queue como precedente — nome transcrito de forma ambígua no áudio ("Thury Syve Sos"), mantido como interpretação de melhor esforço e sinalizado como questão aberta na página da entidade. Conteúdo promocional do vídeo (inscrição no canal, patrocínio, cupom) foi removido na transformação para `raw/`, mantendo só a análise técnica.
## [2026-07-03] ingest | Pare de Terceirizar Suas Decisões

**Source:** [[wiki/sources/pare-de-terceirizar-suas-decisoes]]
**Skill:** tech-mentor-leadership (path de skills configurado em CLAUDE.md, `/home/nemomartins/Documentos/new/skills/`, não existe neste ambiente — ver nota abaixo)

**Páginas criadas:**
- `wiki/sources/pare-de-terceirizar-suas-decisoes.md`
- `wiki/concepts/decisao-terceirizada.md`
- `wiki/concepts/skin-in-the-game.md`
- `wiki/concepts/antifragilidade.md`
- `wiki/concepts/cargo-cult-tecnologico.md`
- `wiki/concepts/falacia-do-custo-afundado.md`
- `wiki/concepts/curva-de-adocao-tecnologica.md`

**Páginas atualizadas:**
- `wiki/entities/fabio-akita.md` — nova seção "Visão de Tomada de Decisão"; `source_count` 2 → 3
- `wiki/concepts/paralisia-por-analise.md` — nuance sobre terceirizar decisão como fuga da paralisia; `source_count` 1 → 2
- `wiki/concepts/principio-da-inversao.md` — link com skin in the game/antifragilidade como modelos mentais de decisão sob incerteza; `source_count` 1 → 2
- `wiki/concepts/ciclo-de-mercado-tech.md` — cada onda como curva de adoção em S; `source_count` 2 → 3
- `wiki/concepts/aprender-a-aprender.md` — leitura não-linear de livros técnicos e ligação com custo afundado; `source_count` 1 → 2
- `index.md` — nova fonte na tabela de Sources + 6 novos conceitos na seção "Carreira & Soft Skills"

**Notas:** Terceira fonte de [[wiki/entities/fabio-akita]] na wiki (após [[wiki/sources/akita-como-aprender-programacao]] e [[wiki/sources/akita-oferta-procura-matematica-carreira]]). O locutor se identifica na transcrição bruta como "Fábio, a Quinta" — quase certamente um erro de transcrição por voz para "Fábio Akita" (confirmado pelo estilo, conteúdo e menções de episódios anteriores do canal). Cruza diretamente com [[wiki/concepts/ciclo-de-mercado-tech]] (mesmo autor, mesmo argumento sobre ondas de tecnologia por década) e com [[wiki/concepts/paralisia-por-analise]] (excesso de escolha/informação). Nenhuma contradição com o wiki existente.

**Drift encontrado:** o `CLAUDE.md` deste repositório referencia `/home/nemomartins/Documentos/new/skills/` e `/home/nemomartins/Documentos/new/dev-study/` como paths absolutos do sistema de skills e do vault Obsidian — nenhum dos dois existe neste ambiente (`$HOME` é `/home/gabriel-martins`, repo real está em `/home/gabriel-martins/Documentos/dev-brain`, e não há pasta `.obsidian/templates/`). O ingest seguiu o padrão de frontmatter e estrutura observado nas páginas existentes de `wiki/sources/` e `wiki/concepts/` em vez do template inexistente. Vale corrigir o `CLAUDE.md` para os paths reais deste ambiente, ou documentar que esses paths são específicos de outra máquina.

---

## [2026-07-03] ingest | ACID vs. BASE: As Garantias que os Bancos de Dados Nos Dão

**Source:** [[wiki/sources/acid-vs-base-garantias-bancos-de-dados]]
**Skill:** tech-mentor-system-design

**Páginas criadas:**
- `wiki/sources/acid-vs-base-garantias-bancos-de-dados.md`
- `wiki/concepts/base-basically-available-soft-state-eventual.md` (stub — BASE não tinha página dedicada, só era citado implicitamente em `consistency-models.md`)

**Páginas atualizadas:**
- `wiki/concepts/acid.md` — exemplo de custo de performance da constraint de e-mail único; link para BASE
- `wiki/concepts/consistency-models.md` — exemplo de leitura desatualizada em réplica não sincronizada; link para BASE
- `wiki/concepts/relational-vs-nosql.md` — quadro de decisão ACID vs. BASE por domínio de negócio (pagamentos/estoque vs. likes/analytics/logs/cache/recomendação)
- `wiki/concepts/database-index.md` — exemplo concreto de índice hash como mecanismo de unicidade
- `wiki/concepts/database-transactions.md` — nuance sobre isolamento em transações concorrentes (não é "ausência de interferência", é "resultado final serial-consistente")
- `wiki/concepts/cap-theorem.md` — relação entre BASE/ACID e a escolha AP/CP do teorema CAP
- `index.md` — adicionadas 6 linhas ausentes da seção "Bancos de Dados & SQL" que já existiam no disco mas não estavam indexadas (`acid`, `relational-vs-nosql`, `database-transactions`, `database-index`, `consistency-models`, além do novo `base-basically-available-soft-state-eventual`)

**Notas:** Fonte é transcrição de vídeo do mesmo canal/autor de [[wiki/sources/sql-nao-e-banco-de-dados-uncle-bob]] (menciona curso de System Design com lançamento em junho de 2026). Nenhuma contradição com o wiki existente — os conceitos de ACID e consistência eventual já estavam documentados via [[wiki/sources/banco-de-dados]] e [[wiki/sources/modelos-de-consistencia]]/[[wiki/sources/cap-pacelc-consistencia]], mas o acrônimo **BASE** em si nunca tinha ganhado página própria, e o exemplo do e-mail único como ilustração concreta do custo de performance da consistência é novo. Drift de índice pré-existente encontrado e corrigido de passagem: seis páginas de conceito sobre banco de dados existiam no disco desde abril/2026 mas nunca haviam sido adicionadas a `index.md` — vale considerar um `/lint` completo depois para checar se há mais casos assim.

---

## [2026-07-03] ingest | Vibe Coding: Limites, Riscos e o Papel do Profissional Maduro

**Source:** [[wiki/sources/vibe-coding-limites-maturidade-profissional]]
**Skill:** tech-mentor-ai

**Páginas criadas:**
- `wiki/sources/vibe-coding-limites-maturidade-profissional.md`
- `wiki/concepts/confidencialidade-de-dados-em-prompts-ia.md` (stub)
- `wiki/concepts/contexto-organizacional-para-arquitetura.md` (stub)

**Páginas atualizadas:**
- `wiki/concepts/vibe-coding.md` — nova seção sobre o limite ser de julgamento, não técnico
- `wiki/concepts/mvp.md` — MVP como contexto onde vibe coding entrega valor real
- `wiki/concepts/arquitetura-de-software.md` — seção sobre decisão arquitetural exigir contexto organizacional, não só um prompt
- `wiki/concepts/pensamento-critico.md` — o que a IA não substitui na análise de negócio/arquitetura
- `wiki/concepts/engenheiro-vs-programador.md` — a mesma distinção pela ótica de uma arquiteta usando IA sem delegar a decisão
- `wiki/concepts/robustez-de-sistemas.md` — vibe coding não entrega robustez por padrão
- `wiki/concepts/governanca-de-codigo-gerado-por-ia.md` — vender sistema vibe-coded como pronto para produção como caso limite de falta de governança

**Notas:** Fonte é transcrição de vídeo (perspectiva de arquiteta de software) sobre os limites do vibe coding. Argumento central: vibe coding brilha em MVP/protótipos/docs/testes, mas sistemas sustentáveis exigem arquitetura, segurança e — o ponto mais novo em relação ao que já estava no wiki — análise de **contexto organizacional** (maturidade de plataforma, CI/CD, processo entre áreas, know-how e licenciamento) e cuidado com **confidencialidade de dados** em prompts. Nenhuma contradição com [[wiki/sources/apagao-de-seniors-vibe-coding]] ou [[wiki/sources/engenheiro-vs-programador-mercado-ia]] — é o mesmo argumento reforçado por uma terceira fonte independente, com ênfase diferente (negócio/organização em vez de técnicas de detecção de bugs). Questão aberta: não há critério objetivo, em nenhuma das três fontes, para saber quando um MVP "saiu" do estágio de validação e precisa de revisão arquitetural formal antes de produção.

---

## [2026-07-03] ingest | SQL não é Banco de Dados: A Confusão da Galera no Twitter

**Source:** [[wiki/sources/sql-nao-e-banco-de-dados-uncle-bob]]
**Skill:** tech-mentor-backend (`references/architecture-foundations.md`)

**Páginas criadas:**
- `wiki/sources/sql-nao-e-banco-de-dados-uncle-bob.md`
- `wiki/concepts/orm.md`
- `wiki/concepts/domain-specific-language.md`
- `wiki/entities/uncle-bob.md`

**Páginas atualizadas:**
- `wiki/concepts/sql-injection.md` — nova seção contestando "eliminar SQL elimina SQL attacks", nota de nomenclatura Bobby Tables vs. Bob Tables, Key Sources
- `wiki/concepts/postgresql.md` — nota sobre Supabase (BaaS) continuar sendo Postgres/SQL por baixo, Key Sources
- `wiki/concepts/nosql.md` — nota desambiguando "SQL embutido no código" de "relacional vs. NoSQL", Key Sources
- `wiki/concepts/relational-vs-nosql.md` — nota sobre eixo ortogonal SQL-cru-vs-abstração, Key Sources
- `wiki/concepts/datomic.md` — nota sobre Datalog como exemplo de linguagem de query alternativa ao SQL, Key Sources
- `wiki/concepts/database-index.md` — nota ligando índice a B-tree e à dificuldade de reimplementar indexação, Key Sources
- `wiki/concepts/database-transactions.md` — nota sobre transactions como parte difícil de recriar num banco do zero, Key Sources
- `wiki/concepts/arvore.md` — Key Sources
- `wiki/concepts/sql-alem-do-basico.md` — link para orm.md, Key Sources
- `wiki/index.md`

**Notas:** Fonte é transcrição de vídeo/reação (autor brasileiro não identificado no arquivo bruto) a uma thread do Twitter atribuída a Robert C. Martin ("Uncle Bob") sobre SQL nunca ter sido pensado para uso embutido em programas. O valor real da fonte não é a polêmica em si, mas a explicação didática de que (1) SQL é uma linguagem, não o banco; (2) ORMs e DSLs são wrappers sobre SQL, não substitutos; (3) um banco relacional tem no mínimo quatro camadas (armazenamento via B-tree/WAL, comunicação/query, planner, execução); (4) BaaS como Supabase continua executando SQL por baixo. Contradição sinalizada com a wiki: a afirmação da thread de que "eliminar SQL elimina SQL attacks" simplifica demais — `sql-injection.md` já documenta que a defesa real é parametrização, não ausência de SQL. Questão aberta: não há confirmação da autoria/URL da thread nem do post "Bob Tables" citado — tratado com cautela nas páginas atualizadas.

---

## [2026-07-03] ingest | TDD, SDD e BDD na Era da IA

**Source:** [[wiki/sources/tdd-sdd-bdd-era-ia]]
**Skill:** tech-mentor-testing (`references/test-patterns.md`, `references/test-strategy.md`)

**Páginas criadas:**
- `wiki/sources/tdd-sdd-bdd-era-ia.md`
- `wiki/concepts/gaming-de-testes-por-ia.md`

**Páginas atualizadas:**
- `wiki/concepts/tdd.md` — nova seção "Não deixe a IA deletar testes que falham", Key Sources
- `wiki/concepts/bdd.md` — nota sobre recomendação de BDD sem experiência prática, Key Sources
- `wiki/concepts/spec-driven-development.md` — nova seção sobre origem não-IA do termo (contratos de boundary: OpenAPI, Protobuf/gRPC, GraphQL), Key Sources
- `wiki/concepts/harness-de-qualidade.md` — reforço do componente TDD com o guardrail de gaming de testes, novo componente SDD, Key Sources
- `wiki/concepts/documentacao-api-swagger.md` — backlink para spec-driven-development, Key Sources
- `wiki/concepts/robustez-de-sistemas.md` — Key Sources
- `wiki/index.md`

**Notas:** Fonte é transcrição de vídeo curto (autor não identificado) cobrindo TDD, SDD e BDD com foco no ângulo "isso funciona também impondo sobre IA". Maior parte do conteúdo já estava coberto por fontes anteriores mais técnicas ([[wiki/sources/tdd]], [[wiki/sources/bdd]], [[wiki/sources/conteudo-tecnico-ia-robustez-sistemas]]); a contribuição nova e mais concreta é o alerta específico sobre a IA deletar testes que falham em vez de corrigir o código (novo conceito `gaming-de-testes-por-ia`) e a origem do termo SDD como contrato de API/boundary entre serviços (complementa a definição de `spec-driven-development`, que na wiki estava focada em specs para agentes). Nenhuma contradição com a wiki existente. Questão aberta: falta dado quantitativo (não anedótico) sobre o efeito de TDD/SDD impostos via harness na taxa de acerto da IA.

---

## [2026-07-03] ingest | Atrofia Cognitiva, IA e a Síndrome do Pânico de Esquecer Programar

**Source:** [[wiki/sources/atrofia-cognitiva-ia-programacao]]
**Skill:** tech-mentor-ai (`references/ai-assisted-engineering.md`)

**Páginas criadas:**
- `wiki/sources/atrofia-cognitiva-ia-programacao.md`
- `wiki/concepts/sintaxe-vs-conhecimento-perene.md`
- `wiki/entities/lucas-montano.md`

**Páginas atualizadas:**
- `wiki/concepts/divida-cognitiva.md`
- `wiki/concepts/fundacao-tecnica.md`
- `wiki/concepts/aprendizado-passivo.md`
- `wiki/concepts/engenheiro-vs-programador.md`
- `wiki/concepts/governanca-de-codigo-gerado-por-ia.md`
- `wiki/concepts/pensamento-em-producao.md`
- `wiki/concepts/autodidata.md`
- `wiki/sources/apagao-de-seniors-vibe-coding.md`

**Notas:** Transcrição de vídeo (Lucas Montano) argumentando que o pânico sobre "atrofia cognitiva" por IA mede o tipo errado de habilidade — memorizar sintaxe já era irrelevante desde autocomplete de IDE e busca no Google, muito antes de LLMs. O que importa é conhecimento perene (causas de erro 401/500, debugging de produção, propagação de exceções). Reforça [[wiki/concepts/fundacao-tecnica]] (esquecimento é reversível quando há base) e [[wiki/concepts/pensamento-em-producao]] (exemplos concretos do que é conhecimento perene). Sem contradição direta com a wiki — adiciona nuance a [[wiki/concepts/divida-cognitiva]]: o risco real de dependência de IA não é esquecer sintaxe, é perder julgamento e capacidade de explicar decisões (ilustrado pelo caso do tech lead sênior que não consegue explicar seu próprio PR). Papers acadêmicos citados na fala (2026, sobre "disuse atrophy"/"cognitive offloading" e "The Instrumental Dissolution of Typing") não têm referência verificável — marcados como confiança baixa/média em [[wiki/sources/atrofia-cognitiva-ia-programacao]]. Questão aberta: quanto a distinção "fundação sólida recupera rápido vs. dev nativo-de-IA nunca teve base" se sustenta além de analogia e experiência pessoal do autor.

---

## [2026-07-03] ingest | Updates em Tempo Real: Polling, SSE e WebSocket na Entrevista

**Source:** [[wiki/sources/updates-tempo-real-polling-sse-websocket]]
**Skill:** `tech-mentor-backend` (`references/realtime.md` — WebSocket vs SSE, Redis Pub/Sub scaling; `references/networking-protocols.md` — Load Balancer L4 vs L7)

**Páginas criadas:**
- `wiki/sources/updates-tempo-real-polling-sse-websocket.md`
- `wiki/entities/pedro-camaforte.md`

**Páginas atualizadas:**
- `wiki/concepts/load-balancer.md` — seção "Por que L7 quebra o fluxo" (LB L7 reempacota a requisição; L4 só encaminha bytes por menor nº de conexões), backlink
- `wiki/concepts/websocket-vs-polling.md` — seção "Polling não é uma escolha inferior — é uma escolha de escala", backlink
- `wiki/concepts/pub-sub.md` — seção "Padrão: um tópico por usuário para chat/WebSocket" (`user:<id>`, `group:<id>`), backlink
- `wiki/concepts/chat-distribuido.md` — seção "Usuário offline: tabela de mensagens pendentes" (dois vieses: histórico vs. limpeza pós-entrega estilo WhatsApp; alternativa por timestamp), backlink
- `wiki/concepts/redis.md` — backlink (Redis Pub/Sub como broker entre servidores WebSocket replicados)
- `wiki/concepts/mensageria.md` — backlink (mitigação de perda de mensagem via tabela de pendentes)
- `wiki/concepts/server-sent-events.md` — backlink (mesmo mecanismo de Pub/Sub usado por WebSocket também propaga SSE entre instâncias)
- `wiki/concepts/escalabilidade-horizontal.md` — seção "Caso especial: serviços de conexão persistente (WebSocket)", backlink
- `wiki/concepts/protocolo-de-rede.md` — seção "WebSocket: upgrade de HTTP para TCP", backlink

**Notas:** Fonte é uma transcrição de vídeo já em português — sem necessidade de tradução, só formatação em Markdown. Overlap temático relevante com duas fontes já existentes ([[wiki/sources/server-sent-events-sse-tempo-real]] e [[wiki/sources/websocket-sse-realtime]]), mas sem contradição — esta fonte contribui especificamente com a moldura de entrevista (quando polling é a resposta certa, o "porquê" do LB L4, o padrão de tópico-por-usuário no Redis, e o padrão de mensagens pendentes para offline). Nenhuma página nova de conceito foi necessária — os conceitos centrais (WebSocket, SSE, Load Balancer, Pub/Sub, Chat Distribuído) já existiam e foram aprofundados.

---

## [2026-07-03] ingest | Golang e o Mercado de Trabalho: Como Migrar do Frontend para o Backend

**Source:** [[wiki/sources/golang-mercado-trabalho-frontend-para-backend]]
**Skill:** `tech-mentor-leadership` (career/mercado — índice `career-progression.md` / `technical-strategy.md`; conteúdo específico de Go calibrado por analogia com `lang-systems/go-fundamentos.md` já existente na wiki)

**Páginas criadas:**
- `wiki/sources/golang-mercado-trabalho-frontend-para-backend.md`
- `wiki/entities/lucas-badico.md`
- `wiki/concepts/ponte-fullstack-para-especializacao.md`

**Páginas atualizadas:**
- `wiki/concepts/ciclo-de-mercado-tech.md` — contra-exemplo do Ruby on Rails (influência sem onda de mercado) e nota sobre Go cloud native, backlink
- `wiki/concepts/go-fundamentos.md` — seções "Filosofia: Pragmatismo vs. Expressividade (Go vs. Rust)" e "Design Cloud Native", backlink
- `wiki/concepts/portfolio-backend-junior.md` — seção "Mirando pleno em vez de júnior", link para a nova ponte fullstack
- `wiki/concepts/curriculo-vs-portfolio.md` — nota sobre portfólio substituindo currículo quando não há experiência formal na stack-alvo
- `wiki/concepts/apego-a-ferramentas.md` — contraste entre apego individual e tecnologia influente que nunca virou onda de mercado (Ruby on Rails)
- `wiki/index.md` — nova fonte, novo conceito, nova entidade

**Notas:** Fonte é opinião qualificada de um criador de conteúdo (Lucas Badico), não dado de mercado medido — números de adoção (40/60 Brasil, 80/20 EUA) sinalizados como estimativa pessoal no próprio source page. Nenhuma contradição direta com conteúdo existente; reforça e adiciona nuance ao padrão já registrado em [[wiki/concepts/ciclo-de-mercado-tech]] e [[wiki/concepts/apego-a-ferramentas]].

---

## [2026-07-03] ingest | Múltiplos Agentes no Claude Code — Work Trees e Subagentes

**Source:** [[wiki/sources/multiplos-agentes-worktrees-subagentes-claude-code]]
**Skill:** `tech-mentor-ai` (`references/ai/agents-orchestration.md`)

**Páginas criadas:**
- `wiki/sources/multiplos-agentes-worktrees-subagentes-claude-code.md`
- `wiki/concepts/subagentes.md`

**Páginas atualizadas:**
- `wiki/concepts/worktree-paralelismo.md` — seção sobre `claude --worktree` nativo, comparação worktree vs. subagente, backlink
- `wiki/entities/claude-code.md` — linhas de worktree/subagentes na tabela de recursos principais
- `wiki/entities/anthropic.md` — backlink de "Subagents" para a nova página de conceito
- `wiki/concepts/agente-ia.md` — subagentes e worktrees detalhados no exemplo Claude Code
- `wiki/concepts/tool-call.md` — tabela de tools nativas do Claude Code (Agent, AskUserQuestion, Bash, Glob, Grep, Read/Write/Edit) e nota sobre restringir tools por subagente
- `wiki/concepts/ciclo-agente.md` — subagentes como forma de conter o crescimento do ciclo/contexto do agente pai
- `wiki/concepts/skills-agente.md` — comparação skill vs. subagente e risco de sobreposição ("parafernália") confundindo roteamento automático
- `wiki/concepts/janela-de-contexto.md` — subagentes e worktrees como estratégias de economia de janela
- `wiki/concepts/reasoning-level.md` — reasoning baixo pode esconder oportunidades de paralelismo automático
- `wiki/index.md` — novo source e novo conceito indexados

**Notas:** Transcrição de live coding (HiperDev) sobre as duas formas nativas do Claude Code de rodar múltiplos agentes em paralelo. Sem contradição com `wiki/concepts/worktree-paralelismo.md` (fonte anterior cobria `git worktree` manual/spec-driven; esta fonte acrescenta o wrapper nativo `claude --worktree` e a distinção formal contra subagentes). Ponto de atenção registrado como questão aberta: a afirmação de que skills não suportam `model`/`tools` customizados foi checada ao vivo, mas vale reconfirmar contra a documentação oficial mais recente da Anthropic.

---

## [2026-07-03] ingest | Server-Sent Events (SSE): Comunicação em Tempo Real na Prática

**Source:** [[wiki/sources/server-sent-events-sse-tempo-real]]
**Skill:** `tech-mentor-backend` (`references/realtime.md`)

**Páginas criadas:**
- `wiki/sources/server-sent-events-sse-tempo-real.md`
- `wiki/concepts/server-sent-events.md`

**Páginas atualizadas:**
- `wiki/concepts/websocket-vs-polling.md` — backlink + referência à página nova de SSE
- `wiki/concepts/redis.md` — seção de conexão como Singleton, Pub/Sub sem criação prévia de canal
- `wiki/concepts/pub-sub.md` — exemplo prático de Redis Pub/Sub notificando endpoint SSE
- `wiki/concepts/singleton-pattern.md` — caso de uso: conexão Redis compartilhada em Pub/Sub
- `wiki/concepts/protocolo-de-rede.md` — SSE como conexão TCP/HTTP mantida aberta
- `wiki/concepts/mensageria.md` — Redis Pub/Sub como notificador leve (sem persistência/replay) vs Kafka/SQS/RabbitMQ
- `wiki/concepts/graceful-shutdown.md` — cleanup por conexão individual (`req.on('close')`) como caso análogo ao shutdown de processo
- `wiki/concepts/load-balancer.md` — WebSocket exige LB L4; SSE não exige infra especializada
- `wiki/index.md` — nova seção "Realtime & Comunicação", novo source indexado

**Notas:** Transcrição de vídeo tutorial (autor se identifica só como "Renato" no texto) sobre SSE, cobrindo polling → long polling → SSE → WebSocket em ordem crescente de sofisticação, com implementação prática em Node.js/Express + Redis Pub/Sub para arquitetura distribuída. Nenhuma contradição com `wiki/concepts/websocket-vs-polling.md` (que já cobria a comparação em nível mais superficial) — esta fonte aprofunda implementação e erros de produção. Questão aberta registrada na fonte: risco de exposição de JWT em logs quando passado via query string, ponto não coberto pela transcrição original mas relevante para produção.

---

## [2026-07-03] ingest | O Mercado Não Precisa de Mais Programadores

**Source:** [[wiki/sources/engenheiro-vs-programador-mercado-ia]]
**Skill:** `tech-mentor-leadership` (`references/career-progression.md`)

**Páginas criadas:**
- `wiki/sources/engenheiro-vs-programador-mercado-ia.md`
- `wiki/concepts/engenheiro-vs-programador.md`
- `wiki/concepts/governanca-de-codigo-gerado-por-ia.md`
- `wiki/concepts/pensamento-em-producao.md`
- `wiki/concepts/arquitetura-de-software.md`

**Páginas atualizadas:**
- `wiki/concepts/fundacao-tecnica.md` (engenheiro coleciona modelos mentais, não ferramentas; eixo vertical/horizontal)
- `wiki/concepts/apego-a-ferramentas.md` (mesma ideia reforçada com outro enquadramento — roadmap.sh, ciclo de ~3 anos de ferramentas)
- `wiki/concepts/complexidade-acidental.md` (segunda fonte independente da distinção essencial/acidental, via Mythical Man-Month de Brooks, não Out of the Tar Pit)
- `wiki/concepts/algoritmos-e-estruturas-de-dados.md` (DSA como primeiro item do eixo vertical de fundamentos)
- `wiki/concepts/entendimento-de-dominio.md` (modelagem de domínio como tradução do problema real para código — DDD, Ousterhout)

**Notas:** Fonte recebida como transcrição pura, sem autor/canal identificado — `author` ficou em branco no frontmatter; nenhuma entidade de pessoa foi criada. A distinção complexidade essencial vs. acidental já existia no wiki a partir de "Out of the Tar Pit" ([[wiki/sources/nubank-clojure-datomic-event-sourcing]]); esta fonte cita a mesma dicotomia via outra origem (Frederick Brooks, 1975) — sem contradição, reforço cruzado de duas fontes primárias independentes. Em aberto: livros citados (Clean Architecture, DDIA, DDD, Fundamentals of Software Architecture, Mythical Man-Month, Lean Startup, Inspired) ainda não têm fonte própria no wiki — são citações de segunda mão.

---

## [2026-07-03] ingest | Oferta, Procura e Matemática Básica — Por Que Sua Carreira em Programação Vai Sofrer

**Source:** [[wiki/sources/akita-oferta-procura-matematica-carreira]]
**Skill:** `tech-mentor-leadership` (`references/career-progression.md`) — domínio secundário: segurança (`password-hashing`, não recarregada skill própria)

**Páginas criadas:**
- `wiki/sources/akita-oferta-procura-matematica-carreira.md`
- `wiki/concepts/ciclo-de-mercado-tech.md`
- `wiki/concepts/raciocinio-matematico-aplicado.md`
- `wiki/concepts/apego-a-ferramentas.md`

**Páginas atualizadas:**
- `wiki/concepts/autodidata.md` (lavagem cerebral do sistema educacional formal treina passividade)
- `wiki/concepts/aprendizado-passivo.md` (tutorial passo-a-passo pré-IA já produzia o mesmo padrão de cópia sem entendimento)
- `wiki/concepts/fundacao-tecnica.md` (raciocínio matemático como componente da fundação)
- `wiki/concepts/password-hashing.md` (caso real citado: vazamento Ministério da Saúde, senha em plaintext)
- `wiki/entities/fabio-akita.md` (perfil ampliado: empresa de outsourcing, caso Vivo ~2002, visão de mercado)

**Notas:** Segundo vídeo de Fábio Akita ingerido — mesmo autor de [[wiki/sources/akita-como-aprender-programacao]], mas foco diferente: ciclos de mercado, raciocínio matemático e apego a ferramentas, em vez de metodologia de aprendizado por exposição. Sem contradição direta com o wiki existente; complementa [[wiki/concepts/autodidata]] e [[wiki/concepts/fundacao-tecnica]]. Possível tensão leve de dados biográficos entre as duas fontes (idade em que começou a programar varia entre "~13 anos" e "14-15 anos" nas duas transcrições) — dentro da margem normal de variação de memória entre vídeos diferentes, não tratado como contradição formal. Questão aberta: nenhuma fonte no wiki até agora testa empiricamente a correlação entre raciocínio matemático e competência como programador — é argumentada por analogia/anedota em ambas as fontes do autor.

---

## [2026-07-03] ingest | Tokens em LLMs — Fundamentos com TypeScript

**Source:** [[wiki/sources/tokens-llm-fundamentos-typescript]]
**Skill:** `tech-mentor-ai` (`references/ai/fundamentals.md`)

**Páginas criadas:**
- `wiki/sources/tokens-llm-fundamentos-typescript.md`
- `wiki/concepts/tokenizacao.md`
- `wiki/entities/matt-pocock.md`
- `wiki/entities/vercel-ai-sdk.md`
- `wiki/entities/google.md`

**Páginas atualizadas:**
- `wiki/concepts/byte-pair-encoding.md` (trade-off de tamanho de vocabulário + fonte)
- `wiki/concepts/token-tax-multilingual.md` (generalização: palavra rara "frabjous" sofre o mesmo efeito que idiomas não-ingleses)
- `wiki/entities/anthropic.md` (exemplo Claude 3.5 Haiku via AI SDK: 11 tokens de entrada para "Hello World")
- `wiki/entities/openai.md` (tiktoken / o200k_base como tokenizer do GPT-4o)

**Notas:** Fonte é vídeo de Matt Pocock (AI Hero) explicando fundamentos de tokens em LLM via TypeScript/`js-tiktoken`/AI SDK. Sem contradição com o wiki existente — na verdade complementa diretamente [[wiki/concepts/byte-pair-encoding]] e [[wiki/concepts/token-tax-multilingual]] (já criados a partir de [[wiki/sources/custo-tokens-portugues-vs-ingles]]), adicionando o mecanismo de treino do tokenizer (nível-caractere → subpalavra → BPE) e o trade-off de tamanho de vocabulário que faltava nessas páginas. Questão aberta: fonte não cobre o multiplicador de token tax para português no Gemini/Google, só documentado para Anthropic.

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

---

## [2026-04-22] ingest | useEffect — Problemas, Armadilhas e Soluções

**Source:** [[wiki/sources/useeffect-problemas-e-solucoes]]
**Skill:** tech-mentor-frontend

**Páginas criadas:**
- `wiki/sources/useeffect-problemas-e-solucoes.md`
- `wiki/concepts/derived-state.md`
- `wiki/concepts/stale-closure.md`

**Páginas atualizadas:**
- `wiki/concepts/useEffect.md`
- `wiki/concepts/useState.md`
- `wiki/concepts/useMemo.md`
- `wiki/concepts/tanstack-query.md`
- `wiki/concepts/race-condition.md`

**Notas:** Transcrição de vídeo sobre os três anti-padrões mais comuns do `useEffect`: (1) sincronizar estado derivado via effects encadeados em vez de calcular na renderização — gera renderizações extras e janelas de estado inconsistente; (2) stale closure em contadores/timers por não usar a updater function do `setState`; (3) fetch de dados em `useEffect` sem `AbortController`, com race condition e memory leak. Regra de ouro: "o melhor effect é o que você deleta." Nenhuma contradição com a wiki existente — reforça e detalha claims já presentes em [[wiki/concepts/useEffect]] e [[wiki/concepts/tanstack-query]]. Este registro completa um ingest que havia sido deixado incompleto (source e concept pages já existiam, mas faltavam no índice e no log).
## [2026-07-03] ingest | Como Não Ser Humilhado no Primeiro Code Review

**Source:** [[wiki/sources/como-nao-ser-humilhado-no-primeiro-code-review]]
**Skill:** tech-mentor-leadership (path de skills configurado em CLAUDE.md, `/home/nemomartins/Documentos/new/skills/`, não existe neste ambiente — drift já registrado no ingest de [[wiki/sources/pare-de-terceirizar-suas-decisoes]])

**Páginas criadas:**
- `wiki/sources/como-nao-ser-humilhado-no-primeiro-code-review.md`
- `wiki/concepts/code-review.md`
- `wiki/concepts/sindrome-do-impostor.md`

**Páginas atualizadas:**
- `wiki/concepts/paridade-local-producao.md` — sequência dev/homologação/produção antes de abrir PR; `source_count` 2 → 3
- `wiki/concepts/definicao-de-pronto.md` — regra de negócio como critério #1, antes de estilo; `source_count` 2 → 3
- `wiki/concepts/inteligencia-emocional.md` — não levar comentários de code review pro lado pessoal; `source_count` 1 → 2
- `wiki/concepts/mentoria-tecnica.md` — comentários secos no review costumam ser falta de tempo, não má intenção; `source_count` 1 → 2
- `wiki/concepts/pensamento-em-producao.md` — validar manualmente em produção antes de fechar a tarefa; `source_count` 2 → 3
- `wiki/concepts/autonomia-responsabilidade.md` — alinhar com o PO antes do PR; não criar tarefas fora do escopo; `source_count` 1 → 2
- `wiki/concepts/dependencia-ia.md` — revisar código com IA antes do PR só é uso produtivo se vier com "porquê" explicado; `source_count` 2 → 3
- `wiki/index.md` — nova fonte na tabela de Sources + 2 novos conceitos em "Carreira & Soft Skills"

**Notas:** Fonte original é a transcrição bruta de um vídeo (autor/canal não identificado no texto) sobre a dinâmica emocional e prática do primeiro code review de um júnior. Como reproduzir a transcrição quase-literal envolveria recriar conteúdo protegido de terceiros, o arquivo em `raw/` foi escrito como resumo estruturado (não verbatim) a pedido do usuário — logo esta fonte tem menos densidade de citação direta que ingests anteriores. Nenhuma contradição com o wiki existente; reforça e conecta diretamente com [[wiki/concepts/definicao-de-pronto]] e [[wiki/concepts/inteligencia-emocional]], que já cobriam parte do terreno (regra de negócio antes de estilo; feedback sem defensividade). Questão aberta registrada na fonte: como equilibrar "não criar tarefa que ninguém pediu" com a expectativa de iniciativa técnica de um júnior.

---

## [2026-07-03] ingest | ISO 27001 — Dicionário do Programador

**Source:** [[wiki/sources/iso-27001-dicionario-programador]]
**Skill:** tech-mentor-security (path de skills configurado em CLAUDE.md, `/home/nemomartins/Documentos/new/skills/`, não existe neste ambiente — path real encontrado em `/home/gabriel-martins/Documentos/skills/tech-mentor-security/SKILL.md`; drift já registrado em ingests anteriores). Referência específica carregada: `references/compliance-audit.md`, seção "ISO 27001 para Engenheiros".

**Páginas criadas:**
- `wiki/sources/iso-27001-dicionario-programador.md`
- `wiki/concepts/iso-27001.md`
- `wiki/concepts/sgsi-isms.md`
- `wiki/concepts/triade-cia.md`
- `wiki/concepts/segregacao-de-funcoes.md`
- `wiki/concepts/iso-42001.md`
- `wiki/entities/mercado-livre.md`

**Páginas atualizadas:**
- `wiki/concepts/compliance.md` — nova seção "ISO 27001 em Detalhe" (SGSI, tríade CIA, Anexo A, SoA, segregação de funções); `source_count` 2 → 3
- `wiki/concepts/audit-log.md` — nota sobre renumeração do Anexo A na versão 2022 (A.12.4 pré-2022 vs. numeração atual); `source_count` 2 → 3
- `wiki/concepts/principio-menor-privilegio.md` — mapeamento para o controle A.5.15 do Anexo A; `source_count` 1 → 2
- `wiki/entities/nubank.md` — nova seção "Segurança e Compliance" (certificação ISO 27001, "modo rua" como controle de acesso contextual); `source_count` 1 → 2
- `wiki/index.md` — nova fonte na tabela de Sources; 5 novos conceitos em "Segurança de APIs & Arquitetura"; nova entidade Mercado Livre

**Notas:** Fonte é a transcrição bruta (traduzida/limpa a pedido do usuário, conteúdo já estava em português) de um vídeo do formato "Dicionário do Programador" (apresentadores Gabriel e Vanessa Weber) sobre ISO/IEC 27001. Contradição potencial e não resolvida: a numeração de controles do Anexo A citada nesta fonte usa a versão 2022 (A.8.28, A.5.15, A.5.8, A.8.25, A.5.3, A.8.4, A.5.34), enquanto [[wiki/sources/compliance-soc2-pci]] e [[wiki/concepts/audit-log]] (ingeridos antes) citam numeração pré-2022 ("A.12.4" para logging). A reorganização de 2022 de fato renumerou o Anexo A de 114 para 93 controles — não é necessariamente erro de nenhuma das duas fontes — mas o mapeamento exato entre as duas numerações não foi verificado contra o texto oficial da norma em nenhum dos dois ingests. Fica como questão aberta registrada na própria fonte. Outra ressalva: os percentuais citados ("40% mais rápido" para contratos enterprise e para implementação da ISO 42001 partindo da 27001) não têm fonte primária no vídeo e foram marcados como não verificados na fonte. Trecho comercial do vídeo (patrocínio Hostinger) foi preservado no raw mas excluído da ingestão por não ser conteúdo técnico.

---

## [2026-07-03] ingest | 3 Dicas para Colocar Conhecimento em Prática no Trabalho

**Source:** [[wiki/sources/3-dicas-colocar-conhecimento-em-pratica]]
**Skill:** tech-mentor-leadership (`/home/gabriel-martins/Documentos/skills/tech-mentor-leadership/SKILL.md`, referência `technical-mentoring.md`)

**Páginas criadas:**
- `wiki/sources/3-dicas-colocar-conhecimento-em-pratica.md`
- `wiki/concepts/granularidade-de-mudanca.md`
- `wiki/concepts/automacao-pessoal-para-aprender.md`
- `wiki/entities/andre-casciotti.md`

**Páginas atualizadas:**
- `wiki/concepts/pratica-deliberada.md` — nova seção "Prática de Curso vs. Prática no Mundo Real"; `source_count` 2 → 3
- `wiki/concepts/aprendizado-passivo.md` — "entupir de teoria" como padrão pré-IA e independente dela; `source_count` 5 → 6
- `wiki/concepts/aprender-a-aprender.md` — convergência independente com Fábio Akita sobre leitura não-linear de livros técnicos; `source_count` 2 → 3
- `wiki/concepts/autonomia-responsabilidade.md` — nova seção registrando a tensão entre "não peça permissão" (prática pessoal) e "não crie tarefa fora do escopo" (entrega formal); `source_count` 2 → 3
- `wiki/concepts/coesao.md` — coesão aplicada a mudanças de processo, não só a código; `source_count` 1 → 2
- `wiki/concepts/cargo-cult-tecnologico.md` — variante do cargo cult motivada por vaidade tecnológica pessoal, não por autoridade de big tech; `source_count` 1 → 2
- `wiki/concepts/zona-de-desconforto-da-aprendizagem.md` — ambiente real de trabalho como fonte estrutural de desconforto produtivo; `source_count` 1 → 2
- `wiki/index.md` — nova fonte na tabela de Sources; 2 novos conceitos em "Carreira & Soft Skills"; nova entidade André Casciotti

**Notas:** Fonte original é a transcrição bruta de um vídeo do canal "Próximo Nível" (André Casciotti), já em português — o pedido de "traduzir" foi interpretado como organizar a fala corrida em prosa estruturada com seções, não tradução de idioma (registrado ao usuário antes da ingestão). Nenhuma contradição forte com o wiki existente; a única tensão real é parcial, entre a Dica 3 ("não peça permissão, vai lá e faz") e a recomendação já registrada em [[wiki/concepts/autonomia-responsabilidade]] de não criar tarefas fora do escopo pedido — reconciliada no texto porque a fonte fala majoritariamente de automações pessoais fora do pipeline formal de entrega, não de tarefas dentro do sprint. Achado interessante: convergência independente entre esta fonte e [[wiki/sources/pare-de-terceirizar-suas-decisoes]] (Fábio Akita) sobre abandonar a leitura linear de livros técnicos — dois criadores de conteúdo relatando a mesma mudança de método sem se referenciar.

---

## [2026-07-03] ingest | 3 Soft Skills Que Poucos Programadores Dominam

**Source:** [[wiki/sources/3-soft-skills-que-poucos-programadores-dominam]]
**Skill:** tech-mentor-leadership (`/home/gabriel-martins/Documentos/skills/tech-mentor-leadership/SKILL.md`, referência `managing-up.md`)

**Páginas criadas:**
- `wiki/sources/3-soft-skills-que-poucos-programadores-dominam.md`
- `wiki/concepts/comunicacao-persuasiva.md`
- `wiki/concepts/imagem-profissional.md`
- `wiki/concepts/habilidade-de-lidar-com-pessoas.md`
- `wiki/entities/dale-carnegie.md`

**Páginas atualizadas:**
- `wiki/entities/renato-augusto.md` — nova key source (soft skills/carreira, além do conteúdo prévio de design patterns); `source_count` 1 → 2, tags ampliadas
- `wiki/concepts/soft-skills.md` — novas conexões (comunicação persuasiva, habilidade de lidar com pessoas, imagem profissional); `source_count` 1 → 2
- `wiki/concepts/comunicacao-tecnica.md` — nova key source e link para comunicação persuasiva como aplicação tática do mesmo princípio; `source_count` 1 → 2
- `wiki/index.md` — nova fonte na tabela de Sources; 3 novos conceitos em "Carreira & Soft Skills"; nova entidade Dale Carnegie

**Notas:** Fonte original é a transcrição bruta de um vídeo de Renato Augusto, já em português (pedido de "traduzir" não se aplicou — apenas organização em prosa estruturada, registrado ao usuário). Duas alegações da fonte têm evidência fraca e foram marcadas como tal na própria página: (1) a estatística "85% do sucesso profissional vem de habilidade interpessoal, 15% de habilidade técnica", atribuída a "Instituto Carnegie" e Harvard sem citação rastreável — número amplamente repetido em conteúdo de carreira sem base sólida conhecida; (2) o "estudo da EO University" sobre vestimenta e liderança, não identificável. Cruzamento com skill: os dois "gatilhos emocionais" (urgência/ganância) da fonte para vender refatoração são uma versão simplificada e menos rigorosa do framework de *managing up* de `references/managing-up.md` — que exige dados concretos (custo, horas, incidentes passados) em vez de apelo emocional puro, marcado com `[skill: tech-mentor-leadership]` em [[wiki/concepts/comunicacao-persuasiva]] e na própria fonte. Nenhuma contradição forte com o restante da wiki; reforça [[wiki/concepts/soft-skills]] e [[wiki/sources/soft-skills-carreira-tecnologia-eduarda]] com uma camada mais tática (persuasão, aparência) que os textos anteriores sobre soft skills não cobriam.

---

## [2026-07-03] ingest | Escalabilidade Horizontal, Load Balancer e Algoritmos de Balanceamento

**Source:** [[wiki/sources/escalabilidade-horizontal-load-balancer-algoritmos]]
**Skill:** tech-mentor-system-design (`/home/gabriel-martins/Documentos/skills/tech-mentor-system-design/SKILL.md`, referências `system-design.md` e `multi-region-global-lb.md`)

**Páginas criadas:**
- `wiki/sources/escalabilidade-horizontal-load-balancer-algoritmos.md`

**Páginas atualizadas:**
- `wiki/concepts/load-balancer.md` — nova seção "Tipos de Load Balancer" (hardware/software/cloud) e seção "Algoritmos de Balanceamento" expandida (Weighted Round Robin, Least Connections, Least Response Time, Sticky Round Robin, IP Hash); `source_count` 5 → 6
- `wiki/concepts/escalabilidade-vertical.md` — nova key source; `source_count` 1 → 2
- `wiki/concepts/escalabilidade-horizontal.md` — nova key source; `source_count` 3 → 4
- `wiki/concepts/protocolo-de-rede.md` — nova seção "UDP em tempo real: jogos e videochamada"; `source_count` 3 → 4
- `wiki/concepts/websocket-vs-polling.md` — nota sobre WhatsApp como exemplo de arquitetura L4/WebSocket; `source_count` 3 → 4
- `wiki/entities/renato-augusto.md` — nova key source (terceiro domínio de conteúdo: system design/escalabilidade, além de design patterns e soft skills); `source_count` 2 → 3, tags ampliadas, bio atualizada com menção ao "Mapa do Arquiteto"
- `wiki/index.md` — nova fonte na tabela de Sources

**Notas:** Fonte original é a transcrição bruta de outro vídeo de Renato Augusto (mesmo criador já registrado em [[wiki/entities/renato-augusto]]), em português — pedido de "traduzir" interpretado neste caso como manter em português e apenas estruturar em prosa/Markdown (confirmado com o usuário antes da ingestão, diferente da vez anterior em que ficou ambíguo). O caminho de skills referenciado no CLAUDE.md do projeto (`/home/nemomartins/Documentos/new/skills/`) não existe nesta máquina — a skill foi carregada do caminho real usado em ingests recentes (`/home/gabriel-martins/Documentos/skills/`). Esta fonte aprofunda [[wiki/sources/escalabilidade-vertical-horizontal-system-design]], que já cobria escalabilidade vertical/horizontal e Load Balancer em nível introdutório; a nova fonte adiciona a taxonomia de tipos de LB (hardware/software/cloud), a razão pela qual AWS/Azure mantêm produtos separados por camada OSI, e uma camada prática de algoritmos de balanceamento com configuração real em Nginx — sem contradições com o conteúdo existente. Duas lacunas registradas como Open Questions na própria fonte: (1) a promessa do autor de um vídeo dedicado (duas partes) sobre a arquitetura do WhatsApp, ainda não ingerido; (2) a afirmação de que `least_time` é exclusivo do Nginx Plus, não verificada contra documentação oficial atual — marcada como alegação da fonte, não confirmada pela skill.

---

## [2026-07-03] ingest | ORM vs. SQL Puro: Organização de Regras de Negócio e Escolha de Banco de Dados

**Source:** [[wiki/sources/orm-sql-organizacao-regras-negocio-bancos-dados]]
**Skill:** tech-mentor-backend (`/home/gabriel-martins/Documentos/skills/tech-mentor-backend/SKILL.md`, referência `architecture-foundations.md` — anti-pattern "Leaky Abstraction" citando ORM — e `architecture/read-replicas-pooling.md`)

**Páginas criadas:**
- `wiki/sources/orm-sql-organizacao-regras-negocio-bancos-dados.md`
- `wiki/concepts/stored-procedure.md` (stub)
- `wiki/concepts/materialized-view.md` (stub)

**Páginas atualizadas:**
- `wiki/concepts/orm.md` — nova seção reforçando a limitação em relacionamentos profundos/chaves compostas e a vantagem de precisão do SQL direto; `source_count` 1 → 2
- `wiki/concepts/sql-alem-do-basico.md` — nova seção "SQL Direto como Escolha Deliberada"; `source_count` 2 → 3
- `wiki/concepts/database-index.md` — nova nota sobre certeza de estar batendo o índice ao escrever SQL direto; `source_count` 3 → 4
- `wiki/concepts/read-replicas.md` — nova seção "Regra Prática: Relatório Nunca Bate em Produção" (razão de escala: ~10% do tempo é escrita); `source_count` 1 → 2
- `wiki/concepts/relational-vs-nosql.md` — novo critério prático (junções múltiplas vs. dado não estruturado/ML) e nota sobre JSONB reduzir necessidade de poliglota; `source_count` 3 → 4
- `wiki/concepts/postgresql.md` — nova seção "JSONB como Ponte para NoSQL"; `source_count` 2 → 3
- `wiki/sources/banco-de-dados.md` — nova seção "Ver também" apontando para a nova fonte
- `wiki/index.md` — nova fonte na tabela de Sources; dois novos conceitos (stored-procedure, materialized-view) em "Bancos de Dados & SQL"

**Notas:** Fonte original era uma transcrição automática (STT) de um Q&A de live/stream, cheia de erros de reconhecimento — vários termos técnicos foram deturpados foneticamente (ex.: "história possível" → *stored procedure*, "trilhas" → *triggers*, "cores"/"correr" → *queries*/*query*, "curva" → *cursor*, "banco no circo" → *banco NoSQL*). O arquivo `raw/` foi reconstruído por inferência de contexto técnico, não é uma transcrição literal verificada palavra a palavra — registrado explicitamente como nota no topo do arquivo raw e reforçado aqui. Autoria não identificada (sem nome de canal ou palestrante no texto bruto); não foi atribuído a [[wiki/entities/fabio-akita]] apesar de estilo e tema (crítica a ORM, ênfase em SQL direto, escalabilidade) serem compatíveis — evitada atribuição sem evidência direta. Conteúdo é altamente complementar a [[wiki/sources/sql-nao-e-banco-de-dados-uncle-bob]] (mesma tensão SQL-abstraído-vs-direto, ângulo diferente) e a [[wiki/sources/acid-vs-base-garantias-bancos-de-dados]]/[[wiki/sources/read-replicas-connection-pooling]] — sem contradições encontradas. Duas Perguntas Abertas registradas na própria fonte: falta de exemplo concreto de query com chave composta inviável em ORM, e falta de critério objetivo para "quando uma stored procedure deixa de ser saudável".

---

## [2026-07-03] ingest | Operador de CRUD vs. Engenheiro: O Que Existe Debaixo do CRUD

**Source:** [[wiki/sources/operador-de-crud-vs-engenheiro-repertorio]]
**Skill:** tech-mentor-leadership (`/home/gabriel-martins/Documentos/skills/tech-mentor-leadership/SKILL.md`, referência `career-progression.md`)

**Páginas criadas:**
- `wiki/sources/operador-de-crud-vs-engenheiro-repertorio.md`
- `wiki/concepts/bluetooth-le.md` (stub — advertising/scan/pair/GATT, restrições de MTU e reconexão)

**Páginas atualizadas:**
- `wiki/concepts/crud-resolvido.md` — nova seção nomeando "operador de CRUD" como a figura central desta fonte; `source_count` 1 → 2
- `wiki/concepts/complexidade-acidental.md` — terceira fonte independente da dicotomia acidental/essencial, ligada a por que a indústria vendeu "aprenda o framework" como suficiente até 2022; `source_count` 2 → 3
- `wiki/concepts/essential-complexity.md` — gatilhos concretos (escala, rede, concorrência) que forçam a complexidade essencial a emergir; `source_count` 1 → 2
- `wiki/concepts/engenheiro-vs-programador.md` — "operador de CRUD" como sinônimo de programador nesta dicotomia; conexão com "fácil vs. simples" da IA; `source_count` 3 → 4
- `wiki/concepts/repertorio.md` — nova seção "A cola entre a IA e o repertório"; exemplos pessoais do autor (RA/3D, Flash/animação); `source_count` 2 → 3
- `wiki/concepts/back-pressure.md` — nova key source; `source_count` 1 → 2
- `wiki/concepts/idempotencia.md` — nova key source (webhook duplicado, at-least-once vs. exactly-once); `source_count` 1 → 2
- `wiki/concepts/protocolo-de-rede.md` — nova seção "O que acontece antes do primeiro byte de um JSON" (DNS → TCP handshake → TLS → HTTP); `source_count` 4 → 5
- `wiki/concepts/database-index.md` — nova seção "Operador vs. Engenheiro no Uso do Índice"; `source_count` 4 → 5
- `wiki/concepts/mobile-navegacao.md` — nova seção "O Risco Escondido: Memória e Ciclo de Vida" (navigation stack, OOM kill); `source_count` 1 → 2
- `wiki/concepts/mobile-design-system.md` — nova key source; `source_count` 1 → 2
- `wiki/concepts/algoritmos-e-estruturas-de-dados.md` — nova key source (matemática como gramática, laço dentro de laço); `source_count` 4 → 5
- `wiki/index.md` — nova fonte na tabela de Sources; novo conceito `bluetooth-le` em "Fundamentos de CS"

**Notas:** Fonte original é transcrição de fala (ASR) recebida em bloco único e sem pontuação — limpa de erros de reconhecimento, pontuada e estruturada em seções pelo agente, mas mantida em português (usuário confirmou explicitamente antes da ingestão que "traduzir" neste pedido não significava trocar de idioma). Autoria/canal não identificado no texto recebido — nenhuma entidade criada; se o usuário confirmar o canal de origem, criar `wiki/entities/<nome>.md`. Esta fonte é altamente complementar a [[wiki/sources/engenheiro-vs-programador-mercado-ia]] (mesmo tema geral — programador/operador de CRUD vs. engenheiro, complexidade acidental/essencial, repertório vs. ferramenta, IA comoditizando execução — possivelmente mesmo tipo de canal), mas com exemplos e ângulo diferentes: esta cobre redes/Bluetooth/streams/mobile em detalhe técnico maior, a outra cobre o framework eixo-vertical/eixo-horizontal com recomendação de livros. Sem contradições entre as duas — reforço mútuo. Três lacunas registradas como Perguntas Abertas na própria fonte: (1) citação de Rich Hickey ("fácil vs. simples") não verificada contra a palestra original; (2) hierarquia de serviços Bluetooth (GATT) descrita não checada contra a especificação oficial do Bluetooth SIG; (3) autoria não identificada.

---

## [2026-07-04] ingest | Vulnerabilidades Comuns de Segurança em Apps/SaaS

**Source:** [[wiki/sources/vulnerabilidades-comuns-seguranca-apps]]
**Skill:** tech-mentor-security (`/home/nemomartins/Documentos/skills/tech-mentor-security/SKILL.md`, referências `appsec-api.md` e `appsec-js-vulns.md`)

**Páginas criadas:**
- `wiki/sources/vulnerabilidades-comuns-seguranca-apps.md`
- `wiki/concepts/idor.md` (IDOR/BOLA — Broken Object Level Authorization)
- `wiki/concepts/mass-assignment.md` (BOPLA — Broken Object Property Level Authorization)
- `wiki/concepts/webhook-signature-validation.md` (HMAC, timing-safe compare, replay/idempotência)
- `wiki/concepts/exposicao-excessiva-de-dados.md` (Excessive Data Exposure)
- `wiki/concepts/toctou.md` (Time of Check to Time of Use — race condition de backend)
- `wiki/concepts/confiar-no-frontend.md` (anti-padrão raiz: client-side trust)

**Páginas atualizadas:**
- `wiki/concepts/rate-limiting.md` — nova seção sobre custo financeiro direto da ausência de rate limit (registros falsos, cota de e-mail); `source_count` 2 → 3
- `wiki/concepts/attack-surface.md` — nova seção "Rotas Previsíveis como Superfície" (webhook em path padrão); `source_count` 1 → 2
- `wiki/concepts/timing-attack.md` — nova seção aplicando o conceito à assinatura de webhook; `source_count` 2 → 3
- `wiki/concepts/race-condition.md` — nova seção distinguindo a race condition de frontend (fetch/useEffect) da TOCTOU de backend; `source_count` 1 → 2
- `wiki/index.md` — nova fonte na tabela de Sources; 6 novos conceitos em "Segurança de APIs & Arquitetura"

**Notas:** Fonte era transcrição bruta de um vídeo em português com fala coloquial e sem pontuação (incluindo uma demonstração prática de bypass client-side via DevTools/breakpoint) — reescrita em `raw/` como markdown estruturado por seção antes da ingestão, sem tradução (já estava em português) e sem alterar o conteúdo técnico. Distinção deliberada feita entre [[wiki/concepts/toctou]] (race condition de concorrência em recurso compartilhado no backend, ex. saldo/estoque) e [[wiki/concepts/race-condition]] (bug de frontend por respostas de fetch fora de ordem em `useEffect`) — mesma família de nome mas causas e correções diferentes; ambas as páginas agora se referenciam. Conteúdo é altamente complementar a [[wiki/sources/owasp-top10]] e [[wiki/sources/api-security]] (IDOR/BOLA, Mass Assignment/BOPLA já documentados ali sob a ótica OWASP formal) — esta fonte cobre os mesmos temas com exemplos mais concretos e de forma mais didática/prática, incluindo TOCTOU e a demonstração de bypass de frontend, que não estavam nas fontes anteriores. Sem contradições encontradas. Duas Perguntas Abertas registradas na própria fonte: falta de menção a ferramentas de detecção automatizada de IDOR/BOLA em CI, e falta de exemplo de locking distribuído (fora de um único banco transacional) para TOCTOU em arquitetura multi-serviço.

---

## [2026-07-04] ingest | Produtividade Falsa vs. Produtividade Verdadeira

**Source:** [[wiki/sources/produtividade-falsa-vs-verdadeira]]
**Skill:** tech-mentor-leadership (`/home/nemomartins/Documentos/skills/tech-mentor-leadership/SKILL.md` — nenhum arquivo de referência específico casou com o tópico; ingerido com conhecimento base do skill, conforme protocolo)

**Páginas criadas:**
- `wiki/sources/produtividade-falsa-vs-verdadeira.md`
- `wiki/concepts/ativo-vs-produtivo.md` (distinção central: terminar tarefas no prazo vs. preencher tempo livre com atividade de aparência produtiva)
- `wiki/concepts/principio-de-pareto.md` (80/20 — qualidade/tempo investido não torna uma tarefa importante)
- `wiki/concepts/eficacia-vs-eficiencia.md` (fazer a coisa certa vs. fazer qualquer coisa de forma econômica)
- `wiki/concepts/tecnica-do-ataque-cardiaco.md` (técnica de Tim Ferriss para achar as tarefas de maior impacto)
- `wiki/concepts/sobrecarga-de-informacao.md` (Herbert Simon — riqueza de informação cria pobreza de atenção; Pascal — incapacidade de silêncio)

**Páginas atualizadas:**
- `wiki/concepts/burnout-dev.md` — nova seção "Confundir Atividade com Progresso"; `source_count` 1 → 2
- `wiki/concepts/dopamina-produtividade.md` — nova seção "Sobrecarga de Informação como Distração"; `source_count` 1 → 2
- `wiki/index.md` — nova fonte na tabela de Sources; 5 novos conceitos em "Carreira & Soft Skills"

**Notas:** Fonte original era transcrição bruta de ASR (fala em bloco único, sem pontuação) — reescrita em `raw/produtividade-falsa-vs-verdadeira.md` como markdown estruturado por seções pelo agente, mantida em português (não havia necessidade de tradução). Autoria não confirmada explicitamente no texto: há pistas fortes (canal paralelo sobre aviação/música, esposa Renata, filho Oliver de 7 meses) consistentes com o criador de conteúdo Felipe Deschamps, mas nenhuma página de entidade foi criada até confirmação do usuário — mesmo cuidado já registrado no ingest de [[wiki/sources/operador-de-crud-vs-engenheiro-repertorio]] em 2026-07-03. Conteúdo é complementar a [[wiki/concepts/otimizacao-prematura]] (mesma lógica de "acertar o alvo antes de otimizar a pontaria", aplicada a código em vez de produtividade pessoal) e a [[wiki/concepts/paralisia-por-analise]] (excesso — de opções ou de estímulo — travando resultado real). Sem contradições encontradas com o restante da wiki. Três questões abertas registradas na própria fonte: autoria não confirmada, citações de Pascal/Herbert Simon não verificadas contra fonte primária, e três vídeos relacionados do mesmo autor mencionados mas não ingeridos.

---

## [2026-07-04] fix | Apagão de Devs Sêniors e Vibe Coding — drift de índice

**Source:** [[wiki/sources/apagao-de-seniors-vibe-coding]] (já existente em `raw/` e já ingerida em 2026-04-29 — usuário colou a mesma transcrição novamente pedindo para recriar o `.md` e rodar "ingest this"; conteúdo idêntico ao já ingerido, nenhuma criação nova de fonte)

**Achado:** a fonte tinha página completa em `wiki/sources/`, estava referenciada em outras páginas e no log, mas nunca apareceu em `wiki/index.md` (index/log drift), e duas das páginas de conceito que ela linka (`[[apagao-de-seniors]]`, `[[adaptive-thinking]]`) nunca foram criadas (broken links de stub pendente).

**Páginas criadas:**
- `wiki/concepts/apagao-de-seniors.md` (stub)
- `wiki/concepts/adaptive-thinking.md` (stub)

**Páginas atualizadas:**
- `wiki/index.md` — adicionada linha da fonte na tabela de Sources; adicionadas 4 linhas em "Qualidade de Software com IA" (apagao-de-seniors, n-plus-um-detector, property-based-testing, adaptive-thinking — as duas últimas também estavam faltando no índice apesar de já existirem)

**Notas:** Nenhum conteúdo novo foi ingerido — apenas fechamento de lacunas de um ingest anterior incompleto. Raw file não foi recriado por já existir com conteúdo idêntico ao colado pelo usuário.

---

## [2026-07-04] ingest | React 19 Memoization: Chega o Fim do useMemo e useCallback?

**Source:** [[wiki/sources/react-19-memoization-sem-usememo-usecallback]]
**Skill:** tech-mentor-frontend (`references/frameworks/react-performance.md`)
**URL original:** https://medium.com/front-end-world/react-19-memoization-no-more-usememo-usecallback-3a09a986f9c7 (autor: Komal Raut, Medium, fev/2025)

**Páginas criadas:**
- `wiki/sources/react-19-memoization-sem-usememo-usecallback.md`
- `wiki/concepts/react-compiler.md` (conceito próprio — antes o React Compiler só existia embutido, mal referenciado, dentro de `concurrent-mode.md`)

**Páginas atualizadas:**
- `wiki/concepts/useMemo.md` — `source_count` 1 → 2; corrigido link quebrado/mal rotulado `[[concurrent-mode|React Compiler]]` para `[[react-compiler]]`
- `wiki/concepts/useCallback.md` — `source_count` 1 → 2; mesma correção de link
- `wiki/concepts/concurrent-mode.md` — seção "React Compiler (beta)" substituída por link de distinção para `[[react-compiler]]` (conteúdo movido, não duplicado)
- `wiki/entities/react.md` — `source_count` 1 → 2; nova fonte
- `wiki/index.md` — nova linha em Sources; 4 novas linhas em "Frontend & Design Engineering" (react-compiler, useMemo, useCallback, concurrent-mode — as três últimas já existiam como páginas mas nunca tinham entrado no índice, um drift antigo)

**Notas:** Artigo em inglês, traduzido integralmente para PT-BR em `raw/react-19-memoization-sem-usememo-usecallback.md` antes da ingestão (conteúdo colado pelo usuário — WebFetch inicial só retornou introdução por paywall do Medium). Conteúdo é introdutório e superficial frente ao que já estava em [[wiki/sources/react-tudo-que-voce-precisa-saber]] — sem contradições, mas também sem detalhamento técnico novo (não cita `babel-plugin-react-compiler`, não menciona a exigência de aderência às Rules of Hooks). Aproveitado o ingest para corrigir um drift antigo: `useMemo`, `useCallback` e `concurrent-mode` já existiam como páginas estáveis desde 2026-04-22 mas nunca haviam sido listadas em `wiki/index.md`. Duas perguntas abertas registradas na própria fonte: falta de exemplo concreto de "cálculo custoso que o compiler não otimiza", e ausência de benchmark real citado pelo autor.

---

## [2026-07-09] ingest | 5 Princípios Que Me Mudaram Como Programador

**Source:** [[wiki/sources/5-principios-que-mudaram-como-programador]]
**Skill:** tech-mentor-leadership (`references/software-craftsmanship.md` — Boy Scout Rule já citado ali como estratégia de pagamento de tech debt; demais princípios com conhecimento base do skill, conforme protocolo)

**Páginas criadas:**
- `wiki/sources/5-principios-que-mudaram-como-programador.md`
- `wiki/concepts/boy-scout-rule.md` (deixar o código mais limpo a cada mudança — popularizado por Uncle Bob)
- `wiki/concepts/codigo-para-o-mantenedor.md` (escrever para quem vai manter, inclusive código gerado por IA)
- `wiki/concepts/fazer-a-coisa-mais-simples-que-poderia-funcionar.md` (princípio de XP, irmão de KISS e YAGNI)

**Páginas atualizadas:**
- `wiki/concepts/yagni.md` — `source_count` 3 → 4; nova seção ligando a `fazer-a-coisa-mais-simples-que-poderia-funcionar`
- `wiki/concepts/otimizacao-prematura.md` — `source_count` 1 → 2; reforço com exemplo de microsserviços/cache prematuros
- `wiki/concepts/kiss.md` — `source_count` 1 → 2; distinção explícita entre KISS (disciplina geral) e "do the simplest thing" (heurística de primeira tentativa de XP)
- `wiki/concepts/tech-debt-como-ferramenta.md` — `source_count` 3 → 4; nova seção ligando pagamento de debt inadvertido à Boy Scout Rule
- `wiki/entities/uncle-bob.md` — `source_count` 1 → 2; segunda menção, agora como popularizador da Boy Scout Rule
- `wiki/index.md` — nova linha em Sources; 3 novas linhas em "Boas Práticas de Engenharia"

**Notas:** Transcrição bruta de ASR (fala em bloco único, em inglês) — traduzida e estruturada em `raw/5-principios-que-mudaram-como-programador.md`. O nome do arquivo em inglês da fonte original (`5-principles-that-changed-me-as-a-programmer`) coincide por acaso com o título de outro vídeo já ingerido em 2026-04-29 (`wiki/sources/5-principles-that-changed-me-as-a-programmer.md`) — conteúdo totalmente diferente (logs, comportamento de usuário, tech debt, naming, paridade de ambiente vs. Boy Scout Rule, otimização prematura, código para o mantenedor, YAGNI, "do the simplest thing that could possibly work"), então foi tratado como fonte nova e independente, com nome de arquivo em português para evitar colisão. Sem contradições com o restante da wiki — os cinco princípios reforçam conceitos já estáveis ([[wiki/concepts/yagni]], [[wiki/concepts/otimizacao-prematura]]) em vez de conflitar com eles. Autor do vídeo não identificado (sem canal, URL ou data na transcrição). Autor menciona uma "segunda parte" com mais princípios — não disponível, não ingerida.

---

## [2026-07-09] ingest | Como Eu Identifico os Próximos Hypes (e Como Isso Se Conecta com Investimentos)

**Source:** [[wiki/sources/como-identificar-o-proximo-hype-tecnologico]]
**Skill:** tech-mentor-leadership (conhecimento base do domínio — diretório `/home/nemomartins/Documentos/new/skills/` referenciado no CLAUDE.md não existe neste ambiente; mesmo protocolo já usado no ingest anterior de "5 Princípios Que Me Mudaram Como Programador")

**Páginas criadas:**
- `wiki/sources/como-identificar-o-proximo-hype-tecnologico.md`
- `wiki/concepts/triade-retorno-risco-liquidez.md` (modelo geral: retorno, risco e liquidez nunca são bons ao mesmo tempo — origem em investimentos, generalizado para qualquer decisão)
- `wiki/concepts/avaliar-hype-tecnologico.md` (aplicação da tríade à decisão de adotar tecnologia hype; caso Node.js no Pagar.me vs. C# na Stone)
- `wiki/entities/filipe-deschamps.md` (fundador do TabNews, autor do vídeo)
- `wiki/entities/tabnews.md`
- `wiki/entities/pagar-me.md`
- `wiki/entities/stone.md`

**Páginas atualizadas:**
- `wiki/concepts/escolha-de-stack.md` — `source_count` 1 → 2; nova seção ligando a dicotomia aprender-vs-monetizar à tríade retorno-risco-liquidez
- `wiki/concepts/tech-debt-como-ferramenta.md` — `source_count` 4 → 5; nova seção lendo o quadrante de Fowler pela ótica da tríade
- `wiki/concepts/hype-de-ia.md` — `source_count` 1 → 2; nota distinguindo o hype de IA financiado por VC do padrão geral de detecção de hype (cross-canal)
- `wiki/concepts/vibe-coding.md` — `source_count` 3 → 4; citado como exemplo de hype em formação no momento do vídeo
- `wiki/concepts/mcp-arquitetura.md` — `source_count` 2 → 3; mesmo motivo (hype em formação, citado junto com Vibe Coding)
- `wiki/index.md` — nova linha em Sources; 2 novas linhas em "Boas Práticas de Engenharia"; 4 novas linhas em Entities

**Notas:** Transcrição em português (sem necessidade de tradução), formato "Request/Response" do TabNews respondendo a um request de Luan Grigolon (não promovido a entidade própria — papel pontual de solicitante, mencionado na página do TabNews). Vídeo não tem data de publicação identificável na transcrição; a apresentação de Pedro Franceschi na RupyIC Conference é referida como "~11 anos atrás", útil só como estimativa relativa. Sem contradições com o restante da wiki — o caso Pagar.me/Node.js vs. Stone/C# reforça [[wiki/concepts/escolha-de-stack]] (já documentado) em vez de conflitar, e a tríade retorno-risco-liquidez dá vocabulário formal para o que [[wiki/concepts/tech-debt-como-ferramenta]] já descrevia informalmente (debt só vale a pena com retorno proporcional ao risco/liquidez ruins). Vibe Coding e MCP foram tratados como meras citações de exemplo (hype em formação no momento do vídeo) — não head de conteúdo novo sobre essas duas tecnologias em si, por isso o touch nessas páginas foi leve (uma seção curta cada, sem reescrever o conteúdo existente).

---

## [2026-07-09] ingest | Sistemas de Arquivos Explicados

**Source:** [[wiki/sources/sistemas-de-arquivos-explicados]]
**Skill:** cs-fundamentals (conhecimento base do domínio — diretório `/home/nemomartins/Documentos/new/skills/` referenciado no CLAUDE.md não existe neste ambiente; mesmo protocolo já usado nos dois ingests anteriores)

**Páginas criadas:**
- `wiki/sources/sistemas-de-arquivos-explicados.md`
- `wiki/concepts/journaling.md` (promovido de seção embutida em `sistema-de-arquivos.md` para página própria — recurso citado por NTFS, ext3/4, HFS+, ZFS, então merece ser referenciável isoladamente)
- `wiki/concepts/fat32.md` (linhagem FAT12/FAT16/FAT32)
- `wiki/concepts/exfat.md`
- `wiki/concepts/ntfs.md`
- `wiki/concepts/apfs.md` (linhagem HFS/HFS+/APFS)
- `wiki/concepts/ext4.md` (linhagem ext2/ext3/ext4)
- `wiki/concepts/zfs.md`

**Páginas atualizadas:**
- `wiki/concepts/sistema-de-arquivos.md` — `source_count` 2 → 3; tabela comparativa agora linka para as páginas individuais de cada sistema de arquivos; seção "Journaling" resumida com link para a página própria
- `wiki/index.md` — nova linha em Sources; 8 novas linhas em "Fundamentos de Sistemas Operacionais"

**Notas:** Transcrição em português (sem necessidade de tradução) — arquivo criado em `raw/sistemas-de-arquivos-explicados.md` com um bloco publicitário sobre um curso de investimentos (AVP) omitido por não ser conteúdo técnico, sinalizado explicitamente no raw. Vídeo é um panorama enumerativo (nenhuma fonte primária, sem autor/canal/data identificáveis na transcrição) — tratado como fonte de referência factual sobre limites técnicos de cada sistema de arquivos, não como opinião a triangular. Sem contradições com o restante da wiki: a tabela comparativa que já existia em [[wiki/concepts/sistema-de-arquivos]] (ext4/NTFS/APFS/ZFS/Btrfs) foi mantida e enriquecida, não substituída — Btrfs continua sem página própria por não ser coberto por esta fonte. Questões abertas registradas na fonte: cobertura ausente de Btrfs em profundidade, F2FS e ReFS (sucessor do NTFS para Windows Server), e se a proteção por checksum do ZFS é exclusiva dele ou compartilhada por outros sistemas copy-on-write como o Btrfs.


---

## [2026-07-09] ingest | Fundamentos de Software Importam Mais que Nunca na Era da IA

**Source:** [[wiki/sources/fundamentos-de-software-importam-mais-que-nunca-na-era-da-ia]]
**Autor:** Matt Pocock (AI Hero)
**Skill:** tech-mentor-backend (referência `architecture/ddd-advanced.md`, que já cobre Ubiquitous Language e módulos profundos — diretório real em `/home/gabriel-martins/Documentos/skills/`, não `/home/nemomartins/...` referenciado no CLAUDE.md, mesmo protocolo já usado nos ingests anteriores)

**Páginas criadas:**
- `wiki/sources/fundamentos-de-software-importam-mais-que-nunca-na-era-da-ia.md`
- `wiki/entities/john-ousterhout.md` (autor de *A Philosophy of Software Design*, citado de segunda mão em `arquitetura-de-software.md` desde antes — agora com página própria e citação de primeira mão)
- `wiki/entities/kent-beck.md` (criador do TDD moderno e da XP — ainda sem página apesar de `tdd.md` já existir e citar o ciclo RED-GREEN-REFACTOR dele)
- `wiki/concepts/modulo-profundo.md` (deep module / shallow module de Ousterhout — conceito central da palestra, sem cobertura prévia na wiki)

**Páginas atualizadas:**
- `wiki/entities/matt-pocock.md` — `source_count` 1 → 2; nova seção sobre a tese "código não é barato"
- `wiki/entities/fred-brooks.md` — `source_count` 1 → 2; nova entrada sobre *The Design of Design* e o conceito de "design concept" (teoria compartilhada e invisível entre quem projeta algo junto), aplicado à colaboração humano-IA
- `wiki/concepts/spec-driven-development.md` — `source_count` 8 → 9; nova seção crítica: "specs to code" sem inspeção de código degenera em vibe coding disfarçado
- `wiki/concepts/vibe-coding.md` — `source_count` 4 → 5; nova seção ligando "specs to code" ao mesmo padrão de decadência progressiva do vibe coding
- `wiki/concepts/tdd.md` — `source_count` 3 → 4; duas novas seções: "outrunning your headlights" (Pragmatic Programmer) aplicado a LLMs, e por que TDD depende de módulos profundos para não virar teste flaky/mockado demais
- `wiki/concepts/ddd.md` — `source_count` 1 → 2; nova seção aplicando Ubiquitous Language ao alinhamento dev-IA (terminologia extraída da codebase, não escrita do zero)
- `wiki/concepts/complexidade-acidental.md` — `source_count` 3 → 4; quarta fonte da distinção essencial/acidental via definição de Ousterhout (estrutura, não implementação)
- `wiki/concepts/arquitetura-de-software.md` — `source_count` 2 → 3; nova seção sobre módulos profundos como unidade estrutural concreta da arquitetura que escala
- `wiki/concepts/entendimento-de-dominio.md` — `source_count` 2 → 3; nova seção sobre a skill de linguagem ubíqua extraída da codebase
- `wiki/concepts/prd-product-requirements-document.md` — `source_count` 3 → 4; nova seção "grill me" — entrevista adversarial para alinhar design concept antes de escrever o PRD
- `wiki/concepts/tech-spec.md` — `source_count` 2 → 3; nova seção sobre especificar mudanças de módulo/interface na tech spec, não só contratos de API externos
- `wiki/index.md` — nova linha em Sources; nova linha em "Boas Práticas de Engenharia" (módulo profundo); 3 novas linhas em Entities (fred-brooks estava faltando no índice apesar de a página já existir — drift corrigido; john-ousterhout e kent-beck adicionados); hook de matt-pocock atualizado

**Notas:** Transcrição em inglês, traduzida para português ao criar `raw/fundamentos-de-software-importam-mais-que-nunca-na-era-da-ia.md` (conforme instrução do usuário). O autor da palestra é Matt Pocock — confirmado pela menção a aihero.dev e ao curso "Claude Code for Real Engineers", que já tinha entidade própria na wiki (`matt-pocock.md`, criada com status stub a partir de outra fonte sobre tokens/LLM). O argumento central da palestra ("código não é barato", crítica ao movimento "specs to code") é relato de experiência pessoal do autor, não estudo controlado — mas consistente com o que a wiki já registra sobre riscos do vibe coding sem harness de qualidade, então foi tratado como reforço de padrão já observado, não como claim isolado a triangular. Durante o ingest notei um drift pré-existente: `wiki/entities/fred-brooks.md` já existia desde 2026-04-23 mas nunca tinha sido adicionado a `index.md` — corrigido nesta ingestão. Questões abertas registradas na fonte: a skill "grill me" citada pelo autor (repositório "Mac PCO skills") não foi verificada — sem acesso à URL para confirmar a contagem de estrelas ou examinar o código; a citação atribuída a Kent Beck ("invest in the design of the system every day") não tem fonte primária identificada na palestra, vale checar contra *Tidy First?* em ingestão futura.

---

## [2026-07-09] ingest | Tipos de Deploy

**Source:** [[wiki/sources/tipos-de-deploy]]
**Skill:** tech-mentor-infra (referência `references/devops/ci-cd-strategies.md`, que já cobre Recreate/Rolling/Blue-Green/Canary/Shadow e a separação deploy vs. release via feature flags)

**Páginas criadas:**
- `wiki/sources/tipos-de-deploy.md`
- `wiki/concepts/deploy-vs-release.md` (distinção central do vídeo — deploy é código na máquina, release é comportamento ligado para o usuário — sem página própria antes, embora `feature-flags.md` já mencionasse "desacopla deploy de release" en passant)
- `wiki/concepts/recreate-deployment.md` (shutdown+start, downtime inevitável — citado no comparativo da skill mas sem página própria na wiki)
- `wiki/concepts/shadow-deployment.md` (tráfego real duplicado para v2 sem servir usuário — citado na tabela "Deployment Strategies" da skill mas sem página própria)
- `wiki/concepts/ab-testing-deployment.md` (split de tráfego para validar hipótese de negócio, distinto de Canary que reduz risco técnico)

**Páginas atualizadas:**
- `wiki/concepts/deploy-strategies.md` — `source_count` 1 → 2; tabela comparativa expandida de 3 para 6 estratégias (Recreate, A/B e Shadow adicionados)
- `wiki/concepts/rolling-update.md` — `source_count` 1 → 2; nova seção linkando ao Recreate como alternativa mais simples/arriscada
- `wiki/concepts/blue-green-deploy.md` — `source_count` 1 → 2; nova seção explicando por que o rollback é rápido (Blue continua de pé)
- `wiki/concepts/canary-release.md` — `source_count` 1 → 2; duas novas seções: Canary deployment vs. Canary release via feature flag (distinção que o vídeo faz explicitamente), e Canary vs. A/B Testing
- `wiki/concepts/feature-flags.md` — `source_count` 1 → 2; link para a nova página `deploy-vs-release`
- `wiki/concepts/zero-downtime-deploy.md` — `source_count` 2 → 3; nota apontando o Recreate como o oposto direto (o problema que todas as estratégias desta página resolvem)
- `wiki/concepts/ci-cd.md` — `source_count` 3 → 4; duas novas seções: deploy manual vs. automático (a diferença é o gatilho, não a ação) e deploy em serverless (cloud administra o roteamento por baixo dos panos)
- `wiki/index.md` — nova linha em Sources; nova seção "Estratégias de Deploy" com 10 linhas (drift corrigido: `deploy-strategies`, `rolling-update`, `blue-green-deploy`, `canary-release`, `zero-downtime-deploy` e `feature-flags` já existiam na wiki desde 2026-04-22 mas nunca tinham sido indexados)

**Notas:** Transcrição já em português — sem necessidade de tradução. Bloco publicitário do patrocinador (HostGator) preservado de forma resumida no `raw/` como parte do fluxo natural da fala, mas não gerou entidade nem claim técnico (ruído comercial, não conteúdo técnico). Fonte é uma aula introdutória/didática sem referências primárias citadas, tratada como complemento prático — não substitui [[wiki/sources/blue-green-canary-rolling]], que já cobria Blue/Green, Canary e Rolling com profundidade técnica de Kubernetes/Argo Rollouts; esta fonte contribui principalmente com o que não estava coberto: a distinção formal deploy vs. release, Recreate como estratégia própria, A/B deployment como conceito distinto de Canary, e Shadow deployment. Sem contradições com o conteúdo técnico já existente. Durante o ingest identifiquei e corrigi um drift de índice pré-existente e não relacionado a esta fonte: seis páginas de deploy criadas em 2026-04-22 (`deploy-strategies`, `rolling-update`, `blue-green-deploy`, `canary-release`, `zero-downtime-deploy`, `feature-flags`) nunca tinham entrado em `wiki/index.md` apesar de já existirem em disco — corrigido nesta ingestão com uma seção nova "Estratégias de Deploy". Questão em aberto registrada na fonte: Shadow deployment com side effects (e-mail, escrita em banco) é levantado como problema mas não resolvido — vale aprofundar em ingestão futura com uma fonte dedicada a progressive delivery.

## [2026-07-09] ingest | Desenvolvedor Acima da Média — 10 Itens para se Destacar

**Source:** [[wiki/sources/desenvolvedor-acima-da-media-10-itens]]
**Skill:** tech-mentor-leadership

**Páginas já existentes no disco (criadas em 2026-04-22, nunca indexadas/logadas):**
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

**Páginas atualizadas nesta sessão:**
- `wiki/index.md` — nova linha em Sources; 9 novas linhas em "Carreira & Soft Skills" (drift corrigido: todas as 9 páginas de conceito e a source já existiam desde 2026-04-22 mas nunca tinham sido indexadas)

**Notas:** Transcrição já em português — sem necessidade de tradução; `raw/desenvolvedor-acima-da-media-10-itens.md` já existia em disco com o mesmo conteúdo exato solicitado nesta sessão. Ao investigar, encontrei que o ingest técnico (source page + 9 conceitos, todos com `[[backlinks]]` cruzados e conteúdo completo) já tinha sido feito integralmente em 2026-04-22, mas nunca chegou a `wiki/index.md` nem a `wiki/log.md` — drift de índice/log pré-existente, corrigido nesta sessão. Conteúdo da source: checklist de 10 itens (do blog "Liro Boy", 60 itens originais) sobre o que distingue um dev sênior acima da média — foco em proximidade com o negócio, ownership proativo, contratação, mentoria, 1:1s, prototipagem antes de produção, flexibilidade técnica, Extreme Ownership (Jocko Willink) e trazer solução junto do problema. Questões abertas já registradas na source: vale ingerir os outros 50 itens da lista original do "Liro Boy"? Como equilibrar item 2 (puxar responsabilidade) com item 7 (não ser inflexível) quando você é o único com contexto suficiente?

---

## [2026-07-09] ingest | 9 Algoritmos que Todo Programador Deveria Saber

**Source:** [[wiki/sources/9-algoritmos-que-todo-programador-deveria-saber]] — transcrição de vídeo em inglês (canal de Forrest), traduzida integralmente para português e reescrita como markdown estruturado em `raw/9-algoritmos-que-todo-programador-deveria-saber.md`
**Skill:** cs-fundamentals — carregado `SKILL.md` e os arquivos de referência `algorithms-complexity.md` e `data-structures.md` (seção Grafos) em `/home/gabriel-martins/Documentos/skills/cs-fundamentals/` para calibrar nomenclatura e validar as afirmações de complexidade da transcrição contra a referência técnica

**Páginas criadas:**
- `wiki/sources/9-algoritmos-que-todo-programador-deveria-saber.md`
- `wiki/concepts/algoritmos-de-ordenacao.md` (Bubble Sort, Insertion Sort, Merge Sort — nenhuma página própria existia; só eram citados en passant em `algoritmos-e-estruturas-de-dados.md`)
- `wiki/concepts/algoritmos-de-busca.md` (Linear Search, Binary Search — mesma situação, citados mas sem página própria)
- `wiki/concepts/algoritmos-de-grafo.md` (DFS, BFS, Dijkstra, A* — mesma situação)

**Páginas atualizadas:**
- `wiki/concepts/algoritmos-e-estruturas-de-dados.md` — `source_count` 5 → 6; sequência de aprendizado agora linka para as três novas páginas de conceito
- `wiki/concepts/big-o.md` — `source_count` 1 → 2; nova seção de relação com as três páginas novas, ilustrando a tabela de complexidade com exemplos concretos
- `wiki/concepts/recursao.md` — `source_count` 1 → 2; linka DFS/Merge Sort às novas páginas
- `wiki/concepts/arvore.md` — `source_count` 3 → 4; nova relação explicando árvore como caso particular de grafo
- `wiki/index.md` — nova linha em Sources; três novas linhas em Concepts logo após `algoritmos-e-estruturas-de-dados`

**Notas:** Transcrição original em inglês (ASR de vídeo do YouTube), traduzida integralmente para português antes de salvar em `raw/` — nomes de algoritmos mantidos em inglês por serem termos técnicos padrão (Bubble Sort, Merge Sort, DFS, BFS, etc.), conforme convenção já usada em `wiki/concepts/big-o.md` e outras páginas de `cs-fundamentals`. Todas as afirmações de complexidade da fonte foram cross-checadas contra `references/algorithms-complexity.md` e `references/data-structures.md` da skill `cs-fundamentals` e batem integralmente — nenhuma contradição encontrada. A fonte é complementar a `10-conceitos-fundamentais-computacao` (que cobre CS de forma mais ampla) e a `estruturas-de-dados-pratica-array-hashmap-fila-pilha-arvore` (que cobre estruturas, não algoritmos) — juntas as três fontes agora cobrem toda a "Sequência de aprendizado sugerida" listada em `algoritmos-e-estruturas-de-dados.md`. Questões em aberto registradas na source: a fonte não explica a condição de admissibilidade da heurística do A* nem detalha por que Quicksort é O(n²) no pior caso — ambas ficam como lacuna para uma fonte técnica futura mais rigorosa (ex: um paper ou a documentação formal de CLRS).

---

## [2026-07-09] ingest | Como um Compilador Transforma Código em Instruções de Máquina

**Source:** [[wiki/sources/como-um-compilador-transforma-codigo-em-instrucoes-de-maquina]] — transcrição em português, salva como markdown estruturado em `raw/como-um-compilador-transforma-codigo-em-instrucoes-de-maquina.md` (sem necessidade de tradução)
**Skill:** cs-fundamentals — carregado `SKILL.md` e `references/compiler-fundamentals.md` em `/home/gabriel-martins/Documentos/skills/cs-fundamentals/` para calibrar nomenclatura e cross-checar o pipeline de 6 estágios e as otimizações citadas

**Páginas criadas:**
- `wiki/sources/como-um-compilador-transforma-codigo-em-instrucoes-de-maquina.md`

**Páginas atualizadas:**
- `wiki/concepts/compilador.md` — `source_count` 2 → 3; pipeline expandido de 3 para 5 seções (separou "Otimização + Geração de Código" e inseriu "Análise Semântica" e "Representação Intermediária (IR)" como estágios próprios); nova explicação de tabela de símbolos e de alocação de registradores
- `wiki/concepts/pipeline-de-compilacao.md` — `source_count` 2 → 3; nova seção relacionando o pipeline de 4 fases do GCC (toolchain) com o pipeline de 6 estágios do front-end do compilador (o segundo roda dentro da fase "Compilação" do primeiro)
- `wiki/index.md` — nova linha em Sources, logo após `desenvolvedor-acima-da-media-10-itens`

**Notas:** Transcrição já em português — sem necessidade de tradução. A wiki já tinha duas páginas de conceito bem desenvolvidas sobre compiladores (`compilador.md` e `pipeline-de-compilacao.md`), então esta fonte não gerou páginas novas de conceito — em vez disso, preencheu lacunas específicas que as páginas existentes não cobriam em detalhe: a análise semântica como estágio próprio (com tabela de símbolos), a IR como forma atômica anti-N×M, e a alocação de registradores na geração de código. Todas as afirmações (as seis etapas, as quatro otimizações citadas — constant folding, dead code elimination, loop unrolling, inlining — e a distinção compilador/interpretador/JIT) foram cross-checadas contra `cs-fundamentals/compiler-fundamentals.md` e batem integralmente, sem contradições. A fonte é mais rasa que a referência técnica da skill (não cita técnicas de parsing, LLVM, WASM ou algoritmos de alocação de registradores), mas serve como uma passagem didática e sequencial pelo pipeline, útil como complemento introdutório a `compilador.md`. Questões em aberto registradas na source: técnicas de parsing reais (recursive descent, LR(k)), backends concretos (LLVM/GraalVM/WASM) e algoritmos de alocação de registradores (graph coloring, linear scan) ficam como lacuna para uma fonte técnica futura mais avançada.

---

## [2026-07-09] ingest | Pub/Sub, Message Queue e BullMQ na Prática

**Source:** [[wiki/sources/pub-sub-message-queue-bullmq-na-pratica]] — transcrição em português, salva como markdown estruturado em `raw/pub-sub-message-queue-bullmq-na-pratica.md` (sem necessidade de tradução; blocos de patrocínio e divulgação de curso omitidos por não serem conteúdo técnico)
**Skill:** tech-mentor-backend — carregado `SKILL.md` e `references/background-jobs.md` em `/home/gabriel-martins/Documentos/skills/tech-mentor-backend/` para calibrar a distinção Pub/Sub vs. message queue e cross-checar os padrões de BullMQ (retry, DLQ, idempotência via `jobId`)

**Páginas criadas:**
- `wiki/sources/pub-sub-message-queue-bullmq-na-pratica.md`
- `wiki/concepts/bullmq.md` (stub — nenhuma página cobria a lib especificamente; `filas-e-workers.md` e `mensageria.md` só citavam BullMQ en passant)

**Páginas atualizadas:**
- `wiki/concepts/pub-sub.md` — `source_count` 3 → 4; nova seção "Distinção de Message Queue: quem depende de quem", formalizando a inversão de dependência (publisher depende do worker numa queue; subscriber depende do publisher em Pub/Sub) como critério prático para escolher entre os dois modelos
- `wiki/concepts/mensageria.md` — `source_count` 3 → 4; nova linha citando BullMQ como implementação de queue em Node.js/Bun
- `wiki/concepts/filas-e-workers.md` — `source_count` 1 → 2; nova seção espelhando a distinção de Pub/Sub e um exemplo mínimo de producer/worker com BullMQ
- `wiki/concepts/fila.md` — `source_count` 1 → 2; nova relação com `bullmq.md` como implementação concreta da estrutura FIFO
- `wiki/index.md` — nova linha em Sources; três novas linhas em Concepts (`pub-sub`, `mensageria` — que faltavam no índice apesar de já existirem como páginas — e `bullmq`, novo)

**Notas:** Transcrição já em português, sem necessidade de tradução. O achado central da fonte é o enquadramento de Pub/Sub vs. message queue por **direção de dependência** em vez de só por "fan-out vs. fila FIFO" — esse ângulo não estava explícito em nenhuma página existente (`pub-sub.md` e `mensageria.md` já cobriam a distinção queue vs. stream, mas não a distinção conceitual entre publicar um fato e publicar um trabalho), então foi adicionado como seção própria nas duas páginas afetadas. Durante o lint incidental do índice, encontrei que `wiki/concepts/pub-sub.md` e `wiki/concepts/mensageria.md` — ambas páginas `stable`/`stub` já estabelecidas com múltiplas fontes — nunca tinham sido adicionadas a `wiki/index.md`; corrigido como parte deste ingest (drift pré-existente, não introduzido por esta fonte). Todas as afirmações de BullMQ (retry/backoff, DLQ manual via `getFailed()`, `jobId` para idempotência) foram cross-checadas contra `tech-mentor-backend/background-jobs.md` e batem — a fonte é mais rasa (cobre só o quickstart), sem contradições. Questões em aberto registradas na source: o vídeo não aprofunda idempotência, retry/backoff nem DLQ no código mostrado — só descreve o comportamento observado (worker retoma de onde parou); esse detalhamento já está coberto por `references/background-jobs.md`, então não abre uma lacuna real na wiki.

---

## [2026-07-09] ingest | HTML vs. Markdown para Agentes de IA

**Source:** [[wiki/sources/html-vs-markdown-para-agentes-de-ia]] — transcrição de vídeo em português, salva como markdown estruturado em `raw/html-vs-markdown-para-agentes-de-ia.md` (sem necessidade de tradução; disfluências e vícios de fala limpos, conteúdo e opiniões preservados)
**Skill:** tech-mentor-ai — carregado `SKILL.md` em `/home/gabriel-martins/Documentos/skills/tech-mentor-ai/`. Nenhum arquivo de `references/` cobre especificamente "HTML vs. Markdown como formato de saída de agente" (verificado via grep por `html`/`markdown` em todo `references/`), então o tópico central da fonte é genuinamente novo na wiki — usei `references/ai/prompt-engineering.md` e `ai-assisted-engineering.md` apenas para calibrar nomenclatura e cross-checar os pontos de prompt engineering e quality gates já cobertos

**Páginas criadas:**
- `wiki/sources/html-vs-markdown-para-agentes-de-ia.md`
- `wiki/concepts/html-vs-markdown-formato-de-saida-agentes.md` (novo — nenhuma página da wiki cobria esse debate especificamente)

**Páginas atualizadas:**
- `wiki/concepts/pipeline-de-qualidade.md` — `source_count` 1 → 2; nova seção de exemplo mostrando quality gate para qualidade de *modelo* (transcrição Whisper local via áudios de referência humano/IA), não apenas qualidade de código — generalização do conceito além do escopo original (lint/testes/segurança)
- `wiki/concepts/prompt-engineering.md` — `source_count` 2 → 3; nova seção "Formato de Estrutura: Markdown, Tags ou HTML?" relacionando a recomendação de Markdown da OpenAI com o debate de formato de saída
- `wiki/entities/anthropic.md` e `wiki/entities/openai.md` — citação de passagem adicionada em Key Sources/Fontes (a fonte só menciona as duas organizações de forma superficial, sem detalhar material específico)
- `wiki/index.md` — nova linha em Sources; nova linha em Concepts logo após `prompt-engineering`

**Notas:** O achado central da fonte é a tensão entre duas práticas: (1) usar HTML gerado por agente como ferramenta de *visualização* para o humano entender sistemas complexos (dois exemplos concretos e verossímeis do autor: relatório de qualidade de transcrição e explicação de implementações de transcrição em tempo real por provedor) e (2) a dúvida, não resolvida pelo próprio narrador, sobre se HTML é de fato melhor que Markdown/tags como formato — ele mesmo relata um teste ad-hoc onde pediu a um modelo para otimizar um prompt com tags e o modelo removeu todas elas, sem chegar a uma conclusão. Tratei a claim de que "a Anthropic divulgou algo parecido" como não verificada, já que a fonte não cita link ou conteúdo específico — registrado como questão em aberto na source e refletido com ressalva na entidade `anthropic.md`. Da mesma forma, não criei página de entidade para "Tarik" (autor do artigo referenciado) por falta de dados verificáveis sobre sua identidade real — ASR pode ter transliterado o nome de forma imprecisa, e nenhuma URL foi citada no vídeo; fica como lacuna para uma fonte futura que cite o artigo original diretamente. A dica final sobre quality gates é o ponto mais solidamente verificável da fonte (mecanismo concreto, replicável, consistente com o padrão de "quality gate determinístico" já em `pipeline-de-qualidade.md`) e foi tratada com confiança alta; o restante do conteúdo (o debate HTML vs. Markdown propriamente dito) foi tratado como opinião/prática emergente sem benchmark, refletido no `status: draft` da nova página de conceito.

---

## [2026-07-09] ingest | Como Evitar o Over-Engineering

**Source:** [[wiki/sources/como-evitar-over-engineering-david-farley]] — transcrição de vídeo já em português (comentário reagindo a um vídeo de David Farley), salva como markdown estruturado em `raw/como-evitar-over-engineering-david-farley.md` (sem necessidade de tradução; disfluências de fala limpas, conteúdo e argumentos preservados)
**Skill:** tech-mentor-leadership — carregado `SKILL.md` e `references/engineering-metrics.md` em `/home/gabriel-martins/Documentos/skills/tech-mentor-leadership/` para calibrar as métricas DORA (thresholds Elite/Alto/Médio/Baixo) citadas na fonte e cross-checar a claim central de correlação velocidade×qualidade

**Páginas criadas:**
- `wiki/sources/como-evitar-over-engineering-david-farley.md`
- `wiki/concepts/dora-metrics.md` (novo — nenhuma página cobria DORA/Accelerate como conceito próprio, apesar de "DORA" aparecer citado de passagem em ~20 páginas)
- `wiki/concepts/walking-skeleton.md` (novo — padrão sem página própria; já existia uma instância não-nomeada dele em `ci-cd.md`, seção "Deploy Imediato do Boilerplate")
- `wiki/entities/david-farley.md` (stub — coautor de *Continuous Delivery*, sem página prévia)

**Páginas atualizadas:**
- `wiki/concepts/over-engineering.md` — `source_count` 1 → 2; nova seção "O maior problema da indústria não é over-engineering — é under-engineering"; seção "Em devs experientes" expandida com as duas causas específicas da fonte (perfeccionismo por falta de objetivo/conhecimento; falta de confiança que antecipa requisitos não-funcionais); nova seção refutando o "triângulo de ferro" com dados DORA
- `wiki/concepts/ci-cd.md` — `source_count` 4 → 5; link explícito entre "Deploy Imediato do Boilerplate" e o padrão formal `walking-skeleton`; nova seção relacionando CI/CD à correlação DORA velocidade×qualidade
- `wiki/concepts/tdd.md` — `source_count` 4 → 5; nova seção curta "TDD não é o que atrasa a entrega", ancorada em DORA
- `wiki/entities/martin-fowler.md` — `source_count` 1 → 2; nova seção de anedota (explicitamente marcada como não verificada) sobre projeto atrasado na Thoughtworks e origem do ágil/XP
- `wiki/index.md` — nova linha em Sources; duas novas linhas em Concepts (`walking-skeleton`, `dora-metrics`); nova linha em Entities (`david-farley`)

**Notas:** O achado central e genuinamente novo da fonte é a refutação do "triângulo de ferro" com a pesquisa DORA/*Accelerate* — nenhuma página da wiki tratava essa correlação empírica entre velocidade e qualidade de forma explícita antes, apesar de `over-engineering.md`, `ci-cd.md` e `tdd.md` já tocarem tangencialmente nos mesmos temas. O segundo achado relevante é a distinção entre as duas causas de over-engineering em devs experientes — perfeccionismo (já documentado, convergente com `overengineering-carol-ate-quinta`) vs. falta de confiança/antecipação de requisitos não-funcionais (nova, com o caso concreto do LMAX e o padrão formal "walking skeleton"). Duas claims da fonte carecem de fonte primária e foram marcadas como não verificadas: (1) a anedota da Thoughtworks/Martin Fowler sobre a origem do ágil, refletida com ressalva explícita na página da entidade; (2) os detalhes técnicos do caso LMAX (mensageria XML/HTTP → protocolo binário), que são plausíveis e consistentes com o trabalho público de Farley mas não foram citados com fonte primária no vídeo — registrado como questão em aberto na source. Nenhuma contradição encontrada com o restante da wiki; a fonte complementa `over-engineering.md` sem substituir nada do que já estava documentado.

---

## [2026-07-09] retroactive fix | Pensamento Estruturado para Resolução de Problemas

**Contexto:** O usuário colou a mesma transcrição já ingerida em 2026-05-01 (`raw/pensamento-estruturado-resolucao-de-problemas.md`, `wiki/sources/pensamento-estruturado-resolucao-de-problemas.md`). Ao invés de duplicar, foi feito um sweep de lint focado nessa fonte, revelando que o ingest original (passos 1–5 do workflow) ficou completo, mas os passos 6–7 (indexação e log) nunca foram executados — drift clássico de índice/log.

**Achados corrigidos:**
- `wiki/index.md` — fonte nunca constava em Sources; adicionada. Os 5 conceitos criados por esse ingest (`pensamento-estruturado`, `arvore-de-decomposicao`, `pensamento-regressivo`, `causa-raiz`, `hipotese-e-validacao`) e o pré-existente `pensamento-sistemico` nunca tinham entrada no índice; criada nova seção "Resolução de Problemas & Debugging Estruturado"
- `wiki/concepts/debugging.md` — linkado pela source (`[[debugging]]`) mas a página nunca existia — link quebrado. Criado stub
- `wiki/concepts/decomposicao-de-problemas.md`, `wiki/concepts/ia-ciclo-dependencia.md`, `wiki/concepts/documentar-conquistas.md` — listados como "Conceitos e Entidades Relacionados" na source, mas nenhum dos três citava a source de volta (backlink faltando); adicionado `Key sources`/seção e `source_count` incrementado em cada um

**Notas:** Nenhum conteúdo novo foi extraído da transcrição em si — o texto colado é idêntico ao já processado. O trabalho aqui foi puramente de reparo de drift (workflow de lint), não de ingest. `raw/` não foi tocado.

---

## [2026-07-09] retroactive fix | Diferenciais de Portfólio para Dev Backend Júnior

**Contexto:** O usuário pediu para transformar a transcrição em MD em `raw/` e ingerir. A transcrição já existia como `raw/diferenciais-portfolio-backend-junior.md` e já tinha sido processada como `wiki/sources/diferenciais-portfolio-backend-junior.md` (ambos commitados no commit inicial `efce70d`), com os 9 conceitos relacionados já criados e backlinkados. Em vez de duplicar, foi feito um sweep de lint focado nessa fonte — mesmo padrão de drift já visto em outras fontes desse commit inicial: passos 1–5 do workflow completos, passos 6–7 (indexação e log) nunca executados.

**Achados corrigidos:**
- `wiki/index.md` — fonte nunca constava em Sources; adicionada. 6 dos 9 conceitos citados pela source (`portfolio-backend-junior`, `docker-portfolio`, `documentacao-api-swagger`, `error-handling-estruturado`, `sql-alem-do-basico`, `curriculo-vs-portfolio`) nunca tinham entrada no índice — adicionados à seção Concepts
- `wiki/concepts/comparacao-na-carreira.md` — listado nos "Conceitos tocados" da source mas não citava a source de volta (backlink faltando); adicionada linha em Key Sources e `source_count` 3 → 4
- `wiki/sources/diferenciais-portfolio-backend-junior.md` — `source_file` apontava para o path do repo antigo (`/home/nemomartins/Documentos/new/dev-study/...`); corrigido para o path atual (`/home/gabriel-martins/Documentos/dev-brain/...`)

**Notas:** Nenhum conteúdo novo foi extraído da transcrição em si — o texto colado é idêntico ao já processado (mesmo conteúdo, só que em fala bruta em vez da versão já estruturada salva em `raw/`). O trabalho aqui foi puramente de reparo de drift, não de ingest. `raw/` não foi tocado.

---

## [2026-07-10] retroactive fix | Acoplamento, Abstração e Estado — Lentes para Enxergar Código

**Contexto:** O usuário pediu para transformar a transcrição em MD em `raw/` e ingerir. A transcrição já existia como `raw/acoplamento-abstracao-estado.md` e já tinha sido processada como `wiki/sources/acoplamento-abstracao-estado.md` (datado 2026-04-25), com os 9 conceitos relacionados (`acoplamento`, `abstracao`, `estado-compartilhado`, `imutabilidade`, `efeito-colateral`, `coesao`, `idempotencia`, `single-responsibility`, `lentes-de-codigo`) já criados e todos com backlink correto em "Key sources". Mesmo padrão de drift já visto em outras fontes deste repo: passos 1–5 do workflow completos, passos 6–7 (indexação e log) nunca executados.

**Achados corrigidos:**
- `wiki/index.md` — fonte nunca constava em Sources; adicionada. 7 dos 9 conceitos (`lentes-de-codigo`, `acoplamento`, `abstracao`, `coesao`, `single-responsibility`, `efeito-colateral`, `estado-compartilhado`) nunca tinham entrada no índice — adicionados à seção "Boas Práticas de Engenharia" (`idempotencia` e `imutabilidade` já constavam em outras seções)

**Notas:** Nenhum conteúdo novo foi extraído da transcrição em si — o texto colado é idêntico ao já processado. O trabalho aqui foi puramente de reparo de drift (workflow de lint), não de ingest. `raw/` não foi tocado; `source_file` na frontmatter da source já apontava para o path correto do repo atual, sem necessidade de correção.

---

## [2026-07-10] retroactive fix | Três Características para Ser o Melhor Candidato

**Contexto:** O usuário pediu para transformar a transcrição em MD em `raw/` e ingerir. A transcrição já existia, já limpa em formato Markdown, como `raw/tres-caracteristicas-melhor-candidato.md`, e já tinha sido processada como `wiki/sources/tres-caracteristicas-melhor-candidato.md` (datado 2026-04-23), com os 6 conceitos/entidade relacionados (`profundidade-e-maestria`, `abrangencia-profissional`, `comunicacao-tecnica`, `curriculo-vs-portfolio`, `maturidade-tecnica`, `comparacao-na-carreira`, `randy-nelson`) já criados. Mesmo padrão de drift já visto repetidas vezes neste repo: passos 1–5 do workflow completos, passos 6–7 (indexação e log) nunca executados.

**Achados corrigidos:**
- `wiki/index.md` — fonte nunca constava em Sources; adicionada. `profundidade-e-maestria` e `abrangencia-profissional` nunca tinham entrada no índice — adicionados à seção "Carreira & Soft Skills". Entidade `randy-nelson` nunca constava em Entities — adicionada
- `wiki/concepts/comparacao-na-carreira.md` — listado nos "Conceitos Tocados" da source mas não citava a source de volta (backlink faltando); adicionada linha em Key Sources e `source_count` 4 → 5

**Notas:** Nenhum conteúdo novo foi extraído da transcrição em si — o texto colado é idêntico ao já processado. O trabalho aqui foi puramente de reparo de drift (workflow de lint), não de ingest. `raw/` não foi tocado; `source_file` na frontmatter da source já apontava para o path correto do repo atual, sem necessidade de correção. As outras 5 páginas relacionadas (`profundidade-e-maestria`, `abrangencia-profissional`, `comunicacao-tecnica`, `curriculo-vs-portfolio`, `maturidade-tecnica`, `randy-nelson`) já citavam a source corretamente em "Key sources" — apenas a indexação central estava faltando.

---

## [2026-07-10] ingest | 5 (ou 6) Recursos Para Se Tornar um Desenvolvedor Melhor

**Fonte:** [[wiki/sources/5-recursos-para-ser-um-desenvolvedor-melhor]] (Augusto Galego) — transcrição bruta salva em `raw/5-recursos-para-ser-um-desenvolvedor-melhor.md`.

**Skill carregada:** `tech-mentor-leadership` (domínio de carreira/mentoria).

**Páginas criadas:**
- `wiki/sources/5-recursos-para-ser-um-desenvolvedor-melhor.md`
- `wiki/concepts/roadmap-sh.md`
- `wiki/concepts/documentacao-oficial-como-recurso.md`
- `wiki/concepts/cs50.md`
- `wiki/concepts/livros-recomendados-programador.md`
- `wiki/concepts/contribuir-open-source.md`
- `wiki/concepts/custo-beneficio-cursos-online.md`
- `wiki/concepts/aprendizado-multimodal.md`

**Páginas atualizadas:**
- `wiki/concepts/good-first-issue.md` — já existia (criado a partir de [[wiki/sources/como-aprender-novas-codebases]] com foco em onboarding interno de time); enriquecido com a perspectiva complementar de contribuição externa a projetos open source, `source_count` 1 → 2
- `wiki/index.md` — nova linha em Sources; nova seção "Recursos de Aprendizado" em Concepts com os 7 conceitos novos

**Notas:** Vídeo opinativo sobre recursos de estudo — contesta LeetCode como melhor uso do tempo e propõe documentação oficial, roadmap.sh, CS50, uma seleção crítica de livros (Refactoring endossado sem ressalvas, Clean Code com reserva explícita sobre o autor), cursos com teto de preço (Udemy ~R$20-30, nunca R$5-10 mil para uma tecnologia pontual) e contribuição em open source via `good first issue`. Fecha reforçando que nenhum recurso substitui escrever muito código na prática. Nenhuma contradição relevante encontrada com o restante do wiki — a avaliação de Clean Code é subjetiva e fica registrada como tal, sem outra fonte no wiki que a contradiga ou reforce até o momento.

---

## [2026-07-10] ingest | Loop Engineering: Por Que Você Deveria Estar Desenhando Loops, Não Prompts

**Fonte:** [[wiki/sources/loop-engineering-planner-critic-grafo]] (autor autoidentificado como "Hulk" na transcrição) — transcrição bruta traduzida/limpa salva em `raw/loop-engineering-planner-critic-grafo.md`.

**Skill carregada:** `tech-mentor-ai` (domínio de agentes/harness/orquestração), referências `agentic-patterns-2025.md` (Padrão 1 — Planner-Executor-Critic) usadas para calibrar nomenclatura.

**Páginas criadas:**
- `wiki/sources/loop-engineering-planner-critic-grafo.md`
- `wiki/concepts/loop-engineering.md`
- `wiki/concepts/planner-executor-critic.md`
- `wiki/concepts/rubrica-de-verificacao.md`
- `wiki/concepts/langgraph.md`
- `wiki/concepts/grafo-como-abstracao-de-agentes.md`

**Páginas atualizadas:**
- `wiki/concepts/harness.md` — nova seção "Próximo Degrau: Loop Engineering"; `source_count` 6 → 7
- `wiki/concepts/ciclo-agente.md` — nova seção sobre sistematizar o brute-force com rúbrica+verificador; `source_count` 4 → 5
- `wiki/concepts/subagentes.md` — nova seção sobre subagentes como executores num loop PEC; `source_count` 1 → 2
- `wiki/sources/agentes-orquestracao.md` — **lint incidental**: os links `[[concepts/planner-executor-critic]]` e `[[concepts/langgraph]]` citados nessa fonte (2026-04-23) nunca tinham sido criados (drift pré-existente); corrigidos para `wiki/concepts/...` e agora resolvem para as páginas criadas nesta ingestão. Os outros 6 links quebrados dessa fonte (`supervisor-pattern`, `handoff-pattern`, `swarm-pattern`, `durable-execution`, `error-boundary-agents`, `checkpointing-agents`) **não** foram corrigidos — fora do escopo desta ingestão, sinalizados para lint futuro.
- `wiki/index.md` — nova linha em Sources; 5 novos conceitos adicionados à seção "Agentes & LLMOps"

**Notas:** Vídeo propõe uma progressão de abstração (prompt engineering → context engineering → harness engineering → loop engineering) e demonstra na prática um sistema Planner-Executor-Critic: um Planner (GPT-5.5) decompõe a entrada em até ~160 subtarefas simultâneas, gerando prompt e rúbrica para cada subagente; um Verificador — obrigatoriamente um modelo diferente do executor, para evitar bias — julga o resultado contra a rúbrica e gera follow-ups (até 3 tentativas no exemplo mostrado) ou aprova. O vídeo defende o grafo (G=(V,E), nós=computação/LLM, arestas=condição de fluxo determinística) como abstração central, independente de LangGraph ou qualquer outro framework. Reforça diretamente [[wiki/sources/agentes-orquestracao]], que já citava Planner-Executor-Critic e LangGraph em termos quase idênticos mas sem exemplo prático nem páginas de conceito criadas — esta ingestão preenche essa lacuna. Sem contradições novas com o resto do wiki; reconhece a mesma tensão token-infinito-vs-qualidade-de-codebase já registrada em [[wiki/concepts/vibe-coding-limites-maturidade-profissional]]. Autoria do vídeo ("Hulk") não verificada externamente — mantida como consta na transcrição, sem criar entidade dedicada dado o baixo grau de confiança na identificação.

---

## [2026-07-10] ingest | Chaves SSH — Como Funcionam, Servidor, Cliente e Configuração

**Fonte:** [[wiki/sources/ssh-chaves-como-funcionam]] — transcrição de vídeo já em português (sem necessidade de tradução), limpa de repetições/disfluências de fala e organizada em seções, salva em `raw/ssh-chaves-como-funcionam.md`.

**Skill carregada:** `tech-mentor-security`, seção "Identidade & Acesso" (`references/identity-iam.md`, exemplo Teleport para acesso unificado SSH) e "Criptografia" (`references/crypto.md`, criptografia assimétrica) usadas para calibrar nomenclatura e evitar tratar SSH como "encriptação de dados" quando na verdade é prova-de-posse de chave (mais próximo de assinatura digital).

**Nota sobre paths do CLAUDE.md:** a skill em `/home/nemomartins/Documentos/new/skills/` referenciada no CLAUDE.md deste repo não existe neste ambiente — o diretório real de skills é `/home/gabriel-martins/Documentos/skills/`. Usado o path real; sinalizado para o usuário corrigir o CLAUDE.md se for drift de configuração.

**Páginas criadas:**
- `wiki/sources/ssh-chaves-como-funcionam.md`
- `wiki/concepts/ssh.md`
- `wiki/concepts/hardening-de-servidor.md`

**Páginas atualizadas:**
- `wiki/concepts/encryption.md` — nova linha na seção "Assimétrica" ligando Ed25519/SSH ao par chave pública/privada; `source_count` 1 → 2
- `wiki/concepts/criptografia.md` — nota após "Assinatura digital" enquadrando autenticação SSH como prova-de-posse, não encriptação de dados; `source_count` 1 → 2
- `wiki/concepts/principio-do-menor-privilegio.md` — nova frase ligando chave SSH + bastion host como duas camadas de menor privilégio (rede + credencial); `source_count` 1 → 2
- `wiki/concepts/defense-in-depth.md` — hardening de infraestrutura adicionado como camada fora da pilha de aplicação já listada; `source_count` 1 → 2
- `wiki/concepts/secure-by-default.md` — exemplo de sshd com defaults de distro mais fracos, reforçados explicitamente; `source_count` 1 → 2
- `wiki/concepts/attack-surface.md` — `AllowTcpForwarding no` e `PermitRootLogin no` como redução de superfície na camada de SO; `source_count` 2 → 3
- `wiki/index.md` — nova linha em Sources; 2 novos conceitos (`ssh`, `hardening-de-servidor`) na seção "Segurança de APIs & Arquitetura"

**Notas:** Vídeo prático (dois containers Docker como cliente/servidor) cobrindo o ciclo completo de chave SSH: gerar par com `ssh-keygen -t ed25519`, autorizar via `authorized_keys`, permissões de arquivo (`700` no diretório, restrito ao dono na chave privada, `644` na pública), configuração do daemon (`sshd_config.d/*.conf`, `PubkeyAuthentication yes` + senha desativada) e aliases de cliente (`~/.ssh/config` com `IdentitiesOnly yes`). Reforça diretamente [[wiki/concepts/encryption]] e [[wiki/concepts/criptografia]] com um exemplo concreto de criptografia assimétrica fora do contexto de TLS/HTTPS já documentado nessas páginas. Também demonstra em código o padrão narrado em [[wiki/concepts/principio-do-menor-privilegio]] (bastion host via SSH) — antes só citado como exemplo abstrato, agora com o mecanismo de autenticação detalhado. Sem contradições com o resto do wiki. Uma alegação de confiança média não verificada nesta ingestão: a ordem exata de leitura de `sshd_config.d/*.conf` pelo OpenSSH (primeira regra que casa prevalece) — fica registrada como open question na fonte para checagem futura contra a documentação oficial do OpenSSH.

---

## [2026-07-10] ingest | Golang: Mercado, Salários e Pesquisa Código Fonte TV (2024)

**Fonte:** [[wiki/sources/golang-mercado-salarios-pesquisa-2024]] — transcrição de fala corrida em português (sem necessidade de tradução), limpa e organizada em seções, salva em `raw/golang-mercado-salarios-pesquisa-2024.md`. Vídeo do canal Código Fonte TV cruzando a pesquisa salarial própria do canal (pesquisa.codefonte.com.br) com o Go Developer Survey oficial do Google.

**Skill carregada:** `tech-mentor-leadership` (mesma skill usada em [[wiki/sources/golang-mercado-trabalho-frontend-para-backend]], tema equivalente de carreira/mercado para Go), seção "Carreira & Níveis" (`references/career-progression.md`) consultada para calibrar linguagem de salário/nível.

**Páginas criadas:**
- `wiki/sources/golang-mercado-salarios-pesquisa-2024.md`
- `wiki/entities/codigo-fonte-tv.md`

**Páginas atualizadas:**
- `wiki/concepts/go-fundamentos.md` — nova frase na seção "Design Cloud Native" com dados de uso do Go Developer Survey (74% API/RPC, maior fatia de experiência 16+ anos); `source_count` 2 → 3
- `wiki/concepts/go-ecossistema.md` — nova seção "Uso Declarado em Produção" cruzando stdlib/ecossistema já documentado com uso real reportado e vagas reais do LinkedIn (Clean Architecture, microsserviços, AWS/GCP); `source_count` 1 → 2
- `wiki/concepts/ciclo-de-mercado-tech.md` — nova frase dando números concretos (Go paga mais que Java em todos os níveis, maior gap no Sênior) ao mecanismo de oferta/demanda já descrito; `source_count` 3 → 4
- `wiki/concepts/modelo-trimodal-compensacao.md` — nova seção "Um Segundo Eixo: Linguagem/Stack, não só Tier de Empresa" distinguindo o eixo de tier de empresa (Orosz) do eixo de raridade de stack (Go vs Java); `source_count` 1 → 2
- `wiki/concepts/dolarizacao-de-renda.md` — nova seção "Especialização em Nicho como Via de Acesso" com o dado de 27,7% dos devs Go no Brasil atuando remoto para o exterior vs. 12% em Java; `source_count` 1 → 2
- `wiki/concepts/ponte-fullstack-para-especializacao.md` — nova seção "Dado de Mercado que Sustenta a Estratégia" com o perfil de experiência dos devs Go (majoritariamente seniors migrando de stack); `source_count` 1 → 2
- `wiki/index.md` — nova linha em Sources; nova linha em Entities (`codigo-fonte-tv`)

**Notas:** Vídeo de dados/pesquisa (não opinativo como a fonte irmã [[wiki/sources/golang-mercado-trabalho-frontend-para-backend]]) trazendo números concretos que sustentam claims que antes só existiam como opinião qualificada no wiki: salário Go > Java em todos os níveis (maior gap no Sênior, ~R$6.000/mês), 93-97% de satisfação em duas pesquisas independentes (Google e Código Fonte), e 27,7% dos devs Go no Brasil trabalhando remoto para empresas estrangeiras (vs. 12% em Java). Reforça diretamente [[wiki/concepts/ciclo-de-mercado-tech]] (a "onda Go" tem números reais por trás) e [[wiki/concepts/ponte-fullstack-para-especializacao]] (o perfil etário/experiência dos devs Go confirma que júnior/pleno concorre contra seniors migrando de stack, não contra outros júniors). Também abre uma conexão nova com [[wiki/concepts/modelo-trimodal-compensacao]] — até agora esse conceito só descrevia variação por tier de empresa (Orosz); esta fonte evidencia um eixo independente, raridade de stack, operando pelo mesmo mecanismo de oferta/demanda. Uma inconsistência não resolvida na própria fonte: o valor de PJ em Go citado na fala ("211.000") é quase certamente erro de transcrição para R$ 21.000 — mantido como open question na fonte, sem correção silenciosa do dado original.

---

## [2026-07-10] ingest | A Filosofia do Design de Software — Introdução (Cap. 1)

**Fonte:** [[wiki/sources/filosofia-do-design-de-software-introducao]] — transcrição em inglês do capítulo introdutório de *A Philosophy of Software Design* (John Ousterhout), traduzida integralmente para português e salva em `raw/filosofia-do-design-de-software-introducao.md`.

**Skill carregada:** `tech-mentor-backend`, seção "Evolutionary Architecture & Quality" (`references/architecture-evolutionary.md`) consultada para calibrar linguagem de qualidade/complexidade arquitetural — mesma skill já usada em [[wiki/sources/fundamentos-de-software-importam-mais-que-nunca-na-era-da-ia]], que citava este mesmo autor de segunda mão.

**Páginas criadas:**
- `wiki/sources/filosofia-do-design-de-software-introducao.md`
- `wiki/concepts/modelo-cascata-vs-desenvolvimento-incremental.md`
- `wiki/concepts/red-flags-de-design.md`

**Páginas atualizadas:**
- `wiki/entities/john-ousterhout.md` — nova seção "Do capítulo introdutório (fonte primária)"; `status` stub → draft; `source_count` 1 → 2
- `wiki/concepts/modulo-profundo.md` — nova seção "Origem no enquadramento geral do livro" ligando módulos profundos às duas estratégias gerais contra complexidade (eliminar vs. encapsular) que abrem o livro; `source_count` 1 → 2
- `wiki/concepts/accidental-complexity.md` — nova seção "Modelo cascata como gerador estrutural de complexidade acidental", mecanismo causal de processo (Ousterhout) complementar ao diagnóstico de Fred Brooks já documentado; `source_count` 2 → 3
- `wiki/concepts/arquitetura-de-software.md` — nova seção "Design de arquitetura como processo contínuo, não fase única"; citação de Ousterhout deixa de ser só de segunda mão; `source_count` 3 → 4
- `wiki/concepts/code-review.md` — nova seção "Code review como método de treino de design, não só de correção"; `source_count` 1 → 2
- `wiki/sources/fundamentos-de-software-importam-mais-que-nunca-na-era-da-ia.md` — nota de atualização apontando para a nova fonte primária que confirma a citação de segunda mão de Ousterhout
- `wiki/index.md` — nova linha em Sources; 2 novas linhas em Concepts (seção "Boas Práticas de Engenharia")

**Notas:** Primeira ingestão de texto primário do próprio livro de Ousterhout — até aqui só existia citação de segunda mão via uma palestra de Matt Pocock ([[wiki/sources/fundamentos-de-software-importam-mais-que-nunca-na-era-da-ia]]). O capítulo 1 traz o enquadramento geral que faltava: complexidade como a real limitação ao escrever software (não física, não de ferramentas), as duas estratégias gerais contra ela (eliminar vs. encapsular — sendo [[wiki/concepts/modulo-profundo]] a elaboração detalhada da segunda, já documentada), por que o modelo cascata falha estruturalmente para software (sem mecanismo de retorno ao design quando os problemas do design inicial aparecem), e o método de trabalho recomendado para todo o livro: reconhecer "red flags" de design, best exercitado via code review do código de outra pessoa. Conecta-se de forma nova com [[wiki/concepts/accidental-complexity]] — Fred Brooks (já documentado) descreve *o quê* é complexidade acidental e suas formas comuns; Ousterhout aqui descreve um mecanismo causal de *processo* (ausência de revisão de design pós-implementação) que explica por que ela se acumula sem correção sob cascata. Sem contradições com o resto do wiki. Uma lacuna registrada como open question na fonte: o texto cita "define errors out of existence" como exemplo de princípio do livro mas não o desenvolve — capítulo dedicado a esse tópico ainda não foi ingerido.

---

## [2026-07-10] ingest | Mappers — Conversão de Entidades Entre Camadas

**Fonte:** [[wiki/sources/mappers-conversao-entre-camadas]] — transcrição de fala corrida em português (sem necessidade de tradução), limpa e organizada em seções, salva em `raw/mappers-conversao-entre-camadas.md`. Vídeo de aula prática sobre uma aplicação de notificações em camadas (entities, use case, HTTP, repositório Prisma).

**Skill carregada:** `tech-mentor-backend`, seção "Clean Architecture, Ports & Adapters, DDD" (`references/architecture-foundations.md`) consultada para calibrar terminologia de Repository/DDD; nenhuma entrada explícita de "mapper" no índice da skill, então o conceito foi calibrado por analogia com Repository/Adapter já presentes na referência.

**Páginas criadas:**
- `wiki/sources/mappers-conversao-entre-camadas.md`
- `wiki/concepts/mapper-pattern.md`

**Páginas atualizadas:**
- `wiki/concepts/repository-pattern.md` — nova frase ligando Data Mapper ao `mapper-pattern` como implementação concreta da conversão campo-a-campo; `source_count` 1 → 2
- `wiki/concepts/adapter-pattern.md` — nova seção "Diferença do Mapper" distinguindo conversão de interface (Adapter) de conversão de forma de dados (Mapper); `source_count` 2 → 3
- `wiki/concepts/hexagonal-architecture.md` — frase no componente Adapter apontando o mapper como peça interna de um adapter de persistência; `source_count` 2 → 3
- `wiki/concepts/ddd.md` — nova seção "Value Object Precisa Ser Desembrulhado na Borda" ligando mapper ao desembrulho de Value Objects na conversão para persistência; `source_count` 2 → 3
- `wiki/sources/presenters.md` — nota de atualização cruzando Presenter (caso HTTP) com Mapper (caso genérico/persistência) como a mesma solução em camadas diferentes
- `wiki/index.md` — nova linha em Sources; nova linha em Concepts (seção "Padrões e Design")

**Notas:** Fonte prática e específica (um único exemplo de código: `Notification` + Prisma), mas o conceito generaliza bem — cria uma página nova (`mapper-pattern`) que várias páginas já existentes tangenciavam sem nomear explicitamente: [[wiki/concepts/repository-pattern]] já citava "Data Mapper" como padrão de persistência (Prisma, Doctrine) mas sem descrever a mecânica da conversão; [[wiki/sources/presenters]] já descrevia exatamente o mesmo problema (mesma entidade, formato diferente por camada) só que do lado HTTP, sem nomear a solução como "mapper". A distinção mais nova e potencialmente reutilizável: Mapper vs. Adapter — ambos convertem entre formatos incompatíveis, mas Adapter resolve incompatibilidade de **interface/comportamento** e Mapper resolve incompatibilidade de **forma de dados**, uma distinção que não estava formalizada em nenhuma página antes desta ingestão. Sem contradições com o resto do wiki. Open question registrada na fonte: o vídeo não mostra o mapper simétrico (`toDomain`, reconstruindo a entidade com Value Objects a partir da linha crua do banco) — só o sentido `toPrisma`.

---

## [2026-07-10] ingest | Os 8 Tipos de JavaScript

**Fonte:** [[wiki/sources/8-tipos-de-javascript]] — transcrição de vídeo em português (sem necessidade de tradução), limpa e organizada em seções, salva em `raw/8-tipos-de-javascript.md`. Qualidade da transcrição original era baixa (erros de reconhecimento de fala como "true string" para `toString`); texto corrigido por inferência de contexto técnico.

**Skill carregada:** `lang-dynamic` (JavaScript/tipagem dinâmica), seguindo a convenção de tag já usada em [[wiki/sources/5-dicas-performance-javascript]].

**Páginas criadas:**
- `wiki/sources/8-tipos-de-javascript.md`
- `wiki/concepts/tipos-primitivos-javascript.md`

**Páginas atualizadas:**
- `wiki/concepts/pitfalls-de-linguagem.md` — expandida a seção de coerção implícita com o mecanismo detalhado de `typeof null`, `==` vs `===` (com exemplo concreto `null == undefined`), e a distinção parâmetro default (`undefined`) vs. fallback `||` (qualquer falsy); `source_count` 1 → 2
- `wiki/concepts/sistema-de-tipos.md` — nova seção "'Tipagem fraca' é um eixo diferente de estática/dinâmica", distinguindo o eixo já documentado (quando os tipos são checados) do eixo de conversão implícita que esta fonte traz; `source_count` 1 → 2
- `wiki/index.md` — nova linha em Sources; nova linha em Concepts (seção "JavaScript / Node.js Performance")

**Notas:** Fonte didática cobrindo os 8 tipos primitivos de JavaScript (`null`, `undefined`, `boolean`, `number`, `bigint`, `string`, `symbol`, `object`) e duas formas de checagem de tipo (`typeof` vs. `Object.prototype.toString.call()`), com ênfase nas armadilhas de conversão implícita de tipo. Conecta-se com duas páginas já existentes sem sobrepor: [[wiki/concepts/pitfalls-de-linguagem]] já citava `typeof null` e `==` vs `===` como armadilhas gerais de JS, mas sem o mecanismo interno (por que `typeof null` é `"object"`, e como `Object.prototype.toString.call()` é historicamente usado — ex. Underscore — como alternativa mais precisa); [[wiki/concepts/sistema-de-tipos]] descrevia tipagem estática vs. dinâmica como o eixo central de sistemas de tipos, e esta fonte deixa explícito que "tipagem fraca" (o rótulo comum para JS) é um eixo ortogonal — sobre conversão implícita, não sobre quando o erro é pego. Distinção nova e potencialmente reutilizável, não formalizada antes: parâmetros default de função reagem apenas a `undefined`, enquanto expressões com `||` reagem a qualquer valor falsy — confundir os dois é fonte comum de bugs silenciosos (ex.: `bar(0)` se comporta diferente dependendo de qual mecanismo é usado). Sem contradições com o resto do wiki. Open question registrada na fonte: autoria do vídeo não identificada com confiança (transcrição ambígua no trecho de autoapresentação) — nenhuma página de entidade foi criada para evitar atribuição incorreta.

---

## [2026-07-15] ingest | Padrão de Projeto: Adapter (Renato Augusto)

**Fonte:** [[wiki/sources/design-pattern-adapter]] — transcrição de fala corrida em português (sem necessidade de tradução), limpa e organizada em seções, salva em `raw/design-pattern-adapter.md`. Vídeo do Renato Augusto sobre o Adapter Pattern com exemplo prático de um gerador de relatório de vendas em PDF (PHP, DomPDF → TCPDF).

**Skill carregada:** `tech-mentor-backend`, `references/design-patterns.md` (seção Structural, entrada "Adapter") — mesma skill já usada em [[wiki/sources/design-pattern-proxy]] e [[wiki/sources/design-pattern-facade]].

**Páginas criadas:**
- `wiki/sources/design-pattern-adapter.md`

**Páginas atualizadas:**
- `wiki/concepts/adapter-pattern.md` — nova seção "Exemplo: troca de biblioteca sem tocar na regra de negócio" (caso DomPDF/TCPDF); `source_count` 3 → 4
- `wiki/concepts/single-responsibility.md` — novo key source ligando `new` direto numa lib externa dentro de uma classe de negócio a duas razões de mudar (viola SRP); `source_count` 1 → 2
- `wiki/concepts/acoplamento.md` — novo key source: `new` de classe concreta de baixo nível dentro de classe de alto nível como manifestação de acoplamento resolvida pelo Adapter; `source_count` 1 → 2
- `wiki/concepts/abstracao.md` — novo key source: extrair interface própria do domínio entre consumidor e lib externa é o que viabiliza troca de lib sem tocar no consumidor; `source_count` 2 → 3
- `wiki/entities/renato-augusto.md` — nova linha em Key Sources; `source_count` 3 → 4
- `wiki/index.md` — nova linha em Sources

**Notas:** Quarta fonte do Adapter Pattern na wiki (já havia 3 via [[wiki/sources/design-pattern-proxy]], [[sources/sete-padroes-de-design-de-software]] e [[sources/design-pattern-facade]]), mas a primeira com um exemplo de código completo e refatorado ao vivo especificamente para esse padrão — as três fontes anteriores mencionavam Adapter só de passagem ou em contraste com Proxy/Facade. Reforça três conceitos já maduros na wiki sem contradição: [[wiki/concepts/acoplamento]] (o `new` direto como manifestação concreta), [[wiki/concepts/single-responsibility]] (duas razões de mudar) e [[wiki/concepts/abstracao]] (interface como o que permite substituição). Nenhuma página nova de conceito foi necessária — o vídeo é um bom exemplo didático encaixando em taxonomia já estabelecida, não um conceito novo. Open question registrada na fonte: o vídeo argumenta testabilidade mas não escreve o teste unitário de fato; fica em aberto como um fake de `PdfAdapter` seria implementado na prática.

---

## [2026-07-15] ingest | Observabilidade de Ponta a Ponta com OpenTelemetry — Palestra em Amsterdã

**Fonte:** [[wiki/sources/observabilidade-ponta-a-ponta-opentelemetry-ia-amsterdam]] — transcrição de fala corrida em português (sem necessidade de tradução), limpa e organizada em seções, salva em `raw/observabilidade-ponta-a-ponta-opentelemetry-ia-amsterdam.md`. Reapresentação em vídeo de uma palestra dada em Amsterdã pelo autor do canal (ver [[wiki/entities/eric-lenda]]) sobre observabilidade fullstack com OpenTelemetry, unida à sua experiência como especialista em performance de aplicações JavaScript e ao uso de agentes de IA via MCP (Grafana MCP, Context7) para automatizar investigação de incidentes.

**Skill carregada:** `tech-mentor-infra`, `references/observability/opentelemetry-deep.md` e `references/observability-foundations.md` — mesma skill já usada em [[wiki/sources/distributed-tracing]] e [[wiki/sources/observabilidade]].

**Páginas criadas:**
- `wiki/sources/observabilidade-ponta-a-ponta-opentelemetry-ia-amsterdam.md`
- `wiki/concepts/investigacao-de-incidentes-com-ia-e-mcp.md` — novo conceito: correlação automática de métricas/logs/traces por um agente de IA conectado via MCP a backends de observabilidade, transformando investigação manual de semanas em relatório de minutos

**Páginas atualizadas:**
- `wiki/concepts/observabilidade.md` — nova seção sobre o Collector como ponto único de roteamento (erro comum: aplicação enviando direto pro backend, pulando o Collector) e nova seção ligando coleta → correlação automática via IA/MCP; `source_count` 5 → 6
- `wiki/concepts/distributed-tracing.md` — expandida de stub para draft: seção sobre OpenTelemetry como padrão vendor-neutral (contribuições de New Relic/Splunk/Google/Amazon/Grafana/Datadog no mesmo projeto), instrumentação de bibliotecas de baixo nível (não só rotas HTTP) com caso real de ganho de ~50% de performance, e uso por IA para correlação automática; `source_count` 1 → 2
- `wiki/concepts/mcp-server.md` — nova seção "Exemplo de domínio: Grafana MCP para observabilidade"; `source_count` 1 → 2
- `wiki/concepts/model-context-protocol.md` — nova seção "Caso de uso: observabilidade"; `source_count` 3 → 4
- `wiki/concepts/gargalo.md` — novo key source ligando CPU profile/flame graph como técnica prática de identificar gargalo de código; `source_count` 1 → 2
- `wiki/entities/eric-lenda.md` — nova linha em Key sources, bio expandida (especialista em performance JS, palestras em 20+ países); `source_count` 1 → 2
- `wiki/entities/anthropic.md` — novo key source (menção de passagem a erros `503` da API do Claude como exemplo do "novo normal" de sistemas caindo); `source_count` 7 → 8
- `wiki/index.md` — nova linha em Sources; nova linha em Concepts (seção MCP/IA)

**Notas:** Fonte com bastante densidade técnica cobrindo três eixos: (1) arquitetura de OpenTelemetry (Collector como hub de roteamento, os três pilares, instrumentação de libs de baixo nível), reforçando e expandindo [[wiki/concepts/observabilidade]] e [[wiki/concepts/distributed-tracing]] sem contradição — ambas já tinham a stack recomendada (Prometheus/Loki/Tempo/Grafana) mas nenhuma detalhava a arquitetura do Collector como ponto único de roteamento nem o erro comum de pular essa etapa; (2) o processo manual de investigação de performance pré-IA do autor (CPU profile/flame graph, Clinic.js, mirar produção em vez de staging), que ligou a [[wiki/concepts/gargalo]] uma técnica prática já esperada mas não documentada (profiling de CPU); (3) o padrão mais novo da fonte — um agente de IA com acesso via MCP a backends de observabilidade correlacionando telemetria automaticamente para achar causa raiz — que não tinha página própria na wiki, por isso a criação de [[wiki/concepts/investigacao-de-incidentes-com-ia-e-mcp]]. Dois casos de segurança reais foram registrados na fonte (extensão maliciosa do VS Code Marketplace no GitHub, ataque de supply chain no NPM afetando 84+ pacotes incluindo o Codex, e um minerador de Bitcoin rodando via RCE numa aplicação Next.js do próprio autor, contido pelo isolamento do container Kubernetes) mas não geraram páginas de conceito novas nem edições em páginas de segurança existentes — são citados como motivação ("por que observabilidade importa"), não como conteúdo técnico de segurança aprofundado o suficiente para expandir [[wiki/sources/supply-chain-security]] ou similares; ficou registrado apenas na fonte. Open questions registradas na fonte: nome do framework da consultoria de performance do autor não identificado com confiança (transcrição distorcida, "Miture JS"/"mito") — nenhuma entidade nova criada para evitar atribuição incorreta; link do repositório de exemplo multi-serviço citado na palestra não foi capturado na transcrição; CVE da vulnerabilidade Next.js/React do caso do minerador não identificado.

---
