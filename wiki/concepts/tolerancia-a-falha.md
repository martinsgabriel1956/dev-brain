---
type: concept
title: "Tolerância a Falha (Fault Tolerance)"
aliases: ["FT", "Fault Tolerance", "fault-tolerant", "ativo-ativo"]
date_created: 2026-08-03
date_updated: 2026-08-03
source_count: 1
tags: ["tolerancia-a-falha", "alta-disponibilidade", "failover", "cluster", "arquitetura", "infra"]
skill: tech-mentor-infra
status: stub
---

# Tolerância a Falha (Fault Tolerance / FT)

Propriedade de um sistema onde múltiplos nós operam **ativos em paralelo** (topologia ativo-ativo), de forma que a queda de um nó ou datacenter inteiro não interrompe o serviço de forma perceptível — não há uma janela de failover porque não existe promoção primário→secundário: o lado saudável já estava servindo tráfego e com os mesmos dados replicados desde antes da falha.

## Distinção de [[wiki/concepts/alta-disponibilidade|Alta Disponibilidade (HA)]]

| | HA (ativo-passivo) | FT (ativo-ativo) |
|---|---|---|
| Topologia | Nó primário + nó(s) secundário(s) em standby | Todos os nós ativos, servindo carga em paralelo |
| Durante a falha | Existe uma janela de indisponibilidade até o failover (promoção do secundário) | Sem janela perceptível — o lado saudável já estava ativo |
| Exemplo típico | Base de dados primária/secundária com failover (MySQL Cluster, Suse/Redhat Cluster) | Nós idênticos ("server A, server A, server A"), cada um persistindo os mesmos dados com clone ativo no outro datacenter |
| Custo | Moderado | Estruturalmente superior — exige tecnologia e engenharia de replicação capazes de sustentar ativo-ativo |

Fonte: [[wiki/sources/ha-vs-ft-alta-disponibilidade-tolerancia-a-falha]] — a aula não nomeia formalmente "ativo-passivo"/"ativo-ativo"; esses termos foram inferidos na wiki para tornar a distinção citável, mas a mecânica descrita (primária/secundária com switch de carga vs. nós idênticos com clone permanente) corresponde exatamente a esse par de topologias.

## FT Não é 100% de Disponibilidade

Mesmo em FT, uma escrita em andamento no exato momento da queda de um datacenter ainda falha para o usuário (erro pontual) — a garantia é que o **retry imediato** já é atendido pelo lado saudável, não que nenhum erro jamais ocorre. Isso distingue FT de uma promessa de disponibilidade absoluta.

## Por que FT é Mais Caro

O custo estrutural mais alto de FT vem de dois fatores, segundo a fonte:

1. **Tecnologia**: o banco de dados (ou mecanismo de replicação) precisa suportar de fato dados consistentes em múltiplos nós ativos simultaneamente — não é toda base de dados que suporta essa garantia nativamente.
2. **Engenharia**: a seleção da base de dados e o desenho da topologia precisam ser feitos especificamente para tolerar a falha, não apenas para sobreviver a ela após um switch.

## Relação com Outros Conceitos

- [[wiki/concepts/alta-disponibilidade]] — FT é uma forma mais forte (e mais cara) de disponibilidade; HA já documentado com a distinção adicional entre Multi-AZ e Multi-Region (Disaster Recovery), que opera em outro eixo (escopo geográfico) além do eixo ativo-passivo vs. ativo-ativo desta página.
- [[wiki/concepts/cluster]] — os exemplos citados na fonte (MySQL Cluster, Suse Cluster, Redhat Cluster) são implementações concretas de cluster que podem viabilizar tanto HA quanto FT, dependendo da topologia configurada.
- [[wiki/concepts/replicacao-de-banco]] — o mecanismo de "clone" ativo entre datacenters na fonte é replicação; em FT a réplica já está servindo tráfego, não é apenas standby.
- [[wiki/concepts/cap-theorem]] — em aberto: a fonte não detalha como a consistência é mantida entre nós ativo-ativo escrevendo em paralelo.

## Key Sources

- [[wiki/sources/ha-vs-ft-alta-disponibilidade-tolerancia-a-falha]]
