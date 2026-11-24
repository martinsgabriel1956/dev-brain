---
type: concept
title: "Escolha de gráfico (gráficos coerentes)"
aliases: ["gráficos coerentes", "tipo de gráfico", "qual gráfico usar", "chart choice", "pizza vs barras"]
date_created: 2026-11-24
date_updated: 2026-11-24
source_count: 1
tags: [visualizacao-de-dados, graficos, dashboard, grafico-de-pizza, grafico-de-linha, grafico-de-barras, tomada-de-decisao]
skill: ux-ui-mentor
status: stub
---

# Escolha de gráfico (gráficos coerentes)

Escolher o tipo de gráfico pela pergunta que os dados respondem. Para [[wiki/entities/nasser|Násser]], "cada gráfico [...] vai servir para poder comparar uma informação determinada" ([[wiki/sources/frontpush-dashboards-principios-parte-1]]).

## Na aula

- **Pizza para porcentagem:** "tantos por cento das nossas vendas são destinadas a tal setor", para ver onde as vendas se concentram e decidir onde investir.
- **Linha para tempo:** meses no eixo, picos e quedas, cruzados com datas comemorativas ("por que que no dia das mães a minha empresa vende mais?").
- **Comparação:** uma segunda linha sobreposta nos mesmos meses, com contraste entre as duas, e filtros nos gráficos para decidir.
- Promete um documento do [[wiki/entities/material-design|Material Design]] em que "de acordo com [...] a escala do número [...] o gráfico muda".

## O que a referência diz

`[skill: ux-ui-mentor]` A referência `dados-dashboards.md`:

| Pergunta | Gráfico |
|---|---|
| Como X muda no tempo? | Linha |
| Comparar categorias | Barras |
| Composição de um todo | Pizza (máx. 5 fatias), donut ou barra empilhada |
| Relação entre duas variáveis | Dispersão |
| Distribuição | Histograma, box plot |
| Progresso até uma meta | Gauge, barra de progresso |

- **Cleveland & McGill (1984):** posição em escala comum (barras) é lida com mais precisão que ângulo (pizza) ou área. Trocar pizza por barras "quase sempre melhora a precisão de leitura"; pizza só para 2 ou 3 categorias bem diferentes. Isso contradiz o "faria pouco sentido [...] em barras" da aula.
- **Armadilhas:** pizza com muitas fatias, eixo Y que não começa em zero, dois eixos Y, 3D.
- **Muitas séries:** em vez de várias linhas sobrepostas, *small multiples* (Tufte).
- **Cor:** nunca só a cor para distinguir séries; combinar com padrão (sólida × tracejada) ([[wiki/concepts/cor-semantica]]).

Ver [[wiki/concepts/dashboard]], [[wiki/concepts/patterns-de-dashboard]] (cards e gráficos).

## Key Sources

- [[wiki/sources/frontpush-dashboards-principios-parte-1]]: pizza, linha, linhas sobrepostas, filtros
