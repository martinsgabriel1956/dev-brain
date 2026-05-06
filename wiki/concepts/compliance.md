---
type: concept
title: "Compliance"
aliases: ["conformidade", "regulatory compliance", "compliance técnico"]
date_created: 2026-05-05
date_updated: 2026-05-05
source_count: 2
tags: [compliance, lgpd, gdpr, pci-dss, soc2, hipaa, iso-27001, security, audit]
skill: tech-mentor-security
status: stable
---

## Definição

Conformidade com regras externas — leis, regulamentos ou padrões da indústria — que definem como sistemas, dados e processos devem ser gerenciados. É a resposta documentada e verificável à pergunta: "como você protege os dados?".

**Compliance ≠ Segurança.** Segurança é o estado real do sistema (quão difícil é comprometer). Compliance é a prova documentada de que as regras foram seguidas. É possível ser compliant e inseguro (checklist sem substância), ou seguro e não-compliant (sem documentação).

## Frameworks Principais

| Framework | Domínio | Quem exige |
|---|---|---|
| LGPD / GDPR | Dados pessoais de usuários | Lei brasileira / europeia |
| PCI-DSS | Dados de cartão de crédito | Bandeiras (Visa, Mastercard) |
| SOC 2 | Segurança, disponibilidade, confidencialidade | Clientes enterprise B2B |
| ISO 27001 | Gestão de segurança da informação | Mercado global |
| HIPAA | Dados de saúde | Regulação americana |

## Quando Compliance Vira Problema de Engenharia

Três cenários em que compliance muda arquitetura e schema:

1. **Data residency** → dado do BR não pode sair do BR → muda topologia multi-region
2. **Audit log obrigatório** → toda operação sensível deve ser registrada → muda schema de DB e fluxo de escrita
3. **DSAR** (direito de acesso/deleção) → você precisa mapear onde cada dado do usuário vive (DB, Redis, S3, backups)

## Padrão de Implementação — Audit Log

```sql
INSERT INTO audit_log (user_id, action, resource, timestamp)
VALUES ($1, 'READ', 'users.cpf', NOW());
```

Satisfaz simultaneamente: LGPD/SOC 2 CC7.2, PCI-DSS Req 10, ISO 27001 A.12.4. Invista uma vez.

## Padrão de Implementação — DSAR

```typescript
async function deleteUserData(userId: string) {
  await prisma.$transaction(async tx => {
    await tx.auditLog.create({ data: { userId, action: "DATA_DELETION_REQUEST" } });
    await tx.userProfile.delete({ where: { userId } });
    await tx.user.update({ where: { id: userId }, data: { deletedAt: new Date() } });
  });
  // Redis, S3, backups — precisam de processo separado
}
```

## Key Sources

- [[sources/compliance]] — visão geral: frameworks, security vs compliance, cenários de engenharia
- [[sources/compliance-soc2-pci]] — SOC 2 Type I vs II, PCI-DSS tokenização, audit logging como evidência universal
- [[sources/lgpd-gdpr]] — data mapping, lawful basis, 72h breach notification
- [[sources/hipaa-sox]] — PHI/BAA, Segregation of Duties, S3 Object Lock

## Conceitos Relacionados

[[concepts/audit-log]] · [[concepts/data-residency]] · [[concepts/dsar]] · [[concepts/zero-trust]] · [[concepts/data-privacy]]
