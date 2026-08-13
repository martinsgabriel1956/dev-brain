---
type: concept
title: "ROPC — Resource Owner Password Credentials"
aliases: ["ROPC", "Resource Owner Password Credentials", "API como proxy de login"]
date_created: 2026-08-13
date_updated: 2026-08-13
source_count: 1
tags: [ropc, oauth2, oidc, antipadrao, autenticacao, seguranca]
skill: tech-mentor-security
status: stub
---

# ROPC — Resource Owner Password Credentials

Antipadrão de autenticação em que a própria API/aplicação (o client) recebe diretamente o login e a senha do usuário e os repassa, por baixo dos panos, ao provedor de identidade — em vez de deixar o usuário autenticar diretamente no provedor via navegador.

## Por que é um antipadrão

Tanto o [[wiki/concepts/openid-connect|OpenID Connect]] quanto o SAML (ver [[wiki/concepts/sso-single-sign-on]]) existem justamente para que a senha do usuário **nunca** passe pela aplicação cliente — só o Identity Provider deve ver essas credenciais. Uma API que atua como proxy de login funciona na prática, mas quebra essa garantia: passa a manipular a senha do usuário, assumindo um risco desnecessário de segurança e arquitetura. Uma implementação nesses moldes, mesmo se tecnicamente parecida, não é de fato OIDC nem SAML.

É por isso que botões de "Entrar com Google/Facebook/GitHub" sempre abrem uma instância do browser mostrando a URL do provedor de identidade — mesmo em single page applications ou apps mobile — em vez de um formulário de login dentro do próprio app.

## Status atual

Completamente desencorajado nas APIs modernas. A recomendação é delegar autenticação inteiramente para o provedor de identidade (via client/navegador) e manter a API focada em regras de negócio.

## Relação com outros conceitos

- [[wiki/concepts/openid-connect]] — exige autenticação via client exatamente para evitar esse antipadrão
- [[wiki/concepts/oauth2]] — o Authorization Code Flow, quando implementado corretamente, também impede esse vínculo entre API e senha do usuário
- [[wiki/concepts/pkce]] — resolve um problema adjacente (client público sem onde guardar segredo), mas pressupõe que a autenticação já acontece corretamente via client/navegador, não via ROPC

## Key Sources

- [[wiki/sources/openid-connect-oidc-autenticacao-alem-do-oauth]]
