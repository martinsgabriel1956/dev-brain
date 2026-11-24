---
type: concept
title: "Modelagem de Dados"
aliases: ["data modeling", "modelagem relacional", "normalização"]
date_created: 2026-07-09
date_updated: 2026-11-24
source_count: 8
tags: [banco-de-dados, modelagem, normalizacao, indice, backend]
skill: tech-mentor-backend
status: stub
---

# Modelagem de Dados

Decidir como o mundo real vira estrutura no banco. Um pedido tem usuário, itens, pagamento, endereço, status — e a forma como essas entidades se relacionam determina o quanto o resto do sistema sofre depois.

## O tradeoff central

| Erro | Consequência |
|---|---|
| Modelar mal / pouco | Regra de negócio fica confusa, dados inconsistentes |
| Normalizar demais | Toda consulta envolve vários joins, complexidade cresce |

## Performance é parte da modelagem

Uma query mal servida por índice pode virar um full scan gigante; a mesma query com índice adequado encontra o dado em poucos passos. Quando um sistema fica lento, o primeiro lugar a olhar costuma ser: falta algum índice? As tabelas foram organizadas de um jeito que obriga o banco a ler dado de vários lugares?

## Em entrevista de system design

Em uma [[wiki/concepts/entrevista-system-design|entrevista de system design]], a expectativa não é modelagem profunda — é mostrar repertório: reconhecer que partes diferentes de um mesmo sistema podem pedir um RDBMS, um banco chave-valor ou um banco de busca (search), conforme o caso de uso de cada parte.

## Exemplo didático: simulador de supermercado como projeto de aprendizado de modelagem

Um simulador de supermercado é citado como projeto ideal para exercitar modelagem porque ações triviais para um humano (pegar um produto, passar no caixa) escondem perguntas nada óbvias para o computador: como saber que o produto ainda tem estoque, como impedir que dois clientes comprem o último item ao mesmo tempo, como calcular o total, como validar que um preço não é um erro. Construir o projeto não é "fazer um supermercado" — é ensinar o computador como um supermercado funciona. Ver [[wiki/concepts/projetos-fundamentais-para-aprender-a-programar]] para os outros dois projetos da mesma progressão (estado e algoritmos).

## Relação com outros conceitos

- [[wiki/concepts/database-transactions]] — depois de modelado, o dado precisa se manter correto sob concorrência
- [[wiki/concepts/cache]] — cache é a camada que se apoia em cima de uma modelagem já feita
- [[wiki/concepts/entrevista-system-design]] — modelagem de dados como sinal de repertório em entrevista
- Ver aprofundamento de índices, EXPLAIN ANALYZE e query optimization em `references/database-query-optimization.md` (tech-mentor-backend)

## Esquema Híbrido SQL + NoSQL

[[wiki/sources/anatomia-entrevista-system-design-bigtech]] descreve o padrão esperado em sistemas grandes: parte transacional (consistência forte) num banco SQL, parte de alto throughput/dados menos estruturados num NoSQL — com colunas SQL apontando para chaves em key-value stores (ex.: DynamoDB) ou para objetos em blob store (ex.: S3). Misturar bancos de propósitos diferentes no mesmo esquema é apresentado como sinal de domínio real, não de "escolher um banco só".

## Critério Prático para Escolher SQL vs. NoSQL: Existe Relação?

[[wiki/sources/system-design-entrevista-cinema-draw-io]] oferece um critério simples e verbalizável em entrevista: usar MySQL para a tabela de filmes (id, nome, categoria) "por motivos didáticos", mas reconhecer que, se filmes "não têm relação com outra coisa" no domínio real, um banco não relacional (MongoDB) seria uma escolha igualmente válida. Não substitui o esquema híbrido SQL+NoSQL de [[wiki/sources/anatomia-entrevista-system-design-bigtech]] acima — é um caso mais simples, de entidade isolada, sem relacionamento a modelar.

## Na NLW #2, dia 5 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-5-banco-de-dados-sqlite-proffy]], o Proffy é modelado em três tabelas (professor 1:N aula 1:N horário). Os horários viram inteiros para permitir `<=` e `>`, e a matéria vira um número que o servidor traduz com `getSubject`. Ver [[wiki/concepts/normalizacao-de-dados]].

## Do requisito à entidade (FrontPUSH)

Na [[wiki/sources/frontpush-dashboards-principios-parte-2|aula 05 do módulo de dashboards]], a modelagem sai dos requisitos: atores viram usuários, usuários e vendas viram entidades, atributos viram campos de formulário, e as relações (venda → comprador, funcionário) definem banco, formulário e filtros. Ver [[wiki/concepts/atributos-como-campos-de-formulario]].

## O modelo do DashClass

Na [[wiki/sources/frontpush-dashboards-levantamento-de-requisitos-dashclass|aula 06 do módulo de dashboards]]: user, venda e produtos (cursos). O modelo põe "id do comprador" no produto, o que é um muitos-para-muitos mal resolvido: falta a tabela de itens da venda e a matrícula do aluno no curso. Ver [[wiki/concepts/relacionamento-muitos-para-muitos]].

## Key sources

- [[wiki/sources/10-conceitos-fundamentais-backend]]
- [[wiki/sources/5-dicas-entrevistas-lousa-branca-system-design]]
- [[wiki/sources/anatomia-entrevista-system-design-bigtech]]
- [[wiki/sources/system-design-entrevista-cinema-draw-io]] — critério prático de escolha SQL vs. NoSQL baseado em existência de relação entre entidades
- [[wiki/sources/tres-projetos-para-aprender-programar]] — simulador de supermercado como projeto de aprendizado de modelagem de domínio
- [[wiki/sources/nlw-2-dia-5-banco-de-dados-sqlite-proffy]]: NLW #2, dia 5: proffys, classes, class_schedule
- [[wiki/sources/frontpush-dashboards-principios-parte-2]]: FrontPUSH, dashboards aula 05: entidades, atributos e relações a partir dos requisitos
- [[wiki/sources/frontpush-dashboards-levantamento-de-requisitos-dashclass]]: FrontPUSH, dashboards aula 06: três entidades e o que falta
