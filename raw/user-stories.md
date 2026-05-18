---
date: 2026-05-17
tags: [tech-mentor, produto, requisitos, agile, user-stories]
skill: tech-mentor-leadership/references/agile-requirements
level: fundamento
---

# User Stories

## Contexto
User Stories são a unidade mínima de valor entregável em contextos ágeis. Capturam **necessidade + contexto + benefício** do ponto de vista do usuário — não do sistema. São o artefato tático de sprint, derivado do [[prd]] e complementar ao [[frd]].

O formato força o time a pensar em valor antes de solução.

## Como Funciona

**Formato canônico:**
```
Como [persona], quero [ação] para [benefício].
```

**Critérios de aceitação — Given/When/Then (Gherkin):**
```
Dado que [contexto/pré-condição],
Quando [ação do usuário ou evento],
Então [resultado esperado e verificável].
```

**Definition of Ready (antes de entrar no sprint):**
- Persona clara e conhecida
- Critérios de aceitação escritos
- Estimada pela equipe
- Dependências mapeadas
- Sem ambiguidade suficiente para bloquear desenvolvimento

**Definition of Done:**
- Código revisado e mergeado
- Testes automatizados escritos e passando
- Critérios de aceitação validados (QA ou PO)
- Documentação atualizada se necessário

## Código de Referência

```markdown
# US-042: Checkout em 1 Clique

**Como** comprador recorrente com cartão salvo,
**quero** confirmar meu pedido sem redigitar os dados de pagamento,
**para** finalizar a compra em menos de 10 segundos.

---

## Critérios de Aceitação

**Cenário 1 — Happy path**
Dado que estou autenticado e tenho um cartão ativo salvo,
Quando clico em "Comprar agora" e confirmo via biometria,
Então o pedido é criado com status "pago" e recebo confirmação por e-mail.

**Cenário 2 — Cartão recusado**
Dado que meu cartão salvo foi recusado pelo gateway,
Quando o sistema tenta processar o pagamento,
Então vejo a mensagem "Pagamento recusado. Verifique seu cartão." sem cobrança.

**Cenário 3 — Biometria indisponível**
Dado que meu dispositivo não suporta biometria,
Quando tento usar o checkout em 1 clique,
Então sou redirecionado para o checkout padrão com meus dados pré-preenchidos.

---

## Notas técnicas
- Integração: Stripe PaymentIntents
- Endpoint: POST /orders
- Retry policy: 2x com intervalo de 3s (ver RN-04 no [[frd]])

## Estimativa
Story points: 8
```

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---|---|---|
| Foco no usuário | Time pensa em valor antes de solução | Pode omitir detalhes técnicos críticos |
| Granularidade pequena | Entregável a cada sprint, feedback rápido | Perda de visão sistêmica sem [[prd]] de respaldo |
| Given/When/Then | Critério de aceitação testável e objetivo | Escrita ruim gera ambiguidade disfarçada de clareza |
| Colaborativo | PO, dev e QA escrevem juntos (Three Amigos) | Depende de maturidade do time para funcionar |

## Quando Usar / Quando Evitar

**Usar:**
- Times ágeis com PO presente e ciclos curtos
- Produtos em descoberta com requisitos mutáveis
- Features com impacto direto na experiência do usuário

**Evitar como substituto de spec em:**
- Sistemas regulados que exigem rastreabilidade de requisitos
- Integrações críticas com SLA contratual → complementar com [[frd]]
- Features puramente de infraestrutura sem impacto de UX direto (usar tasks técnicas)

## Conceitos Relacionados
[[prd]] · [[frd]] · [[backlog]] · [[sprint-planning]] · [[tdd]] · [[bdd]]

---
*Fonte: tech-mentor skill · tech-mentor-leadership · 2026-05-17*
