---
type: source
title: "ICMP Browser: navegando na internet via ping em Go (Michel Leonardo)"
aliases: ["icmp browser", "navegador sobre icmp", "proxy icmp em go"]
date_created: 2026-09-30
date_updated: 2026-09-30
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/icmp-browser-navegar-na-internet-via-ping-go-michel-leonardo.md
source_url: ""
author: "Michel Leonardo"
date_published: ""
date_ingested: 2026-09-30
source_count: 0
tags: [icmp, ipv6, mtu, fragmentacao, proxy, go, golang, gambiarra, prova-de-conceito, networking]
skill: tech-mentor-networking
status: stable
---

## TL;DR

[[wiki/entities/michel-leonardo]] constrói o [[wiki/entities/icmp-browser]]: um proxy em Go que carrega páginas web **sem HTTP entre cliente e proxy**, usando só o [[wiki/concepts/icmp]] (Echo Request/Reply do `ping`) sobre [[wiki/concepts/ipv6]]. O HTML é baixado pelo lado servidor, fatiado em pedaços de 1024 bytes para fugir do [[wiki/concepts/mtu]] e da [[wiki/concepts/fragmentacao-ip]], e devolvido no campo de dados das respostas, com um mini-protocolo próprio (4 bytes iniciais = total de pedaços) e remontagem por array no cliente ([[wiki/concepts/remontagem-de-pacotes-fora-de-ordem]]). Um web server Go com `html/template` exibe o resultado no navegador comum. É uma prova de conceito assumida: sem imagens, sem fontes, lenta, sem retransmissão. Exemplo didático de [[wiki/concepts/icmp-tunneling]] e de [[wiki/concepts/forward-proxy]].

## Key Claims

**Claim:** O ICMP serve para reportar erros de rede e para o `ping` (Echo Request/Reply); seu campo de dados aceita conteúdo arbitrário, o que permite usá-lo como canal de transporte.
**Evidence:** Descrição do pacote no vídeo; o autor coloca o HTML no campo de dados das respostas de eco e o navegador de teste carrega páginas reais.
**Confidence:** alta — coerente com o comportamento padrão do ICMP e com o uso de ICMP como canal encoberto ([external] RFC 792 / RFC 4443).

**Claim:** O tamanho máximo do campo de dados em IPv6 é ~65 KB, mas o MTU (~1500 bytes; o áudio diz "10000", provável erro de transcrição) impede enviar um HTML inteiro num pacote sem fragmentação.
**Evidence:** Raciocínio do autor; a solução adotada é fatiar em 1024 bytes por resposta.
**Confidence:** média — o número de 65 KB corresponde ao limite do campo *Payload Length* de 16 bits do IPv6 (sem jumbograms) [external]; o valor de MTU citado está corrompido e foi corrigido por conhecimento externo (Ethernet = 1500), sinalizado no raw.

**Claim:** Com fragmentação, a perda de um único fragmento faz o destino descartar todos os demais, e o ICMP não oferece entrega garantida nem retransmissão, ao contrário do TCP.
**Evidence:** Explicação do vídeo (exemplo de três fragmentos); o autor decide não implementar retransmissão por complexidade.
**Confidence:** alta — é o comportamento conhecido do reassembly IP; contraste com [[wiki/concepts/tcp-three-way-handshake]] (TCP como transporte confiável).

**Claim:** Filtrar o tráfego ICMP recebido pelo primeiro byte (tipo) é necessário porque a interface recebe muito ICMP não solicitado; só o tipo 128 (Echo Request) interessa ao servidor e 129 (Echo Reply) ao cliente.
**Evidence:** O autor relata o "caos" de pacotes inesperados (erros de roteador) e a solução por tipo. O áudio diz "1228", corrigido para 128 (ICMPv6 Echo Request).
**Confidence:** alta para os números 128/129 em ICMPv6 [external RFC 4443]; a correção da transcrição é inferência.

**Claim:** Um protocolo mínimo sobre o campo de dados (4 bytes de "total de pedaços" + payload) mais o número de sequência do ICMP bastam para saber quando a resposta terminou e reordenar pedaços num array pré-alocado.
**Evidence:** Descrição do lado cliente; o autor admite que não é o método mais eficiente, "mas para um experimento funciona".
**Confidence:** média — funciona na demo local; sem tratamento de perda, duplicação ou timeout, segundo o próprio vídeo.

**Claim:** O sistema é, na prática, um proxy: um intermediário baixa o site por você e devolve só a resposta, escondendo seu IP do site de destino.
**Evidence:** Analogia do "computador contratado" no vídeo.
**Confidence:** média — vale para ocultar o IP do cliente perante o site; **inferência** (não dita no vídeo): o canal ICMP não tem criptografia nem autenticação, então não protege contra quem observa a rede e um servidor assim aberto seria um relay abusável.

**Claim:** O sistema de templates nativo do Go (`html/template`) dispensa criar uma API para levar dados do backend à tela.
**Evidence:** O autor renderiza o HTML recebido via ICMP num web server Go com template; ver [[wiki/concepts/go-stdlib]].
**Confidence:** alta — recurso conhecido da stdlib; detalhes (escape automático do `html/template`) não foram tratados na fonte.

## Entities & Concepts Touched

- [[wiki/entities/michel-leonardo]]
- [[wiki/entities/icmp-browser]]
- [[wiki/concepts/icmp]]
- [[wiki/concepts/mtu]]
- [[wiki/concepts/fragmentacao-ip]]
- [[wiki/concepts/ipv6]]
- [[wiki/concepts/icmp-tunneling]]
- [[wiki/concepts/forward-proxy]]
- [[wiki/concepts/remontagem-de-pacotes-fora-de-ordem]]
- [[wiki/concepts/tcp-three-way-handshake]]
- [[wiki/concepts/dns]]
- [[wiki/concepts/tunelamento]]
- [[wiki/concepts/vpn]]
- [[wiki/concepts/reverse-proxy]]
- [[wiki/concepts/proxy-pattern]]
- [[wiki/concepts/go-stdlib]]
- [[wiki/concepts/http-vs-https]]
- [[wiki/concepts/array]]
- [[wiki/concepts/ddos-syn-flood]]

## Open Questions

- Valor exato do MTU citado (áudio "10000 bytes"): corrigido para ~1500 por conhecimento geral; não confirmado pelo autor.
- Em IPv6, roteadores **não fragmentam** (só a origem) e reportam "Packet Too Big" (ICMPv6 tipo 2); a explicação do vídeo ("fragmentação do Tel/IP", roteador descarta e avisa) mistura o comportamento IPv4/IPv6. Verificar em [external] RFC 8200 / RFC 4443.
- Payloads de 1024 bytes cabem em 1500 de MTU, mas o vídeo não mostra o cálculo dos cabeçalhos; por que não fragmentaria fica implícito.
- Como o cliente lida com pacotes perdidos/duplicados e com sessões simultâneas (ID/sequência)? Não abordado; código citado na descrição do vídeo, não acessado.
- Viabilidade prática de expor um proxy ICMP na internet (filtros de ICMP em firewalls/provedores) não discutida.
- O vídeo anterior do canal (codec de vídeo sobre ICMP) e o post sobre Doom via DNS não foram acessados.

## Raw Quotes

> "o ICMP não é igual o TCP, ele não tem garantia de entrega nem retransmissão."

> "a gente acabou de criar um proxy."

> "esse projeto obviamente tem muitas limitações por conta que ele é apenas uma prova de conceito."
