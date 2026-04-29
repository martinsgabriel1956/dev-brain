---
date: 2026-04-14
tags: [tech-mentor, arquitetura, organizacao, liderança]
skill: tech-mentor-system-design/references/organizacao
level: arquiteto
---

# Conway's Law

## Contexto

> "Any organization that designs a system will produce a design whose structure is a copy of the organization's communication structure."
> — Melvin Conway, 1967

Conway's Law é uma observação empírica, não uma teoria prescritiva. Ela diz que o design de um sistema tende a espelhar os canais de comunicação da organização que o produz. Para arquitetos, isso é uma das forças mais subestimadas em qualquer projeto de grande escala.

## Como Funciona

### A Lei na Prática

Se três times separados constroem um compilador, o compilador vai ter três etapas. Se dois times divididos por frontend/backend constroem uma feature, haverá uma API no meio — mesmo quando ela seria desnecessária.

```
Organização:                Sistema resultante:
┌─────────────────┐         ┌─────────────────┐
│  Time Frontend  │         │   SPA React     │
├─────────────────┤    →    ├─────────────────┤
│   Time Backend  │         │   REST API      │
├─────────────────┤         ├─────────────────┤
│   Time de DB    │         │  Database Layer │
└─────────────────┘         └─────────────────┘
```

O acoplamento técnico reflete o acoplamento organizacional. Isso explica por que migrações puramente técnicas (ex: "vamos para microsserviços") sem mudança organizacional geralmente resultam em um **monolito distribuído**.

### Inverse Conway Maneuver

A implicação estratégica: se você quer um determinado design de sistema, organize o time em torno desse design *antes* de implementá-lo.

```
Objetivo: microsserviços por domínio

Passo 1 — Organize times por domínio (não por função técnica):
  ├── Time Orders   (backend + frontend + dados)
  ├── Time Payments (backend + frontend + dados)
  └── Time Catalog  (backend + frontend + dados)

Passo 2 — Cada time constrói seu serviço de ponta a ponta
  → A arquitetura emergente naturalmente segue a divisão de domínio
```

**Erro comum:** criar um "time de microsserviços" centralizado que constrói infraestrutura para outros times. Resultado: um monolito de infraestrutura com microsserviços simulados.

### Team Topologies

O framework de Matthew Skelton e Manuel Pais formaliza a Inverse Conway Maneuver em quatro tipos de time:

| Tipo | Responsabilidade | Interação com outros |
|---|---|---|
| **Stream-aligned** | Entrega de valor por domínio (a maioria dos times) | Colaboração, X-as-a-Service |
| **Enabling** | Ajuda stream-aligned a adquirir capacidades | Colaboração temporária |
| **Complicated Subsystem** | Conhecimento especializado (ex: ML, criptografia) | X-as-a-Service |
| **Platform** | IDP — reduz carga cognitiva dos stream-aligned | X-as-a-Service |

A ideia central: reduzir **carga cognitiva** dos times de entrega. Times com muita carga cognitiva produzem sistemas com muitos acoplamentos acidentais.

### Comunicação e Acoplamento

A lei implica que **cada interface entre times cria uma interface técnica**. Quanto mais você forçar dois times a colaborar intensamente, mais componentes compartilhados e acoplamentos emergirão entre seus sistemas.

```
Alta colaboração → Shared Kernel, APIs internas, DB compartilhado
Baixa colaboração → Published Language, eventos, contratos estáveis
```

Para limitar acoplamento técnico: limite a frequência e o canal de comunicação entre times.

## Trade-offs

| Aspecto | Implicação para Arquitetos |
|---|---|
| **Reorganização** | Mudança de estrutura de times precede mudança de arquitetura |
| **Fronteiras de serviço** | Boundaries técnicas devem alinhar com boundaries de time |
| **Monolito distribuído** | Ocorre quando os times estão acoplados mas os serviços são separados |
| **Plataforma** | Time de plataforma serve outros como produto — não como camada técnica central |

## Quando Usar / Quando Evitar

**Aplicar quando:**
- Redesenhando arquitetura para microsserviços ou modular
- Diagnosticando por que uma arquitetura "bonita no papel" não funciona na prática
- Decidindo como dividir times em crescimento
- Avaliando por que o acoplamento técnico persiste apesar de refatorações

**Cuidados:**
- Conway's Law descreve o que *acontece*, não o que *deve* acontecer — use conscientemente
- Pequenas empresas com um time só: a lei ainda se aplica, mas as implicações são menores
- Reorganizar times tem custo humano alto — deve ser uma decisão deliberada, não táctica

## Conceitos Relacionados

[[microsservicos]] · [[bounded-context]] · [[monolito-modular]] · [[event-driven-architecture]]

---
*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-04-14*
