---
type: concept
title: "Lógica de Programação"
aliases: ["programming logic", "raciocínio lógico em código"]
date_created: 2026-05-13
date_updated: 2026-06-01
source_count: 2
tags: [logica-de-programacao, fundamentos, cs-fundamentals, carreira, aprendizado]
skill: cs-fundamentals
status: stable
---

# Lógica de Programação

Capacidade de traduzir um problema do mundo real em instruções executáveis por um computador. Não é sobre sintaxe — é sobre o raciocínio por trás das decisões que o sistema precisa tomar.

A pergunta real que as pessoas fazem quando buscam "lógica de programação" é: **como me torno um programador competente?**

## Princípio central (Dijkstra)

> O ato de descrever um programa de forma inambígua e detalhada e o ato de programar são exatamente a mesma coisa.

O código é uma **tradução** de decisões já tomadas, não uma criação. Quem entende o problema antes de abrir o editor escreve código mais claro, com menos surpresas.

Uma descrição em português e um programa em Python que expressam a mesma lógica são o **mesmo programa** — a diferença é apenas de sintaxe. Ver [[wiki/entities/edsger-dijkstra]] para a crítica à linguagem natural em programação.

## O que lógica de programação NÃO é

- **DSA (estruturas de dados e algoritmos):** melhora um pouco a lógica, mas é uma parte pequena do todo — seria leviano dizer que "DSA = lógica de programação".
- **Fluxogramas e máquinas de estado:** são representações visuais do raciocínio, não o raciocínio em si.
- **Memorização de sintaxe ou APIs:** saber o nome do pássaro em 15 línguas não é saber nada sobre o pássaro (Feynman).

## Os 5 pilares da competência em programação

### 1. Quebrar problemas em problemas menores

Dado "clone o Netflix", identificar: cadastro, login, galeria de thumbnails, página de vídeo, streaming, servidor de vídeo. A partir do nebuloso surgem perguntas concretas e acionáveis. Ver [[decomposicao-de-problemas]].

### 2. Habilidade de pesquisa e senso crítico

Encontrar boas referências, avaliar qualidade, e **traduzir para o seu contexto** — uma implementação em Go não serve diretamente se você trabalha em Java, mas a lógica sim.

### 3. Repertório

Acúmulo de experiência prática que gera reconhecimento de padrões. "Esse problema tem cara de Redis" só surge quando você já usou Redis em contextos diferentes. Ver [[repertorio]].

### 4. Projetos variados

A única forma de construir repertório real. Tutoriais ensinam uma receita; projetos ensinam a cozinhar. Repetir a mesma receita 20 vezes não é repertório — é proficiência naquela receita.

### 5. Intuição

Resultado natural de repertório suficiente. Com projetos suficientes, a arquitetura de um novo SaaS emerge em 15 segundos a partir da experiência acumulada.

## Granularidade varia com a linguagem

Quanto mais próxima da máquina, maior a especificidade exigida. Python não exige declarar tipo, mutabilidade ou alocação de memória. Rust exige tudo isso. A lógica não muda — a quantidade de decisões explícitas que você precisa tomar muda.

## Relação com outros conceitos

- Depende de [[decomposicao-de-problemas]] para quebrar o problema em partes manejáveis
- Expressa-se através de [[fluxo-logico]] e [[fluxo-de-controle]]
- Requer atenção ao [[caminho-feliz]] e aos [[edge-case]]s
- O [[estado]] é a memória que o sistema usa para tomar decisões ao longo do fluxo
- O resultado final é [[traducao-logica-para-codigo]]
- [[repertorio]] é o acúmulo que torna a lógica rápida e intuitiva

## Key sources

- [[wiki/sources/logica-de-programacao-quatro-passos]] — framework de 4 passos: entender, decompor, criar fluxo, traduzir
- [[wiki/sources/logica-de-programacao-o-que-e-de-verdade]] — os 5 pilares; programação = descrição inambígua; DSA como parte pequena do todo
