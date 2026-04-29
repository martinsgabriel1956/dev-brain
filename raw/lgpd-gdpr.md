---
date: 2026-04-23
tags: [tech-mentor, security, compliance, lgpd, gdpr, privacidade]
skill: tech-mentor-security/references/lgpd-gdpr
level: intermediário
---

# LGPD / GDPR — Compliance Técnico

## Contexto

LGPD (Lei 13.709/2018, Brasil) e GDPR (Regulation 2016/679, EU) são regulações de proteção de dados com impacto direto em decisões de arquitetura. Não são só documentos jurídicos — elas determinam como dados pessoais são coletados, armazenados, processados e deletados.

Para engenheiros, compliance significa: data mapping, controles técnicos concretos e capacidade de responder a direitos dos titulares (acesso, portabilidade, exclusão) com SLA definido.

## Como Funciona

### Conceitos-Chave

| Conceito | GDPR | LGPD |
|---|---|---|
| Titular | Data Subject | Titular dos Dados |
| Controlador | Controller | Controlador |
| Operador | Processor | Operador |
| Base legal | Lawful basis (6 bases) | Hipóteses de tratamento (10 bases) |
| DPO | Data Protection Officer (obrigatório em alguns casos) | Encarregado (obrigatório se lei determinar) |
| Notificação de breach | 72h à autoridade | Prazo razoável (ANPD define — pratica: 72h) |

### Bases Legais para Tratamento

```
GDPR Art. 6 / LGPD Art. 7:
1. Consentimento (explícito, granular, revogável)
2. Execução de contrato
3. Obrigação legal
4. Interesses vitais
5. Interesse público
6. Legítimo interesse (GDPR) / Proteção de crédito (LGPD)
```

**Consentimento técnico — o que isso significa:**
```typescript
// Consentimento granular — cada finalidade separada
type ConsentRecord = {
  userId: string;
  purposes: {
    marketing: boolean;
    analytics: boolean;
    thirdPartySharing: boolean;
  };
  collectedAt: string; // ISO 8601
  ipAddress: string;   // evidência de coleta
  version: string;     // versão da política de privacidade
};

// Revogar consentimento deve propagar para todos os sistemas
async function revokeConsent(userId: string, purpose: string) {
  await db.consent.update({
    where: { userId },
    data: { [purpose]: false, revokedAt: new Date() }
  });
  await eventBus.publish("consent.revoked", { userId, purpose });
}
```

### Direitos dos Titulares (Right to...)

| Direito | Prazo (GDPR) | Prazo (LGPD) | Implementação técnica |
|---|---|---|---|
| Acesso | 1 mês | 15 dias | Data export endpoint |
| Portabilidade | 1 mês | - | JSON/CSV estruturado |
| Retificação | 1 mês | - | Update via suporte |
| Exclusão (erasure) | 1 mês | - | Soft delete + anonimização |
| Restrição | Imediato | - | Flag `processing_restricted` |
| Oposição | Imediato | - | Opt-out granular |

### Right to Erasure — Implementação

```sql
-- Anonimização em vez de hard delete (preserva integridade referencial)
UPDATE users
SET
  email     = concat('deleted_', id, '@erased.invalid'),
  name      = 'Usuário Removido',
  phone     = NULL,
  cpf       = NULL,
  deleted_at = NOW(),
  erased_at  = NOW()
WHERE id = $1;

-- Logs e audit trails: substituir PII por pseudônimo
UPDATE audit_logs
SET user_identifier = sha256(user_id::text)  -- irreversível
WHERE user_id = $1;
```

### Data Mapping — O Que Documentar

```yaml
# data-map.yaml — inventário de dados pessoais
assets:
  - name: users
    system: PostgreSQL (RDS prod)
    data_classes: [email, name, cpf, phone, address]
    lawful_basis: contract
    retention: 5 years after account closure
    third_parties: [Stripe, SendGrid]
    international_transfer: true  # Stripe → US

  - name: analytics_events
    system: BigQuery
    data_classes: [user_id, ip_address, device_fingerprint]
    lawful_basis: legitimate_interest
    retention: 90 days
    anonymized_after: 30 days
```

### Notificação de Data Breach

```
GDPR Art. 33 / LGPD Art. 48:

Breach detectado
  ↓
< 72h → Notificar autoridade (ANPD / DPA nacional)
  ↓
Se risco alto para titulares → Notificar titulares afetados
  ↓
Documentar: o quê, quando, quantos afetados, medidas tomadas
```

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---|---|---|
| Anonimização vs hard delete | Preserva integridade referencial | Dados ainda existem no banco |
| Consentimento granular | Compliance correto | UX mais complexo, taxa de opt-in menor |
| Data residency (ex: dados BR só no Brasil) | Compliance LGPD | Custo de infra multi-região maior |
| Retenção mínima | Reduz superfície de ataque | Pressão em times de analytics |

## Quando Usar / Quando Evitar

**LGPD se aplica quando:** qualquer operação de tratamento de dados de pessoas físicas no Brasil, independente de onde a empresa está.

**GDPR se aplica quando:** dados de residentes da UE, independente de onde a empresa está.

**Decisões arquiteturais com impacto:**
- **Data residency:** forçar dados a ficar em região específica → requer arquitetura multi-região com routing por nationalidade
- **Retenção:** definir TTL por tipo de dado desde o schema — não como afterthought
- **Anonimização:** pseudonimização (reversível) ≠ anonimização (irreversível) — GDPR reconsider se dado é "pessoal" após anonimização real

## Conceitos Relacionados

[[data-privacy]] · [[compliance-soc2-pci]] · [[hipaa-sox]] · [[autenticacao-segura]] · [[secrets-management]]

---
*Fonte: tech-mentor skill · tech-mentor-security · 2026-04-23*
