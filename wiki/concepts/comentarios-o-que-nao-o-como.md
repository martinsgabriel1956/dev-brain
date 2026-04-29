---
type: concept
title: "Comentários: O Quê, Não o Como"
aliases: ["comments explain what not how", "comentar propósito", "comentários clean code"]
date_created: 2026-04-29
date_updated: 2026-04-29
source_count: 1
tags: [comentarios, clean-code, refactoring, legibilidade, craftsmanship]
skill: tech-mentor-leadership
status: stub
---

## TL;DR

Comentários devem explicar o **propósito** (o quê) do código — nunca o mecanismo interno (o como). Se você precisa de um comentário para explicar como o código funciona, o código precisa ser refatorado para ser autoexplicativo.

## A Regra

- **Comentário bom:** explica *por que* uma decisão foi tomada, *o que* aquele bloco realiza no contexto do sistema
- **Comentário ruim:** explica passo a passo como o código executa internamente

Se o "como" não é óbvio pela leitura → refatore. Código legível dispensa explicação de mecanismo.

## Relacionado

- [[comprimento-de-funcao]] — funções menores e menos complexas geralmente precisam de menos comentários
- [[indentacao-como-aviso]] — aninhamento excessivo gera código que "precisa" de comentários para ser entendido

## Key Sources

- [[sources/estilo-de-codigo-convencoes]]
