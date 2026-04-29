---
type: source
title: "Kubernetes Security"
aliases: ["kubernetes security", "k8s security", "pod security standards", "rbac kubernetes", "network policy k8s", "falco", "opa gatekeeper", "kube-bench"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/kubernetes-security.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [kubernetes-security, pod-security-standards, rbac, network-policy, falco, opa-gatekeeper, kube-bench, cis-benchmark]
skill: tech-mentor-security
status: stable
---

## TL;DR

K8s Security em 5 camadas: CIS Benchmark (kube-bench), Pod Security Standards (restricted namespace), RBAC mínimo (sem cluster-admin para aplicações), Network Policies (default deny-all), Audit Logging. OPA Gatekeeper para policies além do PSS. Falco para runtime threat detection. Verificar: nenhuma aplicação deve rodar com ServiceAccount que tem `cluster-admin`.

## Key Claims

**Claim:** Network Policy default deny-all é o zero trust intra-cluster — sem ela, qualquer pod pode falar com qualquer pod.
**Evidence:** K8s por padrão: sem NetworkPolicy = sem restrição. Pod comprometido pode fazer lateral movement para qualquer serviço no cluster. `default-deny-all` NetworkPolicy no namespace + liberar apenas o necessário (ingress do ingress controller, egress para banco e redis). Cilium para NetworkPolicy com visibilidade L7.
**Confidence:** alta

**Claim:** RBAC mínimo: nenhuma aplicação deve ter `cluster-admin` — ServiceAccount com permissões específicas ao namespace.
**Evidence:** `cluster-admin` ClusterRoleBinding para ServiceAccount de uma aplicação: se o pod for comprometido, atacante tem controle total do cluster. Correto: ServiceAccount com Role (não ClusterRole) no próprio namespace, com permissões apenas para os recursos necessários (ex: `get, list` em `pods` do próprio namespace).
**Confidence:** alta

**Claim:** Pod Security Standards (PSS) `restricted` é o baseline de segurança para workloads de produção.
**Evidence:** PSS `restricted`: sem `runAsRoot`, `readOnlyRootFilesystem: true`, sem `privileged`, seccomp `RuntimeDefault`. Aplica por namespace com label `pod-security.kubernetes.io/enforce: restricted`. Pods que violam são rejeitados na admission. CIS Benchmark (kube-bench) valida a configuração do cluster.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/kubernetes-security]]
- [[concepts/pod-security-standards]]
- [[concepts/rbac]]
- [[concepts/network-policy]]
- [[entities/falco]]
- [[entities/opa-gatekeeper]]
- [[entities/kube-bench]]
- [[concepts/zero-trust]]

## Open Questions

- Falco em produção com alto volume de syscalls — como filtrar alertas relevantes sem falsos positivos excessivos?
- OPA Gatekeeper vs Kyverno — qual tem melhor DX para times sem expertise em Rego?
