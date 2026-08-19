---
type: concept
title: "DVWA (Damn Vulnerable Web Application)"
aliases: ["dvwa", "damn vulnerable web application"]
date_created: 2026-08-19
date_updated: 2026-08-19
source_count: 1
tags: [dvwa, pentest, xss, sql-injection, security-training, ctf]
skill: tech-mentor-security
status: stub
---

# DVWA (Damn Vulnerable Web Application)

Aplicação web deliberadamente vulnerável, usada como laboratório de treino para praticar exploração de falhas de [[wiki/concepts/attack-surface|segurança]] em ambiente controlado e legal. Cobre as classes de vulnerabilidade mais comuns — [[wiki/concepts/xss]], [[wiki/concepts/sql-injection]], IDOR, upload arbitrário, entre outras.

## Níveis de Segurança

O DVWA expõe um seletor de dificuldade (`DVWA Security`) com quatro níveis por vulnerabilidade:

| Nível | Comportamento típico |
|---|---|
| **low** | Nenhum filtro — payload básico funciona direto |
| **medium** | Filtro simples (ex.: blocklist de uma tag/palavra específica) — contornável trocando o vetor |
| **high** | Filtro mais amplo, ainda contornável com técnicas mais específicas |
| **impossible** | Mitigação correta (sanitização/output encoding real, queries parametrizadas) — não contornável pelos vetores comuns |

A progressão por nível é o valor didático central: mostra que "ter um filtro" não é o mesmo que "estar protegido" — a diferença entre medium/high e impossible costuma ser a diferença entre blocklist (frágil) e allowlist/encoding (robusto).

## Relação com Outros Conceitos

- [[wiki/concepts/xss]] — laboratórios dedicados de reflected, stored e DOM-based XSS
- [[wiki/concepts/sql-injection]] — laboratório clássico de injeção via parâmetro de rota/formulário
- [[wiki/concepts/bug-bounty]] — treino prático recomendado antes de procurar falhas reais em programas de bug bounty
- [[wiki/entities/solyd]] — plataforma citada disponibilizando o ambiente DVWA como máquina isolada sob demanda

## Key Sources

- [[wiki/sources/xss-cross-site-scripting-luiz-viana]] — demonstração completa dos três tipos de XSS nos quatro níveis de segurança do DVWA
