---
type: concept
title: "IDOR / BOLA (Insecure Direct Object Reference)"
aliases: ["idor", "bola", "broken object level authorization", "insecure direct object reference"]
date_created: 2026-07-04
date_updated: 2026-07-04
source_count: 2
tags: [idor, bola, owasp, api-security, broken-access-control, appsec]
skill: tech-mentor-security
status: stable
---

# IDOR / BOLA (Insecure Direct Object Reference)

Vulnerabilidade onde a aplicação expõe um recurso por ID (na URL ou no body) e não verifica se o usuário autenticado tem permissão sobre aquele objeto específico. É a #1 do OWASP API Top 10, onde é chamada **BOLA** (Broken Object Level Authorization) — IDOR é o nome mais antigo/genérico da mesma falha.

## O padrão do bug

```
GET /purchase/123
→ retorna os detalhes da compra 123, sem checar se ela pertence ao usuário autenticado
```

Variante mais perigosa: o identificador do **próprio usuário** vindo do corpo da requisição em vez da sessão:

```
PATCH /profile { "userId": "456", "bio": "..." }
→ se o servidor usa o userId do body para decidir o que editar,
  qualquer usuário autenticado pode editar o perfil de outro
```

## Correção

- O ID do objeto acessado deve ser sempre cruzado com o ID do usuário autenticado: `WHERE id = $1 AND user_id = $2`.
- O ID do **usuário que faz a requisição** nunca deve vir do body — sempre da sessão/JWT.
- UUIDs aleatórios dificultam enumeração mas não substituem a checagem de autorização — são defesa complementar, não a solução.

## Ver também

- [[wiki/concepts/rate-limiting]] — outra defesa de borda para APIs (BOPLA/API4 é frequentemente citado junto com BOLA)
- [[wiki/concepts/mass-assignment]] — falha irmã: mesmo padrão de "confiar em ID/campo vindo do cliente", mas em escrita em vez de leitura
- [[wiki/concepts/attack-surface]] — toda rota que aceita ID por parâmetro é um ponto de entrada a proteger

## Teste Prático como Pergunta de Autopentest

[[wiki/sources/testes-de-seguranca-pentest-com-claude-code-pulsar-saas]] descreve o mesmo teste em formato de pergunta guia ("você pode fazer isso?"): usuário A com `user_id = 123` tentando um `DELETE` sobre o recurso do usuário B (`user_id = 234`) deve sempre falhar. A fonte trata isso como teste obrigatório antes de publicar qualquer SaaS, conduzido com apoio de IA (Claude Code) mas com o desenvolvedor entendendo cada verificação — não apenas aceitando um relatório automático.

## Key Sources

- [[wiki/sources/owasp-top10]]
- [[wiki/sources/api-security]]
- [[wiki/sources/vulnerabilidades-comuns-seguranca-apps]]
- [[wiki/sources/testes-de-seguranca-pentest-com-claude-code-pulsar-saas]]
