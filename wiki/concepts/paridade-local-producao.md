---
type: concept
title: "Paridade Local–Produção"
aliases: ["staging parity", "works on my machine", "local vs prod", "paridade de ambiente"]
date_created: 2026-04-26
date_updated: 2026-07-31
source_count: 4
tags: [staging, producao, docker, devops, debugging, ambiente]
skill: tech-mentor-leadership
status: draft
---

# Paridade Local–Produção

"Funciona na minha máquina" é o sintoma — a causa é a falta de paridade entre o ambiente de desenvolvimento e produção. Quanto maior a divergência, mais difícil reproduzir bugs e mais surpresas no deploy.

## Por que o laptop mente

| Laptop | Produção |
|---|---|
| 1 usuário | Milhares simultâneos |
| 10 linhas de teste no banco | Milhões de rows |
| Localhost (sem latência) | Latência de rede real |
| Seu OS e versões | OS diferente, resources diferentes |
| Sem pressão de memória | Limite de memória real |

O bug que só acontece em prod é o pior — você não consegue reproduzir, então depura às cegas.

## Como reduzir a divergência

- **Docker:** mesma imagem em dev e prod — elimina divergências de OS e dependências
- **Staging environment:** ambiente separado com dados reais (anonimizados) e carga similar
- **Deploy cedo e com frequência:** quanto menor o delta entre deploys, menor a superfície de surpresas
- **Testes de carga locais:** `k6`, `artillery` — simule múltiplos usuários antes de ir pra prod

## Clonagem Anonimizada do Banco para Staging — Exemplo Concreto

[[wiki/sources/continuous-integration-delivery-deploy-vs-release]] descreve a prática de forma mais concreta do que a linha genérica acima: clonar o banco de produção inteiro para dev/staging, mas anonimizando seletivamente o que é sensível (senha de usuário, nome de pessoa, dados de compra/pagamento) e preservando o resto — estrutura do schema e a dispersão estatística dos dados reais. O objetivo é o mesmo desta página (reduzir o gap de "dados de teste" vs. "dados reais"), sem expor dado sensível de usuário real ao ambiente de staging.

## Twelve-Factor App (fator X)

O [Twelve-Factor App](https://12factor.net/dev-prod-parity) formaliza paridade como princípio: minimizar gap entre dev, staging e produção em tempo (deploys frequentes), pessoal (dev faz deploy) e ferramentas (mesmos serviços em todos os ambientes).

## Sequência de teste antes de subir um PR

Válido especialmente para quem está começando: nunca validar mudanças direto em produção. Ordem recomendada — ambiente de desenvolvimento → homologação (com QA, se houver) → só então abrir o code review. Depois do deploy, validar manualmente em produção antes de marcar a tarefa como concluída — ver [[wiki/concepts/pensamento-em-producao]] e [[wiki/concepts/code-review]].

## Relacionado

[[concepts/observabilidade]] · [[sources/cicd-pipeline]] · [[sources/zero-downtime-deploy]]

## Key Sources

- [[sources/5-principios-programador]]
- [[wiki/sources/como-nao-ser-humilhado-no-primeiro-code-review]] — sequência dev/homologação/produção antes de abrir PR
- [[wiki/sources/continuous-integration-delivery-deploy-vs-release]] — exemplo concreto de clonagem anonimizada do banco de produção para staging
