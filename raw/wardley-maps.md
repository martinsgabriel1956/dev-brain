---
date: 2026-04-17
tags: [tech-mentor, arquitetura, documentacao, estrategia]
skill: tech-mentor-system-design/references/documentation
level: arquiteto
---

# Wardley Maps

## Contexto
Criados por Simon Wardley (2005), são mapas visuais que combinam **cadeia de valor** (o que o negócio precisa) com **evolução tecnológica** (quão madura é cada componente). Permitem tomar decisões estratégicas como: o que construir vs. comprar, onde inovar vs. commoditizar, e como o cenário vai mudar.

Diferente do C4 ou do ADR — que descrevem *o que existe agora* — Wardley Maps ajudam a pensar *para onde ir*.

## Estrutura de um Wardley Map

```
Visibility ▲
(cadeia de  │
 valor)     │   Usuário
            │      │
            │   Necessidade
            │      │
            │   Componente A ──── Componente B
            │                         │
            │                   Componente C
            │
            └─────────────────────────────────►
                Genesis    Custom    Product    Commodity
                                              (Evolution)
```

**Eixo Y (Visibility):** o quanto o componente é visível para o usuário final. O usuário está no topo. Componentes de infraestrutura ficam na base.

**Eixo X (Evolution):** estágio de maturidade do componente:
- **Genesis:** novo, incerto, diferenciador — construa
- **Custom:** feito sob medida — considere comprar
- **Product:** produto de mercado — compre ou use SaaS
- **Commodity:** utilitário (como eletricidade) — use serviço gerenciado

## Exemplo Prático — Startup de Pagamentos

```
Visibility
    ▲
    │  Usuário final
    │       │
    │  Checkout UX ──────── Regras antifraude (Genesis)
    │       │                       │
    │  Processador de pagamento (Product/Commodity)
    │       │
    │  Infraestrutura de rede (Commodity)
    │
    └─────────────────────────────────────────►
         Genesis    Custom    Product    Commodity
```

**Insight:** Antifraude está em Genesis → diferenciador competitivo → **construa internamente**. Processador de pagamento está em Commodity → **use Stripe/Adyen**, não construa.

## Como Criar um Wardley Map

1. **Defina o usuário e sua necessidade:** "usuário quer pagar em 1 clique"
2. **Liste a cadeia de valor:** o que é necessário para atender essa necessidade?
3. **Posicione na evolução:** para cada componente, onde ele está na maturidade?
4. **Identifique dependências:** conecte com setas
5. **Analise movimento:** o que vai se mover para commodity nos próximos 3 anos?

## Aplicações para Solutions Architect

| Decisão | Como o Wardley Map ajuda |
|---|---|
| Build vs. Buy | Commodity → compre. Genesis → construa |
| Onde inovar | Componentes em Genesis com alto valor para o usuário |
| Reduzir custo | Mova componentes Custom/Product para Commodity (managed services) |
| Risco estratégico | Dependência de fornecedor único em componente crítico |
| Roadmap técnico | Antecipe o movimento de componentes ao longo do eixo X |

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---|---|---|
| Visão estratégica | Conecta decisão técnica a impacto de negócio | Curva de aprendizado — poucos entendem o formato |
| Comunicação | Facilita conversa com C-level sobre tech debt | Subjetivo — posicionamento no eixo X é debatível |
| Planejamento | Identifica onde investir antes que o mercado force | Snapshot no tempo — precisa ser revisitado |

## Quando Usar / Quando Evitar

**Usar quando:**
- Decidindo make vs. buy em componentes estratégicos
- Planejando roadmap de 12-24 meses com impacto em arquitetura
- Apresentando decisões técnicas para stakeholders de negócio
- Avaliando dependências de fornecedores

**Evitar quando:**
- Sprint planning ou decisões táticas — é overhead
- O time não tem tempo para aprender o framework adequadamente

## Conceitos Relacionados
[[adr]] · [[c4-model]] · [[rfc]] · [[conways-law]]

---
*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-04-17*
