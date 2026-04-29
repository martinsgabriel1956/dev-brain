---
date: 2026-03-29
tags: [tech-mentor, system-design, avançado, cap, pacelc, consistência, distribuído]
skill: tech-mentor-system-design/references/distributed-systems-core
level: arquiteto
---

# CAP Theorem, PACELC e Modelos de Consistência

## Contexto

Todo sistema distribuído enfrenta a mesma realidade física: redes falham, nós ficam offline, e mensagens se perdem. CAP e PACELC são frameworks para raciocinar sobre as consequências dessas falhas nas propriedades do sistema. Sem entender esses modelos, decisões de escolha de banco, protocolo de replicação e design de API são feitas no escuro.

---

## CAP Theorem

Em presença de uma **partição de rede** (P), você é obrigado a escolher entre:

- **Consistency (C)**: todos os nós veem o mesmo dado ao mesmo tempo. Leitura sempre retorna o write mais recente.
- **Availability (A)**: o sistema sempre responde. Pode retornar dado desatualizado, mas nunca recusa a resposta.

**P não é opcional.** Redes distribuídas sempre podem particionar — é uma propriedade física, não de design. A escolha real é **CP vs AP**.

```
      C
     / \
    /   \
   CP   CA  ← CA não existe em sistemas distribuídos reais
    \   /       (P é inevitável)
     \ /
      P ───── AP
```

### Exemplos reais

| Sistema | Escolha | Consequência prática |
|---|---|---|
| PostgreSQL, MySQL | **CP** | Pode recusar writes durante partição para manter consistência |
| Cassandra, DynamoDB | **AP** | Pode retornar dado desatualizado; nunca rejeita a operação |
| ZooKeeper, etcd | **CP** | Para de responder se quorum não é atingido; usado para coordenação crítica |
| CockroachDB, Spanner | **CP** | Consensus global, latência maior, consistência forte |

### O que acontece na prática

**CP durante partição**:
```
Node A e Node B partiram (não se comunicam)
Write em Node A: Node A recusa — não consegue garantir que B vai ver
Leitura em A: retorna dados, mas pode bloquear até quorum

Resultado: sistema disponível para leitura, pode recusar escrita
Use case: saldo bancário, inventário, reservas
```

**AP durante partição**:
```
Node A e Node B partiram
Write em Node A: aceita, persiste localmente
Write em Node B: aceita, persiste localmente (valores podem divergir!)
Quando partição cura: sistema reconcilia (última escrita vence, ou merge)

Resultado: sempre responde, dado pode estar stale
Use case: feed de redes sociais, contadores de likes, carrinho não-crítico
```

---

## PACELC — A Extensão Necessária do CAP

CAP só fala sobre o que acontece durante partições. Mas partições são raras — a maioria do tempo o sistema está funcionando normalmente. **PACELC** estende o modelo para o caso normal:

> **P**artition → **A** ou **C** (como CAP)
> **E**lse (sem partição) → **L**atency ou **C**onsistency

```
PACELC:

Com partição: escolhe A ou C (= CAP)
Sem partição: escolhe L (baixa latência) ou C (consistência forte)

Consistência forte sem partição = quorum reads/writes = latência maior
Baixa latência = local reads/writes = pode retornar dado stale
```

### Classificação PACELC dos sistemas reais

| Sistema | Com partição | Sem partição | Classificação |
|---|---|---|---|
| DynamoDB (eventual) | Disponibilidade | Latência | PA/EL |
| DynamoDB (strong) | Disponibilidade | Consistência | PA/EC |
| Cassandra | Disponibilidade | Latência | PA/EL |
| HBase | Consistência | Consistência | PC/EC |
| PostgreSQL | Consistência | Consistência | PC/EC |
| MongoDB (default) | Disponibilidade | Latência | PA/EL |

**Implicação prática**: sistemas PA/EL são mais rápidos em condições normais — reads locais sem coordenação. Sistemas PC/EC sempre coordenam (quorum), pagando latência mesmo sem partição.

Para a maioria dos SaaS: **PA/EL** é a escolha certa — alta disponibilidade e baixa latência com eventual consistency são aceitáveis.

---

## Modelos de Consistência

Do mais forte ao mais fraco:

### Linearizability (Strong Consistency)

Leitura sempre retorna o write mais recente. O sistema parece ter um único nó — mesmo que tenha dezenas de réplicas.

```
Thread 1: Write(x=1) [confirmado]
Thread 2: Read(x) → sempre 1

Qualquer leitura após um write confirmado vê esse write
```

**Custo**: quorum em cada operação — todas as réplicas (ou maioria) precisam confirmar antes de retornar. Latência proporcional à rede mais lenta do quorum.

**Use quando**: saldo bancário, deduplicação de pagamentos, inventário crítico, leader election.

### Sequential Consistency

Operações aparecem em alguma ordem global consistente, mas não necessariamente em tempo real. Threads diferentes podem ver ordens diferentes, desde que a ordem por thread seja preservada.

Mais relaxado que linearizability, mas ainda forte o suficiente para a maioria dos casos de uso.

### Causal Consistency

Operações causalmente relacionadas são vistas na ordem correta. Operações sem relação causal podem ser vistas em ordens diferentes por nós diferentes.

```
A escreve x=1
B lê x=1 (causalidade: B viu o write de A)
B escreve y=2 (causalmente dependente de x=1)

Qualquer nó que vê y=2 também deve ver x=1
Mas nós que não viram x=1 podem ver y=2 sem x=1 (sem causalidade direta)
```

**Usado em**: sistemas de colaboração, comentários em threads (respostas sempre aparecem após o post original).

### Read-Your-Writes

Você sempre lê o que acabou de escrever. Outros usuários podem não ver ainda.

```
Usuário edita perfil → Write(name="João Silva")
Usuário recarrega a página → Read(name) = "João Silva" (garantido)
Outro usuário pode ainda ver "João" por alguns ms
```

**Implementação**: redirecionar reads do mesmo usuário para o primary durante janela de tempo após um write. Sessão sticky ao primary.

### Eventual Consistency

O sistema converge para o estado correto, mas não imediatamente. Dado período sem conflitos e novas escritas, todas as réplicas convergem.

```
Write(x=1) no Node A
Node B pode retornar x=0 por alguns ms/s
Após convergência: todos os nós retornam x=1
```

**Custo de complexidade**: cliente precisa lidar com dados stale. Conflitos de escrita simultânea precisam de resolução (last-write-wins, CRDTs, merge functions).

**Use quando**: feed de redes sociais, contadores não-críticos, cache, histórico de atividade.

---

## Mecanismos de Convergência (Sistemas AP)

Sistemas AP com eventual consistency precisam de mecanismos para garantir que réplicas divergentes eventualmente se reconciliem.

### Read Repair

Na leitura com quorum, o coordenador detecta divergência entre réplicas e envia a versão mais recente para as desatualizadas.

```
Leitura com quorum 2/3:
  Réplica 1: { name: "João", version: 3 }
  Réplica 2: { name: "João Silva", version: 5 }  ← mais recente

Coordenador retorna version=5 ao cliente
Em background: envia version=5 para Réplica 1
```

### Anti-Entropy com Merkle Trees

Processo background que compara réplicas sistematicamente. Divide dados em buckets, constrói hash tree — compara apenas raízes para detectar divergência, depois navega a árvore para localizar exatamente quais buckets diferem. O(log N) comparações para N registros.

### Hinted Handoff

Quando uma réplica está offline, o coordenador guarda as escritas com "hints" e entrega quando a réplica volta. Reduz janela de divergência.

---

## Vector Clocks — Rastreando Causalidade

Como detectar se duas escritas são concorrentes (conflito) ou causalmente relacionadas (uma gerou a outra), sem um clock global confiável.

Cada nó mantém um vetor com o contador de todos os outros nós:

```
Sistema com 3 nós: A, B, C
Estado inicial: A=[0,0,0], B=[0,0,0], C=[0,0,0]

A processa evento:    A=[1,0,0]
A envia para B:       B=[1,1,0]  (incorpora conhecimento de A)
B envia para C:       C=[1,1,1]  (C sabe tudo que todos processaram)

Detectar conflito:
  V1=[2,1,0] vs V2=[1,2,0]
  V1[0]=2 > V2[0]=1 → V1 tem eventos que V2 não tem
  V1[1]=1 < V2[1]=2 → V2 tem eventos que V1 não tem
  → CONFLITO: escritas concorrentes, precisam ser mergeadas
```

**Usado em**: DynamoDB (internamente), Riak, CRDTs, Git (conceito similar para merge conflicts).

---

## Guia de Decisão

```
Dado financeiro (saldo, pagamento, inventário crítico)?
  → Strong consistency (CP) — PostgreSQL, CockroachDB, Spanner

Dado social não-crítico (feed, likes, contadores)?
  → Eventual consistency (AP) — Cassandra, DynamoDB

Coordenação entre serviços (leader election, locks)?
  → CP com quorum — ZooKeeper, etcd, Redis SET NX

Colaboração em tempo real (docs, comentários encadeados)?
  → Causal consistency + CRDTs

Sessão do usuário (perfil após edição)?
  → Read-your-writes — sticky session ao primary por janela de tempo

Escala global, baixa latência de leitura?
  → PA/EL + réplicas de leitura regionais + eventual consistency aceitável
```

---

## Conceitos Relacionados

[[banco-de-dados]] · [[mensageria]] · [[cache]] · [[distributed-locks-raft]] · [[cqrs]] · [[event-sourcing]]

---

*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-03-29*
