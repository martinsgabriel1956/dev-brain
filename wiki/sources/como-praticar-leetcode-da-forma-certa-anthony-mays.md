---
type: source
title: "Como Praticar Questões de LeetCode (Do Jeito Certo)"
aliases: ["how to practice leetcode the right way", "os seis passos leetcode", "six steps anthony mays"]
date_created: 2026-07-22
date_updated: 2026-07-22
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/como-praticar-leetcode-da-forma-certa-anthony-mays.md
source_url: "https://medium.com/@anthonydmays/how-to-practice-leetcode-questions-the-right-way-4f9735cf06c6"
author: "Anthony D. Mays"
date_published: "2022-05-10"
date_ingested: 2026-07-22
source_count: 0
tags: [entrevistas, coding-interview, leetcode, carreira, algoritmos, mock-interview]
skill: tech-mentor-leadership
status: stable
---

# Como Praticar Questões de LeetCode (Do Jeito Certo)

## TL;DR

Artigo original de 2022 de Anthony D. Mays — a fonte primária que o vídeo já ingerido nesta wiki ([[wiki/sources/leetcode-como-se-preparar-entrevistas-coding-anthony-mays]]) apenas resumia pela perspectiva do entrevistador. Aqui o autor detalha o framework prático completo: **"Os Seis Passos"**, aplicado como um roteiro de dez etapas de [[wiki/concepts/seis-passos-mock-interview|entrevista simulada]] (mock interview) que deve substituir a prática solo de LeetCode. Tese central: quem pratica muito e não evolui tem um problema de método, não de inteligência ou esforço — porque [[wiki/concepts/entrevista-tecnica-coding|entrevista técnica]] é um exercício colaborativo, não uma prova solo.

## Key Claims

- **O problema não é volume de prática, é estratégia** — usar a Blind 75 ou o Cracking the Coding Interview não ajuda se a técnica de resolução for a errada, do mesmo jeito que treinar musculação sem boa forma não constrói força de verdade.
- **Entrevista técnica é colaborativa, não solo** — a maior fraqueza de praticar só no LeetCode é que não há humano envolvido: a questão precisa entregar tudo de antemão, enquanto um entrevistador real segura informação de propósito para observar como o candidato lida com ambiguidade. → [[wiki/concepts/entrevista-tecnica-coding]]
- **"Os Seis Passos" como roteiro de dez etapas de entrevista simulada**: (1) ferramenta de código sem IDE completa, (2) entrevistador simulado — que não precisa ser técnico, (3) cronômetro real de 45–60 min, (4) articular o problema só de ouvido, sem olhar o enunciado, (5) fazer perguntas e reafirmar suposições mesmo sabendo a resposta, (6) criar exemplos de entrada/saída como casos de teste, (7) brainstorm de soluções com estimativa de Big-O *antes* de codar, (8) implementação rápida e narrada, nunca em pseudocódigo, (9) testar contra uma checklist mental de erros comuns, (10) otimizar até o tempo acabar. → [[wiki/concepts/seis-passos-mock-interview]]
- **Estimar a complexidade (Big-O) da solução ideal antes de escrever qualquer código** — perguntar "existe uma solução O(1)? O(log n)?" antes de partir para a implementação, em vez de descobrir a complexidade só depois de codar. → [[wiki/concepts/big-o]]
- **A implementação deve ser a parte mais fácil e mais rápida do processo** — se não for, é sinal de que falta prática de escrita de código, não de resolução de problema; usar APIs/idiomas da linguagem sabendo o custo real por trás deles (ex.: `sort()` custa O(n log n) ou O(n²), não é mágica).
- **Manter um diário de entrevistas simuladas** — documentar feedback de cada sessão, incluindo pontos não-técnicos (fala, silêncio, tiques), e comparar a autoavaliação do candidato com a avaliação do entrevistador (contratar / não contratar / em cima do muro) para calibrar percepção.
- **Quem ajuda como entrevistador simulado não precisa ser técnico** — o autor usou a própria esposa, não-técnica, para dar feedback de postura e presença durante a preparação para o Google.

## Entities

[[wiki/entities/anthony-d-mays]]

## Concepts

[[wiki/concepts/entrevista-tecnica-coding]] · [[wiki/concepts/seis-passos-mock-interview]] · [[wiki/concepts/big-o]] · [[wiki/concepts/reconhecimento-de-padroes]] · [[wiki/concepts/algoritmos-e-estruturas-de-dados]]

## Relação com o vídeo já ingerido

Este artigo é a fonte primária referenciada no vídeo [[wiki/sources/leetcode-como-se-preparar-entrevistas-coding-anthony-mays]] (que resolve a "Open Question" deixada naquela fonte sobre o artigo original não ter sido localizado). O vídeo cobre a *tese* (por que memorizar problema falha, por que ficar travado é esperado); este artigo cobre o *método* (o roteiro concreto de dez etapas para praticar). As duas fontes se complementam sem contradição.

## Open Questions

- Não há dados objetivos (taxa de aprovação, estudo controlado) que sustentem a eficácia do framework "Os Seis Passos" — é metodologia de um ex-entrevistador/coach de carreira, tratada aqui como prática de mercado, não como claim cientificamente verificado.

## Raw Quotes

> "You're probably practicing wrong."

> "Technical interviewing is a collaborative problem-solving exercise."

*(Resumo completo em `raw/como-praticar-leetcode-da-forma-certa-anthony-mays.md`.)*
