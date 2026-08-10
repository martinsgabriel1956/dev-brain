---
type: concept
title: "LTV e CAC"
aliases: ["lifetime value", "custo de aquisição de cliente", "unit economics", "LTV/CAC"]
date_created: 2026-07-09
date_updated: 2026-08-05
source_count: 3
tags: [ltv, cac, growth, unit-economics, saas, retencao, graph-engineering, loop-engineering]
skill: tech-mentor-leadership
status: draft
---

# LTV e CAC

LTV (lifetime value) é quanto um cliente médio gera de receita durante todo o tempo em que permanece pagando. CAC (custo de aquisição de cliente) é quanto custa converter um novo cliente pagante. A relação entre os dois — não o faturamento bruto isolado — determina se investir em aquisição vale a pena.

## Por Que Conhecer o LTV Antes do CAC

Investir em aquisição (tráfego pago, comissão para afiliados/microinfluenciadores) sem saber o LTV é apostar às cegas: não há como saber quanto vale pagar por uma conversão. Em [[wiki/sources/como-vender-um-saas-sem-audiencia]], o autor descreve o LTV do seu produto (~€34, equivalente a ~3 meses de assinatura) e usa esse número para calibrar quanto pagar de comissão por conversão a microinfluenciadores — nesse caso, dar o primeiro mês grátis ("custo de aquisição" efetivo) sabendo que o usuário médio fica 3 meses.

## Erro Comum — Faturamento Bruto Sem Custos Reais

Um padrão de erro citado na fonte: ver R$ 50.000 de faturamento, subtrair só os custos óbvios de aquisição (ex.: R$ 30.000 em Google Ads + R$ 5.000 em infra) e concluir que sobram R$ 15.000 de lucro — ignorando impostos, contador, assinaturas de ferramentas e outros custos fixos. O ponto central: sem saber o LTV real, não se deve escalar investimento em aquisição — usar aquisição paga inicialmente apenas para *validar* o custo de conversão, não para crescer de forma agressiva.

## Aquisição "Orgânica Sintética"

Custo de aquisição não se resume a tráfego pago rastreável. Microinfluenciadores falando de um produto de forma orgânica (sem link ou cupom rastreável) também têm custo — seja em cachê fixo, seja em comissão por conversão estimada — e deveriam entrar no cálculo de CAC mesmo sem conversão diretamente trackável.

## Relação com Retenção

LTV está diretamente ligado a por que o usuário continua pagando. Um produto cuja funcionalidade-core tem uso recorrente (ex.: reuniões de trabalho contínuas) tende a ter LTV mais alto que um produto de uso pontual (ex.: uma ferramenta usada só durante a busca de um emprego) — ver [[wiki/concepts/produto-vendivel-desde-o-dia-zero]] para a discussão de como escolher essa funcionalidade-core.

## Por Que Um Agente Não Deve Otimizar CAC Isoladamente

[[wiki/sources/graph-engineering-do-loop-ao-grafo]] usa exatamente essa relação para argumentar contra loops de IA com uma única métrica-alvo: um agente rodando em loop para reduzir o custo de aquisição de uma campanha (CAC/CPI) pode conseguir baixar esse custo enquanto aumenta o churn — porque o tráfego mais barato trouxe leads mais frios ou fora do público-alvo. O churn maior derruba o LTV, o que por sua vez invalida o próprio ganho de CAC (não compensa adquirir barato um cliente que sai rápido demais). A fonte usa esse exemplo para defender que otimização de métricas de negócio via IA precisa considerar CAC, churn e LTV como nós/relações de um mesmo [[wiki/concepts/grafo-como-abstracao-de-agentes|grafo]], não como alvos isolados de loops independentes.

## Relevância para Arquitetura de Software

[[wiki/sources/pos-graduacao-arquitetura-software-vale-a-pena]] cita CAC e LTV (junto com churn e ROI) como conhecimento de negócio que um arquiteto de software precisa ter — não para calcular esses números, mas para entender o vocabulário e a motivação por trás de decisões técnicas que vêm do negócio (ex.: um aumento reportado de churn pode exigir investigação de performance/disponibilidade da arquitetura).

## Key Sources

- [[wiki/sources/como-vender-um-saas-sem-audiencia]]
- [[wiki/sources/pos-graduacao-arquitetura-software-vale-a-pena]]
- [[wiki/sources/graph-engineering-do-loop-ao-grafo]] — CAC/churn/LTV como exemplo de por que um loop de IA de métrica única é insuficiente
