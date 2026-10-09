---
type: concept
title: "Secret Manager (Vault)"
aliases: ["cofre de senhas", "vault", "secrets manager"]
date_created: 2026-10-09
date_updated: 2026-10-09
source_count: 1
tags: [security, secrets-management, vault, producao]
skill: tech-mentor-security
status: draft
---

# Secret Manager (Vault)

Serviço de cofre (Google Secret Manager, AWS Secrets Manager, HashiCorp Vault, Azure Key Vault) que armazena segredos e os **injeta no ambiente** da aplicação (agente no servidor). Ganhos: criptografia, auditoria, controle de acesso, rotação automática (inclusive da senha do banco) e troca sem tocar no servidor — essencial com muitos contêineres atrás de load balancer. Custos: configuração inicial, acesso externo do servidor, possíveis restrições; não compensa em projeto pequeno. Hospedagem compartilhada geralmente não permite agente. Detalhes e dynamic secrets em [[wiki/concepts/secrets-management]]; é uma camada de [[wiki/concepts/defense-in-depth]]; segurança de produção também depende de [[wiki/concepts/compliance]].

## Key Sources

- [[wiki/sources/dotenv-arquivo-env-boas-praticas-secret-manager]]
