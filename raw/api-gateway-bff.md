---
date: 2026-03-29
tags: [tech-mentor, system-design, arquitetura, api-gateway, bff]
skill: tech-mentor-system-design/references/architecture-foundations
level: arquiteto
---

# API Gateway & BFF

## Contexto

À medida que um sistema cresce — múltiplos serviços internos, múltiplos tipos de cliente (web, mobile, parceiros) — surgem dois problemas distintos:

1. **Borda externa**: quem autentica, roteia, limita taxa e monitora as chamadas que entram no sistema?
2. **Contrato por cliente**: como servir mobile e web de forma diferente sem duplicar lógica de negócio?

API Gateway e BFF são as respostas para esses dois problemas. São camadas diferentes, com responsabilidades diferentes — e frequentemente usadas juntas.

---

## API Gateway

Ponto único de entrada para todo tráfego externo. Fica na borda do sistema, entre clientes e serviços internos.

```
                    ┌─────────────────┐
Clientes externos   │   API Gateway   │
────────────────▶   │                 │   ──▶  Serviços internos
(web, mobile,       │ - Authn/Authz   │
 parceiros)         │ - Rate limiting │
                    │ - Routing       │
                    │ - SSL termination│
                    │ - Logging       │
                    └─────────────────┘
```

**Responsabilidades típicas:**

| Função | O que faz |
|---|---|
| **Autenticação/Autorização** | Valida JWT/API Key antes de chegar nos serviços |
| **Rate limiting** | Limita requisições por cliente/IP/rota |
| **Routing** | `/pedidos/*` → serviço de pedidos, `/pagamentos/*` → serviço de pagamentos |
| **SSL termination** | Decripta HTTPS na borda, serviços internos falam HTTP |
| **Logging/Metrics** | Ponto centralizado para observabilidade de borda |
| **Transformação** | Adapta headers, versiona APIs, converte formatos |
| **Cache** | Cache de respostas para rotas estáticas ou semi-estáticas |

**Exemplos de produtos**: Kong, AWS API Gateway, Traefik, NGINX, Envoy como gateway.

---

## BFF — Backend for Frontend

Um backend dedicado por tipo de cliente. Cada BFF agrega chamadas a serviços internos e entrega exatamente o que aquele cliente precisa — nem mais, nem menos.

```
                          ┌─────────────┐
React Web App ───────────▶│   BFF Web   │──┐
                          └─────────────┘  │
                                           │   ┌───────────────┐
iOS/Android  ────────────▶┌─────────────┐ ├──▶│   Pedidos     │
                          │ BFF Mobile  │──┤   │   service     │
                          └─────────────┘  │   └───────────────┘
                                           │   ┌───────────────┐
Parceiros externos ──────▶┌─────────────┐ ├──▶│  Pagamentos   │
                          │  API Pública│──┘   │   service     │
                          └─────────────┘      └───────────────┘
```

**Problema que resolve**: APIs genéricas viram mínimo denominador comum.

- **Over-fetching**: a API retorna 40 campos, mobile usa 8
- **Under-fetching**: montar uma tela de resumo exige 4 chamadas separadas (pedido + usuário + pagamento + endereço)

O BFF resolve fazendo o aggregation server-side: uma chamada do cliente, múltiplas chamadas internas, resposta formatada para aquela tela.

```typescript
// BFF Mobile — endpoint /home agregado
export async function getHomePage(userId: string) {
  const [usuario, pedidosRecentes, saldo] = await Promise.all([
    usuarioService.buscarPerfil(userId),
    pedidosService.listarRecentes(userId, { limit: 3 }),
    carteiraService.buscarSaldo(userId)
  ]);

  // retorna apenas o que o mobile precisa
  return {
    nomeExibicao: usuario.primeiroNome,
    avatarUrl: usuario.avatarUrl,
    saldoFormatado: formatarMoeda(saldo.valor),
    pedidos: pedidosRecentes.map(p => ({
      id: p.id,
      status: p.status,
      valorTotal: p.valorTotal
    }))
  };
}
```

---

## Trade-offs

### API Gateway

| Aspecto | Vantagem | Desvantagem |
|---|---|---|
| **Centralização** | Authn/AuthZ em um lugar só | Single point of failure se não for HA |
| **Observabilidade** | Métricas de borda centralizadas | Pode mascarar problemas internos |
| **Routing** | Roteamento flexível por rota/método | Configuração pode crescer e virar um monolito de config |
| **Acoplamento** | Desacopla clientes dos serviços internos | Gateway conhece todos os serviços |

### BFF

| Aspecto | Vantagem | Desvantagem |
|---|---|---|
| **Contrato ideal** | Cada cliente recebe exatamente o que precisa | Um BFF por cliente = mais código para manter |
| **Autonomia** | Time de mobile evolui seu BFF sem depender de outros | Risco de lógica de negócio vazar para o BFF |
| **Performance** | Aggregation server-side reduz round-trips | BFF vira gargalo se não for bem dimensionado |
| **Especialização** | Otimizado para o cliente (compressão, cache, formatos) | Duplicação se os clientes tiverem necessidades similares |

---

## Quando Usar / Quando Evitar

### API Gateway — use sempre que:
- Sistema tem mais de 1 serviço exposto externamente
- Autenticação precisa ser centralizada
- Você quer rate limiting, logging e routing em um lugar

### API Gateway — cuidado quando:
- Se tornar um God Gateway: lógica de negócio no gateway é anti-padrão
- Configuração crescer sem versionamento → drift entre ambientes

### BFF — use quando:
- Clientes têm necessidades de dados distintas (mobile vs web vs parceiros)
- Under-fetching/over-fetching são problemas reais de performance
- Times diferentes cuidam de canais diferentes

### BFF — evite quando:
- Clientes têm necessidades idênticas → você tem duplicação sem benefício
- Lógica de negócio está migrando para o BFF → é um sinal de que os serviços internos têm contratos ruins
- Alternativa: **GraphQL** resolve o problema de shape por cliente sem um BFF dedicado

---

## API Gateway vs Service Mesh — Não Confundir

São complementares, não substitutos:

| | API Gateway | Service Mesh |
|---|---|---|
| **Onde vive** | Borda (entrada externa) | Dentro do cluster (tráfego interno) |
| **Tráfego** | Norte-Sul (cliente → sistema) | Leste-Oeste (serviço → serviço) |
| **Responsabilidades** | Authn/Authz, rate limiting, routing | mTLS, circuit breaking, retries, observabilidade |
| **Exemplos** | Kong, AWS API GW, Traefik | Istio, Linkerd, Consul Connect |

**Regra prática**: API Gateway controla o que entra. Service mesh controla o que acontece lá dentro. Em sistemas maduros, ambos coexistem.

---

## Armadilhas Comuns

**1. BFF com lógica de negócio**
O BFF deve ser um aggregator/transformer, não um place de regras de negócio. Se o BFF decide preço, desconto ou valida regras de domínio — as regras estão no lugar errado.

**2. Gateway como proxy burro**
Um API Gateway que só faz proxy sem autenticação, sem rate limiting, sem logging, é um ponto de complexidade sem valor. Configure-o de verdade ou remova-o.

**3. Um BFF para tudo**
Um "BFF" que serve web, mobile e parceiros não é BFF — é uma API genérica com outro nome. O ponto do padrão é a especialização.

**4. Cascata síncrona no BFF**
```typescript
// ❌ sequencial — latência somada
const usuario = await buscarUsuario(id);
const pedidos = await buscarPedidos(id);
const saldo = await buscarSaldo(id);

// ✅ paralelo — latência do mais lento
const [usuario, pedidos, saldo] = await Promise.all([
  buscarUsuario(id),
  buscarPedidos(id),
  buscarSaldo(id)
]);
```

---

## Conceitos Relacionados

[[microservicos-vs-monolito-modular]] · [[service-mesh]] · [[rate-limiting]] · [[distributed-tracing]] · [[circuit-breaker]] · [[observabilidade]]

---

*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-03-29*
