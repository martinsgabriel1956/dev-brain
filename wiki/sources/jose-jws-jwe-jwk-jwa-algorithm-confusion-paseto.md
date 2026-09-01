---
type: source
title: "JOSE, JWS, JWE, JWK, JWA: Algorithm Confusion e a Alternativa PASETO"
aliases: ["Anatomia de um Token 2", "ecossistema JOSE", "algorithm confusion", "alg none", "PASETO"]
date_created: 2026-09-01
date_updated: 2026-09-01
source_count: 0
tags: [jwt, jose, jws, jwe, jwk, jwa, algorithm-confusion, paseto, cipher-agility, seguranca, criptografia]
skill: tech-mentor-security
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/jose-jws-jwe-jwk-jwa-algorithm-confusion-paseto.md
source_url:
author: Bernardo Lobato
date_published:
date_ingested: 2026-09-01
---

# JOSE, JWS, JWE, JWK, JWA: Algorithm Confusion e a Alternativa PASETO

## TL;DR

Vídeo de [[wiki/entities/bernardo-lobato]], continuação direta de "Anatomia de um Token 1" (já coberto em [[wiki/concepts/jwt]]). Aprofunda o **ecossistema JOSE** (JSON Object Signing and Encryption) que sustenta o JWT: **JWS** (assinatura — integridade/autenticidade, RFC 7515 implícita), **JWE** (criptografia — confidencialidade, RFC 7516), **JWK** (representação JSON de chaves criptográficas, RFC 7517) e **JWA** (catálogo de algoritmos permitidos, RFC 7518). O núcleo do vídeo é mostrar que o JWA é a fonte de uma filosofia de design chamada **cipher agility** — suportar múltiplos algoritmos e trocar entre eles via o próprio header do token — e que essa flexibilidade é a causa raiz do ataque **algorithm confusion** (incluindo a variante `alg: none`), que expôs bibliotecas populares (Node.js, Python, Ruby, PHP) segundo pesquisa de **Tim McLean em 2015**. Fecha apresentando o **PASETO** (Platform Agnostic Security Token) como alternativa de "cipher rigidity" — versões fixas (V1–V4), algoritmos únicos e modernos (Ed25519, AES-256-GCM), sem espaço para o cliente escolher o algoritmo — e conclui que o JWT continua valendo a pena desde que a validação seja rígida (whitelist de algoritmos no servidor, nunca aceitar o algoritmo vindo do cliente).

## Key Claims

1. **JOSE é o conjunto de especificações; JWT é uma instância/formato dentro dele.** JWT não define por si só como assinar ou criptografar — quem define isso são os quatro pilares do JOSE (JWS, JWE, JWK, JWA). Confidence: alta — consistente com a organização real das RFCs (7515–7518) sob o guarda-chuva JOSE do IETF.
2. **JWS garante integridade/autenticidade, não confidencialidade** — o payload permanece legível em base64; o que impede alteração é a assinatura (simétrica via HMAC, ou assimétrica via par de chaves, onde a privada assina e a pública valida). Já documentado em [[wiki/concepts/jwt]]; esta fonte formaliza o nome da especificação (JWS) por trás desse comportamento. Confidence: alta.
3. **JWE (RFC 7516) é a especificação para confidencialidade**, com estrutura de **cinco partes** (header, chave de criptografia cifrada, IV, cipher text, authentication tag) — usa uma Content Encryption Key (CEK) simétrica aleatória, cifra o payload com ela (ex.: AES-GCM) e cifra a própria CEK com a chave pública do destinatário. Necessário quando o payload carrega dado sensível que não pode ficar exposto em base64 (diferente do JWS puro). Confidence: alta — fluxo consistente com a RFC 7516, embora simplificado (a fonte não detalha todos os `alg`/`enc` possíveis do JWA para JWE).
4. **JWK (RFC 7517) padroniza chaves em JSON e viabiliza rotação de chave via endpoint `/.well-known/jwks.json` + campo `kid`** — elimina chave hardcoded em variável de ambiente/código e permite que múltiplos algoritmos coexistam. Confidence: alta.
5. **JWA (RFC 7518) é a "fonte da cipher agility"**: por listar múltiplos algoritmos válidos — alguns hoje fracos/obsoletos — delega ao desenvolvedor a responsabilidade de escolher o que é seguro, abrindo a superfície do ataque de **algorithm confusion**. Confidence: alta — é a leitura correta e amplamente aceita da causa raiz desse tipo de vulnerabilidade (CWE-347).
6. **Ataque `alg: none`**: o header do token é controlado pelo cliente; se o back end confia cegamente nele, um atacante pode remover a assinatura, setar `alg: none` e ter o payload alterado (ex.: role elevado a admin) aceito sem verificação. Confidence: alta — comportamento real documentado em CVEs de bibliotecas JWT (2015).
7. **Tim McLean revelou em 2015 que bibliotecas JWT populares em Node.js, Python, Ruby e PHP aceitavam `alg: none` por padrão**, expondo sistemas que dependiam delas para autenticação/autorização; casos documentados de impacto incluem Shopify e Microsoft. Confidence: média-alta — o pesquisador e o ano batem com a divulgação amplamente citada (Auth0/blog post de Tim McLean, 2015), mas a fonte não cita CVE específico nem nomeia as bibliotecas exatas (ex.: `pyjwt`, `node-jsonwebtoken` antes de correções, `php-jwt`) — vale checagem externa se precisão de CVE for necessária. [external: a atribuição do achado a Tim McLean e o ano 2015 batem com registros públicos conhecidos, mas não foi verificado contra a fonte primária nesta sessão.]
8. **A defesa correta é whitelist de algoritmos no servidor + nunca aceitar `alg` vindo do cliente** — já era a recomendação registrada em [[wiki/concepts/jwt]] (`algorithms: ['HS256']` explícito na verificação), mas esta fonte nomeia o mecanismo de ataque que essa defesa previne. Confidence: alta.
9. **Existe uma variante mais sofisticada de algorithm confusion**: trocar de um algoritmo assimétrico (RS256) para simétrico (HS256), usando a chave pública RS256 (frequentemente exposta) como chave secreta HMAC — não apenas remover o algoritmo. A fonte menciona essa variante mas não detalha o mecanismo, dizendo que "não cabe nesse vídeo". Confidence: alta que a variante existe e é real (é o ataque RS256→HS256 classicamente documentado), porém a fonte trata superficialmente — mecanismo completo não coberto aqui. [external: o mecanismo do ataque RS256→HS256 é conhecimento de segurança amplamente documentado, não detalhado pela fonte.]
10. **PASETO adota "cipher rigidity"**: versões fixas e imutáveis (V1–V4), cada uma com um conjunto único e não-negociável de algoritmos modernos (Ed25519 para assinatura, AES-256-GCM para criptografia) — o cliente não escolhe algoritmo, eliminando a classe inteira de ataque de algorithm confusion por design. Estrutura de três partes: versão, `purpose` (`local` = criptografado, `public` = assinado) e payload. Confidence: alta — consistente com a especificação pública do PASETO (paseto.io).
11. **Conclusão do autor: JWT continua valendo a pena** para a maioria dos casos, pois é padrão de indústria (RFC) e o problema não é a ferramenta, mas a liberdade excessiva do JOSE combinada com desenvolvedores não versados em segurança usando configuração default. PASETO é recomendado especificamente para quem "quer dormir tranquilo" e está começando um projeto novo. Confidence: média-alta — é uma recomendação de julgamento de autor, coerente com a análise técnica anterior, mas é opinião/trade-off, não fato verificável.

## Entidades Mencionadas

- [[wiki/entities/bernardo-lobato]] — autor
- [[wiki/entities/microsoft]] — citada como exemplo de empresa grande afetada por vulnerabilidade de algorithm confusion documentada publicamente
- [[wiki/entities/shopify]] — idem

## Conceitos Tocados

- [[wiki/concepts/jose]] (novo) — ecossistema de especificações que sustenta o JWT
- [[wiki/concepts/jws]] (novo) — assinatura (integridade/autenticidade)
- [[wiki/concepts/jwe]] (novo) — criptografia (confidencialidade)
- [[wiki/concepts/jwk]] (novo) — representação JSON de chaves e rotação via `kid`/JWKS endpoint
- [[wiki/concepts/jwa]] (novo) — catálogo de algoritmos, fonte da cipher agility
- [[wiki/concepts/cipher-agility]] (novo) — filosofia de design (flexibilidade de algoritmo) e seu custo de segurança
- [[wiki/concepts/algorithm-confusion]] (novo) — ataque central do vídeo (`alg: none` e RS256→HS256)
- [[wiki/concepts/paseto]] (novo) — alternativa de cipher rigidity
- [[wiki/concepts/jwt]] — conceito pai, já cobria HMAC vs. RSA/ECDSA e a recomendação de whitelist de algoritmos; esta fonte nomeia formalmente o ataque que essa recomendação previne
- [[wiki/concepts/criptografia]] — base de assinatura simétrica/assimétrica reaplicada aqui em JWS/JWE
- [[wiki/concepts/rfc-request-for-comments]] — homônimo IETF: RFC 7515–7518 como especificações normativas do JOSE

## Open Questions

- A fonte não cita o CVE específico nem nomeia as bibliotecas exatamente afetadas pela pesquisa de Tim McLean (2015) — fica como lacuna para verificação externa se precisão de CVE for necessária algum dia.
- O mecanismo completo do ataque RS256→HS256 (usar a chave pública RS256 como segredo HMAC) é mencionado mas não explicado — a fonte diz explicitamente que "não cabe nesse vídeo". Vale registrar como pergunta em aberto para uma fonte futura mais profunda sobre esse ataque específico.
- A fonte não detalha os algoritmos `enc` (ex.: A256GCM) vs. `alg` (ex.: RSA-OAEP) do JWA no contexto específico do JWE — trata de forma simplificada ("um algoritmo de criptografia autenticada como o AES-GCM").
- Não há comparação de adoção real de PASETO no mercado (a fonte não cita nenhuma empresa ou framework popular usando PASETO em produção) — fica em aberto se PASETO é recomendação teórica ou tem tração real fora de nichos.

## Raw Quotes

> "JWT é o formato do token, enquanto JOSE é o conjunto das especificações que define como esse token vai ser assinado e criptografado. O JWT pode ser entendido, a grosso modo, como uma instância de um token do JOSE."

> "O ponto crítico é que o JWA é a fonte da cipher agility — ao oferecer tantas opções, algumas hoje consideradas fracas ou obsoletas, ela acaba delegando ao desenvolvedor a responsabilidade de escolher o que é seguro, o que abre margem para vulnerabilidade."

> "Um atacante pode pegar um token legítimo, alterar seu conteúdo [...] modificar o header para excluir o algoritmo atual, e remover completamente a assinatura final. [...] Ele lerá o header, verá que nenhum algoritmo é necessário, e processará o payload alterado como se fosse válido [...]. É a versão digital do 'É verdade, esse bilhete.'"

> "O ponto central: o header do token pode ser controlado pelo cliente — logo, o back end não pode confiar nele para escolher o algoritmo. Isso é um erro de design. A regra é: jamais aceitar o algoritmo que vem do cliente, e manter no servidor uma whitelist com os algoritmos permitidos."

> "Diferente do JWT, onde o cliente pode escolher o algoritmo no header, o PASETO utiliza versões fixas e imutáveis [...] impedindo completamente ataques de algorithm confusion ou a falta de algoritmo no header."

> "O problema não é a ferramenta, é a liberdade excessiva que o ecossistema JOSE dá, e quando o desenvolvedor não é tão ligado nessas questões de segurança, pode dar problema."
