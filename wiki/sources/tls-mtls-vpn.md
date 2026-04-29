---
type: source
title: "TLS/mTLS e VPN"
aliases: ["tls", "mtls", "vpn", "wireguard", "tailscale", "ztna", "certificate pinning", "ocsp stapling"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/tls-mtls-vpn.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [tls, mtls, vpn, wireguard, tailscale, ztna, certificate-pinning, ocsp-stapling, pki, cert-manager, spiffe]
skill: tech-mentor-security
status: stable
---

## TL;DR

TLS 1.3: handshake em 1 RTT (vs 2 no TLS 1.2). mTLS: ambos os lados autenticam via certificado — padrão para service-to-service. cert-manager automatiza emissão e renovação de certificados em K8s. WireGuard supera OpenVPN em performance. Tailscale é WireGuard com zero configuração. ZTNA substitui VPN com acesso por identidade.

## Key Claims

**Claim:** TLS 1.3 é obrigatório — TLS 1.2 deve ser desabilitado em novos sistemas.
**Evidence:** TLS 1.3: handshake em 1 RTT (50% mais rápido). Apenas cipher suites com forward secrecy (ECDHE). Sem renegociação. Sem algoritmos legados (RC4, 3DES, MD5). TLS 1.2 ainda suportado por compatibilidade, mas configure o mínimo como TLS 1.2 com cipher suites seguras.
**Confidence:** alta

**Claim:** mTLS com cert-manager em K8s automatiza PKI interna — certificados com TTL de horas.
**Evidence:** cert-manager emite certificados via Let's Encrypt (externo) ou CA própria (interno). Renovação automática. TTL curto (< 24h) para mTLS interno — se vazar, expira rápido. SPIFFE/SPIRE para identidade de workload em ambientes multi-cluster.
**Confidence:** alta

**Claim:** Tailscale é WireGuard gerenciado com zero configuração — melhor opção para acesso de engenheiros.
**Evidence:** WireGuard tem performance superior ao OpenVPN (10× menos CPU), mas configuração complexa. Tailscale abstrai: instala em todos os nodes, cria mesh automaticamente, gerencia chaves via Tailscale control plane. ACLs granulares por identidade (não por IP).
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/tls]]
- [[concepts/mtls]]
- [[concepts/pki]]
- [[concepts/cert-manager]]
- [[concepts/wireguard]]
- [[entities/tailscale]]
- [[concepts/ztna]]
- [[concepts/ocsp-stapling]]

## Open Questions

- Certificate Pinning em apps móveis: como fazer rotação de certificados sem forçar app update?
- mTLS com SPIFFE em K8s multicluster — como lidar com diferentes trust domains?
