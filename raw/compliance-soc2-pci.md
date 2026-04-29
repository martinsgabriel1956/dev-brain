---
date: 2026-04-01
tags: [tech-mentor, security, compliance, soc2, pci-dss, iso27001, audit-logging, evidence]
skill: tech-mentor-security/references/compliance-audit
level: intermediário
---

# Compliance — SOC 2, PCI-DSS, ISO 27001

## Contexto

Clientes enterprise exigem SOC 2. Fintechs que tocam dados de cartão precisam de PCI-DSS. ISO 27001 é exigida em contratos com governo e grandes corporações. Compliance não é só política — tem implicações diretas em como você constrói e opera sistemas: logging, controle de acesso, gestão de mudanças, continuidade.

O princípio central: **evidência deve ser gerada automaticamente pelo processo normal de trabalho**, não coletada manualmente antes da auditoria.

## SOC 2

Certifica que você tem controles adequados nos **Trust Service Criteria**: Security, Availability, Processing Integrity, Confidentiality, Privacy.

**Type I** → controles existem em uma data (foto). Mais rápido, 3-6 meses.
**Type II** → controles operaram efetivamente por 6-12 meses (filme). **Enterprise sempre exige Type II.**

### O Que Implementar Tecnicamente

```
Controles de Acesso (CC6 — mais cobrado):
  ✅ MFA para todos os acessos a produção
  ✅ SSO com provisionamento/desprovisionamento automático
  ✅ Access review trimestral documentado
  ✅ Least privilege revisado e documentado

Monitoramento (CC7):
  ✅ Logs centralizados com retenção mínima de 12 meses
  ✅ Alertas para acessos não autorizados e anomalias
  ✅ Incident response playbook documentado e testado

Gestão de Mudanças:
  ✅ Todas as mudanças em produção via CI/CD — sem acesso direto
  ✅ Code review obrigatório (não pode fazer merge do próprio PR)
  ✅ Change management tickets linkados a deploys

Continuidade (A7):
  ✅ Backup testado mensalmente (restore, não só backup)
  ✅ DR documentado e testado com resultado registrado
  ✅ RTO e RPO definidos e alcançados
```

### Evidências Técnicas por Controle

```
CC6 — Acesso:
  Screenshot do IdP com MFA enforced + lista de usuários com MFA ativo
  Log de access reviews + prova de offboarding de ex-funcionários

A7 — Availability:
  Uptime reports do período + alertas configurados + runbook de IR
  Resultado do último DR test com RTO/RPO alcançados

CC7 — Incident Response:
  Lista de incidentes com timeline e post-mortem
  Log de investigações de alertas disparados
```

### Evidence Collection Automatizada

```python
# Gerar evidências SOC 2 automaticamente via AWS
def generate_soc2_evidence(period_days=90):
    return {
        'access_reviews':    query_iam_access_advisor(period_days),
        'mfa_enforcement':   check_mfa_policy(),
        'encryption_status': audit_s3_encryption(),
        'patch_compliance':  query_ssm_compliance(period_days),
        'backup_validation': verify_backup_restores(period_days),
    }
```

```sql
-- CloudTrail → Athena: quem acessou dados de produção no período?
SELECT useridentity.arn, eventname, sourceipaddress, eventtime
FROM cloudtrail_logs
WHERE eventsource = 'rds.amazonaws.com'
AND eventtime BETWEEN '2025-01-01' AND '2025-02-01'
ORDER BY eventtime;
```

```yaml
# GitHub Actions — gerar evidência de change management para auditoria
- name: Generate change evidence
  run: |
    gh pr list --state merged \
      --json number,title,mergedAt,reviewDecision,reviews \
      --jq '.[] | select(.reviewDecision == "APPROVED")' \
      > evidence/approved-prs.json
```

**Ferramentas:** Vanta, Drata, Secureframe — automatizam coleta integrando com AWS, GitHub, GSuite.

---

## PCI-DSS

Obrigatório se você processa, armazena ou transmite dados de cartão.

### O Que Nunca Armazenar

```
NUNCA (mesmo criptografado):
  - CVV/CVC (código de segurança)
  - PIN do cartão
  - Track data completo (dados do chip)

PODE armazenar (criptografado, se necessário):
  - PAN — SEMPRE mascarado em logs: 1234 **** **** 5678
  - Nome do portador
  - Data de validade
```

### Tokenização — A Forma Correta

```typescript
// Frontend: número do cartão vai direto para o gateway, nunca para seu servidor
const { token } = await stripe.createToken(cardElement);
// token = "tok_visa_4242" — referência ao cartão, não o cartão em si

// Backend: só vê o token
await stripe.charges.create({
  amount: 2000,
  currency: 'brl',
  source: token,  // servidor nunca viu o número real
});
```

**Escopo PCI com tokenização no frontend:** SAQ A (simples) em vez de SAQ D (complexo) — drasticamente menos controles exigidos.

### Requisitos Técnicos Principais

| Req | O que exige |
|---|---|
| Req 2 | Não use defaults de vendors (senhas padrão, configurações) |
| Req 3 | Criptografia dos dados armazenados + minimização |
| Req 4 | TLS 1.2+ obrigatório, TLS 1.3 recomendado |
| Req 6 | Desenvolvimento seguro: SAST, code review, patch management |
| Req 7 | Controle de acesso por need-to-know |
| Req 8 | MFA obrigatório para acesso admin |
| Req 10 | Log de todos os acessos a dados de cardholders |
| Req 11 | Vulnerability scan trimestral + pentest anual |

---

## ISO 27001

Framework de gestão de segurança da informação. Controles do Annex A mais relevantes para engenharia:

| Controle | O que implementar |
|---|---|
| A.8.2 — Information Classification | Labels em dados (PII, confidential), data catalog |
| A.8.7 — Malware Protection | Container scanning, dependency auditing no CI |
| A.8.15 — Logging | Audit logs imutáveis, retenção mínima 1 ano |
| A.8.24 — Cryptography | TLS 1.2+, chaves gerenciadas via KMS, rotação anual |
| A.8.25 — SDLC seguro | SAST/DAST no pipeline, threat modeling |
| A.8.28 — Secure Coding | Code review obrigatório, OWASP guidelines |
| A.8.32 — Gestão de mudanças | Change management, rollback, aprovações |

**Evidências que auditores pedem:**
- Logs de acesso com retenção ≥ 90 dias
- Relatórios de vulnerability scanning
- Inventário de ativos atualizado (CMDB)
- Incident response plan testado com resultados registrados
- Resultado de penetration testing anual

---

## Audit Logging — Estrutura Universal

```typescript
type AuditEntry = {
  id: string;
  timestamp: Date;
  actorId: string;         // quem fez
  actorType: 'user' | 'system' | 'api_key';
  action: string;          // 'order.cancelled', 'permission.granted', 'data.exported'
  resourceType: string;
  resourceId: string;
  tenantId: string;
  ipAddress: string;
  userAgent: string;
  before?: Record<string, unknown>;  // estado anterior
  after?: Record<string, unknown>;   // estado posterior
};

async function audit(entry: Omit<AuditEntry, 'id' | 'timestamp'>) {
  await db.auditLog.create({
    data: { ...entry, id: randomUUID(), timestamp: new Date() }
  });
}
```

**Imutabilidade no PostgreSQL:**

```sql
-- RLS que bloqueia UPDATE e DELETE
CREATE POLICY audit_immutable ON audit_logs
  FOR UPDATE USING (false)
  FOR DELETE USING (false);
```

**Retenção em camadas:**
```
Logs recentes (30-90 dias) → PostgreSQL — queries rápidas
Logs antigos               → S3 (Parquet) + Athena — barato, consultável
```

---

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---|---|---|
| SOC 2 Type II | Máxima confiança do mercado enterprise | 6-12 meses de operação contínua dos controles |
| Evidence automation | Auditoria não paralisa o time | Setup inicial exige integração com múltiplas ferramentas |
| Tokenização PCI | Escopo PCI drasticamente reduzido | Dependência do gateway para toda cobrança |
| Audit log imutável | Rastreabilidade completa + evidência de compliance | Volume de dados cresce continuamente |

## Quando Usar / Quando Evitar

**SOC 2:** comece quando os primeiros clientes enterprise perguntarem. Type I em 3-6 meses desbloqueou vendas; Type II é o objetivo de médio prazo.

**PCI-DSS:** use tokenização no frontend desde o dia 1 — reduz escopo e complexidade permanentemente. Não tente processar dados de cartão diretamente.

**ISO 27001:** investimento relevante de tempo e dinheiro. Vale quando o mercado-alvo exige (governo, financeiro, saúde, grandes corporações).

## Conceitos Relacionados

[[data-privacy]] · [[devsecops-pipeline]] · [[secret-scanning]] · [[cloud-security]] · [[autenticacao-segura]] · [[audit-logging]]

---
*Fonte: tech-mentor skill · tech-mentor-security · 2026-04-01*
