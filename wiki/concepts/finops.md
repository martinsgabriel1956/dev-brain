---
type: concept
title: "FinOps — Cost-Aware Architecture"
aliases: ["finops", "cloud cost", "unit economics", "cost optimization"]
date_created: 2026-04-23
date_updated: 2026-08-03
source_count: 4
tags: [finops, cloud-cost, unit-economics, right-sizing, spot-instances, egress, aws]
skill: tech-mentor-infra
status: stub
---

# FinOps

Prática de tratar custo de cloud como variável de engenharia — não só responsabilidade do financeiro.

**Métrica correta:** custo por unidade de negócio (por transação, por usuário ativo) — não custo absoluto. Crescer receita 2x com custo 1.5x é sucesso.

**Hierarquia de otimização:**
1. Arquitetura (maior impacto) — batch vs realtime, storage tier
2. Right-sizing — CPU/memória adequados ao workload real
3. Modelo de pricing — Reserved vs On-demand vs Spot
4. Otimizações pontuais (menor impacto)

**Batch vs Realtime:** maior decisão de custo — processar S3 em batch é 10–100x mais barato que stream.

**Egress:** o custo invisível mais subestimado — transferência entre AZs e para internet.

**Storage hierárquico:** Hot (S3) → Warm (S3 IA) → Cold (Glacier) economiza ~80% em dados raramente acessados.

**CI/CD:** Infracost integrado na pipeline mostra custo por PR antes do merge.

## Gastar Mais Pode Ser Otimizar Custo

Contra-intuitivo mas central: às vezes a decisão de menor custo é *aumentar* recurso. Exemplo didático: uma loja virtual fora do ar por 1h perde R$ 1 milhão em receita; dobrar de 10 para 20 servidores custa R$ 100 mil a mais — o resultado líquido é um ganho de R$ 900 mil (perda evitada − custo extra), não um gasto adicional. A métrica correta nesse caso não é "quanto gastei a mais", é "quanto deixei de perder". Isso amarra FinOps diretamente ao [[wiki/concepts/planejamento-de-capacidade]] — a otimização de custo depende dos mesmos dados de observabilidade que definem o dimensionamento.

## Desperdício por Degrau Forçado de Instância

Em cloud providers, o próximo tier de instância geralmente é o dobro do anterior — não dá para adicionar um número "quebrado" de CPU/memória. Um monolito não modularizado que só precisava de um pouco mais de capacidade acaba pagando por uma instância inteira dobrada, com boa parte ociosa. Ver [[wiki/concepts/escalabilidade-vertical]] para o mecanismo completo.

## RTO Como Justificativa de Custo, Não Só Detalhe Técnico

Reforço direto do exemplo acima ("gastar mais pode ser otimizar custo"), agora do lado da recuperação: um site que fatura ~$1.000/minuto perde ~$120 mil em receita se o [[wiki/concepts/rto|RTO]] for de duas horas. Isso significa que o RTO tolerável de um sistema não é uma escolha técnica isolada — é uma decisão de custo, exatamente como escalar de 10 para 20 servidores é uma decisão de custo. Ver [[wiki/sources/rto-rpo-recovery-time-point-objective]].

## Key Sources

- [[sources/finops-cost-aware-architecture]]
- [[wiki/sources/sre-capacidade-observabilidade-confiabilidade-custo]] — otimização de custo como "gastar mais para perder menos"; ligação com planejamento de capacidade
- [[wiki/sources/escalabilidade-horizontal-vertical-custo-grafico]] — exemplo gráfico de desperdício quando escalar verticalmente força dobrar o tier da instância
- [[wiki/sources/rto-rpo-recovery-time-point-objective]] — custo de downtime ($/minuto) como justificativa direta para o RTO tolerável de uma arquitetura
