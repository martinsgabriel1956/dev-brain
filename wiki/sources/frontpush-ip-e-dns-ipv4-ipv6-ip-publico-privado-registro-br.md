---
type: source
title: "O que é IP e o que é DNS: IPv4 × IPv6, IP público × privado, Registro.br (FrontPUSH)"
aliases: ["FrontPUSH hospedagem aula 02", "IP & DNS", "Módulo de hospedagem, aula 02"]
date_created: 2026-11-21
date_updated: 2026-11-21
source_count: 0
tags: [ip, ipv4, ipv6, ip-publico, ip-privado, nat, rfc-1918, dns, dominio, registro-br, ping, icmp, hospedagem, internet-das-coisas, curso, frontend, networking]
skill: tech-mentor-networking
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/frontpush-ip-e-dns-ipv4-ipv6-ip-publico-privado-registro-br.md"
source_url: ""
author: "Násser (inferido)"
date_published: ""
date_ingested: 2026-11-21
---

# O que é IP e o que é DNS: IPv4 × IPv6, IP público × privado, Registro.br (FrontPUSH)

## TL;DR

Segunda aula do módulo de hospedagem do [[wiki/entities/frontpush|FrontPUSH]], cerca de 9 minutos, "bem superficial", com dois slides, as configurações de rede do Windows, `ping` no prompt e o site da [[wiki/entities/registro-br|Registro.br]]. [[wiki/entities/nasser|Násser]] não diz o nome em primeira pessoa; as perguntas de aluno que ele encena ("Ah, Násser, qual é a diferença...") e o domínio "o Násser também" confirmam a autoria (a legenda trouxe "Lácia", "Nascia", "nasher"). Responde a pergunta deixada na aula 01 ([[wiki/sources/frontpush-introducao-hospedagem-de-websites-url-localhost-porta]]).

- **IP:** "O IP é um protocolo"; "identificar o seu dispositivo na internet", como um CPF; serve para saber "para quem eu estou mandando" o pacote ([[wiki/concepts/endereco-ip]]).
- **IPv4 × IPv6:** "quatro grupos [...] com 32 bits" × "oito grupos que constituem 128 bits"; o IPv6 existe por causa da "internet das coisas", "muito dispositivo para pouco endereço", "mas a gente sempre está utilizando o IPv4" ([[wiki/concepts/ipv6]]).
- **O celular, resolvido:** `localhost` no celular aponta "para ele mesmo"; digita-se o IP do computador, `192.168.1.92:5500`, e "ele vai rodar", desde que "na mesma rede", "no mesmo Wi-Fi" ([[wiki/concepts/localhost]]).
- **Privado × público:** a rede de casa é privada; para hospedar, "você precisa ter um IP público e o IP público é fixo". `ping frontpush.com.br` → `162.241.61.29`, "o IP do servidor em que está hospedado o meu website" ([[wiki/concepts/ip-publico-vs-ip-privado]]).
- **DNS:** "converte nomes de domínio em endereço de IP", porque "é bem mais fácil eu lembrar de um nome do que lembrar de um IP" ([[wiki/concepts/dns]]).
- **Registro.br:** "o órgão para poder a gente registrar o domínio no Brasil"; frontpush.com.br, creatorpush.com.br e o domínio do autor já registrados, "todos eles [...] no mesmo servidor que é na HostGator" ([[wiki/concepts/dominio]], [[wiki/entities/hostgator]]).

## Slides

**Slide 1, "O que é IP? E DNS?"**
- "Significa Internet Protocol, um protocolo de internet que identifica o seu dispositivo na internet e permite a comunicação entre eles."
- "IPv4 x IPv6: Qual a diferença?" — "IPv4: 255.255.255.255: São 4 grupos c/ 32 bits"; "IPv6: 3002:0bd6:0000:0000:0000:ee00:0033:6778 : São 8 grupos c/ 128 bits".
- "IP Privado x IP público" — "Classe A: Faixa de 10.0.0.0 a 10.255.255.255"; "Classe B: Faixa de 172.16.0.0 a 172.31.255.255"; "Classe C: Faixa de 192.168.0.0 a 192.168.255.255".

**Slide 2, "O que é o DNS?"**
- "O DNS converte nomes de domínio em endereços IP para que os navegadores possam carregar os recursos da internet."
- `www.seudominio.com.br` → `154.168.1.21`; embaixo da seta, "Mozilla Firefox, Google Chrome, Opera"; embaixo do IP, "Seu servidor de hospedagem com a sua página HTML".
- "Registro.br — Órgão para registrar o seu domínio no Brasil".

## Key Claims

### Abertura

- "Esses conceitos aqui [...] eu não vou aprofundar muito, vai ser bem superficial", mas servem para quando ele estiver "ensinando o método mais tradicional de hospedagem de websites".

### O que é o IP

- "O IP é um protocolo." A internet é "um conglomerado de computadores e eles precisam se comunicar, eu preciso estabelecer regras de comunicação e é isso que os protocolos fazem" ([[wiki/concepts/protocolo-de-rede]]).
- "O protocolo de internet nada mais faz do que identificar o seu dispositivo na internet." Analogia: "assim como você, pessoa, detém de um CPF que identifica você [...] no Brasil", o computador "precisa de um IP", para que, "mandando o pacote na internet, eu preciso saber para quem eu estou mandando".

### IPv4 e IPv6

- Nas configurações do computador aparecem "a velocidade da conexão", "o endereço IPv6 e o endereço IPv4".
- "Na maioria das vezes eu só vejo o IPv4, a gente não utiliza o IPv6." IPv4: "quatro grupos [...] com 32 bits"; IPv6: "oito grupos que constituem 128 bits de endereçamento".
- Por que o IPv6: "internet das coisas", "geladeiras, lâmpadas inteligentes, casas inteligentes"; o IPv4 "vai ser insuficiente para tanto dispositivo", "muito dispositivo para pouco endereço".

### Acessando o site de outro celular

- "Servidor DNS [...] 192.168.1.154"; "o endereço IPv4 do meu computador é 192.168.1.92".
- "Se eu digitar localhost, ele vai estar apontando para ele mesmo, então não faz sentido." No outro celular: "192.168.1.92 e na porta 5500", e "ele vai rodar, mas [...] ele precisa estar na mesma rede". "Um dispositivo só vai enxergar o outro quando ele está na mesma rede. E no caso, essa rede aqui é privada."

### Rede privada e rede pública

- "Para você estar na internet de fato e visível para toda essa rede de computadores, você precisa ter um IP público e o IP público é fixo." Demonstração: `ping www.google.com.br` "me dá um endereço de IP"; `ping frontpush.com.br` dispara em `162.241.61.29`, "o IP do servidor em que está hospedado o meu website", "um IP fixo e público, enquanto o 192.168 é uma rede privada" ([[wiki/concepts/icmp]]).
- "Na sua casa, se você verificar o seu IP, provavelmente ele pode ser igual ao meu, mas ele está em uma rede privada." "Quando você faz alguma coisa na internet, ele faz a demodulação de uma rede privada para uma rede pública" (ver Precisões).
- Outro Wi-Fi "também não vai conseguir enxergar". "Precisa de um IP público, porque senão a gente não consegue, de fato, hospedar na internet" ([[wiki/concepts/hospedagem-de-sites]]).

### O que é o DNS

- "O DNS nada mais é do que ele converte nomes de domínio em endereço de IP"; o `ping` em frontpush.com.br "vinculou esse nome a um IP".
- "Eu consigo acessar o meu site digitando 162.241.61.29, mas é bem mais difícil eu lembrar desse número do que sempre lembrar do nome FrontPUSH" (ver Precisões).
- O domínio "sempre é vinculado a um número de IP, que é o servidor que está com a sua página lá", acessado "por meio do protocolo HTTP para mostrar no browser" ([[wiki/concepts/http-vs-https]]).

### Registro.br

- "Para você registrar domínios no Brasil, sempre vem aqui na Registro.br." Buscando frontpush.com.br: "não está mais disponível porque já está registrado no meu nome", com sugestões ".app, .art, .blog".
- "Registrar o seu nome para deixar fixo apontando para um IP, que é o servidor que você pode hospedar em qualquer lugar." creatorpush.com.br e o domínio do autor também registrados; "todos eles estão no mesmo servidor que é na HostGator", tema das "próximas aulas" ([[wiki/entities/creatorpush]]).

## Precisões e ressalvas

1. **"O IP é público, logo fixo" mistura duas coisas.** Público × privado é sobre roteabilidade; fixo × dinâmico é sobre se o endereço muda. A internet de casa costuma ter IP público **dinâmico** (ou nem isso, com CGNAT); o servidor precisa de um IP estável para o registro DNS valer `[skill: tech-mentor-networking]` (alta). Ver [[wiki/concepts/ip-publico-vs-ip-privado]].
2. **"Demodulação" é NAT.** O roteador traduz o IP privado de cada aparelho para o IP público da casa (NAT/PAT); demodular é o que o modem faz com o sinal, outra coisa `[skill: tech-mentor-networking]` (alta). É por isso que o IP de casa "pode ser igual ao meu".
3. **"Classe A/B/C" no slide é nomenclatura antiga.** As faixas estão certas (RFC 1918: `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`), mas o endereçamento por classes foi substituído pelo CIDR em 1993 `[external]` (https://www.rfc-editor.org/rfc/rfc1918; https://www.rfc-editor.org/rfc/rfc4632; alta). Classe A, B e C são faixas maiores que estas; as privadas são só um pedaço de cada.
4. **IPv6 não é só para o futuro da IoT.** O pool central de IPv4 da IANA esgotou em 2011, e o NAT foi o remendo que adiou a falta. "A gente não utiliza o IPv6" também envelheceu: uma parte grande dos acessos ao Google, inclusive no Brasil, já chega por IPv6 `[external]` (https://www.google.com/intl/en/ipv6/statistics.html; média, o número oscila).
5. **"IP como CPF" vale até certo ponto.** O CPF acompanha a pessoa; o IP é mais um endereço de entrega: muda quando o aparelho troca de rede e, com NAT, vários aparelhos dividem o mesmo IP público.
6. **`ping` não é HTTP.** Usa ICMP; a resolução de nome que o `ping` mostra é o DNS trabalhando, e servidores podem bloquear ICMP e ainda servir o site ([[wiki/concepts/icmp]]).
7. **Acessar pelo IP numa hospedagem compartilhada** costuma cair na página padrão do servidor, não no site, porque o mesmo IP atende muitos domínios e o servidor escolhe pelo cabeçalho `Host` ([[wiki/concepts/virtual-host]]) `[skill: tech-mentor-networking]` (média; vale se o plano não tiver IP dedicado). O próprio autor diz que FrontPUSH, CreatorPUSH e portfólio dividem o servidor. `162.241.x.x` é de fato faixa usada pela HostGator `[inferência; média]`.
8. **"Servidor DNS 192.168.1.154"** é o roteador (ou um equipamento da rede) repassando as consultas; quem resolve de fato é o resolver recursivo do provedor ou público, que percorre raiz → TLD → autoritativo. O slide põe "Firefox, Chrome, Opera" na seta, mas a consulta parte do sistema operacional (ou do DoH do browser) ([[wiki/concepts/dns]]).
9. **Registro.br registra só domínios `.br`** (`.com.br`, `.app.br`, `.art.br`, `.blog.br`...), operado pelo NIC.br. Para `.com`, `.app` e outros TLDs genéricos, o caminho é um registrador como a [[wiki/entities/godaddy]] `[external]` (https://registro.br; alta). As sugestões da tela são categorias `.br`.
10. **O celular só abriu `192.168.1.92:5500`** porque o servidor local escutava na interface de rede, não só em `127.0.0.1`, e o firewall deixou passar. Isso confirma o que a aula 01 deixava em aberto ([[wiki/concepts/localhost]]).

## Entities

- [[wiki/entities/frontpush]], [[wiki/entities/nasser]], [[wiki/entities/creatorpush]]
- [[wiki/entities/registro-br]] (novo), [[wiki/entities/hostgator]], [[wiki/entities/godaddy]] (contraste), [[wiki/entities/google]] (alvo do `ping`)

## Concepts

- [[wiki/concepts/endereco-ip]], [[wiki/concepts/ipv6]], [[wiki/concepts/ip-publico-vs-ip-privado]] (novo)
- [[wiki/concepts/dns]], [[wiki/concepts/dominio]], [[wiki/concepts/localhost]], [[wiki/concepts/icmp]]
- [[wiki/concepts/protocolo-de-rede]], [[wiki/concepts/hospedagem-de-sites]], [[wiki/concepts/segmentacao-de-rede-por-faixa-de-ip-e-firewall]]

## Open Questions

- O plano da HostGator do autor tem IP dedicado? Se não, digitar `162.241.61.29` mostra mesmo o FrontPUSH?
- O DNS dos três domínios aponta para o IP da HostGator por registro A ou pelos name servers da HostGator?

## Raw quotes

> "É literalmente muito dispositivo para pouco endereço."

> "Para você estar na internet de fato e visível para toda essa rede de computadores, você precisa ter um IP público."

> "É bem mais fácil eu lembrar de um nome do que lembrar de um IP."

## Continuação

As "próximas aulas" vão mostrar como os três domínios ficam no mesmo servidor da HostGator. A aula 03 ([[wiki/sources/frontpush-website-estatico-vs-aplicacao-web-php-apache-xampp-react]]) antes separa website estático de aplicação web: CreatorPUSH estático, FrontPUSH em PHP.
