---
type: source
title: "HMAC: Integridade de Mensagem em Local-First (Entrevista de System Design)"
aliases: ["hmac local-first", "carrinho local-first hmac", "integridade sem storage"]
date_created: 2026-07-10
date_updated: 2026-07-10
source_count: 0
tags: [hmac, criptografia, local-first, system-design, entrevista, appsec, rfc-2104]
skill: tech-mentor-security
status: draft
source_file: raw/hmac-integridade-mensagem-local-first-entrevista.md
source_url:
author:
date_published:
date_ingested: 2026-07-10
---

# HMAC: Integridade de Mensagem em Local-First (Entrevista de System Design)

## TL;DR

Pergunta de entrevista de system design (nível médio/avançado, segurança): um `cart service` computa o carrinho (payload com produto, quantidade, preço unitário e total) e manda para o cliente sem querer persistir esse carrinho no servidor (padrão **local-first** — o dado local é tratado como fidedigno). Como garantir que o payload devolvido pelo cliente no fechamento é exatamente o que o servidor gerou, sem pagar custo de storage/lookup? Criptografar o payload inteiro quebra a exibição ao usuário; chave assimétrica (RSA) resolve mas é cara demais em alto volume; concatenar `secret + mensagem` e fazer hash simples (MD5/SHA1) é vulnerável a ataque de extensão de mensagem. A resposta correta é **HMAC**: deriva uma chave interna e uma externa a partir do mesmo segredo via XOR com os bytes de padding `0x36` (ipad) e `0x5C` (opad, escolhidos por serem os mais distantes entre si), faz hash em duas etapas (`Hash(chave_interna || msg)`, depois `Hash(chave_externa || hash_1)`), e envia o resultado como header junto do payload em claro no body. O servidor recalcula o HMAC ao receber de volta e compara — sem nunca ter armazenado o carrinho.

## Key Claims

| Claim | Evidência |
|---|---|
| Criptografar o payload garante consistência mas quebra a exibição ao usuário | Se o body está cifrado, o cliente não tem a chave para decifrar e mostrar o preço |
| Chave assimétrica (RSA) resolve o problema de integridade mas é cara demais em alto volume | Custo computacional de operações assimétricas é ordens de magnitude maior que hashing/HMAC |
| `Hash(secret + mensagem)` simples (ex. MD5) é vulnerável a ataque de extensão de mensagem | O segredo fica no início da concatenação; algoritmos de hash processam por blocos, expondo padrão explorável para anexar dados à mensagem original preservando o hash |
| HMAC deriva duas chaves (interna e externa) do mesmo segredo via XOR com padding, em vez de concatenar a chave direto com a mensagem | RFC do HMAC (RFC 2104) — bytes `0x36` (ipad) e `0x5C` (opad) escolhidos por maximizar distância/entropia entre as duas chaves derivadas |
| A chave precisa ser normalizada para o tamanho de bloco do algoritmo de hash (64 bytes para MD5/SHA-1) antes do XOR | Chave menor recebe padding de zeros; chave maior é reduzida aplicando hash sobre si mesma |
| O segundo hash (com a chave externa) usa como entrada o *hash* da primeira etapa, não a mensagem original | Isso é o que dificulta a extensão de mensagem — o atacante não manipula mais a mensagem em claro, mas um digest intermediário protegido por chave derivada |
| Local-first com HMAC elimina custo de storage/lookup de carrinhos em alto volume | Índice em memória sobre milhões de registros (relacional) ou custo de leitura/escrita por lookup (NoSQL) some quando o estado vive só no cliente |

## Conceitos

- [[wiki/concepts/hmac]] — novo conceito criado a partir desta fonte; mecânica interna (ipad/opad, duas etapas de hash)
- [[wiki/concepts/local-first]] — novo conceito criado a partir desta fonte; padrão de tratar dado do cliente como fidedigno para evitar storage
- [[wiki/concepts/criptografia]] — atualizado com seção sobre HMAC como terceira alternativa entre simétrica/assimétrica
- [[wiki/concepts/encryption]] — atualizado, link para HMAC como mecanismo de integridade separado de confidencialidade
- [[wiki/concepts/webhook-signature-validation]] — já documentava uso de HMAC para webhooks, sem detalhar a construção interna (ipad/opad); atualizado com backlink para o novo conceito

## Entidades Mencionadas

Nenhuma entidade nomeada (autor/canal não se identifica na transcrição bruta).

## Open Questions

- A fonte não detalha como o servidor deveria lidar com **expiração/replay** do HMAC — se o mesmo payload+header for reenviado dias depois com preços já desatualizados (ex.: produto teve o preço alterado), o HMAC ainda validaria como íntegro. Não há timestamp ou nonce no esquema descrito, ao contrário do padrão de webhook em [[wiki/concepts/webhook-signature-validation]], que inclui `x-timestamp` e checagem de idade da requisição.
- Não fica claro qual algoritmo de hash de bloco de 64 bytes é usado na prática (o autor cita MD5 e SHA-1 apenas como exemplo do tamanho de bloco) — SHA-256 também usa bloco de 64 bytes, mas SHA-512 usa 128 bytes; a escolha do algoritmo de hash subjacente ao HMAC não é fechada na fonte.
- A fonte não menciona a necessidade de comparação em tempo constante (`timingSafeEqual`) ao validar o HMAC recebido — gap já coberto em [[wiki/concepts/timing-attack]] e na implementação de referência de [[wiki/concepts/webhook-signature-validation]].

## Raw Quotes

> "A criptografia ela é muito interessante quando você quer garantir consistência, só que por outro lado se você quer exibir aquele dado descriptografado numa das pontas, você perde essa possibilidade."

> "Se você tem tempo e computação suficiente, só concatenando um segredo na frente de uma mensagem não gera entropia suficiente para você conseguir ter uma mensagem segura."

> "A grande vantagem [de validar um payload que o próprio servidor gerou] é: no modelo local-first, eu não preciso armazenar — se eu não preciso armazenar, não me custa armazenamento."

## Key Sources

_Este é o documento primário._
