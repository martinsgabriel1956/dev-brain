---
type: concept
title: "Secrets Management"
aliases: ["secrets management", "gerenciamento de segredos", "env variables", "credenciais", ".env"]
date_created: 2026-06-10
date_updated: 2026-07-19
source_count: 2
tags: [security, secrets-management, env, credenciais, devsecops, ci-cd, under-engineering]
skill: tech-mentor-security
status: stable
---

# Secrets Management

Prática de armazenar, distribuir e rotacionar credenciais (senhas, API keys, tokens) de forma que nunca apareçam em código-fonte, logs ou repositórios. Uma das regras mais simples e mais violadas de segurança.

## A Regra Fundamental

**Credenciais jamais no código. Sem exceção.**

Se você commitou uma credencial: **altere essa credencial imediatamente** — não basta remover do código ou reescrever o histórico do git. A credencial vazou e deve ser considerada comprometida.

## Por Que Não Basta "Repositório Privado"

- Repositórios privados podem ser tornados públicos acidentalmente
- Funcionários saem das empresas com acesso ao histórico
- Ferramentas de secret scanning (Gitleaks, TruffleHog, GitHub Advanced Security) varrem repositórios automaticamente — incluindo histórico de commits
- Hardcoded no frontend: o bundle JavaScript é entregue ao browser do usuário — qualquer credencial ali está exposta publicamente

## Gestão Local (Desenvolvimento)

```
.env              # variáveis reais — NUNCA commitado
.env.example      # template com chaves mas sem valores — pode commitar
.gitignore        # deve incluir .env, .env.local, .env.*.local
```

Exemplo de `.env`:
```bash
DB_PASSWORD=senha_local_nao_producao
OPENAI_API_KEY=sk-...
```

**Regra:** credenciais de produção nunca na máquina local do dev.

## Gestão em Produção

Ferramentas injetam as variáveis na aplicação em tempo de execução, sem que fiquem visíveis após configuradas:

| Ferramenta | Contexto de uso |
|---|---|
| **GitHub Secrets** | Injetado no CI/CD durante o deploy |
| **AWS Secrets Manager** | Gerenciamento centralizado na AWS; rotação automática |
| **HashiCorp Vault** | Alternativa open-source; dynamic secrets |
| **Google Secret Manager** | Equivalente para GCP |

Propriedade desejável: **secrets configurados não são mais visíveis** — nem ao próprio configurador. Apenas a aplicação em execução os recebe.

## Níveis de Gravidade (Pior para Menos Pior)

1. **Credencial de produção hardcoded no frontend** → exposta a qualquer usuário do site
2. **Credencial hardcoded no backend** (repositório privado) → exposta a qualquer pessoa com acesso ao repositório
3. **`.env` de produção commitado** → exposta no histórico do git
4. **`.env` local com credencial de produção** → risco se a máquina for comprometida

## Variável de Ambiente Configurada no Provedor de Deploy

[[wiki/sources/underengineering-overengineering-mario-souto]] descreve o fluxo do lado "gestão em produção" desta página aplicado a um projeto pessoal na Vercel: valores de configuração — incluindo chaves públicas expostas ao navegador e a chave de API da OpenAI usada em outro projeto do autor — ficam todos como variáveis de ambiente configuradas no painel da Vercel (Settings do ambiente), não hardcoded no código. O benefício prático citado, além de segurança: trocar um valor e disparar um novo deploy sem tocar no código-fonte. A fonte trata hardcode de configuração como um dos sinais centrais de [[wiki/concepts/under-engineering]] — não é tratado como problema exclusivamente de segurança, mas também de manutenção (mudar um valor não deveria exigir um PR).

## Relação com Outros Conceitos

- [[principio-do-menor-privilegio]] — cada secret deve ter escopo mínimo (API key com permissão só do que precisa)
- [[attack-surface]] — credenciais expostas expandem massivamente a superfície de ataque
- [[secure-by-default]] — o default deve ser que credenciais nunca estejam no código

## Key Sources

- [[sources/cinco-praticas-seguranca-pragmatic-programmer]] — regra de não commitar + .env + ferramentas de secrets management; história do frontend com credenciais hardcoded
- [[wiki/sources/underengineering-overengineering-mario-souto]] — variáveis de ambiente configuradas na Vercel em vez de hardcode, incluindo chave de API da OpenAI; hardcode tratado como sintoma de under-engineering
