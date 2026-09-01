---
type: source
title: "Event Sourcing — Conceito, Prós, Contras e Cases de Mercado"
aliases: ["Event Sourcing ARQ", "Event Sourcing prós e contras"]
date_created: 2026-09-01
date_updated: 2026-09-01
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/event-sourcing-conceito-pros-contras-cases-mercado.md
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-09-01
source_count: 0
tags: [event-sourcing, arquitetura, cqrs, saga, auditoria, lgpd, kafka, martin-fowler, telecomunicacoes]
skill: tech-mentor-system-design
status: stable
---

# Event Sourcing — Conceito, Prós, Contras e Cases de Mercado

## TL;DR

Vídeo didático em português (canal/autor não identificado, apresentador se dirige ao público como "ARQ") introduzindo Event Sourcing do zero para arquitetos: define o padrão (persistir a trajetória de eventos que levou um objeto a um estado, em vez do estado em si), a regra de **só insert, nunca update/delete**, e ilustra com um exemplo concreto de modelagem de tabelas `extrato`/`account`/`saldo` — inclusive uma variante "leve" do padrão (histórico via insert + flag `enabled`, sem event store/streaming completo). Depois desenha a arquitetura completa com APIs → microsserviços → streaming (Kafka ou similar) → banco transacional, e um componente dedicado a registrar eventos e outro a "replayar" eventos de volta na fila para reprocessamento. Fecha com prós (reprodutibilidade total, auditoria, troubleshooting), contras (volume de dados/infra, complexidade de código, tempo de desenvolvimento) e quatro cases reais de mercado onde o apresentador diz já ter aplicado o padrão: Saga, opt-in/LGPD, auditoria de segurança em operações financeiras, e faturamento de telecomunicações (fiscalização Anatel).

## Claims Principais

| Claim | Confiança |
|---|---|
| Event Sourcing persiste a trajetória (eventos) que levou um objeto a um estado, em vez do estado atual diretamente — o padrão é atribuído a Martin Fowler | Alta — consistente com [[wiki/concepts/event-sourcing]] e [[wiki/entities/martin-fowler]], embora Fowler não seja o único ou o primeiro a formalizar o padrão (Greg Young é mais citado como origem em [[wiki/sources/cqrs-event-sourcing-full-cycle-wesley-williams]]) |
| Regra fundamental: Event Sourcing só funciona com inserts — nunca update, nunca delete; mudança de estado é sempre um novo registro | Alta — idêntica à regra de append-only já registrada em [[wiki/concepts/event-sourcing]] |
| Existe uma variante "leve" do padrão: manter uma tabela só-insert com campos `enabled`/`state_date`, mudando o registro anterior para `enabled=false` em vez de fazer update de valor — dá rastro histórico sem implementar Event Sourcing por completo (sem event store dedicado, sem streaming) | Média — não documentado em nenhuma outra fonte já ingerida; é uma proposta pragmática do próprio autor, plausível mas não uma definição formal do padrão |
| Arquitetura completa: APIs → microsserviços coreografados ouvindo uma fila/streaming (Kafka ou equivalente, tratado como "black box" — não precisa ser Kafka) → um componente dedicado grava cada mudança de estado tanto no banco de eventos/streaming quanto num banco SQL transacional, serializando o objeto de domínio | Alta — consistente com o desenho de EventStore + streaming já documentado em `references/event-sourcing-cqrs.md` (skill tech-mentor-system-design) |
| Para reprocessar/auditar, um componente separado lê o evento do banco e o relança na fila no estado daquele momento passado, fazendo os microsserviços reexecutarem as ações — reproduzindo exatamente o que aconteceu no passado | Alta — é a mecânica de event replay, já documentada em [[wiki/sources/system-design-copa-do-mundo-tempo-real-kafka-event-sourcing-renato-augusto]] motivada por bug de cálculo financeiro |
| Prós: reprodutibilidade total (a ponto de poder dropar o banco e reconstruir tudo a partir dos eventos), auxílio forte em auditoria (ex.: CMMI) e em troubleshooting | Alta |
| Contras: aumento de volume de dados/custo de infraestrutura (backup, processamento), aumento de complexidade de código (mais componentes arquiteturais, mais pontos de falha, exige muito log), e maior tempo de desenvolvimento/manutenção | Alta — consistente com o trade-off já central em [[wiki/concepts/event-sourcing]] (❌ times sem experiência em DDD, complexidade alta) |
| Case de mercado — **Saga**: para aplicar o padrão Saga em microsserviços sem transação de banco garantida, é necessário aplicar Event Sourcing (total ou parcialmente) para as transações, permitindo desfazer em caso de falha no fluxo | Alta — consistente com [[wiki/concepts/saga-pattern]], que já lista compensação/rollback como mecanismo central |
| Case de mercado — **Opt-in/LGPD**: Event Sourcing é citado como ideal para manter histórico de mudanças de consentimento do cliente e fazer broadcast confiável dessas mudanças para parceiros (cobrança, marketing), com garantia registrada de quando e como o pedido foi feito | Média — plausível e consistente com os requisitos gerais de auditoria de [[wiki/concepts/compliance]] e [[wiki/concepts/audit-log]], mas sem uma fonte técnica detalhada de implementação; é relato de experiência do apresentador, não um case nomeado publicamente |
| Case de mercado — **Auditoria de segurança financeira**: o apresentador relata ter implementado Event Sourcing depois de uma empresa sofrer uma auditoria sem os dados necessários, especificamente para operações financeiras/transferências | Baixa — relato de experiência pessoal do autor, sem nome de empresa ou verificação externa |
| Case de mercado — **Telecomunicações (Anatel)**: faturas de operadoras de telecom/TV a cabo são um uso "batido" de Event Sourcing; segundo o apresentador, das "várias" empresas de telecom em que trabalhou, apenas duas aplicaram o padrão corretamente, e essas conseguiram justificar rapidamente à Anatel o porquê de cada lançamento/estado do cliente | Baixa — relato de experiência pessoal, números não verificáveis ("só duas", "trabalhei em vários") |
| Não existe bala de prata em arquitetura — a decisão de usar Event Sourcing deve pesar prós e contras, e não deve ser aplicada a toda a solução, só onde necessário (ex.: parte financeira/transacional) | Alta — princípio geral já recorrente na wiki em fontes de arquitetura |

## Entidades

- [[wiki/entities/martin-fowler]] — citado como um dos fundadores do padrão Event Sourcing (referência aos posts do bliki)

## Conceitos

- [[wiki/concepts/event-sourcing]]
- [[wiki/concepts/cqrs]] — vídeo recomenda assistir a um conteúdo anterior do canal sobre CQRS
- [[wiki/concepts/saga-pattern]]
- [[wiki/concepts/kafka]]
- [[wiki/concepts/compliance]] — caso de uso opt-in/LGPD
- [[wiki/concepts/audit-log]]

## Open Questions

- Autor/canal do vídeo não identificado — a fala se dirige ao público como "ARQ" (abreviação de "arquiteto"), padrão de endereçamento não visto em nenhuma outra fonte já ingerida na wiki; nenhuma entidade foi criada para o autor por falta de confirmação.
- Os três cases pessoais (opt-in/LGPD, auditoria financeira, telecom/Anatel) são relatos de experiência do apresentador sem nome de empresa, métricas ou fonte externa verificável — tratados como confiança baixa/média, mas mantidos porque ilustram aplicações plausíveis e consistentes com a literatura já registrada.
- A variante "leve" do padrão (insert + flag `enabled`, sem event store) não tem nome formal na literatura de Event Sourcing consultada até agora — vale investigar se corresponde a algum padrão já nomeado (ex.: soft-delete temporal, slowly changing dimension tipo 2 em modelagem de dados).

## Contradições com a Wiki Existente

Nenhuma contradição direta. Um ponto de tensão leve, não uma contradição: esta fonte atribui a origem/fundamento do padrão a **Martin Fowler**, enquanto [[wiki/sources/cqrs-event-sourcing-full-cycle-wesley-williams]] atribui a criação do CQRS (e a ideia complementar de Command Sourcing) a **Greg Young** — ambas as atribuições podem coexistir (Fowler documentou/popularizou via bliki; Young é mais citado como o praticante/teórico original do par CQRS+Event Sourcing na comunidade DDD), mas nenhuma fonte já ingerida cita Fowler como o "criador" de Event Sourcing propriamente — só como quem descreveu/nomeou o padrão em seu bliki. Registrado como nuance em [[wiki/entities/martin-fowler]], não como contradição.

## Citações Brutas Preservadas

> "Event Sourcing é um padrão de projeto que visa, ao invés de você persistir os dados diretamente do banco o estado atual [...] persistir toda a trajetória que levou aquele objeto a chegar aquele status."

> "Para isso tudo funcionar, ele precisa trabalhar somente com inserts — nunca com updates, nunca com deletes. É sempre a inserção."

> "O event sourcing serve para basicamente duas coisas: a primeira é para que você tenha a capacidade de desfazer as coisas que aconteceram no passado [...] a segunda finalidade é você conseguir ter o histórico."

> "Muitas vezes, se você precisar simplesmente ter histórico das coisas [...] ao invés de você aplicar o event sourcing na sua plenitude, você pode simplesmente alterar o seu modelo de dados."

> "Escolher errado aqui vai custar caro [...] esforço de desenvolvimento a mais, componentes arquiteturais a mais [...] também não é para colocar em tudo dentro de uma única solução."

## Key Sources (páginas que citam esta fonte)

- [[wiki/concepts/event-sourcing]]
- [[wiki/concepts/saga-pattern]]
- [[wiki/concepts/cqrs]]
- [[wiki/concepts/kafka]]
- [[wiki/concepts/compliance]]
- [[wiki/entities/martin-fowler]]
