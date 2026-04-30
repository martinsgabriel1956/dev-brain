# Wiki Index

Catálogo de todas as páginas do knowledge graph.

---

## Sources

| Página | Hook |
|---|---|
| [[sources/encoding-hashing-encryption]] | Encoding vs Hashing vs Encryption — representação reversível, hash irreversível, encryption com chave |
| [[sources/overengineering-carol-ate-quinta]] | Over-engineering — KISS, ego-driven development, abstração prematura, conhecimento restrito no time |
| [[sources/por-que-devs-nao-terminam-projetos]] | Psicologia do cemitério de projetos — dopamina, planning fallacy, scope creep, perfeccionismo, MVP e goal gradient effect |
| [[sources/roadmap-dev-senior-2026]] | 5 pilares para sênior em 2026 — pensar antes de codar, entender execução, sistema vs arquivos, produção, IA sem dependência |
| [[sources/trimodal-compensacao-tech]] | Modelo trimodal de compensação em tech — 3 tiers, por que sites de salário erram, equity como diferencial, decisão de empresa > decisão de cargo |
| [[sources/5-principios-programador]] | 5 princípios aprendidos na dor — logs, usuários caóticos, tech debt deliberado, naming, paridade local-prod |
| [[sources/apagao-de-seniors-vibe-coding]] | Vibe coding + apagão de sêniors — detector N+1, property-based testing, memory profiling, segurança e arquitetura no código da IA |
| [[sources/estilo-de-codigo-convencoes]] | 4 regras contraintuitivas — indentação 8 chars, strings de log íntegras, função inversamente proporcional à complexidade, comentários explicam o quê |
| [[sources/como-aprender-um-codebase-novo]] | Método 7 passos para onboarding em codebases novos — docs, uso, exploração intencional, tarefas, pair programming |
| [[sources/listen-notes-one-person-startup]] | Listen Notes — compilação PT-BR da trilogia de Wenbin Fang (raw source) |
| [[sources/listen-notes-boring-tech-one-person-company]] | Listen Notes — stack boring (Django, Postgres, ES, Celery, RabbitMQ), 20 servidores AWS, 1 pessoa |
| [[sources/listen-notes-good-enough-engineering]] | Good Enough Engineering — anti-over-engineering, "existe uma ferramenta pra isso", side project → fulltime |
| [[sources/listen-notes-podcasts-nova-wikipedia]] | Podcasts como nova Wikipédia — 61M episódios, aprendizado por tópico, origem do Listen Notes |
| [[sources/multi-tenancy]] | Multi-tenancy — shared schema vs schema-per-tenant vs DB-per-tenant, RLS, GDPR, migrations |
| [[sources/notification-system]] | Notification System — fan-out write/read, deduplicação Redis, FCM token cleanup, quiet hours |
| [[sources/case-youtube-streaming]] | YouTube — transcodificação paralela, HLS/DASH ABR, CDN imutável, storage Hot/Warm/Cold |
| [[sources/case-whatsapp]] | Chat em tempo real — WebSocket, ACK triplo, Cassandra, presença escalável, S3 upload |
| [[sources/case-url-shortener]] | URL Shortener — Snowflake ID, 301 vs 302, cache hot path, analytics async |
| [[sources/case-uber]] | Ride-sharing — geohash, Redis GEO, matching pipeline, distributed lock, surge pricing |
| [[sources/zero-downtime-deploy]] | Zero-Downtime — Rolling/Blue-Green/Canary + Expand-Contract + Graceful Shutdown checklist |
| [[sources/sre-error-budget-incidents]] | SRE — Incident lifecycle, severidade, papéis IC/TL, post-mortem completo, runbook, Game Day |
| [[sources/observabilidade]] | Observabilidade — três pilares, RED/Prometheus, logs estruturados, alertas, stack recomendada |
| [[sources/sre-sli-slo-sla]] | SRE — SLI/SLO/SLA/Error Budget, burn rate alerting, blameless post-mortem |
| [[sources/service-discovery]] | Service Discovery — client-side vs server-side, K8s DNS, Consul multi-cloud |
| [[sources/service-mesh]] | Service Mesh — sidecar pattern, mTLS/AuthorizationPolicy, canary YAML, fault injection, ambient mesh |
| [[sources/blue-green-canary-rolling]] | Blue/Green, Canary, Rolling — estratégias de deploy com rollback, custo e Expand-Contract |
| [[sources/two-phase-commit]] | 2PC — protocolo, XA transactions, blocking problem, comparativo Saga, quando usar/evitar |
| [[sources/skip-locked-fencing-token]] | SKIP LOCKED — fila no PostgreSQL sem broker; Fencing Token — rejeita lock fantasma pós-TTL |
| [[sources/modelos-de-consistencia]] | Linearizability/Causal/Eventual — espectro, vector clocks, DynamoDB, armadilhas |
| [[sources/3pc]] | 3PC vs 2PC — blocking, split-brain, Raft/Paxos, Saga, Outbox como alternativas |
| [[sources/como-aprender-programacao-3-dicas]] | Aprender programação — tempo variável/capacidade fixa, neuroplasticidade, spaced repetition, postura |
| [[sources/logica-programacao-sem-matematica]] | Lógica sem matemática avançada — decomposição em passos, SRP em métodos, pensamento algorítmico |
| [[sources/9-habitos-programador-junior]] | 9 hábitos de dev júnior — voluntariar, comunicar progresso, escrever, bloquear agenda, pausar |
| [[sources/retry-backoff]] | Retry — backoff exponencial + jitter, thundering herd, idempotência, BullMQ/SQS |
| [[sources/bulkhead]] | Bulkhead pattern — isolamento de pools, circuit breaker, fail fast, Little's Law |
| [[sources/banco-de-dados]] | ACID, índices, transações, read replicas, connection pooling, N+1, PostgreSQL vs NoSQL |
| [[sources/react-tudo-que-voce-precisa-saber]] | Visão geral completa do React — hooks, padrões, estado, performance |
| [[sources/tanstack-query-tudo-que-voce-precisa-saber]] | TanStack Query — server state, cache, mutations, optimistic updates, infinite scroll |
| [[sources/design-first-vs-code-first-referencias]] | Design first vs code first, Design Engineer, fake delay e referências de design |
| [[sources/useeffect-problemas-e-solucoes]] | Três anti-padrões de useEffect: estado derivado, stale closure, race condition em fetch |
| [[sources/desenvolvedor-acima-da-media-10-itens]] | 10 comportamentos que distinguem devs acima da média — negócio, ownership, liderança |
| [[sources/habitos-ruins-de-programador]] | 4 hábitos ruins de programador — dizer sim pra tudo, definição de pronto, testes, commits |
| [[sources/4-habitos-programador-ineficiente]] | 4 Habits That Make You an Inefficient Developer — artigo original do Medium com URL, versão EN traduzida |
| [[sources/comparacao-na-carreira-dev]] | Comparação com colegas no início da carreira — bastidor vs palco, familiaridade vs capacidade |
| [[sources/piramide-de-testes]] | Estratégia de testes em camadas — unitário, integração, E2E e variantes Trophy |
| [[sources/tdd]] | TDD Red/Green/Refactor — ciclo obrigatório, escolas Detroit vs London |
| [[sources/test-doubles]] | Taxonomia de Meszaros — Dummy, Stub, Fake, Spy, Mock e regra Fake > Mock |
| [[sources/bdd]] | BDD com Gherkin/Cucumber — specs executáveis como living documentation |
| [[sources/contract-testing]] | Contract Testing com Pact — consumer-driven contracts e can-i-deploy |
| [[sources/living-documentation]] | Documentação gerada automaticamente de código/testes — nunca desatualizada |
| [[sources/principio-da-inversao-programador]] | Princípio da inversão aplicado a programação — 7 hábitos do pior dev e o que eles revelam |
| [[sources/sistema-operacional-por-baixo-dos-panos]] | Do duplo-clique à tela — processos, threads, escalonador, memória virtual, syscalls, kernel |
| [[sources/cicd-pipeline]] | Pipeline em 7 stages, GitHub Actions de referência, Argo Rollouts, rollback automático |
| [[sources/tres-caracteristicas-melhor-candidato]] | Pixar/Randy Nelson — profundidade, abrangência e comunicação como filtro de contratação |
| [[sources/circuit-breaker]] | Circuit breaker — 3 estados, Opossum Node.js, retry dentro do breaker, métricas |
| [[sources/crdt-colaboracao-tempo-real]] | CRDT vs OT — colaboração em tempo real sem servidor de sequenciamento, Y.js, offline-first |
| [[sources/db-sharding]] | DB Sharding — range/hash/consistent hashing, shard key, cross-shard ops, resharding |
| [[sources/distributed-locks]] | Distributed Locks — Redis NX, Redlock, PostgreSQL advisory lock, SKIP LOCKED, fencing token |
| [[sources/distributed-locks-raft]] | Redlock vs Fencing Token — crítica de Kleppmann, GC pause, clock skew, etcd/Raft |
| [[sources/distributed-tracing]] | Distributed Tracing — OpenTelemetry, spans, traceparent W3C, Jaeger, sampling |
| [[sources/feature-flags]] | Feature Flags — 4 tipos de toggle, rollout gradual, kill switch, Unleash/LaunchDarkly |
| [[sources/finops-cost-aware-architecture]] | FinOps — unit economics, right-sizing, batch vs realtime, egress, storage hierárquico |
| [[sources/fintech-system-design]] | FinTech — ledger dupla entrada, idempotência financeira, antifraude em camadas, conciliação |
| [[sources/graceful-degradation]] | Graceful Degradation — hierarquia de fallbacks, fail-open vs fail-closed, Promise.allSettled |
| [[sources/idempotencia]] | Idempotência — idempotency key, CAS, at-least-once, deduplicação financeira |
| [[sources/load-balancer]] | Load Balancer — L4 vs L7, algoritmos, health check, alta disponibilidade, dois níveis |
| [[sources/mensageria]] | Mensageria — queue vs stream, Kafka/SQS/RabbitMQ, DLQ, outbox pattern, at-least-once |
| [[sources/presence-system]] | Presence System — heartbeat + Redis TTL, multi-node Pub/Sub, typing indicator |
| [[sources/raft-leader-election]] | Raft — eleição de líder, replicação de log, quorum, safety, etcd, log compaction |
| [[sources/rate-limiting]] | Rate Limiting — 4 algoritmos, sliding window counter, Redis Lua, hierarquia de limites |
| [[sources/read-replicas-connection-pooling]] | Read Replicas + PgBouncer — replication lag, read-your-writes, 1000→25 conexões reais |
| [[sources/uuid-primary-key-mysql]] | UUID como PK no MySQL — page splitting, storage, UUIDv7, UUID_TO_BIN swap flag, alternativas |
| [[sources/agentes-core]] | AI Agents — ReAct loop, tool use, Agent SDK Anthropic, single vs multi-agent |
| [[sources/agentes-em-producao]] | Agentes em produção — rate limits, timeouts, circuit breaker, observabilidade, cost control |
| [[sources/agentes-orquestracao]] | Orquestração de agentes — Swarm, handoffs, guardrails, avaliação de fluxos multi-agente |
| [[sources/agent-memory]] | Agent Memory — in-context, external (Redis/pgvector), procedural, episodic, semantic |
| [[sources/ai-gateway-token-economics]] | AI Gateway — token economics, rate limiting por modelo, caching semântico, routing |
| [[sources/ai-llm-security]] | LLM Security — prompt injection, jailbreak, data exfiltration, output validation |
| [[sources/ai-safety-guardrails]] | AI Safety — Constitutional AI, guardrails, refusal tuning, red-teaming |
| [[sources/como-llms-funcionam]] | Como LLMs funcionam — transformer, attention, tokenização, RLHF, temperature |
| [[sources/context-engineering]] | Context Engineering — context window, chunking, compression, RAG vs long context |
| [[sources/evals-sistematicas]] | Evals sistemáticas — métricas de avaliação LLM, LLM-as-judge, benchmarks, datasets |
| [[sources/fine-tuning]] | Fine-tuning — LoRA, QLoRA, PEFT, quando fine-tuning vs RAG vs prompting |
| [[sources/llmops-observabilidade]] | LLMOps — tracing de prompts, Langfuse, cost tracking, latência por modelo |
| [[sources/mcp]] | MCP — Model Context Protocol, tools, resources, prompts, transports |
| [[sources/open-weight-deployment]] | Open Weight — Llama, Mistral, vLLM, quantização, self-hosted vs cloud |
| [[sources/prompt-engineering]] | Prompt Engineering — chain-of-thought, few-shot, system prompts, structured output |
| [[sources/rag-retrieval]] | RAG — chunking, embedding, vector search, reranking, hybrid search |
| [[sources/reasoning-models]] | Reasoning Models — o1/o3, chain-of-thought estendido, quando usar vs modelos base |
| [[sources/structured-outputs-function-calling]] | Structured Outputs — function calling, JSON mode, tool use, Zod validation |
| [[sources/adr]] | ADR — Architecture Decision Record, formato Y-statements, quando criar, lifecycle |
| [[sources/anti-patterns]] | Anti-patterns — Anemic Domain Model, God Class, Distributed Monolith, Shotgun Surgery |
| [[sources/api-contracts-versioning]] | API Contracts — URI versioning, header versioning, Sunset policy, Expand-Contract |
| [[sources/background-jobs]] | Background Jobs — queues, workers, retry, idempotency, dead letter, at-least-once |
| [[sources/clean-architecture]] | Clean Architecture — camadas, dependency rule, use cases, gateways, presenters |
| [[sources/conways-law]] | Conway's Law — estrutura org reflete arquitetura, Team Topologies, Inverse Conway |
| [[sources/ddd-cqrs]] | DDD + CQRS — Command/Query segregation, event sourcing, projeções, sagas |
| [[sources/ddd-strategic]] | DDD Estratégico — Bounded Context, Context Map, Core/Generic/Supporting Domain |
| [[sources/ddd-tactical]] | DDD Tático — Aggregate, Entity, Value Object, Domain Event, Repository, Factory |
| [[sources/dependency-injection]] | Dependency Injection — IoC container, constructor injection, testabilidade |
| [[sources/design-patterns-gof]] | GoF Patterns — Creational, Structural, Behavioral; quando usar cada categoria |
| [[sources/event-driven-architecture]] | EDA — event sourcing, CQRS, choreography vs orchestration, schema evolution |
| [[sources/event-ordering-long-running]] | Event Ordering — particionamento por chave, inbox pattern, long-running processes |
| [[sources/event-versioning]] | Event Versioning — upcasting, weak schema, consumer-driven schema evolution |
| [[sources/graphql]] | GraphQL — schema, resolvers, N+1 com DataLoader, subscriptions, federation |
| [[sources/grpc]] | gRPC — Protobuf, unary/streaming, deadline propagation, load balancing |
| [[sources/hexagonal-architecture]] | Hexagonal — ports & adapters, testabilidade, separação de domínio e infra |
| [[sources/integration-patterns-eip]] | EIP — Pipes & Filters, Message Router, Aggregator, Scatter-Gather, Claim Check |
| [[sources/microsservicos]] | Microsserviços — boundaries, comunicação sync/async, decomposição por domínio |
| [[sources/monolito-modular]] | Monólito Modular — módulos com contratos explícitos, caminho para microsserviços |
| [[sources/kubernetes-core]] | Kubernetes Core — Pod, Deployment, Service, ConfigMap, Secret, RBAC |
| [[sources/k8s-autoscaling]] | K8s Autoscaling — HPA, VPA, KEDA, custom metrics, cluster autoscaler |
| [[sources/k8s-networking]] | K8s Networking — CNI, NetworkPolicy, Ingress, Service types, CoreDNS |
| [[sources/gitops-argocd]] | GitOps + ArgoCD — reconciliation loop, app-of-apps, sync waves, rollback |
| [[sources/terraform]] | Terraform — providers, state, modules, workspaces, Atlantis, drift detection |
| [[sources/platform-engineering-devex]] | Platform Engineering — IDP, golden paths, developer portal, Backstage, DevEx metrics |
| [[sources/postgresql-avancado]] | PostgreSQL Avançado — EXPLAIN ANALYZE, índices parciais/GIN/BRIN, particionamento, vacuuming |
| [[sources/postgresql-extensions]] | PostgreSQL Extensions — pg_vector, TimescaleDB, PostGIS, pg_stat_statements, pg_cron |
| [[sources/redis-avancado]] | Redis Avançado — data structures, Lua scripts, keyspace notifications, Redis Cluster |
| [[sources/mongodb]] | MongoDB — document model, aggregation pipeline, indexes, transactions, Atlas Search |
| [[sources/owasp-top10]] | OWASP Top 10 — injection, broken auth, IDOR, SSRF, security misconfiguration |
| [[sources/oauth2-oidc-jwt]] | OAuth2/OIDC/JWT — flows, access/refresh tokens, PKCE, token revocation |
| [[sources/zero-trust]] | Zero Trust — never trust always verify, mTLS, SPIFFE, microsegmentação |
| [[sources/api-security]] | API Security — rate limiting, input validation, CORS, auth, logging |
| [[sources/autenticacao-segura]] | Autenticação Segura — bcrypt, argon2, MFA, session fixation, credential stuffing |
| [[sources/secrets-management]] | Secrets Management — HashiCorp Vault, AWS Secrets Manager, rotation, dynamic secrets |
| [[sources/threat-modeling]] | Threat Modeling — STRIDE, PASTA, attack trees, DFD, LINDDUN para privacidade |
| [[sources/tls-mtls-vpn]] | TLS/mTLS/VPN — handshake, certificate pinning, ALPN, WireGuard, service mesh mTLS |
| [[sources/rbac-abac-rebac]] | RBAC/ABAC/ReBAC — modelos de autorização, OPA, Casbin, Zanzibar (Google) |
| [[sources/criptografia-fundamentos]] | Criptografia — AES-GCM, RSA, ECDSA, HKDF, envelope encryption, HSM |
| [[sources/browser-security]] | Browser Security — SOP, CORS, CSP strict-dynamic, COEP/COOP, Fetch Metadata |
| [[sources/bug-bounty]] | Bug Bounty — VDP, CVSS v3.1, HackerOne/Bugcrowd, report quality, triage |
| [[sources/cloud-security]] | Cloud Security — OIDC Workload Identity, Permission Boundaries, SCPs, CSPM/Prowler |
| [[sources/compliance-soc2-pci]] | Compliance — SOC 2 Type I vs II, PCI-DSS tokenization, audit logging |
| [[sources/container-hardening]] | Container Hardening — Distroless, rootless, DROP ALL capabilities, Seccomp, PSS |
| [[sources/data-privacy]] | Data Privacy — crypto-shredding, PII in logs, pseudonymization, Privacy by Design |
| [[sources/devsecops-pipeline]] | DevSecOps — SAST (Semgrep), SCA (Snyk), Trivy, DAST (ZAP), Conftest |
| [[sources/federated-identity]] | Federated Identity — SAML vs OIDC, SCIM, Identity Router, home realm discovery |
| [[sources/hipaa-sox]] | HIPAA/SOX — PHI/BAA, Segregation of Duties, S3 Object Lock COMPLIANCE 7 anos |
| [[sources/identidade-avancada]] | Identidade Avançada — Passkeys phishing-resistant, SPIFFE/SPIRE, JIT access |
| [[sources/identity-iam-avancado]] | IAM Avançado — PAM zero standing privilege, Machine Identity X.509, OAuth 2.1 |
| [[sources/incident-response]] | Incident Response — NIST 800-61 phases, blameless post-mortem, SOAR automation |
| [[sources/input-validation-output-encoding]] | Input Validation — Zod at boundary, DOMPurify allowlist, prototype pollution |
| [[sources/kubernetes-security]] | K8s Security — CIS Benchmark, PSS restricted, RBAC no cluster-admin, NetworkPolicy default-deny |
| [[sources/lgpd-gdpr]] | LGPD/GDPR — data mapping, lawful basis, 72h breach notification, DPA |
| [[sources/mobile-security]] | Mobile Security — certificate pinning backup pin, Keychain/Keystore, Frida |
| [[sources/passkeys-webauthn]] | Passkeys/WebAuthn — RP ID binding anti-phishing, Secure Enclave, counter clone detection |
| [[sources/pentest-redteam]] | Pentest/Red Team — MITRE ATT&CK, Red vs Pentest vs Purple Team, PoC in reports |
| [[sources/policy-as-code]] | Policy as Code — OPA/Rego, Kyverno YAML, Conftest for Terraform |
| [[sources/post-quantum-crypto]] | Post-Quantum Crypto — Harvest-Now-Decrypt-Later, Kyber/ML-KEM, Dilithium/ML-DSA, hybrid |
| [[sources/runtime-security]] | Runtime Security — Falco eBPF rules, Falco Sidekick routing, automated pod isolation |
| [[sources/secret-scanning]] | Secret Scanning — Gitleaks pre-commit, TruffleHog --only-verified, GHAS, revoke immediately |
| [[sources/secure-design-patterns]] | Secure Design — Defense in Depth (independent layers), Fail Secure, Assume Breach |
| [[sources/supply-chain-security]] | Supply Chain Security — SBOM para CVEs, Sigstore keyless signing, SLSA Level 2 |
| [[sources/kafka]] | Kafka — partições, consumer groups, retenção, exactly-once, compaction, Schema Registry |
| [[sources/rabbitmq]] | RabbitMQ — exchanges (Direct/Fanout/Topic), DLX, Quorum Queues, consumer ACK |
| [[sources/nats-jetstream]] | NATS JetStream — Core vs JetStream, KV Store, request-reply, pull consumers |
| [[sources/sqs-sns]] | SQS/SNS — Visibility Timeout, SNS fanout, SQS FIFO deduplication, DLQ |
| [[sources/saga-pattern]] | Saga Pattern — Choreography vs Orchestration, compensações, Temporal, rollback |
| [[sources/outbox-pattern]] | Outbox Pattern — dual-write atomicity, CDC+Debezium, Inbox Pattern, exactly-once |
| [[sources/dlq-event-patterns]] | DLQ & Event Patterns — at-least-once+idempotence, Tolerant Reader, Upcasting |
| [[sources/schema-registry]] | Schema Registry — Confluent, Avro schema ID, BACKWARD compatibility, schema evolution |
| [[sources/architecture-fitness-functions]] | Fitness Functions — ArchUnit, Deptrac, k6 thresholds, evolutionary architecture gates |
| [[sources/bancos-especializados]] | Bancos Especializados — Neo4j, InfluxDB/TimescaleDB, pgvector/Qdrant, DuckDB, CockroachDB |
| [[sources/c4-model]] | C4 Model — 4 níveis, Structurizr DSL, diagrams-as-code, ADR integration |
| [[sources/cdc-debezium]] | CDC/Debezium — WAL, replication slot, before/after state, Schema Registry integration |
| [[sources/cell-based-architecture]] | Cell-Based Architecture — blast radius containment, Amazon/Slack pattern, cell router |
| [[sources/checklist-solutions-architect]] | Checklist Solutions Architect — 24 domínios para entrevistas SA |
| [[sources/dynamodb]] | DynamoDB — Single-Table Design, access patterns first, GSI, DynamoDB Streams |
| [[sources/elasticsearch-opensearch]] | Elasticsearch/OpenSearch — BM25, mapping schema, CDC sync, relevance tuning |
| [[sources/evolutionary-architecture]] | Evolutionary Architecture — Big bang anti-pattern, Strangler Fig, Feature Flags, fitness functions |
| [[sources/expand-contract]] | Expand-Contract — 3 fases (Expand/Migrate/Contract), zero-downtime column rename |
| [[sources/fase-1-fundamentos-infraestrutura]] | Fundamentos Infra — DNS, LB, CDN, cache, latency numbers, back-of-envelope |
| [[sources/flame-graph-profiling]] | Flame Graph Profiling — CPU profiling, USE/RED methods, Four Golden Signals, pprof/Clinic.js |
| [[sources/fraud-abuse]] | Fraud & Abuse — FingerprintJS, velocity checks em Redis, fraud scoring 0-100 |
| [[sources/go-core]] | Go Core — goroutines (CSP), channels, Context propagation, implicit interfaces, error wrapping |
| [[sources/http-tcp-quic]] | HTTP/TCP/QUIC — HTTP/2 HoL blocking, HTTP/3/QUIC elimina HoL, 0-RTT replay risk |
| [[sources/micro-kernel]] | Micro-Kernel — Core + plugins, registry, plugin contract versioning, Eclipse/VS Code |
| [[sources/migrations-schema-evolution]] | Migrations — ADD COLUMN NOT NULL lock danger, Testcontainers in CI, never edit applied |
| [[sources/otel-collector-sampling]] | OTel Collector — tail vs head sampling, K8s Operator auto-instrumentation, Pyroscope/eBPF |
| [[sources/otel-sdk]] | OTel SDK — init before imports, auto vs manual instrumentation, semantic attributes |
| [[sources/pagination]] | Pagination — offset O(n) degradation, keyset O(log n), cursor opaque em base64 |
| [[sources/performance-methods]] | Performance Methods — p95/p99 over p50, k6 thresholds as SLOs, USE Method discipline |
| [[sources/presenters]] | Presenters — UseCase → OutputData → Presenter → ViewModel, mesmo UseCase múltiplas UIs |
| [[sources/reactive-architecture]] | Reactive Architecture — 4 pilares Reactive Manifesto, backpressure, RxJS bufferTime |
| [[sources/rest-openapi]] | REST/OpenAPI — API-First mock server, 400/422 distinction, Sunset Policy RFC 8594 |
| [[sources/rfc]] | RFC — processo RFC vs ADR, o que merece RFC (> 1 sprint para reverter) |
| [[sources/serialization-protocols]] | Serialization — Protobuf field numbers backward compat, MessagePack drop-in, Avro+Registry |
| [[sources/sessions]] | Sessions — JWT irrevogável vs Redis sessions, SPIFFE sem shared secrets |
| [[sources/solid]] | SOLID — SRP (actor-based), DIP (testabilidade), OCP (polymorphism over if-else) |
| [[sources/space-based-architecture]] | Space-Based Architecture — Processing Units + Data Grid (Hazelcast), consistência eventual |
| [[sources/temporal]] | Temporal — Durable Execution, event history replay, Activities para I/O, Signals |
| [[sources/tolerant-reader]] | Tolerant Reader — ignorar campos desconhecidos, defaults, Protobuf/Avro guarantee |
| [[sources/twelve-factor-app]] | Twelve-Factor App — config em env vars, stateless processes, graceful shutdown |
| [[sources/two-sum-explicacao]] | Two Sum — hash map complemento O(n), lógica produtor/consumidor, Python vs TypeScript |
| [[sources/typescript-avancado]] | TypeScript Avançado — generics/infer, conditional types, template literal, satisfies, NoInfer |
| [[sources/wardley-maps]] | Wardley Maps — eixo Evolução (Genesis→Commodity), value chain, build vs buy strategy |
| [[sources/webhook]] | Webhooks — HMAC-SHA256, replay attack prevention, deduplicação X-Webhook-Id, fanout |
| [[sources/websocket-sse-realtime]] | WebSocket/SSE — SSE Last-Event-ID, cluster Redis Pub/Sub, heartbeat zumbi detection |
| [[sources/api-gateway-bff]] | API Gateway & BFF — north-south, BFF por cliente, rate limiting por token, vs service mesh |
| [[sources/async-io-memory-management]] | Async I/O — Node.js event loop/libuv, io_uring, goroutines Go, Node heap leaks, JVM GC |
| [[sources/conceitos-que-ninguem-ensina]] | Back Pressure, Thundering Herd, Temporal Coupling, Complexidade Acidental vs Essencial (Fred Brooks) |
| [[sources/divida-cognitiva-ai-brainfry]] | Dívida Cognitiva e AI Brainfry — supervisão de IA +14% esforço mental, Vibe Coding paralisia, Margaret Storey |
| [[sources/ia-salario-ou-carga-de-trabalho]] | IA multiplica salário (compute como 4º pilar) ou carga de trabalho (ActiveTrack +104% e-mails) — depende de quem controla |
| [[sources/mobile-platform-engineering]] | Platform Engineering Mobile — Shared SDK, Adapter Pattern analytics, Native Modules RN, monorepo Turborepo |
| [[sources/mobile-animacoes-performaticas]] | Animações Performáticas — Reanimated 3 worklets UI thread, Compose animate*AsState, Flutter implicit/explicit |
| [[sources/mobile-armazenamento-local]] | Armazenamento Local — MMKV vs AsyncStorage, SQLite/Room, Keychain/Keystore, SQLCipher para PII |
| [[sources/mobile-baseline-profiles]] | Baseline Profiles — ART pré-compilação, cold start -30-40%, Macrobenchmark, CI integration |
| [[sources/mobile-biometria]] | Biometria — Face ID/Touch ID, BiometricPrompt, Secure Enclave, Keystore, fallback PIN obrigatório |
| [[sources/mobile-chamadas-http]] | Chamadas HTTP — TanStack Query, Retrofit+OkHttp interceptors, skeleton/shimmer, timeout obrigatório |
| [[sources/mobile-cicd]] | CI/CD Mobile — Fastlane match, EAS Build, GitHub Actions, rollout gradual Play/TestFlight |
| [[sources/mobile-cross-platform-decision]] | Cross-Platform — Flutter (pixel-perfect), RN (JSI), KMP (shared logic), Nativo (hardware intensivo) |
| [[sources/mobile-deep-links]] | Deep Links — Universal Links (iOS), App Links (Android), deferred deep links, evitar custom schemes |
| [[sources/mobile-design-system]] | Design System — tokens como fonte única, Figma Variables, Style Dictionary, primitivos agnósticos |
| [[sources/mobile-feature-flags]] | Feature Flags — deploy≠release, Firebase Remote Config, LaunchDarkly, cache local obrigatório |
| [[sources/mobile-kmp]] | KMP — shared domain/data, expect/actual, Ktor networking, SQLDelight, UI nativa por plataforma |
| [[sources/mobile-layouts-responsivos]] | Layouts — SafeArea obrigatório, WindowSizeClass, Flexbox RN (column default), LayoutBuilder Flutter |
| [[sources/mobile-metricas-criticas]] | Métricas — Cold Start < 2s, FPS ≥ 60, ANR < 0.1%, crash-free > 99.5%, TTI vs startup |
| [[sources/mobile-monetizacao]] | Monetização — StoreKit 2, Play Billing 6, RevenueCat, validação server-side obrigatória |
| [[sources/mobile-monitoramento]] | Monitoramento — Crashlytics (symbolication), Sentry (session replay), Firebase Performance, alertas |
| [[sources/mobile-navegacao]] | Navegação — Tab→Stack pattern, React Navigation, Navigation Compose tipado, GoRouter Flutter |
| [[sources/mobile-offline-first-basico]] | Offline-First Básico — cache-first, stale-while-revalidate, badge offline, fila de operações |
| [[sources/mobile-offline-first-avancado]] | Offline-First Avançado — delta sync watermark, Last-Write-Wins, CRDT, idempotency key |
| [[sources/mobile-on-device-ai]] | On-Device AI — Core ML Neural Engine, TFLite INT8, MediaPipe Tasks, Gemini Nano Pixel/S24+ |
| [[sources/mobile-performance-listas]] | Performance Listas — FlashList vs FlatList, LazyColumn, ListView.builder itemExtent, sem ScrollView+map |
| [[sources/mobile-permissoes]] | Permissões Runtime — pedir no contexto, Privacy Manifest iOS, shouldShowRationale Android |
| [[sources/mobile-profiling]] | Profiling — Perfetto, Instruments Time Profiler, Android Studio Profiler, Hermes Profiler RN |
| [[sources/mobile-publicacao-aso]] | Publicação e ASO — título>keywords, preview video +20% conversão, rating no momento certo |
| [[sources/mobile-push-notifications]] | Push Notifications — FCM/APNs, token refresh listener, cold/warm start handling, quiet hours |
| [[sources/mobile-seguranca]] | Segurança — Keychain/Keystore, certificate pinning backup pin, Frida defense in depth, zero hardcoded keys |
| [[sources/mobile-state-management-global]] | State Global — Zustand (RN), Redux Toolkit, Riverpod (Flutter), Bloc, server state NÃO vai aqui |
| [[sources/mobile-state-management-local]] | State Local — useState/useReducer (RN), ViewModel+StateFlow (Android), StatefulWidget (Flutter) |
| [[sources/mobile-testes]] | Testes — Maestro YAML (E2E), Detox, XCUITest, Espresso, integration_test Flutter, ViewModel unit |
| [[sources/clean-architecture-ia-custo-real]] | Clean Architecture na Era da IA — 18 arquivos por feature, custo em tokens, YAGNI escalado, DDD estratégico vivo |
| [[sources/navigation-paradox-2026]] | Navigation Paradox (2026) — agente perde 1/4 dos arquivos críticos em G3; ferramenta de grafos ignorada 58% |
| [[sources/addy-osmani-80-problem-agentic-coding]] | Addy Osmani — abstraction bloat, comprehension debt, assumption propagation em codebases agentic |
| [[sources/super-productivity-ai-architecture-guide]] | Abstraction Illusion — IA torna padrões acessíveis sem torná-los apropriados; constraints-first workflow |
| [[sources/go-is-not-java]] | Go is not Java — princípios de Clean Architecture sem cerimônia: interfaces implícitas, DI via construtor |
| [[sources/go-fundamentos]] | Go Fundamentos — zero values, slices/maps/structs, iota, controle de fluxo, defer |
| [[sources/go-concorrencia]] | Go Concorrência — CSP, goroutines, channels buffered/unbuffered, context, sync, race detector |
| [[sources/go-arquitetura]] | Go Arquitetura — Clean Architecture, repository pattern, DI via construtor, functional options |
| [[sources/go-avancado]] | Go Avançado — generics, reflection, cgo, WASM, memory model, GC tuning |
| [[sources/go-ecossistema]] | Go Ecossistema — Chi, sqlc, sqlx, GORM, golangci-lint, modules |
| [[sources/go-oop-composicao]] | Go OOP — composição via embedding, interfaces implícitas, value/pointer receivers |
| [[sources/go-producao]] | Go Produção — graceful shutdown, health checks, Prometheus, OpenTelemetry, pprof, Docker multi-stage |
| [[sources/go-stdlib]] | Go Stdlib — net/http, encoding/json, database/sql, table-driven tests, log/slog |
| [[sources/acoplamento-abstracao-estado]] | Acoplamento, Abstração e Estado — lentes de design: o que cada termo revela no código |
| [[sources/diferenciais-portfolio-backend-junior]] | Portfólio Backend Júnior — 7 diferenciais reais vs o que NÃO focar na primeira vaga |

---

## Concepts

### Go

| Página | Hook |
|---|---|
| [[concepts/go-fundamentos]] | Tipos primitivos, zero values, slices, maps, structs, iota, defer |
| [[concepts/go-concorrencia]] | CSP, goroutines, channels, context.Context, sync, padrões de concorrência |
| [[concepts/go-arquitetura]] | Clean Architecture, repository pattern, DI via construtor, functional options |
| [[concepts/go-avancado]] | Generics, reflection, cgo, WASM, memory model, GC tuning |
| [[concepts/go-ecossistema]] | Chi, sqlc, sqlx, GORM, golangci-lint, Go modules |
| [[concepts/go-oop-composicao]] | Embedding, interfaces implícitas, duck typing, value/pointer receivers |
| [[concepts/go-producao]] | Graceful shutdown, health checks, Prometheus, OpenTelemetry, pprof, Docker multi-stage |
| [[concepts/go-stdlib]] | net/http, encoding/json, database/sql, table-driven tests, log/slog |

### Mobile

| Página | Hook |
|---|---|
| [[concepts/shared-sdk]] | Shared SDK mobile — Auth, Networking, Analytics, Storage, FeatureFlags, Push como packages compartilhados |
| [[concepts/adapter-pattern-analytics]] | Adapter Pattern analytics — AnalyticsService registra providers, troca sem mudar call sites |
| [[concepts/native-module]] | Native Module RN — ponte JS↔Kotlin/Swift, criação manual quando não existe lib matura |
| [[concepts/monorepo-mobile]] | Monorepo mobile — Turborepo + pnpm workspaces para múltiplos apps com SDK compartilhado |
| [[concepts/mobile-animacoes-performaticas]] | Animações performáticas — Reanimated 3 worklets, Compose animate*AsState, Flutter implicit/explicit |
| [[concepts/mobile-armazenamento-local]] | Armazenamento local — MMKV, SQLite, Keychain/Keystore, hierarquia de decisão por tipo de dado |
| [[concepts/mobile-baseline-profiles]] | Baseline Profiles Android — pré-compilação ART, cold start -30-40%, geração com Macrobenchmark |
| [[concepts/mobile-biometria]] | Biometria — Face ID/Touch ID/Fingerprint, BiometricPrompt, Secure Enclave, fallback PIN |
| [[concepts/mobile-chamadas-http]] | Chamadas HTTP — TanStack Query, Retrofit+OkHttp, skeleton/shimmer, offline UX |
| [[concepts/mobile-cicd]] | CI/CD Mobile — Fastlane match, EAS Build, GitHub Actions macOS, rollout gradual |
| [[concepts/mobile-cross-platform-decision]] | Cross-Platform Decision — Flutter vs RN vs KMP vs Nativo, framework de decisão por critério |
| [[concepts/mobile-deep-links]] | Deep Links — Universal Links, App Links, assetlinks.json, deferred deep links |
| [[concepts/mobile-design-system]] | Design System — tokens, Figma Variables, Style Dictionary, componentes primitivos e compostos |
| [[concepts/mobile-feature-flags]] | Feature Flags — Firebase Remote Config, LaunchDarkly, A/B testing, cache local |
| [[concepts/mobile-kmp]] | KMP — expect/actual, Ktor, SQLDelight, shared domain+data, UI nativa por plataforma |
| [[concepts/mobile-layouts-responsivos]] | Layouts Responsivos — SafeArea obrigatório, WindowSizeClass, Flexbox RN, LayoutBuilder Flutter |
| [[concepts/mobile-metricas-criticas]] | Métricas Críticas — Cold Start, FPS, ANR, crash-free rate, TTI, testar em Moto G |
| [[concepts/mobile-monetizacao]] | Monetização — StoreKit 2, Play Billing 6, RevenueCat, receipt validation server-side |
| [[concepts/mobile-monitoramento]] | Monitoramento — Crashlytics, Sentry session replay, Firebase Performance, alertas críticos |
| [[concepts/mobile-navegacao]] | Navegação — Tab→Stack pattern, React Navigation tipado, Navigation Compose, GoRouter |
| [[concepts/mobile-offline-first-basico]] | Offline-First Básico — cache-first, stale-while-revalidate, badge offline |
| [[concepts/mobile-offline-first-avancado]] | Offline-First Avançado — delta sync, Last-Write-Wins, CRDT, idempotency key na fila |
| [[concepts/mobile-on-device-ai]] | On-Device AI — Core ML Neural Engine, TFLite INT8, MediaPipe, Gemini Nano |
| [[concepts/mobile-performance-listas]] | Performance Listas — FlashList, LazyColumn, ListView.builder, anti-pattern ScrollView+map |
| [[concepts/mobile-permissoes]] | Permissões — pedir no contexto de uso, Privacy Manifest iOS, rationale Android |
| [[concepts/mobile-profiling]] | Profiling — Perfetto, Xcode Instruments, Android Studio Profiler, Hermes Profiler |
| [[concepts/mobile-publicacao-aso]] | Publicação e ASO — título como keyword, preview video, rating no momento certo |
| [[concepts/mobile-push-notifications]] | Push Notifications — FCM/APNs, token refresh, cold/warm start handling, quiet hours |
| [[concepts/mobile-seguranca]] | Segurança Mobile — Keychain/Keystore, certificate pinning, Frida defense in depth |
| [[concepts/mobile-state-management-global]] | State Global — Zustand, Redux Toolkit, Riverpod, Bloc; server state fora do global |
| [[concepts/mobile-state-management-local]] | State Local — useState/useReducer, ViewModel+StateFlow, StatefulWidget Flutter |
| [[concepts/mobile-testes]] | Testes — Maestro YAML, Detox, XCUITest, Espresso, integration_test, pirâmide mobile |

### React / Frontend

| Página | Hook |
|---|---|
| [[concepts/jsx]] | Sintaxe JSX — compilação, diferenças do HTML, expressões |
| [[concepts/useState]] | Estado local — callback form, lazy init, quando migrar para useReducer |
| [[concepts/useEffect]] | Efeitos — dependências, cleanup, quando NÃO usar |
| [[concepts/useRef]] | Refs — acesso ao DOM, valores sem re-render |
| [[concepts/useReducer]] | Estado complexo com múltiplas ações relacionadas |
| [[concepts/useMemo]] | Memoização de valores — quando usar e quando evitar |
| [[concepts/useCallback]] | Memoização de funções — referência estável para props |
| [[concepts/context-api]] | Estado compartilhado sem prop drilling — baixa frequência de mudança |
| [[concepts/custom-hooks]] | Extração de lógica stateful reutilizável |
| [[concepts/error-boundary]] | Captura de erros na árvore de componentes |
| [[concepts/compound-components]] | Subcomponentes com estado compartilhado implícito via Context |
| [[concepts/container-presenter]] | Separação de lógica e apresentação para testabilidade |
| [[concepts/concurrent-mode]] | React 18+ — useTransition, useDeferredValue, React Compiler |
| [[concepts/feature-sliced-architecture]] | Organização por feature — estrutura escalável de projetos React |
| [[concepts/tanstack-query]] | Server state, cache, fetch — modelo mental e hooks principais |
| [[concepts/server-state]] | Dados do servidor vs client state — separação de responsabilidades |
| [[concepts/query-key]] | Endereço do cache — fábrica de keys e invalidação granular |
| [[concepts/optimistic-updates]] | Atualiza UI antes da resposta do servidor com rollback em erro |
| [[concepts/infinite-query]] | Paginação por cursor e scroll infinito com useInfiniteQuery |
| [[concepts/swr]] | Alternativa leve ao TanStack Query — comparativo e quando usar |
| [[concepts/design-first]] | Layout no Figma antes do código — funciona em times com designers dedicados |
| [[concepts/code-first]] | Começa codando com component libraries — risco de "Frankenstein" sem visão de design |
| [[concepts/design-engineer]] | Perfil que experimenta layout diretamente no código com repertório de design |
| [[concepts/fake-delay]] | Delay mínimo intencional (300ms) para tornar feedback visual perceptível |
| [[concepts/derived-state]] | Valores calculados a partir de estado/props — nunca em useState + useEffect |
| [[concepts/stale-closure]] | Closure que captura variável de renderização antiga — bug em useEffect + timers |
| [[concepts/race-condition]] | Requests que completam fora de ordem — AbortController ou TanStack Query |

### Hábitos & Produtividade

| Página | Hook |
|---|---|
| [[concepts/voluntariar-para-desconhecido]] | Pegar tarefas fora da zona de conforto — hábito que não tem data de validade |
| [[concepts/comunicar-progresso]] | Update contínuo para envolvidos — elimina bomba de desapontamento no deadline |
| [[concepts/escrever-para-aprender]] | Escrever enquanto aprende organiza pensamento linearmente e melhora comunicação |
| [[concepts/bloqueio-de-agenda]] | Reservar horários para tarefas importantes antes que outros preencham o calendário |
| [[concepts/pausa-estrategica]] | Quando travado, pausar e recomeçar do zero — base melhor, destrava mais rápido |
| [[concepts/fazer-por-voce]] | Meta-hábito: crescer por si mesmo, não para impressionar chefe ou empresa |
| [[concepts/pair-programming]] | Parear para kickoff de tarefas desconhecidas — requisitos, solução, convenções |
| [[concepts/pomodoro]] | 30min de foco + recap — detecta travamento e serve como trigger para habit stacking |
| [[concepts/documentar-conquistas]] | Bullet points diários de vitórias — agrega para avaliações de performance |
| [[concepts/sem-balas-de-prata]] | Não existe arquitetura, framework ou linguagem universal — opinião precisa de argumento |
| [[concepts/decomposicao-de-problemas]] | Dividir problema em passos + SRP em métodos — núcleo da lógica de programação |

### Carreira & Portfólio

| Página | Hook |
|---|---|
| [[concepts/compute-como-compensacao]] | Compute como 4º pilar da compensação — tokens, budget de inference, $100k = 20% do salário |
| [[concepts/ia-como-chicote-de-produtividade]] | IA obrigada sem método — transferência de responsabilidade, caso Amazon, ActiveTrack +104% e-mails |
| [[concepts/tech-debt-como-ferramenta]] | Tech debt deliberado — Quadrante de Fowler, quando tomar, quando pagar, a regra do "se" |
| [[concepts/naming]] | Naming — anti-padrões (doStuff, data2, manager), por que é difícil, regra dos 5 minutos |
| [[concepts/paridade-local-producao]] | Paridade local-prod — por que o laptop mente, Docker, staging, Twelve-Factor fator X |
| [[concepts/portfolio-backend-junior]] | Diferenciais reais para primeira vaga: Docker, testes, SQL, Swagger, error handling, observabilidade |
| [[concepts/testes-integracao-banco-real]] | Testes end-to-end com banco real — não mockar banco; banco dedicado para testes |
| [[concepts/docker-portfolio]] | Docker + Docker Compose + multi-stage build como diferencial de portfólio |
| [[concepts/documentacao-api-swagger]] | Swagger + Scalar — API reference automática; 1 em 10 devs faz isso |
| [[concepts/error-handling-estruturado]] | Classes de erro + HTTP codes corretos + handler global |
| [[concepts/sql-alem-do-basico]] | JOINs, agregações, subqueries, window functions — sair do CRUD |

### Software Design

| Página | Hook |
|---|---|
| [[concepts/lentes-de-codigo]] | Vocabulário técnico como lentes — acoplamento/abstração/estado como ferramentas de percepção |
| [[concepts/acoplamento]] | Acoplamento — dependência entre partes; alto = código congela; baixo = mudanças locais |
| [[concepts/abstracao]] | Abstração — esconder detalhes atrás de contratos; trocar implementação sem mudar consumidor |
| [[concepts/estado-compartilhado]] | Estado Compartilhado — múltiplas funções mutando o mesmo objeto = debugging impossível |
| [[concepts/imutabilidade]] | Imutabilidade — criar novo estado em vez de mutar; rastreabilidade total |
| [[concepts/efeito-colateral]] | Efeito Colateral — o que uma função muda além do que retorna; isolar nos limites externos |
| [[concepts/coesao]] | Coesão — responsabilidades relacionadas dentro de uma unidade; alta coesão + baixo acoplamento |
| [[concepts/single-responsibility]] | SRP — uma única razão para mudar; o critério é o ator, não o número de linhas |

### System Design Cases

| Página | Hook |
|---|---|
| [[concepts/video-transcoding]] | FFmpeg + SQS + workers paralelos por segmento — 2h de vídeo em ~10min |
| [[concepts/adaptive-bitrate-streaming]] | HLS/DASH — segmentos de 6s, player muda qualidade por bandwidth, buffer 30s |
| [[concepts/cdn-strategy]] | TTL 365 dias para imutáveis, TTL 60s para manifesto, pré-aquecimento anti-viral |
| [[concepts/storage-tiering]] | Hot/Warm/Cold — 90% volume em Glacier, <5% do tráfego, 80% de economia |
| [[concepts/websocket-vs-polling]] | WebSocket full-duplex vs polling vs Long Polling vs SSE — quando cada um |
| [[concepts/chat-distribuido]] | Redis Pub-Sub para 1:1, Kafka para grupos — roteamento cross-server |
| [[concepts/ack-triplo]] | Enviado ✓ / Entregue ✓✓ / Lido ✓✓ azul — idempotência via client_message_id |
| [[concepts/presenca-online]] | Heartbeat + Redis TTL — propagar só para contatos ativos na tela |
| [[concepts/cassandra-schema]] | Partition key = padrão de acesso — conversation_id + Snowflake ID DESC |
| [[concepts/media-upload-pattern]] | Presigned URL → upload direto S3, servidor fora do caminho de bytes |
| [[concepts/snowflake-id]] | ID distribuído sem coordenação central — timestamp + worker_id + sequence → Base62 |
| [[concepts/http-redirect-301-302]] | 301 cacheia no browser (sem analytics) vs 302 passa pelo servidor (analytics preciso) |
| [[concepts/cache-hot-path]] | Cache em camadas aproveitando power law — hot cache local + Redis resolve 95% |
| [[concepts/analytics-pipeline]] | Kafka async + ClickHouse — analytics fora do caminho crítico com Redis INCR |
| [[concepts/geohash]] | Indexação geoespacial por prefixo de string — busca por raio sem calcular distância para 5M |
| [[concepts/redis-geo]] | GEOADD/GEOSEARCH — 1.25M writes/s, dados voláteis, 350MB para 5M motoristas |
| [[concepts/ride-matching-pipeline]] | GEOSEARCH → ETA real → ranking → lock → oferta → fallback com expansão de raio |
| [[concepts/distributed-lock]] | Redis SET NX EX — exclusão mútua atômica sem coordenação pesada |
| [[concepts/surge-pricing]] | Kafka stream + Redis cache — ratio demand/supply por geohash, desacoplado do match |
| [[concepts/realtime-tracking]] | WebSocket + Kafka — motorista → passageiro desacoplado via tópico por corrida |
| [[concepts/multi-tenancy]] | Shared Schema vs Schema-per-Tenant vs DB-per-Tenant — custo, isolamento, GDPR, noisy neighbor |
| [[concepts/tenant-context]] | AsyncLocalStorage propaga tenant_id pela stack sem prop drilling — resolve na borda |
| [[concepts/notification-system]] | Fan-out, deduplicação Redis NX, FCM token cleanup, quiet hours, bounce handling |
| [[concepts/fanout-pattern]] | Write (< 1000 destinatários) vs Read (viral) vs Híbrido — trade-off write amplification |
| [[concepts/estimativas-back-of-envelope]] | Cálculos rápidos de escala — valida escolha de tecnologia com números |

### SRE & Observabilidade

| Página | Hook |
|---|---|
| [[concepts/observabilidade]] | Métricas/Traces/Logs — três pilares, RED method, logs estruturados, alertas essenciais |
| [[concepts/red-method]] | Rate + Errors + Duration — instrumentação mínima para SLOs rastreáveis |
| [[concepts/sre]] | Disciplina de confiabilidade como engenharia — SLI, SLO, SLA, Error Budget |
| [[concepts/sli]] | Métrica concreta de qualidade — disponibilidade, latência, freshness |
| [[concepts/slo]] | Meta interna de confiabilidade — fonte da verdade operacional |
| [[concepts/sla]] | Contrato externo com penalidade — derivado do SLO com margem de segurança |
| [[concepts/error-budget]] | Folga operacional — governa velocidade vs. estabilidade com burn rate alerting |
| [[concepts/error-budget-policy]] | Regras por nível de budget — quando deploiar, quando parar |
| [[concepts/blameless-post-mortem]] | Análise de incidente focada no sistema, não na pessoa |
| [[concepts/incident-lifecycle]] | Fluxo de resposta — alerta → acknowledge → severidade → IC → mitigar → post-mortem |
| [[concepts/incident-severity]] | SEV-1 a SEV-4 — critério, tempo de resposta e escalonamento |
| [[concepts/incident-roles]] | IC coordena, TL investiga, Comunicador atualiza, Escriba documenta — nunca misturar |
| [[concepts/runbook]] | Documento executável sob stress — diagnóstico rápido + árvore de decisão + comandos |
| [[concepts/game-day]] | Simulação planejada de falha em staging — valida runbooks e SLOs antes do incidente real |

### Deploy & CI/CD

| Página | Hook |
|---|---|
| [[concepts/deploy-strategies]] | Comparativo Blue/Green vs Canary vs Rolling — rollback, custo, tráfego misto |
| [[concepts/blue-green-deploy]] | Swap atômico no load balancer — rollback em segundos, custo 2x |
| [[concepts/canary-release]] | Exposição gradual com análise automática de métricas — requer Prometheus |
| [[concepts/rolling-update]] | Pod a pod, nativo no Kubernetes, sem custo extra — rollback lento |
| [[concepts/expand-contract]] | DB migration em 3 fases — compatível com v1 e v2 simultâneas |
| [[concepts/zero-downtime-deploy]] | Deploy sem interrupção — pré-requisito: Expand-Contract |
| [[concepts/feature-flags]] | Ativa/desativa feature sem deploy — desacopla deploy de release |
| [[concepts/ci-cd]] | Disciplina de entrega contínua — CI vs CD vs Continuous Deployment e 6 princípios |
| [[concepts/pipeline-de-ci]] | 7 stages ordenados por velocidade — fail fast, artefato único, gates de merge |
| [[concepts/github-actions]] | CI/CD no GitHub — needs, services, Docker cache, environments com aprovação |
| [[concepts/argo-rollouts]] | Progressive delivery com rollback automático via métricas Prometheus |

### Service Mesh

| Página | Hook |
|---|---|
| [[concepts/service-discovery]] | Client-side vs server-side vs DNS K8s vs Consul — como serviços se encontram em ambientes dinâmicos |
| [[concepts/service-mesh]] | Proxy sidecar move retry/mTLS/tracing para infra — app não sabe que existe |
| [[concepts/sidecar-pattern]] | Container proxy injetado em cada pod — intercepta tráfego sem alterar aplicação |
| [[concepts/mtls]] | mTLS automático + AuthorizationPolicy — Zero Trust dentro do cluster |
| [[concepts/fault-injection]] | Delay/abort declarativo via VirtualService — chaos engineering na camada de rede |
| [[concepts/ambient-mesh]] | Istio 1.22+ sem sidecar — ztunnel no nó, ~200MB economizados por pod |

### Colaboração em Tempo Real

| Página | Hook |
|---|---|
| [[concepts/crdt]] | CRDT — estrutura de dados que sempre converge sem servidor central, offline-first nativo |
| [[concepts/operational-transformation]] | OT — edição colaborativa com servidor central de sequenciamento (Google Docs) |

### Sistemas Distribuídos

| Página | Hook |
|---|---|
| [[concepts/three-phase-commit]] | 3PC — fase PreCommit evita blocking mas não tolera partição de rede — uso acadêmico |
| [[concepts/two-phase-commit]] | 2PC — coordinator failure = blocking indefinido com lock ativo |
| [[concepts/split-brain]] | Partição de rede causa decisões conflitantes — resolvido com quorum |
| [[concepts/raft-paxos]] | Consenso distribuído com quorum — etcd, CockroachDB, Kafka KRaft |
| [[concepts/saga-pattern]] | Consistência eventual com compensação — alternativa ao 2PC em microsserviços |
| [[concepts/outbox-pattern]] | Tabela outbox + CDC garante entrega sem lock distribuído |
| [[concepts/consistency-models]] | Linearizable → Sequential → Causal → Eventual — espectro, trade-offs, quando usar cada um |
| [[concepts/distributed-transactions]] | Mapa de abordagens — 2PC, 3PC, Saga, Outbox, CockroachDB |
| [[concepts/skip-locked]] | SELECT FOR UPDATE SKIP LOCKED — fila de jobs no PostgreSQL sem broker, até ~10k/s |
| [[concepts/fencing-token]] | Token monotônico que rejeita escritas de lock expirado — solução para lock fantasma |

### AI / LLM & Arquitetura com IA

| Página | Hook |
|---|---|
| [[concepts/divida-cognitiva]] | Falta de entendimento acumulada ao delegar para IA — quebra a capacidade do time de pensar |
| [[concepts/ai-brainfry]] | Esgotamento por supervisão de IA — +14% esforço mental, +12% fadiga, +19% sobrecarga |
| [[concepts/vibe-coding]] | Múltiplas threads de agentes paralelas — alta iniciativa, baixa acabativa, paralisia por foco |
| [[concepts/navigation-paradox]] | Agente perde 1/4 dos arquivos críticos em deps escondidas (DI); ferramenta de grafos ignorada 58% |
| [[concepts/abstraction-bloat]] | Agente gera 1000 linhas onde 100 bastariam — viés de treinamento para o complexo |
| [[concepts/comprehension-debt]] | Erosão progressiva de entender o próprio codebase gerado por IA — rubber stamping em revisão |
| [[concepts/yagni]] | You Ain't Gonna Need It — não abstrai até a dor ser real; IA escalou o problema |
| [[concepts/abstraction-illusion]] | IA torna padrões sofisticados acessíveis sem torná-los apropriados |
| [[concepts/vertical-slice-architecture]] | Feature-first vs camada-first — 1–3 arquivos por feature vs 7–13; melhor para agentes |

### Resiliência

| Página | Hook |
|---|---|
| [[concepts/retry-backoff]] | Backoff exponencial + jitter — distribui carga no tempo, evita thundering herd |
| [[concepts/thundering-herd]] | Spike coordenado de clientes que amplifica falha — solução é jitter |
| [[concepts/back-pressure]] | Produtor mais rápido que consumidor — desacelerar, bufferizar ou descartar deliberadamente |
| [[concepts/cache-stampede]] | Cache expira e N callers vão ao banco simultaneamente — probabilistic expiration + coalescing |
| [[concepts/temporal-coupling]] | Ordem implícita de chamadas sem enforcement no código — design de API impossível de chamar errado |
| [[concepts/accidental-complexity]] | Complexidade introduzida pelo time, não pelo domínio — pode e deve ser removida |
| [[concepts/essential-complexity]] | Complexidade inerente ao problema — não pode ser removida, projete bem para conviver |
| [[concepts/idempotencia]] | Mesma operação N vezes = mesmo resultado — pré-requisito para retry seguro |
| [[concepts/bulkhead]] | Pool separado por downstream — um serviço lento não derruba os outros |
| [[concepts/circuit-breaker]] | Decide SE tenta — 3 estados, Opossum, retry dentro do breaker, métricas por criticidade |
| [[concepts/falha-em-cascata]] | Serviço lento esgota thread pool do chamador — mecanismo e padrões de prevenção |
| [[concepts/blast-radius]] | Extensão do impacto quando um componente falha — reduza com isolamento |
| [[concepts/fail-fast]] | Rejeitar em 1s é melhor que enfileirar e falhar em 30s |
| [[concepts/graceful-degradation]] | Continua com capacidade reduzida ao invés de falhar completamente |
| [[concepts/littles-law]] | `L = λ × W` — fórmula para dimensionar concorrência de pool |

### Mensageria & Async

| Página | Hook |
|---|---|
| [[concepts/mensageria]] | Queue vs Stream, Kafka/SQS/RabbitMQ, DLQ, at-least-once, outbox pattern |
| [[concepts/rate-limiting]] | Token Bucket, Sliding Window Counter, Redis Lua, hierarquia de limites |
| [[concepts/load-balancer]] | L4 vs L7, round-robin, health check ativo, VIP para HA, dois níveis em microsserviços |

### Observabilidade & FinOps

| Página | Hook |
|---|---|
| [[concepts/distributed-tracing]] | Spans, traceparent W3C, OpenTelemetry → Jaeger, sampling obrigatório |
| [[concepts/finops]] | Unit economics, right-sizing, batch vs realtime, egress invisível, storage hierárquico |
| [[concepts/ledger-dupla-entrada]] | Double entry bookkeeping, append-only, conciliação, invariante débito = crédito |

### Banco de Dados / Infra

| Página | Hook |
|---|---|
| [[concepts/acid]] | Atomicity, Consistency, Isolation, Durability — fundação do relacional |
| [[concepts/nosql]] | Document, Key-Value, Wide-Column, Graph, Search — cada tipo resolve um problema |
| [[concepts/relational-vs-nosql]] | Trade-offs de consistência, escala, schema e queries |
| [[concepts/postgresql]] | Default para tudo — JSONB, full-text, pg_vector, Timescaledb |
| [[concepts/database-index]] | Índices aceleram reads ao custo de overhead em escritas |
| [[concepts/database-transactions]] | $transaction obrigatório para operações dependentes |
| [[concepts/read-replicas]] | Réplicas para workload read-heavy — roteamento explícito |
| [[concepts/read-your-writes]] | Consistência pós-escrita com réplicas — flag Redis por N segundos |
| [[concepts/connection-pooling]] | PgBouncer — 1000 conexões de entrada → 20 conexões reais |
| [[concepts/n-plus-one]] | Bug mais comum de ORM — 1+N queries viram 1 query com JOIN |
| [[concepts/db-sharding]] | Sharding horizontal — range/hash/consistent hashing, shard key, resharding |
| [[concepts/uuid]] | UUIDv4 vs v7 — page splitting, BINARY(16), alternativas Snowflake/ULID/NanoID |
| [[concepts/page-splitting]] | Rebalanceamento do B+ Tree com PKs aleatórias — 50% utilização vs 94% com sequenciais |

### Carreira & Liderança

| Página | Hook |
|---|---|
| [[concepts/vocabulario-tecnico]] | Nomear conceitos com precisão — sem isso, documentação não faz sentido e discussões excluem |
| [[concepts/pensamento-sistemico]] | Pensar em sistema (carga real, inputs inesperados) vs arquivos que passam em teste |
| [[concepts/ia-ciclo-dependencia]] | Quanto menos entende o que IA gera, menos consegue avaliar — ciclo de degradação |
| [[concepts/dev-e-negocio]] | Dev que entende receita, custo e margem influencia resultados reais |
| [[concepts/ownership-proativo]] | Puxar responsabilidade por projetos de alto impacto — não esperar cair no colo |
| [[concepts/contratacao-barra-alta]] | Manter padrões elevados na contratação — sênior deve participar do filtro |
| [[concepts/mentoria-tecnica]] | Transferir conhecimento a júniors — escala o time e preserva cultura |
| [[concepts/one-on-one]] | Reunião individual que revela o que reuniões abertas nunca revelam |
| [[concepts/prova-de-conceito]] | Testar tecnologia nova em projeto isolado antes de levar para produção |
| [[concepts/flexibilidade-tecnica]] | Aceitar múltiplas soluções válidas — inflexibilidade impede inovação |
| [[concepts/extreme-ownership]] | Líder assume responsabilidade total pelo time — sem desculpas, sem ego |
| [[concepts/problema-com-solucao]] | Levar problemas ao gestor sempre com sugestão — distingue solucionador de reclamante |
| [[concepts/dizer-sim-para-tudo]] | Hábito de aceitar toda solicitação — fragmenta foco e inibe crescimento alheio |
| [[concepts/definicao-de-pronto]] | Código legível + testado + documentado = pronto; funcionar não é suficiente |
| [[concepts/testar-proprio-codigo]] | Testar além do happy path — casos de erro são onde os bugs vivem |
| [[concepts/atomic-commits]] | Commit = alteração + teste juntos; uma unidade funcional por commit |
| [[concepts/neuroplasticidade]] | Cérebro muda estrutura física por exposição — preparar terreno é etapa obrigatória antes de aprender |
| [[concepts/spaced-repetition]] | Exposição espaçada ao longo dos dias — nunca copiar/colar código, redigitar tudo manualmente |
| [[concepts/tempo-variavel-capacidade-fixa]] | Conseguir é constante, tempo é variável — inversão que remove bloqueio de "falta de dom" |
| [[concepts/aprendizado-deliberado]] | Avalanche → pausa → prática → intercalar teoria/prática — processo estruturado de aprendizagem |
| [[concepts/postura-de-programador]] | Sobrevivência > curiosidade > salário — motivação de futuro é o que sustenta consistência |
| [[concepts/comparacao-na-carreira]] | Bastidor vs palco — o único referencial válido é você hoje vs você ontem |
| [[concepts/familiaridade-vs-capacidade]] | Velocidade inicial ≠ talento — linha de largada diferente, não capacidade diferente |
| [[concepts/log-de-aprendizado]] | Registro periódico do que foi aprendido — torna visível a evolução imperceptível no dia a dia |
| [[concepts/linha-de-largada]] | Ponto de partida determinado por exposição anterior, não por talento |
| [[concepts/principio-da-inversao]] | Modelo mental de Jacobi/Munger — inverter o problema para revelar a solução |
| [[concepts/dados-vs-intuicao]] | Dados superam intuição especialmente em ideias inovadoras — HiPPO effect |
| [[concepts/complexidade-como-estrategia]] | Os 3 estágios de quem complica o código intencionalmente como estratégia |
| [[concepts/ciclo-da-desgraca-software]] | Espiral de reescrita que sempre volta ao ponto inicial |
| [[concepts/pitfalls-de-linguagem]] | Funcionalidades que existem mas não devem ser usadas — JS e além |
| [[concepts/maturidade-tecnica]] | Capacidade de extrair aprendizado de qualquer situação, incluindo feedback crítico |
| [[concepts/atualizacao-tecnologica]] | Equilíbrio entre acompanhar evolução e evitar fadiga tecnológica |
| [[concepts/tutorial-hell]] | Espiral de consumo passivo de tutoriais sem produzir resultados reais |
| [[concepts/profundidade-e-maestria]] | Maestria em qualquer assunto como prognóstico universal — falhar e se recuperar como filtro |
| [[concepts/abrangencia-profissional]] | Interessado > interessante — T-shape saudável e o risco do Tony Funil |
| [[concepts/comunicacao-tecnica]] | Tradução na ponta emissora — responsabilidade de quem fala, não de quem ouve |
| [[concepts/curriculo-vs-portfolio]] | Promessa vs prova — currículo descreve, portfólio demonstra maestria |

### CS Fundamentals — Sistemas Operacionais

| Página | Hook |
|---|---|
| [[concepts/processo]] | Instância de programa em execução — PID, ciclo de vida, isolamento de memória |
| [[concepts/thread]] | Execução dentro do processo — pilha própria, memória compartilhada, race condition |
| [[concepts/deadlock]] | Bloqueio mútuo eterno — 4 condições de Coffman e estratégias de prevenção |
| [[concepts/mutex]] | Mutual exclusion — chave de porta para seção crítica, custo e alternativas |
| [[concepts/escalonador]] | Decide quem roda e quando — round-robin, filas de prioridade, aging, CFS |
| [[concepts/context-switch]] | Salvar e restaurar estado ao trocar de processo — custo e TLB flush |
| [[concepts/interrupcao-de-hardware]] | Sinal que para o processador e entrega controle ao SO — timer, teclado, disco |
| [[concepts/memoria-virtual]] | Cada processo acha que tem a RAM toda — page table, TLB, page fault |
| [[concepts/swap]] | RAM transborda para disco — thrashing e quando desativar |
| [[concepts/sistema-de-arquivos]] | Abstração de arquivos sobre blocos brutos — ext4/NTFS/APFS, delete ≠ apagar |
| [[concepts/syscall]] | Interface user mode → kernel — open/read/write/fork e custo de troca de modo |
| [[concepts/kernel]] | Núcleo com acesso total ao hardware — user mode vs kernel mode, BSOD |

### Testes

| Página | Hook |
|---|---|
| [[concepts/piramide-de-testes]] | Estratégia de testes — camadas unitário/integração/E2E e variante Trophy |
| [[concepts/tdd]] | Red/Green/Refactor — design emergente e as escolas Detroit vs London |
| [[concepts/test-doubles]] | Dummy/Stub/Fake/Spy/Mock — taxonomia e regra Fake > Mock |
| [[concepts/bdd]] | Gherkin/Cucumber — specs executáveis por PO/QA/Dev como living docs |
| [[concepts/contract-testing]] | Pact — consumer-driven contracts e gate can-i-deploy em microsserviços |
| [[concepts/living-documentation]] | Docs geradas de testes/código — Cucumber Report, OpenAPI, Structurizr |

---

## Entities

| Página | Hook |
|---|---|
| [[entities/react]] | Biblioteca JS para UI — modelo mental, versões, ecossistema |
| [[entities/tanstack]] | Organização open-source — TanStack Query, Table, Router, Form, Virtual |
| [[entities/linear-app]] | Referência de design e performance — velocidade percebida, keyboard-first |
| [[entities/figma]] | Ferramenta de design — papel varia por abordagem (design first vs code first) |
| [[entities/dribbble]] | Plataforma de referências visuais para devs frontend |
| [[entities/lovable]] | Ferramenta IA para construção de apps — exemplo de design de produto acessível |
| [[entities/charlie-munger]] | Investidor, sócio de Buffett — popularizou o princípio da inversão como modelo mental |
| [[entities/george-hotz]] | geohot — hacker do iPhone/PS3, carro autônomo open source, citado sobre aprendizado na prática |
| [[entities/karl-gustav-jakob-jacobi]] | Matemático alemão — origem do "inverter, sempre inverta" |
| [[entities/randy-nelson]] | Ex-Pixar, Apple, educador — framework profundidade/abrangência/comunicação |
| [[entities/martin-kleppmann]] | Autor de "Designing Data-Intensive Applications" — crítica ao Redlock, pesquisa em CRDTs |
| [[entities/yjs]] | Biblioteca CRDT de sequência — padrão da indústria para edição colaborativa em tempo real |
| [[entities/fred-brooks]] | Autor de "No Silver Bullet" (1986) e "Mythical Man-Month" — cunhou complexidade essencial vs acidental |
| [[entities/margaret-storey]] | Pesquisadora UBC — formalizou conceito de dívida cognitiva aplicada a times com IA (2026) |

---

## Questions

_Nenhuma questão aberta registrada ainda._
