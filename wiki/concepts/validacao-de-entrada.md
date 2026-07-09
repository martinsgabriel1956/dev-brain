---
type: concept
title: "Validação de Entrada"
aliases: ["input validation", "validação de dados", "nunca confie no client"]
date_created: 2026-07-09
date_updated: 2026-07-09
source_count: 1
tags: [validacao, seguranca, backend, regra-de-negocio, arquitetura-em-camadas]
skill: tech-mentor-backend
status: stub
---

# Validação de Entrada

O backend nunca pode confiar no que vem do cliente. Quantidade negativa, e-mail malformado, preço recalculável a partir do que o cliente mandou — tudo isso precisa ser barrado ou recalculado antes de tocar a regra de negócio.

## Separação em camadas

Uma forma comum de organizar essa proteção:

| Camada | Responsabilidade |
|---|---|
| Controller | Entende de HTTP — parse, status codes |
| Service | Entende de regra de negócio — validação, cálculo |
| Banco | Guarda os dados |

Essa separação evita que a regra crítica se espalhe por múltiplos lugares do código. Quando a regra fica espalhada, o sistema pode começar a se contradizer — dois pontos de entrada validando a mesma coisa de formas diferentes.

## Relação com outros conceitos

- [[wiki/concepts/contrato-de-api]] — o contrato define o formato esperado; a validação garante que ele é respeitado em runtime
- [[wiki/concepts/autenticacao-e-autorizacao]] — validação de identidade/permissão é uma forma específica de validação de entrada
- Ver detalhamento em `references/api-design.md` e `references/cors-security.md` (tech-mentor-backend) para validação na borda (input sanitization, output encoding)

## Key sources

- [[wiki/sources/10-conceitos-fundamentais-backend]]
