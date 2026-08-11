---
type: concept
title: "Monolito Modular"
aliases: ["monolito modular", "modular monolith", "majestic monolith", "bounded modules"]
date_created: 2026-08-10
date_updated: 2026-08-10
source_count: 2
tags: [monolito-modular, monolito, arquitetura, ports-adapters, migracao, backend]
skill: tech-mentor-backend
status: draft
---

# Monolito Modular

Arquitetura em que o sistema continua sendo **um único artefato** (um deploy, um banco, um runtime), mas é internamente dividido em **módulos com fronteiras explícitas**. Os módulos **não** chamam funções internas uns dos outros: comunicam-se por **contratos/interfaces** ([[wiki/concepts/hexagonal-architecture|Ports & Adapters]]), do mesmo jeito que uma classe expõe getters/setters para o mundo externo. Isso captura o benefício de isolamento dos [[wiki/concepts/microsservicos]] — e o fim do [[wiki/concepts/code-espaguete]] — **sem** os contras da comunicação via rede e do overhead de DevOps distribuído.

## Por que existe

É a resposta à pergunta "dá para aproveitar alguns prós de microsserviços sem alguns contras?". Prós desejados: melhor isolamento + coibir o código-sopa. Contras evitados: comunicação via protocolos de rede (mais lenta que chamada de função, só justificável por razão de hardware/escala) e DevOps complexo. O objetivo prático é **fazer os desenvolvedores tropeçarem menos uns nos outros** mantendo a code base razoável de manter. Ver [[wiki/sources/monolito-modular-transicao-mvp-empresa-madura]].

## Etapa de transição MVP → empresa madura

O monolito modular é a **etapa intermediária** entre um [[wiki/concepts/monolito]] pequeno de MVP e o eventual salto para microsserviços. Como as interfaces entre módulos já estão expostas, extrair um módulo depois (ex.: mover IA para GPUs próprias) é só trocar o **transporte**: chamada de função → gRPC. Convergente com o skill `tech-mentor-backend`: comece como módulo no monolito; extraia quando o módulo tiver time dedicado, SLA independente ou escala diferente — extrair *antes* de ter módulo bem definido gera **distributed monolith**.

## Garantias

Contratos entre módulos garantem [[wiki/concepts/separation-of-concerns]] e [[wiki/concepts/encapsulamento]]. Relacionado a [[wiki/concepts/contrato-de-api]] (aqui o "contrato" é in-process, não necessariamente HTTP). Ver também a variante frontend em [[wiki/concepts/monolito-modular-frontend]].

## Key sources

- [[wiki/sources/arquitetura-de-sacrificio]] — boa modularidade é o que permite *sacrificar módulos individuais* em vez do sistema inteiro conforme ele cresce (Fowler)
- [[wiki/sources/monolito-modular-transicao-mvp-empresa-madura]]
