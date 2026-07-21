---
type: concept
title: "Camada de Aplicação vs. Camada de Modelo"
aliases: ["application layer llm", "camada de aplicação IA", "app layer vs model layer"]
date_created: 2026-07-21
date_updated: 2026-07-21
source_count: 1
tags: [mercado-de-ia, produto, camada-de-aplicacao, estrategia]
skill: tech-mentor-ai
status: stub
---

# Camada de Aplicação vs. Camada de Modelo

Tese de mercado: com a competição entre modelos frontier fechados e modelos [[wiki/concepts/mixture-of-experts|MoE]] open source cada vez mais equilibrada (ver [[wiki/concepts/corrida-preco-qualidade-llm]]), o modelo em si deixa de ser a principal fonte de vantagem competitiva para quem constrói produto. Quem atua na camada de aplicação — a integração, o produto, a orquestração em torno do LLM — consegue extrair valor real de negócio mesmo usando modelos que não são de ponta.

## Quando modelos grandes ainda importam

A tese não descarta modelos frontier: em padrões como *Dynamic Workflows*, um modelo grande e caro é ótimo para gerar o **plano** de execução, que depois é delegado a modelos baratos para executar os passos — resultado de alta qualidade com baixo custo agregado. A escolha do modelo, nesse caso, é por etapa da tarefa, não uma escolha única e fixa para toda a aplicação.

## Implicação de negócio

Se o modelo deixa de ser o diferencial (porque a concorrência já entrega qualidade comparável a custo menor — ver [[wiki/entities/moonshot-ai]], [[wiki/entities/deepseek]]), o lock-in em um único provedor de IA perde sentido estratégico. Decisores deveriam desenhar a arquitetura de forma a trocar de modelo com baixo atrito.

## Key Sources

- [[wiki/sources/kimi-k3-china-mercado-ia-open-source]]
