---
type: source
title: "Introdução ao Terraform — o que é, para que serve e como funciona (com prática)"
aliases: ["Introdução ao Terraform", "Terraform para iniciantes"]
date_created: 2026-10-26
date_updated: 2026-10-26
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/introducao-ao-terraform-iac-devops.md
source_url: ""
author: "não identificado (canal de DevOps)"
date_published: ""
date_ingested: 2026-10-26
source_count: 1
tags: [tech-mentor-infra, terraform, iac, devops, aws, ec2, hcl, providers, state]
skill: tech-mentor-infra
status: stable
---

## TL;DR

Vídeo introdutório (PT-BR) sobre o [[wiki/entities/terraform]]: ferramenta open source de [[wiki/concepts/infraestrutura-como-codigo|IaC]] que provisiona infraestrutura de forma [[wiki/concepts/infraestrutura-declarativa|declarativa]]. Valor: **automação**, **versionamento** e **multi-provedor**. Três pilares: [[wiki/concepts/hcl|HCL]], [[wiki/concepts/terraform-provider|providers]] e [[wiki/concepts/terraform-state|state]]; fluxo [[wiki/concepts/terraform-workflow|init → plan → apply]]. Na prática (sandbox oficial com [[wiki/concepts/localstack|LocalStack]]), cria uma [[wiki/concepts/ec2|EC2]] `t3.micro` "Hello World", errando de propósito ao omitir a [[wiki/concepts/ami|AMI]].

## Key Claims

**Claim:** IaC troca cliques no console por código que descreve o que criar; o Terraform chama a API do provedor.
**Evidence:** exemplo da EC2 criada por console vs. por código. **Confidence:** alta. Ver [[wiki/concepts/infraestrutura-como-codigo]].

**Claim:** Três ganhos: automação (escrever uma vez, reusar; evita repetir 5 vezes à mão), versionamento (Git mostra histórico e autor; no console a mudança de 2 para 4 CPUs não deixa registro do valor anterior) e um só código para várias nuvens.
**Evidence:** exemplos do apresentador (EC2 na AWS + banco no GCP + bucket no Azure). **Confidence:** alta como princípio; exemplos didáticos. Ver [[wiki/concepts/git]], [[wiki/concepts/terraform-provider]].

**Claim:** O Terraform é declarativo: compara o declarado com o state e aplica só a diferença (3 desejados, 1 existente → cria 2).
**Evidence:** exemplo do vídeo. **Confidence:** alta. Ver [[wiki/concepts/infraestrutura-declarativa]], [[wiki/concepts/terraform-state]].

**Claim:** O state guarda tudo o que o Terraform já criou e é comparado a cada execução; é "extremamente importante".
**Evidence:** descrição do apresentador; o vídeo não aborda state remoto, locking nem perda do state. **Confidence:** alta. [skill: tech-mentor-infra] `references/terraform.md` acrescenta backend remoto S3 + locking (DynamoDB) como obrigatório em times, e que o state é a maior fonte de dor — **não dito no vídeo**.

**Claim:** `init` baixa providers e prepara o diretório; `plan` gera o plano comparando state e código; `apply` executa após confirmação `yes`.
**Evidence:** demonstração (apply em ~10 s; `describe-instances` vazio antes, 1 instância depois, AMI final `7D99`, tag `Name=Hello World`). **Confidence:** alta. Ver [[wiki/concepts/terraform-workflow]].

**Claim:** O tipo do resource (`aws_instance`) é imutável e exato; o nome do bloco é livre e não é o nome na AWS (este vem da tag `Name`).
**Evidence:** explicação no editor. **Confidence:** alta. Ver [[wiki/concepts/terraform-blocos]].

**Claim:** `ami` consta como opcional na documentação, mas é obrigatória sem `launch_template`; o erro no plan foi simulado para mostrar que é preciso ler a doc.
**Evidence:** erro e correção ao vivo. **Confidence:** alta. Ver [[wiki/concepts/ami]], [[wiki/concepts/terraform-argumentos-e-atributos]].

**Claim:** Usar providers oficiais; credenciais no código funcionam mas não são boa prática.
**Evidence:** fala do apresentador, sem alternativas detalhadas. **Confidence:** média (corroborado por [[wiki/concepts/least-privilege]] em espírito). Ver [[wiki/concepts/terraform-registry]].

**Claim:** Arquivos `.tf` podem ter qualquer nome; `main.tf`/`terraform.tf` são só convenção.
**Evidence:** explicação no sandbox. **Confidence:** alta. Ver [[wiki/concepts/hcl]].

## Entities

[[wiki/entities/terraform]] (novo), [[wiki/entities/aws]], [[wiki/entities/google-cloud-platform]], [[wiki/entities/mitchell-hashimoto]] (criador do Terraform, citado só em outra fonte). Apresentador não identificado; menciona seu "Laboratório DevOps" no YouTube.

## Concepts

Novos: [[wiki/concepts/infraestrutura-declarativa]], [[wiki/concepts/hcl]], [[wiki/concepts/terraform-provider]], [[wiki/concepts/terraform-workflow]], [[wiki/concepts/terraform-blocos]], [[wiki/concepts/terraform-registry]], [[wiki/concepts/terraform-argumentos-e-atributos]], [[wiki/concepts/ami]].
Ligados: [[wiki/concepts/infraestrutura-como-codigo]], [[wiki/concepts/iac]], [[wiki/concepts/terraform-state]], [[wiki/concepts/terraform-modules]], [[wiki/concepts/ec2]], [[wiki/concepts/localstack]], [[wiki/concepts/regiao-aws]], [[wiki/concepts/vpc]], [[wiki/concepts/git]], [[wiki/concepts/devops-culture]], [[wiki/concepts/drift-detection]], [[wiki/concepts/least-privilege]], [[wiki/concepts/ci-cd]].

## Open Questions

- Como proteger o state (remoto, locking, criptografia) e evitar segredos nele? (não coberto; ver [[wiki/sources/terraform]])
- O que acontece com o state ao alterar o recurso fora do Terraform ([[wiki/concepts/drift-detection|drift]])?
- Alternativas de autenticação além de chaves no código (perfis, roles, OIDC)?
- Módulos, `data` e `output` ficaram só citados ([[wiki/concepts/terraform-modules]]).

## Raw quotes

> "infraestrutura como código assim como o nome diz ao invés de eu ir lá e clicar nos botões na AWS eu escrevo um código que representa exatamente isso"
> "o provider é onde você vai criar"
> "o Terraform ele funciona de forma declarativa"
> "ele fala que é um parâmetro opcional mas você tem que ler obviamente"
