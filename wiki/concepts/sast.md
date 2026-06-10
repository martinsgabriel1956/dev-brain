---
type: concept
title: "SAST (Static Application Security Testing)"
aliases: ["sast", "static application security testing", "análise estática de segurança", "sonarqube"]
date_created: 2026-06-10
date_updated: 2026-06-10
source_count: 1
tags: [security, sast, devsecops, sonarqube, appsec, static-analysis]
skill: tech-mentor-security
status: stable
---

# SAST (Static Application Security Testing)

Análise estática do código-fonte para detectar padrões de vulnerabilidade **antes** do código ser executado. É uma camada do [[defense-in-depth]] aplicada no processo de desenvolvimento — não no runtime.

## O Que Faz

- Detecta padrões de código vulneráveis (SQL Injection, XSS, secrets hardcoded, etc.)
- Funciona sem executar a aplicação — analisa o código como texto/AST
- Integra no pipeline de CI/CD, bloqueando PRs com vulnerabilidades

## Ferramenta Principal: SonarQube

O SonarQube (também SonarCloud para SaaS) é um dos SASTs mais adotados. Analisa código em múltiplas linguagens e sinaliza:
- Possíveis injeções SQL
- Vulnerabilidades XSS
- Secrets hardcoded
- Code smells e bugs além de segurança

## Limitações

SAST é análise **estática** — não observa o comportamento real em runtime:
- Falsos positivos frequentes (código que parece vulnerável mas não é no contexto real)
- Falsos negativos para vulnerabilidades lógicas (business logic bugs)
- Não detecta ataques em tempo real

Por isso deve ser combinado com outras camadas:

| Ferramenta | Quando atua | O que detecta |
|---|---|---|
| **SAST** | Durante desenvolvimento | Padrões vulneráveis no código |
| **DAST** | Após deploy (runtime) | Comportamento real da aplicação |
| **SCA** | No build | CVEs em dependências (ex: Dependabot) |
| **WAF** | Em produção (runtime) | Ataques HTTP em tempo real |

## No Pipeline

```yaml
# Exemplo conceitual de CI
- step: sast
  run: sonarqube-scanner
  on-failure: block-merge
```

SAST no CI transforma segurança em gate de qualidade — nenhum código com vulnerabilidade conhecida passa para produção sem ser revisado.

## Relação com Outros Conceitos

- [[defense-in-depth]] — SAST é a camada de desenvolvimento; WAF é a camada de runtime
- [[waf]] — complementar ao SAST: SAST age antes do deploy, WAF age em produção
- [[attack-surface]] — SAST ajuda a identificar e reduzir superfície de ataque no código
- [[sql-injection]], [[xss]] — classes de vulnerabilidade que SAST detecta estaticamente

## Key Sources

- [[sources/cinco-praticas-seguranca-pragmatic-programmer]] — SAST + WAF como camadas complementares; SonarQube como exemplo de ferramenta
