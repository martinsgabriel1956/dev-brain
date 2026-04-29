---
type: concept
title: "Strings de Log Íntegras"
aliases: ["log strings intactas", "nunca quebrar log", "grep log message"]
date_created: 2026-04-29
date_updated: 2026-04-29
source_count: 1
tags: [logging, debugging, grep, clean-code, observabilidade]
skill: tech-mentor-leadership
status: stub
---

## TL;DR

Strings visíveis ao usuário e mensagens de log nunca devem ser quebradas no meio. Uma mensagem dividida em duas linhas impede `grep` pela mensagem completa — o texto não existe inteiro em lugar nenhum no código.

## O Problema

```c
// ERRADO — impossível fazer grep por "Erro ao processar usuário"
printk("Erro ao processar "
       "usuário com id %d\n", user_id);
```

## A Solução

Quebrar a linha em outro ponto — nos argumentos, não dentro da string:

```c
// CERTO — string íntegra, grep funciona
printk("Erro ao processar usuário com id %d\n",
       user_id);
```

## Relacionado

- [[observabilidade]] — logs estruturados e pesquisáveis são parte de boa observabilidade

## Key Sources

- [[sources/estilo-de-codigo-convencoes]]
