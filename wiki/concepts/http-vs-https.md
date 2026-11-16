---
type: concept
title: "HTTP vs HTTPS"
aliases: ["HTTP", "HTTPS", "http vs https", "hypertext transfer protocol secure"]
date_created: 2026-08-12
date_updated: 2026-11-16
source_count: 7
tags: [rede, http, https, ssl, tls, seguranca, man-in-the-middle]
skill: tech-mentor-networking
status: stub
---

# HTTP vs HTTPS

Ambos são **HyperText Transfer Protocol** — o protocolo de transferência de hipertexto da web. A diferença é a camada de segurança:

| | HTTP | HTTPS |
|---|---|---|
| Nome | HyperText Transfer Protocol | HyperText Transfer Protocol **Secure** |
| Criptografia | Nenhuma (dados em texto claro) | Sim — troca de chaves entre navegador e servidor via [[wiki/concepts/certificado-ssl-acm|SSL/TLS]] |
| Man-in-the-Middle | Vulnerável | Risco muito reduzido |
| Navegador | Marca "not secure" | Cadeado / conexão segura |

**Man-in-the-Middle:** sem criptografia, alguém no meio do caminho pode alterar a requisição/resposta ou se passar pelo servidor. O HTTPS fecha essa brecha criptografando o tráfego entre as pontas (o [[wiki/concepts/tls-handshake|TLS handshake]] negocia as chaves antes do primeiro request).

**O que o certificado SSL realmente prova:** que quem responde é o **dono daquele domínio** — *não* que o dono é a marca que você imagina. Um golpe com domínio parecido (`aidas` no lugar de `adidas`) pode ter HTTPS válido: a conexão é "segura", mas o domínio é outro. Acessar `adidas.com.br` via HTTPS garante que quem responde é o dono de `adidas.com.br`, e a atenção ao domínio digitado continua sendo responsabilidade do usuário.

> A fonte chama HTTPS de "criptografia de ponta a ponta". Rigorosamente, TLS é criptografia **em trânsito** (cliente↔servidor; o servidor descriptografa) — não end-to-end no sentido estrito. `[skill: tech-mentor-networking — references/protocols-transport.md]`

## Navegar sem HTTP entre cliente e proxy

[[wiki/sources/icmp-browser-navegar-na-internet-via-ping-go-michel-leonardo]]: o [[wiki/entities/icmp-browser]] troca o HTTP por [[wiki/concepts/icmp]] no trecho cliente↔proxy (sem TLS); o proxy ainda usa HTTP(S) para buscar o site.

## Na NLW #1 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-1-programacao-web-html-css-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]]: HTTP é o "protocolo de transferência de hipertextos", protocolo é "conjunto de regras", e o S "significa que é seguro". `[external]` É HTTP sobre TLS: cifra o tráfego e autentica o servidor, sem atestar o conteúdo do site (https://developer.mozilla.org/en-US/docs/Glossary/HTTPS).

## Na NLW #2, dia 1 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-1-programacao-web-html-css-proffy]]: HTTP é "um conjunto de regras para transferência de hipertexto" e o S "é secure".

## Na NLW #2, dia 4 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-4-back-end-node-express-nunjucks-proffy]], a promessa de que o POST vai "esconder os dados" do cadastro repete o mal-entendido da NLW #1: quem protege o conteúdo em trânsito é o HTTPS.

## Key sources
- [[wiki/sources/enderecos-ip-dns-dominios-https-aws-fernanda-kipper]] — HTTP sem criptografia vs HTTPS seguro; Man-in-the-Middle; o que o SSL garante (e o que não garante)
- [[wiki/sources/icmp-browser-navegar-na-internet-via-ping-go-michel-leonardo]] — trecho sem HTTP/TLS
- [[wiki/sources/requisicao-http-anatomia-metodos-headers-body-status-code-middleware]] — HTTPS como camada criptografada negociada antes da requisição; cadeado do navegador
- [[wiki/sources/nlw-1-dia-1-programacao-web-html-css-ecoleta]]: protocolo como regras; S de seguro
- [[wiki/sources/nlw-2-dia-1-programacao-web-html-css-proffy]]: NLW #2, dia 1: protocolo como conjunto de regras
- [[wiki/sources/nlw-2-dia-4-back-end-node-express-nunjucks-proffy]]: NLW #2, dia 4: POST não esconde, HTTPS protege

## Key sources (adição 2026-10-09)
- [[wiki/sources/url-vs-uri-diferenca-urn-identificacao-localizacao]] — protocolo (`http`/`https`) como a parte da URL que diz como acessar
