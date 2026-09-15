---
type: concept
title: "Output vs. Outcome (métricas de produtividade)"
aliases: ["output vs outcome", "metricas de output", "metricas de outcome", "volume vs valor"]
date_created: 2026-08-10
date_updated: 2026-09-15
source_count: 3
tags: [engineering-metrics, ia-produtividade, dora, space, goodharts-law]
skill: tech-mentor-leadership
status: draft
---

# Output vs. Outcome

**TL;DR:** Métricas de **output** medem o que o time devolve (linhas, commits, PRs, velocidade, volume); métricas de **outcome** medem o efeito no mundo (bugs em produção, incidentes, tempo de ciclo, facilidade de mudar o sistema). A IA é o tipo de ferramenta que **infla output independente de qualidade** — por isso medir output é enganoso justamente quando se usa IA.

## Por que a distinção importa mais com IA

Se você mede volume, a IA vai fazer o número subir — e a percepção acompanha: 95% dos devs se sentem mais produtivos, mesmo produzindo código de qualidade menor. É [[wiki/concepts/goodharts-law]] em ação: a métrica de atividade vira alvo e perde significado. No vocabulário do SPACE (ver [[wiki/concepts/dora-metrics]]), **Activity** sozinha é gamificável; o que vale é **Performance/outcome**.

## As perguntas de outcome que revelam a verdade

1. **Bug rate pós-deploy** — se a IA aumenta produtividade *e* qualidade, bugs após o deploy têm que **cair**. Se sobem, há problema.
2. **Ciclo de code review** — se o último PR levou mais de uma semana para mergear, o gargalo é o **processo**, não a pessoa; adicionar mais PRs piora. Ver [[wiki/concepts/paradoxo-da-aceleracao]].
3. **Facilidade de mudar o codebase** — o sistema **como um todo** (não só o módulo tocado) está mais fácil ou mais difícil de mudar?

## A pergunta-raiz

> Você está usando IA para escrever **mais** código ou **melhor** código?

São escolhas diferentes que produzem resultados diferentes — e as métricas de output não distinguem uma da outra.

## Fora do Contexto de IA: Tickets Fechados como Métrica de Output

[[wiki/sources/fatores-nao-tecnicos-codigo-ruim-bons-desenvolvedores-bernardo-lobato]] descreve a mesma distinção sem envolver IA: uma organização que avalia dev por "quantidade de tarefas entregues" está medindo output puro; a métrica de outcome equivalente seria redução de complexidade, boa gestão de dívida técnica e cobertura de testes. O mecanismo é idêntico ao caso de IA já documentado nesta página — medir só output cria incentivo racional para otimizar o número, não a qualidade real — mas aqui a causa é estrutura de avaliação da empresa, não ferramenta de IA. Ver [[wiki/concepts/fatores-nao-tecnicos-qualidade-de-codigo]] e [[wiki/concepts/goodharts-law]].

## Na Escala da Sociedade: Produtividade Também É Output, Não Outcome

[[wiki/sources/ia-produtividade-nao-reduz-trabalho-corrida-da-ia-profecia-autorrealizavel]] eleva a distinção desta página do nível de time de engenharia para o nível de sociedade: produtividade (output agregado) é o indicador certo do ponto de vista da acumulação de capital, mas não necessariamente do ponto de vista do bem-estar social (outcome). A fonte questiona diretamente se "tempo economizado" e "produtividade" são os melhores indicadores quando o objetivo real seria bem-estar e construção de conhecimento — não apenas volume de trabalho entregue. É a mesma estrutura de raciocínio desta página (medir o número errado porque é mais fácil de medir), aplicada fora do contexto de engenharia de software.

## Conceitos Relacionados

[[wiki/concepts/goodharts-law]] · [[wiki/concepts/dora-metrics]] · [[wiki/concepts/paradoxo-da-aceleracao]] · [[wiki/concepts/roi-de-ia]] · [[wiki/concepts/code-review]]

## Key Sources

- [[wiki/sources/paradoxo-da-aceleracao-ia-produtividade-metricas]]
- [[wiki/sources/fatores-nao-tecnicos-codigo-ruim-bons-desenvolvedores-bernardo-lobato]] — caso sem IA: tickets fechados/deadline cumprido como métrica de output que não captura qualidade
- [[wiki/sources/ia-produtividade-nao-reduz-trabalho-corrida-da-ia-profecia-autorrealizavel]] — mesma distinção elevada ao nível de sociedade: produtividade como output vs. bem-estar como outcome
