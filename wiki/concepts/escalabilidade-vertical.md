---
type: concept
title: "Escalabilidade Vertical"
aliases: ["vertical scaling", "scale up", "upgrade de servidor"]
date_created: 2026-06-26
date_updated: 2026-08-03
source_count: 4
tags: [system-design, escalabilidade, infra, performance, tradeoff]
skill: tech-mentor-system-design
status: draft
---

# Escalabilidade Vertical

Tornar um único servidor **mais potente**: mais CPU, mais RAM, mais disco, mais rede. Também chamado de *scale up*.

## Vantagens

- **Simplicidade** — é só uma máquina; sem complexidade de distribuição, sem Load Balancer, sem sincronização
- O código não precisa saber que existe mais de uma máquina — nenhuma mudança arquitetural
- Fácil de operar no início do ciclo de vida do produto

## Desvantagens

| Problema | Detalhe |
|---|---|
| **Custo não-linear** | 2× capacidade pode custar 3–4×; 4× capacidade pode custar 10× |
| **Teto físico** | O maior servidor do mundo ainda é só uma máquina — não existe RAM infinita |
| **Single point of failure** | Se o servidor cair, nenhum usuário acessa o app até ele reiniciar |

## Quando Usar

- Estágio inicial do produto — simples, barato, funciona
- Banco de dados legacy que não foi projetado para distribuição (primeiro passo antes de replicação ou sharding)
- Cargas que não justificam a complexidade operacional de escalabilidade horizontal

## Granularidade de Cloud Provider Força Desperdício

Em cloud providers, o próximo tier de instância geralmente é **o dobro** do anterior — não é possível adicionar um número "quebrado" de CPU/memória. Isso torna o custo não-linear ainda pior na prática: um monolito centralizado que precisa só de um pouco mais de capacidade é obrigado a dobrar a instância inteira, ficando com uma fração ociosa de CPU/RAM paga mas não usada. Comparar com [[wiki/concepts/finops]] — right-sizing é justamente a prática de calibrar o tier real necessário contra esse degrau forçado.

Vertical online (aumentar CPU/memória sem desligar) existe via hypervisor há bastante tempo, mas a redução online é rara na prática, e o caso comum ainda envolve indisponibilidade — refresh da aplicação, reboot, stop/start, dependendo do hypervisor ou cloud provider.

## Quando Migrar para Horizontal

- O servidor maior começa a custar desproporcionalmente
- O teto físico está próximo
- O SLA exige alta disponibilidade (single point of failure se torna risco inaceitável)

## Relação com outros conceitos

- [[escalabilidade-horizontal]] — a alternativa com trade-off inverso: mais complexidade, sem teto
- [[gargalo]] — vertical resolve gargalos de CPU/RAM mas não de throughput ilimitado
- [[sharding]] — quando vertical não é suficiente para banco de dados, sharding é o próximo passo

## Key sources

- [[wiki/sources/escalabilidade-vertical-horizontal-system-design]]
- [[wiki/sources/escalabilidade-horizontal-load-balancer-algoritmos]] — reforça que escalar horizontalmente só faz sentido depois de esgotar a vertical
- [[wiki/sources/10-conceitos-fundamentais-backend]] — vertical descrita como "colocar uma máquina mais potente com mais CPU mais memória mais capacidade na mesma instância"
- [[wiki/sources/escalabilidade-horizontal-vertical-custo-grafico]] — exemplo gráfico de desperdício quando cloud provider força dobrar o tier da instância; vertical online existe via hypervisor mas redução é rara e indisponibilidade ainda é o caso comum
