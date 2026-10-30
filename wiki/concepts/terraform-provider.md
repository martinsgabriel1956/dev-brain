---
type: concept
title: "Terraform Provider"
aliases: ["provider", "providers do terraform"]
date_created: 2026-10-26
date_updated: 2026-10-26
source_count: 1
tags: [terraform, provider, plugin, multi-cloud]
skill: tech-mentor-infra
status: draft
---

# Terraform Provider

**Plugin** que ensina o [[wiki/entities/terraform]] a falar com a API de um provedor. O provider da AWS conversa com a API da [[wiki/entities/aws|AWS]]; o do Google, com a [[wiki/entities/google-cloud-platform|GCP]]; há também Azure e Kubernetes. Atalho mental do vídeo: *"o provider é onde você vai criar"*.

- É o que permite **um único código** gerir várias nuvens (EC2 na AWS, banco no GCP, bucket no Azure) sem repetir o trabalho manual em cada console.
- Declarado no bloco `terraform { required_providers }` (fonte + versão) e configurado no bloco `provider` (ex.: `region = "us-east-1"`). Ver [[wiki/concepts/terraform-blocos]].
- Baixado por `terraform init` ([[wiki/concepts/terraform-workflow]]); só é preciso rodar `init` de novo ao adicionar um provider novo.
- Preferir **providers oficiais** (mais seguros) — selo visível no [[wiki/concepts/terraform-registry]].
- Autenticação: o Terraform precisa de credenciais com permissão. Colocar Access/Secret Key no código "dá para fazer, mas não é boa prática" (ver [[wiki/concepts/least-privilege]]); o vídeo não detalha as alternativas.

## Key sources

- [[wiki/sources/introducao-ao-terraform-iac-devops]]
