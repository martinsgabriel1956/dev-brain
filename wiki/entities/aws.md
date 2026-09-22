---
type: entity
title: "AWS"
aliases: ["amazon web services"]
date_created: 2026-09-15
date_updated: 2026-09-22
source_count: 4
tags: [empresa, cloud, forward-deployed-engineer, solutions-architect]
skill: tech-mentor-leadership
status: stub
---

# AWS

Provedor de nuvem citado como um dos primeiros a adotar o modelo Forward Deployed Engineer fora do contexto original da [[wiki/entities/palantir]], sob o nome de **Solutions Architect** — ver [[wiki/concepts/arquiteto-de-solucoes]]. Quando bancos, empresas de energia e varejo começaram a migrar para a nuvem, a AWS percebeu que vender o serviço de computação/banco de dados sozinho não bastava para viabilizar a migração de clientes Enterprise com dados e aplicações legadas — passou a alocar especialistas próprios dentro do dia a dia desses clientes.

## Caso Relatado: Itaú

Segundo [[wiki/sources/forward-deployed-engineers-origem-palantir-onda-brasil]], relato pessoal do autor da fonte: ao trabalhar no [[wiki/entities/itau]], viu funcionários da AWS atuando diretamente no dia a dia do banco, próximos dos desafios e features sendo construídas, guiando o uso correto dos recursos AWS para migração. O incentivo é duplo: ajuda o cliente a migrar com segurança e aumenta a conta que ele paga à AWS à medida que adota mais serviços.

**Confidence:** Média — relato pessoal e específico do autor da fonte, não verificado externamente nesta ingestão.

## Key Sources

- [[wiki/sources/cloud-security]] — Cloud Security: IAM com least privilege, Permission Boundaries para delegação segura, SCPs para guardrails em toda a org AWS. CSPM (Prowler, Security Hub) audita misconfigurations continuamente....
- [[wiki/sources/dynamodb]] — DynamoDB: NoSQL serverless AWS com escala ilimitada. Single-Table Design: todos os tipos de entidade em uma tabela, acesso por PK+SK patterns. GSI (Global Secondary Index) permite queries por outras...
- [[wiki/sources/sqs-sns]] — SQS é uma fila gerenciada AWS (zero operação). Standard: alta throughput, ordenação best-effort. FIFO: ordering garantido por MessageGroupId, deduplicação nativa (5 min window), limitado a 3k msg/s...
- [[wiki/sources/forward-deployed-engineers-origem-palantir-onda-brasil]] — relato de engenheiros AWS atuando dentro do Itaú, modelo Solutions Architect como precursor do FDE em cloud
