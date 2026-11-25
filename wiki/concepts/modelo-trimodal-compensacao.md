---
type: concept
title: "Modelo Trimodal de Compensação"
aliases: ["trimodal compensation", "tres tiers salario tech", "trimodal nature"]
date_created: 2026-04-29
date_updated: 2026-11-25
source_count: 5
tags: [compensacao, salario, carreira, mercado, tier, trimodal]
skill: tech-mentor-leadership
status: stable
---

## TL;DR

O mercado de tech não tem uma distribuição salarial uniforme — tem três distribuições distintas com seus próprios centros de gravidade. A mesma posição pode pagar 2–4x mais dependendo do tier da empresa. Desenvolvido por Gergely Orosz em 2021 com dados da Holanda, validado globalmente.

## Os Três Tiers

| Tier | Tipo | Benchmark |
|---|---|---|
| **1** | Empresas locais tradicionais | Sites públicos de salário (Glassdoor, Payscale) |
| **2** | Startups/scaleups VC-funded | Acima do mercado local, equity em startup |
| **3** | Big Tech, hedge funds, scaleups globais | Competição global por talento, RSU significativo |

## Por que a Maioria não Sabe que Existe

Sites de benchmark capturam a mediana — que é Tier 1. Tier 3 é minoria em volume, quem ganha bem não compartilha, e equity raramente é capturado. O resultado: a percepção pública do "salário de dev" é sistematicamente subestimada.

## A Regra Prática

A decisão de qual empresa trabalhar impacta mais a compensação do que a decisão de qual cargo ter. Um Senior em Tier 3 supera um Staff em Tier 1.

## Um Segundo Eixo: Linguagem/Stack, não só Tier de Empresa

O modelo trimodal explica a variação por *tier de empresa*, mas [[wiki/sources/golang-mercado-salarios-pesquisa-2024]] mostra um eixo independente: dentro do mesmo tier de empresa, a *linguagem/stack* também move a compensação, por causa de oferta e demanda de profissionais qualificados. Pesquisa salarial brasileira (Código Fonte TV, 2024) mostra Go pagando acima de Java em todos os níveis — maior gap no Sênior (~R$ 6.000/mês a mais). O mecanismo é o mesmo — mercado mais seleto/nichado paga prêmio — só que aplicado à raridade da stack, não ao tier da empresa. Ver [[wiki/concepts/ciclo-de-mercado-tech]].

## Relacionado

- [[equity-como-diferencial]] — equity é o principal separador entre tiers
- [[tier-de-empresas-tech]] — como identificar o tier de uma empresa
- [[wiki/concepts/ciclo-de-mercado-tech]] — o mecanismo de oferta/demanda por trás do prêmio de stacks de nicho

## Big Tech vs. média salarial de júnior em São Paulo

Na abertura do módulo Mapeando Vagas ([[wiki/sources/introducao-mapeando-vagas]]), a média salarial de um júnior em São Paulo aparece como "infinitamente mais baixa" que o que o [[wiki/entities/google]] paga a um júnior na mesma cidade, e as empresas que concorrem com Big Techs têm faixas "totalmente invisíveis" que não aparecem nas médias. É a tese do Tier 3 em versão brasileira, sem números.

## Versão brasileira, com números (aula bônus de Galego)

[[wiki/sources/aula-bonus-artigo-salarios-invisiveis-galego]] lê o artigo ([[wiki/sources/trimodal-compensacao-tech]]) e traduz os tiers para o Brasil, com números estimados pelo autor, sem fonte:

| Tier | Exemplo brasileiro | Sênior (mensal) |
|---|---|---|
| 1, mercado local | "agência de marketing do seu Zé" | ~R$ 6 mil |
| 2, topo do mercado local | Banrisul (o autor duvida do exemplo) | ~R$ 12 mil |
| 3, topo do mercado regional | [[wiki/entities/nubank]], Brex | R$ 30 mil ou mais (Brex "acima de 50 mil") |

A média de sênior no Brasil (~R$ 10 mil, segundo ele) não mostra a cauda. Exemplo extremo: L6 do Google no Brasil com TC de R$ 1,1 milhão no [[wiki/entities/levels-fyi]]. **Divergência:** o autor fala em 5x entre o topo e o Tier 1 e diz que Orosz "foi conservador"; o artigo fala em 2-4x.

## Key Sources

- [[wiki/sources/trimodal-compensacao-tech]]
- [[wiki/sources/golang-mercado-salarios-pesquisa-2024]]
- [[wiki/sources/introducao-mapeando-vagas]] — júnior em SP: média do mercado vs. Google; faixas "invisíveis" dos concorrentes de Big Tech
- [[wiki/sources/big-techs-salarios-vagas-processo-de-aplicacao]] — Google x Amazon no Brasil
- [[wiki/sources/aula-bonus-artigo-salarios-invisiveis-galego]] — versão brasileira com números estimados (R$ 6 mil × 12 mil × 30 mil+); diz 5x contra os 2-4x do artigo

## Exemplo em reais: Google x Amazon no Brasil (2026-11-16)

[[wiki/sources/big-techs-salarios-vagas-processo-de-aplicacao]]: anual de entrada no Brasil R$ 277 mil no Google x R$ 189 mil na Amazon (Levels.fyi). Mesmo dentro do tier de topo há diferença relevante entre empresas; o salário base da Amazon é "bem menor".
