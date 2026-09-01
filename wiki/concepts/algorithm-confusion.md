---
type: concept
title: "Algorithm Confusion Attack"
aliases: ["algorithm confusion", "alg none attack", "confusão de algoritmo", "key confusion attack", "RS256 HS256 confusion"]
date_created: 2026-09-01
date_updated: 2026-09-01
source_count: 1
tags: [algorithm-confusion, jwt, jose, jwa, cipher-agility, seguranca, appsec, cwe-347]
skill: tech-mentor-security
status: draft
---

# Algorithm Confusion Attack

Classe de ataque contra tokens autocontidos (tipicamente [[wiki/concepts/jwt|JWT]]) que explora uma falha de implementação onde o verificador **confia cegamente no algoritmo declarado no header do próprio token**, em vez de impor uma whitelist fixa de algoritmos aceitos no servidor. É a consequência prática de expor [[wiki/concepts/cipher-agility]] sem restringi-la — o [[wiki/concepts/jwa|JWA]], catálogo de algoritmos do ecossistema [[wiki/concepts/jose|JOSE]], é a fonte estrutural dessa superfície de ataque.

## Por que o header é atacável

O header de um JWS/JWT é apenas base64 — não criptografado — e é o **cliente** quem o transporta de volta ao servidor a cada requisição. Nada impede um atacante de decodificar o header, alterá-lo, e reencodá-lo antes de enviar. Se o servidor não valida explicitamente o algoritmo esperado, o atacante decide o algoritmo, não o servidor.

## Variante 1 — `alg: none`

O padrão JWA reserva o valor `none` para cenários (originalmente pensados para redes internas já protegidas por outros meios) onde nenhuma assinatura é necessária. Um atacante pode:

1. Pegar um token legítimo e alterar o payload (ex.: elevar `role` de `user` para `admin`).
2. Trocar o `alg` do header para `none`.
3. Remover completamente a assinatura.

Se a biblioteca do servidor aceitar esse header sem rejeitar `none` explicitamente, ela lê "nenhum algoritmo necessário" e processa o payload adulterado como válido — sem jamais checar uma assinatura que não existe.

### O caso Tim McLean (2015)

Em 2015, o pesquisador Tim McLean revelou que bibliotecas JWT populares em Node.js, Python, Ruby e PHP aceitavam `alg: none` por padrão. Como essas bibliotecas formavam a base de autenticação/autorização de milhões de aplicações, sistemas inteiros ficaram expostos — qualquer atacante podia elevar privilégios em um token só editando o header. Casos de impacto documentados publicamente incluem empresas como [[wiki/entities/shopify]] e [[wiki/entities/microsoft]]. [external: atribuição e ano batem com registros públicos amplamente citados sobre a divulgação de Tim McLean; CVE específico e nomes exatos das bibliotecas não foram verificados nesta sessão.]

## Variante 2 — confusão RS256 ↔ HS256

Mais sofisticada: o servidor espera um token assinado com **RS256** (assimétrico — chave pública para verificar, privada para assinar) mas aceita, sem checagem estrita, que o header declare **HS256** (simétrico — mesma chave assina e verifica). Como a chave **pública** RS256 costuma estar disponível publicamente (via [[wiki/concepts/jwk|JWK]]/JWKS ou simplesmente porque é pública por design), um atacante pode usá-la como o **segredo HMAC** para forjar um token HS256 válido — o servidor, ao tentar verificar com HS256 usando essa mesma chave pública como segredo, valida a assinatura forjada. Mencionada na fonte original sem detalhamento completo do mecanismo — registrada aqui como ponto de aprofundamento futuro.

## Defesa

- **Whitelist explícita de algoritmos aceitos no servidor** — nunca aceitar o `alg` vindo do token sem checar contra uma lista fixa (ex.: `algorithms: ['RS256']`, nunca vazio, nunca incluindo `none`).
- **Nunca misturar simétrico e assimétrico no mesmo verificador** sem checagem de tipo de chave — a causa raiz da variante RS256→HS256.
- Bibliotecas JOSE modernas já implementam essa whitelist como comportamento padrão ou exigem declaração explícita — ver exemplo em [[wiki/concepts/jwt#JWT — JSON Web Token]] (`algorithms: ['HS256']` explícito na verificação).

## Relação com outros conceitos

- [[wiki/concepts/cipher-agility]] — a filosofia de design que cria a superfície explorada aqui
- [[wiki/concepts/jwa]] — catálogo de algoritmos, incluindo `none`, que o ataque abusa
- [[wiki/concepts/jws]] — mecanismo de assinatura cuja ausência (ou verificação incorreta) o ataque explora
- [[wiki/concepts/jwk]] — a chave pública exposta via JWKS é o vetor da variante RS256→HS256
- [[wiki/concepts/paseto]] — elimina essa classe de ataque por design (sem algoritmo negociável)
- [[wiki/concepts/jwt]] — alvo mais comum na prática desse ataque

## Key Sources

- [[wiki/sources/jose-jws-jwe-jwk-jwa-algorithm-confusion-paseto]]
