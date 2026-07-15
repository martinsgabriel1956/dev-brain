---
type: concept
title: "Protocolo de Rede"
aliases: ["network protocol", "TCP/IP", "HTTP", "modelo em camadas", "OSI"]
date_created: 2026-06-26
date_updated: 2026-07-15
source_count: 6
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

## UDP em tempo real: jogos e videochamada

Jogos online (ex.: FPS) e videochamada (ex.: Google Meet) usam UDP em vez de TCP/HTTP porque toleram perda de pacote em troca de velocidade — é por isso que uma chamada de vídeo "pixela" ou trava quando a rede piora: os pacotes perdidos simplesmente não são reenviados. Encapsular cada frame/tiro numa requisição HTTP seria inviável (overhead de desempacotar sessão, headers e cookies a cada interação). Esse tipo de tráfego exige [[wiki/concepts/load-balancer|load balancer de camada 4]], que só encaminha bytes por IP/porta sem interpretar o conteúdo.

## O que acontece antes do primeiro byte de um JSON

Antes de qualquer resposta HTTP chegar, três etapas já consumiram latência: **DNS** resolve o nome para IP, o **TCP three-way handshake** (SYN, SYN-ACK, ACK) abre a conexão, e o **TLS** negocia a criptografia por cima dela — só então o HTTP trafega. Quando um app está lento, o gargalo costuma estar numa dessas camadas, não no código de tela; quem entende essa sequência debuga em minutos o que quem só opera CRUD leva dias chutando. Ver [[wiki/concepts/bluetooth-le]] para o equivalente em conexões sem fio de curto alcance (advertising → scan → pair → GATT, em vez de DNS → TCP → TLS).

## Porta: o endereçamento dentro do host

`IP:porta` é o par completo de endereçamento: o IP diz qual host (camada de rede), a porta diz qual serviço/processo dentro daquele host (camada de transporte). Portas são um número virtual de 0 a 65.535, administradas pela [[wiki/entities/iana]] em três faixas — well-known (ex. HTTP/80, HTTPS/443, SSH/22), registered (ex. RDP/3389) e private/dynamic, estas últimas atribuídas pelo sistema operacional ao **cliente** a cada nova conexão de saída, para que a resposta volte ao processo exato que a originou (ex.: cada aba de vídeo aberta ganha sua própria porta dinâmica local, mesmo todas conectando ao mesmo servidor remoto na porta 443). Ver [[wiki/concepts/porta-de-rede]] para as faixas, estados de conexão (`LISTEN`/`ESTABLISHED`) e ferramentas de diagnóstico (`ss` no Linux, `netstat` no Windows).

## Relação com outros conceitos

- [[abstracao]] — o modelo em camadas é abstração aplicada a redes: cada camada esconde como a de baixo funciona
- [[criptografia]] — HTTPS adiciona TLS entre HTTP e TCP para encriptar o conteúdo
- [[acid]] — bancos de dados distribuídos dependem de redes confiáveis; latência de rede é uma variável em sistemas distribuídos
- [[wiki/concepts/server-sent-events]] — exemplo de conexão TCP/HTTP mantida aberta indefinidamente para streaming unidirecional

## Key sources

- [[wiki/sources/portas-de-rede-como-funcionam]] — porta como endereçamento de serviço dentro do host, faixas IANA e portas dinâmicas
- [[wiki/sources/10-conceitos-fundamentais-computacao]]
- [[wiki/sources/server-sent-events-sse-tempo-real]] — SSE como tunelamento HTTP/TCP mantido aberto
- [[wiki/sources/updates-tempo-real-polling-sse-websocket]] — handshake HTTP→TCP do WebSocket e por que exige LB de camada 4
- [[wiki/sources/escalabilidade-horizontal-load-balancer-algoritmos]] — UDP em jogos e videochamada; analogia dos Correios para camada 4 (caminhoneiro) vs camada 7 (atendente/triagem)
- [[wiki/sources/operador-de-crud-vs-engenheiro-repertorio]] — DNS → TCP handshake → TLS → HTTP como latência escondida atrás de "digitar uma URL e apertar enter"
