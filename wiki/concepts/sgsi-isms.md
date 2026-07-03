---
type: concept
title: "SGSI / ISMS"
aliases: ["Sistema de Gestão de Segurança da Informação", "Information Security Management System", "ISMS"]
date_created: 2026-07-03
date_updated: 2026-07-03
source_count: 2
tags: [sgsi, isms, iso-27001, compliance, security, risk-management]
skill: tech-mentor-security
status: draft
---

## Definição

Framework de gestão — não um software ou produto — composto por políticas, procedimentos, processos e tecnologia, desenhado para gerenciar riscos de segurança da informação de forma sistêmica. É o objeto central que a norma [[wiki/concepts/iso-27001]] exige que a organização construa e mantenha.

O SGSI existe para sustentar, de forma auditável, os três pilares da [[wiki/concepts/triade-cia]].

## Por que "gestão" e não "ferramenta"

Ter antivírus, firewall ou até uma boa arquitetura de segurança não é, por si só, um SGSI. O SGSI é o processo formal que garante que esses controles:

- foram escolhidos com base em uma avaliação de risco real, não em achismo;
- estão documentados e auditáveis (a **SoA** — Declaração de Aplicabilidade — é o artefato central desse processo);
- são revisados e melhorados continuamente (cláusulas 9 e 10 da norma: avaliação de desempenho e melhoria).

## Relação com Risk Assessment

O SGSI se apoia em uma avaliação formal de riscos: identificar ativos, ameaças e vulnerabilidades, e decidir quais dos controles do Anexo A da ISO 27001 mitigam esses riscos de forma proporcional ao contexto da organização — nunca aplicando os 93 controles de forma indiscriminada.

## Key Sources

- [[wiki/sources/iso-27001-dicionario-programador]] — define SGSI como framework de gestão sistêmico organizado em torno da tríade CIA
- [[wiki/sources/compliance-soc2-pci]] — ISMS com Risk Assessment formal como base da certificação ISO 27001

## Conceitos Relacionados

[[wiki/concepts/iso-27001]] · [[wiki/concepts/triade-cia]] · [[wiki/concepts/compliance]]
