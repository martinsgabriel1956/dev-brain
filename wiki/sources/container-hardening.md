---
type: source
title: "Container Hardening"
aliases: ["container hardening", "docker security", "distroless", "rootless container", "seccomp", "apparmor", "linux capabilities"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/container-hardening.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [container-hardening, docker-security, distroless, rootless, seccomp, apparmor, linux-capabilities, kubernetes-security]
skill: tech-mentor-security
status: stable
---

## TL;DR

Container Hardening em 4 níveis: (1) Imagens Distroless — sem shell, sem package manager, superfície mínima. (2) Rootless + read-only filesystem — sem root, sem escrita em runtime. (3) Linux Capabilities — DROP ALL, adicionar apenas o necessário. (4) Seccomp profile — bloqueia syscalls não usadas. AppArmor para MAC (Mandatory Access Control). kube-score valida o checklist automaticamente.

## Key Claims

**Claim:** Imagens Distroless eliminam 60-80% das vulnerabilidades de imagem — sem shell = sem escape interativo.
**Evidence:** Alpine com shell: mesmo sem vulnerabilidades conhecidas, um atacante com RCE pode executar `/bin/sh` para pivotar. Distroless (gcr.io/distroless): sem shell, sem package manager, apenas o runtime e a aplicação. Trivy scan: imagem Node.js padrão ~200 CVEs; Distroless ~5-20 CVEs. Multi-stage build copia apenas o artifact final.
**Confidence:** alta

**Claim:** `runAsNonRoot: true` + `readOnlyRootFilesystem: true` são os controles mais impactantes no K8s SecurityContext.
**Evidence:** Container rodando como root com UID 0: se processo for comprometido, o atacante tem root no container (potencialmente root no host com misconfiguration). `runAsUser: 1000` + `runAsNonRoot: true` impede execução como root. `readOnlyRootFilesystem: true` + volumes específicos para escrita: sem persistência de malware em disco.
**Confidence:** alta

**Claim:** `DROP ALL` capabilities + adicionar apenas o necessário é o princípio de least privilege para containers.
**Evidence:** Container padrão Docker herda ~14 capabilities, incluindo `NET_RAW` (ping attacks, MITM), `SYS_PTRACE` (debug de processos). `DROP ALL` + `ADD NET_BIND_SERVICE` (porta < 1024): apenas o mínimo para o processo funcionar. Ataque que explora `NET_RAW` é bloqueado sem impactar a aplicação.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/container-hardening]]
- [[concepts/distroless]]
- [[concepts/linux-capabilities]]
- [[concepts/seccomp]]
- [[concepts/apparmor]]
- [[concepts/kubernetes-security]]

## Open Questions

- Distroless com debug: como fazer troubleshooting em produção sem shell (ephemeral containers)?
- Seccomp profiles gerados automaticamente (OCI Hook) vs manuais — qual tem melhor cobertura sem falsos positivos?
