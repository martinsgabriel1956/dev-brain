---
type: concept
title: "Story Points"
aliases: ["Pontos de História", "Estimativa Relativa", "Story Point Estimation"]
date_created: 2026-07-28
date_updated: 2026-08-20
source_count: 3
tags: [agile, scrum, estimativa, engineering-management]
skill: tech-mentor-leadership
status: stable
---

# Story Points

**TL;DR:** Unidade de estimativa **relativa de complexidade**, não de tempo absoluto. Uma história de 5 pontos é ~2,5x mais complexa que uma de 2 pontos, não "5 horas" de trabalho. O valor numérico em si não importa — o que importa é a constância da escala e a tendência do time ao longo do sprint a sprint.

## Como Calibrar

1. Escolha uma história de referência que o time conhece bem.
2. Defina-a como um valor base (ex.: "3 pontos").
3. Todas as novas histórias são comparadas a ela, não estimadas em isolamento.

Escalas comuns usam Fibonacci (1, 2, 3, 5, 8, 13, 21) para forçar o time a admitir incerteza crescente — a distância entre 13 e 21 é grande de propósito, porque histórias "muito grandes" deveriam ser subdivididas, não estimadas com precisão falsa.

Times novos vão essencialmente **chutar** o valor inicial. Isso é esperado e correto — leva de 3 a 5 sprints para a métrica de [[wiki/concepts/story-points#velocity|velocity]] se estabilizar e virar ferramenta de previsão confiável. A escala em si é arbitrária (pode ser Fibonacci, números primos, "bananas e maçãs" — o time escolhe) — o que precisa se manter é o critério de comparação relativa.

## Velocity

**Velocity** é a média de pontos entregues por sprint. Depois que o time roda alguns sprints com a mesma composição, a velocity se estabiliza e permite previsão de prazo: "temos 120 pontos no backlog, velocity ~40/sprint → ~3 sprints".

Uma equipe saudável tende a aumentar sua velocity organicamente ao longo do tempo — desde que a composição do time não mude constantemente. Isso é a métrica revelando aprendizado real, não pressão externa.

## A Equivalência Implícita com Horas (Crítica)

[[wiki/sources/por-que-estimativas-de-software-falham-como-melhorar]] observa um padrão comum, não declarado formalmente pelo método: se uma sprint de duas semanas (80h de trabalho, considerando 40h/semana) comporta, digamos, 80 pontos no planejamento do time, existe uma equivalência implícita de **1 ponto ≈ 1 hora**, mesmo que a doutrina oficial negue que pontos meçam tempo. Isso explicaria por que, na prática, é comum duas tarefas de 1 ponto consumirem um dia inteiro (idas e vindas de revisão, bikeshedding, tempo de build/teste) — a discrepância entre "2 pontos" e "6h reais" raramente é admitida abertamente porque contraria a lógica declarada do sistema. Não é uma regra do framework Scrum, mas uma crítica empírica plausível ao *uso* comum do sistema — não contradiz a definição formal de complexidade relativa acima, mas alerta que na prática a calibração inicial do time frequentemente ancora, sim, em uma noção implícita de tempo.

## O Erro de Forçar um Número-Alvo

Quando um Scrum Master ou PO decide, sem consultar o time, que "o time precisa fazer 30 ou 40 pontos por sprint por pessoa" — o processo já está corrompido. Isso inverte a lógica da métrica:

- Story points deveriam **emergir** do processo de estimativa do time (via [[wiki/concepts/planning-poker]]) e refletir a complexidade real observada.
- Quando um número é imposto de cima para baixo, o time passa a inflar estimativas para "bater a meta" (ex.: dar 20 pontos a um CRUD de três horas) em vez de estimar com honestidade.
- Nesse ponto os pontos deixam de ser uma ferramenta de planejamento e viram uma métrica de exibição — o equivalente, em complexidade forçada, a manter o GitHub "verdinho" com commits vazios. Ver [[wiki/concepts/goodharts-law]].

Consequências observadas quando isso acontece:
- **Colaboração cai** — se o incentivo é "fechar meus pontos", ninguém quer gastar tempo ajudando colegas durante o sprint.
- **Jornadas de trabalho se estendem** (10h/dia, fins de semana) sem remuneração extra, para "bater" um número que nunca foi calibrado pelo time — sintoma de erro de planejamento, não de falta de esforço individual.

## O Gargalo Que Definiu a Métrica Pode Ter Mudado de Lugar

[[wiki/sources/engenharia-de-contexto-vs-prompt-engineering-gargalo-real-times-ia]] levanta um ponto anterior à discussão de como calcular velocity corretamente: story points, velocity e throughput foram definidos numa época em que o gargalo do time era a capacidade de uma pessoa **escrever código**. Se a IA move esse gargalo para outra etapa do ciclo (revisão, teste, homologação, aprovação), a régua usada para medir "quanto o time acelerou" pode já não capturar onde o ganho real está acontecendo — o que reforça, por um ângulo diferente, o motivo por que comparar velocity entre contextos distintos (aqui, antes/depois de IA) tende a ser enganoso. A fonte prefere não amarrar decisões de processo a essas métricas até elas serem redefinidas, argumento coerente com o mecanismo da [[wiki/concepts/goodharts-law|Lei de Goodhart]]: uma métrica desenhada para um gargalo antigo, virada meta, otimiza o número errado quando o gargalo já mudou.

A mesma fonte também questiona, por extensão, o timebox padrão de sprint (2 semanas): trata-o como meio (criar ritmo de feedback num mundo em que escrever código era caro), não como fim — e relata reduzi-lo experimentalmente (1 semana, ou até 3 dias em projetos menos complexos) sob o argumento de que manter a janela de feedback fixa enquanto a produção acelera só acumula trabalho não validado. Nenhum dado de resultado desse experimento é citado — ver [[wiki/sources/engenharia-de-contexto-vs-prompt-engineering-gargalo-real-times-ia]] para o open question sobre isso.

## Quando Usar / Evitar

**Usar:** planejamento de sprint, previsão de entrega baseada em velocity histórica, conversa estruturada sobre complexidade via [[wiki/concepts/planning-poker]].

**Evitar:** comparar velocity entre times diferentes (contextos e calibrações distintas tornam a comparação sem sentido); tratar pontos como horas; impor uma meta numérica de pontos por pessoa sem que ela tenha emergido do próprio time.

## Conceitos Relacionados

[[wiki/concepts/planning-poker]] · [[wiki/concepts/scrum-master]] · [[wiki/concepts/goodharts-law]] · [[wiki/concepts/user-stories]] · [[wiki/concepts/dora-metrics]]

## Key Sources

- [[wiki/sources/story-points-po-forcando-30-40-pontos-por-sprint]]
- [[wiki/sources/por-que-estimativas-de-software-falham-como-melhorar]] — crítica à equivalência implícita entre pontos e horas dentro de uma sprint
- [[wiki/sources/engenharia-de-contexto-vs-prompt-engineering-gargalo-real-times-ia]] — velocity/throughput definidos para um gargalo (escrever código) que a IA pode ter deslocado; experimento de reduzir o timebox de sprint quando a produção de código acelera
