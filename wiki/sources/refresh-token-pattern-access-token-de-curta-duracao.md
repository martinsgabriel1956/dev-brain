---
type: source
title: "Refresh Token: como manter o access token curto e o usuário logado com segurança"
aliases: ["refresh token pattern", "refresh token rotation", "access token curta duração", "janela de exposição"]
date_created: 2026-08-14
date_updated: 2026-08-14
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/refresh-token-pattern-access-token-de-curta-duracao.md
source_url: ""
author: "Bernardo Lobato"
date_published: ""
date_ingested: 2026-08-14
source_count: 0
tags: [jwt, refresh-token, oauth2, autenticacao, autorizacao, seguranca, stateless, stateful, httponly-cookie, refresh-token-rotation, device-fingerprinting]
skill: tech-mentor-security
status: stable
---

## TL;DR

Access token JWT de longa duração (ex.: 1 ano) é uma falha de segurança: por ser stateless e auto-contido, ele trafega por logs, VPNs, load balancers, e não pode ser revogado antes de expirar — quem o rouba tem acesso pelo tempo total de validade. O padrão correto é combinar dois tokens: access token curto (5-15min, stateless, enviado em toda requisição) + refresh token de vida longa (dias/semanas, stateful, guardado no servidor/authorization server, revogável, usado só para renovar o access token via um endpoint dedicado quando a API retorna `401`). O refresh token deve ser armazenado em cookie `HttpOnly` (nunca `localStorage` — vulnerável a XSS) e reforçado com duas camadas extras: **rotation** (cada uso invalida o token antigo e emite um novo; reapresentação de um token já rotacionado é sinal de roubo e dispara revogação de toda a família de tokens) e **fingerprinting** (vincular o refresh token a um user agent/hash de dispositivo capturado no login; renovação a partir de um dispositivo diferente é bloqueada).

## Key Claims

**Claim:** Access token JWT de validade longa (ex.: 1 ano) é uma falha de segurança em produção porque o token é stateless, auto-contido e não revogável antes de expirar.
**Evidence:** Sendo stateless, o servidor só checa a assinatura — não há como invalidar antes do prazo sem reintroduzir estado (denylist). O token trafega por logs de servidor, pode ficar em consoles, atravessa VPNs e load balancers em rede corporativa. Se vazado em qualquer um desses pontos, um atacante tem o prazo inteiro (1 ano no exemplo) para usá-lo livremente — inclusive via ferramentas como Postman, já que o esquema `Bearer` dá posse total a quem porta o token.
**Confidence:** alta — consistente com [[wiki/concepts/jwt]] § "O problema da revogação".

**Claim:** O padrão correto combina access token curto (stateless) + refresh token de vida longa (stateful, revogável), trocados via endpoints e campos distintos (`access_token`, `refresh_token`, `expires_in`, `token_type: Bearer`).
**Evidence:** Access token dura 5-15min e vai em toda requisição no header `Authorization`. Refresh token dura dias/semanas, fica guardado no servidor (authorization server), e só é enviado ao endpoint de renovação quando o access token expira. Fluxo: (1) login retorna os dois tokens; (2) access token expira → API retorna `401`; (3) frontend intercepta o 401 (via interceptor HTTP/Axios), usa o refresh token guardado para pedir um novo access token num endpoint diferente do login; (4) a requisição original é refeita com sucesso — tudo de forma transparente ao usuário.
**Confidence:** alta.

**Claim:** Tornar o access token stateful (validado no banco a cada request) resolveria a revogação, mas cria um gargalo de performance que mata a escalabilidade da API.
**Evidence:** Com 1000 req/s, tornar o access token stateful significa 1000 validações no banco/authorization server por segundo. Mantendo-o stateless, a validação central só acontece nos momentos em que ele expira e precisa ser renovado via refresh token — daí o refresh token ser o único componente que compensa ser stateful.
**Confidence:** alta — mesmo trade-off central de [[wiki/concepts/stateless]].

**Claim:** "Janela de exposição" é o risco residual aceito ao manter o access token stateless: um usuário banido/revogado continua com acesso até o access token expirar (5-15min no pior caso).
**Evidence:** Após a revogação, o refresh token passa a ser recusado no servidor, então o usuário não consegue renovar — mas o access token já emitido continua válido até expirar, pois nada verifica revogação nesse meio-tempo. Para a maioria das aplicações (rede social, e-commerce, backoffice) esse risco é aceito em troca de escalabilidade. Para sistemas de alta criticidade (PIX, Banco Central, tempo real, operações financeiras de alto valor), nem essa janela curta é tolerável, exigindo repensar o modelo de autenticação.
**Confidence:** alta.

**Claim:** O refresh token deve ser armazenado em cookie `HttpOnly`, nunca em `localStorage`, e a aplicação cliente não precisa nem deve acessar seu conteúdo.
**Evidence:** `localStorage` é acessível por qualquer script, tornando o refresh token roubável via XSS. Armazenamento em memória/estado da aplicação (Redux, Angular service) evita XSS mas perde o token a cada F5 — inaceitável para um token cujo propósito é persistir a sessão. Cookie `HttpOnly` é ilegível por JavaScript (bloqueado pelo próprio navegador), o que neutraliza XSS; como o refresh token só precisa "estar lá e ser válido" (nunca ser lido pelo client), essa restrição não é uma limitação — é exatamente a propriedade desejada.
**Confidence:** alta — reforça claim já registrada em [[wiki/concepts/jwt]] § "Onde Armazenar o Token no Cliente", mas aqui aplicada especificamente ao refresh token (não ao access token).

**Claim:** Guardar o refresh token apenas no backend (sem devolver nada ao cliente) quebra o propósito da autenticação stateless: o cliente perde a forma de provar sua identidade na requisição seguinte sem reintroduzir sessão de servidor.
**Evidence:** Sem alguma referência no lado do cliente (o próprio cookie HttpOnly), não há vínculo entre a requisição seguinte e o servidor — seria necessário reintroduzir sessão de servidor, anulando o ganho de ter migrado para tokens.
**Confidence:** média — argumentação lógica do autor, não citada de uma fonte externa.

**Claim:** Refresh token rotation: a cada uso, o token antigo é invalidado e um novo é emitido junto com o novo access token; a reapresentação de um refresh token já rotacionado é tratada como sinal de roubo e pode disparar logout preventivo em todos os dispositivos.
**Evidence:** Sem rotation, um refresh token roubado continua válido pelo prazo inteiro (dias/semanas) mesmo com o dono legítimo usando o sistema normalmente. Com rotation, se o token antigo reaparece (porque um atacante o capturou antes do dono usá-lo, ou vice-versa), a API detecta a reapresentação como fraude — o sistema reage como um alarme automático, revogando a sessão para forçar reautenticação.
**Confidence:** alta — mesma técnica documentada em [[wiki/concepts/jwt]] § "Rotação do Refresh Token" e no `references/appsec-authn-authz.md` da skill `tech-mentor-security`, que a chama de "refresh token reuse detection" com recomendação explícita de revogar "toda a família de tokens".

**Claim:** Fingerprinting/vinculação de dispositivo reforça o refresh token ao amarrar sua validade a um user agent ou hash de dispositivo capturado no login; renovação a partir de um dispositivo diferente é bloqueada.
**Evidence:** No login, o servidor guarda o fingerprint (user agent, hash de dispositivo em mobile) atrelado ao refresh token. Se a renovação chegar de um navegador/dispositivo diferente do capturado, o servidor recusa — mesmo que o token em si seja válido, ele precisa estar "nas mãos de quem o solicitou".
**Confidence:** média — técnica é apresentada como boa prática opcional, sem citar mecanismo específico de coleta/hash; é mais fraca que DPoP (RFC 9449) `[external]`, que amarra o token a uma prova criptográfica de posse de chave privada em vez de um fingerprint de navegador, que pode ser forjado — sem página própria na wiki ainda.

**Claim:** O refresh token deve ser majoritariamente **stateful** (verificável/revogável no authorization server), diferente do access token, que é stateless por design.
**Evidence:** Se o refresh token também fosse stateless, ele herdaria os mesmos problemas de não-revogação do JWT tradicional — anulando o próprio motivo de existir. No OAuth, esse papel de validação/revogação é do authorization server.
**Confidence:** alta.

## Entities & Concepts Touched

- [[wiki/entities/bernardo-lobato]]
- [[wiki/concepts/jwt]] — expandido com claims sobre janela de exposição e distinção explícita access vs. refresh token quanto a onde armazenar
- [[wiki/concepts/refresh-token-rotation]] — conceito novo, criado a partir desta fonte
- [[wiki/concepts/oauth2]] — authorization server como componente que valida/revoga o refresh token
- [[wiki/concepts/stateless]] — trade-off performance vs. revogação
- [[wiki/concepts/sessoes-http-cookies]] — cookie `HttpOnly` como mecanismo de armazenamento seguro
- [[wiki/concepts/xss]] — motivo de excluir `localStorage` como opção de armazenamento

## Open Questions

- O vídeo não detalha como calcular/armazenar o "hash de dispositivo" em mobile para fingerprinting — falta profundidade técnica de implementação.
- Não há discussão de refresh token em apps mobile nativos, onde `HttpOnly` cookie não se aplica da mesma forma (keychain/keystore são a alternativa) — ponto em aberto para complementar esta fonte no futuro.

## Quotes

> "Se o seu token dura um ano [...] essa pessoa vai ter um ano para usar esse token tranquilamente [...] pois a gente não pode revogá-lo, como a gente já viu, o JWT é stateless."

> "É mais seguro a gente pensar no access token como um certo tipo de crachá de visitante [...] do que de fato uma chave real de uma fechadura."

> "No caso do refresh token a gente realmente não precisa de acesso a ele. A gente só precisa que ele esteja lá e seja válido."

> "Ferramentas não substituem o critério técnico: dominar esses conceitos [...] é o que te dá o controle para usar a ferramenta do jeito certo."
