---
type: concept
title: "Começar no Relacional e Adicionar Peças Quando o Problema Aparecer"
aliases: ["maturidade é começar simples","problema com nome e sobrenome","relacional primeiro"]
date_created: 2026-10-05
date_updated: 2026-10-05
source_count: 1
tags: [arquitetura, banco-de-dados, yagni, tomada-de-decisao, maturidade]
skill: tech-mentor-data
status: stub
---

# Começar Simples, Adicionar Peça Quando Doer

Conclusão de [[wiki/sources/cinco-tipos-de-armazenamento-de-dados-qual-usar-codigo-fonte-tv]]: "maturidade muitas vezes é começar com o bom e velho banco relacional e adicionar as outras peças quando o problema aparecer de verdade — **quando chega com nome e sobrenome**". Loja pequena pode ficar com produtos no relacional, busca do próprio banco e tarefas simples (o apresentador ainda assim usaria cache no começo). Cada tecnologia nova custa instalação, configuração, monitoramento, backup, segurança, aprendizado e **mais um jeito de falhar**.

Variante específica de [[wiki/concepts/yagni]] e [[wiki/concepts/over-engineering]] para dados; paralelo com [[wiki/concepts/monolith-first]] e [[wiki/concepts/cargo-cult-tecnologico]] (escolher "o que a gigante usa"). Cuidado do mesmo vídeo: começar no relacional ≠ usá-lo para tudo (sessão, log, fila improvisada) quando o problema já apareceu. Ver [[wiki/concepts/persistencia-poliglota]].

## Key Sources

- [[wiki/sources/cinco-tipos-de-armazenamento-de-dados-qual-usar-codigo-fonte-tv]]
