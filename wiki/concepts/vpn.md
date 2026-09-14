---
type: concept
title: "VPN — Virtual Private Network"
aliases: ["vpn", "rede privada virtual", "virtual private network"]
date_created: 2026-09-14
date_updated: 2026-09-14
source_count: 1
tags: [vpn, networking, tunelamento, criptografia, seguranca]
skill: tech-mentor-networking
status: draft
---

# VPN — Virtual Private Network

**Privada** porque é de acesso restrito a uma organização ou pessoa; **virtual** porque usa a infraestrutura de uma rede pública (a internet) em vez de um link físico dedicado. A rede "virtual" é construída via [[wiki/concepts/tunelamento]]: um túnel lógico que carrega apenas o tráfego criptografado daquele acesso específico, sobre a mesma infraestrutura pública que qualquer outro tráfego de internet usa.

## Caso de uso 1 — Conectar redes distantes (site-to-site)

Matriz e filial de uma empresa, em cidades diferentes, querem conectar suas redes sem expor dados na internet pública. Em vez de contratar um link físico dedicado (caro, lento de provisionar), a empresa cria um túnel VPN sobre a internet: os dados trafegam pela mesma infraestrutura pública que qualquer usuário usa, mas criptografados e isolados dentro do túnel.

Implementações modernas resolvem isso com WireGuard (site-to-site com `AllowedIPs` apontando para a sub-rede remota) ou IPSec (mais comum em equipamento de rede legado — roteadores Cisco/Juniper — e em VPNs gerenciadas por cloud, como AWS Site-to-Site VPN).

## Caso de uso 2 — Acesso remoto / bypass de restrição geográfica

Um usuário se conecta a um provedor de VPN e todo (ou parte d)o seu tráfego passa a sair pelo IP do servidor VPN, não pelo IP real do usuário. Isso serve tanto para acesso remoto seguro a uma rede corporativa quanto para contornar geo-blocking — acessar conteúdo restrito por localização geográfica "como se" o provedor de VPN estivesse fazendo o acesso. Ver [[wiki/concepts/restricao-geografica-geo-blocking]].

## VPN tradicional vs. Zero Trust (ZTNA)

VPN clássica cria uma zona de confiança plana: uma vez dentro do túnel, o cliente tem acesso à rede inteira (ou a uma sub-rede ampla) — comprometer um único endpoint dentro da VPN pode significar acesso lateral a tudo. ZTNA substitui esse modelo por "nunca confie, sempre verifique": cada request é autorizado individualmente por identidade + postura do dispositivo, sem expor a rede inteira. Ver contraste detalhado em [[wiki/sources/zero-trust]].

Híbrido comum na prática: WireGuard/VPN para acesso de infra (SSH, banco de dados direto), ZTNA (Cloudflare Access, Tailscale) para acesso a aplicações web internas.

## Protocolos

WireGuard (moderno, kernel-integrado, ~4000 linhas de código, alta performance) tende a substituir OpenVPN (userspace, ~70k linhas) e IPSec (~400k linhas, mais complexo, ainda dominante em equipamento legado e VPNs site-to-site gerenciadas por cloud). Detalhes de configuração, split tunneling e key management em escala (Tailscale/Headscale) estão na referência `vpn-wireguard.md` da skill `tech-mentor-networking` — não cobertos pela fonte introdutória que originou esta página.

## Relação com outros conceitos

- [[wiki/concepts/tunelamento]] — o mecanismo que torna a VPN "virtual"
- [[wiki/concepts/criptografia]] — a garantia de confidencialidade dentro do túnel
- [[wiki/concepts/restricao-geografica-geo-blocking]] — um dos usos práticos mais comuns de VPN hoje
- [[wiki/concepts/mtls]] — autenticação mútua por certificado, mecanismo relacionado usado em alternativas de acesso como ZTNA/service mesh

## Key sources

- [[wiki/sources/vpn-conceito-tunelamento-acesso-remoto]] — definição introdutória, caso de uso matriz/filial e bypass de restrição geográfica
- [[wiki/sources/tls-mtls-vpn]] — comparação técnica WireGuard vs. IPSec vs. OpenVPN, Tailscale como WireGuard gerenciado
- [[wiki/sources/zero-trust]] — contraste VPN tradicional (zona de confiança plana) vs. ZTNA (verificação por request)
