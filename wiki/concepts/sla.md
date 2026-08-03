---
type: concept
title: "SLA — Service Level Agreement"
aliases: ["service level agreement", "sla"]
date_created: 2026-04-22
date_updated: 2026-08-03
source_count: 2
tags: [sre, contrato, confiabilidade]
skill: tech-mentor-infra
status: stable
---

# SLA — Service Level Agreement

Contrato externo com penalidades (créditos, multas). Derivado do [[concepts/slo]] com margem de segurança — sempre menos rigoroso que o SLO interno.

## Estrutura

```
SLO interno:  99.9% disponibilidade  ← operacional, critério para Error Budget
SLA externo:  99.5% disponibilidade  ← contratual, com créditos se violado

Margem de segurança: 0.4%
→ Se o SLO for violado, ainda há folga antes de violar o SLA e gerar multa
```

## Por que SLO ≠ SLA

SLO é ferramenta de decisão interna. SLA é compromisso legal com cliente. Gerir pelo SLA é tarde demais — o SLO funciona como alarme antecipado.

## A Mesma Promessa, Duas Naturezas Diferentes

O que separa um SLO de um SLA não é o número prometido nem a métrica usada — é quem são as partes do acordo. O mesmo "99,9% de disponibilidade" é um SLO quando dito entre times da mesma empresa (ex.: time de banco de dados prometendo disponibilidade para o time de aplicação) e vira SLA quando dito entre duas empresas distintas com contrato formal (ex.: uma empresa que vende banco de dados como serviço para outra). Se a promessa interna falha, gera "problema interno" — não existe multa entre áreas da mesma empresa. Se a promessa contratual falha, gera penalidade.

Isso também explica por que nem todo serviço tem SLA: um usuário final comprando num e-commerce não tem nenhum acordo formal com a loja — se o site cai, ele simplesmente compra em outro lugar. Já um lojista que contrata a mesma plataforma para vender seus produtos, e recebe a garantia formal de "99% do tempo disponível", tem um SLA de verdade, porque há uma consequência contratual pactuada.

## Key Sources

- [[sources/sre-sli-slo-sla]]
- [[sources/slo-sli-sla-exemplo-ecommerce]]
