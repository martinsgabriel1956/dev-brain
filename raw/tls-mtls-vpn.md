---
date: 2026-04-17
tags: [tech-mentor, networking, tls, mtls, vpn, pki, seguranca]
skill: tech-mentor-networking/references/security
level: avançado
---

# TLS/mTLS e VPN

## TLS — Handshake e Certificados

TLS (Transport Layer Security) garante confidencialidade, integridade e autenticidade. Em TLS padrão, apenas o servidor é autenticado. Em mTLS, **ambos** os lados se autenticam com certificado.

### TLS 1.3 Handshake

```
Client                                    Server
  │── ClientHello (ciphers, KeyShare) ──►│
  │                                       │ gera par de chaves
  │◄── ServerHello, Certificate, ─────────│
  │    CertificateVerify, Finished        │
  │                                       │
  │── [verifica cert contra CA] ──────────│
  │── Finished + dados ────────────────►  │
  │◄── dados ─────────────────────────────│
```

**OCSP Stapling:** o servidor inclui a prova de que seu certificado não foi revogado junto ao handshake — evita que o cliente faça uma requisição separada ao OCSP da CA (mais rápido, mais privado).

**Certificate Pinning:** a aplicação só aceita um certificado específico (ou conjunto), mesmo que a CA seja confiável. Usado em apps móveis para prevenir ataques MITM com CA comprometida. Cuidado: dificulta renovação de certificados.

---

## mTLS — Mutual TLS

Em mTLS, ambos cliente e servidor apresentam certificados. O servidor valida o certificado do cliente contra sua CA interna.

```
Client                                    Server
  │── ClientHello ──────────────────────►│
  │◄── ServerHello + ServerCert ──────────│
  │── ClientCert ──────────────────────►  │
  │── [verifica ServerCert] ──────────────│ [verifica ClientCert]
  │── Finished ─────────────────────────►│
  │◄── Finished ──────────────────────────│
  │                                        │
  │◄──── comunicação bidirecional segura ──│
```

### PKI Interna — cert-manager no K8s

```yaml
# cert-manager — emite certificados automaticamente para workloads K8s
apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  name: order-api-cert
  namespace: production
spec:
  secretName: order-api-tls
  duration: 24h         # certificados de curta duração — rotação automática
  renewBefore: 1h
  subject:
    organizations: ["MyCompany"]
  commonName: order-api.production.svc.cluster.local
  dnsNames:
    - order-api.production.svc.cluster.local
    - order-api
  issuerRef:
    name: internal-ca
    kind: ClusterIssuer

---
# ClusterIssuer usando Vault como CA
apiVersion: cert-manager.io/v1
kind: ClusterIssuer
metadata:
  name: internal-ca
spec:
  vault:
    path: pki/sign/internal-services
    server: https://vault.internal:8200
    auth:
      kubernetes:
        role: cert-manager
        mountPath: /v1/auth/kubernetes
```

```typescript
// Aplicação Node.js com mTLS
import { createServer, createConnection } from "tls";
import { readFileSync } from "fs";

// Server — exige certificado do cliente
const server = createServer({
  cert: readFileSync("/etc/certs/tls.crt"),
  key: readFileSync("/etc/certs/tls.key"),
  ca: readFileSync("/etc/certs/ca.crt"),
  requestCert: true,   // solicita cert do cliente
  rejectUnauthorized: true  // rejeita se não apresentar cert válido
}, socket => {
  const peerCert = socket.getPeerCertificate();
  console.log({ message: "Client authenticated", cn: peerCert.subject.CN });
});

// Client — apresenta certificado próprio
const client = createConnection({
  host: "order-api.production.svc.cluster.local",
  port: 443,
  cert: readFileSync("/etc/certs/client.crt"),
  key: readFileSync("/etc/certs/client.key"),
  ca: readFileSync("/etc/certs/ca.crt")
});
```

---

## VPN — WireGuard, Tailscale e ZTNA

### WireGuard

Protocolo moderno de VPN — ~4000 linhas de código vs ~100k do OpenVPN. Mais rápido, mais seguro, mais simples de auditar.

```ini
# /etc/wireguard/wg0.conf (servidor)
[Interface]
Address = 10.0.0.1/24
ListenPort = 51820
PrivateKey = <server_private_key>
PostUp = iptables -A FORWARD -i wg0 -j ACCEPT; iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
PostDown = iptables -D FORWARD -i wg0 -j ACCEPT; iptables -t nat -D POSTROUTING -o eth0 -j MASQUERADE

[Peer]
PublicKey = <client_public_key>
AllowedIPs = 10.0.0.2/32
```

### Tailscale — Mesh VPN Zero-Config

Tailscale usa WireGuard sob o capô mas adiciona:
- **Plano de controle:** chaves gerenciadas pelo Tailscale (ou self-hosted com Headscale)
- **NAT Traversal:** peers se conectam diretamente mesmo atrás de NAT
- **ACLs:** controle de acesso entre peers via policy declarativa

```json
// tailscale-acl.json — quem pode acessar o quê
{
  "acls": [
    { "action": "accept", "src": ["group:dev"], "dst": ["tag:staging:*"] },
    { "action": "accept", "src": ["group:ops"], "dst": ["tag:production:22,443"] },
    { "action": "accept", "src": ["tag:ci"], "dst": ["tag:registry:443"] }
  ]
}
```

### ZTNA vs. VPN Tradicional

| Aspecto | VPN Tradicional | ZTNA |
|---|---|---|
| Modelo | "Dentro da rede = confiável" | "Nunca confiar, sempre verificar" |
| Acesso | Acesso à rede inteira | Acesso a recursos específicos |
| Lateral movement | Possível após comprometimento | Bloqueado por micro-segmentação |
| Exemplos | OpenVPN, WireGuard | Tailscale + ACLs, Cloudflare Access, BeyondCorp |

## Conceitos Relacionados
[[zero-trust]] · [[service-mesh]] · [[k8s-networking]] · [[identidade-avancada]] · [[http-tcp-quic]]

---
*Fonte: tech-mentor skill · tech-mentor-networking · 2026-04-17*
