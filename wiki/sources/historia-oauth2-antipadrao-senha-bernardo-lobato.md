---
type: source
title: "A História do OAuth: Do Antipadrão da Senha ao Protocolo de Autorização"
aliases: ["história do OAuth", "origem do OAuth", "antipadrão da senha (vídeo)"]
date_created: 2026-08-24
date_updated: 2026-08-24
source_count: 0
tags: [oauth2, autorizacao, historia, antipadrao-da-senha, grant-types, twitter, magnolia, rfc-5849, rfc-6749, seguranca]
skill: tech-mentor-security
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/historia-oauth2-antipadrao-senha-bernardo-lobato.md
source_url:
author: Bernardo Lobato
date_published:
date_ingested: 2026-08-24
---

# A História do OAuth: Do Antipadrão da Senha ao Protocolo de Autorização

## TL;DR

Vídeo de [[wiki/entities/bernardo-lobato]], continuação da série sobre OAuth/OIDC/JWT já bem coberta na wiki ([[wiki/concepts/pkce]], [[wiki/concepts/openid-connect]], [[wiki/concepts/saml]]) — mas cobre um ângulo que a wiki só tinha em forma de citação solta em [[wiki/concepts/oauth2]]: a origem histórica exata do protocolo. Nomeia pela primeira vez na wiki o **antipadrão da senha** (password antipattern), a dupla que criou o OAuth (Blaine Cook, do Twitter; Larry Halff, do Magnolia), a linha do tempo formal (grupo de discussão em abril/2007 → RFC 5849/OAuth 1.0 em abril/2010 → RFC 6749/OAuth 2.0 em 2012), os quatro pilares nomeados (Resource Owner, Client, Authorization Server, Resource Server), e detalha os três grant types centrais e a distinção token opaco/introspecção vs. token autoassinado/validação local — nenhum desses termos estava nomeado explicitamente em [[wiki/concepts/oauth2]] antes desta fonte.

## Key Claims

**Claim:** O antipadrão da senha (password antipattern) é o nome técnico para sistemas/usuários se autenticarem entre si trocando usuário e senha — mecanismo pensado para pessoas, não para credenciamento de serviço a serviço — o que impede identificação real do serviço, dificulta auditoria e inviabiliza rotação de credenciais.
**Evidence:** Definição dada no vídeo como contexto direto do problema que motivou a criação do OAuth em 2006-2007: antes do protocolo, dar acesso a um serviço terceiro (ex.: Flickr) exigia entregar a própria senha, e o único jeito de revogar acesso era trocar a senha — quebrando o acesso de todos os outros serviços conectados.
**Confidence:** alta — termo e definição vêm diretamente da fala do autor; a wiki não tinha esse antipadrão nomeado antes (só o [[wiki/concepts/ropc-resource-owner-password-credentials|ROPC]], que é um antipadrão adjacente mas distinto — ROPC é a API atuando como proxy de login, não o compartilhamento direto de senha com terceiros).

**Claim:** O OAuth nasceu do encontro entre Blaine Cook (Twitter), que trabalhava numa implementação de OpenID para o Twitter, e Larry Halff (Magnolia, serviço de favoritos), que buscava um protocolo de delegação de acesso para conectar widgets de macOS à API do Magnolia — o grupo de discussão OAuth começou em abril de 2007.
**Evidence:** Vídeo narra o encontro dos dois como origem direta do grupo de trabalho, formado após perceberem que não existia nenhum padrão aberto de delegação de acesso em APIs; Google se junta pouco depois às discussões.
**Confidence:** alta para a narrativa geral (consistente com o histórico público do OAuth); a wiki não tinha essa origem registrada antes — [[wiki/concepts/oauth2]] só dizia "criado em 2006 por um grupo de empresas da web (incluindo o Twitter)", sem nomear os dois criadores nem o Magnolia.

**Claim:** OAuth 1.0 (RFC 5849, abril de 2010) exigia assinaturas criptográficas em cada requisição e canonicalização de parâmetros — complexo demais de implementar e manter interoperável — e por isso caiu em desuso; OAuth 2.0 (RFC 6749, 2012) trocou essa complexidade por HTTPS como base de segurança, token Bearer e fluxos mais simples, viabilizando adoção em SPAs e mobile.
**Confidence:** alta — fato histórico bem documentado; primeira vez que a wiki registra a comparação direta 1.0 vs. 2.0 com as datas e números de RFC exatos.

**Claim:** O framework OAuth se apoia em quatro pilares nomeados: Resource Owner (usuário dono do dado), Client (aplicação que quer o dado), Authorization Server (emite/valida tokens) e Resource Server (API que guarda o recurso protegido).
**Evidence:** Enumeração explícita no vídeo, aplicada depois ao exemplo passo a passo do login com Google (contatos).
**Confidence:** alta — terminologia padrão da RFC 6749, mas a wiki não tinha essa nomenclatura de "quatro pilares" registrada explicitamente antes; [[wiki/concepts/oauth2]] já descrevia o fluxo mas sem nomear os papéis dessa forma.

**Claim:** O access token OAuth 2 é opaco por especificação — o padrão não obriga formato — mas na prática muitos provedores usam JWT/JOSE; a validação do token pelo resource server acontece por introspecção (stateful, consulta o Authorization Server a cada requisição) ou validação local (token autoassinado, validação embutida sem round-trip).
**Confidence:** alta — distinção técnica relevante ausente de [[wiki/concepts/oauth2]] e de [[wiki/concepts/jwt]] antes desta fonte.

**Claim:** Três grant types centrais definem como a aplicação obtém o token: Authorization Code (login humano via redirecionamento no browser, hoje exige PKCE), Client Credentials (sistema-a-sistema, sem usuário humano, autenticação via client id/secret) e Refresh Token (renovação de access token expirado).
**Evidence:** Vídeo detalha os três, contrastando explicitamente Authorization Code (requer redirecionamento e consentimento humano) com Client Credentials (integrações back-end/jobs agendados).
**Confidence:** alta — [[wiki/concepts/refresh-token-pattern-access-token-de-curta-duracao|refresh token]] e [[wiki/concepts/pkce|PKCE/Authorization Code]] já estavam documentados na wiki em fontes separadas; esta é a primeira fonte a nomear "Client Credentials" como grant type e a organizar os três lado a lado como taxonomia única.

**Claim:** Em arquiteturas de microsserviços internas (sem provedor terceiro como Google/GitHub), o OAuth resolve o problema de cada API de negócio precisar validar senha ou consultar banco de usuários — centralizando identidade num Authorization Server interno (ex.: Keycloak, Spring Authorization Server) e deixando as APIs de negócio "burras" quanto à identidade, validando só se o token é válido e tem o escopo certo.
**Confidence:** alta — reforça e detalha o que [[wiki/concepts/token-relay-pattern]] já cobria sobre repasse de token entre serviços internos, com o ângulo adicional de "por que centralizar identidade" que não estava explícito antes.

## Entities & Concepts Touched

- [[wiki/concepts/oauth2]]
- [[wiki/concepts/api-economy]]
- [[wiki/concepts/pkce]]
- [[wiki/concepts/ropc-resource-owner-password-credentials]]
- [[wiki/concepts/token-relay-pattern]]
- [[wiki/concepts/jwt]]
- [[wiki/entities/bernardo-lobato]]
- [[wiki/entities/flickr]]
- [[wiki/entities/google]]
- [[wiki/entities/ietf]]

## Open Questions

- O vídeo cita o grupo de discussão OAuth formado em abril de 2007 sem mencionar a fundação da OpenID Foundation, ocorrida no mesmo ano (2007, já registrada em [[wiki/entities/google]] via [[wiki/sources/openid-connect-oidc-autenticacao-alem-do-oauth]]) — são iniciativas paralelas e distintas (delegação de acesso vs. padronização de identidade), mas a wiki ainda não tem uma fonte que explique se/como as duas comunidades se cruzaram naquele momento.
- A fonte não detalha por que exatamente o OAuth 1.0 exigia assinatura criptográfica por requisição (qual ataque isso mitigava) — só afirma que era complexo. Ponto em aberto para uma eventual leitura direta da RFC 5849, análoga ao que [[wiki/sources/rfc-7636-pkce-oauth-public-clients]] fez para o PKCE.
