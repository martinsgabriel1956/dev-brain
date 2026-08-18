---
type: concept
title: "Sessões HTTP e Cookies"
aliases: ["sessão HTTP", "session ID", "cookie de sessão", "sessão stateful"]
date_created: 2026-07-27
date_updated: 2026-08-14
source_count: 4
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
- **Regenerar o ID após login**: previne [[wiki/concepts/session-fixation|session fixation]] (atacante força uma sessão conhecida antes do usuário autenticar).

## Invalidar Sessões Antigas ao Trocar a Senha

Trocar a senha não revoga automaticamente sessões já ativas. Se um atacante já tinha roubado uma sessão antes da troca, ela continua válida normalmente — a senha nova não afeta um session ID já emitido. Por isso, toda troca de senha precisa invalidar explicitamente **todas** as sessões existentes do usuário, forçando um novo login em qualquer dispositivo.

## Onde Armazenar a Sessão no Servidor

| Onde | Vantagem | Limite |
|---|---|---|
| Memória do processo | Mais rápido | Perdida se o servidor reiniciar; não funciona com múltiplas instâncias |
| Banco de dados | Persistente | Cada requisição vira uma consulta extra |
| Redis | Rápido e compartilhado entre servidores | Dependência central adicional (ver seção abaixo) |

Redis é o padrão de produção justamente por resolver o caso de múltiplos servidores atrás de um load balancer: sem um armazenamento compartilhado, a sessão só existe no servidor que a criou, e a próxima requisição — que pode cair em outro servidor do pool — não reconhece o usuário.

## Teste de CSRF em Autopentest

[[wiki/sources/testes-de-seguranca-pentest-com-claude-code-pulsar-saas]] enquadra o teste de CSRF como a pergunta "meu navegador pode me sacanear?": verificar que não é possível disparar uma ação autenticada no sistema a partir de um link ou botão malicioso hospedado fora do domínio da aplicação. É a contrapartida prática do atributo `SameSite` já documentado acima — o teste confirma que a defesa (`SameSite=Strict`/`Lax`, ou token CSRF explícito) realmente bloqueia a falsificação, em vez de assumir que está configurada corretamente.

## Relação com outros conceitos

- [[wiki/concepts/jwt]] — alternativa stateless que elimina a dependência central de armazenamento de sessão
- [[wiki/concepts/criptografia]] — cookie de sessão em si não é criptografado, apenas um identificador opaco; a segurança vem de HttpOnly/Secure/SameSite, não de criptografia do valor

## Relação com outros conceitos (cont.)

- [[wiki/concepts/session-fixation]] — ataque específico contra a regeneração de session ID
- [[wiki/concepts/step-up-authentication]] — uma sessão válida não deve ser suficiente para ações sensíveis, mesmo sem session fixation

## Key Sources

- [[wiki/sources/historia-autenticacao-senha-mfa-oauth-jwt]]
- [[wiki/sources/testes-de-seguranca-pentest-com-claude-code-pulsar-saas]]
- [[wiki/sources/autenticacao-moderna-senha-sessao-jwt-oauth-mfa-passkeys]] — invalidação ao trocar senha; comparação memória vs. banco vs. Redis para armazenamento de sessão
- [[wiki/sources/refresh-token-pattern-access-token-de-curta-duracao]] — cookie `HttpOnly` recomendado especificamente para o refresh token, comparado com `localStorage` e armazenamento em memória/estado da aplicação
