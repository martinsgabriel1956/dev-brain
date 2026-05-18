---
date: 2026-05-17
tags: [tech-mentor, infra, ops, runbook]
skill: tech-mentor-infra/references/ops-docs
level: intermediário
---

# Runbook

## Contexto
Runbook é um documento **procedural e técnico** que descreve como executar uma operação específica e repetível. É a documentação operacional mais granular — criada para que qualquer engenheiro de plantão consiga executar uma tarefa sem depender do autor original.

Vive no ciclo **pré-incidente**: é consultado durante deploys, manutenções programadas e operações rotineiras.

## Como Funciona

Um runbook tem **passos lineares**, sem decisões ramificadas. A premissa é: a situação já está identificada, agora é só executar.

Estrutura típica:

- **Título** — nome da operação (ex: `Rotacionar credenciais do banco`)
- **Pré-requisitos** — permissões, ferramentas, contexto necessário
- **Passos numerados** — comandos exatos, em ordem
- **Verificação** — como confirmar que funcionou
- **Rollback** — o que fazer se algo der errado

## Código de Referência

```markdown
## Runbook: Rotacionar credenciais do banco (RDS + Secrets Manager)

**Pré-requisitos:** AWS CLI configurado, acesso ao Secrets Manager, kubectl com contexto correto

### Passos

1. Gerar nova senha segura
   ```bash
   openssl rand -base64 32
   ```

2. Atualizar no Secrets Manager
   ```bash
   aws secretsmanager put-secret-value \
     --secret-id prod/api/db-password \
     --secret-string '{"password":"<nova-senha>"}'
   ```

3. Fazer rolling restart dos pods para pegar a nova secret
   ```bash
   kubectl rollout restart deployment/api -n production
   ```

4. Acompanhar o rollout
   ```bash
   kubectl rollout status deployment/api -n production
   ```

5. Verificar conexões ativas no banco
   ```bash
   # Checar métrica db_connections_active no Grafana
   # Dashboard: https://grafana.internal/d/db-overview
   ```

### Verificação de sucesso
- Todos os pods em `Running` com `READY 1/1`
- Métrica `db_connections_active` estável
- Nenhum erro 5xx no log da API

### Rollback
Se os pods não subirem após 5 minutos:
```bash
kubectl rollout undo deployment/api -n production
```
Restaurar senha anterior no Secrets Manager e repetir o rollout.
```

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---|---|---|
| Padronização | Elimina variação humana na execução | Pode ficar desatualizado se não houver processo de revisão |
| Velocidade | Reduz MTTR em operações conhecidas | Não cobre situações inesperadas (para isso existe o playbook) |
| Autonomia | Qualquer engenheiro executa sem depender do autor | Requer disciplina para manter atualizado |

## Quando Usar / Quando Evitar

**Usar quando:**
- A operação é repetível e bem definida
- O caminho feliz tem passos claros
- Há risco de erro humano em sequências longas

**Evitar quando:**
- A situação tem múltiplas possíveis causas (→ use [[playbook]])
- É um caso único sem previsão de repetição

## Conceitos Relacionados
[[playbook]] · [[post-mortem]] · [[sre]] · [[oncall]]

---
*Fonte: tech-mentor skill · tech-mentor-infra · 2026-05-17*
