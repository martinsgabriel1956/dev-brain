---
date: 2026-03-30
tags: [tech-mentor, security, threat-modeling, stride, pasta, dfd, attack-trees]
skill: tech-mentor-security/references/threat-modeling
level: intermediário
---

# Threat Modeling

## Contexto

Threat modeling é o processo de identificar ameaças a um sistema **no design**, antes de construir. É fundamentalmente diferente de pentest — pentest testa o que já foi feito, threat modeling evita que o problema exista.

O custo de corrigir uma vulnerabilidade no design é ordens de magnitude menor do que em produção. Regulatórias como PCI-DSS e ISO 27001 exigem threat modeling documentado. E mais importante: força o time a pensar nos adversários reais em vez de assumir que o sistema não será atacado.

**4 perguntas que toda sessão responde**:

```
1. O que estamos construindo?      → Diagrama do sistema (DFD ou C4)
2. O que pode dar errado?          → Identificação de ameaças
3. O que fazemos a respeito?       → Mitigações e controles
4. Fizemos um bom trabalho?        → Validação e revisão
```

---

## STRIDE — Framework da Microsoft

Categoriza ameaças em 6 tipos, mapeados para propriedades de segurança e mitigações típicas.

| Letra | Ameaça | Viola | Mitigação típica |
|---|---|---|---|
| **S**poofing | Fingir ser outro ator | Autenticação | MFA, mTLS, certificados |
| **T**ampering | Modificar dados em trânsito ou em repouso | Integridade | HMAC, assinaturas digitais, TLS |
| **R**epudiation | Negar ter realizado uma ação | Não-repúdio | Audit log imutável, assinatura digital |
| **I**nformation Disclosure | Expor dados a quem não deveria ver | Confidencialidade | Criptografia, access control |
| **D**enial of Service | Tornar o sistema indisponível | Disponibilidade | Rate limiting, auto-scaling, WAF |
| **E**levation of Privilege | Ganhar permissões além do permitido | Autorização | Least privilege, RBAC rigoroso |

### Como aplicar STRIDE

Pegue cada elemento do DFD (processos, data stores, data flows, external entities) e aplique as 6 categorias sistematicamente: "pode haver Spoofing neste data flow? Tampering neste data store?"

**Exemplo — API de login**:

| STRIDE | Ameaça concreta | Mitigação |
|---|---|---|
| Spoofing | Brute force de credenciais | Rate limiting (5 tentativas / 15min) + account lockout |
| Tampering | JWT manipulado com role elevada | Assinatura RS256, validação de algoritmo explícita |
| Repudiation | Usuário nega ter feito login | Log com IP, timestamp, user-agent — imutável |
| Information Disclosure | Password visível em stack trace | Nunca logar inputs de auth, sanitizar erros |
| Denial of Service | Flood de requests no endpoint | WAF + rate limit por IP + CAPTCHA |
| Elevation of Privilege | Token de user comum acessa /admin | RBAC rigoroso, verificação em cada endpoint |

---

## PASTA — Process for Attack Simulation and Threat Analysis

Framework de 7 estágios orientado a risco de negócio. Mais completo que STRIDE — adequado para sistemas críticos, compliance enterprise ou avaliação de sistema inteiro.

| Estágio | Pergunta | Output |
|---|---|---|
| 1. Define Objectives | Quais são os objetivos de segurança do negócio? | Risk profile |
| 2. Define Technical Scope | Quais componentes estão no escopo? | Architecture diagram |
| 3. App Decomposition | Como o sistema processa dados? | DFD, use cases |
| 4. Threat Analysis | Quais ameaças existem no ambiente? | Threat library |
| 5. Vulnerability Analysis | Onde o sistema é vulnerável? | Vulnerability list |
| 6. Attack Modeling | Como um atacante exploraria isso? | Attack trees |
| 7. Risk/Impact Analysis | Qual o impacto real? | Risk register |

**Quando usar STRIDE vs PASTA**:
- **STRIDE**: sessões rápidas (2–4h), times de desenvolvimento, features específicas
- **PASTA**: projetos críticos, compliance, avaliação de sistema inteiro (8h+)

---

## Data Flow Diagram (DFD) — Base para Threat Modeling

Toda sessão começa com um DFD. Sem um diagrama do sistema, o threat modeling é superficial.

**Elementos**:
```
Processo        (círculo)           → transforma dados — ex: Auth Service
Data Store      (retângulo duplo)   → persiste dados — ex: PostgreSQL, Redis
External Entity (retângulo)         → ator externo — ex: Browser, Mobile App
Data Flow       (seta)              → dados em movimento — ex: JWT Token
Trust Boundary  (linha tracejada)   → onde o nível de confiança muda
```

**Toda seta que cruza uma trust boundary é um vetor potencial de ataque.**

```
┌─────────────────────────────────────────────────────────────────┐
│  INTERNET (untrusted)                                           │
│                                                                 │
│  [Browser] ──── HTTPS request ──── ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ │
│                                   ↓ trust boundary             │
├─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─┤
│  DMZ / Load Balancer                                            │
│                 ↓                                               │
├─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─┤
│  APP ZONE (trusted)                                             │
│                                                                 │
│  (Auth Service) ──── JWT ────▶ (API Service)                   │
│       │                              │                          │
│       ▼                              ▼                          │
│  ═══ Session DB ══              ═══ Postgres ══                 │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

Cada cruzamento de boundary recebe análise STRIDE completa.

---

## Attack Trees

Representação gráfica do raciocínio do atacante. A raiz é o objetivo; as folhas são os vetores de exploração.

```
[GOAL: Roubar dados de cartão de crédito]
├── [OR] Comprometer banco de dados
│   ├── SQL Injection na API de busca
│   └── Acesso direto ao DB (credenciais expostas em repositório)
├── [OR] Interceptar tráfego
│   ├── MITM por certificado falso
│   └── Sniffing de rede interna (insider)
└── [OR] Comprometer a aplicação
    ├── [AND] Obter sessão de admin
    │   ├── Phishing do usuário admin
    │   └── Credential stuffing com base de dados vazada
    └── RCE via dependência com CVE crítico
```

- **Nós OR**: qualquer caminho é suficiente para o atacante
- **Nós AND**: o atacante precisa de todas as condições simultâneas

Cada folha recebe um score de: **probabilidade** × **custo de exploração** vs **custo de mitigação**. Priorize mitigações com alto impacto e baixo custo — bloquear o nó pai elimina toda a subárvore.

---

## Trust Boundaries — Onde o Risco Aumenta

Trust boundaries são onde o sistema muda de nível de confiança. Exemplos:

| Boundary | Por quê importa |
|---|---|
| Internet → Load Balancer | Input completamente não confiável — validar tudo |
| Load Balancer → App | Ainda pode ter bypass de WAF — não relaxar validação |
| App → Banco de dados | Credenciais de acesso, SQL injection |
| App → Serviço externo (Stripe, SendGrid) | Dados saindo do seu controle |
| Container → Host | Escape de container, volume mounts |
| Microserviço A → Microserviço B | Autenticação interna — não assumir que é seguro |

**Regra**: nunca assuma confiança por posição na rede. Autentique e valide em cada boundary.

---

## Quando Fazer Threat Modeling

```
✅ Novo sistema sendo desenhado do zero
✅ Nova feature com superfície de ataque significativa:
   autenticação, pagamentos, dados sensíveis, integrações externas
✅ Mudança de infraestrutura: novo cloud, nova rede, novo provider
✅ Antes de releases de alta criticidade
✅ Anualmente para sistemas em produção (revisão)

❌ Para cada PR — é processo de design, não code review
❌ Depois do sistema estar em produção (tarde para mudar design)
```

---

## Output — O Que Documentar

Uma sessão que não gera documento não aconteceu. O output mínimo:

```
1. Diagrama do sistema (DFD Level 1 ou C4 Level 2)
2. Lista de ameaças identificadas com categoria STRIDE
3. Mitigações planejadas — responsável, prazo, status
4. Riscos aceitos — justificativa e owner explícito
5. Data da sessão e próxima revisão prevista
```

Ferramentas: **OWASP Threat Dragon** (open source, diagramas + ameaças), **Microsoft Threat Modeling Tool** (integrado a ADO), **draw.io** com notação DFD manual.

---

## Threat Modeling no SDLC

```
Sprint Planning  → identificar features de alta superfície de ataque
Design Review    → sessão STRIDE (2-4h) com dev + security + produto
Implementation   → mitigações vão para os tickets do sprint
Code Review      → validar que mitigações foram implementadas
Release Gate     → verificar que riscos aceitos têm owner documentado
```

Integrado ao SDLC, o threat modeling deixa de ser um evento isolado e passa a ser parte do processo de design de features.

---

## Trade-offs

| | Vantagem | Desvantagem |
|---|---|---|
| **Fazer** | Encontra problemas antes de construir; documenta decisões | Consome 4–8h por sessão complexa |
| **Não fazer** | Entrega mais rápida no curto prazo | Vulnerabilidades de design são caras de corrigir depois |
| **STRIDE só** | Rápido, qualquer dev consegue aplicar | Pode perder ameaças de negócio |
| **PASTA completo** | Cobre risco de negócio e compliance | Requer facilitador experiente |

**Armadilha mais comum**: fazer threat modeling como "checkbox exercise" para compliance — sessão superficial que não identifica nada real. O valor está em ter pessoas certas na sala (dev + security + produto) com o diagrama real do sistema, não em preencher um template.

---

## Conceitos Relacionados

[[secure-design-patterns]] · [[owasp-top10]] · [[zero-trust]] · [[api-security]] · [[devsecops-pipeline]]

---

*Fonte: tech-mentor skill · tech-mentor-security · 2026-03-30*
