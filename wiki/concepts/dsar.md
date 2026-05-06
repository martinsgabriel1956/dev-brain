---
type: concept
title: "DSAR"
aliases: ["Data Subject Access Request", "direito de acesso", "direito de deleção", "right to erasure", "right to be forgotten"]
date_created: 2026-05-05
date_updated: 2026-05-05
source_count: 1
tags: [dsar, lgpd, gdpr, compliance, data-privacy, user-rights]
skill: tech-mentor-security
status: stub
---

## Definição

Data Subject Access Request — direito do usuário de acessar, corrigir ou deletar todos os seus dados pessoais. Na LGPD (Art. 18) e no GDPR (Art. 17), empresas têm prazo definido para responder (LGPD: 15 dias para informar, GDPR: 30 dias para responder/executar).

## Por Que É Problema de Engenharia

Para atender um DSAR de deleção, você precisa saber onde cada dado do usuário vive. Em sistemas típicos, dados existem em:
- DB relacional (tabelas de usuário, perfil, logs de atividade)
- Redis (sessões, cache de perfil, rate limiting por usuário)
- S3 / object storage (avatares, documentos, exports)
- Backups (precisam de processo separado — não é possível deletar de um backup sem restaurar)
- Sistemas de terceiros integrados (analytics, CRM, email marketing)

## Padrão de Implementação

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

O `auditLog.create` dentro da transação é obrigatório — a deleção em si é uma operação auditável.

## Key Sources

- [[sources/compliance]] — DSAR como cenário de engenharia obrigatório para LGPD/GDPR

## Conceitos Relacionados

[[concepts/compliance]] · [[concepts/data-privacy]] · [[concepts/audit-log]] · [[concepts/soft-delete]]
