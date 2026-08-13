---
type: source
title: "OpenID Connect (OIDC): Autenticação Além do OAuth"
aliases: ["openid connect", "oidc", "openid original", "id token"]
date_created: 2026-08-13
date_updated: 2026-08-13
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/openid-connect-oidc-autenticacao-alem-do-oauth.md
source_url: ""
author: "Bernardo Lobato (provável, não confirmado)"
date_published: ""
date_ingested: 2026-08-13
source_count: 0
tags: [openid-connect, oidc, openid, saml, oauth2, id-token, autenticacao, identidade-federada, ropc, seguranca]
skill: tech-mentor-security
status: stable
---

## TL;DR

Percurso histórico do OpenID original (2005, identidade via URL + descoberta HTML dinâmica, descontinuado em 2014) ao OpenID Connect (2014, camada de autenticação sobre o OAuth 2 via ID Token em JWT). Contrasta OpenID original com SAML (mesma época, mesmo objetivo, premissas de confiança opostas: descentralizada e sem governança vs. formal e corporativa) para explicar por que o SAML prosperou e o OpenID original não. Detalha o fluxo OIDC completo, insiste que autenticação deve sempre passar pelo client/navegador (nunca pela API como proxy — nomeia esse antipadrão como ROPC), e fecha explicando por que interceptação do `code` exige PKCE em SPA/mobile.

## Key Claims

**Claim:** O protocolo OpenID original (2005) usava uma URL como identidade do usuário, descoberta dinamicamente via tags `<link>` ocultas no HTML retornado por essa URL, num fluxo inteiramente por redirecionamento de navegador.
**Evidence:** Passo a passo descrito: usuário informa a URL no site de destino → site faz `GET` na URL → HTML de resposta contém `<link>` apontando para `openid.server` e `openid.delegate` → navegador é redirecionado ao provedor real → login acontece na tela do provedor → provedor redireciona de volta com mensagem assinada (XML) → site valida assinatura e cria sessão.
**Confidence:** média — mecanismo tecnicamente coerente e consistente com a arquitetura documentada do OpenID 1.0/2.0 original, mas esta fonte é a única na wiki a descrever o fluxo em detalhe; sem fonte primária (spec) cruzada nesta ingestão.

**Claim:** OpenID original e SAML surgiram quase na mesma época com objetivos parecidos, mas partiram de premissas de confiança opostas — e isso explica por que o SAML sobreviveu e o OpenID original foi descontinuado (~2014).
**Evidence:** SAML pressupunha acordos formais entre empresas conhecidas, implementado por times internos de organizações que já confiavam umas nas outras — encaixava no modelo de federação corporativa. OpenID original apostava em qualquer site aceitando qualquer provedor de identidade sem governança nem confiança pré-estabelecida — risco prático para quem aceitava o login.
**Confidence:** média-alta — explicação causal plausível e consistente com [[wiki/concepts/sso-single-sign-on]] (que já registra SAML como "historicamente anterior" ao OIDC), mas é uma leitura/opinião do autor sobre adoção de mercado, não um fato verificável por spec.

**Claim:** OpenID Connect (OIDC, 2014) é uma camada de identidade construída sobre o OAuth 2, usando um ID Token em formato JWT para carregar claims do usuário (nome, e-mail, foto).
**Evidence:** Reforça o que já está registrado em [[wiki/concepts/openid-connect]] — ID Token distinto do access token do OAuth: o access token é para a API, o ID Token é para a aplicação cliente.
**Confidence:** alta — consistente com múltiplas fontes já presentes na wiki (`references/appsec-authn-authz.md` do skill tech-mentor-security confirma a definição).

**Claim:** No fluxo OIDC, a autenticação deve sempre acontecer via client/navegador diretamente no provedor de identidade — nunca com a API atuando como proxy que recebe login/senha do usuário e repassa ao provedor.
**Evidence:** Esse é o único jeito de garantir que login, senha e MFA não sejam interceptados pela API. Se a API pede a senha do usuário para repassar ao provedor, não se está de fato usando SAML nem OIDC — está se usando o antipadrão **ROPC (Resource Owner Password Credentials)**, hoje desencorajado nas APIs atuais.
**Confidence:** alta — alinhado com o skill tech-mentor-security e com o motivo de existir do PKCE já documentado em [[wiki/concepts/pkce]] e [[wiki/sources/pkce-proof-key-code-exchange-spa-mobile]] (prova de posse, não confiar em segredo estático do client).

**Claim:** SAML trafega XML pesado tanto no request quanto no response, aumentando a complexidade de implementação especialmente em SPA/mobile; OIDC trafega apenas JSON, mais leve e compatível com o mercado atual.
**Evidence:** Comparação direta feita no vídeo como um dos motivos de o OIDC ter suplantado o SAML fora do mundo corporativo legado.
**Confidence:** alta — consistente com a tabela comparativa já presente em `references/appsec-authn-authz.md` (skill tech-mentor-security) e com [[wiki/concepts/sso-single-sign-on]].

**Claim:** Interceptar o `authorization_code` gerado pelo provedor de identidade permite a um atacante se passar pelo usuário legítimo junto à API e obter os tokens — problema agravado em SPA/mobile, onde não há como embutir um `client_secret` estático de forma segura.
**Evidence:** Todo código de uma SPA roda exposto no browser; qualquer segredo embutido no bundle é visível via DevTools ou engenharia reversa. O vídeo aponta o PKCE como a solução, mas deixa o mecanismo detalhado para um vídeo dedicado.
**Confidence:** alta — mecanismo e solução já documentados em detalhe em [[wiki/concepts/pkce]] via [[wiki/sources/pkce-proof-key-code-exchange-spa-mobile]]; esta fonte apenas motiva o problema sem repetir o mecanismo do PKCE.

## Entities & Concepts Touched

- [[wiki/concepts/openid-connect]]
- [[wiki/concepts/openid-legado]]
- [[wiki/concepts/oauth2]]
- [[wiki/concepts/sso-single-sign-on]]
- [[wiki/concepts/pkce]]
- [[wiki/concepts/jwt]]
- [[wiki/concepts/ropc-resource-owner-password-credentials]]
- [[wiki/entities/bernardo-lobato]]
- [[wiki/entities/google]]
- [[wiki/entities/microsoft]]

## Open Questions

- Autoria não confirmada nominalmente na transcrição — atribuição a [[wiki/entities/bernardo-lobato]] por convergência de sinais (numeração de série "nossa jornada no mundo das APIs, autenticação e autorização", menção direta ao vídeo já ingerido sobre PKCE como continuação, estilo de fala). Mesmo padrão de inferência já usado em [[wiki/sources/pkce-proof-key-code-exchange-spa-mobile]].
- O vídeo não cita nenhuma fonte primária (RFC, spec do OpenID 1.0/2.0, documento da OpenID Foundation) para os detalhes do fluxo original — tratado como relato histórico, não verificado contra a especificação original nesta ingestão.
- Não ficou claro se a "mensagem assinada baseada em XML" do fluxo OpenID original tem relação formal de reaproveitamento de formato com o SAML da mesma época, ou se é apenas coincidência de ambos usarem XML — não explorado no vídeo.
