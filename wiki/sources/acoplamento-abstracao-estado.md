---
type: source
title: "Acoplamento, Abstração e Estado — Lentes para Enxergar Código"
aliases: ["lentes de código", "acoplamento abstracao estado video"]
date_created: 2026-04-25
date_updated: 2026-04-25
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/acoplamento-abstracao-estado.md"
source_url: ""
author: ""
date_published: 2026-04-25
date_ingested: 2026-04-25
source_count: 0
tags: [acoplamento, abstracao, estado, software-design, clean-code, fundamentos]
skill: tech-mentor-backend
status: stable
---

# Acoplamento, Abstração e Estado — Lentes para Enxergar Código

## TL;DR

Termos técnicos como acoplamento, abstração e estado não são para decorar — são **lentes** que mudam a forma como você lê código. Sem elas, você não consegue avaliar se o código gerado por IA (ou por você) é bom ou apenas funcionante.

## Claims principais

**Claim:** Acoplamento não é sobre "estar junto", é sobre dependência entre partes.
- **Evidência:** Uma função que busca, valida, transforma, envia e loga tem cada etapa dependendo das outras. Mudar o banco afeta a validação. Mudar a API afeta a transformação.
- **Confiança:** Alta

**Claim:** Baixo acoplamento = cada função tem uma responsabilidade; mudanças são locais.
- **Evidência:** Separando em `buscarPedido`, `validarPedido`, `transformarPedido`, `enviarPedido` — cada mudança afeta apenas uma função.
- **Confiança:** Alta

**Claim:** Abstração é esconder detalhes de implementação atrás de um contrato.
- **Evidência:** `PedidoRepository` como tipo genérico permite trocar implementação DB→API sem alterar `processarPedido`.
- **Confiança:** Alta

**Claim:** Estado compartilhado mutado por múltiplas funções torna debugging impossível em escala.
- **Evidência:** `estadoGlobal.saldo` modificado por `fazerCompra` e `aplicarDesconto` perde rastreabilidade. Solução: funções que recebem estado e retornam novo estado.
- **Confiança:** Alta

**Claim:** IAs geram código que funciona, não necessariamente código bom. Essas lentes são o critério de avaliação.
- **Evidência:** Argumento implícito — sem vocabulário para identificar acoplamento/estado compartilhado, o dev não consegue rejeitar código problemático.
- **Confiança:** Média (argumento persuasivo, não demonstrado empiricamente na fonte)

## Entidades mencionadas

- Nenhuma entidade nomeada

## Conceitos tocados

- [[acoplamento]]
- [[abstracao]]
- [[estado-compartilhado]]
- [[imutabilidade]]
- [[efeito-colateral]]
- [[coesao]]
- [[idempotencia]]
- [[single-responsibility]]
- [[lentes-de-codigo]]

## Questões abertas

- A fonte menciona coesão, idempotência, efeito colateral e imutabilidade como "família" mas não os define em profundidade — são candidatos a sources dedicados.

## Citações relevantes

> "Sem saber como utilizar sem saber o que significa na prática talvez você esteja programando de forma vendado"

> "IAs geram código que funciona na maioria das vezes [...] mas não necessariamente aquele código ele é bom"

> "Esses termos são basicamente ferramentas para você conseguir fazer escolhas melhores dentro do código"
