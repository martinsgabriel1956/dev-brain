---
type: concept
title: "AMI (Amazon Machine Image)"
aliases: ["AMI", "imagem de máquina"]
date_created: 2026-10-26
date_updated: 2026-10-26
source_count: 1
tags: [aws, ec2, ami, terraform]
skill: tech-mentor-infra
status: draft
---

# AMI

Imagem que define o **sistema operacional** de uma instância [[wiki/concepts/ec2]]. Sem AMI (ou `launch_template`) não se cria a máquina — nem no console, nem no [[wiki/entities/terraform]]: o `terraform plan` falha. Em [[wiki/sources/introducao-ao-terraform-iac-devops]] o ID real foi copiado do console (Ubuntu Server elegível ao nível gratuito); em ambiente simulado como o [[wiki/concepts/localstack]] qualquer valor basta.

Ver [[wiki/concepts/terraform-argumentos-e-atributos]].

## Key sources

- [[wiki/sources/introducao-ao-terraform-iac-devops]]
