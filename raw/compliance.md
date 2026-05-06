---
date: 2026-05-05
tags: [tech-mentor, security, compliance]
skill: tech-mentor-security/references/compliance
level: intermediário
---

# Compliance

## Contexto
Compliance é a conformidade com regras externas — leis, regulamentos ou padrões da indústria — que definem como sistemas, dados e processos devem ser gerenciados. É a resposta documentada e verificável à pergunta: "como você protege os dados?"

## Como Funciona

Frameworks definem controles obrigatórios. Uma auditoria verifica se esses controles estão implementados e documentados. Falhar na auditoria resulta em multas, perda de certificação ou impedimento de operar em determinados mercados.

## Frameworks Mais Relevantes

| Framework | Domínio | Quem exige |
|---|---|---|
| **LGPD / GDPR** | Dados pessoais de usuários | Lei brasileira / europeia |
| **PCI-DSS** | Dados de cartão de crédito | Bandeiras (Visa, Mastercard) |
| **SOC 2** | Segurança, disponibilidade, confidencialidade | Clientes enterprise B2B |
| **ISO 27001** | Gestão de segurança da informação | Mercado global |
| **HIPAA** | Dados de saúde | Regulação americana |

## Código de Referência

```sql
-- Audit log para operações sensíveis (exigido por LGPD/SOC 2)
INSERT INTO audit_log (user_id, action, resource, timestamp)
VALUES ($1, 'READ', 'users.cpf', NOW());
```

```typescript
// Deleção de dados pessoais (DSAR — LGPD Art. 18)
async function deleteUserData(userId: string) {
  await prisma.$transaction(async tx => {
    await tx.auditLog.create({ data: { userId, action: "DATA_DELETION_REQUEST" } });
    await tx.userProfile.delete({ where: { userId } });
    await tx.user.update({ where: { id: userId }, data: { deletedAt: new Date() } });
  });
  // Redis, S3, backups — precisam de processo separado
}
```

## Trade-offs

| Decisão | Sem compliance | Com compliance |
|---|---|---|
| Logs | Log o que for útil | Log tudo auditável, com retenção definida |
| Deleção de dados | DELETE simples | Deleção em cascata em múltiplos sistemas |
| Deploy | Qualquer dev faz push | Change management com aprovação documentada |
| Infra | Escolha o mais barato | Só regiões certificadas (ex: AWS GovCloud para HIPAA) |

## Compliance vs. Segurança

São relacionados, mas diferentes:
- **Segurança** é o estado real do sistema — quão difícil é comprometer.
- **Compliance** é a prova documentada de que você seguiu as regras.

Você pode ser compliant e inseguro (checklist sem substância). Pode ser seguro e não-compliant (sem documentação). O objetivo é os dois.

## Quando Usar / Quando Evitar

**Compliance vira problema de engenharia quando:**
- Precisam de **data residency** → dado do BR não pode sair do BR → muda arquitetura multi-region
- Precisam de **audit log** em toda operação sensível → muda schema de DB e fluxo de escrita
- Precisam de **DSAR** (direito de acesso/deleção) → você precisa mapear onde cada dado do usuário vive

**Evitar a armadilha de:** tratar compliance como checklist burocrático sem substância técnica — isso cria falsa sensação de segurança.

## Conceitos Relacionados
[[lgpd]] · [[gdpr]] · [[audit-log]] · [[criptografia]] · [[zero-trust]] · [[data-residency]]

---
*Fonte: tech-mentor skill · tech-mentor-security · 2026-05-05*
