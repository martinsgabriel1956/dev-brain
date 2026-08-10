---
type: concept
title: "Produto Vendível Desde o Dia Zero"
aliases: ["feature vendível", "PMF de uma única feature", "não dar tempo grátis esperando apego"]
date_created: 2026-07-09
date_updated: 2026-08-06
source_count: 2
tags: [product-market-fit, saas, mvp, growth, pricing]
skill: tech-mentor-leadership
status: draft
---

# Produto Vendível Desde o Dia Zero

Princípio de que a primeira versão de um produto deve ter, desde o lançamento, ao menos uma funcionalidade pela qual usuários pagariam — em vez de lançar uma versão gratuita na esperança de o usuário "gostar" e só depois tentar convertê-lo em pagante conforme mais funcionalidades são adicionadas.

## O Argumento

Em [[wiki/sources/como-vender-um-saas-sem-audiencia]], o autor descreve um erro comum: lançar um produto onde nenhuma funcionalidade isolada seria suficiente para alguém pagar, torcendo para que o acúmulo de features eventualmente justifique um preço. A alternativa proposta é inverter a ordem: validar desde o início que existe **uma única funcionalidade** que, sozinha, já convenceria alguém a pagar — e só depois decidir a estratégia de distribuição (gratuita ou paga) em cima dela.

## Case — Persoa (Pivô de Feature)

O produto do autor começou com a funcionalidade de "ChatGPT invisível durante uma reunião", atraindo público vindo de ferramentas como Roy Lee/Cluely/Interview Coder — usado para colar em entrevistas de emprego. Problema: uso único (a pessoa usa até conseguir o emprego e nunca mais volta), o que é ruim para [[wiki/concepts/ltv-cac]].

A funcionalidade que substituiu esse posicionamento como core do produto — tradução de reunião em tempo real — tem uso recorrente (reuniões de trabalho contínuas) e, segundo o autor, é ela quem de fato sustentaria pagamento. Ambas as funcionalidades (stealth mode e tradução em tempo real) foram pagas desde o dia 1 do produto, mesmo que a versão atual, distribuída para uma audiência já existente, seja majoritariamente gratuita — a gratuidade aqui é uma decisão de distribuição, não uma admissão de que a funcionalidade não vale a pena pagar.

## Ser Usuário do Próprio Produto

Complementar a esse princípio: o autor recomenda que quem empreende pela primeira vez construa um produto do qual é o próprio usuário. Cita o caso da versão Windows do "Persoa", que ficou ruim porque o autor não tinha máquina Windows para testar — ao adquirir uma e corrigir ~8 bugs num fim de semana, a experiência do usuário Windows mudou completamente. A lógica: resolver o próprio problema primeiro, tornar-se o primeiro cliente dessa solução, depois vender para quem pensa de forma parecida.

## Caso adjacente: monetização via boost, sem gate de feature

Em [[wiki/sources/15-dias-depois-lancar-sas-numeros-ataques-vulnerabilidades]], o Find My SaaS monetiza desde o lançamento via um único mecanismo pago (boost/destaque temporário de um SaaS cadastrado na home) — o produto central (listar e receber upvote) continua gratuito, mas a via de receita já existe desde o dia zero, gerando R$ 4.819 em 15 dias sem tráfego pago. Reforça o princípio central desta página com uma variante: em vez de uma feature core paga, é uma camada de visibilidade paga sobre um produto gratuito — mesma lógica de "algo vendível desde o início", aplicada a marketplace em vez de SaaS de uso direto.

## Key Sources

- [[wiki/sources/como-vender-um-saas-sem-audiencia]]
- [[wiki/sources/15-dias-depois-lancar-sas-numeros-ataques-vulnerabilidades]] — monetização via boost pago desde o lançamento, sobre produto core gratuito
