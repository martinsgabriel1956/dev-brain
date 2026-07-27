---
type: source
title: "História da Autenticação: de Senha a Tokens, Criptografia Assimétrica e Identidade Federada"
aliases: ["quem é você segurança do clube", "história da autenticação", "senha para OAuth JWT"]
date_created: 2026-07-27
date_updated: 2026-07-27
source_file: "raw/historia-autenticacao-senha-mfa-oauth-jwt.md"
source_url: ""
author: "não identificado (vídeo YouTube, português)"
date_published: ""
date_ingested: 2026-07-27
source_count: 0
tags: [autenticacao, mfa, oauth, openid-connect, jwt, webauthn, biometria, criptografia-assimetrica, seguranca, identidade-federada]
skill: tech-mentor-security
status: stable
---

## TL;DR

Percurso histórico de 70 anos da autenticação de usuários, usando a metáfora do segurança de um clube perguntando "quem é você?": do identificador de usuário sem senha do *time-sharing* dos anos 60, à senha com hash+salt do Unix (1976), às perguntas de segurança, aos três fatores de [[wiki/concepts/mfa-multifator-autenticacao|MFA]] (sei/tenho/sou), passando pela evolução do segundo fator ([[wiki/entities/rsa-security|RSA SecurID]] → [[wiki/concepts/otp-hotp-totp|HOTP/TOTP]] → [[wiki/concepts/webauthn-fido2-u2f|U2F/WebAuthn]]), pelas três gerações de biometria (minúcias → vetor único → isolamento de hardware), até a identidade federada moderna ([[wiki/concepts/sso-single-sign-on|SSO]] → [[wiki/concepts/oauth2|OAuth 2.0]] → [[wiki/concepts/openid-connect|OpenID Connect]]) e o par [[wiki/concepts/jwt|Access Token/Refresh Token]] que resolve o dilema entre [[wiki/concepts/sessoes-http-cookies|sessões stateful]] escaláveis e tokens stateless revogáveis.

## Key Claims

**Claim:** A necessidade de identificar usuários surgiu com o *time-sharing* nos anos 60 (múltiplos usuários no mesmo computador), não desde o início da computação nos anos 40, quando máquinas eram dedicadas a uma única tarefa por vez.
**Evidence:** Ambiente de confiança absoluta em sistemas fechados de universidades/laboratórios inicialmente exigia só um identificador digitado, sem senha — a senha surgiu depois, à medida que mais pessoas ganharam acesso e a confiança absoluta deixou de ser sustentável.
**Confidence:** média-alta — narrativa histórica coerente e amplamente replicada em fontes de história da computação, mas não verificada contra fonte primária nesta ingestão.

**Claim:** O Unix, por volta de 1976, foi um dos primeiros sistemas a substituir senha em texto puro por hash + salt no arquivo de senhas, resolvendo o problema de a função de hash ser determinística.
**Evidence:** Salt não precisa ser secreto, só único por usuário — o que invalida ataques de rainbow table pré-computados.
**Confidence:** alta — consistente com o já registrado em [[wiki/concepts/password-hashing]] e [[wiki/concepts/hashing]], reforça a linha do tempo sem contradizer.

**Claim:** MFA robusto exige fatores de **categorias diferentes** (algo que você sabe / tem / é) — dois fatores da mesma categoria não aumentam a segurança da mesma forma, porque um único vetor de ataque pode comprometer ambos.
**Evidence:** Perguntas de segurança são citadas como exemplo de "MFA falso": tecnicamente uma segunda verificação, mas da mesma categoria (algo que você sabe), portanto uma senha mais fraca, não um segundo fator de verdade.
**Confidence:** alta — princípio de segurança amplamente aceito, também presente em `references/appsec-authn-authz.md` da skill tech-mentor-security.

**Claim:** A evolução do segundo fator de hardware seguiu uma linha específica: RSA SecurID (anos 90, seed+relógio proprietário) → HOTP (IETF RFC 4226, 2005, contador em vez de relógio) → TOTP (IETF RFC 6238, relógio novamente, mas padronizado) → U2F (2014, criptografia assimétrica).
**Evidence:** Cada geração resolveu uma fragilidade da anterior: HOTP eliminou dependência de relógio sincronizado do SecurID; U2F eliminou o segredo compartilhado (seed) que, se vazado do servidor, permitia gerar códigos válidos.
**Confidence:** média-alta — datas e RFCs citados são verificáveis externamente (RFC 4226/6238 são de fato IETF), mas a atribuição de "primeira aparição comercial em grande escala" ao SecurID especificamente não foi checada contra fonte primária nesta ingestão.

**Claim:** Biometria de impressão digital passou por três gerações arquiteturais: (1) minúcias com alinhamento e contagem de coincidências, (2) vetor numérico único combinando minúcias + direção/densidade/textura, (3) isolamento em processador dedicado (Secure Enclave/TEE) para que nem o sistema operacional comprometido consiga interceptar o template.
**Evidence:** A motivação da terceira geração é explicitamente arquitetural, não algorítmica — resposta ao fato de que biometria vazada não pode ser trocada como senha, então a defesa se torna "nunca deixar vazar" em vez de "dificultar reverter".
**Confidence:** média — plausível e coerente com o padrão Secure Enclave (Apple) e TEE (Android) já documentado em `references/mobile-security.md` da skill, mas as "três gerações" como framework specific não foram cross-checadas contra literatura acadêmica de biometria.

**Claim:** OAuth 2.0 (2006, atribuído a um grupo de empresas web incluindo o Twitter) resolve delegação de acesso com escopo limitado, mas foi desenhado para **autorização**, não autenticação — essa lacuna motivou o OpenID Connect (2014), construído sobre o OAuth, que acrescenta um ID Token (JWT com claims `issuer`/`subject`/`audience`) verificável via JWKS.
**Evidence:** Distinção central: Access Token do OAuth prova "o que o app pode fazer"; ID Token do OIDC prova "quem é o usuário". Verificação do ID Token não exige confiar no emissor: o relying party busca a chave pública no JWKS e verifica a assinatura criptograficamente.
**Confidence:** alta — distinção OAuth (autorização) vs. OIDC (autenticação) é consenso estabelecido na indústria, e corroborada por `references/appsec-authn-authz.md` da skill tech-mentor-security.

**Claim:** O par Access Token (curta duração, stateless) + Refresh Token (longa duração, armazenado e revogável no servidor) é a solução padrão para o problema de revogação de JWT, equilibrando escalabilidade stateless com controle de revogação centralizado.
**Evidence:** Se o JWT sozinho fosse de longa duração, não haveria como revogá-lo antes de expirar sem reintroduzir estado (denylist). Refresh Token revogado força reautenticação completa na próxima tentativa de renovação.
**Confidence:** alta — padrão amplamente documentado e já presente em `references/appsec-authn-authz.md` (seção JWT) da skill de segurança, sem contradição com o restante da wiki.

## Linha do Tempo Consolidada

```
anos 40   → computador de sala única, sem múltiplos usuários, sem autenticação
anos 60   → time-sharing → identificador de usuário (sem senha)
(sem data)→ senha em texto puro (problema: vazamento total se o arquivo vazar)
1976      → Unix: hash + salt (Unix crypt)
(sem data)→ perguntas de segurança (2ª camada fraca, mesma categoria "sabe")
anos 90   → RSA SecurID (token de hardware, seed + relógio proprietário)
2005      → HOTP (IETF RFC 4226) — contador em vez de relógio
(depois)  → TOTP (IETF RFC 6238) — relógio, mas padronizado e público
2014      → U2F — criptografia assimétrica, challenge-response
(atual)   → WebAuthn/FIDO2/Passkeys — U2F generalizado para o browser
2006      → OAuth (Twitter + outras empresas web) — delegação de acesso
2014      → OpenID Connect — camada de autenticação sobre OAuth
(atual)   → JWT + Access/Refresh Token — autenticação stateless com revogação controlada
```

## Entities & Concepts Touched

- [[wiki/concepts/mfa-multifator-autenticacao]] (novo)
- [[wiki/concepts/otp-hotp-totp]] (novo)
- [[wiki/concepts/webauthn-fido2-u2f]] (novo)
- [[wiki/concepts/jwt]] (novo)
- [[wiki/concepts/oauth2]] (novo)
- [[wiki/concepts/openid-connect]] (novo)
- [[wiki/concepts/sso-single-sign-on]] (novo)
- [[wiki/concepts/sessoes-http-cookies]] (novo)
- [[wiki/concepts/password-hashing]]
- [[wiki/concepts/mobile-biometria]]
- [[wiki/concepts/token-relay-pattern]]
- [[wiki/concepts/criptografia]]
- [[wiki/concepts/ssh]]
- [[wiki/entities/rsa-security]] (novo)
- [[wiki/entities/ietf]] (novo)

## Open Questions

- A atribuição de "criação do OAuth" ao Twitter especificamente é uma simplificação do vídeo — o padrão foi de fato desenvolvido por um grupo de empresas web (incluindo Twitter, Google, entre outras) coordenado dentro de um processo aberto que depois virou IETF RFC 6749. Vale precisão numa ingestão futura de fonte primária (spec ou história oficial do OAuth).
- Não foi possível confirmar nesta ingestão se "RSA SecurID" foi de fato a *primeira* aparição comercial em grande escala do segundo fator, ou apenas a mais conhecida — afirmação aceita como plausível, mas não verificada contra fonte primária.
- O vídeo não detalha se a "terceira geração" de biometria (isolamento de hardware) é uma classificação de mercado estabelecida ou uma simplificação didática do autor — vale checar contra `references/mobile-security.md` da skill tech-mentor-security ou literatura de biometria em uma ingestão futura.
- Nenhuma fonte primária (RFC, documentação oficial do OAuth/OIDC, artigo acadêmico de biometria) foi lida diretamente nesta ingestão — todas as claims vêm de uma transcrição de vídeo em português sem citação de fontes.
