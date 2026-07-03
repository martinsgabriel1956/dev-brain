---
type: entity
title: "Nubank"
aliases: ["Nu", "Nu Holdings", "Nu Bank"]
date_created: 2026-05-31
date_updated: 2026-07-03
source_count: 2
tags: [nubank, fintech, banco-digital, clojure, datomic, event-sourcing, iso-27001, security]
skill: tech-mentor-backend
status: stable
---

# Nubank

## TL;DR

Maior banco digital da América Latina. 100 milhões de clientes. Fundado ~2013. Pioneiro no uso de [[clojure]], [[datomic]] e [[event-sourcing]] em escala de banco de varejo, motivado pelo paper "Out of the Tar Pit" e pela necessidade de eliminar [[complexidade-acidental]].

## Perfil

- **Sede:** São Paulo, Brasil
- **Fundação:** ~2013
- **Clientes:** 100 milhões (América Latina)
- **Produtos:** conta digital, cartão de crédito, pagamentos, investimentos

## Decisões Técnicas Fundamentais

| Decisão | Escolha | Motivação |
|---------|---------|-----------|
| Linguagem principal | [[clojure]] | Funcional, imutável, JVM |
| Banco de dados | [[datomic]] | Imutável, time-travel, auditoria |
| Arquitetura | [[event-sourcing]] + [[cqrs]] + [[ddd]] | Eliminar complexidade acidental |
| Framework | Interno (não público) | Controle total de threads e GC |

## Contexto das Escolhas

O CTO do Nubank leu o paper *"Out of the Tar Pit"* antes de construir o banco. A conclusão foi direta: para construir um banco que sobrevivesse a escala de varejo, era necessário eliminar [[imutabilidade|estado mutável]] e [[efeitos-colaterais]] desde o início.

A escolha de [[datomic]] veio da pergunta: "E o banco de dados? Como ter um banco imutável?" — Datomic resolve isso com um log append-only e time-travel nativo.

## Segurança e Compliance

Possui certificação [[wiki/concepts/iso-27001]], usada como garantia formal a investidores e reguladores de que os dados de mais de 100 milhões de clientes estão protegidos. O recurso "modo rua" do app — que limita transações quando o usuário sai de uma rede Wi-Fi segura — é citado como exemplo de controle de acesso contextual alinhado aos controles de segurança móvel e acesso lógico da norma.

## Key Sources

- [[wiki/sources/nubank-clojure-datomic-event-sourcing]]
- [[wiki/sources/iso-27001-dicionario-programador]] — certificação ISO 27001 e "modo rua" como controle de acesso contextual
