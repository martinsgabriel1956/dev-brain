---
date: 2026-04-01
tags: [tech-mentor, security, privacy, lgpd, gdpr, pii, erasure, pseudonimizacao, data-retention]
skill: tech-mentor-security/references/data-privacy
level: intermediário
---

# Data Privacy — LGPD/GDPR

## Contexto

LGPD e GDPR não são só políticas — impõem obrigações técnicas concretas que afetam schema de banco, logging, backups, APIs e pipelines de dados. Privacidade precisa ser **by design**, não um módulo adicionado depois.

**Multas:** LGPD até R$50M/ano por infração · GDPR até €20M ou 4% do faturamento global.

## Conceitos Fundamentais

**PII (Personally Identifiable Information):**
- Diretos: nome, CPF, email, telefone, IP, cookie ID
- Indiretos: combinação de localização + idade + profissão pode identificar alguém

**Categorias sensíveis** (proteção extra): saúde, biometria, origem racial, orientação sexual, dados de crianças.

**Bases legais** — obrigatório ter uma para cada tratamento:
```
Consentimento       → revogável; não use como base default para tudo
Execução de contrato → o mais comum em e-commerce
Obrigação legal     → nota fiscal exige CPF
Legítimo interesse  → requer balancing test documentado

❌ Pedir CPF para newsletter (sem base legal)
✅ Pedir CPF apenas para emissão de nota fiscal
```

## Código de Referência

### Data Mapping — Primeiro Passo Obrigatório

```typescript
// ROPA — Record of Processing Activities
type DataProcessingRecord = {
  purpose: string;          // "envio de email transacional"
  legalBasis: string;       // "execução de contrato"
  dataCategories: string[]; // ["email", "nome"]
  retention: string;        // "2 anos após último login"
  thirdParties: string[];   // ["SendGrid", "AWS SES"]
  crossBorder: boolean;     // transferência para fora do BR/UE?
};
```

### Right to Erasure — Direito ao Esquecimento

Não é só `DELETE FROM users WHERE id = $1`. PII pode estar em múltiplos sistemas.

```typescript
async function eraseUser(userId: string): Promise<void> {
  await db.transaction(async trx => {
    // 1. Anonimizar — não deletar (integridade referencial + retenção fiscal)
    await trx.query(`
      UPDATE users SET
        name = 'Usuário Removido',
        email = $2,
        cpf = NULL,
        phone = NULL,
        deleted_at = NOW()
      WHERE id = $1
    `, [userId, `deleted-${userId}@removed.invalid`]);

    // 2. Deletar dados de comportamento (sem retenção legal)
    await trx.query('DELETE FROM user_preferences WHERE user_id = $1', [userId]);
    await trx.query('DELETE FROM sessions WHERE user_id = $1', [userId]);

    // 3. Anonimizar em tabelas com retenção obrigatória (ex: pedidos para fiscal)
    await trx.query(`
      UPDATE orders SET customer_name = 'Cliente Removido', customer_cpf = NULL
      WHERE user_id = $1
    `, [userId]);

    // 4. Registrar no audit log — prova de cumprimento
    await trx.query(
      'INSERT INTO erasure_log (user_id, requested_at, completed_at) VALUES ($1, $2, NOW())',
      [userId, new Date()]
    );
  });

  // 5. Propagar para sistemas externos via evento
  await eventBus.publish('user.erased', { userId });
  // Consumidores: search index, analytics, marketing platform, CDN cache
}
```

**Onde PII pode estar:**
```
Banco de dados          ✅ update direto
Cache (Redis)           ✅ DEL por chave de userId
Elasticsearch           ✅ delete by query
S3 / Object Storage     ✅ delete objeto por chave
Kafka                   ❌ imutável — use crypto-shredding
Backups                 ❌ não modifique — expire via TTL de retenção
Data Warehouse          ⚠️ anonimize na próxima ETL
Logs de aplicação       ❌ não devem conter PII — prevenção > remediação
```

**Crypto-shredding para sistemas imutáveis (Kafka):**
```
1. Encriptar dado com chave por usuário: AES(email, key=userId-key)
2. Para "apagar": deletar userId-key no KMS
3. O dado torna-se lixo indecifrável — efetivamente apagado
```

### PII em Logs — Nunca em Texto Plano

```typescript
const PII_FIELDS = ['email', 'cpf', 'phone', 'password', 'creditCard', 'token'];

function sanitizeForLog(data: Record<string, unknown>): Record<string, unknown> {
  return Object.fromEntries(
    Object.entries(data).map(([key, value]) => {
      if (PII_FIELDS.includes(key)) return [key, '[REDACTED]'];
      if (key === 'email' && typeof value === 'string') {
        const [local, domain] = value.split('@');
        return [key, `${local[0]}***@${domain}`];
      }
      return [key, value];
    })
  );
}

console.log({ message: 'User login', ...sanitizeForLog({ userId: user.id, email: user.email }) });
// { message: 'User login', userId: 'uuid', email: 'j***@example.com' }
```

### Pseudonimização vs Anonimização

| | Pseudonimização | Anonimização |
|---|---|---|
| Reversível? | Sim (com chave) | Não |
| Ainda é dado pessoal? | Sim | Não |
| Uso | Analytics, data warehouse | Datasets públicos, pesquisa |

```typescript
// Pseudonimização determinística — mesmo input gera mesmo output
// Permite joins em analytics sem expor PII
function pseudonymize(value: string, secret: string): string {
  return createHmac("sha256", secret).update(value).digest("hex").slice(0, 16);
}

// "john@example.com" → "a3f8c2d1e9b4f7a2" (consistente, irreversível sem o secret)
const pseudoId = pseudonymize(user.email, process.env.PSEUDONYM_SECRET!);
```

### Audit Trail Imutável

```sql
CREATE TABLE data_access_audit (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  accessed_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  user_id UUID,
  subject_user_id UUID,        -- de quem são os dados acessados
  resource_type TEXT NOT NULL, -- 'profile', 'orders', 'medical_records'
  resource_id UUID,
  operation TEXT NOT NULL,     -- 'READ', 'UPDATE', 'DELETE', 'EXPORT'
  ip_address INET,
  user_agent TEXT
);

-- Tabela imutável
REVOKE UPDATE, DELETE ON data_access_audit FROM app_user;
```

### Data Retention Automática

```typescript
async function enforceRetentionPolicy() {
  const cutoffs = {
    sessions:      subDays(new Date(), 90),
    logs:          subYears(new Date(), 1),
    inactiveUsers: subYears(new Date(), 3),
    orderHistory:  subYears(new Date(), 7),  // obrigação fiscal
  };

  await db.sessions.deleteMany({ where: { createdAt: { lt: cutoffs.sessions } } });
  // inactiveUsers → anonimizar, não deletar (histórico fiscal permanece)
}
```

### PII Detection no CI

```yaml
# .github/workflows/pii-scan.yml
- name: Scan com Microsoft Presidio
  run: |
    pip install presidio-analyzer
    python scripts/scan_pii.py --path ./src --fail-on-found
```

```toml
# .gitleaks.toml — padrões brasileiros
[[rules]]
id = "cpf"
regex = '''\d{3}\.\d{3}\.\d{3}-\d{2}'''
severity = "HIGH"

[[rules]]
id = "cnpj"
regex = '''\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}'''
severity = "HIGH"
```

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---|---|---|
| Erasure por anonimização | Mantém integridade referencial | PII precisa ser mapeada em todos os sistemas |
| Crypto-shredding | "Apaga" dados em sistemas imutáveis | Complexidade de gestão de chaves por usuário |
| Pseudonimização | Permite analytics sem expor PII | Ainda é dado pessoal — LGPD/GDPR se aplica |
| PII Detection no CI | Previne vazamentos antes de chegar ao repo | Falsos positivos em strings sintéticas de testes |

## Privacy by Design — Checklist

```
1. Data minimization:   colete apenas o estritamente necessário
   → Cada campo novo no schema exige: "qual base legal?"
2. Purpose limitation:  dados coletados para X não são usados para Y
3. Storage limitation:  TTL definido para cada tipo de dado na criação
4. Privacy by default:  opt-in para analytics, não opt-out
5. Encryption at rest:  PII sempre criptografada em repouso
6. Access minimization: views mascaradas para times de analytics
```

## Prazos Legais

```
LGPD: resposta a solicitação de titular → 15 dias
GDPR: resposta a solicitação de titular → 30 dias
GDPR: notificação de vazamento à autoridade → 72 horas
LGPD: notificação de vazamento à ANPD → prazo razoável (ainda indefinido em lei)
```

## Conceitos Relacionados

[[secrets-management]] · [[criptografia-fundamentos]] · [[audit-logging]] · [[compliance-soc2-pci]] · [[secure-design-patterns]]

---
*Fonte: tech-mentor skill · tech-mentor-security · 2026-04-01*
