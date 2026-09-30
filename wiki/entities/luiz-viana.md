---
type: entity
title: "Luiz Viana"
aliases: ["Luiz Viana"]
date_created: 2026-08-19
date_updated: 2026-09-30
source_count: 2
tags: [tech-mentor-security, pentest, xss, sql-injection, sqlmap, bug-bounty, dvwa]
skill: tech-mentor-security
status: draft
---

# Luiz Viana

Especialista em hacking e pentest, autor de [[wiki/sources/xss-cross-site-scripting-luiz-viana]] — vídeo prático sobre [[wiki/concepts/xss]] usando o laboratório [[wiki/concepts/dvwa]]. Demonstra os três tipos de XSS (reflected, stored, DOM-based) e técnicas de bypass de filtro nos quatro níveis de segurança do laboratório, reforçando que testes de segurança só devem ser feitos com permissão explícita e citando [[wiki/concepts/bug-bounty]] como caminho legítimo para monetizar a habilidade.

## SQL Injection com SQLMap

Em [[wiki/sources/sql-injection-sqlmap-luiz-viana]], mesmo formato de curso: explica [[wiki/concepts/sql-injection]] do zero (mecanismo da aspa simples que quebra a query) e depois automatiza detecção/exploração com [[wiki/concepts/sqlmap]] contra um laboratório numerado por "lessons" — cobrindo taxonomia de técnicas de blind injection ([[wiki/concepts/sql-injection-tecnicas-de-exploracao]]), leitura de arquivo no servidor ([[wiki/concepts/load-file-into-outfile-mysql]]), os parâmetros `--level`/`--risk`, injeção via POST e cookie, e bypass de [[wiki/concepts/waf]]. Repete o mesmo princípio pedagógico do vídeo de XSS: ferramenta de automação sem entendimento da exploração manual é inútil.

## Key Sources

- [[wiki/sources/xss-cross-site-scripting-luiz-viana]]
- [[wiki/sources/sql-injection-sqlmap-luiz-viana]]
