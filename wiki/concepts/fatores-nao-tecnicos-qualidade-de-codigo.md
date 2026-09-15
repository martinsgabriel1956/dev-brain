---
type: concept
title: "Fatores Não Técnicos na Qualidade de Código"
aliases: ["por que bons devs escrevem código ruim", "código ruim não é sempre dev ruim", "4 fatores de código ruim"]
date_created: 2026-09-15
date_updated: 2026-09-15
source_count: 1
tags: [tech-debt, carreira, code-review, contexto-organizacional, incentivos, mentoria]
skill: tech-mentor-leadership
status: draft
---

# Fatores Não Técnicos na Qualidade de Código

**TL;DR:** Código-fonte não é produzido no vácuo — é resultado das condições em que o desenvolvimento acontece. A simplificação "código ruim = dev ruim" (e suas variantes: "arquitetura ruim = arquiteto ruim", "muita dívida técnica = time negligente") ignora que mesmo profissionais excelentes entregam código abaixo do próprio potencial sob certas condições. Quatro fatores recorrentes explicam esse gap.

## Os Quatro Fatores

1. **Pressão de prazo** — a solução ideal levaria X tempo, o negócio exige menos. A decisão de cortar caminho (menos testes, abstração inadequada, duplicação) pode ser racional dada a restrição — desde que a solução ideal seja registrada como dívida técnica a resolver depois. Ver [[wiki/concepts/quadrante-de-fowler]] e [[wiki/concepts/tech-debt-como-ferramenta]].
2. **Contexto do projeto** — código legado, dependências externas, decisões anteriores, limitação de infraestrutura, contratos de API que não podem ser quebrados. O que "dá para entregar" é limitado pelo que o sistema permite, não pelo que o dev sabe fazer. Ver [[wiki/concepts/contexto-organizacional-para-arquitetura]] e [[wiki/concepts/julgar-codigo-fora-de-contexto]].
3. **Conhecimento incompleto e o fator tempo** — mesmo bons profissionais têm lacunas fora da própria área principal (ex.: transportar padrões idiomáticos de uma linguagem para outra onde não se encaixam). O próprio código do passado pode parecer pior visto de hoje — evidência de aprendizado, não de incompetência retroativa.
4. **Incentivos organizacionais** — se a empresa recompensa fechar tickets e cumprir deadline sem avaliar qualidade, e não recompensa redução de complexidade/dívida técnica/cobertura de testes, até bons profissionais racionalmente otimizam para o que é medido. Instância não nomeada da [[wiki/concepts/goodharts-law|Lei de Goodhart]] — ver também [[wiki/concepts/output-vs-outcome]].

## O Erro Nos Dois Extremos

- **Extremo 1 (o que este framework corrige):** julgar código ruim como prova de incompetência do dev, ignorando o contexto real de produção.
- **Extremo 2 (o que este framework não é licença para fazer):** normalizar qualquer código ruim como "culpa do contexto" — isso já é parte do problema, não da solução.

O ponto de equilíbrio: reconhecer quando se está tomando dívida técnica **conscientemente**, e tratar essa consciência como um ato de disciplina — registrar o tradeoff no backlog, explicar por que a decisão foi tomada daquele jeito — em vez de deixar o problema implícito para o futuro. Isso é exatamente a fronteira entre debt Prudente+Deliberado e os outros três quadrantes de [[wiki/concepts/quadrante-de-fowler]], e a mesma disciplina descrita na seção "Hábito Prático: Linkar Ticket ao Código" de [[wiki/concepts/tech-debt-como-ferramenta]].

## Relacionado

[[wiki/concepts/quadrante-de-fowler]] · [[wiki/concepts/tech-debt-como-ferramenta]] · [[wiki/concepts/contexto-organizacional-para-arquitetura]] · [[wiki/concepts/julgar-codigo-fora-de-contexto]] · [[wiki/concepts/goodharts-law]] · [[wiki/concepts/output-vs-outcome]] · [[wiki/concepts/code-review]] · [[wiki/concepts/boy-scout-rule]]

## Key Sources

- [[wiki/sources/fatores-nao-tecnicos-codigo-ruim-bons-desenvolvedores-bernardo-lobato]] — fonte de origem do framework de quatro fatores
