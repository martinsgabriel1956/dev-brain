---
type: entity
title: "Terraform"
aliases: ["terraform", "hashicorp terraform"]
date_created: 2026-10-26
date_updated: 2026-10-26
source_count: 1
tags: [terraform, iac, devops, cloud, ferramenta]
skill: tech-mentor-infra
status: draft
---

# Terraform

Ferramenta **open source** de [[wiki/concepts/infraestrutura-como-codigo|infraestrutura como código]], criada por [[wiki/entities/mitchell-hashimoto]]. Segundo [[wiki/sources/introducao-ao-terraform-iac-devops]], é uma das mais usadas porque fala com várias nuvens por meio de [[wiki/concepts/terraform-provider|providers]] ([[wiki/entities/aws]], [[wiki/entities/google-cloud-platform|GCP]], Azure, Kubernetes).

- Funciona de forma [[wiki/concepts/infraestrutura-declarativa|declarativa]]: o código descreve o estado desejado e a ferramenta compara com o [[wiki/concepts/terraform-state|state]].
- Três pilares: [[wiki/concepts/hcl|HCL]], [[wiki/concepts/terraform-provider|providers]] e [[wiki/concepts/terraform-state|state]].
- Fluxo: [[wiki/concepts/terraform-workflow|init → plan → apply]].
- Documentação: [[wiki/concepts/terraform-registry]] (providers) e a doc da linguagem ([[wiki/concepts/terraform-blocos]]).
- Benefícios citados: automação, versionamento em [[wiki/concepts/git]] e uso multi-provedor.
- Material mais aprofundado (state remoto, módulos, drift): [[wiki/sources/terraform]].

## Key sources

- [[wiki/sources/introducao-ao-terraform-iac-devops]]
