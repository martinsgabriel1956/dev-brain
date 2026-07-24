---
type: concept
title: "MVP (Minimum Viable Product)"
aliases: ["mvp", "produto mínimo viável", "minimum viable product"]
date_created: 2026-04-29
date_updated: 2026-07-24
source_count: 4
tags: [projetos, produtividade, entrega, planejamento, carreira, startup]
skill: tech-mentor-leadership
status: stable
---

# MVP (Minimum Viable Product)

O menor conjunto de funcionalidades que (1) resolve o problema central e (2) pode ser entregue a um usuário real para validar a hipótese. Não é um produto incompleto — é um produto completo com escopo mínimo.

## O Que "Mínimo" Significa na Prática

**Mínimo não é:**
- Lista de features cortada aleatoriamente
- Produto bugado "pra sair logo"
- Protótipo não funcional

**Mínimo é:**
- Uma coisa que o usuário consegue usar do início ao fim
- Sem features que não provam a hipótese central
- Qualidade suficiente para não gerar atrito na validação

## Por Que Devs Falham no MVP

1. **[[concepts/scope-creep]]**: adicionam features antes de ter usuários
2. **[[concepts/perfeccionismo-em-devs]]**: ficam polindo o que já funciona
3. **[[concepts/planning-fallacy]]**: subestimam o tempo de cada "pequena adição"
4. **Automação prematura**: no framework [[concepts/lean-startup]], o erro simétrico é automatizar processos (pagamento, entrega) antes de validar que alguém quer o produto — um MVP de assinatura pode rodar inteiramente com Pix manual e mensagem de WhatsApp

## Regra Prática

> "Bom o suficiente para shippar > perfeito mas eternamente em dev."

Se o MVP não gera vergonha, está grande demais.

## MVP como Unidade do Ciclo Lean Startup

No [[concepts/lean-startup]], o MVP não é o produto final reduzido — é o artefato construído em cada volta do ciclo [[concepts/build-measure-learn]], com escopo de **uma única funcionalidade** por iteração, para gerar aprendizado real com o menor investimento possível.

## Estrutura Inicial a Serviço do MVP

O [[wiki/concepts/checklist-primeiro-dia-projeto]] propõe documentar a estrutura inicial do projeto num `.md` **antes** de codar, pensando explicitamente no MVP — evita tanto a gambiarra sem plano quanto o over-engineering para um produto que ainda não existe.
## MVP e Vibe Coding

MVPs e protótipos são o contexto onde [[wiki/concepts/vibe-coding]] entrega valor real: validar uma hipótese de negócio rapidamente, sem o custo de implementação manual completa. O risco não é usar vibe coding para validar — é confundir o MVP validado com um sistema pronto para produção sem revisão arquitetural, de segurança e de contexto de negócio. Ver [[wiki/sources/vibe-coding-limites-maturidade-profissional]].

## Ver Também

- [[concepts/scope-creep]] — inimigo principal do MVP
- [[concepts/dopamina-e-projetos]] — entrega do MVP gera dopamina real, não apenas antecipada
- [[concepts/lean-startup]] — metodologia onde o MVP é a unidade tática de validação
- [[concepts/build-measure-learn]] — ciclo iterativo que consome e refina o MVP
- [[wiki/concepts/checklist-primeiro-dia-projeto]] — sequência tática do dia 1 a serviço do MVP
- [[wiki/concepts/vibe-coding]] — ferramenta natural para construir MVPs rápido

## Key Sources

- [[sources/por-que-devs-nao-terminam-projetos]]
- [[sources/lean-startup-para-devs-mano-deivin]]
- [[wiki/sources/5-ou-6-dicas-para-projetos-novos]]
- [[wiki/sources/vibe-coding-limites-maturidade-profissional]] — MVP como um dos contextos onde vibe coding brilha
- [[wiki/sources/system-design-simulador-hotel-booking-replit]] — reforça a tese de lançar com monetização desde o dia um e escopo mínimo sendo exatamente a única funcionalidade pela qual alguém pagaria (o simulador em si, não uma tela de diagramação gratuita); o próprio autor admite em retrospecto ter violado essa regra ao incluir um "simulador de caos" no MVP inicial
