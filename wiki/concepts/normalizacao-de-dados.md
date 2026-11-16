---
type: concept
title: "Normalização de dados"
aliases: ["normalização", "normalization", "formas normais", "primeira forma normal", "1FN", "3FN"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 1
tags: [banco-de-dados, modelagem, normalizacao, relacional, sql]
skill: tech-mentor-data
status: stub
---

# Normalização de dados

Organizar as tabelas para que cada fato fique guardado num lugar só. Os dados que se repetiriam em várias linhas vão para uma tabela própria, ligada por uma [[wiki/concepts/chave-estrangeira|chave estrangeira]] à [[wiki/concepts/chave-primaria|chave primária]] da outra. Com isso, atualizar o nome de um professor é mudar uma linha, e não todas as aulas dele, e não há como duas cópias ficarem diferentes (anomalia de atualização).

As formas normais formalizam isso. Na prática, as que mais aparecem são três:

- **1FN:** um valor por célula, sem listas dentro de uma coluna.
- **2FN e 3FN:** cada coluna depende da chave inteira, e só da chave.

O caminho inverso, duplicar de propósito para ler mais rápido, é a [[wiki/concepts/desnormalizacao]]. Ver também [[wiki/concepts/modelagem-de-dados]] e [[wiki/concepts/relacionamento-muitos-para-muitos]].

`[skill: tech-mentor-data]` Em OLTP, normalize por padrão e desnormalize com motivo medido. Em analytics, modelos como o star schema desnormalizam as dimensões de propósito.

## Na NLW #2, dia 5 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-5-banco-de-dados-sqlite-proffy]], o Proffy ganha três tabelas, `proffys`, `classes` e `class_schedule`, ligadas por `proffy_id` e `class_id`. A pergunta "por que eu não cadastro tudo numa tabela só?" recebe a resposta da normalização, sem o nome: nome, avatar, WhatsApp e bio se repetiriam "10, 20, 30 vezes", e "depois eu vou querer atualizar o nome do professor só". As ligações ficam sem `REFERENCES`, então o banco não garante que uma aula aponte para um professor existente. A [[wiki/sources/nlw-1-dia-5-banco-de-dados-sqlite-cadastro-pesquisa-ecoleta|NLW #1]] explicou a mesma ideia (clientes e estados), mas guardou os itens numa coluna de texto, contra a 1FN.

## Key sources

- [[wiki/sources/nlw-2-dia-5-banco-de-dados-sqlite-proffy]]: três tabelas para não repetir os dados do professor
