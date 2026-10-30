---
type: concept
title: "Terraform workflow: init, plan, apply"
aliases: ["terraform init", "terraform plan", "terraform apply", "fluxo do terraform"]
date_created: 2026-10-26
date_updated: 2026-10-26
source_count: 1
tags: [terraform, init, plan, apply, cli]
skill: tech-mentor-infra
status: draft
---

# Terraform workflow: init → plan → apply

Fluxo de [[wiki/sources/introducao-ao-terraform-iac-devops]]:

1. **`terraform init`** — baixa os [[wiki/concepts/terraform-provider|providers]] declarados e prepara o diretório de trabalho. Reexecutar só ao adicionar provider.
2. **`terraform plan`** — gera o **plano de execução** comparando [[wiki/concepts/terraform-state|state]] e código. Mostra o que será criado/alterado/destruído (resumo: `1 to add, 0 to change, 0 to destroy`); valores como ARN e IP público aparecem como conhecidos só após o apply. Se o código mudar, rodar o plan de novo.
3. **`terraform apply`** — reapresenta o plano, pede `yes` e executa; cria os recursos no provedor (instância `t3.micro` em ~10 s no laboratório).

**Erros no plan** fazem parte: no laboratório, faltou `ami` (ou `launch_template`) e o plan falhou — ver [[wiki/concepts/ami]].

Verificação independente do Terraform: `aws ec2 describe-instances` (vazio antes, uma instância depois) — ver [[wiki/concepts/ec2]], [[wiki/concepts/localstack]]. Relação com [[wiki/concepts/infraestrutura-declarativa]]. Em time, o mesmo fluxo roda em pipeline ([[wiki/concepts/ci-cd]]).

## Key sources

- [[wiki/sources/introducao-ao-terraform-iac-devops]]
