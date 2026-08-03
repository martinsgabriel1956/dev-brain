---
type: source
title: "HA vs FT — Alta Disponibilidade vs Tolerância a Falha"
aliases: ["HA vs FT", "High Availability vs Fault Tolerance"]
date_created: 2026-08-03
date_updated: 2026-08-03
source_count: 0
tags: ["alta-disponibilidade", "tolerancia-a-falha", "failover", "cluster", "arquitetura", "infra"]
skill: tech-mentor-infra
status: stable
source_file: "raw/ha-vs-ft-alta-disponibilidade-tolerancia-a-falha.md"
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-08-03
---

# HA vs FT — Alta Disponibilidade vs Tolerância a Falha

## TL;DR

Aula curta em português (transcrição, sem necessidade de tradução) que distingue duas propriedades comumente confundidas: **Alta Disponibilidade (HA)** tolera uma janela de indisponibilidade durante o failover — o sistema "cai" brevemente e depois volta —, enquanto **Tolerância a Falha (FT)** mantém o serviço operando de forma contínua porque múltiplos nós ativos já servem a mesma carga em paralelo, sem depender de uma promoção primário→secundário para se recuperar. A diferença central não está na tecnologia em si, mas na topologia ativo-passivo (HA) vs. ativo-ativo (FT) e no custo — FT é estruturalmente mais caro.

## Key Claims

1. **HA é "altamente disponível", não "sempre disponível".** O sistema tem uma indisponibilidade mensurável durante eventos de falha — a métrica pode ser 95%, 99,9% etc., mas nunca 100%.
   - Evidência: *"a ideia do alta disponibilidade é que ele é altamente disponível [...] talvez ele seja 95% de disponível, mas não 99,9 ou quase próximo dos 100%."*

2. **No exemplo de HA dado, a topologia é ativo-passivo com failover no banco.** Dois datacenters recebem tráfego 50/50 nos servidores de aplicação (que rodam a mesma versão), mas a base de dados tem uma primária e uma secundária — se a primária cai, existe uma janela de indisponibilidade até o switch de carga (failover) se completar.
   - Evidência: *"a minha base de dados 1 [...] está fazendo um failover se necessário, então aqui ela seria uma base primária e aqui a minha secundária [...] existe uma indisponibilidade para eu fazer esse switch de carga."*

3. **FT usa topologia ativo-ativo: todos os nós são iguais e já operam em paralelo.** Cada nó persiste os mesmos dados e existe uma réplica (clone) constantemente ativa do outro lado — não é uma promoção pós-falha, é redundância operando desde antes da falha.
   - Evidência: *"todos os servidores [...] Eles são todos iguais [...] eu persisto Os mesmos dados nesse DB 1 [...] e aí ele existe um clone para o outro lado [...] mesmo que eu tenha uma indisponibilidade nesse datacenter, [...] ainda vou continuar operando porque eu tenho uma réplica ali."*

4. **FT não é 100% de disponibilidade — é ausência de downtime perceptível ao usuário, não ausência de erro pontual.** Uma escrita em andamento no exato momento da queda do datacenter ainda falha (o usuário recebe um erro), mas o retry imediato já cai no lado saudável.
   - Evidência: *"Eu não estou falando que é 100% de disponibilidade aqui [...] com certeza Ele receberia um erro, mas quando ele tentasse de novo, ele já ia cair para o outro lado e o banco de dados estaria ali em pé."*

5. **FT custa estruturalmente mais que HA**, tanto em tecnologia (bancos de dados e mecanismos de replicação capazes de sustentar ativo-ativo) quanto em engenharia (seleção de banco precisa suportar essa garantia).
   - Evidência: *"quando a gente começa a falar de tolerância a falha, a gente começa a pensar em aumento de custo [...] o custo é bem superior [...] o tipo de tecnologia que você vai ter que ter, ela é superior."*

## Entities

Nenhuma entidade nomeada (pessoa, empresa, produto) — aula genérica/didática, sem menção a ferramentas específicas de mercado (ex: não cita Patroni, Aurora, etc. nominalmente, apenas "MySQL Cluster", "Suse Cluster", "Redhat Cluster" como exemplos genéricos de categoria).

## Concepts

- [[wiki/concepts/alta-disponibilidade]]
- [[wiki/concepts/tolerancia-a-falha]] (novo)
- [[wiki/concepts/cluster]]
- [[wiki/concepts/replicacao-de-banco]]
- [[wiki/concepts/robustez-de-sistemas]]
- [[wiki/concepts/sre]]
- [[wiki/concepts/cap-theorem]]

## Open Questions

- A fonte não detalha *como* a topologia ativo-ativo resolve consistência entre os nós que escrevem em paralelo (ela assume "eu persisto os mesmos dados", sem entrar em consenso/replicação síncrona vs. assíncrona) — fica em aberto a relação explícita com [[wiki/concepts/cap-theorem]].
- Não há menção a RTO/RPO nem a Disaster Recovery — a fonte cobre a distinção HA/FT dentro de uma única região/par de datacenters, não o eixo região inteira já documentado em [[wiki/concepts/alta-disponibilidade]] (seção HA vs. DR).
- "Failover" é usado tanto para o mecanismo de promoção (HA) quanto para a réplica já ativa (FT) — a aula não nomeia formalmente os termos "ativo-passivo" e "ativo-ativo"; essa nomeação foi inferida na wiki para tornar a distinção citável.

## Raw Quotes

> "Existem formas de você fazer uma alta disponibilidade, mas vamos dizer assim, um sistema de tolerância falha. Aí ele já tolera. Toleraria, né? A falha."

> "Note, quando a gente fala de tolerância, falhas, o custo com certeza é bem superior, porque o tipo de tecnologia que você vai ter que ter, ela é superior."

## Key Sources (páginas que citam esta fonte)

—
