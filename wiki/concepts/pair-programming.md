---
type: concept
title: "Pair Programming"
aliases: ["pairing", "programação em par", "pair up", "pair coding"]
date_created: 2026-04-22
date_updated: 2026-08-13
source_count: 4
tags: [carreira, habitos, colaboração, aprendizado, programador-junior, onboarding, tech-debt]
skill: tech-mentor-leadership
status: stable
---

# Pair Programming

Duas pessoas trabalhando juntas no mesmo código — uma conduz, a outra aconselha, depois trocam.

## Kickoff de Tarefa Desconhecida

Quando travado sem contexto para começar, peça para um colega experiente parear. Discuta:
1. Requisitos — o que é esperado?
2. Solução — qual o caminho?
3. Codebase — quais convenções explícitas e implícitas?

## Além do Kickoff

Trabalhe junto por mais tempo. Você aprende como o parceiro pensa e resolve problemas — às vezes vale mais que resolver a tarefa.

## Remoto

A barreira de pedir pairing aumenta no remoto — uma mensagem no Slack tem mais atrito que bater no ombro. Se isso for problema no time, traga para uma retro. Depois de discutido, a barreira cai.

## Complementa

[[concepts/voluntariar-para-desconhecido]] — pairing é a forma de encarar o desafio sem ficar completamente sozinho.

## Modo de aprendizado: observar antes de participar

Quando ainda aprendendo a codebase, o papel mais valioso é o de observador ativo:
- Veja como o dev que conhece a codebase **navega** (busca, jump-to-definition, grep)
- Observe quais **perguntas** ele faz antes de codar
- Note como ele **decide** onde fazer a mudança (qual arquivo, qual função)
- Veja que **testes** ele escreve e com qual intenção

Essa observação revela o modelo mental de quem já conhece o sistema mais rápido do que qualquer leitura de código.

## Mentalidade correta

> "O objetivo não é parecer inteligente — é ficar inteligente o mais rápido possível."

## Prevenção de Dívida Técnica

[[wiki/sources/tech-debt-guia-completo-gestao-metricas]] cita pairing como prática de **prevenção** de dívida técnica imprudente, não só de aprendizado: com duas pessoas olhando o mesmo código, fica mais difícil tomar um atalho ruim sem que o parceiro questione ("vamos fazer direito"), ou o simples fato de ter alguém olhando por cima do ombro já inibe o "hack rápido". A fonte chama essa função de subestimada — no vocabulário do [[wiki/concepts/quadrante-de-fowler]], pairing ataca principalmente a célula Imprudente+Inadvertido, reduzindo a chance de um atalho ser tomado sem sequer ser uma decisão consciente.

## Mob Programming e o Multiplicador de 1,6x

[[wiki/sources/pull-requests-por-que-falham-alternativas-sem-pr]] cita **mob programming** (variante do pairing com mais de duas pessoas simultaneamente no mesmo código) como parte do pacote de empresas que dispensam [[wiki/concepts/code-review|pull request]] inteiramente — a revisão acontece embutida no próprio ato de escrever, não como etapa separada depois. A objeção gerencial óbvia ("duas pessoas fazendo o trabalho de uma") é endereçada com um número concreto citado pela fonte: estudos (não nomeados na transcrição) apontam pair programming rendendo **~1,6x a velocidade de uma pessoa sozinha, não 2x** — há perda real de velocidade bruta de escrita, mas o código sai com mais qualidade, o que tende a compensar em menos tempo de revisão e menos retrabalho depois. Esse número é uma quantificação nova sobre o ganho de qualidade já registrado na seção "Prevenção de Dívida Técnica" acima — mesma mecânica (mais um par de olhos reduz atalho ruim), agora com estimativa numérica de custo/benefício.

## Key Sources

- [[sources/9-habitos-programador-junior]]
- [[wiki/sources/como-aprender-novas-codebases]]
- [[wiki/sources/tech-debt-guia-completo-gestao-metricas]] — pairing como prática de prevenção de dívida técnica imprudente/inadvertida, não só ferramenta de aprendizado
- [[wiki/sources/pull-requests-por-que-falham-alternativas-sem-pr]] — mob programming e trunk-based como substituto de PR; multiplicador de ~1,6x de velocidade citado para pair programming
