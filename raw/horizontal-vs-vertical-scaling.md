---
date: 2026-03-27
tags: [tech-mentor, system-design, escalabilidade, scaling, stateless, auto-scaling]
skill: tech-mentor-system-design/references/system-design.md
level: fundamento
---

# Horizontal vs Vertical Scaling

## Contexto

A primeira decisão de escalabilidade. Tudo que vem depois — sharding, CQRS, mensageria — é consequência de ter escolhido (ou precisado) escalar horizontalmente. A regra base: **vertical primeiro, horizontal quando necessário**.

## Como Funciona

### A Diferença Fundamental

```
Vertical (Scale Up):              Horizontal (Scale Out):

  ┌─────────────────┐             ┌────┐ ┌────┐ ┌────┐
  │  Servidor único │             │ S1 │ │ S2 │ │ S3 │
  │  32 cores       │             │ 4c │ │ 4c │ │ 4c │
  │  256 GB RAM     │             └────┘ └────┘ └────┘
  │  10 TB SSD      │                  Load Balancer
  └─────────────────┘                  distribui tráfego

  Mais potente → mais caro         Mais instâncias → escala linear
  Limite físico existe             Limite é o quanto você paga
  Zero mudança no código           Exige serviços stateless
```

### O Pré-requisito do Horizontal: Stateless

Você não pode escalar horizontalmente um serviço que guarda estado local.

```typescript
// ❌ Stateful — não escala horizontalmente
const sessions: Map<string, Session> = new Map(); // em memória

app.post("/login", (req, res) => {
  const session = createSession(req.body);
  sessions.set(session.id, session); // fica só nesse processo
  res.cookie("sid", session.id);
});

app.get("/profile", (req, res) => {
  const session = sessions.get(req.cookies.sid);
  // Se o LB rotear para outro servidor → sessão não existe
  if (!session) return res.status(401).send("Unauthorized");
});

// ✅ Stateless — escala para N instâncias
app.post("/login", async (req, res) => {
  const session = createSession(req.body);
  await redis.set(`session:${session.id}`, JSON.stringify(session), "EX", 3600);
  res.cookie("sid", session.id);
});

app.get("/profile", async (req, res) => {
  const session = await redis.get(`session:${req.cookies.sid}`);
  // Qualquer instância consegue resolver — estado está no Redis
  if (!session) return res.status(401).send("Unauthorized");
});
```

**Regra:** estado vai para fora do processo — Redis para sessão/cache, banco para persistência, S3 para arquivos.

## Código de Referência

### Banco de Dados — Estratégia em Camadas

Adicionar instâncias da aplicação é fácil — o problema é que todas apontam para o mesmo banco.

```
10 instâncias da aplicação
         ↓
    PostgreSQL único
    (agora é o gargalo)
```

**Ordem correta de ataque:**

```
1. Índices              → resolve 80% dos problemas de leitura lenta
2. Cache (Redis)        → tira carga de leitura do banco
3. Read Replicas        → escala reads sem tocar no código
4. Vertical no banco    → mais RAM = mais cache de páginas no PostgreSQL
5. Connection Pool      → PgBouncer antes de escalar o banco
6. Sharding             → último recurso, quando tudo acima não basta
```

### Auto Scaling — Horizontal Automático

```yaml
# Kubernetes HorizontalPodAutoscaler
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: api-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: api
  minReplicas: 2      # mínimo para HA
  maxReplicas: 20     # teto de custo
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70   # escala quando CPU > 70%
```

**Cold start é o problema do auto scaling:**
- Manter `minReplicas: 2` — nunca desce a zero
- Scale up agressivo (antecipa a demanda), scale down conservador (aguarda estabilizar)
- `readinessProbe` — LB só envia tráfego quando a instância está pronta

## Trade-offs

| Aspecto | Vertical | Horizontal |
|---|---|---|
| **Complexidade** | Zero — muda o tamanho da instância | Alta — LB, stateless, consistência |
| **Custo** | Linear até certo ponto, depois exponencial | Linear por instância |
| **Disponibilidade** | SPOF | HA nativo com N≥2 |
| **Limite** | Hardware físico (~192 cores, ~24TB RAM) | Praticamente ilimitado |
| **Deploy** | Downtime (reinicia a instância) | Rolling update sem downtime |
| **Banco de dados** | Escala bem verticalmente | Requer sharding ou réplicas |

## Quando Usar / Quando Evitar

**Comece sempre vertical:**
- ✅ Produto novo, tráfego imprevisível
- ✅ Banco de dados (PostgreSQL escala muito bem vertical)
- ✅ Quando a equipe não tem experiência com sistemas distribuídos

**Mude para horizontal quando:**
- ✅ Disponibilidade é requisito (SLA > 99.9%)
- ✅ Deploy sem downtime é obrigatório
- ✅ Tráfego tem picos imprevisíveis (auto scaling)
- ✅ Vertical chegou no limite de custo/hardware

**Nunca escale horizontalmente sem antes:**
- ❌ Garantir que o serviço é stateless
- ❌ Ter um LB na frente
- ❌ Validar que o banco aguenta N conexões simultâneas (PgBouncer)

## Conceitos Relacionados

[[fase-2-escalabilidade]] · [[load-balancer]] · [[cache]] · [[banco-de-dados]] · [[db-sharding]] · [[connection-pooling]]

---
*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-03-27*
