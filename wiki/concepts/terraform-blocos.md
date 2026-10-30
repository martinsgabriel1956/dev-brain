---
type: concept
title: "Blocos do Terraform (provider, resource, variable)"
aliases: ["blocos hcl", "resource block", "variable block"]
date_created: 2026-10-26
date_updated: 2026-10-26
source_count: 1
tags: [terraform, hcl, blocos, resource, variable]
skill: tech-mentor-infra
status: draft
---

# Blocos do Terraform

Sintaxe de [[wiki/concepts/hcl]]: `tipo "tipo-específico" "nome" { argumentos }`. Tipos mostrados em [[wiki/sources/introducao-ao-terraform-iac-devops]]:

- **`provider`** — configura o [[wiki/concepts/terraform-provider]] (projeto/região no Google; região/credenciais na AWS).
- **`resource`** — o que criar. Em `resource "aws_instance" "web"`, o 1º rótulo é o tipo (**imutável**, exatamente o nome do recurso no provider) e o 2º é só o nome do bloco no código. O nome da máquina na AWS vem da tag `Name`. Exemplos: `aws_vpc` ([[wiki/concepts/vpc]]), `aws_instance` ([[wiki/concepts/ec2]]).
- **`variable`** — entrada parametrizável com `type`, `description` e `default` (ex.: `instance_type` = `t2.micro`); referenciada pelo resource.
- Outros citados sem detalhe: `module` ([[wiki/concepts/terraform-modules]]), `output`, `backend`, `data`.

Documentar argumentos e atributos: [[wiki/concepts/terraform-argumentos-e-atributos]].

## Key sources

- [[wiki/sources/introducao-ao-terraform-iac-devops]]
