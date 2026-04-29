---
type: source
title: "Convenções de Estilo de Código — O que Ninguém Conta"
aliases: ["estilo codigo", "linux kernel coding style", "indentacao 8 caracteres"]
date_created: 2026-04-29
date_updated: 2026-04-29
source_count: 0
tags: [clean-code, estilo, indentacao, comentarios, funcoes, log, craftsmanship]
skill: tech-mentor-leadership
status: stable
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/estilo-de-codigo-convencoes.md"
source_url: ""
author: "desconhecido (vídeo YouTube)"
date_published: ""
date_ingested: "2026-04-29"
---

## TL;DR

Convenções de estilo de código baseadas no Linux Kernel Coding Style. Quatro regras contraintuitivas: indentação é 8 caracteres (não 2 ou 4), strings de log nunca devem ser quebradas no meio, o tamanho máximo de uma função é inversamente proporcional à sua complexidade/aninhamento, e comentários explicam o QUÊ — nunca o COMO.

---

## Reivindicações Principais

**Claim:** Tabs/indentação são 8 caracteres — não 2, não 4.
**Evidência:** Padrão histórico do Linux Kernel Coding Style. Código que "sai da tela" com 8 caracteres está sinalizando aninhamento excessivo, não que a indentação está errada.
**Confiança:** Alta — padrão documentado no kernel Linux.

**Claim:** A indentação de 8 caracteres funciona como um aviso: se o código está indo para a direita da tela, o problema é o aninhamento, não a indentação.
**Evidência:** Lógica direta — reduzir indentação mascara o problema real (código muito aninhado) em vez de resolvê-lo.
**Confiança:** Alta.

**Claim:** Strings visíveis ao usuário e mensagens de log nunca devem ser quebradas no meio da string.
**Evidência:** Uma mensagem de log quebrada em duas linhas impede `grep` pela mensagem completa. O programa roda, o log é gerado, mas a busca falha porque a string não existe inteira em lugar nenhum.
**Confiança:** Alta — comportamento determinístico e verificável.

**Claim:** O tamanho máximo de uma função é inversamente proporcional à sua complexidade e nível de indentação.
**Evidência:** Regra explícita do Linux Kernel Coding Style. Funções complexas e aninhadas devem ser curtas. Funções simples (ex: um `switch/case` longo com casos diretos) podem ser mais longas.
**Confiança:** Alta.

**Claim:** Comentários devem explicar o QUÊ o código faz, nunca o COMO ele funciona internamente.
**Evidência:** Se você precisa de comentário para explicar o mecanismo interno, o código deve ser refatorado para ser autoexplicativo. Comentários de "como" são sinal de código que precisa de refactoring.
**Confiança:** Alta — princípio universal de clean code (Clean Code, Robert Martin).

---

## As 4 Regras

| Regra | Resumo |
|---|---|
| Indentação | 8 caracteres. Se empurra pra direita, refatore o aninhamento. |
| Comprimento de linha | Não sair da tela. Nunca quebrar strings de log no meio. |
| Tamanho de função | Inversamente proporcional à complexidade + aninhamento. |
| Comentários | Explicam o QUÊ. Se precisar explicar o COMO, refatore. |

---

## Conceitos

- [[indentacao-como-aviso]] — indentação excessiva sinalizando aninhamento problemático
- [[comentarios-o-que-nao-o-como]] — comentários explicam propósito, não mecanismo
- [[comprimento-de-funcao]] — tamanho máximo inversamente proporcional à complexidade
- [[strings-de-log-integras]] — nunca quebrar mensagens de log no meio da string

---

## Conexões com Outras Sources

- [[anti-patterns]] — aninhamento excessivo e comentários desnecessários como anti-patterns
- [[conceitos-que-ninguem-ensina]] — convenções práticas que ninguém ensina formalmente
- [[clean-architecture]] — princípios de código legível e manutenível

---

## Perguntas Abertas

- O limite de 80 ou 120 caracteres por linha ainda faz sentido em monitores widescreen modernos?
- Como calibrar "complexidade" de forma objetiva para aplicar a regra do tamanho de função?

---

## Citações

> "O problema não é a indentação de 8 caracteres. O problema é que o código está aninhado até o infinito. A indentação está te avisando."

> "Nunca tente explicar como o seu código funciona em um comentário. Refatore o código para que o funcionamento seja óbvio — e reserve os comentários para explicar o que ele faz."
