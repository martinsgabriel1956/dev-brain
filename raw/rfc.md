---
date: 2026-04-13
tags: [tech-mentor, lideranca, rfc, processo-tecnico, decisao]
skill: tech-mentor-leadership/references/technical-process
level: intermediário
---

# RFC — Request for Comments

## Contexto

RFC é um documento que propõe uma mudança técnica significativa e convida o time a comentar antes da implementação. Diferente do ADR (que documenta decisões já tomadas), o RFC é o processo de **chegar à decisão**.

Usado por: Rust, Python (PEP), TC39 (JavaScript), grandes times de engenharia (Stripe, Shopify, etc.).

O valor: força o autor a pensar profundamente antes de implementar, expõe trade-offs para o time, cria registro histórico do "porquê".

## Template de RFC

```markdown
# RFC-0042: Migração do autenticador para Keycloak

**Status:** Draft | In Review | Accepted | Rejected | Withdrawn  
**Author:** @alice  
**Created:** 2026-04-13  
**Updated:** 2026-04-15  
**Reviewers:** @bob, @carol, @dave

---

## Resumo

*Uma frase: o que está sendo proposto.*

Migrar nosso sistema de autenticação caseiro para Keycloak para suportar SSO, 
SAML e provisionamento automático de usuários (SCIM).

---

## Motivação

*Por que isso precisa existir? Qual problema resolve? Use dados quando possível.*

- Nosso auth caseiro não suporta SSO (blocker para 3 contratos enterprise)
- SCIM não está implementado — provisionamento de usuários é manual (4h/semana)
- Auditoria de segurança identificou ausência de MFA como risco crítico
- Keycloak resolve os 3 pontos com solução battle-tested

---

## Proposta Detalhada

*Como funciona? Inclua diagramas, código de referência, API contracts.*

### Arquitetura

[diagrama C4 ou ASCII da nova arquitetura]

### Migration Path

Fase 1 (semanas 1-2): Deploy do Keycloak em staging
Fase 2 (semanas 3-4): Migração de usuários via API bulk
Fase 3 (semanas 5-6): Cutover gradual (5% → 25% → 100%)

### Schema Changes

[SQL das mudanças de banco necessárias]

---

## Alternativas Consideradas

*Quais outras opções foram avaliadas e por que foram descartadas.*

| Opção | Prós | Contras | Decisão |
|---|---|---|---|
| Auth0 | Managed, fácil | $X/mês, vendor lock-in | Descartado — custo |
| Continuar caseiro | Zero custo | Não resolve SSO/SCIM | Descartado — blocker |
| Cognito | AWS nativo | Limitado, difícil customizar | Descartado — flexibilidade |
| **Keycloak** | Open source, completo, SSO | Ops overhead | **Escolhido** |

---

## Impacto e Riscos

*O que pode dar errado? Como mitigamos?*

| Risco | Probabilidade | Impacto | Mitigação |
|---|---|---|---|
| Dados perdidos na migração | Baixa | Alto | Dry run + validação de contagem |
| Downtime no cutover | Média | Alto | Rollback em < 5min via feature flag |
| Curva de aprendizado Keycloak | Alta | Médio | 2 sprints de spike antes |

---

## Plano de Rollout

- [ ] Spike de 2 sprints para a equipe aprender Keycloak
- [ ] RFC aprovado antes do início da implementação
- [ ] Feature flag para cutover gradual
- [ ] Runbook de rollback documentado
- [ ] Load testing antes do cutover

---

## Perguntas em Aberto

*O que ainda não foi decidido. Use o thread de review para resolver.*

1. Onde hospedar o Keycloak? (K8s próprio vs managed via RHBK)
2. Estratégia de migração de senhas (hash Keycloak ≠ hash nosso)

---

## Referências

- [Keycloak documentation](https://keycloak.org/docs)
- [RFC-0038: Nova estratégia de autenticação] (ADR que motivou este RFC)
```

## O Processo

```
1. Autor identifica mudança significativa → cria RFC como Draft
2. Compartilha no canal do time (Slack, email)
3. Review period: 3-7 dias (dependendo do tamanho)
4. Discussão assíncrona nos comentários do PR
5. Reunião síncrona apenas se houver bloqueio real
6. Decisão: Accepted / Rejected / Needs Changes
7. Merge do RFC no repositório
8. ADR criado com base na decisão
```

### O que merece um RFC?

```
Merece RFC:
✓ Nova dependência de infraestrutura (banco, broker, serviço)
✓ Mudança de API que afeta múltiplos consumidores
✓ Mudança de arquitetura que afeta múltiplos times
✓ Qualquer coisa que demore > 2 sprints para implementar
✓ Decisões com trade-offs não óbvios

NÃO merece RFC:
✗ Bug fixes
✗ Refactoring interno a um serviço
✗ Nova feature dentro do escopo de um time
✗ Mudanças de configuração triviais
```

## RFC vs ADR

| | RFC | ADR |
|---|---|---|
| **Quando** | Antes de decidir | Depois de decidir |
| **Objetivo** | Coletar input, chegar à decisão | Registrar a decisão e o contexto |
| **Formato** | Proposta + alternativas + perguntas abertas | Decisão + consequências |
| **Mutabilidade** | Evolui durante o review | Imutável após aprovação |
| **Quem escreve** | Proponente da mudança | Qualquer dev após a decisão |

Na prática: RFC → decisão → ADR.

## Ferramentas

- RFC como PR em `docs/rfcs/` no repositório da equipe
- GitHub Discussions para times menores
- Confluence para times enterprise
- Linear para integração com tarefas

## Conceitos Relacionados

[[adr]] · [[c4-model]] · [[tech-debt]] · [[evolutionary-architecture]] · [[code-review]]

---
*Fonte: tech-mentor skill · tech-mentor-leadership · 2026-04-13*
