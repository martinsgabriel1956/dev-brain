---
type: concept
title: "Recreate Deployment"
aliases: ["recreate deploy", "deploy recreate", "shutdown e start"]
date_created: 2026-07-09
date_updated: 2026-07-09
source_count: 1
tags: [devops, deploy, cicd, downtime, infra]
skill: tech-mentor-infra
status: stable
---

# Recreate Deployment

Estratégia de deploy mais simples e mais comum quando ninguém pensou muito na estratégia: desliga a instância rodando a versão antiga (shutdown) e sobe a versão nova no lugar (start).

## Fluxo

```
[v1 rodando na porta 3000]
        ↓ shutdown
[nada rodando]
        ↓ start (não é instantâneo)
[v2 rodando na porta 3000]
```

## Por que causa downtime

Entre o shutdown de v1 e o start de v2 concluído, não há nenhuma instância respondendo — requests dos usuários nessa janela são perdidos. O tempo pode ser curto, mas não é zero.

Origem histórica: a "janela de manutenção" ("site em manutenção das 9 às 10 da noite") é Recreate manual — acessar o servidor, derrubar o código antigo, subir o novo, sem se preocupar com tráfego durante a janela anunciada.

## Quando ainda faz sentido

- Ambientes sem SLA de disponibilidade (dev, staging, projetos pessoais)
- Sistemas onde o downtime é aceitável ou já é comunicado (janela de manutenção)
- Deploys serverless simples, onde a própria cloud faz algo equivalente a um Recreate instantâneo por baixo dos panos — ver [[concepts/ci-cd]]

## Quando evitar

Qualquer sistema com SLA de disponibilidade real — nesse caso usar [[concepts/rolling-update]], [[concepts/blue-green-deploy]] ou [[concepts/canary-release]], todos desenhados para eliminar essa janela de downtime. Ver [[concepts/zero-downtime-deploy]] para o objetivo geral e [[concepts/deploy-strategies]] para o comparativo completo.

## Key Sources

- [[sources/tipos-de-deploy]]
