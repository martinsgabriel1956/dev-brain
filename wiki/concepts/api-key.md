---
type: concept
title: "API Key"
aliases: ["API Key", "chave de serviço", "service key"]
date_created: 2026-09-14
date_updated: 2026-09-14
source_count: 1
tags: [api-key, token, autenticacao, b2b, seguranca]
skill: tech-mentor-security
status: draft
---

# API Key

Identificador secreto usado para autenticar **aplicações** consumindo uma API — diferente de um token de usuário, que autentica uma pessoa. É um tipo de [[wiki/concepts/token-opaco|token opaco]]: enviada tipicamente em um header da requisição, permite que a API identifique qual serviço/cliente está fazendo aquela chamada.

Comum em integrações sistema-a-sistema, cenários B2B, e serviços públicos que precisam controlar uso (APIs de mapas, pagamento, envio de e-mail, IA). Também chamada de **chave de serviço**.

## Vantagem: Simplicidade

Fácil de gerar, distribuir e validar — uma requisição com o header correto já basta. Não exige fluxo de login, redirecionamento, ou emissão de tokens temporários como o [[wiki/concepts/oauth2|Authorization Code Flow]] do OAuth. Isso reduz a complexidade de integrações técnicas e automações.

## Risco: Vazamento

Se a chave vazar, qualquer pessoa pode usá-la até que seja revogada — não há vínculo com identidade de usuário nem escopo dinâmico por padrão.

## Boas Práticas

- Armazenar com segurança (nunca hardcoded em repositório público).
- Nunca expor em frontend público — uma API key em JavaScript client-side é visível a qualquer visitante.
- Sempre usar HTTPS.
- Rotação periódica da chave.
- Em sistemas maduros, combinar com camadas adicionais (ex. mTLS) para reduzir a superfície de ataque.

## Relação com outros conceitos

- [[wiki/concepts/token-opaco]] — categoria arquitetural à qual a API key pertence
- [[wiki/concepts/oauth2]] — alternativa mais complexa quando é preciso delegar acesso em nome de um usuário (não apenas autenticar uma aplicação)

## Key Sources

- [[wiki/sources/anatomia-de-um-token-1-opaco-vs-autocontido-bernardo-lobato]] — definição, vantagem de simplicidade, risco de vazamento, boas práticas de armazenamento/rotação/mTLS
