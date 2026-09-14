---
type: concept
title: "CWT — CBOR Web Token"
aliases: ["CWT", "CBOR Web Token", "COSE"]
date_created: 2026-09-14
date_updated: 2026-09-14
source_count: 1
tags: [cwt, cbor, cose, jwt, iot, token]
skill: tech-mentor-security
status: stub
---

# CWT — CBOR Web Token

Versão **binária** do [[wiki/concepts/jwt|JWT]], baseada no padrão **COSE** (CBOR Object Signing and Encryption) — o equivalente ao [[wiki/concepts/jose|JOSE]] do mundo JSON, mas para o formato binário CBOR em vez de JSON textual.

Por ser binário em vez de texto (Base64), é significativamente mais leve em bytes trafegados. Tem RFC própria e é usado sobretudo em **dispositivos IoT** ou sistemas onde cada byte transmitido tem custo relevante — sensores, comunicação via satélite, equipamentos com restrição de banda.

## Status desta página

Stub — a fonte que introduziu este conceito na wiki (vídeo em português) o trata de forma breve, sem exemplo de payload nem comparação real de tamanho de bytes contra um JWT equivalente. Números de RFC (CWT: RFC 8392; COSE: RFC 8152/9052) não foram citados pela fonte primária — adicionados aqui como referência de navegação, não verificados contra a especificação original nesta sessão. [external]

## Relação com outros conceitos

- [[wiki/concepts/jwt]] — equivalente textual/JSON do qual o CWT é a variante binária
- [[wiki/concepts/jose]] — equivalente ao COSE no mundo JSON

## Key Sources

- [[wiki/sources/anatomia-de-um-token-1-opaco-vs-autocontido-bernardo-lobato]] — introdução breve ao CWT como alternativa binária ao JWT para IoT
