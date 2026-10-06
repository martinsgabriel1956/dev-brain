---
type: source
title: "DMV da Califórnia: IA para descobrir as regras de negócio de 6 milhões de linhas de COBOL"
aliases: ["dmv california cobol ia", "dxp dmv", "discovery de regras de negócio mainframe"]
date_created: 2026-10-06
date_updated: 2026-10-06
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/dmv-california-ia-descoberta-regras-negocio-mainframe-cobol.md
source_url: ""
author: "não identificado (canal não citado na transcrição)"
date_published: ""
date_ingested: 2026-10-06
source_count: 0
tags: [mainframe, cobol, modernizacao, legado, ia, analise-estatica, regras-de-negocio, human-in-the-loop, ibm]
skill: tech-mentor-ai
status: draft
---

# DMV da Califórnia: IA para descobrir as regras de negócio de 6 milhões de linhas de COBOL

## TL;DR

Antes de reescrever o sistema legado do [[wiki/entities/california-dmv]] (~6M de linhas de [[wiki/concepts/cobol]]/Assembly, ~2.500 programas, anos 70), o projeto DXP precisou **descobrir o que ele faz**. A IA entrou como acelerador de [[wiki/concepts/descoberta-de-regras-de-negocio-legado]]: análise estática determinística ([[wiki/entities/ibm-arc]]) restringe o LLM ([[wiki/entities/watsonx]]), que escreve as regras em linguagem humana; revisores técnicos e de negócio validam em ciclo ([[wiki/concepts/analise-estatica-como-ancora-de-llm]], [[wiki/concepts/human-in-the-loop]]). Discovery em 15 meses vs. ~5 anos manual (estimativa da [[wiki/entities/ibm]]). A IA **não reescreveu** o sistema; o projeto segue atrasado (go-live adiado, integradora demitida, nota vermelha de qualidade, término previsto 2029, US$ 767M).

## Key claims

1. **O gargalo da modernização é saber por que cada linha existe, não o tamanho do código** — evidência: 50 anos de regras acumuladas, parte do conhecimento perdido com aposentadorias. Ver [[wiki/concepts/descoberta-de-regras-de-negocio-legado]], [[wiki/concepts/conhecimento-perdido-em-legado]].
2. **Não se pede a um LLM para "traduzir COBOL para Java" de início**; primeiro se recupera o conhecimento embutido no código. Ver [[wiki/concepts/modernizacao-de-mainframe]].
3. **Pipeline: análise estática (ARC) → LLM (watsonx) → revisão técnica + revisão de negócio → realimentação.** O contexto restrito e determinístico "eliminou boa parte" das alucinações (afirmação do autor, sem métrica; ainda assim exigiu o ciclo humano). Ver [[wiki/concepts/analise-estatica-como-ancora-de-llm]], [[wiki/concepts/alucinacao-llm]].
4. **Ganho de tempo:** 5M de linhas varridas em 12 meses; discovery completo em 15 meses, contra ~60 meses da análise manual (estimativa inicial da IBM, citada pelo autor). Fonte de segunda mão, não verificada.
5. **A IA acelera a leitura; a validação é humana.** Quem decide se a regra está certa são os especialistas, com a pergunta certa. Ver [[wiki/concepts/human-in-the-loop]], [[wiki/concepts/ia-como-amplificador]].
6. **Modernização é lenta, cara e arriscada:** início formal em 2021, término previsto 2029, US$ 767M; contrato da integradora cancelado no fim de 2025; nota vermelha de qualidade em julho (órgão de acompanhamento). Ver [[wiki/entities/california-dmv]].
7. **Dependências e risco definem a ordem das ondas de migração** (ver [[wiki/concepts/ondas-de-migracao-por-risco-e-dependencia]]; relação com [[wiki/concepts/strangler-fig-pattern]] é **inferência minha**).
8. **Profissional de mainframe/COBOL continua essencial** por muitos anos (opinião do autor). Ver [[wiki/concepts/mercado-de-trabalho-mainframe-cobol]].

## Entities

[[wiki/entities/california-dmv]], [[wiki/entities/ibm]], [[wiki/entities/ibm-arc]], [[wiki/entities/watsonx]]

## Concepts

[[wiki/concepts/descoberta-de-regras-de-negocio-legado]], [[wiki/concepts/analise-estatica-como-ancora-de-llm]], [[wiki/concepts/conhecimento-perdido-em-legado]], [[wiki/concepts/ondas-de-migracao-por-risco-e-dependencia]], [[wiki/concepts/modernizacao-de-mainframe]], [[wiki/concepts/mainframe]], [[wiki/concepts/cobol]], [[wiki/concepts/human-in-the-loop]], [[wiki/concepts/alucinacao-llm]], [[wiki/concepts/engenharia-reversa]], [[wiki/concepts/teoria-do-programa-naur]], [[wiki/concepts/ia-como-amplificador]], [[wiki/concepts/ondas-de-modernizacao-tecnologica]]

## Open questions / lacunas

- Como se mediu a taxa de acerto/alucinação do watsonx? A fonte só diz "eliminou boa parte".
- Ano do go-live truncado no áudio ("janeiro de 202…"); provável 2027, **não confirmado**.
- A estimativa de 5 anos (IBM) e os números do projeto (US$ 767M, nota vermelha) vêm do autor; **[external, não verificado na web]**.
- Nome da integradora cancelada e do órgão revisor não citados.
- Como tratar regra que existe no código mas é bug/obsoleta (o código é "a verdade", mas nem toda verdade é desejada)? Não abordado.

## Contradições / tensões com a wiki

- Sem contradição direta. Nuance: [[wiki/concepts/modernizacao-de-mainframe]] registra a tendência de **integrar** em vez de substituir; o DXP é caso de **substituição** gradual, com os mesmos riscos que justificam a tendência.

## Quotes

> "O problema não era ter 6 milhões de linhas de código; o problema era saber por que cada uma daquelas linhas estava ali."

> "A IA ... localiza e organiza coisas com uma velocidade que nenhuma equipe humana conseguiria fazer, mas ainda depende de pessoas fazendo a pergunta certa do jeito certo e com capacidade de verificar se aquela resposta está fazendo sentido."
