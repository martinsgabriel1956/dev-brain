---
type: source
title: "Terraform — IaC, State, Módulos, Terragrunt"
aliases: ["terraform", "iac", "state terraform", "terragrunt", "modules terraform"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/terraform.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [terraform, iac, state, modules, terragrunt, drift-detection, plan-apply, hcl, remote-state]
skill: tech-mentor-infra
status: stable
---

## TL;DR

Terraform é o padrão de IaC. State é o coração — armazena o mapa entre código e infraestrutura real; deve ficar no S3 + DynamoDB lock. Módulos encapsulam recursos reutilizáveis. Terragrunt resolve DRY para múltiplos ambientes. `plan` antes de `apply` é obrigatório — nunca apply sem review. Drift Detection: `terraform plan` detecta mudanças manuais no cloud.

## Key Claims

**Claim:** State remoto (S3 + DynamoDB lock) é obrigatório em times — state local não escala.
**Evidence:** State local = conflito quando dois devs aplicam ao mesmo tempo. S3: state compartilhado. DynamoDB: distributed lock previne apply simultâneo. Encrypt state at rest — contém IPs, credenciais, dados sensíveis.
**Confidence:** alta

**Claim:** Módulos são a unidade de reutilização — um módulo por padrão de infraestrutura.
**Evidence:** Módulo `ecs-service` aceita `container_image`, `desired_count`, `subnet_ids` como inputs e cria toda a infra ECS. Reutilizado em dev/staging/prod com variáveis diferentes. Versionamento via Git tag ou Terraform Registry.
**Confidence:** alta

**Claim:** Terragrunt resolve o problema de múltiplos ambientes sem copiar/colar.
**Evidence:** HCL root define backend e provider. `terragrunt.hcl` por ambiente sobrescreve variáveis. `terragrunt run-all apply` aplica em todos os módulos em ordem de dependência. Reduz boilerplate de 80% em projetos multi-ambiente.
**Confidence:** alta

**Claim:** `terraform plan` é a proteção principal — nunca executar `apply` sem review do plan.
**Evidence:** Plan mostra exatamente o que será criado/modificado/destruído. `~` = in-place update. `-` = destroy. Recursos marcados com `-` acidentalmente (ex: `force_new = true`) são frequente causa de outage.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/terraform]]
- [[concepts/iac]]
- [[concepts/terraform-state]]
- [[concepts/terraform-modules]]
- [[concepts/terragrunt]]
- [[concepts/drift-detection]]

## Open Questions

- Terraform drift em recursos gerenciados por múltiplos sistemas (Terraform + Helm + manual) — como rastrear autoridade?
- OpenTofu vs Terraform após mudança de licença — quando migrar faz sentido?
