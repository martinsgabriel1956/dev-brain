---
type: concept
title: "FinOps para IA (Token FinOps)"
aliases: ["finops para ia", "token finops", "finops de ia", "governança de custo de ia"]
date_created: 2026-07-31
date_updated: 2026-07-31
source_count: 1
tags: [finops, token-economics, custo-de-ia, governanca, budget, metricas-de-valor]
skill: tech-mentor-ai
status: stub
---

# FinOps para IA (Token FinOps)

Especialização do [[wiki/concepts/finops|FinOps]] genérico de cloud para o consumo de tokens de LLM em times de engenharia — motivada pelo mesmo problema que gerou o [[wiki/concepts/token-maxing|token maxing]] corporativo: sem visibilidade e limite de consumo por pessoa/ferramenta, orçamentos anuais inteiros de IA são estourados em poucos meses (caso [[wiki/entities/uber]], que zerou o orçamento anual do ano em abril de 2026).

## Quatro Práticas

1. **Budget e limite por dev/ferramenta/período** — monitorar consumo de token e custo de cloud subjacente (ex.: AWS hospedando os modelos) separadamente, com teto configurável por semana/mês por desenvolvedor e por ferramenta. Sem essa granularidade, não há como identificar onde o consumo está concentrado antes do orçamento estourar.
2. **Métricas de valor, não dashboards de volume de token** — medir o efeito da IA no resultado de engenharia (frequência de deploy, bugs em produção, crash-free sessions, tickets atrasados por release) em vez de apenas quem consumiu mais tokens. Um dashboard de consumo sem essas métricas paralelas não distingue token gasto com valor entregue de token gasto em [[wiki/concepts/token-maxing|token maxing]] improdutivo.
3. **Classificação de dados por sensibilidade** — dado proprietário/estratégico/de cliente deveria rodar em modelo aberto self-hosted (nunca exposto a um modelo fechado de terceiros); dado commodity pode seguir via API de modelo frontier fechado. Motivado pela mesma preocupação levantada por [[wiki/entities/palantir-technologies]] sobre exposição do "alfa" do negócio a laboratórios de IA fechados.
4. **Ownership em prototipagem** — usar livremente qualquer API de modelo frontier na fase de protótipo, mas evitar estruturar toda a arquitetura do produto em torno de um único provedor de modelo — lock-in estrutural transfere ownership do negócio para o laboratório de IA.

## Origem do Conceito Nesta Wiki

Formulado como as "quatro dicas" de encerramento de [[wiki/sources/palantir-ceo-token-tax-nvidia-scam-ia]], em reação direta à crítica do CEO da Palantir ([[wiki/entities/palantir-technologies]]) ao modelo de cobrança por token da OpenAI e Anthropic. As mesmas quatro práticas aparecem, com nomenclatura e exemplos de código diferentes, na seção "FinOps para LLM" do material de referência de token economics do tech-mentor (budget por feature/tenant, anomaly detection de custo, model routing) — ver [[wiki/concepts/modelo-por-leverage-tarefa]] e [[wiki/concepts/roteamento-automatico-de-modelo]] para o lado de roteamento de modelo dessa mesma prática.

## Key Sources

- [[wiki/sources/palantir-ceo-token-tax-nvidia-scam-ia]]
