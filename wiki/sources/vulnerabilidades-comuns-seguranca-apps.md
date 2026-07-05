---
type: source
title: "Vulnerabilidades Comuns de Segurança em Apps/SaaS"
aliases: ["vulnerabilidades comuns seguranca apps", "webhook idor mass assignment toctou", "confiar no frontend"]
date_created: 2026-07-04
date_updated: 2026-07-04
source_file: /home/nemomartins/Documentos/dev-brain/raw/vulnerabilidades-comuns-seguranca-apps.md
source_url: ""
date_published: ""
date_ingested: 2026-07-04
source_count: 0
tags: [appsec, idor, bola, mass-assignment, webhook, toctou, race-condition, data-exposure, rate-limiting, client-side-security]
skill: tech-mentor-security
status: stable
---

## TL;DR

Vídeo (transcrição) sobre as vulnerabilidades mais comuns em apps/SaaS — fora do escopo de grandes CVEs, focando em erros de lógica de aplicação: webhook sem validação de assinatura, IDOR/BOLA, exposição excessiva de dados, ausência de rate limiting, mass assignment, TOCTOU (race condition em operações financeiras) e a falha raiz de "confiar no frontend" para regras de negócio. Demonstração prática de bypass client-side via DevTools/breakpoint.

## Key Claims

**Claim:** Webhooks sem validação de assinatura permitem forjar eventos de pagamento.
**Evidence:** Rotas de webhook costumam usar paths previsíveis (`/api/webhook`, `/api/hook`), permitindo enumeração. Sem validar o cabeçalho de assinatura (`Stripe-Signature`, `X-Signature` no Mercado Pago), um atacante pode enviar uma requisição forjada simulando confirmação de compra.
**Confidence:** alta — consistente com `references/appsec-js-vulns.md` (HMAC + `timingSafeEqual` + replay prevention via timestamp).

**Claim:** IDOR/BOLA ocorre quando o ID do recurso vem da requisição sem checar ownership, e é agravado quando o ID do usuário também vem do body em vez da sessão/JWT.
**Evidence:** Exemplo dado: `GET /purchase/:id` retornando dados de qualquer compra pelo ID, e `PATCH /profile` recebendo `userId` no body — permitindo que o requisitante edite o perfil de outro usuário.
**Confidence:** alta — mesma vulnerabilidade #1 do OWASP API Top 10, já documentada em [[wiki/sources/owasp-top10]] e [[wiki/sources/api-security]].

**Claim:** Retornar objetos completos do backend (sem projeção de campos) vaza dados sensíveis mesmo quando o frontend não os exibe.
**Evidence:** Endpoint de produto de marketplace retornando o vendedor completo (nome, foto, e-mail, CPF, telefone, endereço, senha criptografada) porque a query buscou a entidade inteira em vez de projetar apenas os campos exibidos.
**Confidence:** alta — reforça o princípio de minimização de dados: nunca confiar que o frontend vai "filtrar" o que exibe.

**Claim:** TOCTOU (Time of Check to Time of Use) em operações financeiras permite múltiplos saques com um único saldo, quando requisições concorrentes passam pelo check de saldo antes de qualquer uma processar o saque.
**Evidence:** Exemplo do saque de R$100 disparado em paralelo — delay de rede naturalmente faz múltiplas requisições chegarem quase simultaneamente, cada uma vendo o saldo ainda intacto. Correção: transactions atômicas no banco (ou locks/semáforos/filas) garantindo que check+use aconteçam como operação única.
**Confidence:** alta — é uma race condition clássica de sistema, distinta da [[wiki/concepts/race-condition]] de frontend (fetch fora de ordem em React); aqui o problema é concorrência no backend sobre um recurso compartilhado (saldo).

**Claim:** Toda regra de negócio validada só no frontend (preço, saldo, permissão de botão) pode ser contornada manipulando variáveis client-side via DevTools/debugger.
**Evidence:** Demonstração prática: localizar a condição de renderização que habilita um botão de saque, colocar um breakpoint, e alterar manualmente as variáveis (`amount`, uma flag booleana) para forçar a UI a liberar uma ação sem saldo real. A requisição ao backend só falha porque o servidor reconfere o saldo — se o backend confiasse no valor enviado (ex: preço de produto calculado no frontend), o ataque teria sucesso.
**Confidence:** alta — princípio fundamental de segurança de aplicação: cliente é sempre não confiável; toda validação de negócio deve ser reexecutada no servidor.

**Claim:** Ausência de rate limiting/captcha em rotas públicas gera custo financeiro direto, não só risco de segurança.
**Evidence:** Exemplos dados: POST público sem limite permite criação em massa de registros falsos (custo de armazenamento); API de envio de e-mail sem limite permite esgotar cota paga do provedor de e-mail; login sem proteção permite brute force de senha.
**Confidence:** alta — consistente com `references/appsec-api.md` (API4 — Unrestricted Resource Consumption) e [[wiki/concepts/rate-limiting]].

## Entities & Concepts Touched

- [[wiki/concepts/idor]]
- [[wiki/concepts/mass-assignment]]
- [[wiki/concepts/webhook-signature-validation]]
- [[wiki/concepts/exposicao-excessiva-de-dados]]
- [[wiki/concepts/toctou]]
- [[wiki/concepts/confiar-no-frontend]]
- [[wiki/concepts/rate-limiting]]
- [[wiki/concepts/race-condition]]
- [[wiki/concepts/timing-attack]]
- [[wiki/concepts/attack-surface]]

## Open Questions

- Fonte não cita ferramentas de detecção automatizada (Schemathesis, Burp Turbo Intruder) para IDOR/BOLA em CI — como a equipe testaria isso sistematicamente?
- Não há exemplo de locking distribuído (Redis lock, `SELECT FOR UPDATE`) para o caso de TOCTOU fora de um único banco transacional — relevante em arquitetura com múltiplos serviços.
