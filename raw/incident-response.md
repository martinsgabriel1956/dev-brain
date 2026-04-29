---
date: 2026-04-23
tags: [tech-mentor, security, incident-response, forensics, siem, soar]
skill: tech-mentor-security/references/incident-response
level: avançado
---

# Incident Response

## Contexto

Breaches são inevitáveis — a questão é quanto tempo leva para detectar e conter. MTTD (Mean Time to Detect) e MTTR (Mean Time to Respond) são as métricas que definem o impacto de um incidente. A diferença entre um incidente contido em horas e uma violação catastrófica está na qualidade do processo e da preparação.

IR não é só processo de segurança — é uma capacidade que envolve times de eng, legal, comunicação e C-level. Planejar durante o incidente é tarde demais.

## Como Funciona

### Fases do Incident Response (NIST SP 800-61)

```
1. Preparação
   ↓
2. Detecção & Análise
   ↓
3. Contenção, Erradicação & Recuperação
   ↓
4. Atividade Pós-Incidente (Post-Mortem)
```

### Fase 1 — Preparação

```
O que ter pronto ANTES de qualquer incidente:

Playbooks por tipo de incidente:
  - Ransomware
  - Data breach (PII exposta)
  - Account takeover em escala
  - Credential leak no repositório
  - Comprometimento de supply chain
  - DDoS

Runbook mínimo para cada playbook:
  1. Quem notificar (escalation path)
  2. Como isolar o sistema afetado
  3. Como preservar evidências
  4. Como se comunicar (internamente + externamente)
  5. Critérios para resolver o incidente

Ferramentas com acesso testado:
  - SIEM (Splunk, Elastic SIEM, Sentinel)
  - Canais de comunicação backup (incidente pode afetar Slack)
  - Acesso read-only a logs de prod sem comprometer chaves
  - Contatos de resposta: legal, PR, ANPD/DPA, seguros
```

### Fase 2 — Detecção & Análise

**Fontes de detecção:**
```
Internas:  SIEM alerts, anomaly detection, IDS/IPS
Externas:  bug bounty reports, threat intel, notificação de parceiro, usuário afetado
Proativas: threat hunting, pentest findings
```

**Triagem — classificar o incidente:**
```
Severidade:
  P1 Critical: dados de usuários comprometidos, sistema de pagamento afetado,
               ransomware ativo, acesso não autorizado a dados sensíveis
  P2 High:     tentativa de acesso detectada sem sucesso confirmado,
               vulnerabilidade crítica explorada sem impacto confirmado
  P3 Medium:   anomalia de comportamento sem evidência de comprometimento
  P4 Low:      scan de vulnerabilidade, brute force bloqueado

SLA de resposta:
  P1: acknowledge 15min, contenção 1h
  P2: acknowledge 1h, contenção 4h
  P3: acknowledge 4h, análise 24h
  P4: análise 72h
```

**Indicators of Compromise (IOC):**
```
Network:
  - IPs incomuns em logs de acesso
  - DNS queries para domínios suspeitos
  - Exfiltração: volume incomum de dados saindo
  - Conexões em horários fora do padrão

Host:
  - Processos desconhecidos rodando
  - Arquivos criados em locais incomuns (/tmp, /var)
  - Modificações em arquivos de sistema
  - Usuários criados sem autorização
  - Cron jobs adicionados

Application:
  - Logins de IPs/países não usuais
  - Picos de erro 4xx/5xx fora do normal
  - Queries de banco incomuns (volume, padrão)
  - Escalação de privilégios não autorizada
```

### Fase 3 — Contenção, Erradicação & Recuperação

```
Contenção (PRIMEIRO — limitar dano adicional):
  1. Isolar sistema afetado (sem desligar — preservar evidências em memória)
  2. Revogar credenciais comprometidas
  3. Bloquear IPs/contas do atacante
  4. Habilitar logging adicional no perímetro

Preservação de evidências (ANTES de remediar):
  - Capturar memória do sistema (dump)
  - Snapshot de disco antes de qualquer modificação
  - Exportar logs relevantes para storage imutável
  - Registrar timeline com timestamps

Erradicação:
  - Identificar root cause (não só os sintomas)
  - Remover malware / backdoors
  - Patchear a vulnerabilidade explorada
  - Verificar outros sistemas com mesmo vetor

Recuperação:
  - Restaurar de backup limpo (não do sistema comprometido)
  - Verificar integridade dos dados restaurados
  - Monitorar intensivamente por 72h após retorno
  - Comunicar stakeholders sobre retorno ao normal
```

### Forensics Digital — Fundamentos

```bash
# Capturar memória RAM (Linux) — ANTES de desligar
sudo avml /tmp/memory.lime

# Preservar disco sem modificar
sudo dd if=/dev/sda of=/mnt/evidence/disk.img bs=4M status=progress
sha256sum /mnt/evidence/disk.img > disk.img.sha256  # hash para evidência

# Timeline de acesso a arquivos
sudo find / -newer /var/log/auth.log -type f 2>/dev/null | sort

# Verificar processos ocultos
ps auxf
ls -la /proc/*/exe 2>/dev/null | grep -v "Permission denied"

# Conexões de rede ativas
ss -tunapm
netstat -tulpn

# Usuários logados e comandos recentes
who
last | head -20
cat /root/.bash_history
```

### SIEM — Correlação de Eventos

```
SIEM (Security Information and Event Management) centraliza logs e correlaciona eventos
para detectar padrões de ataque que seriam invisíveis em logs individuais.

Fontes de log para ingerir:
  - Firewall / WAF
  - DNS resolver
  - IAM / SSO (logins, mudanças de permissão)
  - CloudTrail / audit log cloud
  - Kubernetes audit log
  - Application logs (estruturados)
  - Endpoint (EDR: CrowdStrike, SentinelOne)

Regras de correlação exemplo:
  - Login de novo país + mudança de senha em 1h → ALERT
  - 10+ downloads de arquivos S3 sensíveis em 5min → ALERT
  - Processo em container com conexão de rede inesperada → ALERT
  - Criação de usuário IAM fora do horário comercial → ALERT
```

### SOAR — Automação de Resposta

```python
# SOAR playbook — resposta automática a credential stuffing
# (Pseudocódigo de plataformas como Palo Alto XSOAR, Splunk SOAR)

def handle_credential_stuffing(alert):
  ip = alert["source_ip"]
  affected_users = alert["affected_accounts"]

  # 1. Enriquecer IOC
  ip_reputation = virustotal.check_ip(ip)
  is_known_bad = ip_reputation["malicious_votes"] > 10

  # 2. Contenção automática se alta confiança
  if is_known_bad and len(affected_users) > 10:
    waf.block_ip(ip, duration_hours=24)
    slack.alert(channel="#security-incidents",
                message=f"IP {ip} bloqueado automaticamente: credential stuffing")

  # 3. Para usuários afetados — forçar re-auth
  for user in affected_users:
    if user["login_successful"]:
      auth_service.invalidate_sessions(user["id"])
      email.send_security_alert(user["email"])

  # 4. Criar ticket para análise humana
  jira.create_ticket(
    project="SEC",
    summary=f"Credential stuffing de {ip}",
    description=alert["details"],
    priority="High" if is_known_bad else "Medium"
  )
```

### Comunicação Durante Incidente

```
Interna (imediata):
  - Security team → Engineering lead → CTO
  - Usar canal de comunicação fora da infra comprometida (Signal, phone)
  - Status updates a cada 30min durante P1

Externa (quando necessário):
  - Usuários afetados: notificar o mais rápido possível (requisito LGPD/GDPR: 72h)
  - ANPD/DPA: incidentes com PII (LGPD art. 48)
  - Reguladores específicos (BACEN para fintechs, ANS para saúde)
  - Mídia: apenas via PR, nunca eng team direto

Template de notificação a usuários:
  "Identificamos um incidente de segurança em [data] que pode ter afetado [dados].
   Tomamos as seguintes ações: [ações].
   O que você deve fazer: [ações do usuário].
   Contato para dúvidas: [canal]."
```

### Post-Mortem

```markdown
## Incident Post-Mortem — [Nome do Incidente] — [Data]

**Duração:** [início] → [resolução] ([duração total])
**Severidade:** P1/P2/P3
**Impacto:** [usuários afetados, dados expostos, downtime]

## Timeline
| Horário | Evento |
|---|---|
| 14:23 | Alert disparado no SIEM |
| 14:31 | On-call notificado |
| 14:45 | Root cause identificado |
| 15:10 | Contenção aplicada |
| 16:30 | Serviço restaurado |

## Root Cause
[Uma frase descrevendo a causa raiz — sem culpar pessoas]

## Contributing Factors
- [fator 1]
- [fator 2]

## O Que Funcionou Bem
## O Que Pode Melhorar

## Action Items
| Ação | Responsável | Prazo |
|---|---|---|
| Adicionar rate limiting em /api/login | @eng | 2026-04-30 |
| Criar alerta para X padrão no SIEM | @security | 2026-05-07 |
```

**Regra fundamental de post-mortem: blameless.** O objetivo é aprender, não punir. Processos e sistemas falham — a pergunta é por que o sistema permitiu a falha, não quem a cometeu.

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---|---|---|
| SOAR automação | Resposta em segundos, 24/7 | Falsos positivos podem bloquear legítimos |
| Isolamento imediato | Contém dano | Pode causar outage de serviço |
| Preservar antes de remediar | Evidências para investigação | Prolonga exposição se demorar |
| Notificação proativa de usuários | Trust, compliance | Pode gerar pressão desnecessária se incidente for contido |

## Quando Usar / Quando Evitar

**Playbooks:** todo produto em produção com dados de usuários deve ter pelo menos playbook de data breach e credential stuffing. Simular (tabletop exercise) a cada 6 meses.

**SIEM:** obrigatório para compliance (SOC 2, PCI-DSS). Necessário quando o volume de logs torna análise manual impossível.

**SOAR:** quando o SIEM já gera alertas bem calibrados (baixo false positive rate). Automação sobre alertas ruins é pior que nada.

## Conceitos Relacionados

[[observabilidade]] · [[distributed-tracing]] · [[sre-error-budget-incidents]] · [[pentest-redteam]] · [[compliance-soc2-pci]] · [[cloud-security]]

---
*Fonte: tech-mentor skill · tech-mentor-security · 2026-04-23*
