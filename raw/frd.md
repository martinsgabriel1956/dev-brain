---
date: 2026-05-17
tags: [tech-mentor, produto, requisitos, frd]
skill: tech-mentor-leadership/references/functional-requirements
level: intermediário
---

# FRD — Functional Requirements Document

## Contexto
O FRD detalha **como o sistema deve se comportar** funcionalmente. É derivado do [[prd]] e serve como especificação técnica suficiente para que engenharia implemente sem ambiguidade.

É especialmente crítico em projetos com alta complexidade técnica, integrações externas, sistemas regulados (fintech, saúde, jurídico) ou times distribuídos onde o PM não tem contato diário com o time.

## Como Funciona

O FRD descreve fluxos funcionais, regras de negócio, entradas/saídas, estados do sistema e comportamentos de erro. Não prescreve arquitetura — apenas o contrato funcional que a implementação deve honrar.

**Estrutura típica:**

```
1. Visão geral do módulo/feature
2. Atores e permissões
3. Fluxos funcionais (happy path + alternativos)
4. Regras de negócio explícitas
5. Entradas, saídas, validações
6. Integrações e dependências externas
7. Tratamento de erros e estados de falha
8. Requisitos não-funcionais: performance, SLA, segurança
```

## Código de Referência

```markdown
# FRD: Checkout em 1 Clique

## Ator
Usuário autenticado com cartão de crédito salvo e biometria habilitada.

## Fluxo principal
1. Usuário clica em "Comprar agora" na PDP
2. Sistema exibe resumo do pedido + cartão salvo (últimos 4 dígitos)
3. Usuário confirma via biometria (FaceID / Touch ID)
4. Sistema processa pagamento via Stripe
5. Sistema persiste pedido com status `pending`
6. Stripe retorna confirmação → status atualizado para `paid`
7. Webhook dispara notificação de e-mail e push

## Regras de negócio
- RN-01: Apenas cartões com status `active` são elegíveis
- RN-02: Valor máximo por transação: R$ 10.000,00
- RN-03: Biometria obrigatória para valores > R$ 500,00
- RN-04: Retry automático em falha Stripe: máximo 2 tentativas com intervalo de 3s

## Tratamento de erros
| Cenário | Comportamento |
|---|---|
| Stripe timeout | Exibir "Tente novamente" + não debitar |
| Biometria falha 3x | Redirecionar para checkout padrão |
| Cartão recusado | Exibir mensagem do gateway + sugerir outro cartão |

## SLA
- Tempo de resposta do endpoint POST /orders: p95 < 800ms
- Disponibilidade: 99.9%
```

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---|---|---|
| Especificação detalhada | Reduz ambiguidade e retrabalho | Custo alto de escrita e manutenção |
| Regras de negócio explícitas | QA consegue derivar casos de teste direto | Fica desatualizado rapidamente em produtos com iteração rápida |
| Cobertura de erros | Edge cases mapeados antes do código | Pode atrasar o início do desenvolvimento |

## Quando Usar / Quando Evitar

**Usar:**
- Sistemas regulados: PCI-DSS, LGPD, HIPAA
- Integrações críticas com terceiros (pagamentos, gateways, ERPs)
- Times grandes ou distribuídos sem contato diário com o PM
- Features com SLA contratual

**Evitar:**
- MVPs e experimentos rápidos — overhead não compensa
- Times pequenos com PO presente no dia a dia — [[user-stories]] com bons critérios de aceitação cobrem o mesmo espaço

## Conceitos Relacionados
[[prd]] · [[user-stories]] · [[sla]] · [[contrato-de-api]] · [[testes-de-contrato]]

---
*Fonte: tech-mentor skill · tech-mentor-leadership · 2026-05-17*
