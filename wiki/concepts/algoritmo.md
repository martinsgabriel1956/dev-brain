---
type: concept
title: "Algoritmo"
aliases: ["algorithm", "propriedades do algoritmo"]
date_created: 2026-10-09
date_updated: 2026-11-16
source_count: 5
tags: [algoritmo, fundamentos, cs-fundamentals]
skill: cs-fundamentals
status: draft
---

# Algoritmo

Sequência **finita** e **precisa** de passos que transforma uma entrada em uma saída para resolver um problema. A linguagem de programação é só a ferramenta que traduz essa lógica para a máquina ([[wiki/sources/o-que-e-um-algoritmo-propriedades-pseudocodigo-sistemas-de-recomendacao]]).

## Quatro propriedades (segundo a fonte)

1. **Entrada** — dados recebidos para processar.
2. **Clareza e precisão** — cada instrução unívoca; o computador não deduz, executa.
3. **Finitude** — precisa terminar; loop infinito sem resultado é falha.
4. **Saída** — resultado esperado ao fim.

[external] Knuth (*TAOCP* vol. 1) acrescenta **efetividade** (cada passo é básico o bastante para ser executado de fato) e agrupa clareza como "definição precisa". Ressalva: serviços de longa duração (servidores) não terminam por desenho — a finitude vale por *requisição/tarefa*, não pelo processo inteiro.

## Analogia

Receita de bolo: ingredientes (entrada) → passos (misturar, bater, 180 °C por 40 min) → bolo (saída). "Um pouco de farinha até ficar bom" é vago demais para ser algoritmo.

## Relações

- Rascunhado como [[wiki/concepts/pseudocodigo]] ou [[wiki/concepts/fluxo-logico]] antes do código; ver [[wiki/concepts/traducao-logica-para-codigo]].
- Usa decisões e repetições: [[wiki/concepts/fluxo-de-controle]].
- Custo medido por [[wiki/concepts/big-o]]; catálogo em [[wiki/concepts/algoritmos-e-estruturas-de-dados]].
- Uso popular ("o algoritmo do TikTok") = [[wiki/concepts/sistema-de-recomendacao]].

## Na NLW #1 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-1-programacao-web-html-css-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]]: algoritmo "tem mais a ver com o passo a passo das coisas que você está fazendo", não com "aquele log de 10" da escola. Exemplo: acordar, lavar o rosto, escovar os dentes, tomar café.

## Na NLW #1, dia 3 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-3-itens-de-coleta-modal-pagina-de-resultados-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] escreve o passo a passo da seleção de itens em comentários antes de codar: verificar se está selecionado, tirar se estiver, adicionar se não estiver, atualizar o campo escondido. "Isso aqui chama-se algoritmo de programação." No fim: "primeiro foi uma ideia lógica pensada, escrita, e depois a gente só veio colocando em código".

## Na NLW #2, dia 1 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-1-programacao-web-html-css-proffy]], [[wiki/entities/mayk-brito|Mayk]] volta à rotina matinal e acrescenta o detalhe: o computador "não sabe aonde está o café" nem "o que é escovar os dentes", então o algoritmo tem que ser ensinado "de uma maneira muito detalhada".

## Na NLW #2, dia 3 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-3-formulario-dar-aulas-javascript-proffy]], o algoritmo ganha caminhos: "se estiver chovendo, você vai pegar um guarda-chuva [...] se estiver frio, você vai pegar uma jaqueta". Para Mayk, é a existência de opções que faz algo ser linguagem de programação, e HTML e CSS "não é programar de fato".

## Key sources

- [[wiki/sources/o-que-e-um-algoritmo-propriedades-pseudocodigo-sistemas-de-recomendacao]] — definição, quatro propriedades, receita de bolo
- [[wiki/sources/nlw-1-dia-1-programacao-web-html-css-ecoleta]]: rotina da manhã como algoritmo
- [[wiki/sources/nlw-1-dia-3-itens-de-coleta-modal-pagina-de-resultados-ecoleta]]: algoritmo em comentários antes do código
- [[wiki/sources/nlw-2-dia-1-programacao-web-html-css-proffy]]: NLW #2, dia 1: rotina matinal detalhada
- [[wiki/sources/nlw-2-dia-3-formulario-dar-aulas-javascript-proffy]]: NLW #2, dia 3: caminhos e condições
