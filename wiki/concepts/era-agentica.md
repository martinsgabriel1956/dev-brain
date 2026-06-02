---
type: concept
title: "Era Agêntica"
aliases: ["agentic era", "era dos agentes", "agentes de ia em producao"]
date_created: 2026-05-31
date_updated: 2026-05-31
source_count: 1
tags: [era-agentica, agente-ia, token-economics, paradoxo-de-jevons, llmops]
skill: tech-mentor-ai
status: stable
---

# Era Agêntica

## TL;DR

Fase atual do desenvolvimento de IA onde agentes executam **tarefas inteiras** de forma autônoma — não apenas autocomplete ou sugestões. Isso muda fundamentalmente o modelo de custo: em vez de tokens por sugestão, são tokens por funcionalidade. A [[paradoxo-de-jevons|conta explode]] mesmo com tokens mais baratos.

## O que Mudou

| Antes (autocomplete) | Agora (era agêntica) |
|---------------------|----------------------|
| Sugestão de linha/função | Funcionalidade completa |
| Tokens por sugestão | Tokens por tarefa (muitas chamadas) |
| Dev aprova cada linha | Agente trabalha em loop, noite inteira |
| Custo previsível | Custo por resultado, imprevisível |
| Dezenas de $/dev/mês | Centenas a milhares de $/dev/mês |

## O Impacto no Custo

**CEO do GitLab** descreveu a escalada para os clientes:
> dezenas de dólares/dev/mês → centenas → indo para milhares

**Gartner:** 29% das empresas já gastam $200–500/dev/mês em tokens. Power users passam de **$2.000/mês**.

Goldman Sachs estima multiplicação de consumo por **24x até 2030** — o [[paradoxo-de-jevons]] em escala máxima.

## Mudanças de Modelo de Negócio Induzidas

- **GitHub:** congelou novas assinaturas do Copilot — modelo de uso ilimitado não fechava com o custo de agente
- **GitLab:** mudou a unidade de cobrança de *seat* (assento por dev) para *unidade de tarefa* — cobra pelo que o agente faz, não por quem tem acesso
- **Microsoft:** cancelou licenças internas do Claude Code por uso excessivo

Toda a indústria está reprecificando o acesso à IA porque o modelo de assinatura fixa não absorve o consumo agêntico.

## Implicações para Times de Desenvolvimento

Na era agêntica, a qualidade do **harness** (testes, cobertura, contexto, arquitetura) determina se o agente:

- **Amplifica** — propaga padrões sênior, aplica convenções consistentemente, escreve mais testes
- **Dispersa** — gera código sem padrão, cria débito técnico, desperdiça tokens em loops sem saída

Sem harness adequado, mais agente = mais custo sem mais valor. Com harness de qualidade, o [[roi-de-ia]] começa a aparecer.

## Relação com [[token-anxiety]]

A era agêntica é o contexto que tornou o [[token-anxiety]] um fenômeno de mercado, não apenas individual. A pressão de custo em nível organizacional (Uber, Microsoft, GitLab) reflete a mesma ansiedade de "quanto está me custando isso?" — agora no nível de board e CFO.

## Era Agêntica e CRUD Resolvido

A era agêntica tornou [[crud-resolvido|CRUD simples obsoleto como diferencial]]: qualquer dev gera um CRUD funcional em horas com IA. Isso fechou a porta de entrada do dev júnior e criou escassez de dev sênior — profissionais que consigam manter e evoluir os sistemas complexos que a IA gerou.

O diferencial na era agêntica não é velocidade de geração — é [[harness-de-qualidade]] e [[robustez-de-sistemas]].

## Era Agêntica na Escala do Dev Individual

Os níveis 5–7 da [[escala-maturidade-ia-dev]] são a materialização individual da era agêntica:

- **Nível 5 (Orquestrador):** agente navega, roda testes, corrige erros — você define a tarefa de alto nível
- **Nível 6 (Multi-agentes):** múltiplos agentes em paralelo; modelo mental de engineering manager
- **Nível 7 (Arquiteto):** define arquitetura e contratos; agentes constroem tudo

A maioria dos devs ainda opera nos níveis 1–2 — o que explica por que estudos medem apenas 20–30% de ganho enquanto a diferença real entre nível 2 e nível 4 é de ~5x.

## Key Sources

- [[wiki/sources/ia-custo-roi-bolha-ou-realidade]]
- [[wiki/sources/conteudo-tecnico-ia-robustez-sistemas]]
- [[wiki/sources/conteudo-tecnico-ia-hype-sistemas-robustos]]
- [[wiki/sources/escala-niveis-uso-ia-engenheiros]] — níveis 5–7 como materialização individual da era agêntica
