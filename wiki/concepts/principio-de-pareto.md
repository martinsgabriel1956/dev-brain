---
type: concept
title: "Princípio de Pareto"
aliases: ["regra 80/20", "distribuição de Pareto", "80-20 rule"]
date_created: 2026-07-04
date_updated: 2026-11-19
source_count: 4
tags: [produtividade, priorizacao, carreira]
skill: tech-mentor-leadership
status: draft
---

# Princípio de Pareto

Heurística de que aproximadamente 80% dos resultados vêm de 20% dos esforços — a maior parte do valor gerado se concentra numa fração pequena das ações tomadas, e o restante das tarefas contribui de forma marginal.

## Não é sobre exatidão da métrica

O número exato (80/20 vs. 90/10 vs. 70/30) não importa. O que importa é o princípio: a distribuição de resultados **não é uniforme** entre as tarefas realizadas. Algumas poucas decisões e ações concentram a maior parte do impacto.

## Aplicação prática: identificar os 20%

Duas armadilhas comuns ao tentar aplicar o princípio:

- **Fazer uma tarefa bem feita não a torna importante.** Qualidade de execução é ortogonal a relevância da tarefa.
- **Uma tarefa exigir muito tempo não a torna importante.** Tempo investido não é proxy de valor gerado.

Sem entender essas duas distinções, é impossível sair da armadilha de confundir [[wiki/concepts/eficacia-vs-eficiencia|eficiência com eficácia]].

## A técnica de identificação: [[wiki/concepts/tecnica-do-ataque-cardiaco]]

Uma forma prática de encontrar os 20% que geram 80% do resultado é perguntar: "se eu só pudesse trabalhar duas horas por dia, no que eu trabalharia?" — e anotar a resposta. Tudo que não está na lista pertence aos 80% de esforço de baixo retorno.

## Relação com [[wiki/concepts/ativo-vs-produtivo]]

A maior parte da atividade que gera sensação de produtividade sem resultado real acontece justamente nos 80% de esforço marginal — daí a importância de identificar e proteger os 20% antes de preencher o tempo restante.

## Em interfaces: os 20% das funcionalidades

Uma aula de UI afirma que usuários "só utilizam 20% das funcionalidades" de sistemas cheios de funções, como argumento por [[wiki/concepts/simplicidade-visual|simplicidade]] ([[wiki/sources/elementos-da-interface-visao-geral-proposito-consistencia-simplicidade]]). `[external]` O número costuma vir do Standish Group (Jim Johnson, XP 2002): 7% das funções usadas sempre e 13% com frequência. Amostra de software customizado e dado muito repetido sem checagem; confiança baixa a média.

## Os "20% das funções" em interfaces

No curso de UI e interfaces web, o número aparece duas vezes, sem fonte: programas de gestão "com N funções" em que "usa-se em torno de 20% das funções implementadas" ([[wiki/sources/usabilidade-facilmente-tres-esferas-boas-praticas-auxilio-emergencial]]). O argumento é que a [[wiki/concepts/usabilidade]] poupa trabalho do dev ao cortar o que ninguém usa. `[external]` O dado costuma ser atribuído ao Standish Group (64% das funcionalidades raramente ou nunca usadas, 2002), de metodologia pouco documentada; confiança baixa como regra geral.

## 80-20 na performance web (FrontPUSH, otimização aula 06)

Em [[wiki/sources/frontpush-relatorio-pagespeed-imagens-render-blocking-dom-regra-80-20]]: "você consegue resolver 80% das coisas fazendo 20%. Grande parte disso é mídia"; o resto rende "30 milissegundos" e "não vale a pena mais". Vale para landing pages, onde mídia domina os bytes; em web app o gargalo costuma ser JavaScript, cujo custo de CPU cresce muito em celular lento.

## Key Sources

- [[wiki/sources/produtividade-falsa-vs-verdadeira]]
- [[wiki/sources/elementos-da-interface-visao-geral-proposito-consistencia-simplicidade]] — "20% das funcionalidades" como argumento de UI
- [[wiki/sources/usabilidade-facilmente-tres-esferas-boas-praticas-auxilio-emergencial]] — "usa-se em torno de 20% das funções" (sem fonte)
- [[wiki/sources/frontpush-relatorio-pagespeed-imagens-render-blocking-dom-regra-80-20]]: FrontPUSH, otimização aula 06: 80% resolvido pela mídia
