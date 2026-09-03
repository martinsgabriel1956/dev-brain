---
type: entity
title: "Bernardo Lobato"
aliases: ["Bernardo Lobato"]
date_created: 2026-06-05
date_updated: 2026-09-01
source_count: 14
tags: [arquitetura-software, segurança, criador-de-conteudo, youtube, backend]
skill: tech-mentor-security
status: stub
---

# Bernardo Lobato

Desenvolvedor e criador de conteúdo brasileiro. Publica vídeos toda sexta-feira sobre arquitetura de software, padrões de design e tópicos avançados de engenharia de software.

## Key Sources

- [[sources/padroes-arquiteturais-seguranca-gatekeeper-valet-key-token-relay]]
- [[wiki/sources/o-que-e-refatoracao-quando-usar]] — vídeo introdutório de uma série planejada sobre refatoração
- [[wiki/sources/api-gateway-padrao-essencial-arquiteturas-distribuidas]] — primeiro vídeo de uma série planejada sobre padrões de integração de aplicações
- [[wiki/sources/vale-a-pena-estudar-microsservicos-mesmo-sem-usar]] — vídeo de carreira/reflexão, fora da série técnica hands-on; defende estudar microsserviços como eixo de aprendizado de arquitetura, relato pessoal de retorno ao mercado
- [[wiki/sources/pkce-proof-key-code-exchange-spa-mobile]] — vídeo sobre PKCE como solução para autenticação em SPAs/mobile sem client secret estático, continuação de uma série sobre OAuth/OIDC; menciona vídeo futuro planejado sobre BFF stateless/stateful híbrido
- [[wiki/sources/openid-connect-oidc-autenticacao-alem-do-oauth]] — vídeo anterior da mesma série sobre OAuth/OIDC (referenciado dentro do próprio vídeo de PKCE como continuação): contexto histórico do OpenID original vs. OpenID Connect, comparação com SAML, e o antipadrão ROPC
- [[wiki/sources/tecnologias-hype-passado-soap-xml-esb-jquery-cobol]] — vídeo mais leve/reflexivo, fora da série técnica hands-on; argumenta que o ciclo de hype da comunidade não acompanha o ritmo real de obsolescência, usando SOAP, XML, ESB, jQuery e COBOL como exemplos de tecnologias fora do mainstream que ainda sustentam sistemas críticos
- [[wiki/sources/cache-vs-buffer-diferenca-conceitual]] — distinção conceitual entre cache (reutilização) e buffer (diferença de velocidade produtor/consumidor), percorrida do hardware (cache L1/L2/L3, buffer de I/O) à arquitetura distribuída (Redis, filas de mensagem, streaming)
- [[wiki/sources/refresh-token-pattern-access-token-de-curta-duracao]] — vídeo da série sobre OAuth/OIDC/JWT: padrão access+refresh token, rotation, fingerprinting e janela de exposição
- [[wiki/sources/historia-e-evolucao-das-apis-bernardo-lobato]] — primeira parte de uma nova série sobre APIs: percurso histórico década a década, de rotina local de sistema operacional (anos 60) a infraestrutura crítica (anos 2020)
- [[wiki/sources/autenticacao-federada-sso-saml-bernardo-lobato]] — continuação da série sobre OAuth/OIDC: LDAP como base de identidade corporativa, Kerberos (MIT, anos 80) como antecessor do modelo de terceiro confiável, e o protocolo SAML 2.0 em detalhe (fluxo IdP/SP, troca de metadados, ponte com OAuth)
- [[wiki/sources/microsservicos-historia-soa-esb-bernardo-lobato]] — vídeo dedicado a microsserviços: origem histórica (Peter Rogers 2005, SOA/ESB, "Microservices — Java, the Unix Way" 2012), três requisitos práticos (standalone, deploy independente, funcionalidade útil), exemplo de streaming (Netflix/YouTube-like), e capacitação de time como desafio central pouco discutido
- [[wiki/sources/historia-oauth2-antipadrao-senha-bernardo-lobato]] — vídeo da série sobre OAuth/OIDC/JWT dedicado à origem histórica do OAuth: antipadrão da senha nomeado, Blaine Cook (Twitter) e Larry Halff (Magnolia) como criadores, linha do tempo RFC 5849 (OAuth 1.0) → RFC 6749 (OAuth 2.0), quatro pilares, grant types e token opaco vs. autoassinado
- [[wiki/sources/jose-jws-jwe-jwk-jwa-algorithm-confusion-paseto]] — "Anatomia de um Token 2": ecossistema JOSE (JWS/JWE/JWK/JWA) por trás do JWT, o ataque de algorithm confusion (`alg: none`, caso Tim McLean 2015, variante RS256→HS256) e o PASETO como alternativa de cipher rigidity
