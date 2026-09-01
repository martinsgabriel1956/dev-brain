---
type: concept
title: "JWS — JSON Web Signature"
aliases: ["JWS", "JSON Web Signature"]
date_created: 2026-09-01
date_updated: 2026-09-01
source_count: 1
tags: [jws, jose, jwt, assinatura-digital, seguranca, criptografia]
skill: tech-mentor-security
status: draft
---

# JWS — JSON Web Signature

Especificação dentro do ecossistema [[wiki/concepts/jose]] responsável por **integridade e autenticidade**: garante que um dado não foi alterado desde que foi criado pelo emissor, e que o emissor é quem diz ser. Não garante confidencialidade — para isso existe o [[wiki/concepts/jwe]].

Funciona vinculando um **header** (algoritmo utilizado) e um **payload** através de uma **assinatura digital**, gerada com uma chave secreta simétrica ou um par de chaves assimétrico. O resultado é a estrutura de três partes separadas por ponto, codificadas em base64, que forma o [[wiki/concepts/jwt|JWT]] tradicional. O payload continua **legível** por qualquer um que decodifique o base64 — a assinatura só impede alteração silenciosa, não leitura.

## Chave simétrica vs. assimétrica

- **Simétrica (HMAC/HS256)**: emissor e receptor compartilham a mesma chave secreta. O emissor gera um hash da assinatura; o receptor recalcula e compara. Quem consegue verificar também consegue forjar — por isso o cliente nunca deve ter essa chave.
- **Assimétrica (RSA/ECDSA — RS256/ES256)**: a chave **privada** assina (só o emissor tem acesso); a chave **pública** verifica (pode ser distribuída livremente, inclusive via [[wiki/concepts/jwk]]).

Já detalhado com exemplo de código em [[wiki/concepts/jwt#HMAC vs. RSA/ECDSA: Qual Algoritmo de Assinatura Usar]].

## O header é a superfície de ataque

O header instrui o verificador sobre qual algoritmo e qual chave usar — mas o header é escrito pelo **emissor original** e transportado pelo **cliente**, que pode alterá-lo. Um verificador que confia cegamente no `alg` declarado no header, sem impor uma whitelist própria, fica exposto ao ataque de [[wiki/concepts/algorithm-confusion]].

## Relação com outros conceitos

- [[wiki/concepts/jose]] — conceito pai
- [[wiki/concepts/jwt]] — formato de token mais comum instanciando JWS
- [[wiki/concepts/jwe]] — contraparte de confidencialidade (criptografa em vez de só assinar)
- [[wiki/concepts/algorithm-confusion]] — ataque que explora a confiança cega no header do JWS

## Key Sources

- [[wiki/sources/jose-jws-jwe-jwk-jwa-algorithm-confusion-paseto]]
