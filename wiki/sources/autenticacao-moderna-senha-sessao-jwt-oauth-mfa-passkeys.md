---
type: source
title: "Autenticação Moderna: Senhas, Sessões, JWT, OAuth, MFA e Passkeys"
aliases: ["200 milissegundos logou", "cada etapa da autenticação moderna", "autenticação moderna de ponta a ponta"]
date_created: 2026-08-03
date_updated: 2026-08-03
source_file: "raw/autenticacao-moderna-senha-sessao-jwt-oauth-mfa-passkeys.md"
source_url: ""
author: "não identificado (vídeo YouTube, português)"
date_published: ""
date_ingested: 2026-08-03
source_count: 0
tags: [autenticacao, autorizacao, password-hashing, sessao, jwt, oauth2, openid-connect, mfa, passkeys, webauthn, sql-injection, xss, csrf, cors, session-fixation, open-redirect, step-up-authentication]
skill: tech-mentor-security
status: stable
---

# Autenticação Moderna: Senhas, Sessões, JWT, OAuth, MFA e Passkeys

## TL;DR

Percurso de ponta a ponta pela autenticação moderna, do clique em "entrar" ao fluxo completo com MFA/passkey + JWT + OAuth. Abre com a distinção [[wiki/concepts/autenticacao-e-autorizacao|autenticação vs. autorização]] (metáfora da portaria: documento = autenticação, crachá de andar = autorização), cobre [[wiki/concepts/password-hashing|hashing de senha]] (bcrypt/Argon2 como *work factor* deliberadamente lento contra SHA-256 rápido demais) e [[wiki/concepts/salt|salt]] contra [[wiki/concepts/rainbow-table|rainbow tables]], erros de login (mensagens genéricas, [[wiki/concepts/rate-limiting|rate limiting]], [[wiki/concepts/sql-injection|SQL Injection]]), [[wiki/concepts/sessoes-http-cookies|sessões]] (flags de cookie, *session fixation*, invalidação ao trocar senha, Redis vs. memória vs. banco), [[wiki/concepts/jwt|JWT]] (HMAC vs. RSA/ECDSA, chave fraca, validação de issuer/audience, local storage vs. cookie httpOnly, rotação de refresh token), [[wiki/concepts/oauth2|OAuth]] (Authorization Code Flow, [[wiki/concepts/pkce|PKCE]], *open redirect*, parâmetro `state`), [[wiki/concepts/openid-connect|OpenID Connect]] (ID Token, `nonce` contra replay, escopos), [[wiki/concepts/mfa-multifator-autenticacao|MFA]] ([[wiki/concepts/otp-hotp-totp|TOTP]] vs. SMS vs. chave física, *step-up authentication*) e [[wiki/concepts/webauthn-fido2-u2f|passkeys]] (vínculo criptográfico ao domínio, sincronização via nuvem vs. hardware dedicado), fechando com [[wiki/concepts/xss]], CSRF, CORS mal configurado e tokens de reset de senha previsíveis. Funciona majoritariamente como **fonte de confirmação/consolidação**: quase todo conceito citado já tinha página própria na wiki (grande sobreposição com [[wiki/sources/historia-autenticacao-senha-mfa-oauth-jwt]] e [[wiki/sources/autenticacao-segura]]), mas introduz quatro mecanismos que ainda não tinham página dedicada — *session fixation*, *open redirect* no fluxo OAuth, *step-up authentication* e CORS mal configurado.

## Claims Principais

| Claim | Evidência | Confiança |
|---|---|---|
| Autenticação e autorização são etapas sequenciais e distintas — a metáfora da portaria (documento → autenticação; crachá de andar → autorização) | Explicação de abertura do vídeo | Alta — reforço direto de [[wiki/concepts/autenticacao-e-autorizacao]] |
| SHA-256 processa ~1 bilhão de hashes/segundo numa GPU moderna, tornando-o inadequado para senhas; bcrypt/Argon2 usam *work factor* para forçar centenas de milissegundos por hash, transformando um ataque de segundos em anos | Comparação numérica direta (bilhão de hashes/s vs. work factor) | Alta — consistente com [[wiki/concepts/password-hashing]], que já documenta CPU-hard/memory-hard mas sem essa métrica de velocidade bruta do SHA-256 |
| Mensagens de erro de login diferenciadas ("usuário não encontrado" vs. "senha incorreta") permitem enumeração de contas — a mensagem correta é sempre genérica | Explicação do vetor de ataque de enumeração | Alta — nuance específica não coberta antes em [[wiki/concepts/autenticacao-e-autorizacao]] nem em [[wiki/concepts/rate-limiting]] |
| *Session fixation*: o atacante planta um session ID conhecido no browser da vítima antes do login; se o ID não é regenerado após autenticar, o atacante herda a sessão autenticada | Explicação do ataque e da mitigação (regenerar session ID pós-login) | Alta — já citado en passant em [[wiki/concepts/sessoes-http-cookies]] ("Regenerar o ID após login"), mas sem explicar o mecanismo do ataque em si |
| Trocar a senha não revoga sessões antigas automaticamente — se o atacante já tinha uma sessão ativa, ela continua válida até ser invalidada explicitamente | Argumento de fechamento sobre gestão de sessão | Alta — ponto novo para [[wiki/concepts/sessoes-http-cookies]], que documentava as flags de cookie mas não o ciclo de vida pós-troca de senha |
| Sessões em memória são rápidas mas se perdem no restart; em banco têm persistência mas custam uma consulta extra por requisição; Redis é a solução padrão em produção por ser compartilhado entre múltiplos servidores atrás de um load balancer | Comparação das três opções de armazenamento de sessão | Alta — detalha o "porquê" do Redis já citado indiretamente via [[wiki/concepts/redis]] |
| JWT assinado com HMAC usa a mesma chave simétrica para assinar e verificar (adequado a servidor único); RSA/ECDSA usam par assimétrico, permitindo que microsserviços validem com a chave pública sem acesso à chave privada do emissor | Explicação dos dois algoritmos de assinatura JWT | Alta — [[wiki/concepts/jwt]] cita "HMAC ou par de chaves assimétrico" en passant; esta fonte detalha o motivo prático da escolha (servidor único vs. microsserviços) |
| Chave secreta HMAC fraca (dicionário) permite forjar qualquer token; a chave precisa de pelo menos 256 bits de entropia gerados aleatoriamente. Validar apenas a assinatura sem checar `issuer`/`audience` permite que um token emitido para o serviço A seja reutilizado no serviço B | Dois erros comuns de implementação de JWT | Alta — nuance de campo não detalhada antes em [[wiki/concepts/jwt]], que já mostra `issuer`/`audience` no exemplo de código mas sem explicar o ataque de reuso entre serviços |
| Refresh token com rotação: a cada uso, o token antigo é invalidado e um novo é emitido, de forma que um refresh token roubado e não usado pelo atacante perde validade assim que o dono legítimo o usa | Explicação da prática de rotação | Alta — mecanismo específico não detalhado antes em [[wiki/concepts/jwt]], que já cobre a dualidade access/refresh token mas não a rotação |
| Local storage é acessível por qualquer script (inclusive malicioso via XSS); cookie `httpOnly` é a opção recomendada para aplicações web porque JavaScript não consegue ler o valor | Comparação de onde armazenar o JWT no cliente | Alta — reforça [[wiki/concepts/xss]] e a lógica de `httpOnly` já documentada em [[wiki/concepts/sessoes-http-cookies]], agora aplicada especificamente ao token JWT |
| *Open redirect* no fluxo OAuth: se o Authorization Server não valida a `redirect_uri` caractere por caractere (permitindo wildcard/comparação parcial), o atacante troca o domínio de retorno e recebe o código de autorização em servidor próprio | Explicação do ataque e da mitigação (validação exata) | Alta — mecanismo novo para a wiki; nem [[wiki/concepts/oauth2]] nem [[wiki/concepts/pkce]] documentavam esse vetor específico |
| O parâmetro `state` no OAuth previne CSRF no fluxo de login social: sem ele, um atacante pode iniciar um fluxo com a própria conta e induzir a vítima a completar o callback, vinculando a conta do atacante ao perfil da vítima | Explicação do ataque de CSRF via OAuth | Alta — `state` já aparece citado como "anti-CSRF" no bloco de código de [[wiki/concepts/oauth2]], mas sem essa explicação do cenário de ataque completo |
| O campo `nonce` do OpenID Connect protege contra replay: um ID Token interceptado e reenviado é rejeitado porque o servidor reconhece que aquele nonce específico já foi consumido | Explicação do mecanismo de replay protection | Alta — mecanismo novo para [[wiki/concepts/openid-connect]], que já documentava `iss`/`sub`/`aud` mas não `nonce` |
| TOTP é vulnerável a phishing (o código pode ser digitado num site falso que o repassa em tempo real), enquanto chaves físicas como YubiKey não são, porque a prova é vinculada criptograficamente ao domínio | Comparação SMS (SIM swap) vs. TOTP (phishing) vs. chave física (phishing-resistant) | Alta — consistente com [[wiki/concepts/otp-hotp-totp]] e [[wiki/concepts/webauthn-fido2-u2f]], que já documentam os mecanismos separadamente; esta fonte é a primeira a nomear explicitamente a vulnerabilidade de phishing do TOTP como contraste direto com WebAuthn |
| *Step-up authentication*: MFA aplicado só no login não protege operações sensíveis pós-login (trocar e-mail, mudar senha, desativar MFA, transferir dinheiro) — essas ações devem re-solicitar o segundo fator | Argumento sobre limitação do MFA tradicional | Alta — mecanismo novo para a wiki, sem página própria antes desta ingestão |
| Passkeys eliminam phishing porque a chave é vinculada ao domínio do site (um domínio "Google" com caractere trocado não recebe assinatura válida) — nenhum outro método (senha, TOTP, SMS) tem essa proteção | Explicação do vínculo de domínio | Alta — consistente com [[wiki/concepts/webauthn-fido2-u2f]], que já documenta essa propriedade para U2F/WebAuthn de forma geral |
| CORS mal configurado — `Access-Control-Allow-Origin: *` combinado com `Allow-Credentials: true` — permite que qualquer site na internet faça requisições autenticadas contra a API | Explicação do erro de configuração | Alta — mecanismo novo para a wiki; nenhuma página de conceito cobria CORS antes desta ingestão |
| Token de reset de senha previsível (ex.: base64 do ID do usuário) permite a um atacante gerar tokens válidos para qualquer conta; o token precisa ser aleatório, expirar em minutos, ser de uso único, e o reset deve invalidar todas as sessões ativas | Explicação do vetor de ataque e da mitigação completa | Alta — combina três exigências (aleatoriedade, expiração curta, invalidação de sessão) que a wiki não tinha reunido em um único lugar antes |

## Conceitos Abordados

- [[wiki/concepts/autenticacao-e-autorizacao]]
- [[wiki/concepts/password-hashing]]
- [[wiki/concepts/salt]]
- [[wiki/concepts/rainbow-table]]
- [[wiki/concepts/rate-limiting]]
- [[wiki/concepts/sql-injection]]
- [[wiki/concepts/sessoes-http-cookies]]
- [[wiki/concepts/jwt]]
- [[wiki/concepts/oauth2]]
- [[wiki/concepts/pkce]]
- [[wiki/concepts/openid-connect]]
- [[wiki/concepts/mfa-multifator-autenticacao]]
- [[wiki/concepts/otp-hotp-totp]]
- [[wiki/concepts/webauthn-fido2-u2f]]
- [[wiki/concepts/xss]]
- [[wiki/concepts/session-fixation]] (página nova)
- [[wiki/concepts/open-redirect]] (página nova)
- [[wiki/concepts/step-up-authentication]] (página nova)
- [[wiki/concepts/cors-misconfiguration]] (página nova)

## Entidades Abordadas

Nenhuma — autor não identificado, sem menção a empresas/pessoas específicas além de exemplos genéricos (Google, iCloud).

## Observações / Contradições

Nenhuma contradição com o que já está registrado na wiki. Forte sobreposição temática com [[wiki/sources/historia-autenticacao-senha-mfa-oauth-jwt]] (percurso histórico) e [[wiki/sources/autenticacao-segura]] (checklist de segurança) — esta fonte não traz uma narrativa nova, mas funciona como consolidação prática com foco em "erros comuns que causam incidentes em produção", cobrindo o fluxo de ponta a ponta em uma única passada. O valor incremental real está nos quatro mecanismos sem página própria (*session fixation*, *open redirect*, *step-up authentication*, CORS mal configurado) e em detalhes pontuais já listados nas claims acima (rotação de refresh token, validação de issuer/audience, nonce do OIDC, token de reset previsível).

## Perguntas Abertas

- A fonte não cita o termo "credential stuffing" explicitamente, mas descreve exatamente esse ataque ("lista de e-mails e senhas vazadas de outro site") — vale considerar adicionar esse termo como alias em [[wiki/concepts/rate-limiting]] se ainda não estiver coberto por outra fonte.
- Não há atribuição de autoria nem link do vídeo original — mesma limitação já registrada em [[wiki/sources/historia-autenticacao-senha-mfa-oauth-jwt]] e [[wiki/sources/autenticacao-segura]]; possível que as três fontes sejam do mesmo canal/autor, mas isso não pôde ser confirmado a partir do texto bruto fornecido.
