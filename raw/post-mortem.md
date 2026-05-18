---
date: 2026-05-17
tags: [tech-mentor, infra, ops, post-mortem, incident-response, sre]
skill: tech-mentor-infra/references/ops-docs
level: intermediário
---

# Post-mortem

## Contexto
Post-mortem é um documento **retrospectivo** que analisa um incidente após a resolução com o objetivo de evitar recorrência. É a peça mais importante do ciclo operacional porque transforma falhas em aprendizado sistêmico.

O princípio central é **blameless**: o foco é em sistemas, processos e ferramentas — nunca em culpar pessoas. Erros humanos são sintomas de falhas de sistema.

Vive no ciclo **pós-incidente**: deve ser escrito em até 48h após a resolução, enquanto o contexto ainda está fresco.

## Como Funciona

Um post-mortem eficaz responde três perguntas:
1. **O que aconteceu?** — fatos, linha do tempo, impacto
2. **Por que aconteceu?** — causa raiz + fatores contribuintes (os "5 porquês")
3. **Como evitar?** — action items concretos, com dono e prazo

A técnica dos **5 Porquês** é usada para ir além do sintoma e chegar à causa sistêmica:

```
Sintoma: API ficou fora por 45 minutos
Por quê? → Migration travou o banco com lock
Por quê? → NOT NULL sem default em tabela de 8M rows
Por quê? → Não foi testada com volume de produção
Por quê? → Staging tem apenas 10k rows
Por quê? → Não existe processo de validar migrations com dump de prod
                          ↑
                    Causa raiz sistêmica
```

## Código de Referência

```markdown
## Post-mortem: Outage total da API — 2026-05-14

**Severidade:** P1  
**Duração:** 45 minutos (14:32 – 15:17 UTC)  
**Impacto:** 100% dos requests falhando com 503. ~12.000 usuários afetados.

---

### Linha do Tempo

| Horário (UTC) | Evento |
|---|---|
| 14:30 | Deploy da v2.3.1 iniciado |
| 14:32 | Alertas de 5xx disparam (threshold: > 1% por 2min) |
| 14:38 | Engenheiro de plantão inicia investigação |
| 14:45 | Causa identificada: migration com lock no RDS |
| 14:50 | Decisão de rollback tomada |
| 15:17 | Rollback completo, serviço restaurado |

---

### Impacto

- **Usuários afetados:** ~12.000
- **Receita estimada:** R$ 4.200 em transações bloqueadas
- **SLA:** violação de 99.9% mensal (limite: 43min/mês)

---

### Causa Raiz

Migration `0048_add_verified_at_to_users` adicionou coluna `verified_at NOT NULL`
sem valor default em tabela `users` com 8.2M rows. O PostgreSQL adquiriu
um `AccessExclusiveLock` durante o `ALTER TABLE`, bloqueando 100% das queries
por 47 minutos até o lock ser liberado manualmente.

---

### Fatores Contribuintes

- Migration não testada com volume representativo de produção (staging tem 10k rows)
- Checklist de deploy não inclui validação de migrations pesadas (> 1M rows)
- Ausência de alerta de `lock_timeout` no RDS → demora para identificar causa
- Runbook de deploy não menciona estratégia segura para `ALTER TABLE` em larga escala

---

### O que foi bem

- Alertas de 5xx dispararam em menos de 2 minutos
- Comunicação interna foi rápida e centralizada no #incidents
- Rollback executado sem problemas adicionais

---

### Action Items

| Ação | Responsável | Prazo |
|---|---|---|
| Adicionar validação de migrations em staging com dump de produção anonimizado | João | 2026-05-21 |
| Atualizar checklist de deploy com inspeção de migrations > 1M rows | Maria | 2026-05-19 |
| Configurar `lock_timeout = 5s` no RDS para alertar antes de travar | DevOps | 2026-05-24 |
| Adicionar runbook para `ALTER TABLE` seguro em produção (CONCURRENTLY, backfill) | João | 2026-05-28 |

---

### Lições Aprendidas

Para adicionar `NOT NULL` em tabela grande sem downtime:
1. Adicionar coluna como `NULL` primeiro
2. Backfill em batches: `UPDATE users SET verified_at = now() WHERE id BETWEEN x AND y`
3. Adicionar constraint `NOT NULL` após backfill completo
4. Usar `ALTER TABLE ... SET NOT NULL` com `lock_timeout` curto como safety net
```

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---|---|---|
| Cultura blameless | Engenheiros reportam problemas sem medo | Requer maturidade da liderança para não virar caça às bruxas |
| Action items concretos | Converte incidente em melhoria real | Sem acompanhamento, action items ficam no papel |
| Documentação pública interna | Dissemina aprendizado para toda a eng | Pode expor falhas embaraçosas se não houver cultura psicológica segura |

## Quando Usar / Quando Evitar

**Usar quando:**
- Qualquer incidente P1 ou P2
- Incidente P3 com causa raiz nova ou recorrente
- Near-miss que poderia ter sido grave

**Evitar quando:**
- Incidente trivial com causa óbvia e fix imediato sem risco de recorrência
- (Nunca evite por medo de constrangimento — isso destrói a cultura)

## Conceitos Relacionados
[[runbook]] · [[playbook]] · [[sre]] · [[oncall]] · [[sla-slo-sli]]

---
*Fonte: tech-mentor skill · tech-mentor-infra · 2026-05-17*
