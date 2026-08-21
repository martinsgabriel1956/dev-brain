---
type: source
title: "Código Espaguete (Wikipédia) — incl. Big Ball of Mud"
aliases: ["spaghetti code wikipedia", "big ball of mud", "wikipedia spaghetti code"]
date_created: 2026-08-14
date_updated: 2026-08-14
source_count: 0
tags: [code-espaguete, anti-patterns, big-ball-of-mud, arquitetura, entropia-de-software, goto, legado]
skill: tech-mentor-backend
status: draft
source_file: /home/nemomartins/Documentos/new/dev-study/raw/codigo-espaguete-wikipedia.md
source_url: https://en.wikipedia.org/wiki/Spaghetti_code
author: "Wikipédia (colaborativo, CC BY-SA)"
date_published: 
date_ingested: 2026-08-14
---

# Código Espaguete (Wikipédia) — incl. Big Ball of Mud

## TL;DR

Verbete da Wikípédia (traduzido para pt-BR em `raw/`) que define **[[wiki/concepts/code-espaguete|código espaguete]]** como código-fonte cujo **[[wiki/concepts/fluxo-de-controle|fluxo de controle]]** é convoluto e difícil de entender — a metáfora do prato de macarrão "torcido e emaranhado". O texto faz três movimentos úteis: (1) traça a **história** do termo (Hopkins 1972, Conway 1978, e a etimologia física de [[wiki/entities/richard-hamming|Richard Hamming]], em que a bagunça nasce literalmente de *saltos* `goto` empilhados na memória para corrigir bugs); (2) cataloga uma família de **[[wiki/concepts/anti-pattern|anti-padrões]]** por analogia de massas — [[wiki/concepts/lasagna-code|lasagna code]] (camadas entrelaçadas), [[wiki/concepts/ravioli-code|ravioli code]] (classes boas isoladamente, design ruim no todo); e (3) formaliza a **[[wiki/concepts/big-ball-of-mud|Big Ball of Mud]]** — sistema sem arquitetura perceptível, de [[wiki/entities/brian-foote|Brian Foote]] e [[wiki/entities/joseph-yoder|Joseph Yoder]] (1997) — como o estado macroarquitetural para onde o código espaguete escala. A tese de fundo conecta com [[wiki/concepts/entropia-de-software|entropia de software]]: a bagunça é o resultado *default* de pressão de negócio, turnover e reparos improvisados, não de má intenção individual.

## Key claims

1. **Código espaguete = fluxo de controle convoluto.** "Código-fonte que codifica um fluxo de controle convoluto e, portanto, difícil de entender." A metáfora é o macarrão cozido "torcido e emaranhado". *Evidência:* definição de abertura do verbete.
2. **Causa multi-autor / temporal.** É "causado por vários fatores, como uso contínuo de modificações por várias pessoas ao longo do tempo, com estilos de programação distintos e possivelmente conflitantes." Liga direto a [[wiki/concepts/entropia-de-software|entropia de software]]. *Evidência:* verbete.
3. **Também é um anti-padrão de OO procedural.** "Pode descrever um anti-padrão em que código orientado a objetos é escrito de forma procedural" — classes com métodos longos e emaranhados, misturando responsabilidades. Ponte para [[wiki/concepts/god-object|God Object]] e [[wiki/concepts/single-responsibility-principle|SRP]]. *Evidência:* verbete.
4. **A etimologia é física, não estética.** [[wiki/entities/richard-hamming|Hamming]]: nos primórdios, para inserir instruções esquecidas você substituía uma instrução por um *transfer* para espaço vazio, executava o trecho novo e voltava; erros geravam mais saltos; "o caminho de controle do programa pela memória logo tomava a aparência de uma lata de espaguete." *Evidência:* citação de Hamming no verbete. **A bagunça nasceu de `goto` acumulado — daí a cruzada de [[wiki/entities/edsger-dijkstra|Dijkstra]] contra o `goto` (1968).**
5. **Big Ball of Mud = sistema sem arquitetura perceptível.** "Uma selva de código espaguete estruturada de forma desordenada, esparramada, desleixada, montada com fita adesiva e arame." Informação "compartilhada promiscuamente" até virar quase toda global ou duplicada. *Evidência:* citação de [[wiki/entities/brian-foote|Foote]] & [[wiki/entities/joseph-yoder|Yoder]], PLoP '97.
6. **BBoM é comum por pressão de negócio, turnover e entropia — não por incompetência isolada.** O verbete lista essas três forças como causa de sistemas "indesejáveis do ponto de vista da engenharia, mas comuns na prática." *Evidência:* verbete. Foote/Yoder creditam **Brian Marick** por cunhar o termo.
7. **Família de anti-padrões por massa.** [[wiki/concepts/lasagna-code|Lasagna]]: camadas tão entrelaçadas que mudar uma força mudar as outras. [[wiki/concepts/ravioli-code|Ravioli]]: classes bem estruturadas isoladamente, mas cujo conjunto produz design pouco claro (excesso de fragmentação). *Evidência:* verbete.
8. **Prevenção = ferramentas + treino + processo.** Não é uma bala de prata técnica: "melhores ferramentas, treinamento de desenvolvedores e melhores processos." Alinha com [[wiki/concepts/refatoracao|refatoração]] contínua e [[wiki/concepts/complexidade-ciclomatica|complexidade ciclomática]] como gate. *Evidência:* seção de prevenção.

## Entidades

- [[wiki/entities/richard-hamming|Richard Hamming]] — etimologia física do termo (saltos na memória).
- [[wiki/entities/brian-foote|Brian Foote]] & [[wiki/entities/joseph-yoder|Joseph Yoder]] — popularizaram *Big Ball of Mud* (PLoP '97).
- [[wiki/entities/brian-marick|Brian Marick]] — creditado por cunhar o termo *Big Ball of Mud*.
- [[wiki/entities/edsger-dijkstra|Edsger Dijkstra]] — "Go To Statement Considered Harmful" (1968), a raiz da luta contra o espaguete.

## Conceitos

[[wiki/concepts/code-espaguete]] · [[wiki/concepts/big-ball-of-mud]] · [[wiki/concepts/lasagna-code]] · [[wiki/concepts/ravioli-code]] · [[wiki/concepts/anti-pattern]] · [[wiki/concepts/entropia-de-software]] · [[wiki/concepts/fluxo-de-controle]] · [[wiki/concepts/complexidade-ciclomatica]] · [[wiki/concepts/god-object]] · [[wiki/concepts/refatoracao]]

## Open questions / contradições contra o wiki

- **Ravioli code tem duas leituras no próprio verbete.** Na abertura, "ravioli code" aparece como elogio irônico a código *complexo porém bem escrito*; na seção de anti-padrões, é *pejorativo* (fragmentação excessiva). Registrado em [[wiki/concepts/ravioli-code]] como ambivalência do termo, não erro.
- **BBoM vs. [[wiki/concepts/arquitetura-de-sacrificio|arquitetura de sacrifício]].** O verbete trata BBoM como puramente indesejável; [[wiki/sources/arquitetura-de-sacrificio|Fowler]] argumenta que aceitar uma arquitetura descartável pode ser *deliberado e racional*. A fronteira entre "lama por negligência" e "lama por escolha estratégica" fica em aberto.

## Citações preservadas

> "A Big Ball of Mud is a haphazardly structured, sprawling, sloppy, duct-tape-and-baling-wire, spaghetti-code jungle." — Foote & Yoder, 1997

> "...the resulting programs will not look like a bowl of spaghetti." — Martin Hopkins, 1972

> "...the same clean logical structure as a plate of spaghetti." — Richard Conway, 1978
