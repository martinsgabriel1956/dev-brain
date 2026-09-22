---
type: entity
title: "Nubank"
aliases: ["Nu", "Nu Holdings", "Nu Bank"]
date_created: 2026-05-31
date_updated: 2026-09-15
source_count: 4
tags: [nubank, fintech, banco-digital, clojure, datomic, event-sourcing, iso-27001, security, cell-based-architecture, observabilidade]
skill: tech-mentor-backend
status: stable
---

# Nubank

## TL;DR

Maior banco digital da América Latina. 122 milhões de clientes (Brasil, México, Colômbia — dado de 2025). Fundado ~2013. Pioneiro no uso de [[clojure]], [[datomic]] e [[concepts/event-sourcing]] em escala de banco de varejo, motivado pelo paper "Out of the Tar Pit" e pela necessidade de eliminar [[complexidade-acidental]]. Além da fundação em Clojure/Datomic, opera hoje com 4.000+ microsserviços particionados em 20 shards via [[wiki/concepts/cell-based-architecture|Scalability Units]], e construiu observabilidade própria ([[wiki/entities/alexandria-nubank|Alexandria]]) por custo de escala.

## Perfil

- **Sede:** São Paulo, Brasil
- **Fundação:** ~2013
- **Clientes:** 122 milhões (Brasil, México, Colômbia — 2025; era reportado como 100 milhões em fontes anteriores desta wiki)
- **Produtos:** conta digital, cartão de crédito, pagamentos, investimentos
- **Escala de infraestrutura (2025):** 4.000+ microsserviços, 72 bilhões de eventos Kafka/dia, 20 shards no Brasil, 600 TB de logs/dia, 450 milhões de eventos antifraude/dia

## Decisões Técnicas Fundamentais

| Decisão | Escolha | Motivação |
|---------|---------|-----------|
| Linguagem principal | [[clojure]] | Funcional, imutável, JVM |
| Banco de dados | [[datomic]] | Imutável, time-travel, auditoria |
| Arquitetura | [[concepts/event-sourcing]] + [[concepts/cqrs]] + [[ddd]] | Eliminar complexidade acidental |
| Framework | Interno (não público) | Controle total de threads e GC |
| Sharding | [[wiki/concepts/cell-based-architecture\|Scalability Units]] (clone de infra completa, não só do banco) | Sharding de banco sozinho parou de bastar em 2016 — AWS chegou a ficar sem máquinas para o ritmo de crescimento |
| Observabilidade | [[wiki/entities/alexandria-nubank\|Alexandria]] (construída internamente) | Solução de logs terceirizada ficou financeiramente inviável na escala do banco |

## Escala e Autorização de Transação (dado de 2025)

Autorização de transação de cartão precisa responder em menos de 100ms ponta a ponta (maquininha → adquirente → bandeira → Nubank → resposta). O time de engenharia reduziu a latência crítica desse caminho de ~10.000ms para **288ms no P90** (redução de 76%), removendo dependências síncronas do caminho crítico: em vez de buscar dados em tempo real, o sistema **precomputa e materializa** as informações necessárias no momento da escrita, deixando a leitura como um único lookup em datastore de baixa latência — [[wiki/concepts/cqrs|CQRS]] aplicado à latência do caminho crítico. Ver [[wiki/sources/nubank-arquitetura-escala-122-milhoes-clientes]].

A plataforma antifraude processa 450 milhões de eventos/dia, dividida em detecção (regras manuais + ML — regra simples classificando como suspeita evita rodar o modelo de ML) e ação (bloquear/alertar/deixar passar). Um orquestrador refatorado para modelo DAG (grafo acíclico dirigido — cada componente espera só pelos dados que precisa) reduziu a latência de 550ms para 350ms em fluxos complexos.

## Contexto das Escolhas

O CTO do Nubank leu o paper *"Out of the Tar Pit"* antes de construir o banco. A conclusão foi direta: para construir um banco que sobrevivesse a escala de varejo, era necessário eliminar [[imutabilidade|estado mutável]] e [[efeitos-colaterais]] desde o início.

A escolha de [[datomic]] veio da pergunta: "E o banco de dados? Como ter um banco imutável?" — Datomic resolve isso com um log append-only e time-travel nativo.

## Segurança e Compliance

Possui certificação [[wiki/concepts/iso-27001]], usada como garantia formal a investidores e reguladores de que os dados de mais de 100 milhões de clientes estão protegidos. O recurso "modo rua" do app — que limita transações quando o usuário sai de uma rede Wi-Fi segura — é citado como exemplo de controle de acesso contextual alinhado aos controles de segurança móvel e acesso lógico da norma.

## Key Sources

- [[wiki/sources/nubank-clojure-datomic-event-sourcing]]
- [[wiki/sources/iso-27001-dicionario-programador]] — certificação ISO 27001 e "modo rua" como controle de acesso contextual
- [[wiki/sources/cqrs-event-sourcing-full-cycle-wesley-williams]] — citado como caso de uso do Datomic ao explicar Event Sourcing
- [[wiki/sources/nubank-arquitetura-escala-122-milhoes-clientes]] — números de 2025 (122M clientes, 4.000 microsserviços, 20 shards), Scalability Units, otimização da latência de autorização de transação (10.000ms → 288ms P90), plataforma antifraude (450M eventos/dia, DAG), Alexandria (observabilidade in-house)
