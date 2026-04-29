# 🏛️ Checklist de Conhecimentos — Solutions Architect

> Mapa completo de domínios técnicos para uma carreira de Solutions Architect / Tech Lead.
> Baseado nas skills: `tech-mentor-backend`, `tech-mentor-system-design`, `tech-mentor-infra`, `tech-mentor-data`, `tech-mentor-security`, `tech-mentor-testing`, `tech-mentor-networking`, `tech-mentor-platform`, `tech-mentor-leadership`, `lang-dynamic`, `lang-managed`, `lang-systems`, `tech-mentor-ai`

---

## Legenda

- ⬜ Não estudado
- 🟡 Em andamento
- ✅ Concluído / Dominado

---

## 🏛️ 1. Fundamentos de Arquitetura de Software

### Estilos Arquiteturais
- [x] Clean Architecture — camadas, Dependency Rule, inversão de controle
- [x] Hexagonal / Ports & Adapters — InMemory adapters, testabilidade, DI
- [x] Monolito Modular — bounded modules, acoplamento interno, migração
- [ ] Microsserviços — decomposição por domínio, trade-offs, autonomia de deploy
- [ ] Micro-Kernel — plugin architecture, core + extensões
- [ ] Space-Based Architecture — tuple space, processing units, escalabilidade horizontal
- [ ] Cell-Based Architecture — failure isolation, blast radius, deployment cells
- [ ] Reactive Architecture — Reactive Manifesto, backpressure, non-blocking I/O
- [x] Event-Driven Architecture (EDA) — event broker, async-first, temporal decoupling

### Documentação e Decisão
- [x] C4 Model — Context, Container, Component, Code diagrams
- [x] ADR (Architecture Decision Record) — formato, processo, revisão
- [ ] Wardley Maps — value chain, evolução de componentes, estratégia
- [x] RFC — processo, template, revisão, decisão técnica
- [ ] Architecture Fitness Functions — testes automatizados de restrições arquiteturais

### Princípios e Padrões Transversais
- [x] SOLID — Single Responsibility, Open/Closed, Liskov, Interface Segregation, DIP
- [x] Twelve-Factor App — config, logs, stateless, backing services
- [ ] Conway's Law — implicações organizacionais no design de sistemas
- [ ] Evolutionary Architecture — mudança incremental, fitness functions, strangler fig
- [ ] BFF (Backend for Frontend) — pattern por cliente/time
- [x] Design Patterns (GoF) — Factory, Strategy, Observer, Decorator, Command, Adapter
- [ ] Integration Patterns (EIP) — Claim Check, Competing Consumers, Routing Slip
- [ ] Anti-patterns — Big Ball of Mud, God Object, Distributed Monolith, Anemic Domain

---

## 🧩 2. Domain-Driven Design (DDD)

### Strategic Design
- [x] Bounded Context — definição de fronteiras, linguagem ubíqua
- [x] Context Map — upstream/downstream, tipos de relacionamento
- [x] Shared Kernel — código compartilhado, riscos e governança
- [x] Customer/Supplier — negociação de contratos entre contextos
- [x] Anti-Corruption Layer (ACL) — tradução entre modelos
- [x] Open Host Service — API publicada para múltiplos consumidores
- [x] Published Language — protocolo canônico entre contextos

### Tactical Design
- [x] Aggregate e Aggregate Root — invariantes, consistência transacional
- [x] Value Objects — imutabilidade, identidade por valor
- [x] Entities — identidade por ID, ciclo de vida
- [x] Domain Events — o que aconteceu, integração entre contextos
- [x] Domain Services — lógica sem dono natural em uma entidade
- [x] Application Services — orquestração de use cases
- [x] Repository Pattern — abstração de persistência por aggregate
- [x] Specification Pattern — regras de negócio encapsuláveis e combináveis

### DDD Avançado
- [x] Event Storming — discovery colaborativo, Big Picture, Process Level
- [x] Domain Events vs Integration Events — diferenças e uso correto
- [x] DDD com Microsserviços — mapeamento Bounded Context → serviço
- [ ] DDD com CQRS — separação Command/Query no domain model

---

## 🔀 3. Padrões Arquiteturais Avançados

### Consistência e Entrega
- [x] CQRS — separação de leitura e escrita, projeções, eventual consistency
- [x] Event Sourcing — Append-only, Snapshot, Replay, Event Store, Event Schema Migration
- [x] Outbox Pattern — garantia de entrega transacional, Outbox + CDC pipeline
- [x] Inbox Pattern — exactly-once delivery, deduplicação
- [x] Dual Write Problem — riscos, soluções (Outbox, CDC)
- [x] Transactional Outbox — implementação com Debezium e WAL

### Resiliência
- [x] Saga — Choreography vs Orchestration, compensação, rollback distribuído
- [ ] Strangler Fig — migração incremental de legado
- [x] Circuit Breaker — estados, half-open, fallback
- [x] Retry e Exponential Backoff — jitter, dead letter
- [x] Timeout e Bulkhead — isolamento de falhas, thread pool
- [x] Graceful Degradation — backpressure, overflow strategies, load shedding
- [ ] Tolerant Reader — compatibilidade retroativa no consumo de eventos

### Migração e Evolução
- [ ] Expand-Contract — migrações sem breaking change
- [ ] Blue/Green Deploy — troca atômica de ambiente
- [ ] Canary Release — rollout gradual com análise automática
- [ ] Rolling Update — atualização gradual sem downtime
- [ ] Feature Flags como deployment strategy — dark launch, kill switch

---

## 🌐 4. Sistemas Distribuídos

### Fundamentos Teóricos
- [ ] CAP Theorem — Consistency, Availability, Partition Tolerance
- [ ] PACELC — extensão do CAP para latência vs consistência
- [ ] Modelos de Consistência — linearizability, sequential, causal, eventual
- [ ] Vector Clocks — causalidade e ordenação de eventos
- [ ] Gossip Protocol — propagação de estado, anti-entropy
- [ ] Quorum — leitura/escrita, majority quorum, Dynamo model
- [ ] Leader Election — Raft, ETCD, algoritmos de consenso
- [ ] Raft Consensus — log replication, eleição, safety

### Concorrência e Coordenação
- [ ] Idempotência — Idempotency Key, TTL, dedup, CAS
- [ ] 2PC (Two-Phase Commit) — coordinator, participants, falhas
- [ ] 3PC — extensão do 2PC, problemas de performance
- [ ] Distributed Lock — Redlock, Redis NX, etcd, Advisory Lock (PostgreSQL)
- [ ] SKIP LOCKED — processamento paralelo de filas no banco
- [ ] Fencing Token — prevenção de stale locks

### Topologia e Escala
- [ ] DB Sharding — Shard Key, consistent hashing, resharding, cross-shard queries
- [ ] Read Replicas — lag, eventual consistency, casos de uso
- [ ] Connection Pooling — PgBouncer, pgpool, RDS Proxy, prepared statements
- [ ] Multi-region — geo-failover, active-active, latency routing, anycast
- [ ] Consistent Hashing — virtual nodes, adição/remoção de nós
- [ ] Service Discovery — DNS-based, client-side (Eureka), server-side (Envoy)

---

## 📨 5. Mensageria e Eventos

### Brokers
- [ ] Kafka — topics, partitions, consumer groups, Schema Registry, DLQ, replication
- [ ] Kafka Avançado — compaction, exactly-once, transactions, tiered storage
- [ ] RabbitMQ — exchanges, bindings, DLX, routing keys
- [ ] NATS / NATS JetStream — subjects, consumers, KV Store, object store
- [ ] SQS / SNS — fifo, visibility timeout, fanout pattern
- [ ] Comparação de brokers — Kafka vs RabbitMQ vs SQS vs NATS vs Pulsar

### Integração e CDC
- [ ] CDC (Change Data Capture) — Debezium, WAL, Binlog, Kafka Connect
- [ ] Schema Registry — Avro, Protobuf, evolução de schema, breaking changes
- [ ] AsyncAPI — spec para sistemas event-driven, documentação de tópicos

### Jobs e Workflows
- [ ] Background Jobs — BullMQ, Celery, Sidekiq, SKIP LOCKED, retry strategy
- [ ] Workflow Orchestration — Temporal, Step Functions, Conductor
- [ ] Temporal Avançado — Signals, Queries, Child Workflows, Continue-as-New, versionamento
- [ ] Durable Execution — garantias de Temporal vs Saga manual

### Padrões de Eventos
- [ ] DLQ e Poison Pill — estratégias de quarentena e reprocessamento
- [ ] At-least-once vs Exactly-once — trade-offs, implementação
- [ ] Event Ordering — particionamento como solução, limitações
- [ ] Long-Running Processes — Process Manager, Saga com state machine
- [ ] Event Versioning — upcasting, schema evolution, consumer migration

---

## 🔌 6. APIs e Protocolos

### Design e Contratos
- [ ] REST — OpenAPI 3.1, versionamento, API-First, status codes, HATEOAS
- [ ] API Contracts — TypeSpec, Spectral linting, breaking changes, Prism mock, Microcks
- [ ] API Versioning — Sunset Policy (RFC 8594), Expand-Contract, Tolerant Reader
- [ ] API Economy — monetização, developer portal, API como produto, marketplace
- [ ] API Gateway — Kong, AWS API Gateway, rate limit, auth na borda, plugin model

### Protocolos Específicos
- [ ] GraphQL — DataLoader, N+1, persisted queries, schema-first, Federation v2
- [ ] gRPC — Protobuf, streaming unary/server/client/bidi, interceptors
- [ ] Serialização — JSON, Protobuf, Avro, MessagePack, Thrift, FlatBuffers

### Comunicação em Tempo Real
- [ ] WebSocket avançado — backpressure, heartbeat, bufferedAmount, reconexão com backoff
- [ ] SSE (Server-Sent Events) — Last-Event-ID, X-Accel-Buffering, reconnection
- [ ] WebTransport — 0-RTT, multiplexing, QUIC-based, vs WebSocket
- [ ] LLM Streaming — SSE token streaming, Partial Response, Abort Signal, JSON Schema enforcement

### Webhooks e Segurança de API
- [ ] Webhook — HMAC, signWebhook, verifyWebhook, timingSafeEqual, retry, fanout
- [ ] CORS — preflight, security headers, Helmet, CSP, CSRF, SameSite
- [ ] OWASP API Top 10 — BOLA, BFLA, Mass Assignment, Schema Poisoning

### Padrões de Acesso
- [ ] Pagination — Keyset, Cursor, Offset, Seek Method, paginação bidirecional/distribuída
- [ ] Idempotency Key — padrão completo, TTL, armazenamento, edge cases
- [ ] Rate Limiting — Token Bucket, Leaky Bucket, Fixed Window, Sliding Window, algoritmos distribuídos

---

## 🗃️ 7. Banco de Dados Relacional

### PostgreSQL
- [x] MVCC — Multi-Version Concurrency Control, vacuum, xmin/xmax
- [x] EXPLAIN ANALYZE — planos de execução, seq scan, index scan, cost
- [x] WAL — Write-Ahead Log, replicação lógica, ponto de recuperação
- [x] Autovacuum — dead tuples, bloat, tuning de parâmetros
- [x] pg_stat_statements — análise de queries, top queries por custo
- [ ] pg_partman — particionamento por range/list/hash, gerenciamento automático
- [ ] pglogical — replicação lógica entre versões, upgrade sem downtime
- [ ] pg_repack — desfragmentação sem lock exclusivo
- [x] Full-Text Search — tsvector, GIN, pg_trgm, configurações de idioma

### Índices e Otimização
- [x] B-tree, Covering Index, Partial Index — quando usar cada um
- [x] GIN, GiST, BRIN — tipos especializados e casos de uso
- [x] Query Optimization — EXPLAIN, índices compostos, predicate pushdown
- [x] ACID e Isolation Levels — Read Committed, Repeatable Read, Serializable, anomalias

### SQL Avançado
- [x] Window Functions — RANK, LEAD, LAG, PARTITION BY, ROWS BETWEEN
- [x] CTEs — recursivas, materializadas, WITH RECURSIVE
- [x] Upsert — ON CONFLICT DO UPDATE, uso com idempotência
- [ ] Savepoints — nested transactions, rollback parcial

### Migrations e Evolução
- [ ] Migrations — Flyway, Liquibase, Alembic, Prisma, estratégias de versionamento
- [ ] Schema Evolution — DDL sem bloqueio, online schema change
- [ ] Expand-Contract em banco — adição de coluna nullable → backfill → constraint
- [ ] Database Testing — Testcontainers, Fixtures, Seed, Schema Snapshot

---

## 📦 8. Banco de Dados NoSQL e Especializados

### Document / Key-Value
- [ ] MongoDB — Aggregation Pipeline, Change Streams, Schema Validation, Atlas
- [ ] Redis — cache, pub/sub, streams, Redlock, eviction policies, modules
- [ ] DynamoDB — single-table design, GSI, LSI, streams, DynamoDB Accelerator

### Search e Analítica
- [ ] Elasticsearch / OpenSearch — BM25, faceted search, full-text, inverted index, mappings
- [ ] DuckDB — OLAP in-process, SQL sobre Parquet/CSV, edge analytics

### Especializados
- [ ] Graph DB — Neo4j, Cypher, casos de uso (fraude, recomendação, social)
- [ ] Time-Series — TimescaleDB, InfluxDB, QuestDB, retention policy, downsampling
- [ ] Vector DB — Qdrant, Weaviate, pgvector, HNSW, flat index, busca híbrida
- [ ] Embedded DB — SQLite, DuckDB, libSQL, LiteFS, edge database
- [ ] Banco Distribuído — CockroachDB, Spanner, YugabyteDB, TiDB — trade-offs

### Arquitetura de Dados
- [ ] Database per Service — federation, polyglot persistence, trade-offs de acesso
- [ ] Multitenancy DB — RLS, schema per tenant, row isolation, Supabase
- [ ] CQRS + Read Model — projeções desnormalizadas para leitura

---

## ♻️ 9. Cache e Performance

### Estratégias de Cache
- [ ] Cache-Aside — padrão lazy loading, cache miss, TTL
- [ ] Write-Through — consistência forte, latência de escrita
- [ ] Write-Behind (Write-Back) — performance, risco de perda de dados
- [ ] Cache Stampede — mutex lock, probabilistic early expiration, request collapsing
- [ ] Cache Invalidation — event-driven, TTL-based, versioned keys

### Performance
- [ ] Flame Graph — CPU profiling, identificação de hot paths
- [ ] USE Method — Utilization, Saturation, Errors para diagnóstico
- [ ] RED Method — Rate, Errors, Duration para serviços
- [ ] Four Golden Signals — latência, tráfego, erros, saturação
- [ ] Load Testing — k6, Gatling: stress, soak, spike, breakpoint tests
- [ ] Async I/O — Event Loop, io_uring, epoll, Goroutines, UV Thread Pool
- [ ] Memory Management — GC Tuning, JVM ZGC/G1, Node Heap, memory leak patterns

### Espacial e Geolocalização
- [ ] PostGIS — queries espaciais, índice GIST, ST_DWithin, geometrias
- [ ] Geohash, H3 — indexação geoespacial, hierarquia, proximity queries
- [ ] Redis GEO — GEORADIUS, comandos geoespaciais, use cases

---

## 🔐 10. Auth e Identidade

### Protocolos de Autenticação
- [x] OAuth2 — Authorization Code, Client Credentials, PKCE, Device Flow
- [x] OIDC — ID Token, UserInfo endpoint, Discovery, sessão federada
- [x] JWT — claims padrão, rotação de chaves, revogação, JWK Set
- [ ] Sessions — server-side session, Redis session store, cookie security

### Autorização
- [x] RBAC — roles, permissions, herança de papéis
- [x] ABAC — policy engine, atributos de subject/resource/environment
- [x] ReBAC — relationship-based (Zanzibar model), grafos de permissão
- [x] OpenFGA — implementação open source do Zanzibar, tuplesets
- [ ] Casbin — PERM model, adaptadores, enforcer policies
- [ ] SCIM — provisionamento automático de usuários, sincronização com IdP

### Segurança de Identidade
- [ ] IAM Avançado — permissões granulares, least privilege, just-in-time access
- [ ] SSO — SAML 2.0, OIDC federation, provider linking
- [ ] MFA — TOTP, WebAuthn/FIDO2, Passkeys, SMS fallback risks
- [ ] Workload Identity — SPIFFE/SPIRE, SVID, service-to-service auth sem segredo

---

## 📡 11. Realtime e Comunicação

- [ ] WebSocket — arquitetura de cluster, Redis Pub/Sub para broadcast, auth
- [ ] WebRTC — STUN, TURN, ICE, SFU, Janus, mediasoup, simulcast
- [ ] CRDT — G-Counter, LWW, Y.js, resolução de conflito, collaborative editing
- [ ] Pub/Sub — arquitetura, fan-out, deduplicação, at-least-once delivery
- [ ] Notification System — fan-out on write vs read, push FCM/APNs, email bounce, SSE
- [ ] Backend for Mobile — offline-first, delta sync, conflict resolution
- [ ] Presence System — online/offline, heartbeat, TTL-based, Redis

---

## ☁️ 12. Cloud e Infraestrutura

### Kubernetes
- [ ] Kubernetes Core — Pod, Deployment, StatefulSet, DaemonSet, RBAC, Probes
- [ ] K8s Autoscaling — HPA, VPA, KEDA, Karpenter, ScaledObject
- [ ] K8s Networking — CNI, Cilium, Calico, NetworkPolicy, Gateway API
- [ ] K8s Storage — CSI, PVC, StorageClass, Longhorn, Velero
- [ ] K8s Operators — CRD, Kubebuilder, Reconcile Loop, Admission Webhooks
- [ ] K8s Security — seccomp, AppArmor, PSS, OPA Gatekeeper, Kyverno
- [ ] K8s Cost Optimization — Kubecost, LimitRange, ResourceQuota, bin packing
- [ ] Multi-cluster K8s — Cluster API, vcluster, ArgoCD ApplicationSet, Fleet

### Cloud Providers
- [ ] AWS — EC2, ECS, EKS, Lambda, RDS, Aurora, DynamoDB, S3, IAM, SQS, SNS
- [ ] GCP — GKE, Cloud Run, Spanner, BigQuery, Pub/Sub, Workload Identity
- [ ] Azure — AKS, App Service, Functions, Cosmos DB, Entra ID, Service Bus
- [ ] Multi-cloud — Landing Zone, cloud-agnostic patterns, egress cost, portabilidade

### Serverless e Edge
- [ ] Serverless — Lambda, cold start, provisioned concurrency, Fargate, arm64 Graviton
- [ ] Edge Computing — Cloudflare Workers, Lambda@Edge, CDN, Durable Objects
- [ ] WebAssembly Backend — WASM, WASI, Wasmtime, Spin, Extism, plugins isolados

### Storage e Upload
- [ ] Object Storage — S3, multipart upload, presigned URL, lifecycle policies
- [ ] Media Pipeline — transcoding, CDN, signed URLs, video streaming HLS/DASH
- [ ] IoT — MQTT, QoS levels, Device Shadow, Digital Twin, OTA, AWS IoT Core

### Service Mesh
- [ ] Service Mesh — Istio, Linkerd, Cilium Mesh, Envoy, mTLS, traffic shaping
- [ ] mTLS — cert-manager, PKI interna, SPIFFE, certificate rotation

---

## 🔒 13. Segurança

### Secrets e Zero Trust
- [x] Secrets Management — Vault, SOPS, AWS Secrets Manager, rotação automática
- [ ] External Secrets Operator — sincronização K8s, backends suportados
- [x] Zero Trust — BeyondCorp, ZTNA, microsegmentação, device trust, IAP
- [ ] Policy as Code — OPA/Rego, Gatekeeper, Kyverno, Conftest, tfsec

### Supply Chain e AppSec
- [x] Supply Chain Security — SBOM, Sigstore, Cosign, Fulcio, SLSA, attestation
- [x] OWASP Top 10 — Injection, XSS, IDOR, SSRF, SAST, DAST, dependency scanning
- [x] Threat Modeling — STRIDE, PASTA, árvore de ataque, DREAD, threat intel
- [x] DevSecOps — shift-left security, pipeline de segurança, secret scanning

### Criptografia e Compliance
- [x] Data Encryption — Envelope Encryption, KMS, field-level encryption, tokenização
- [ ] TLS/mTLS — handshake, certificados, pinning, PKI interna
- [x] Compliance — LGPD, GDPR, auditoria, DSAR, consent management, data retention
- [x] PCI-DSS — card data environment, segmentação, tokenização de cartão
- [ ] CSPM — AWS Security Hub, GuardDuty, Defender for Cloud, Prowler, Wiz
- [x] Runtime Security — Falco, eBPF-based detection, container escape

---

## 🧪 14. Testes e Qualidade

### Estratégia
- [x] Pirâmide de Testes — unit, integration, E2E — proporcionalidade e custo
- [x] TDD — Red-Green-Refactor, design guiado por testes
- [x] BDD — Gherkin, Cucumber, alinhamento com negócio
- [ ] Mutation Testing — PIT, Stryker, cobertura qualitativa real

### Tipos de Teste
- [x] Contract Testing — Pact, CDC, provider verification
- [ ] Property-Based Testing — fast-check, Hypothesis, fuzz testing
- [ ] Testcontainers — PostgreSQL, Kafka, Redis com containers reais
- [ ] Snapshot Testing — regressão de output, Supertest para APIs
- [ ] E2E Testing — Playwright, Cypress, estratégia de ambiente

### Confiabilidade e Performance
- [ ] Chaos Engineering — Chaos Mesh, Gremlin, pod kill, network partition, Game Day
- [ ] Load Testing — k6, Gatling: thresholds, CI integration, relatórios
- [ ] Capacity Planning — estimativas de carga, análise de bottlenecks

### Qualidade de Código
- [ ] Software Craftsmanship — Clean Code, refactoring patterns, SOLID na prática
- [ ] Code Review — cultura, checklist arquitetural, feedback construtivo
- [ ] Architecture Fitness Functions — ArchUnit, Deptrac, validação de regras de dependência

---

## 🗺️ 15. System Design

### Metodologia
- [x] HLD (High-Level Design) — componentes, fluxo de dados, trade-offs explícitos
- [ ] Estimativas — QPS, storage, bandwidth, latência, back-of-envelope
- [ ] Framing de Arquiteto — escalabilidade, operacionalidade, custo, segurança
- [x] Casos Clássicos — URL Shortener, Twitter Feed, YouTube, WhatsApp, Uber, Typeahead

### Componentes de Infraestrutura
- [x] Load Balancer — L4 vs L7, algoritmos (round-robin, least conn), health check
- [x] CDN — edge caching, invalidação, arquitetura, signed URLs, WAF na borda
- [ ] Search Engine — Elasticsearch, inverted index, BM25, faceted search, ranking

### Domínios Específicos de Design
- [ ] FinTech System Design — ledger, dupla entrada, idempotência financeira, antifraude
- [ ] Billing System Design — subscription, metered, proration, dunning, revenue recognition
- [ ] Notification Service Design — fan-out on write/read, push, email, SMS, deduplicação
- [x] Ride-sharing Design — geolocalização, GEORADIUS, matching, surge pricing
- [ ] Gaming Backend — game state autoritativo, tick rate, matchmaking, leaderboard
- [ ] LLM Gateway Design — rate limiting por token, semantic cache, fallback chain, cost attribution

### Feature Design
- [x] Multi-tenancy Design — RLS, schema per tenant, billing por tenant
- [x] Feature Flags — LaunchDarkly, Unleash, dark launch, A/B test, kill switch
- [x] Zero-Downtime Deploy — estratégias, database migration durante deploy
- [x] Distributed Rate Limiter — Redis Lua, sliding window distribuído
- [x] Distributed Cache Design — Redis Cluster, cache invalidation strategies, replication

---

## 📊 16. Observabilidade e Confiabilidade (SRE)

### Pilares de Observabilidade
- [x] MELT — Metrics, Events, Logs, Traces — conceitos e diferenças
- [x] Structured Logging — JSON logs, correlation ID, request tracing
- [x] Metrics — counters, gauges, histograms, exemplars
- [x] Distributed Tracing — spans, baggage, context propagation, sampling

### OpenTelemetry
- [ ] OTel SDK — instrumentação em TypeScript, Java, Go, Python
- [ ] OTel Collector — receivers, processors, exporters, pipeline
- [ ] Tail Sampling — decisão no collector, estratégias por latência/erro
- [ ] Auto-instrumentation — agentes, zero-code instrumentation
- [ ] Continuous Profiling — Pyroscope, pprof, async-profiler, Clinic.js, eBPF

### SRE e Confiabilidade
- [ ] SLI, SLO, SLA — definição, medição, alinhamento com produto
- [ ] Error Budget — política, burn rate alerting, when to stop shipping
- [ ] SRE Incident Lifecycle — severidades, roles (IC/TL), comunicação, timeline
- [ ] Post-mortem Blameless — formato, facilitação, ação corretiva
- [ ] Runbook efetivo — automação, playbooks, on-call rotation, toil
- [ ] Game Day — planejamento, execução, métricas de aprendizado

---

## 🌍 17. Networking

### Protocolos de Rede
- [ ] TCP/IP — handshake, flow control, congestion control, BBR, tuning de kernel
- [ ] HTTP/1.1 — keep-alive, pipelining, limitações
- [ ] HTTP/2 — multiplexing, server push, header compression, ALPN
- [ ] HTTP/3 / QUIC — UDP-based, 0-RTT, connection migration, head-of-line blocking
- [ ] WebTransport — QUIC-based, streams bidirecionais, datagrams
- [ ] TLS — handshake TLS 1.3, certificados, OCSP stapling, session resumption
- [ ] DNS — resolução recursiva, tipos de registro, TTL, split-horizon, DNSSEC
- [ ] BGP — AS, peering, route reflector, ECMP, SD-WAN

### Segurança de Rede
- [ ] mTLS — mutual auth, client certificates, PKI interna
- [ ] VPN — WireGuard, IPSec, Tailscale, Mesh VPN, Zero Trust Network Access
- [ ] Network Observability — VPC Flow Logs, Hubble/Cilium, eBPF network tracing

### Serialização
- [ ] JSON — limitações de performance, parsing cost
- [ ] Protobuf — schema evolution, field numbering, backward/forward compatibility
- [ ] Avro — schema registry integration, union types
- [ ] MessagePack, Thrift, FlatBuffers — casos de uso, trade-offs

---

## 🏗️ 18. Platform Engineering e DevOps

### Developer Experience
- [ ] Platform Engineering — IDP, Backstage, Golden Paths, scaffolding, paved roads
- [ ] DevEx — SPACE Metrics, inner loop, cognitive load, developer satisfaction
- [ ] DORA Metrics — deploy frequency, lead time, MTTR, change failure rate
- [ ] Software Catalog — Backstage, service ownership, dependency mapping
- [ ] Golden Path Templates — cookiecutter, Backstage scaffolder, service templates

### CI/CD
- [ ] CI/CD Strategies — trunk-based development, GitFlow, feature toggles, ephemeral envs
- [ ] GitHub Actions Avançado — reusable workflows, composite actions, OIDC, matrix
- [ ] Progressive Delivery — Argo Rollouts, Flagger, canary automatizado, analysis templates
- [ ] Build Caching — Turborepo, Nx, Bazel, BuildKit, remote cache
- [ ] Monorepo Backend — Nx, Turborepo, Changesets, affected builds, workspace protocols

### IaC e GitOps
- [ ] Terraform — provider, state, módulos, Terragrunt, drift detection
- [ ] Pulumi — IaC com TypeScript/Python, ComponentResource, Automation API
- [ ] Crossplane — K8s-native IaC, Managed Resource, Composite Resource
- [ ] Ansible — Configuration Management, Playbook, Role, Molecule
- [ ] GitOps — ArgoCD, Flux, pull-based, reconciliation loop
- [ ] ArgoCD Avançado — ApplicationSet, sync waves, resource hooks, multi-cluster

### FinOps
- [ ] FinOps — Reserved Instances, Spot, rightsizing, savings plans, unit economics
- [ ] FinOps Avançado — FOCUS standard, GPU cost, anomaly detection, chargeback

### Local Development
- [ ] Docker Compose avançado — depends_on, profiles, extends, Compose Watch
- [ ] Devcontainer — setup reproduzível, features, extensions
- [ ] LocalStack, WireMock, MSW — simulação de serviços externos localmente

---

## 📐 19. Dados e Arquitetura de Dados

### Arquiteturas
- [ ] Lambda Architecture — batch + speed layer, serving layer
- [ ] Kappa Architecture — streaming-only, reprocessamento via replay
- [ ] Data Warehouse — dimensional modeling, star schema, snowflake
- [ ] Data Lake — raw data, zone architecture (bronze/silver/gold)
- [ ] Lakehouse — Delta Lake, Apache Iceberg, Apache Hudi, time travel
- [ ] Data Mesh — domain ownership, data product, self-serve platform, federated governance
- [ ] Medallion Architecture — Bronze → Silver → Gold, qualidade incremental

### Streaming e Processamento
- [ ] Kafka Streams — stateful processing, KTable, windowed aggregations
- [ ] Apache Flink — CEP, exactly-once, checkpointing, watermarks
- [ ] ksqlDB — SQL sobre Kafka, push queries, materialized views
- [ ] dbt — transformação, testes de dados, Semantic Layer, lineage

### Governança e Qualidade
- [ ] Data Contracts — Schema Registry, AsyncAPI, Soda, breaking change detection
- [ ] Data Quality — Great Expectations, data SLA, circuit breaker em pipeline
- [ ] Data Governance — DataHub, OpenLineage, RBAC, data masking, LGPD pipelines
- [ ] Cloud Warehouses — BigQuery, Snowflake, Azure Synapse — trade-offs e features

### AI/ML Data
- [ ] Feature Store — Feast, Tecton, offline/online store, feature reuse
- [ ] MLOps — Kubeflow, MLflow, Ray, model registry, champion/challenger
- [ ] Reverse ETL — dados do warehouse de volta para sistemas operacionais

---

## 🤖 20. AI e LLM Backend

- [x] RAG (Retrieval-Augmented Generation) — chunking, embedding, retrieval, reranking
- [x] Vector DB — pgvector, Qdrant, Weaviate, HNSW, busca híbrida (BM25 + dense)
- [x] LLM Gateway — LiteLLM, routing, rate limiting por token, fallback chain
- [x] Semantic Cache — pgvector, cosine similarity, cache invalidation
- [x] AI Agents — tool use, ReAct, planning, multi-agent patterns
- [x] MCP (Model Context Protocol) — server, client, tools, resources
- [x] LLM Streaming — SSE, backpressure, Abort Signal, partial JSON
- [x] Structured Outputs — JSON Schema enforcement, function calling, validation
- [x] Prompt Caching — Anthropic/OpenAI, cost reduction, TTL
- [x] Batch Inference — async jobs, cost attribution, throughput vs latency
- [x] Evals — LLM-as-judge, human feedback, regression, ragas, BLEU
- [ ] LLM Serving — vLLM, TGI, Triton, KServe, quantization, tensor parallelism
- [ ] AI System Design — RAG pipeline, vector DB sharding, LLM inference scaling

---

## 👨‍💻 21. Linguagens e Ecossistemas

### TypeScript / Node.js
- [ ] TypeScript avançado — generics, conditional types, template literal types, decorators
- [ ] Node.js internals — event loop, libuv, streams, worker threads, clustering
- [ ] Fastify — lifecycle hooks, plugins, schemas, validação com Zod/AJV
- [ ] Performance Node — heap profiling, Clinic.js, async_hooks, diagnostics channel

### Java / Kotlin / JVM
- [ ] Spring Boot — Web, Data JPA, Security, Actuator, configuration
- [ ] Spring avançado — GraalVM native image, Project Loom, Virtual Threads
- [ ] Kotlin — coroutines, Flow, structured concurrency, Ktor, KMP
- [ ] JVM Tuning — G1GC, ZGC, heap sizing, GC logging, thread dump

### Go
- [ ] Go core — goroutines, channels, select, context, interfaces, error handling
- [ ] Go avançado — profiling com pprof, benchmarks, generics, sync primitives
- [ ] Go backend — Chi/Gin/Echo/Fiber, middleware, database/sql, sqlc

### Rust
- [ ] Rust core — ownership, borrowing, lifetimes, traits, trait objects
- [ ] Rust backend — Axum, Tokio, async/await, error handling com anyhow/thiserror
- [ ] Rust avançado — unsafe, macros, WASM, FFI, embedded

### Python
- [ ] Python avançado — asyncio, type hints, dataclasses, generators, Protocol
- [ ] Frameworks — FastAPI, Celery, SQLAlchemy, Pydantic v2
- [ ] Python performance — profiling com cProfile, memory_profiler, Cython

---

## 🎯 22. Liderança Técnica e Arquitetural

### Processo e Decisão
- [x] RFC — processo, template, revisão, decisão, aprovação
- [x] ADR — Architecture Decision Record, processo, consequências documentadas
- [ ] OKRs técnicos — alinhamento com produto, métricas de sucesso
- [ ] Tech Debt — Technical Debt Quadrant, identificação, priorização, pagamento incremental
- [ ] Evolutionary Architecture — fitness functions, architecture as code, guardrails

### Cultura e Time
- [ ] Code Review — cultura, checklist técnico, feedback construtivo, async review
- [ ] Mentoria — pair programming, 1:1s, feedback estruturado, crescimento do time
- [ ] Inner Source — Trusted Committers, governança, InnerSource Commons
- [ ] Engineering Excellence — standards de código, linting, CI gates, documentação viva

### Comunicação Técnica
- [x] Documentação — C4 Model, Runbooks, READMEs, API docs, diagramas atualizados
- [ ] Stakeholder Management — apresentação de trade-offs, risco, custo para não-técnicos
- [ ] Pre-mortem — análise antecipada de falhas antes do lançamento
- [ ] Architecture Review — checklist de segurança, performance, operacionalidade

---

## 🔗 23. Domínios de Negócio Especializados

- [ ] FinTech — ledger dupla entrada, idempotência financeira, antifraude, conciliação
- [ ] Billing e Assinatura — Stripe, metered billing, proration, dunning, chargeback
- [ ] E-commerce / Marketplace — catálogo, inventário, checkout, pricing engine, fulfillment
- [ ] Content Management — Headless CMS, versionamento, i18n, media pipeline, slug
- [ ] Gaming Backend — game state autoritativo, matchmaking, tick rate, leaderboard
- [ ] Healthcare — FHIR, HL7, PHI, HIPAA, audit trail imutável
- [ ] EdTech — content delivery, progresso do usuário, certificação, offline support
- [ ] Logistics / Ride-sharing — geolocalização em tempo real, routing, ETA calculation

---

## 🧩 24. Fundamentos de Ciência da Computação

- [ ] Algoritmos e Complexidade — Big-O, P vs NP, algoritmos clássicos
- [ ] Estruturas de Dados — árvores, heaps, grafos, hash maps, tries, skip lists
- [ ] Bloom Filter, HyperLogLog, Count-Min Sketch — estruturas probabilísticas
- [ ] Sistemas Operacionais — processos, threads, scheduling, memória virtual, I/O
- [ ] Compiladores — AST, type systems, JIT, AOT, GraalVM
- [ ] Regex e Automata — FSM, expressões regulares, custo de backtracking
- [ ] Matemática Discreta — teoria dos grafos, probabilidade, lógica, combinatória

---

> **Prioridade para Solutions Architect**
>
> Se tivesse que ordenar por impacto na carreira:
> 1. System Design (15) — é o que mais aparece em entrevistas e no trabalho real
> 2. Fundamentos de Arquitetura (1) + DDD (2) — base intelectual de todas as decisões
> 3. Sistemas Distribuídos (4) — onde os bugs mais difíceis vivem
> 4. Observabilidade / SRE (16) — sistemas vivos precisam de visibilidade
> 5. Segurança (13) — cada vez mais cobrado como responsabilidade do arquiteto
> 6. Cloud + K8s (12) — onde tudo roda na prática
