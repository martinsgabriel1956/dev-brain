---
date: 2026-04-17
tags: [tech-mentor, networking, http, tcp, quic, tls, protocolos]
skill: tech-mentor-networking/references/protocols
level: intermediário
---

# TCP/IP, HTTP/1.1, HTTP/2, HTTP/3 e QUIC

## TCP — Three-Way Handshake e Controle de Fluxo

```
Client          Server
  │── SYN ────────►│
  │◄─── SYN-ACK ───│
  │── ACK ────────►│   ← conexão estabelecida (1.5 RTT)
  │                │
  │── dados ──────►│
```

**Flow Control:** receptor anuncia um `window size` — quantos bytes pode receber sem ACK. Emissor não pode enviar mais que o window.

**Congestion Control:** TCP detecta congestionamento via perda de pacotes e reduz a taxa. BBR (Bottleneck Bandwidth and RTT) — algoritmo moderno do Google — estima bandwidth real sem depender de perda de pacote, resultando em throughput 30-40% maior em redes com perda.

**Tuning de kernel para alta performance:**
```bash
# /etc/sysctl.conf
net.core.somaxconn = 65535           # tamanho da fila de accept()
net.ipv4.tcp_max_syn_backlog = 65535
net.core.rmem_max = 16777216         # buffer de recepção máximo
net.core.wmem_max = 16777216
net.ipv4.tcp_congestion_control = bbr
net.core.default_qdisc = fq          # necessário para BBR
```

---

## HTTP/1.1 — Keep-Alive e Head-of-Line Blocking

```
HTTP/1.0: nova conexão TCP por request
HTTP/1.1: keep-alive — reutiliza a conexão (padrão)
          pipelining — envia múltiplos requests sem esperar resposta

Problema do pipelining: Head-of-Line Blocking
Request 1 (lento) bloqueia Request 2 e 3
→ browsers abrem 6 conexões paralelas por domínio como workaround
```

---

## HTTP/2 — Multiplexing e Header Compression

```
HTTP/1.1: Uma requisição por vez por conexão
HTTP/2:   Múltiplos streams na mesma conexão TCP

Stream 1: GET /api/users     ──────────────────────────►
Stream 3: GET /api/orders    ──────────────────────────►
Stream 5: POST /api/events   ──────────────────────────►
                                        ◄─── responses interleaved
```

**HPACK:** comprime headers HTTP — evita enviar `User-Agent`, `Accept`, `Cookie` completos em cada request. Economia de 30-80% no tamanho dos headers em sequências de requests.

**Server Push:** servidor pode enviar recursos antes que o cliente peça — praticamente não usado na prática (HTTP/103 Early Hints é a alternativa moderna).

**ALPN:** negocia protocolo durante o TLS handshake — cliente e servidor concordam em usar HTTP/2 sem round-trip extra.

**Problema:** HTTP/2 ainda usa TCP. Um pacote perdido bloqueia todos os streams (TCP-level HoL blocking).

---

## HTTP/3 e QUIC — UDP-based, Zero HoL Blocking

QUIC resolve o TCP HoL blocking substituindo TCP por UDP com controle de fluxo implementado no user space.

```
HTTP/2 sobre TCP:
Stream 1 ──────────────────────────────────────────────►
Stream 2 ──── [LOSS] ◄──WAIT──────────────────────────►  ← HoL block
Stream 3 ──── BLOCKED BY STREAM 2 ─────────────────────►

HTTP/3 sobre QUIC:
Stream 1 ──────────────────────────────────────────────►
Stream 2 ──── [LOSS] ◄──RETRANSMIT────────────────────►  ← só stream 2 para
Stream 3 ──────────────────────────────────────────────►  ← outros continuam
```

**0-RTT Connection Resumption:** em conexões retomadas com o mesmo servidor, QUIC envia dados na primeira mensagem — eliminando o handshake inicial.

```
Conexão nova:
  → QUIC handshake (1-RTT) → dados
  Total: 1 RTT antes de dados

Conexão retomada (0-RTT):
  → dados imediatamente (com session ticket)
  Total: 0 RTT antes de dados
```

**Connection Migration:** QUIC identifica conexões por Connection ID (não por IP:port). Se o cliente muda de WiFi para 4G (muda o IP), a conexão continua — zero reconexão, zero interrupção de streaming.

---

## Comparativo

| Aspecto | HTTP/1.1 | HTTP/2 | HTTP/3 |
|---|---|---|---|
| Multiplexing | Não | Sim (sobre TCP) | Sim (sobre QUIC) |
| HoL Blocking | Por request e TCP | TCP nível | Não |
| Compressão headers | Não | HPACK | QPACK |
| Handshake | TCP + TLS (2-3 RTT) | TCP + TLS (2-3 RTT) | QUIC (1-RTT ou 0-RTT) |
| Adoção | Universal | > 60% web | ~30% e crescendo |
| Troubleshooting | Wireshark fácil | Wireshark com plugin | Difícil (UDP + encrypt) |

---

## TLS 1.3 — Handshake Otimizado

```
TLS 1.2: 2 RTT para handshake (Client Hello → Server Hello → Certificate → Finished...)
TLS 1.3: 1 RTT — cliente envia key share junto com Client Hello

Client Hello + KeyShare ──────────────────────────────►
                         ◄──── Server Hello + Cert + Finished
Finished + dados ─────────────────────────────────────►
```

**Session Resumption (0-RTT):** com PSK (Pre-Shared Key) de sessão anterior, cliente pode enviar dados no primeiro pacote. Cuidado: dados 0-RTT são **replay-able** — não usar para operações não-idempotentes (POST, PUT).

## Conceitos Relacionados
[[dns]] · [[service-mesh]] · [[websocket-sse-realtime]] · [[api-gateway-bff]] · [[load-balancer]]

---
*Fonte: tech-mentor skill · tech-mentor-networking · 2026-04-17*
