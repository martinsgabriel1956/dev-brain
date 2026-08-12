---
type: concept
title: "HTTP vs HTTPS"
aliases: ["HTTP", "HTTPS", "http vs https", "hypertext transfer protocol secure"]
date_created: 2026-08-12
date_updated: 2026-08-12
source_count: 1
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

## Key sources
- [[wiki/sources/enderecos-ip-dns-dominios-https-aws-fernanda-kipper]] — HTTP sem criptografia vs HTTPS seguro; Man-in-the-Middle; o que o SSL garante (e o que não garante)
