---
type: concept
title: "localhost e loopback (127.0.0.1)"
aliases: ["localhost", "loopback", "127.0.0.1", "::1", "host local"]
date_created: 2026-11-21
date_updated: 2026-11-21
source_count: 3
tags: [localhost, loopback, ip, desenvolvimento-local, networking]
skill: tech-mentor-networking
status: stub
---

# localhost e loopback (127.0.0.1)

`localhost` é o nome que resolve para o endereço de *loopback* da própria máquina: `127.0.0.1` em IPv4 (todo o bloco `127.0.0.0/8` é reservado) e `::1` em IPv6 `[external]` (RFC 6761 §6.3, https://www.rfc-editor.org/rfc/rfc6761#section-6.3; RFC 1122). O pacote nunca sai da placa de rede: volta para o mesmo computador.

## Por que o outro celular não abre

No [[wiki/entities/frontpush|FrontPUSH]] ([[wiki/sources/frontpush-introducao-hospedagem-de-websites-url-localhost-porta]]), a animação roda em `127.0.0.1:5500/index.html` e a pergunta é por que o endereço não funciona "em outro celular, por mais que esteja na rede da minha própria casa". A aula só diz que 127.0.0.1 "é a sua própria máquina". O resto `[skill: tech-mentor-networking]`:

1. No celular, `127.0.0.1` é o **celular**.
2. Na mesma rede, use o IP privado do computador (`192.168.x.x:5500`). Só funciona se o servidor escutar nessa interface (`0.0.0.0`, não só `127.0.0.1`) e o firewall liberar a porta.
3. Da internet, o IP privado não é roteável (fica atrás do NAT do roteador). Daí a [[wiki/concepts/hospedagem-de-sites|hospedagem]] (ou um túnel, para testes).

## Na NLW e no JStack

O mesmo par localhost × IP da máquina aparece no app mobile da NLW #1 e #2 (ver [[wiki/concepts/endereco-ip]]); no JStack, o Node sem host escuta em todas as interfaces (ver [[wiki/concepts/porta-de-rede]]).

Ver também [[wiki/concepts/url]].

## FrontPUSH, hospedagem aula 02: a resposta

Em [[wiki/sources/frontpush-ip-e-dns-ipv4-ipv6-ip-publico-privado-registro-br]], a pergunta da aula 01 é respondida: "se eu digitar localhost, ele vai estar apontando para ele mesmo"; no celular, `192.168.1.92:5500`, "mas [...] ele precisa estar na mesma rede", "no mesmo Wi-Fi". Funcionou porque o servidor local escutava na interface de rede.

## FrontPUSH, hospedagem aula 03

Em [[wiki/sources/frontpush-website-estatico-vs-aplicacao-web-php-apache-xampp-react]], `http://localhost/frontpush` (Apache do [[wiki/entities/xampp]] na porta 80, "a minha própria máquina") e `localhost:3000` (servidor de desenvolvimento do React) só respondem com o servidor ligado.

## Key sources

- [[wiki/sources/frontpush-introducao-hospedagem-de-websites-url-localhost-porta]]: 127.0.0.1 = localhost = "a sua própria máquina"; a pergunta do celular
- [[wiki/sources/frontpush-ip-e-dns-ipv4-ipv6-ip-publico-privado-registro-br]]: FrontPUSH, hospedagem aula 02: 192.168.1.92:5500 no celular, mesma rede
- [[wiki/sources/frontpush-website-estatico-vs-aplicacao-web-php-apache-xampp-react]]: FrontPUSH, hospedagem aula 03: localhost/frontpush e localhost:3000
