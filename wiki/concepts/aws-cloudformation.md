---
type: concept
title: "AWS CloudFormation"
aliases: ["CloudFormation", "CFN"]
date_created: 2026-08-05
date_updated: 2026-08-05
source_count: 1
tags: ["aws", "cloudformation", "iac", "stack", "infra"]
skill: tech-mentor-infra
status: stub
---

# AWS CloudFormation

Forma nativa da AWS de descrever infraestrutura como um arquivo de configuração declarativo (YAML ou JSON), agrupado em uma "stack" — um conjunto de recursos AWS gerenciados como uma unidade. É possível criar uma stack diretamente pelo console da AWS (seção CloudFormation) ou gerá-la a partir de outra ferramenta, como o [[wiki/concepts/aws-cdk|AWS CDK]].

## Papel dentro do ecossistema de IaC AWS

O [[wiki/concepts/aws-cdk|CDK]] não substitui o CloudFormation — ele é uma camada acima: o desenvolvedor escreve TypeScript (ou outra linguagem suportada), e o CDK sintetiza esse código para um template de CloudFormation, que é o artefato de fato aplicado pela AWS. O template de CloudFormation gerado é descrito, na fonte que documenta esse fluxo, como difícil de ler diretamente ("tenebroso") — a experiência de desenvolvimento pretendida é escrever/revisar o código de mais alto nível (CDK), não o CloudFormation gerado.

## Relação com outros conceitos

- [[wiki/concepts/infraestrutura-como-codigo]] — categoria geral
- [[wiki/concepts/aws-cdk]] — ferramenta que sintetiza para CloudFormation em vez de escrevê-lo à mão

## Key Sources

- [[wiki/sources/infraestrutura-como-codigo-cdk-aws]]
