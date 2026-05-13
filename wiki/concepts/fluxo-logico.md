---
type: concept
title: "Fluxo Lógico"
aliases: ["logical flow", "fluxo de decisão", "mapa de decisões"]
date_created: 2026-05-13
date_updated: 2026-05-13
source_count: 1
tags: [fluxo-logico, decisao, fundamentos, cs-fundamentals]
skill: cs-fundamentals
status: draft
---

# Fluxo Lógico

Representação das decisões de um sistema na ordem em que ocorrem — em linguagem natural, pseudocódigo ou diagrama — **antes** de escrever código. É o passo 3 do framework de [[logica-de-programacao]].

## Por que fazer antes do código

Quando o fluxo está mapeado, o código é uma tradução mecânica. Quando não está, o programador descobre as decisões no meio da implementação — onde o custo de corrigi-las é muito maior.

## Formato

Pode ser escrito em português estruturado:

```
1. Usuário insere o cartão
2. Sistema verifica se o cartão existe
   - NÃO existe → devolve cartão, exibe mensagem, encerra
   - Existe → continua
3. Sistema pede a senha
4. Usuário digita a senha
5. Sistema verifica se a senha está correta
   - INCORRETA → incrementa contador
     - tentativas >= 3 → bloqueia cartão, encerra
     - tentativas < 3  → volta ao passo 3
   - CORRETA → autenticação concluída
```

Cada `→` é uma ramificação. Cada ramificação vira um `if` ou `while` no [[fluxo-de-controle]].

## Relação com outros conceitos

- Produto da [[decomposicao-de-problemas]]: cada módulo tem seu próprio fluxo lógico
- Mapeia [[caminho-feliz]] e [[edge-case]]s juntos
- Usa [[estado]] onde o sistema precisa lembrar algo entre passos
- É a entrada para [[traducao-logica-para-codigo]]

## Key sources

- [[wiki/sources/logica-de-programacao-quatro-passos]]
