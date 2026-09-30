---
type: concept
title: "Forward Proxy"
aliases: ["proxy direto","proxy de saída","forward proxy"]
date_created: 2026-09-30
date_updated: 2026-09-30
source_count: 1
tags: [networking, proxy, privacidade, anonimato]
skill: tech-mentor-networking
status: stub
---

# Forward Proxy

Intermediário que age **em nome do cliente**: o cliente envia o link ao proxy, este acessa o site, pega o conteúdo e devolve só a resposta; o site vê o IP do proxy, não o do cliente. Oposto do [[wiki/concepts/reverse-proxy]] (que age em nome do servidor). Não confundir com o padrão de projeto [[wiki/concepts/proxy-pattern]].

Na fonte, o [[wiki/entities/icmp-browser]] é um forward proxy cujo canal cliente↔proxy é [[wiki/concepts/icmp]] ([[wiki/concepts/icmp-tunneling]]) e cujo trecho proxy↔site é HTTP normal. Inferência: como o canal não é cifrado nem autenticado, o benefício de privacidade é limitado ao IP visto pelo site. Outras categorias (SOCKS5, forward/reverse) em [skill: tech-mentor-networking — `references/networking-infra-containers.md`].

## Key sources

- [[wiki/sources/icmp-browser-navegar-na-internet-via-ping-go-michel-leonardo]] — forward proxy explicado com a analogia do computador contratado
