---
type: concept
title: "Zona Local Dedicada AWS"
aliases: ["Dedicated Local Zone", "AWS Dedicated Local Zone"]
date_created: 2026-05-06
date_updated: 2026-05-06
source_count: 1
tags: ["aws", "soberania-digital", "compliance", "infraestrutura-dedicada"]
skill: tech-mentor-infra
status: stub
---

# Zona Local Dedicada AWS (Dedicated Local Zone)

Infraestrutura de nuvem AWS criada especificamente para um cliente, setor ou governo, para atender a requisitos regulatórios e de [[soberania-digital]]. Diferente de uma [[zona-local-aws|Zona Local]] padrão, é isolada e dedicada — operada pela AWS, mas com acesso restrito à entidade contratante.

## Diferença em relação à Local Zone padrão

| | Local Zone | Dedicated Local Zone |
|---|---|---|
| Acesso | Multi-tenant (compartilhada) | Single-tenant (dedicada) |
| Público-alvo | Qualquer cliente AWS | Governo, defesa, setor regulado |
| Requisitos | Latência metropolitana | Soberania digital, compliance |
| Localização | Definida pela AWS | Negociada com o cliente/governo |

## Casos de Uso

- Governo federal com requisito de dados dentro do território nacional
- Setor de defesa com isolamento rigoroso
- Setores financeiros com regulação de residência de dados (ex: BACEN no Brasil)
- Saúde com requisitos HIPAA ou equivalentes nacionais

## Relação com AWS GovCloud

AWS GovCloud é uma região isolada para o governo dos EUA (FedRAMP, ITAR). Dedicated Local Zones expandem esse conceito para outros países e setores, sem precisar de uma região completa.

## Key Sources

- [[wiki/sources/aws-infraestrutura-global]]
