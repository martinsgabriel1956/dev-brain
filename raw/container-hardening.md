---
date: 2026-04-01
tags: [tech-mentor, security, container, docker, distroless, seccomp, apparmor, rootless, capabilities]
skill: tech-mentor-security/references/container-hardening
level: intermediário
---

# Container Hardening

## Contexto

Um container padrão tem shell, curl, apt e roda como root. Se comprometido, o atacante tem tudo que precisa para explorar o sistema. Container hardening aplica o princípio do menor privilégio em múltiplas camadas — cada camada reduz o blast radius de um eventual comprometimento.

## Como Funciona

Quatro camadas progressivas:

```
1. Imagem distroless    → remove ferramentas do atacante
2. Rootless + read-only → sem root, sem escrita no FS
3. Capabilities drop    → remove privilégios desnecessários do kernel
4. Seccomp / AppArmor  → filtra syscalls e acesso a recursos
```

## Código de Referência

### Nível 1 — Imagens Distroless

```dockerfile
# ❌ Problemático — bash, curl, wget, apt, ~1GB, roda como root
FROM python:3.12
CMD ["python", "main.py"]

# ✅ Multi-stage + Distroless — ~50MB, zero ferramentas para o atacante
FROM python:3.12-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --prefix=/install -r requirements.txt

FROM gcr.io/distroless/python3-debian12
COPY --from=builder /install /usr/local
COPY --from=builder /app .
USER nonroot  # UID 65532
CMD ["main.py"]
```

**Node.js distroless:**
```dockerfile
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json .
RUN npm ci --only=production
COPY . .

FROM gcr.io/distroless/nodejs20-debian12
WORKDIR /app
COPY --from=builder /app .
USER nonroot
CMD ["server.js"]
```

**Go — imagem scratch (zero SO):**
```dockerfile
FROM golang:1.22 AS builder
RUN CGO_ENABLED=0 GOOS=linux go build -o server .

FROM scratch  # imagem vazia — ZERO arquivos do sistema
COPY --from=builder /app/server /server
COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
USER 65532:65532
ENTRYPOINT ["/server"]
# ~10MB, zero superfície de ataque
```

### Nível 2 — Rootless + Read-only Filesystem

```yaml
# Pod spec completo hardened
apiVersion: v1
kind: Pod
spec:
  securityContext:
    runAsNonRoot: true
    runAsUser: 1001
    runAsGroup: 1001
    fsGroup: 1001
    seccompProfile:
      type: RuntimeDefault
  containers:
    - name: app
      image: gcr.io/distroless/nodejs20-debian12
      securityContext:
        allowPrivilegeEscalation: false
        readOnlyRootFilesystem: true
        capabilities:
          drop: [ALL]
          add: [NET_BIND_SERVICE]  # apenas se precisar porta < 1024
      resources:
        limits:
          cpu: "500m"
          memory: "256Mi"
        requests:
          cpu: "100m"
          memory: "128Mi"
      volumeMounts:
        - name: tmp
          mountPath: /tmp  # exceção para escrita se necessário
  volumes:
    - name: tmp
      emptyDir: {}
```

### Nível 3 — Linux Capabilities

```
# Capabilities comuns:
# CAP_NET_BIND_SERVICE: bind em porta < 1024 — manter apenas se precisar
# CAP_SYS_ADMIN:        operações administrativas — SEMPRE remover
# CAP_NET_RAW:          raw sockets (sniffing) — remover em produção
# CAP_SETUID/SETGID:    mudar UID/GID — remover se não precisar
```

```yaml
securityContext:
  capabilities:
    drop: [ALL]                  # remove todas
    add: [NET_BIND_SERVICE]      # adiciona apenas o necessário
```

### Nível 4 — Seccomp

Filtra syscalls que um processo pode fazer. Bloqueia chamadas de sistema desnecessárias.

```yaml
# Mínimo recomendado — perfil padrão do runtime
securityContext:
  seccompProfile:
    type: RuntimeDefault

# Perfil customizado — allowlist explícita para web server
# seccomp-profile.json
{
  "defaultAction": "SCMP_ACT_ERRNO",
  "syscalls": [{
    "names": ["accept4", "bind", "connect", "read", "write", "epoll_wait", ...],
    "action": "SCMP_ACT_ALLOW"
  }]
}
```

### AppArmor — Mandatory Access Control

```
profile docker-nginx {
  network inet tcp,
  deny network raw,        # sem raw sockets
  deny /etc/passwd r,      # não lê /etc/passwd
  deny /etc/shadow r,
  /var/log/nginx/** w,
  /etc/nginx/** r,
}
```

### Checklist de Hardening (validar com kube-score)

```yaml
spec:
  securityContext:
    runAsNonRoot: true              # ✅ não-root
    seccompProfile:
      type: RuntimeDefault          # ✅ seccomp
  containers:
    - image: gcr.io/distroless/...  # ✅ distroless
      securityContext:
        allowPrivilegeEscalation: false  # ✅
        readOnlyRootFilesystem: true     # ✅
        capabilities:
          drop: [ALL]                    # ✅
      resources:
        limits:                          # ✅ sem limits = DoS potencial
          cpu: "500m"
          memory: "256Mi"
```

```bash
# Validar
kube-score score deployment.yaml
checkov -f deployment.yaml --check CKV_K8S_6,CKV_K8S_28,CKV_K8S_30
kube-bench run --targets node
```

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---|---|---|
| Distroless | Superfície de ataque mínima | Debugging em prod difícil — sem shell |
| Read-only FS | Previne escrita de malware | App precisa de volumes para dirs writable |
| Seccomp custom | Bloqueia syscalls desnecessárias | Perfil errado quebra a aplicação |
| Capabilities drop ALL | Sem privilégios desnecessários | Algumas libs esperam capabilities implícitas |

## Quando Usar / Quando Evitar

**Sempre aplique:** `runAsNonRoot`, `allowPrivilegeEscalation: false`, `drop: [ALL]`, resource limits. Custo zero, impacto imediato.

**Distroless:** obrigatório em produção para serviços voltados à internet. Em jobs internos de baixo risco pode usar alpine.

**Seccomp customizado:** vale o investimento para serviços críticos (pagamentos, autenticação). Para o restante, `RuntimeDefault` é suficiente.

## Conceitos Relacionados

[[kubernetes-security]] · [[runtime-security]] · [[supply-chain-security]] · [[devsecops-pipeline]] · [[secure-design-patterns]]

---
*Fonte: tech-mentor skill · tech-mentor-security · 2026-04-01*
