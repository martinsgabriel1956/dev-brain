---
date: 2026-05-17
tags: [tech-mentor, produto, requisitos, prd]
skill: tech-mentor-leadership/references/product-requirements
level: fundamento
---

# PRD — Product Requirements Document

## Contexto
O PRD é o artefato de alinhamento estratégico de produto. Ele responde ao **por quê** e ao **o quê** — sem entrar em como o sistema será implementado. É escrito antes de qualquer sprint e serve como contrato de escopo entre negócio, produto e engenharia.

Em times maduros, o PRD é o ponto de partida para derivar FRDs, User Stories e roadmaps técnicos.

## Como Funciona

O PRD captura o problema de negócio, define sucesso de forma mensurável e delimita escopo. Ele deve ser suficientemente detalhado para alinhar stakeholders, mas suficientemente abstrato para não antecipar decisões técnicas.

**Estrutura típica:**

```
1. Problema e oportunidade
2. Objetivos e métricas de sucesso (OKRs / KPIs)
3. Personas e casos de uso em alto nível
4. Escopo (in / out of scope)
5. Restrições: prazo, orçamento, compliance, dependências
6. Riscos e premissas
```

## Código de Referência

```markdown
# PRD: Checkout em 1 Clique

## Problema
Taxa de abandono de carrinho: 68%. Principal causa: fricção no fluxo de pagamento.

## Objetivo
Reduzir etapas de checkout de 4 para 1 para usuários com cartão salvo.

## Métricas de sucesso
- Conversão de checkout: +15% em 90 dias
- Tempo médio de checkout: < 5s

## Personas
- Comprador recorrente com cartão salvo
- Mobile-first (72% do tráfego)

## Escopo
In: pagamento com cartão salvo, confirmação via biometria
Out: novos métodos de pagamento, parcelamento

## Restrições
- Compliance PCI-DSS nível 1
- Lançamento até Q3 2026
```

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---|---|---|
| Alto nível de abstração | Flexibilidade técnica, alinhamento rápido | Ambiguidade pode gerar retrabalho |
| Métricas explícitas | Critério objetivo de sucesso | Exige dados históricos para definir metas realistas |
| Escopo delimitado | Foco no MVP | Pode parecer restritivo para stakeholders |

## Quando Usar / Quando Evitar

**Usar:**
- Antes de qualquer iniciativa de produto
- Para alinhar C-level, PM, engenharia e design em torno do mesmo problema
- Quando múltiplos times trabalham na mesma feature

**Evitar como substituto de spec técnica:** o PRD não detalha fluxos funcionais — para isso, use o [[frd]].

## Conceitos Relacionados
[[frd]] · [[user-stories]] · [[okr]] · [[roadmap]] · [[mvp]]

---
*Fonte: tech-mentor skill · tech-mentor-leadership · 2026-05-17*
