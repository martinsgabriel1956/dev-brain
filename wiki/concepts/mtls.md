---
type: concept
title: "mTLS — Mutual TLS"
aliases: ["mtls", "mutual tls", "tls mútuo", "spiffe"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [seguranca, service-mesh, kubernetes, criptografia, zero-trust]
skill: tech-mentor-system-design
status: stable
---

# mTLS — Mutual TLS

TLS onde tanto o cliente quanto o servidor apresentam certificados para autenticação mútua. No contexto de [[concepts/service-mesh]], ativado automaticamente entre todos os serviços sem alterar código da aplicação.

## Com Istio

Cada serviço recebe um certificado SPIFFE (identidade criptográfica baseada em Kubernetes Service Account). mTLS automático entre todos os pods do mesh.

```yaml
# PeerAuthentication — modo mTLS por namespace
apiVersion: security.istio.io/v1beta1
kind: PeerAuthentication
metadata:
  name: default
  namespace: checkout
spec:
  mtls:
    mode: STRICT      # rejeita plaintext — apenas mTLS permitido
    # PERMISSIVE: aceita ambos (útil durante migração gradual)
    # DISABLE: sem mTLS
```

## AuthorizationPolicy — Controle de Acesso

Mesmo que um pod seja comprometido, não consegue chamar serviços para os quais não tem permissão — mesmo dentro do cluster:

```yaml
apiVersion: security.istio.io/v1beta1
kind: AuthorizationPolicy
metadata:
  name: checkout-policy
  namespace: checkout
spec:
  selector:
    matchLabels:
      app: checkout-api
  action: ALLOW
  rules:
    - from:
        - source:
            principals:
              - "cluster.local/ns/frontend/sa/frontend-service"
              - "cluster.local/ns/orders/sa/order-service"
      to:
        - operation:
            methods: ["GET", "POST"]
            paths: ["/api/*"]
```

## Zero Trust

mTLS + AuthorizationPolicy implementa Zero Trust dentro do cluster: nenhum serviço é implicitamente confiável apenas por estar na mesma rede.

## Key Sources

- [[sources/service-mesh]]
