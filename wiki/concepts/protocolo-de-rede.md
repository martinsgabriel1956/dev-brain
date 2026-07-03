---
type: concept
title: "Protocolo de Rede"
aliases: ["network protocol", "TCP/IP", "HTTP", "modelo em camadas", "OSI"]
date_created: 2026-06-26
date_updated: 2026-07-03
source_count: 3
tags: [cs-fundamentals, redes, protocolos, tcp-ip, http, networking]
skill: cs-fundamentals
status: draft
---

# Protocolo de Rede

**Regras que definem como computadores se comunicam.** Sem protocolos, cada sistema teria seu próprio formato — nenhum conseguiria falar com o outro.

## O modelo em camadas

A comunicação em rede é organizada em camadas — cada uma responsável por um aspecto específico, escondendo os detalhes das demais:

| Camada | Responsabilidade | Exemplo |
|---|---|---|
| **Aplicação** | O que dizer | HTTP, HTTPS, WebSocket, gRPC |
| **Transporte** | Como garantir entrega | TCP (confiável), UDP (rápido) |
| **Rede** | Para onde enviar | IP — endereçamento e roteamento |
| **Física** | Como transmitir bits | Ethernet, Wi-Fi, fibra ótica |

## Como uma requisição HTTP funciona

```
1. Browser → HTTP: "GET /index.html"
2. TCP empacota e garante entrega (reenvia se perder pedaço)
3. IP determina rota pelo grafo de roteadores
4. Física transmite os bits pelo cabo/Wi-Fi
— atravessa cabos, roteadores, às vezes satélites —
5. Servidor recebe, camadas desempacotam na ordem inversa
6. Resposta retorna pelo mesmo processo
```

## TCP vs UDP

| | TCP | UDP |
|---|---|---|
| **Confiabilidade** | Garante entrega e ordem | Best-effort — pode perder pacotes |
| **Handshake** | 3-way handshake antes de enviar | Sem handshake |
| **Velocidade** | Mais lento | Mais rápido |
| **Uso** | HTTP, bancos de dados, SSH | Vídeo ao vivo, DNS, games |

## Encapsulamento

Cada camada **adiciona um cabeçalho** com suas informações ao empacotar — e **remove o cabeçalho** ao desempacotar:

```
[HTTP body]
[TCP header | HTTP body]
[IP header | TCP header | HTTP body]
[Ethernet frame | IP header | TCP header | HTTP body]
```

É como colocar uma carta dentro de um envelope dentro de outro envelope — cada um endereçado para a próxima camada.

## Conexão HTTP mantida aberta (streaming)

Nem toda comunicação HTTP segue request→resposta→fim. [[wiki/concepts/server-sent-events|SSE]] abre a conexão TCP subjacente ao HTTP e nunca finaliza a resposta — o servidor escreve continuamente dentro dela, criando um tunelamento unidirecional servidor→cliente sobre a mesma conexão. É a mesma camada de transporte (TCP) sendo usada de um jeito não convencional: a camada de aplicação (HTTP) decide não fechar o que a camada de transporte abriu.

## WebSocket: upgrade de HTTP para TCP

Diferente do SSE (que nunca sai do HTTP), o WebSocket começa como uma requisição HTTP comum, mas carrega cabeçalhos especiais (`Upgrade: websocket`, `Connection: Upgrade`) que pedem ao servidor para trocar de protocolo. Depois desse handshake, a conexão deixa de falar HTTP e passa a ser um túnel TCP bidirecional cru, mantido aberto — daí a exigência de [[wiki/concepts/load-balancer|load balancer de camada 4]], que opera no nível de TCP e não entende (nem precisa entender) o conteúdo que passa por dentro.

## Relação com outros conceitos

- [[abstracao]] — o modelo em camadas é abstração aplicada a redes: cada camada esconde como a de baixo funciona
- [[criptografia]] — HTTPS adiciona TLS entre HTTP e TCP para encriptar o conteúdo
- [[acid]] — bancos de dados distribuídos dependem de redes confiáveis; latência de rede é uma variável em sistemas distribuídos
- [[wiki/concepts/server-sent-events]] — exemplo de conexão TCP/HTTP mantida aberta indefinidamente para streaming unidirecional

## Key sources

- [[wiki/sources/10-conceitos-fundamentais-computacao]]
- [[wiki/sources/server-sent-events-sse-tempo-real]] — SSE como tunelamento HTTP/TCP mantido aberto
- [[wiki/sources/updates-tempo-real-polling-sse-websocket]] — handshake HTTP→TCP do WebSocket e por que exige LB de camada 4
