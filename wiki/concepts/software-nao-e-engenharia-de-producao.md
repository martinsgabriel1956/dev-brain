---
type: concept
title: "Software Não É Engenharia de Produção"
aliases: ["software não é hardware", "lean/kanban não se aplica a software", "soft porque não é hard"]
date_created: 2026-09-18
date_updated: 2026-09-22
source_count: 2
tags: [agile, engineering-management, filosofia-de-software, metricas]
skill: tech-mentor-leadership
status: stub
---

# Software Não É Engenharia de Produção

**TL;DR:** Argumento de [[wiki/entities/fabio-akita]]: técnicas nascidas na engenharia de produção física — Lean, Kanban, Six Sigma, PERT, Monte Carlo — resolvem problemas específicos de fabricação de bens físicos (carros, navios, prédios), sob restrições físicas reais (peso, gravidade, tolerância de material). Software (*soft*ware, não *hard*ware) é uma abstração sem forma física, sem peso, sem essas restrições — por isso a transferência dessas técnicas para desenvolvimento de software é, na melhor das hipóteses, superficial.

## O Argumento Central

Todos os campos da engenharia física foram refinados ao longo de décadas para lidar com restrições concretas: duas construtoras seguindo a mesma especificação constroem casas parecidas, em custo e tempo parecidos, com qualidade parecida, dadas as mesmas condições. Em software, dois programadores implementando a mesma especificação podem produzir resultados em **ordens de grandeza** de diferença — não uma variação de 20-30%, como seria esperado numa obra física. Um profissional medíocre pode levar horas e dezenas de linhas para uma tarefa que um profissional excelente resolve em minutos e uma linha. Não existe paralelo direto entre gerenciar produção de bens físicos e gerenciar produção de software além de semelhanças superficiais.

O mesmo raciocínio, segundo a fonte, vale para qualquer campo criativo/de ideias: literatura, música, pintura. Ninguém tenta medir a produtividade de escrever um livro com Kanban, ou controlar a composição de uma música com métricas de fluxo — soa ridículo nesses domínios, mas é aceito sem questionamento em software.

## Números Não São Prova

Métricas ("funciona no Google", "funciona no Spotify") raramente vêm acompanhadas das condições sob as quais foram coletadas: repetibilidade, grupos de controle, premissas do contexto. Ter algo que parece evidência está longe de ter prova — diferente da engenharia civil, onde é possível teorizar, calcular e provar fisicamente o funcionamento de uma solução, nenhuma metodologia ágil tem esse tipo de validação formal. A fonte compara isso a "numerologia": números que contam a história que você quer ouvir não são ciência, mesmo quando "computam".

## Onde a Parte Conceitual do Lean Ainda Faz Sentido

A fonte não descarta o Lean por completo — a parte *conceitual* (evitar desperdício, ser rápido para mudar de direção) tem valor. O que não se sustenta são as técnicas e métricas específicas nascidas para resolver problemas de linha de produção física, aplicadas mecanicamente a um domínio sem restrições físicas.

## O Compilador é o "Operário", o Programador é o Arquiteto

[[wiki/sources/sobre-ser-gerente-fabio-akita]] aprofunda o argumento central com duas metáforas que a fonte anterior não usa. Primeiro, refuta a comparação de programador com operário de linha de fábrica (que executa uma "planta baixa" detalhada feita por um arquiteto): esse papel de execução mecânica e repetitiva já está automatizado — é o compilador/interpretador que recebe o código-fonte e produz o binário executado mecanicamente. O código-fonte não é a "planta baixa", é o produto final do raciocínio — o que faz de todo programador, tecnicamente, um arquiteto, não um operário.

Segundo, refuta a metáfora de orquestra clássica (maestro = gerente, composição = trabalho do arquiteto, músicos = executores de precisão): a analogia mais correta é um grupo de jazz, onde intuição, improvisação e estilo individual de cada músico moldam o resultado final, dentro de uma base mínima compartilhada para não virar "só barulho". Reforça com o mesmo argumento já documentado acima (duas construtoras convergem para o mesmo prédio; dois programadores com a mesma especificação divergem em ordens de grandeza) que **o código é a própria especificação** — não é possível especificar software com precisão antes de codificar, exceto em nichos onde o grosso do trabalho já é integração/customização de algo pronto (ex.: agências WordPress, ERPs consolidados), que se aproximam de fato de uma linha de montagem.

## Ver também

- [[wiki/concepts/goodharts-law]] — mecanismo complementar: mesmo quando uma métrica de software faz algum sentido inicialmente, virar alvo formal a corrompe
- [[wiki/concepts/manifesto-agil-como-adjetivo]] — a distorção de nome (Kanban, Scrum) que acompanha essa transferência equivocada de técnicas

## Key Sources

- [[wiki/sources/agilidade-manifesto-agil-fabio-akita]] — fonte primária desta ingestão
- [[wiki/sources/sobre-ser-gerente-fabio-akita]] — metáforas do compilador como "operário automatizado" e orquestra clássica vs. jazz; nichos (WordPress, ERPs) onde o trabalho se aproxima de fato de linha de montagem
