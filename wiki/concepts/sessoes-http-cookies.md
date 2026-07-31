---
type: concept
title: "Sessões HTTP e Cookies"
aliases: ["sessão HTTP", "session ID", "cookie de sessão", "sessão stateful"]
date_created: 2026-07-27
date_updated: 2026-07-31
source_count: 2
tags: [sessao, cookie, autenticacao, stateless, http, seguranca]
skill: tech-mentor-security
status: draft
---

# Sessões HTTP e Cookies

Solução clássica para o problema de HTTP ser um protocolo **sem estado**: cada requisição é independente, o servidor não guarda contexto entre elas. Sem algum mecanismo, o servidor não sabe se a próxima requisição vem do mesmo usuário que acabou de fazer login.

## Como funciona

```
1. Login: servidor verifica credenciais
2. Servidor cria uma entrada no banco (a sessão) — ID único + dados do usuário/permissões
3. Servidor envia o ID de volta ao cliente, guardado em um cookie
4. Toda requisição seguinte: browser envia o cookie automaticamente
5. Servidor pega o ID, consulta o banco/cache de sessões, descobre quem é o usuário
```

## O limite: dependência central

Em arquitetura com múltiplos servidores, todos precisam acessar o **mesmo** armazenamento de sessões (tipicamente Redis). Isso funciona, mas cria uma dependência central: se esse armazenamento cai, a autenticação de todo o sistema cai junto. É o motivo pelo qual arquiteturas distribuídas migram para tokens stateless como [[wiki/concepts/jwt]], que carregam a própria informação de identidade sem consulta central.

## Segurança do cookie

- **`HttpOnly`**: inacessível via JavaScript — protege contra roubo de sessão por XSS.
- **`Secure`**: só trafega em HTTPS.
- **`SameSite`**: mitiga CSRF (`Strict` bloqueia todo cross-site; `Lax` permite navegação top-level).
- **Regenerar o ID após login**: previne *session fixation* (atacante força uma sessão conhecida antes do usuário autenticar).

## Teste de CSRF em Autopentest

[[wiki/sources/testes-de-seguranca-pentest-com-claude-code-pulsar-saas]] enquadra o teste de CSRF como a pergunta "meu navegador pode me sacanear?": verificar que não é possível disparar uma ação autenticada no sistema a partir de um link ou botão malicioso hospedado fora do domínio da aplicação. É a contrapartida prática do atributo `SameSite` já documentado acima — o teste confirma que a defesa (`SameSite=Strict`/`Lax`, ou token CSRF explícito) realmente bloqueia a falsificação, em vez de assumir que está configurada corretamente.

## Relação com outros conceitos

- [[wiki/concepts/jwt]] — alternativa stateless que elimina a dependência central de armazenamento de sessão
- [[wiki/concepts/criptografia]] — cookie de sessão em si não é criptografado, apenas um identificador opaco; a segurança vem de HttpOnly/Secure/SameSite, não de criptografia do valor

## Key Sources

- [[wiki/sources/historia-autenticacao-senha-mfa-oauth-jwt]]
- [[wiki/sources/testes-de-seguranca-pentest-com-claude-code-pulsar-saas]]
