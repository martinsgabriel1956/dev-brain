---
date: 2026-03-29
tags: [tech-mentor, system-design, avançado, finops, custo, arquitetura]
skill: tech-mentor-system-design/references/architecture-ops
level: arquiteto
---

# FinOps e Cost-Aware Architecture

## Contexto

Custo de infraestrutura é uma dimensão arquitetural, não um problema de operações. Decisões de design têm implicações de custo que, ignoradas, transformam um produto tecnicamente correto em inviável financeiramente. FinOps é a prática de tratar custo como first-class concern — da mesma forma que performance e disponibilidade.

O cenário típico: startup escala, infra cresce junto sem revisão, e em algum momento o CEO pergunta por que a conta AWS é R$ 80k/mês para um produto com 10k usuários.

---

## Unit Economics — A Métrica Certa

Não analise custo absoluto. Analise **custo por unidade de valor entregue**.

```
Custo por transação = infra_mensal ÷ transações_mensais

Exemplo:
  R$ 5.000/mês de infra, 1M transações = R$ 0,005/transação
  Margem por transação = R$ 0,50
  Ratio custo/receita = 1% → saudável

Ao adicionar feature de processamento em tempo real:
  + Lambda: R$ 0,0001/invocação × 100K = R$ 10/mês
  + RDS read replica: R$ 500/mês
  → Custo aumenta 10% para servir 10% mais volume
  → Custo por transação não mudou → feature viável

Contra-exemplo:
  + Elasticsearch cluster para busca full-text: R$ 1.200/mês
  → Busca usada por 2% dos usuários
  → Custo por busca = R$ 1.200 ÷ 20.000 buscas = R$ 0,06/busca
  → Vale? Depende do valor da busca para retenção
```

**Implicação prática**: toda decisão arquitetural que tem custo relevante deve ser acompanhada de uma estimativa de unit economics. "Vamos colocar em Kafka" sem saber o volume de eventos por dia e o custo por evento é decisão cega.

---

## Hierarquia de Otimização de Custo

Sempre nessa ordem — otimizar o errado é desperdício de engenharia:

```
1. Arquitetura  → a maior alavanca. Batch vs realtime, cache vs query, tier de storage
2. Right-sizing → instância certa para o workload
3. Pricing model → Reserved vs On-demand vs Spot
4. Configuração → compressão, TTL, lifecycle rules
```

Nunca pular para o nível 3 sem revisar o nível 1. Comprar Reserved Instance de uma EC2 superprovisionada é economizar 40% sobre um desperdício.

---

## Decisões Arquiteturais com Lente de Custo

| Decisão | Opção cara | Opção econômica | Trade-off |
|---|---|---|---|
| **Compute** | On-demand 24/7 | Spot + fallback On-demand | Tolerância a interrupção |
| **Storage** | S3 Standard para tudo | Hot/Warm/Cold (Standard → IA → Glacier) | Latência de acesso |
| **Processamento** | Lambda por evento unitário | Batch off-peak em Spot instances | Latência de resultado |
| **Cache** | Redis Cluster multi-AZ | Redis single-AZ + fallback | Disponibilidade |
| **DB** | RDS Multi-AZ em todos os ambientes | Multi-AZ prod, Single-AZ dev/staging | RPO/RTO em não-prod |
| **Egress** | Replicação cross-region frequente | Agregar antes de transferir | Latência de dados |
| **Queries** | Query full-table a cada request | Cache de resultado com TTL | Freshness dos dados |

### Batch vs Realtime — a decisão de maior impacto de custo

```
Realtime (Lambda por evento):
  100M eventos/mês × $0,0000002/ms × 100ms = $2.000/mês
  Mais: API Gateway, VPC, logs = +$500/mês

Batch off-peak (ECS/Fargate Spot, 2h por dia):
  1 job/dia × 2h × $0,01268/vCPU-hora × 4 vCPU = $3,68/mês
  Redução: ~98%

Critério de decisão: o resultado precisa estar disponível em < 1 minuto?
  Sim → realtime ou near-realtime (micro-batch a cada 5min)
  Não → batch off-peak
```

---

## Right-Sizing

Superprovisionamento por medo é o desperdício mais comum. Instâncias rodando a 10% de CPU média pagam pelo pico que nunca acontece.

```
Análise de utilização (últimas 2 semanas):
  CPU média < 20%  → downsizing possível
  CPU pico > 80%   → undersized (risco de performance)
  Memória < 30%    → tipo de instância errado (memória é cara)

Ferramentas:
  AWS: Compute Optimizer → recomendações automáticas de right-sizing
  GCP: Recommender → mesma funcionalidade
  Azure: Advisor
  Todos: CloudHealth, Spot.io para visão multi-cloud
```

**Exemplo prático**:
```
Situação atual: m5.xlarge (4 vCPU, 16GB RAM), $140/mês
  CPU média: 12%, pico: 35%
  Memória média: 8GB

Recomendação: t3.large (2 vCPU, 8GB RAM), $60/mês
  Economia: $80/mês por instância
  Risco: burst workloads — t3 usa créditos de CPU; monitorar CPU Credit Balance
```

---

## Modelo de Pricing — Reserved vs On-demand vs Spot

```
On-demand:    preço cheio, sem compromisso
              Use para: carga imprevisível, novo workload não compreendido ainda

Reserved:     1 ou 3 anos de compromisso → 40-60% desconto
              Use para: baseline previsível (servidores de API, banco de dados)

Spot:         capacidade ociosa da AWS → até 90% desconto
              Pode ser interrompido com 2 minutos de aviso
              Use para: workers stateless, batch jobs, CI/CD runners, ML training
```

### Arquitetura Spot-aware

Para usar Spot com segurança, a aplicação precisa ser projetada para interrupção:

```
[Job Queue (SQS)] → [Worker Pool em Spot]
                          ↓
                    Recebe interruption notice (2min de aviso da AWS)
                          ↓
                    Checkpoint: salva progresso no S3/DB
                    Drain: para de pegar novos jobs
                    Graceful shutdown
                          ↓
                    Nova instância Spot assume
                    Retoma do checkpoint
```

```typescript
// Detectar interruption notice (polling do metadata endpoint)
async function checkSpotInterruption(): Promise<boolean> {
  try {
    const response = await fetch(
      "http://169.254.169.254/latest/meta-data/spot/interruption-action",
      { signal: AbortSignal.timeout(100) }
    );
    return response.status === 200; // 404 = sem interrupção
  } catch {
    return false;
  }
}

// Loop de worker com checkpoint
async function runWorker() {
  while (true) {
    if (await checkSpotInterruption()) {
      await saveCheckpoint();
      process.exit(0); // drain limpo
    }
    await processNextJob();
  }
}
```

### Estratégia de composição

```
Baseline (sempre ligado, previsível) → Reserved Instances (1 ano)
Capacidade normal (variável, tolerante) → On-demand
Bursts e batch jobs → Spot com fallback On-demand
```

---

## FinOps no CI/CD — Custo por PR

Impacto de custo visível no processo de revisão, não só na fatura do mês:

```yaml
# .github/workflows/infracost.yml
name: Infracost
on: [pull_request]

jobs:
  infracost:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: infracost/actions/setup@v2
        with:
          api-key: ${{ secrets.INFRACOST_API_KEY }}

      - name: Generate cost diff
        run: infracost diff --path=terraform/ --format=json --out-file=/tmp/infracost.json

      - name: Post comment on PR
        uses: infracost/actions/comment@v2
        with:
          path: /tmp/infracost.json
          behavior: update
          # Resultado no PR: "Esta mudança aumenta o custo em +$127/mês"
```

PR que adiciona um RDS Multi-AZ ou um ElastiSearch cluster mostra o custo antes de mergear. Decisão com informação, não surpresa.

---

## Storage Hierárquico — O Maior Ganho por Esforço

Storage hierárquico é a otimização com maior ROI na maioria dos sistemas. Dados frios custam 10-20× mais quando ficam em S3 Standard.

```
S3 Standard:     $0,023/GB/mês  → dados acessados frequentemente (< 30 dias)
S3 Standard-IA:  $0,0125/GB/mês → dados acessados ocasionalmente (30 dias – 1 ano)
S3 Glacier IR:   $0,004/GB/mês  → dados raramente acessados, retrieval em ms
S3 Glacier:      $0,0036/GB/mês → arquivamento, retrieval em horas
S3 Deep Archive: $0,00099/GB/mês → retenção regulatória, retrieval em 12h
```

**S3 Intelligent-Tiering**: move automaticamente entre camadas baseado no padrão de acesso. Custo extra de $0,0025/1k objetos monitorados. Vale quando o padrão de acesso é imprevisível.

```json
// Lifecycle rule — mover automaticamente para tiers mais baratos
{
  "Rules": [{
    "Status": "Enabled",
    "Transitions": [
      { "Days": 30,  "StorageClass": "STANDARD_IA" },
      { "Days": 90,  "StorageClass": "GLACIER_IR" },
      { "Days": 365, "StorageClass": "GLACIER" }
    ],
    "Expiration": { "Days": 2555 }  // deletar após 7 anos (compliance)
  }]
}
```

---

## Egress — O Custo Invisível

Transferência de dados para fora da AWS (egress) é cara e frequentemente esquecida no design.

```
Intra-região (mesmo AZ):    grátis
Inter-AZ (mesma região):    $0,01/GB  ← frequentemente ignorado
Inter-região:               $0,02/GB
Internet (egress):          $0,09/GB  (primeiros 10TB)
```

**Implicações de design**:
```
Replicação de banco cross-region:
  10M writes/dia × 1KB = 10GB/dia × $0,02 = $0,20/dia = $73/ano
  Tolerável.

Stream de eventos cross-region (Kafka Mirror):
  100M eventos/dia × 5KB = 500GB/dia × $0,02 = $10/dia = $3.650/ano
  Agregar antes de replicar reduz 10-50×.

CDN vs servir do origin:
  Servir 100TB/mês de vídeo do S3 diretamente: $9.000/mês
  CloudFront (CDN): $850/mês (precio diferenciado de egress)
  + cache hit rate alta → requisições ao origin reduzidas → ainda mais barato
```

---

## Observabilidade de Custo

```
Tagging obrigatório em todos os recursos:
  team: checkout
  environment: production
  service: order-processor
  cost-center: engineering

Alertas de anomalia:
  AWS Cost Anomaly Detection → alerta quando custo de um serviço
  sobe >X% em comparação à semana anterior

Dashboard por equipe:
  Cada time vê o custo de seus recursos → ownership de custo
  "O time de checkout gastou $X este mês, alta de 15% vs mês anterior"
```

---

## Checklist de Cost Review Arquitetural

Antes de colocar qualquer componente novo em produção:

```
[ ] Qual é o unit economics? (custo por unidade de negócio)
[ ] O workload é previsível? → Reserved ou On-demand?
[ ] Tem tolerância a interrupção? → Spot candidato
[ ] Dados têm padrão de acesso decrescente? → Lifecycle policy no S3
[ ] Há egress cross-region? → Quanto/mês?
[ ] O resultado precisa ser realtime? → Batch off-peak como alternativa?
[ ] A instância está right-sized para o workload real?
[ ] O custo vai aparecer no PR via Infracost?
```

---

## Conceitos Relacionados

[[observabilidade]] · [[horizontal-vs-vertical-scaling]] · [[cdn]] · [[cache]] · [[multi-region-global-lb]] · [[zero-downtime-deploy]]

---

*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-03-29*
