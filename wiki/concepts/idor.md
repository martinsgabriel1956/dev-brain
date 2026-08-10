---
type: concept
title: "IDOR / BOLA (Insecure Direct Object Reference)"
aliases: ["idor", "bola", "broken object level authorization", "insecure direct object reference"]
date_created: 2026-07-04
date_updated: 2026-08-06
source_count: 4
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

## Encadeando IDOR em Account Takeover e Escalonamento de Privilégio

[[wiki/sources/vibe-coding-env-exposto-idor-account-takeover-rce-loja-ia]] demonstra que o impacto de um IDOR depende do que o endpoint vazado expõe. Nesta fonte, dois IDORs no mesmo padrão (ID sequencial no perfil de usuário) têm impactos muito diferentes:

- Vazar nome/e-mail/endereço de outro pedido é exposição de dados.
- Vazar a **chave de integração** do perfil de outro usuário é [[wiki/concepts/account-takeover|account takeover]] — a chave sozinha autentica no endpoint de login e gera um cookie de sessão válido, sem senha e sem MFA.

A partir daí, o mesmo IDOR foi escalado de manual para automatizado: a requisição de perfil foi enviada ao Burp Intruder com o ID como payload numérico (1 a 15), usando "Grep - Extract" para capturar o campo `role` de cada resposta. O único ID sem `role: user` revelou o perfil do administrador do sistema — cuja chave de integração, usada da mesma forma, gerou um cookie de sessão administrativa. Uma falha de autorização simples, sem nenhuma defesa de rate limiting observada, foi suficiente para ir de usuário anônimo a administrador em poucos minutos.

## UUID como Mitigação Parcial (não substitui autorização)

[[wiki/sources/uuid-quando-usar-pergunta-diogo]] discute o mesmo padrão de vulnerabilidade a partir do lado da modelagem de dados: URLs de API REST com ID sequencial (`/organizacoes/1/usuarios/2`) permitem que um usuário autenticado varie o número e acesse dados de outro cliente/usuário, principalmente em sistemas multi-tenant com tabelas compartilhadas. A fonte reforça o mesmo ponto já registrado acima — [[wiki/concepts/uuid|UUID]] dificulta a enumeração, mas não substitui a validação de autorização em cada referência entre entidades (cada chave estrangeira precisa ser cruzada com as permissões do usuário autenticado). A fonte também descreve um caso de uso legítimo do UUID como "senha implícita" de recurso não autenticado — ex.: comprovante de compra acessível só por link, sem login.

## Ver também

- [[wiki/concepts/rate-limiting]] — outra defesa de borda para APIs (BOPLA/API4 é frequentemente citado junto com BOLA); ausência de rate limiting é o que permite a enumeração automatizada acima
- [[wiki/concepts/account-takeover]] — quando o dado exposto pelo IDOR é uma credencial, não apenas informação
- [[wiki/concepts/attack-surface]] — IDs sequenciais como superfície de ataque
- [[wiki/concepts/uuid]] — mitigação parcial de enumeração; ver também o argumento de merge de bases shardeadas

## Key Sources

- [[wiki/sources/vibe-coding-env-exposto-idor-account-takeover-rce-loja-ia]]
- [[wiki/concepts/mass-assignment]] — falha irmã: mesmo padrão de "confiar em ID/campo vindo do cliente", mas em escrita em vez de leitura
- [[wiki/concepts/attack-surface]] — toda rota que aceita ID por parâmetro é um ponto de entrada a proteger

## Teste Prático como Pergunta de Autopentest

[[wiki/sources/testes-de-seguranca-pentest-com-claude-code-pulsar-saas]] descreve o mesmo teste em formato de pergunta guia ("você pode fazer isso?"): usuário A com `user_id = 123` tentando um `DELETE` sobre o recurso do usuário B (`user_id = 234`) deve sempre falhar. A fonte trata isso como teste obrigatório antes de publicar qualquer SaaS, conduzido com apoio de IA (Claude Code) mas com o desenvolvedor entendendo cada verificação — não apenas aceitando um relatório automático.

## Key Sources

- [[wiki/sources/owasp-top10]]
- [[wiki/sources/api-security]]
- [[wiki/sources/vulnerabilidades-comuns-seguranca-apps]]
- [[wiki/sources/testes-de-seguranca-pentest-com-claude-code-pulsar-saas]]
- [[wiki/sources/uuid-quando-usar-pergunta-diogo]]
