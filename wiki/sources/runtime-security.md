---
type: source
title: "Runtime Security"
aliases: ["runtime security", "falco", "ebpf", "sysdig", "container escape", "threat detection runtime"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/runtime-security.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [runtime-security, falco, ebpf, sysdig, container-escape, threat-detection, syscall-monitoring]
skill: tech-mentor-security
status: stable
---

## TL;DR

Runtime Security monitora comportamento em produção via syscalls — detecta o que scanning estático não vê (exploits zero-day, comportamento anômalo pós-compromise). Falco: engine de regras sobre syscalls via eBPF. eBPF é superior ao kernel module — sem risco de crash do kernel, menor overhead. Falco Sidekick roteia alertas para Slack/PagerDuty/Kafka/SIEM. Resposta automática: isolar pod, revogar credencial.

## Key Claims

**Claim:** Runtime Security detecta ataques que scanning estático não detecta — comportamento anômalo pós-compromise.
**Evidence:** SAST/SCA: detecta vulnerabilidades conhecidas no código. Runtime: detecta quando um processo normal começa a fazer coisas anormais. "Container nginx executando `bash`", "processo abrindo `/etc/passwd`", "conexão de saída para IP externo não esperado" — padrões de post-exploitation que só aparecem em runtime, não na imagem.
**Confidence:** alta

**Claim:** eBPF é superior ao kernel module para runtime security — sem risco de crash do kernel.
**Evidence:** Kernel module: código executa no kernel space. Bug no módulo = kernel panic = node inteiro derrubado. eBPF: programa verificado pelo verifier do kernel antes de executar, sandbox. Se tiver bug: falha graciosamente sem afetar o kernel. Falco com eBPF: overhead < 2% de CPU vs kernel module com mesmo overhead porém com risco.
**Confidence:** alta

**Claim:** Falco Sidekick + resposta automática transforma detecção em contenção — pod isolado em segundos.
**Evidence:** Regra Falco: "processo spawna shell em container de produção" → Falco Sidekick → Lambda/Function → `kubectl label pod compromised=true` + NetworkPolicy bloqueia todo tráfego do pod + credenciais rotacionadas + PagerDuty alert. Sem intervenção humana para contenção inicial. Investigação posterior com pod isolado.
**Confidence:** alta

## Entities & Concepts Touched

- [[entities/falco]]
- [[concepts/ebpf]]
- [[concepts/runtime-security]]
- [[concepts/syscall-monitoring]]
- [[entities/falco-sidekick]]
- [[concepts/container-escape]]

## Open Questions

- Falco em clusters Kubernetes de alta densidade — como tunar regras para reduzir noise sem perder cobertura real?
- Runtime security para serverless (Lambda, Cloud Functions) — como monitorar syscalls em ambiente efêmero sem agente persistente?
