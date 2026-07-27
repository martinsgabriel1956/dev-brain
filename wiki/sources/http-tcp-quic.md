---
type: source
title: "TCP/IP, HTTP/1.1, HTTP/2, HTTP/3 e QUIC"
aliases: ["http3", "quic", "tcp", "http2", "multiplexing", "head of line blocking", "tls handshake"]
date_created: 2026-04-23
date_updated: 2026-07-27
source_file: /home/nemomartins/Documentos/new/dev-study/raw/http-tcp-quic.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 1
tags: [tcp, http, http2, http3, quic, tls, head-of-line-blocking, multiplexing, 0rtt, networking]
skill: tech-mentor-backend
status: stable
---

## TL;DR

Evolução HTTP: HTTP/1.1 (keep-alive, HoL blocking por conexão) → HTTP/2 (multiplexing em uma conexão TCP, HPACK header compression, HoL blocking no nível TCP) → HTTP/3/QUIC (UDP-based, HoL blocking eliminado, 0-RTT reconnect). TLS 1.3 reduz handshake para 1 RTT. 0-RTT com PSK é replay-able — não usar para operações não-idempotentes.

## Key Claims

**Claim:** HTTP/2 resolve HoL blocking por conexão mas não no nível TCP — HTTP/3/QUIC resolve ambos.
**Evidence:** HTTP/1.1: 1 request por conexão (sem pipelining prático). HTTP/2: múltiplos streams em 1 conexão TCP — mas perda de pacote TCP bloqueia TODOS os streams (HoL no TCP). HTTP/3: UDP + QUIC — cada stream é independente, perda de pacote afeta apenas aquele stream. Em redes com perda >1% de pacotes, HTTP/3 supera HTTP/2 significativamente.
**Confidence:** alta

**Claim:** QUIC implementa TLS 1.3 integrado — reduz handshake inicial para 1 RTT (0-RTT para reconexões).
**Evidence:** TCP + TLS: 3-way handshake (1 RTT TCP) + TLS handshake (1 RTT TLS 1.3) = 2 RTT antes do primeiro byte de dados. QUIC: TCP handshake e TLS handshake são combinados = 1 RTT total. 0-RTT: cliente reconectando com PSK envia dados no primeiro pacote. Crítico para mobile com redes instáveis.
**Confidence:** alta

**Claim:** 0-RTT no TLS 1.3/QUIC é replay-able — seguro apenas para operações idempotentes (GET).
**Evidence:** 0-RTT data é enviada antes de estabelecer anti-replay protection. Atacante com acesso a 0-RTT data pode retransmitir a mesma request. Safe para: GET (idempotente). Inseguro para: POST, PUT, DELETE, transações financeiras. Servidores devem verificar se a request 0-RTT é idempotente antes de processar.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/tcp]]
- [[concepts/quic]]
- [[concepts/http2]]
- [[concepts/http3]]
- [[concepts/tls]]
- [[concepts/head-of-line-blocking]]
- [[concepts/multiplexing]]

## Open Questions

- HTTP/3 em load balancers internos — quando vale o overhead de QUIC para tráfego intra-DC já confiável?
- HPACK vs QPACK header compression — quais são as diferenças práticas em performance? Parcialmente conectado por [[wiki/sources/por-que-letras-minusculas-economizam-dados]]: HPACK usa uma tabela de Huffman estática (baseada em frequências típicas de headers HTTP), o mesmo princípio de "caracteres mais frequentes, código mais curto" documentado em [[wiki/concepts/compactacao-de-texto]] — ainda falta uma fonte dedicada a QPACK para comparar diretamente.
