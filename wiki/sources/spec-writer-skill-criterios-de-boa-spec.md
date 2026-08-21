---
type: source
title: "Spec Writer: Skill para Gerar Specs a Partir do PRD e os 7 Critérios de uma Boa Spec"
aliases: ["Spec Writer skill", "7 critérios de uma boa spec", "falseabilidade de specs"]
date_created: 2026-08-18
date_updated: 2026-08-18
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/spec-writer-skill-criterios-de-boa-spec.md
source_url: ""
author: "Não identificado — transcrição colada pelo usuário no chat, sem nome de canal/autor. Vocabulário (PRD → spec por feature, contexto passo a passo, demo ao vivo no Claude Code) é consistente com o estilo do curso [[wiki/sources/formacao-ia-devs-aula-04-agentes-planejamento|Formação IA para Devs]], mas os termos centrais desta fonte (\"Spec Writer\", \"gates determinísticos\", os 7 critérios de falseabilidade/comportamento/invariantes/edge cases/fronteira/inputs/decisões de negócio) não aparecem em nenhuma fonte já ingerida — sem correspondência suficiente para atribuir a uma entidade específica."
date_published: null
date_ingested: 2026-08-18
source_count: 0
tags: [spec-driven, tech-spec, prd, skills, context-engineering, qualidade-de-spec, ia-para-devs]
skill: tech-mentor-ai
status: stable
---

# Spec Writer: Skill para Gerar Specs a Partir do PRD e os 7 Critérios de uma Boa Spec

## TL;DR

Transcrição de demonstração ao vivo (Claude Code) de uma skill pessoal chamada **Spec Writer**, que converte uma feature de um [[wiki/concepts/prd-product-requirements-document|PRD]] existente numa [[wiki/concepts/tech-spec|tech spec]] estruturada por meio de 6 etapas (validar inputs → entrevista → sumarizar → gerar documento → validar a spec → escrever output). A fonte formaliza um framework de **7 critérios de qualidade de spec** — falseabilidade, comportamento (não implementação), invariantes, edge cases nomeados, fronteira/escopo explícito, entradas/restrições, decisões de negócio — usado como gate de validação na etapa 5 da skill. Reforça, com um exemplo concreto (login sem contexto suficiente vira redirect errado), a tese já central na wiki de que a IA é pura inferência e depende inteiramente do contexto fornecido pelo dev.

## Claims Principais

| Claim | Evidência | Confiança |
|---|---|---|
| Uma spec boa é falseável: cada afirmação deve ser verificável contra o output real ("sistema deve ser performático" vs. "P99 < 200ms sob 1000 req/s") | Exemplo direto dado pelo autor, contraste explícito entre afirmação vaga e mensurável | Alta — critério concreto e replicável, consistente com [[wiki/concepts/quality-gate]] |
| Spec deve descrever comportamento, não implementação — "aplicar desconto sobre um valor proporcionado", não "criar classe X.Y.Z com método apply" | Exemplo direto dado pelo autor | Alta — mesmo princípio já central em [[wiki/concepts/tech-spec]] ("O que NÃO Contém") |
| Specs maduras nomeiam invariantes (ex.: preço final nunca negativo) e edge cases explícitos (vazio, negativo, limite, concorrência) separadamente | Exemplos dados pelo autor com caso de cupom de desconto | Média-alta — é uma proposta de framework do autor, não uma citação de terceiros |
| Specs devem declarar fronteira/escopo explicitamente (o que está fora, ex.: "só BRL, reembolso é outro fluxo") | Exemplo dado pelo autor | Alta — reforça a distinção PRD (alto nível, sem tecnologia) vs. spec (granular, ainda sem nível de implementação) já documentada em [[wiki/concepts/prd-product-requirements-document]] |
| A skill Spec Writer roda em 6 etapas determinísticas: validar inputs, entrevistar o usuário, sumarizar, gerar o documento, validar contra os 7 critérios, escrever o output | Descrição direta do autor sobre a própria skill, com demonstração ao vivo (carregamento da skill, leitura do PRD e de docs existentes, escrita do arquivo) | Alta — comportamento observado na demo, não só declarado |
| Sem contexto suficiente, o agente preenche o vazio com a própria inferência — exemplo: pedir "implemente um login" sem especificar o redirect pós-sucesso resulta em um agente que não sabe redirecionar para o dashboard | Exemplo didático do autor | Alta — mesma tese central de [[wiki/concepts/context-engineering-harness]] e [[wiki/concepts/harness]] ("guias" antecipam comportamento) |
| A fonte gera dois arquivos a partir da spec — `spec` e `plan` — organizados sob um único contrato, e a execução acontece só depois | Descrição do fluxo observado na demo | Média — a fonte não detalha o conteúdo exato de `plan` além de mencionar que organiza a implementação junto com a spec |

## Conceitos Abordados

- [[wiki/concepts/prd-product-requirements-document]]
- [[wiki/concepts/tech-spec]]
- [[wiki/concepts/spec-driven-development]]
- [[wiki/concepts/agente-prd]]
- [[wiki/concepts/context-engineering-harness]]
- [[wiki/concepts/harness]]
- [[wiki/concepts/criterios-de-uma-boa-spec]] (novo)

## Entidades Abordadas

Nenhuma entidade identificável — autor não se apresenta por nome na transcrição fornecida.

## Observações / Contradições

Sem contradições com o que já está registrado na wiki. Esta fonte converge com [[wiki/concepts/spec-driven-development]] e [[wiki/concepts/tech-spec]] no mesmo modelo mental (PRD alto nível → spec por feature → execução), mas contribui dois elementos que nenhuma fonte anterior detalhava com este nível de granularidade:

1. **O framework explícito de 7 critérios de qualidade de spec** (falseabilidade, comportamento, invariantes, edge cases, fronteira, inputs/restrições, decisões de negócio) — até agora `tech-spec.md` listava "o que contém"/"o que não contém" uma tech spec, mas sem um critério operacional de *como avaliar se uma spec está boa o suficiente*. Criada página nova [[wiki/concepts/criterios-de-uma-boa-spec]] para isso.
2. **A skill "Spec Writer" com 6 etapas nomeadas**, incluindo uma etapa de validação explícita contra os 7 critérios antes do output — um caso concreto adicional ao lado de "TLC Spec Driven" (já documentada em [[wiki/concepts/spec-driven-development]] via [[wiki/sources/spec-driven-development-otimizando-contexto-agentes]]), mas com nome, etapas e critério de validação diferentes — não há evidência de que sejam a mesma skill.

## Perguntas Abertas

- Autor não identificado — sem nome de canal, curso ou pessoa na transcrição colada. Vale re-checar se uma fonte futura do mesmo material identifica o autor, para então linkar a uma entidade.
- A fonte menciona "gates determinísticos" como "a primeira coisa que eu falei" — referência a conteúdo anterior não incluído nesta transcrição (provavelmente parte de um vídeo/aula maior). Não há página `wiki/concepts/gates-deterministicos` ainda; avaliar se uma fonte futura com esse trecho anterior justifica criá-la, ou se o conceito já é coberto por [[wiki/concepts/quality-gate]] + [[wiki/concepts/sensores-vs-guias]].
- Conteúdo exato do arquivo `plan` gerado ao lado da spec não é detalhado além de "organiza o plano de implementação".

## Raw Quotes

> "A IA é inferência, ela não sabe o que você quer criar, ela não sabe como você quer criar, ela não sabe a melhor maneira de criar. A gente acha que ela sabe — ela não sabe."

> "Lembra da primeira coisa que eu falei: primeiro são gates determinísticos, e a segunda é contexto. O que a gente está fazendo aqui é basicamente alimentando o contexto."

> "A spec vai dizer o que é verdade, não o como fazer."

> "Se vocês usarem esse método de sete etapas que passei para vocês, vocês conseguem gerar uma skill exatamente com tudo que precisa uma spec para ser boa."
