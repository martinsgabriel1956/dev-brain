---
type: concept
title: "Quality Gate"
aliases: ["quality gates", "portão de qualidade", "análise estática em pull request"]
date_created: 2026-07-16
date_updated: 2026-07-16
source_count: 1
tags: [quality-gate, linter, analise-estatica, clean-code, modularizacao, ia]
skill: tech-mentor-ai
status: stub
---

# Quality Gate

Conjunto de regras automatizadas (linter, análise estática, limites estruturais) que um pull request precisa passar antes de ser mergeado. Diferente de uma [[wiki/concepts/rfc-request-for-comments|RFC]] — que define o que deve ser feito antes de codar — o quality gate valida o que foi de fato produzido, incluindo código gerado por IA.

## Quality Gate Forçando Clean Code em Código Gerado por IA

[[wiki/sources/rfcs-grill-me-e-o-risco-da-preguica-no-vibe-coding]] argumenta que quality gates com **limites estruturais** — tamanho máximo de função, quantidade de funções por arquivo, quantidade de linhas por arquivo, percentual aceitável de duplicação — não servem só para barrar código ruim: eles mudam o comportamento da própria IA durante a geração. Ao limitar o tamanho de uma função ou arquivo, a IA é forçada a pensar em como modularizar o projeto para respeitar o limite, em vez de gerar um bloco monolítico que só depois seria refatorado.

**Caso prático citado (app code.persua.com):** ao pedir para a IA modularizar um app por "flavor" (variante de build), o processo passou por etapas sucessivas — primeiro modularização com `if`s em runtime (trechos de código não executados dependendo do flavor buildado), depois questões de build mais finas: desabilitar renderização de componentes não usados, desabilitar arquivos/pacotes/assets por flavor para reduzir o tamanho final do build, e inspecionar o artefato final para verificar compliance com as regras de modularização definidas.

## Quality Gate Não Substitui Entendimento do Projeto

A mesma fonte é explícita sobre o limite dessa prática: **"tu não pode só ter agentes pra revisar, só ter agentes pra testar, só ter linter [...] se tu deixar o entendimento do teu próprio projeto ir por água abaixo."** Quality gates, testes automatizados e linters rodando em paralelo garantem qualidade objetiva e mensurável, mas não substituem o dev entender as regras que a IA colocou no sistema — para isso, a fonte recorre à skill [[wiki/concepts/skills-agente|Grill Me]] como complemento, não como substituto.

## Key Sources

- [[wiki/sources/rfcs-grill-me-e-o-risco-da-preguica-no-vibe-coding]]
