---
type: concept
title: "Validação de Entrada"
aliases: ["input validation", "validação de dados", "nunca confie no client"]
date_created: 2026-07-09
date_updated: 2026-07-30
source_count: 3
tags: [validacao, seguranca, backend, regra-de-negocio, arquitetura-em-camadas, celebrate, joi, schema-validation]
skill: tech-mentor-backend
status: stub
---

# Validação de Entrada

O backend nunca pode confiar no que vem do cliente. Quantidade negativa, e-mail malformado, preço recalculável a partir do que o cliente mandou — tudo isso precisa ser barrado ou recalculado antes de tocar a regra de negócio.

## Caso concreto: validação de e-mail

"E-mail malformado" não é um conceito único — [[wiki/sources/email-address]] mostra que a spec formal (RFC 5322/5321) e a prática de mercado divergem em pontos que uma validação ingênua costuma errar:

- A parte local é *tecnicamente* case-sensitive pela RFC, mas todo provedor trata como case-insensitive na prática — validar case-sensitivity estrita rejeita endereços válidos por convenção de mercado.
- `user+tag@domain.com` (sub-addressing, RFC 5233) é sintaxe formalmente válida e suportada por Gmail, Outlook.com, Yahoo Mail Plus, iCloud e Proton Mail — uma regex que rejeita `+` na parte local está rejeitando endereços reais.
- Correção sintática (regex, HTML5 form validation) **não prova** que a caixa existe. A única validação confiável de existência é um link de confirmação enviado ao próprio endereço — callback verification direta (conectar na caixa e checar) existe mas arrisca directory harvest attacks e denúncias de spam.

## Separação em camadas

Uma forma comum de organizar essa proteção:

| Camada | Responsabilidade |
|---|---|
| Controller | Entende de HTTP — parse, status codes |
| Service | Entende de regra de negócio — validação, cálculo |
| Banco | Guarda os dados |

Essa separação evita que a regra crítica se espalhe por múltiplos lugares do código. Quando a regra fica espalhada, o sistema pode começar a se contradizer — dois pontos de entrada validando a mesma coisa de formas diferentes.

## Validação de Schema como Middleware (Celebrate + Joi)

Em Node/Express, uma forma concreta de aplicar essa camada é um middleware de validação de schema entre a rota e o handler: **Celebrate** (usando **Joi** para descrever o schema) verifica, antes de qualquer lógica rodar, se cada segmento da requisição (params, query, body) bate com o tipo/formato esperado — ex.: `celebrate({ [Segments.PARAMS]: Joi.object({ id: Joi.number() }) })` garante que `id` só pode ser número. Se vier fora do formato (ex.: uma tentativa de [[wiki/concepts/sql-injection]] como `1 OR 1=1`), a requisição é rejeitada com erro antes de tocar o banco. Ver demonstração completa em [[wiki/sources/injecao-sql-aula-modulo-seguranca]].

Essa camada **não substitui** a query parametrizada (placeholders `$1`/`$2`) — é defesa adicional na borda, mesma lógica de "nunca confiar no client" já descrita acima.

## Relação com outros conceitos

- [[wiki/concepts/contrato-de-api]] — o contrato define o formato esperado; a validação garante que ele é respeitado em runtime
- [[wiki/concepts/autenticacao-e-autorizacao]] — validação de identidade/permissão é uma forma específica de validação de entrada
- [[wiki/concepts/sql-injection]] — validação de schema é camada adicional, não substituta, da parametrização de query
- Ver detalhamento em `references/api-design.md` e `references/cors-security.md` (tech-mentor-backend) para validação na borda (input sanitization, output encoding)

## Key sources

- [[wiki/sources/10-conceitos-fundamentais-backend]]
- [[wiki/sources/injecao-sql-aula-modulo-seguranca]] — exemplo prático de validação de schema (Celebrate/Joi) como camada extra contra SQL Injection
- [[wiki/sources/email-address]] — sintaxe formal RFC 5322 de e-mail vs. práticas reais de validação de provedores
