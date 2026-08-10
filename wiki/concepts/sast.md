---
type: concept
title: "SAST (Static Application Security Testing)"
aliases: ["sast", "static application security testing", "análise estática de segurança", "sonarqube"]
date_created: 2026-06-10
date_updated: 2026-08-06
source_count: 3
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

## SAST no Delta, a Cada Rodada de Refinamento com IA

[[wiki/sources/codigo-gerado-por-ia-mais-falhas-seguranca-degradacao-iterativa]] propõe um uso mais granular de SAST especificamente para código gerado/refinado por IA: rodar a análise **antes e depois de cada modificação**, e revisar apenas o *delta* entre os dois relatórios — não o código inteiro de novo a cada vez. A motivação é o achado de [[wiki/concepts/degradacao-de-seguranca-iterativa-ia]]: pedir para uma IA refinar código repetidamente tende a piorar a segurança (37,6% mais vulnerabilidades críticas depois de 5 rodadas, num paper citado pela fonte), então esperar até o final do ciclo de iteração para rodar SAST uma única vez deixa passar degradação acumulada que um checkpoint por rodada pegaria mais cedo e mais barato.

## Relação com Outros Conceitos

- [[defense-in-depth]] — SAST é a camada de desenvolvimento; WAF é a camada de runtime
- [[waf]] — complementar ao SAST: SAST age antes do deploy, WAF age em produção
- [[attack-surface]] — SAST ajuda a identificar e reduzir superfície de ataque no código
- [[sql-injection]], [[xss]] — classes de vulnerabilidade que SAST detecta estaticamente
- [[wiki/concepts/degradacao-de-seguranca-iterativa-ia]] — motivação para rodar SAST a cada rodada de refinamento com IA, não só uma vez no fim

## Key Sources

- [[sources/cinco-praticas-seguranca-pragmatic-programmer]] — SAST + WAF como camadas complementares; SonarQube como exemplo de ferramenta
- [[wiki/sources/devsecops-origem-cultura-manifesto]] — SAST como parte do mapeamento de ferramentas por fase do ciclo DevSecOps (build/código), dentro da abordagem [[wiki/concepts/shift-left-testing]]
- [[wiki/sources/codigo-gerado-por-ia-mais-falhas-seguranca-degradacao-iterativa]] — SAST no delta, a cada rodada de refinamento com IA, como mitigação para degradação de segurança iterativa
