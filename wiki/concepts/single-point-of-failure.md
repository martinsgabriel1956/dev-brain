---
type: concept
title: "Single Point of Failure (SPOF)"
aliases: ["spof", "ponto único de falha", "single point of failure"]
date_created: 2026-08-10
date_updated: 2026-08-24
source_count: 2
tags: [system-design, spof, alta-disponibilidade, resiliencia, arquitetura, escalabilidade]
skill: tech-mentor-system-design
status: stub
---

# Single Point of Failure (SPOF)

Qualquer componente cuja falha, sozinha, derruba o sistema inteiro. É o conceito organizador por trás da maior parte das decisões de escala e resiliência: **eliminar SPOFs** é o motivo pelo qual se adiciona redundância (múltiplos servidores, réplicas de banco, load balancer em par ativo-passivo).

## O SPOF como fio condutor da escala

No desenho incremental "de zero a milhões de usuários", cada evolução da arquitetura existe para remover um SPOF ou destravar o gargalo que ele criava:

- **Servidor único** → é SPOF: se cai, a aplicação cai. Resolve-se com **múltiplos servidores** ([[escalabilidade-horizontal]]) atrás de um [[load-balancer]].
- **Banco único** → vira o próximo SPOF e gargalo. Resolve-se com [[replicacao-de-banco|replicação]]: um banco de escrita + réplicas de leitura, com **promoção** de uma réplica caso o primário caia.
- **Cache única** → também é SPOF: exige política de invalidação e uma aplicação que **tolere a cache indisponível** (degradar para o banco).
- **Load balancer** → não pode ser SPOF: usa-se par active-passive com VIP (Virtual IP).

O padrão se repete: mover estado para fora do servidor ([[stateless]]) é o que permite que qualquer instância seja substituível, tornando a redundância eficaz.

## Relação com outros conceitos

- [[escalabilidade-vertical]] — escalar "para cima" mantém o servidor único como SPOF; é o limite que motiva a escala horizontal
- [[escalabilidade-horizontal]] — redundância de instâncias é a forma direta de eliminar o SPOF de servidor
- [[replicacao-de-banco]] — remove o SPOF da camada de dados via réplicas + failover/promoção
- [[load-balancer]] — quem distribui carga entre instâncias redundantes; ele próprio não pode ser SPOF
- [[stateless]] — pré-requisito para que instâncias sejam intercambiáveis

## Key Sources

- [[wiki/sources/escalar-para-um-milhao-de-usuarios]] — SPOF como fio condutor do desenho incremental: servidor único → múltiplos servidores + LB; banco único → replicação + promoção de réplica; cache como SPOF que exige invalidação e tolerância a indisponibilidade
- [[wiki/sources/escalando-aplicacao-zero-a-um-milhao-usuarios-renato-augusto]] — mesma progressão de eliminação de SPOF, com um nível adicional explícito: o data center inteiro como SPOF de nível mais alto, resolvido replicando toda a arquitetura em um segundo data center/região
