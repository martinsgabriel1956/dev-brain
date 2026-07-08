---
type: concept
title: "Segregação de Funções"
aliases: ["Segregation of Duties", "SoD", "Separation of Duties"]
date_created: 2026-07-03
date_updated: 2026-07-03
source_count: 1
tags: [segregacao-de-funcoes, sod, iso-27001, compliance, security, code-review]
skill: tech-mentor-security
status: draft
---

## Definição

Princípio de controle segundo o qual a pessoa que executa uma ação sensível não deve ser a mesma que tem autoridade para aprová-la ou finalizá-la sozinha. Na engenharia de software, a aplicação mais comum é: **quem escreve o código não deve poder fazer deploy em produção sozinho**. Corresponde ao controle **A.5.3** do Anexo A da [[wiki/concepts/iso-27001]].

## Por que existe

Evitar fraude e erro operacional — um único ponto de falha humana (intencional ou não) não deveria conseguir, sozinho, alterar produção sem nenhuma checagem independente.

## Implementação técnica

A prática padrão é o **pull request com aprovação obrigatória de outro dev** antes do merge/deploy — é a materialização técnica do controle A.5.3.

## A tensão real

Esse é um dos controles mais polêmicos na prática: em empresas e equipes pequenas, manter uma segregação estrita entre quem desenvolve e quem aprova/faz deploy pode ser difícil ou quase impossível — o time inteiro às vezes é a mesma pessoa ou um grupo muito reduzido. Isso levanta a questão de saber quando a segregação vira teatro de compliance (aprovação de PR por alguém sem tempo de revisar de fato) em vez de controle real.

## Key Sources

- [[wiki/sources/iso-27001-dicionario-programador]] — controle A.5.3, PR com aprovação como implementação técnica, tensão em times pequenos

## Conceitos Relacionados

[[wiki/concepts/iso-27001]] · [[wiki/concepts/compliance]] · [[wiki/concepts/code-review]]
