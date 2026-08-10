---
type: concept
title: "Infrastructure as Code (IaC)"
aliases: ["IaC", "infra as code", "infraestrutura como código"]
date_created: 2026-08-05
date_updated: 2026-08-05
source_count: 1
tags: ["iac", "infra", "devops", "cloud", "versionamento", "gitops"]
skill: tech-mentor-infra
status: stub
---

# Infrastructure as Code (IaC)

Tratar infraestrutura (cloud, redes, bancos, funções serverless etc.) como um "cidadão de mesma categoria" que código de aplicação: descrita em arquivos de texto, versionada em Git, revisável via pull request, documentada implicitamente pelo próprio código e reproduzível de forma determinística — em vez de configurada manualmente clicando em consoles de provedores como AWS, GCP ou Azure.

## Problema que resolve

Configuração manual via console (clicar em "create function", ajustar uma configuração de banco de dados direto no RDS/Aurora etc.) não deixa rastro: não é visível para o time, não é bem documentada e é fácil esquecer de replicar a mudança entre ambientes (ex.: alterar em staging e esquecer produção). IaC resolve isso ao forçar toda configuração de infraestrutura a passar por um arquivo (ou conjunto de arquivos) — YAML, HCL, ou uma linguagem de propósito geral como TypeScript — commitado e revisado como qualquer outra mudança de código.

## Benefícios centrais

- **Versionamento** — histórico completo de quem mudou o quê e quando.
- **Revisão/auditabilidade** — mudanças passam por pull request antes de serem aplicadas.
- **Replicabilidade** — o mesmo código gera o mesmo ambiente em dev, staging e produção, com variações controladas explicitamente (ex.: `if (environment === 'prod')` alterando política de backup).
- **Automação** — a aplicação da infraestrutura roda via pipeline, não do laptop de alguém.

## Caminho de maturidade

A progressão natural sugerida por uma fonte é: começar configurando manualmente pelo console (bom para aprender qualquer provedor, seguindo tutoriais/documentação oficial) e migrar para IaC conforme o projeto e a empresa amadurecem. Para uma startup muito nova, configuração manual às vezes é aceitável; para um projeto robusto, IaC é considerado o padrão profissional esperado.

## Ferramentas

- [[wiki/concepts/aws-cdk]] — TypeScript (ou outras linguagens de propósito geral) que sintetiza para CloudFormation.
- [[wiki/concepts/aws-cloudformation]] — formato nativo AWS, YAML/JSON.
- Terraform / OpenTofu — ver [[wiki/sources/terraform]] — linguagem franca de IaC multi-cloud (HCL); OpenTofu é o fork open-source surgido após a mudança de licença do Terraform.
- Pulumi — IaC com linguagens de propósito geral (TypeScript, Python, Go, C#), sem DSL customizada.
- Outras citadas: Ansible, Bicep (Azure). Kubernetes também pode ser considerado uma forma de IaC.

## Relação com outros conceitos

- [[wiki/concepts/aws-cdk]] — uma das implementações concretas de IaC demonstradas
- [[wiki/concepts/aws-cloudformation]] — formato-alvo gerado pelo CDK
- [[wiki/concepts/aws-lambda]] — recurso tipicamente provisionado via IaC no exemplo demonstrado
- [[wiki/concepts/api-gateway]] — componente da arquitetura de exemplo usada para ilustrar uma "stack"

## Key Sources

- [[wiki/sources/infraestrutura-como-codigo-cdk-aws]]
