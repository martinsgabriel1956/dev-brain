---
type: concept
title: "Capital de Tokens"
aliases: ["token capital", "capital computacional vs capital humano"]
date_created: 2026-07-16
date_updated: 2026-07-16
source_count: 2
tags: [capital-de-tokens, token-economics, custo-ia, roi-de-ia, organizacoes]
skill: tech-mentor-ai
status: draft
---

# Capital de Tokens

Expressão cunhada por Satya Nadella (CEO da [[wiki/entities/microsoft]]) para descrever o consumo de tokens de IA como um novo tipo de capital organizacional, análogo ao capital humano: assim como pessoas geram conhecimento e valor para uma empresa, o volume de tokens processados (infraestrutura + consumo de modelos) passa a ser tratado como um ativo equivalente de geração de valor.

## A Migração de Custo

A tese central é que o custo da indústria de software historicamente era majoritariamente **capital humano** (salários, contratação, retenção). Com a adoção de IA em escala, uma parcela crescente desse custo está migrando para **capital computacional** — GPUs, inferência, tokens processados por agente. Isso não substitui o capital humano, mas reconfigura onde o dinheiro da empresa é alocado.

## Relação com [[wiki/concepts/era-agentica]]

Na era agêntica, o custo por desenvolvedor deixou de ser dezenas de dólares/mês (autocomplete) para centenas ou milhares (agentes executando tarefas inteiras). O conceito de capital de tokens formaliza essa mudança: o orçamento que antes ia quase todo para folha de pagamento agora precisa contemplar uma linha de custo computacional que cresce junto com o [[wiki/concepts/paradoxo-de-jevons|paradoxo de Jevons]] — quanto mais barato o token, mais ele é consumido, e mais a conta total sobe.

## Relação com [[wiki/concepts/roi-de-ia]]

Tratar tokens como capital implica medir seu retorno com o mesmo rigor que se mede o retorno do capital humano — o que a maioria das organizações ainda não faz (ver [[learning-gap-organizacional]]). Sem essa disciplina de medição, o capital de tokens vira apenas um custo crescente sem contrapartida de valor rastreável.

## O "Paradoxo da Informação Invertida"

Em outro artigo (segunda menção na wiki a Nadella comentando sobre a economia de IA dentro de organizações), Satya Nadella descreveu o que chamou de **paradoxo da informação invertida** (reverse information paradox): entre os pontos que ele lista como importantes para uma organização estão manter traces de como a informação e os problemas são encontrados, evals sistemáticas (ver [[wiki/concepts/evals-sistematicas]]), "adapted weights" e "memory accumulates". [[wiki/sources/rfcs-grill-me-e-o-risco-da-preguica-no-vibe-coding]] cita isso como o ponto em que a organização constrói confiança entre capital humano e capital de tokens — reforçando a tese central desta página de que o capital de tokens precisa da mesma disciplina de medição que o capital humano já recebe.

## Key Sources

- [[wiki/sources/custo-real-ia-tokens-produtividade-demissoes]]
- [[wiki/sources/rfcs-grill-me-e-o-risco-da-preguica-no-vibe-coding]] — "paradoxo da informação invertida" de Nadella (traces, evals, adapted weights, memory accumulates)
