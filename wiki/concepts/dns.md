---
type: concept
title: "DNS — Domain Name System"
aliases: [Domain Name System]
date_created: 2026-04-22
date_updated: 2026-08-19
source_count: 6
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

## DNS como "agenda telefônica" e propagação de name servers

[[wiki/sources/enderecos-ip-dns-dominios-https-aws-fernanda-kipper]] usa a analogia da **agenda telefônica**: servidores DNS espalhados pelo mundo recebem o [[wiki/concepts/dominio|domínio]] e devolvem o [[wiki/concepts/endereco-ip|endereço IP]] correspondente. A resolução costuma partir do provedor de internet (ex.: Claro), que consulta um DNS quando o navegador pede um domínio. A fonte também torna concreta a **propagação DNS**: ao trocar os *name servers* de um domínio no registrador (ex.: [[wiki/entities/godaddy]] → [[wiki/concepts/aws-route-53|Route 53]]), a mudança leva minutos porque precisa ser replicada para todos os servidores DNS do mundo — verificável em ferramentas "DNS propagation checker".

## DNS vs. Load Balancer

Confusão comum: os dois "decidem para onde a requisição vai", mas em camadas diferentes. Analogia de restaurante usada em [[wiki/sources/system-design-load-balancer-nivel-macaco]]: DNS decide **em qual mesa você senta** (resolve nome → IP, escolhe a rota); o [[wiki/concepts/load-balancer]] decide **qual garçom vai te atender** (decide quem/como atende dentro daquela rota). A diferença técnica: DNS apenas traduz nome em endereço, sem saber se o destino está saudável — por isso é possível resolver um domínio corretamente e ainda cair num erro no meio do caminho. O load balancer faz health check ativo dos servidores e só roteia para instâncias saudáveis, redirecionando na hora se uma estiver sobrecarregada ou fora do ar.

## Key sources
- [[sources/dns]]
- [[wiki/sources/system-design-load-balancer-nivel-macaco]] — distinção didática DNS vs. Load Balancer (analogia de restaurante) e o health check como diferencial do load balancer
- [[wiki/sources/enderecos-ip-dns-dominios-https-aws-fernanda-kipper]] — DNS como agenda telefônica (domínio → IP); resolução via provedor; propagação de name servers
- [[wiki/sources/portas-de-rede-como-funcionam]] — DNS como resolução de nome, complementar à porta como resolução de serviço
- [[wiki/sources/pipeline-de-renderizacao-do-browser-url-ate-pixel]] — DNS como primeira etapa de rede do critical rendering path, analogia com lista de contatos do celular
- [[wiki/sources/email-address]] — registros MX como aplicação de DNS ao roteamento de e-mail (SMTP)
