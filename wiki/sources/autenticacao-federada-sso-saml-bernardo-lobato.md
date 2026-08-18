---
type: source
title: "Autenticação Federada e SSO: de LDAP e Kerberos ao SAML"
aliases: ["autenticação federada", "SAML", "Kerberos", "LDAP", "SSO corporativo"]
date_created: 2026-08-18
date_updated: 2026-08-18
source_count: 0
tags: [tech-mentor-security, saml, sso, kerberos, ldap, federated-identity, oauth2, identity-provider]
skill: tech-mentor-security
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/autenticacao-federada-sso-saml-bernardo-lobato.md
source_url:
author: Bernardo Lobato
date_published:
date_ingested: 2026-08-18
---

# Autenticação Federada e SSO: de LDAP e Kerberos ao SAML

## TL;DR

Vídeo de [[wiki/entities/bernardo-lobato]], parte da série sobre autenticação/OAuth/OIDC. Percorre a linha do tempo do problema de "autenticar em múltiplos sistemas": LDAP como base de identidade corporativa (chmod corporativo), Kerberos (MIT, anos 80) como primeira solução de "provar quem você é uma vez e receber um ticket aceito por outros servidores", e a transição para o SSO moderno baseado em tokens/claims quando a autenticação precisou sair da intranet e atravessar a internet. O núcleo técnico do vídeo é o protocolo **SAML 2.0**: fluxo completo IdP/SP com troca de metadados via certificado X.509, `SAMLRequest`/`SAMLResponse`, assinatura digital, e por que SAML (XML, dependente de browser/redirects) cede espaço a OIDC em SPAs/mobile mas continua dominante em SSO corporativo legado. Fecha mostrando a ponte SAML→OAuth (assertion SAML validada por um Authorization Server que emite um access token/JWT).

## Key Claims

1. **LDAP é "chmod corporativo"** — base única de usuários que vira provedor de autenticação; resolve a fragmentação de bases de usuário mas não resolve múltiplas autenticações (login único, mas ainda era preciso autenticar em cada sistema separadamente). Confidence: alta (fato de arquitetura amplamente documentado, embora a fonte não cite RFCs específicas do LDAPv3).
2. **Kerberos (MIT, anos 80) introduziu o modelo de "provar identidade uma vez para um terceiro confiável e receber um ticket aceito por outros servidores"**, sem nunca expor a senha na rede — o antecessor conceitual direto do modelo de Identity Provider usado hoje. Adotado pela Microsoft como protocolo padrão do Windows 2000/Active Directory (Kerberos V5, RFC 4120). Confidence: alta — consistente com [[wiki/concepts/kerberos]] e documentação histórica amplamente conhecida.
3. **A transição do Kerberos para o SSO moderno foi motivada pela saída da intranet para a internet** — tickets/sessões persistentes de rede local não funcionam bem quando não há conexão direta com o servidor da empresa; a solução foi mover para tokens e claims verificáveis via assinatura digital, mantendo o princípio central (confiar em um terceiro — o Identity Provider). Confidence: média-alta — é uma leitura de linhagem histórica plausível e coerente com a existência independente do SAML, mas não é uma sucessão técnica direta e documentada (SAML não "evoluiu do" Kerberos tecnicamente, ambos resolvem o mesmo problema de formas diferentes).
4. **SAML 2.0 (2005) opera com três partes — IdP, SP, browser do usuário — e depende de troca de metadados prévia** (certificado X.509 com a chave pública do IdP) para que o SP confie no IdP; a chave privada nunca sai do IdP. Confidence: alta — consistente com `references/appsec-authn-authz.md` do skill (fluxo SP-initiated SSO).
5. **Fluxo SAML: SP gera `SAMLRequest` e redireciona ao IdP → usuário autentica no IdP (SP nunca vê a senha) → IdP gera `SAMLResponse` (assertion XML assinada) → SP valida a assinatura com a chave pública e concede acesso.** Todo o transporte acontece via redirecionamentos no navegador — não há chamada servidor-a-servidor direta entre IdP e SP nesse fluxo. Confidence: alta.
6. **SAML é XML, verboso, e mal adequado a APIs/SPAs** justamente por depender do browser para os redirecionamentos — nesses casos a fonte recomenda OpenID Connect. Confidence: alta — mesma conclusão já registrada em [[wiki/sources/openid-connect-oidc-autenticacao-alem-do-oauth]] e em [[wiki/concepts/sso-single-sign-on]].
7. **SAML ainda domina SSO corporativo legado** (Salesforce, sistemas integrados a Active Directory) por oferecer controle de segurança centralizado rígido já integrado a essas tecnologias. Confidence: alta.
8. **SAML e OAuth são interoperáveis**: uma assertion SAML pode ser apresentada a um Authorization Server OAuth como credencial, que valida a assinatura XML e emite um access token (potencialmente um JWT) — ponte que permite APIs REST modernas consumirem identidades de diretórios legados. Confidence: média — mecanismo real (SAML Bearer Assertion Grant, RFC 7522), mas a fonte não nomeia o RFC nem o grant type especificamente, tratando de forma conceitual/simplificada.

## Entidades Mencionadas

- [[wiki/entities/bernardo-lobato]] — autor
- [[wiki/entities/microsoft]] — adotou Kerberos V5 como padrão do Windows 2000/Active Directory; citada também como provedora de identidade moderna (Microsoft Entra ID)
- [[wiki/entities/google]] — citada como IdP (Google Workspace) e exemplo de login social (Google)

## Conceitos Tocados

- [[wiki/concepts/saml]] (novo) — núcleo técnico do vídeo
- [[wiki/concepts/kerberos]] (novo)
- [[wiki/concepts/ldap]] (novo)
- [[wiki/concepts/federated-identity]] (novo — conceito já tinha uma página de source com o mesmo nome, mas nenhuma página de conceito)
- [[wiki/concepts/sso-single-sign-on]] — já cobria SAML em nível de hook; este vídeo aprofunda o protocolo em si
- [[wiki/concepts/oauth2]] — ponte SAML→OAuth (assertion como credencial trocada por access token)
- [[wiki/concepts/openid-connect]] — citado como sucessor recomendado do SAML para SPA/mobile/API

## Open Questions

- A fonte não cita RFCs específicos do LDAPv3 (menciona "um conjunto de RFCs" sem nomeá-los — RFC 4510 é a referência atual consolidada).
- A leitura de que o SSO moderno "evoluiu" diretamente do Kerberos é uma linhagem conceitual do autor, não uma sucessão técnica documentada — SAML e Kerberos são protocolos independentes que resolvem o mesmo problema (autenticação federada) em contextos diferentes (rede local vs. web). Mesmo padrão de simplificação de linhagem histórica já observado em [[wiki/sources/historia-e-evolucao-das-apis-bernardo-lobato]] (ligação Unix→REST tratada como fato, não como interpretação).
- A ponte SAML→OAuth é descrita de forma genérica ("a assertion é apresentada... como uma credencial") sem nomear o mecanismo formal (SAML 2.0 Bearer Assertion Profile, RFC 7522) nem o grant type OAuth correspondente — fica como lacuna técnica para uma fonte futura mais aprofundada.
- Não há menção a SCIM (provisionamento/desprovisionamento automatizado) mesmo ao discutir o problema de revogação de acesso no desligamento de funcionários — [[wiki/sources/federated-identity]] já cobre esse ponto especificamente e resolve a lacuna que este vídeo deixa em aberto.

## Raw Quotes

> "Pense no LDAP como se fosse uma espécie de chmod corporativo — da mesma maneira que o chmod dá permissões em diretórios dentro da sua máquina Linux, o LDAP serve para dar permissões dentro de diretórios corporativos."

> "Em vez de você provar quem é para cada servidor que acabaria exigindo múltiplas senhas, você prova quem é para uma espécie de cão de guarda e recebe um ticket — que é algo como um token — e o apresenta aos outros servidores. Esses outros servidores confiam nesse cão de guarda e deixam você passar sem precisar autenticar novamente."

> "Tecnicamente o sistema não autentica o ser humano, mas sim suas credenciais — se eu sei sua senha e eu tenho seu celular para receber o OTP, pro sistema eu sou você."

> "A aplicação original, o service provider, nunca tem acesso nem visualiza a senha digitada, pois isso acontece inteiramente na tela do provedor de identidade."

> "A grande sacada da engenharia moderna não foi descartar o protocolo, mas sim criar essas pontes — transformando essas assertions pesadas em XML em tokens JWT leves que nossas APIs conseguem consumir com uma performance considerável."
