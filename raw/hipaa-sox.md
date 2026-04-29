---
date: 2026-04-01
tags: [tech-mentor, security, compliance, hipaa, sox, phi, audit-trail, change-management, segregation-of-duties]
skill: tech-mentor-security/references/hipaa-engineering
level: avançado
---

# HIPAA & SOX

## Contexto

**HIPAA** (EUA, 1996): qualquer sistema que processe, armazene ou transmita PHI (dados de saúde) precisa ser compliant. Impacta EHR/EMR, telemedicina, apps de saúde, plataformas de seguros.

**SOX** (EUA, 2002): empresas públicas ou em processo de IPO precisam de controles auditáveis em sistemas financeiros. Para engenharia: change management, segregação de funções e audit trails imutáveis.

Ambos têm implicações diretas de arquitetura — não são só políticas.

---

# HIPAA

## O Que é PHI

```
PHI = qualquer informação que identifique um indivíduo E esteja relacionada a:
  - Condição de saúde física ou mental
  - Prestação de cuidados de saúde
  - Pagamento por cuidados de saúde

Os 18 identificadores HIPAA (Safe Harbor):
  Nome, localização geográfica, datas (nascimento, admissão, alta),
  telefone, fax, email, SSN/CPF, número de prontuário, número do plano de saúde,
  número de conta, número de certificado/licença, VIN, URL, IP, biometria,
  foto de rosto, número de dispositivo, qualquer outro identificador único
```

## Código de Referência

### Arquitetura de Sistema HIPAA-Compliant

```
[Cliente Web/Mobile]
    ↓ TLS 1.2+ (mínimo), preferir TLS 1.3
[WAF / API Gateway]
    ↓ TLS interno
[Aplicação] ← IAM role-based (sem credenciais hardcoded)
    ↓ TLS interno + mTLS
[Banco de Dados] ← encryption at rest (AES-256)
    ↓
[Backup] ← encryption + chaves separadas
    ↓
[Audit Logs] ← imutáveis, retenção mínima 6 anos
```

### Encryption at Rest — RDS + KMS para PHI

```hcl
# Terraform — RDS PostgreSQL HIPAA-compliant
resource "aws_db_instance" "phi_database" {
  engine         = "postgres"
  instance_class = "db.r6g.large"

  # Encryption at rest — obrigatório para HIPAA
  storage_encrypted = true
  kms_key_id        = aws_kms_key.phi_key.arn

  backup_retention_period = 35  # HIPAA exige recoverabilidade
  publicly_accessible     = false
  deletion_protection     = true
  monitoring_interval     = 60
}

# Chave KMS dedicada para PHI com rotação automática
resource "aws_kms_key" "phi_key" {
  description             = "PHI encryption key"
  enable_key_rotation     = true  # rotação anual automática
  deletion_window_in_days = 30

  policy = jsonencode({
    Statement = [
      {
        Effect    = "Deny"
        Principal = "*"
        Action    = ["kms:Decrypt", "kms:Encrypt"]
        Resource  = "*"
        Condition = {
          StringNotEquals = {
            "aws:PrincipalArn" = [
              "arn:aws:iam::ACCOUNT:role/phi-app-role",
              "arn:aws:iam::ACCOUNT:role/phi-readonly-role"
            ]
          }
        }
      }
    ]
  })
}
```

### PHI no Código — Boas Práticas

```typescript
// ❌ NUNCA logar PHI
logger.info(`Processing patient ${patient.ssn} with diagnosis ${diagnosis.code}`);

// ✅ Identificadores anônimos em logs — nunca dados de saúde
logger.info(`Processing record ${recordId} for user ${userId}`);

// ❌ PHI em URLs — aparece em logs de servidor e histórico de browser
// GET /api/patients?ssn=123-45-6789&name=John+Doe

// ✅ PHI apenas no body de POST/PUT, nunca em GET params
// POST /api/patients/search
// Body: { "criteria": { "ssn": "123-45-6789" } }

// Mascaramento para logs de debug
function maskPHI(value: string, type: 'ssn' | 'email' | 'phone'): string {
  switch (type) {
    case 'ssn':   return `***-**-${value.slice(-4)}`;
    case 'email': {
      const [local, domain] = value.split('@');
      return `${local[0]}***@${domain}`;
    }
    case 'phone': return `(***) ***-${value.slice(-4)}`;
  }
}
```

### Audit Logging de Acesso a PHI

HIPAA §164.312(b) exige log de toda atividade de acesso a PHI.

```typescript
class PHIAccessLogger {
  async logAccess(event: {
    userId: string;
    patientId: string;
    action: 'READ' | 'CREATE' | 'UPDATE' | 'DELETE' | 'EXPORT';
    resourceType: string;
    reason?: string;  // justificativa para Break-the-Glass
    ipAddress: string;
    timestamp: Date;
  }): Promise<void> {
    await this.auditDb.create({ ...event });  // append-only — nunca deletar

    // Alerta para acesso excessivo (possível exfiltração)
    const recentAccess = await this.countRecentAccess(event.userId, '1h');
    if (recentAccess > 100) {
      await this.alertSecurityTeam({ type: 'EXCESSIVE_PHI_ACCESS', userId: event.userId });
    }
  }
}

// Break-the-Glass — acesso de emergência com justificativa obrigatória
async function emergencyAccess(userId: string, patientId: string, justification: string) {
  await phiLogger.logAccess({
    userId,
    patientId,
    action: 'READ',
    resourceType: 'PatientRecord',
    reason: `BREAK_THE_GLASS: ${justification}`,
    ipAddress: getCurrentIP(),
    timestamp: new Date()
  });

  await notifyPrivacyOfficer(userId, patientId, justification);
  return patientRepository.findById(patientId);
}
```

### De-identificação (Safe Harbor)

```python
def deidentify_record(phi_record: dict) -> dict:
    """Remove os 18 identificadores HIPAA para uso em pesquisa."""
    deidentified = phi_record.copy()

    fields_to_remove = ['name', 'ssn', 'phone', 'email', 'address', 'mrn', 'device_id']
    for field in fields_to_remove:
        deidentified.pop(field, None)

    # Generalizar datas — datas precisas são PHI
    if 'birth_date' in deidentified:
        birth = datetime.fromisoformat(deidentified['birth_date'])
        age_years = (datetime.now() - birth).days / 365
        deidentified['birth_year'] = '90+' if age_years > 89 else str(birth.year)
        del deidentified['birth_date']

    # Generalizar localização para estado apenas (ZIP = PHI)
    if 'zip_code' in deidentified:
        deidentified['state'] = get_state_from_zip(deidentified['zip_code'])
        del deidentified['zip_code']

    return deidentified
```

### BAA — Business Associate Agreement

```
HIPAA exige BAA com todo fornecedor que processa PHI:

Covered Entity (hospital, clínica)
  → assina BAA com → Business Associate (seu SaaS)
    → assina BAA com → Sub-contractor (AWS, SendGrid, etc.)

✅ Têm BAA disponível: AWS, Google Cloud, Azure, Twilio, SendGrid
❌ Sem BAA (não usar para PHI): Sentry, Slack free/pro, Google Analytics

Se um fornecedor recebe PHI acidentalmente (ex: stack trace com dados de paciente
enviado para o Sentry sem BAA) = violação HIPAA.
```

### Retenção de PHI

```python
class PHIRetentionPolicy:
    MINIMUM_RETENTION_YEARS = 6  # HIPAA mínimo; alguns estados exigem mais

    def secure_delete(self, record_id: str):
        self.db.records.delete(record_id)
        self.backup_service.delete_record(record_id)
        # Crypto-shredding — desautoriza chave de criptografia
        # Mesmo se dados sobreviverem em storage, são indecifráveis
        self.kms.disable_key_material(record_id)
        # Log de destruição deve ser preservado
        self.audit_log.record_destruction(record_id, datetime.now())
```

---

# SOX

## Os 4 Pilares de Controle de TI

```
1. Change Management    → todo deploy em produção requer aprovação documentada
2. Access Controls      → quem desenvolve ≠ quem aprova ≠ quem deploya
3. Audit Trails         → logs imutáveis de quem fez o quê em sistemas financeiros
4. Business Continuity  → backup, recovery e DR testados e documentados
```

## Código de Referência

### Change Management — Pipeline Auditável

```yaml
# GitHub Branch Protection Rules para SOX
required_pull_request_reviews:
  required_approving_review_count: 2  # 2 revisores independentes
  dismiss_stale_reviews: true         # re-aprovação após novos commits
  require_code_owner_reviews: true

restrictions:
  # Apenas release-managers podem mergear — segregação de funções
  teams: ["release-managers"]

required_status_checks:
  - "security-scan"
  - "tests-pass"
  - "compliance-check"
```

```yaml
# GitHub Actions — audit log de deploy em produção
- name: Log deploy event
  run: |
    curl -X POST "$AUDIT_LOG_ENDPOINT/events" \
      -H "Authorization: Bearer $AUDIT_TOKEN" \
      -d '{
        "event_type": "production_deploy",
        "actor": "${{ github.actor }}",
        "commit": "${{ github.sha }}",
        "pr_number": "${{ github.event.pull_request.number }}",
        "approvers": "${{ steps.get-approvers.outputs.approvers }}",
        "timestamp": "'$(date -u +%Y-%m-%dT%H:%M:%SZ)'"
      }'
```

### Segregação de Funções (SoD)

```
❌ Anti-padrão (viola SOX):
  Dev A escreve → Dev A aprova → Dev A deploya
  Uma pessoa controla o ciclo inteiro = risco de fraude não detectada

✅ Padrão SOX-compliant:
  Dev A escreve →
  Dev B + Dev C revisam e aprovam PR →
  Release Manager (diferente de A, B, C) autoriza deploy →
  Pipeline automatizado executa
```

```python
def check_segregation_of_duties(pr_number: str) -> bool:
    pr = github.get_pr(pr_number)
    author = pr.author
    approvers = [r.user for r in pr.reviews if r.state == "APPROVED"]
    deployer = get_pipeline_trigger_user()

    if author in approvers:
        raise ComplianceError(f"Author {author} cannot approve own PR")
    if len(approvers) < 2:
        raise ComplianceError("Requires at least 2 approvers")
    if deployer == author:
        raise ComplianceError(f"Author {author} cannot trigger own deploy")

    return True
```

### Audit Trail Imutável com S3 Object Lock

```hcl
# S3 bucket com Object Lock — nem admin pode deletar
resource "aws_s3_bucket" "audit_logs" {
  bucket = "company-sox-audit-logs"

  object_lock_configuration {
    object_lock_enabled = "Enabled"
    rule {
      default_retention {
        mode  = "COMPLIANCE"  # COMPLIANCE: nem admin pode deletar
        years = 7             # SOX requer retenção mínima de 7 anos
      }
    }
  }
}

# CloudTrail para toda atividade AWS em sistemas financeiros
resource "aws_cloudtrail" "sox_trail" {
  name                          = "sox-audit-trail"
  s3_bucket_name                = aws_s3_bucket.audit_logs.id
  include_global_service_events = true
  is_multi_region_trail         = true
  enable_log_file_validation    = true  # detectar tampering de logs

  event_selector {
    read_write_type           = "All"
    include_management_events = true
    data_resource {
      type   = "AWS::S3::Object"
      values = ["arn:aws:s3:::financial-data-bucket/"]
    }
  }
}
```

### Audit Log no Código com Decorator

```typescript
function audited(action: AuditAction) {
  return function(_target: unknown, _key: string, descriptor: PropertyDescriptor) {
    const original = descriptor.value;
    descriptor.value = async function(...args: unknown[]) {
      const prev = await this.getCurrentState(args[0]);
      const result = await original.apply(this, args);
      const next = await this.getCurrentState(args[0]);

      await auditLog.log({
        action,
        resourceType: 'FinancialRecord',
        resourceId: String(args[0]),
        previousState: prev,
        newState: next,
        actorId: getCurrentUser().id,
        ipAddress: getCurrentIP(),
        timestamp: new Date()
      });

      return result;
    };
  };
}

class FinancialService {
  @audited(AuditAction.UPDATE_ACCOUNT)
  async updateBalance(accountId: string, amount: number): Promise<void> {
    // qualquer mudança é auditada automaticamente com before/after
  }
}
```

### Access Reviews Trimestrais

```python
# Auditores exigem revisão trimestral de acessos a sistemas financeiros
def generate_access_review_report():
    privileged_users = iam.list_users_with_role([
        "FinancialDataReader", "FinancialDataWriter",
        "ProductionDeploy", "DatabaseAdmin"
    ])

    for user in privileged_users:
        last_login = cloudtrail.get_last_activity(user.id)
        inactive = last_login > timedelta(days=90)

        if inactive:
            revoke_access(user.id)  # revogar automaticamente inativos
            notify_security_team(user)
        else:
            send_review_request(hr.get_manager(user.id), user)  # confirmar via manager
```

---

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---|---|---|
| PHI encryption com KMS | Crypto-shredding viável, acesso auditável | Latência adicional em queries |
| BAA com fornecedores | Compliance legal coberta | Limita escolha de ferramentas (sem Sentry free, etc.) |
| SOX SoD automatizada | Bloqueia violações antes de acontecer | Pode atrasar deploys urgentes |
| S3 Object Lock COMPLIANCE | Logs verdadeiramente imutáveis | Não é possível corrigir erros de logging |
| Audit decorator | Auditoria automática sem esquecer | Custo de storage cresce com volume de operações |

## Armadilhas Comuns

**HIPAA:**
- PHI em logs de aplicação sem sanitização — frameworks capturam request bodies automaticamente
- Backup sem encryption — verificar que encryption at rest inclui backups
- Fornecedor sem BAA recebendo PHI acidentalmente (Sentry com stack trace de paciente = violação)
- PHI em variáveis de URL (GET params aparecem em logs de servidor)

**SOX:**
- Aprovar PRs retroativamente (após merge) — auditores detectam pela timeline dos commits
- Conta root compartilhada — viola não-repúdio; todo acesso deve ser individual e rastreável
- Logs deletáveis — CloudWatch sem retention lock ou S3 sem Object Lock = reprovação na auditoria
- "SOX é problema do compliance" — quem implementa sistemas financeiros é responsável pelos controles técnicos

## Quando Usar / Quando Evitar

**HIPAA:** obrigatório se você processa qualquer dado de saúde de cidadão americano. Sem exceção.

**SOX:** aplicável se a empresa é pública nos EUA ou está em processo de IPO. Times de engenharia em fintechs globais frequentemente precisam implementar controles equivalentes para outros reguladores (DORA na UE, BACEN no Brasil).

## Conceitos Relacionados

[[data-privacy]] · [[compliance-soc2-pci]] · [[audit-logging]] · [[secrets-management]] · [[criptografia-fundamentos]] · [[devsecops-pipeline]]

---
*Fonte: tech-mentor skill · tech-mentor-security · 2026-04-01*
