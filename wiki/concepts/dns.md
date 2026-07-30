---
type: concept
title: "DNS — Domain Name System"
aliases: [Domain Name System]
date_created: 2026-04-22
date_updated: 2026-07-30
source_count: 4
tags: [dns, rede, infraestrutura]
skill: tech-mentor-system-design
status: stub
---
# DNS — Domain Name System

Sistema que traduz nomes de domínio legíveis (ex: `api.empresa.com`) em endereços IP. É o primeiro componente atravessado por qualquer requisição. O fluxo de resolução percorre cache local → resolver recursivo → root NS → TLD NS → authoritative NS, cacheando cada nível pelo TTL configurado.

DNS e [[wiki/concepts/porta-de-rede|porta]] resolvem endereçamento em camadas diferentes e complementares: DNS resolve nome → IP (qual host); a porta resolve IP → serviço (qual processo dentro daquele host). Uma requisição só chega ao destino final depois das duas resoluções.

DNS é a primeira etapa de rede do [[wiki/concepts/critical-rendering-path]] do browser: o browser resolve o domínio para IP antes de abrir a conexão via [[wiki/concepts/tcp-three-way-handshake]].

## Registros MX — DNS aplicado a roteamento de e-mail

[[wiki/sources/email-address]] mostra um uso de DNS específico para SMTP: agentes de e-mail (MUA/MTA) consultam registros **MX** (Mail Exchange) para descobrir o servidor de e-mail responsável por um domínio, antes de entregar a mensagem via SMTP. Na ausência de registro MX, a resolução cai para os registros A/AAAA do próprio domínio. É o mesmo padrão de "nome → recurso" do DNS geral, só que aplicado à pergunta "qual servidor recebe e-mail para este domínio", não "qual IP responde por este host".

## Key sources
- [[sources/dns]]
- [[wiki/sources/portas-de-rede-como-funcionam]] — DNS como resolução de nome, complementar à porta como resolução de serviço
- [[wiki/sources/pipeline-de-renderizacao-do-browser-url-ate-pixel]] — DNS como primeira etapa de rede do critical rendering path, analogia com lista de contatos do celular
- [[wiki/sources/email-address]] — registros MX como aplicação de DNS ao roteamento de e-mail (SMTP)
