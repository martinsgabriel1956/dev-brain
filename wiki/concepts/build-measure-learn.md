---
type: concept
title: "Construir-Medir-Aprender (Build-Measure-Learn)"
aliases: ["build-measure-learn", "ciclo construir medir aprender", "bml loop"]
date_created: 2026-07-07
date_updated: 2026-07-07
source_count: 1
tags: [carreira, produto, mvp, startup, validacao]
skill: tech-mentor-leadership
status: stable
---

# Construir-Medir-Aprender

Loop operacional central do [[concepts/lean-startup]]: um ciclo iterativo de três etapas que substitui "construir tudo de uma vez" por validação incremental.

## As Três Etapas

### 1. Construir

Um MVP com **uma única funcionalidade**, sem automação prematura. Exemplo: para validar assinatura de pão, o pagamento pode ser um Pix manual seguido de uma mensagem manual pro fornecedor — sem integrar gateway de pagamento. O objetivo não é ter um produto polido; é gerar aprendizado real com o menor investimento possível. → [[concepts/mvp]]

### 2. Medir

Traquear um funil de conversão simples: acessos → cliques → conversões (ex: assinaturas). Regra crítica: **medir com estranhos, não com amigos e família** — eles sempre apoiam, o que produz dados falsos e infla a confiança na ideia.

### 3. Aprender

Conversar diretamente com os usuários para entender os números do funil — algo que a maioria dos programadores evita. Descobertas típicas: preço errado, método de pagamento ausente, desconfiança na interface (ex: achar que um QR code é golpe).

## O Ciclo se Repete

O aprendizado de uma iteração alimenta a próxima construção. Exemplo: se o aprendizado mostra que usuários preferem cartão de crédito a Pix, a próxima construção integra pagamento por cartão — ainda pela via mais simples possível, sem otimizar taxas nesse momento. **O dado do usuário real vale mais que a economia de centavos em taxa de gateway.**

O ciclo continua até o produto ficar validado o suficiente para avançar para [[concepts/aprendizagem-validada]] (teste A/B) e fases posteriores.

## Erro Comum do Dev Emocionado

Automatizar ou polir antes de validar — pular a etapa "Medir/Aprender" e ir direto para uma nova rodada de "Construir" mais elaborada. Isso é essencialmente [[concepts/scope-creep]] disfarçado de iteração.

## Ver Também

- [[concepts/lean-startup]] — metodologia que contém este ciclo
- [[concepts/mvp]] — a unidade construída em cada iteração
- [[concepts/validacao-de-problema]] — validação que precede o primeiro ciclo

## Key Sources

- [[sources/lean-startup-para-devs-mano-deivin]]
