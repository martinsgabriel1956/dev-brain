---
date: 2026-04-01
tags: [tech-mentor, security, runtime, falco, ebpf, sysdig, container-escape, siem]
skill: tech-mentor-security/references/runtime-security
level: avançado
---

# Runtime Security

## Contexto

SAST e image scanning encontram vulnerabilidades **conhecidas** antes do deploy. Runtime security detecta **exploits ativos** em produção — quando um container já está comprometido e o atacante está se movendo.

Um container executando `curl | bash`, lendo `/etc/shadow` ou acessando `169.254.169.254` (metadata AWS) é detectável em milissegundos via monitoramento de syscalls.

eBPF tornou isso viável com overhead < 3% de CPU — antes era inviável em produção.

## Como Funciona

```
Kernel (eBPF probe)
  ↓ syscalls capturadas em tempo real
Falco Engine (avalia regras em microsegundos)
  ↓ alerta gerado
Falco Sidekick → Slack, PagerDuty, Kafka, Elasticsearch, SIEM
  ↓ (opcional)
Resposta automática: isolar pod, revogar credenciais, abrir incident
```

## Código de Referência

### Instalação do Falco

```bash
helm repo add falcosecurity https://falcosecurity.github.io/charts
helm install falco falcosecurity/falco \
  --namespace falco \
  --create-namespace \
  --set driver.kind=ebpf \
  --set falcosidekick.enabled=true \
  --set falcosidekick.config.slack.webhookurl="https://hooks.slack.com/..."
```

### Regras Customizadas

```yaml
# Shell em container de produção — sempre suspeito
- rule: Shell in Production Container
  condition: >
    container and
    proc.name in (bash, sh, ash, zsh) and
    k8s.ns.name in (payments, orders)
  output: >
    Shell em container (user=%user.name container=%container.name
    pod=%k8s.pod.name cmd=%proc.cmdline)
  priority: WARNING

# Acesso ao metadata AWS — SSRF ou credential theft
- rule: Access AWS Instance Metadata
  condition: >
    outbound and
    fd.sip = "169.254.169.254" and
    container
  output: >
    Container acessando metadata AWS
    (container=%container.name cmd=%proc.cmdline)
  priority: CRITICAL

# Leitura de arquivos sensíveis
- rule: Read Sensitive Files
  condition: >
    open_read and container and
    fd.name in (/etc/shadow, /etc/passwd, /root/.ssh/id_rsa, /proc/1/mem)
  output: "Leitura de arquivo sensível (file=%fd.name proc=%proc.cmdline)"
  priority: CRITICAL

# Container escape — namespace manipulation
- rule: Container Namespace Change
  condition: >
    evt.type in (setns, unshare) and container
  output: "Namespace change em container (proc=%proc.name)"
  priority: CRITICAL

# Processo inesperado fazendo conexão de rede
- rule: Unexpected Outbound Connection
  condition: >
    outbound and container and
    not proc.name in (node, python, java) and
    not fd.sport in (80, 443, 5432, 6379)
  output: >
    Conexão inesperada (container=%container.name port=%fd.sport proc=%proc.cmdline)
  priority: WARNING

# Escrita em diretório de binários — possível backdoor
- rule: Write to Binary Directory
  condition: >
    open_write and bin_dir and container
  output: "Escrita em diretório de binários (file=%fd.name proc=%proc.cmdline)"
  priority: ERROR
```

### Roteamento de Alertas (Falco Sidekick)

```yaml
# falcosidekick config
slack:
  webhookurl: "https://hooks.slack.com/services/..."
  minimumpriority: "warning"

pagerduty:
  routingkey: "your-routing-key"
  minimumpriority: "critical"

elasticsearch:
  hostport: "http://elasticsearch:9200"
  index: "falco-events"
  minimumpriority: "notice"

kafka:
  brokers: "kafka:9092"
  topic: "security-events"
  minimumpriority: "warning"
```

### Resposta Automática a Incidentes

```python
# Kafka → SIEM com isolamento automático de pod comprometido
from kafka import KafkaConsumer
import json

consumer = KafkaConsumer("security-events", bootstrap_servers=["kafka:9092"])

for msg in consumer:
    event = json.loads(msg.value)
    siem_client.index(event)

    if event.get("priority") == "CRITICAL":
        pod_name = event["output_fields"].get("k8s.pod.name")
        # Isola o pod removendo do LB — NÃO matar para preservar evidências forenses
        k8s_client.label_pod(pod_name, labels={
            "security-incident": "true",
            "remove-from-lb": "true"
        })
        pagerduty.trigger_incident(event)
```

## eBPF — Por que é Superior

| Abordagem | Overhead CPU | Cobertura | Bypass possível |
|---|---|---|---|
| ptrace (strace) | > 50% | Total | Não |
| Kernel module | Baixo | Total | Difícil |
| **eBPF** | **< 3%** | **Total** | **Difícil** |
| Sidecar proxy | Médio | Rede apenas | Sim (syscall direto) |
| Userspace interceptor | Alto | Parcial | Sim |

**O que eBPF monitora:**
- Syscalls (open, execve, connect, write, etc.)
- Atividade de rede (pacotes, conexões, DNS)
- Operações de filesystem
- Criação/destruição de processos
- Mudanças de capability e privilege escalation

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---|---|---|
| Falco | Detecção de exploits ativos em ms | Ruído de alertas sem tuning de regras |
| eBPF | Overhead < 3%, difícil de bypassar | Requer kernel >= 4.14 |
| Resposta automática | Contenção rápida sem intervenção humana | Falso positivo pode isolar pod legítimo |
| Audit de syscalls | Visibilidade total do que acontece | Volume de eventos é massivo |

## Quando Usar / Quando Evitar

**Use quando:**
- Workloads sensíveis em produção (pagamentos, autenticação, dados de usuário)
- Compliance exige detecção de intrusão em runtime (PCI-DSS, SOC 2, FedRAMP)
- Ambiente multi-tenant onde um tenant comprometido pode afetar outros

**Comece com as regras padrão do Falco** — já cobrem os casos mais comuns. Adicione regras customizadas conforme você aprende os padrões normais do seu ambiente. Regras muito agressivas sem tuning geram fadiga de alertas.

## Conceitos Relacionados

[[kubernetes-security]] · [[container-hardening]] · [[incident-response]] · [[cloud-security]] · [[threat-modeling]]

---
*Fonte: tech-mentor skill · tech-mentor-security · 2026-04-01*
