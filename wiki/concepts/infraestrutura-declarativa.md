---
type: concept
title: "Infraestrutura declarativa"
aliases: ["declarativo", "modelo declarativo", "estado desejado"]
date_created: 2026-10-26
date_updated: 2026-10-26
source_count: 1
tags: [terraform, iac, declarativo, estado-desejado]
skill: tech-mentor-infra
status: draft
---

# Infraestrutura declarativa

Você declara **o estado final desejado** e a ferramenta calcula o que fazer. No [[wiki/entities/terraform]], ele compara o que já existe (via [[wiki/concepts/terraform-state|state]]) com o código e aplica só a diferença.

Exemplo de [[wiki/sources/introducao-ao-terraform-iac-devops]]: já existe 1 servidor e o código declara 3 → o Terraform cria apenas **2**.

Contraste com o modo manual (console) e com scripts imperativos ("crie 3"): o declarativo é reaplicável e convergente. Ver [[wiki/concepts/infraestrutura-como-codigo]] e [[wiki/concepts/terraform-workflow]].

## Key sources

- [[wiki/sources/introducao-ao-terraform-iac-devops]]
