---
date: 2026-03-27
tags: [tech-mentor, system-design, infraestrutura, load-balancer, rede, escalabilidade]
skill: tech-mentor-system-design/references/system-design.md
level: fundamento
---

# Load Balancer

## Contexto

Load Balancer distribui tráfego entre múltiplas instâncias de um serviço. Sem ele, escalar horizontalmente é impossível — você teria que apontar o DNS para um único servidor, criando um SPOF. É o componente que transforma N servidores em um sistema coeso.

## Como Funciona

```
Sem LB:                        Com LB:
                                              ┌── App Server 1
Client → App Server 1         Client → LB ───┼── App Server 2
(único ponto de falha)                        └── App Server 3
```

### L4 vs L7 — A Divisão Fundamental

**L4 — Transport Layer (TCP/UDP)**

Opera com IP + porta. Não lê o conteúdo da requisição — é um túnel inteligente.

- Mais rápido (menos processamento)
- Funciona com qualquer protocolo sobre TCP/UDP
- Não roteia por URL, header ou cookie
- Exemplo AWS: NLB (Network Load Balancer)

**L7 — Application Layer (HTTP/HTTPS)**

Lê e entende o payload HTTP. Decisões baseadas em URL, headers, cookies, método.

- Roteamento por path, host, header
- SSL termination, compressão, autenticação
- Mais lento (descriptografa TLS + parseia HTTP)
- Exemplo AWS: ALB (Application Load Balancer), Nginx, Traefik

| Cenário | L4 | L7 |
|---|---|---|
| Alta performance, baixa latência | ✅ | — |
| Roteamento por path/subdomínio | — | ✅ |
| Protocolos não-HTTP (gRPC raw, MQTT) | ✅ | — |
| Microsserviços com múltiplos serviços | — | ✅ |

### Algoritmos de Distribuição

**Round-robin** — sequência circular. Simples, ignora carga real dos servidores.

**Least connections** — servidor com menos conexões ativas. Melhor para workloads heterogêneos onde o tempo de resposta varia.

**IP hash** — mesmo IP sempre vai para o mesmo servidor. Útil para sessões sem cache distribuído. Problema: hotspot se o servidor cair.

**Weighted** — servidores mais potentes recebem proporcionalmente mais tráfego. Útil para canary release ou instâncias com capacidades diferentes.

**Least response time** — combina conexões ativas + tempo de resposta médio. Versão mais sofisticada do least connections.

## Código de Referência

### Health Check — O Coração do LB

```typescript
app.get("/health", async (req, res) => {
  try {
    await db.raw("SELECT 1");   // banco acessível?
    await redis.ping();         // cache acessível?
    res.json({ status: "ok" });
  } catch (err) {
    res.status(503).json({ status: "degraded", error: err.message });
  }
});
```

**Liveness vs Readiness** (Kubernetes):
- **Liveness**: "o processo está vivo?" → se falhar, reinicia o container
- **Readiness**: "está pronto para receber tráfego?" → se falhar, remove do LB sem reiniciar

```yaml
livenessProbe:
  httpGet:
    path: /health/live
    port: 8080
  periodSeconds: 10

readinessProbe:   # crítico para zero-downtime deploy
  httpGet:
    path: /health/ready
    port: 8080
  periodSeconds: 5
```

### Alta Disponibilidade do LB

O LB em si pode ser SPOF. Solução: múltiplos LBs com IP flutuante (VIP):

```
              ┌── LB Primary (ativo)    ─┐
DNS → VIP ────┤                           ├── App Servers
              └── LB Secondary (standby) ─┘

Se o primary cai, o VIP migra automaticamente para o secondary.
Tecnologias: keepalived + VRRP | AWS ALB (HA gerenciado, built-in)
```

### LB em Microsserviços (dois níveis)

**Edge LB — externo:**
```
Internet → ALB → API Gateway → Serviços internos
```

**Internal LB — service-to-service:**
```
# Client-side via service discovery
Order Service → descobre instâncias do Payment via Consul/K8s DNS
             → distribui entre elas no cliente (sem LB intermediário)

# Via service mesh
Order Service → Envoy sidecar → Payment Service (qualquer instância)
```

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---|---|---|
| **Round-robin** | Simples, sem overhead | Ignora carga real — hotspot possível |
| **Least connections** | Distribuição justa sob carga variável | Overhead de contagem de conexões |
| **IP hash / Sticky** | Estado sem cache distribuído | Hotspot, falha perde sessão |
| **L7** | Roteamento inteligente, SSL termination | Mais lento que L4 |
| **L4** | Alta performance, agnóstico de protocolo | Sem visibilidade do conteúdo |

## Quando Usar / Quando Evitar

**Sticky sessions** — não use por padrão. Armazene estado fora dos servidores:
- Sessões → Redis
- Autenticação → JWT stateless

Sticky cria hotspot e quebra a premissa de que qualquer servidor atende qualquer request.

**L4 vs L7**: prefira L7 para HTTP/HTTPS (90% dos casos). Use L4 para protocolos binários, UDP, ou quando latência < 1ms é crítica.

## Conceitos Relacionados

[[fase-1-fundamentos-infraestrutura]] · [[dns]] · [[cdn]] · [[service-mesh]] · [[zero-downtime-deploy]]

---
*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-03-27*
