---
type: concept
title: "Comentários: O Quê, Não o Como"
aliases: ["comments explain what not how", "comentar propósito", "comentários clean code"]
date_created: 2026-04-29
date_updated: 2026-07-19
source_count: 2
tags: [comentarios, clean-code, refactoring, legibilidade, craftsmanship, coding-agents]
skill: tech-mentor-leadership
status: stub
---

## TL;DR

Comentários devem explicar o **propósito** (o quê) do código — nunca o mecanismo interno (o como). Se você precisa de um comentário para explicar como o código funciona, o código precisa ser refatorado para ser autoexplicativo.

## A Regra

- **Comentário bom:** explica *por que* uma decisão foi tomada, *o que* aquele bloco realiza no contexto do sistema
- **Comentário ruim:** explica passo a passo como o código executa internamente

Se o "como" não é óbvio pela leitura → refatore. Código legível dispensa explicação de mecanismo.

## Nuance na Era de Agentes: Comentário Como Contexto Recuperável

[[wiki/sources/quality-gate-ratchet-multiplos-agentes-ia]] não contradiz a regra acima, mas adiciona um motivo extra para manter comentários de propósito ("o quê"/"por quê") no próprio arquivo, específico de quando quem lê o código é um agente de IA: AI harnesses recuperam contexto via busca (grep) no arquivo que estão editando, não lendo documentação externa por completo. Um comentário de propósito bem colocado é, na prática, mais recuperável pelo agente do que a mesma informação num README ou spec separada — reforçando que "o quê"/"por quê" continua sendo o conteúdo certo do comentário, mas mudando o cálculo de custo-benefício de tê-lo no código versus só na documentação. Ver [[wiki/concepts/codebase-legibilidade-ia]] para o detalhamento completo desse caso.

## Relacionado

- [[comprimento-de-funcao]] — funções menores e menos complexas geralmente precisam de menos comentários
- [[indentacao-como-aviso]] — aninhamento excessivo gera código que "precisa" de comentários para ser entendido
- [[wiki/concepts/codebase-legibilidade-ia]] — por que comentários de propósito são mais recuperáveis por agentes do que documentação externa

## Key Sources

- [[sources/estilo-de-codigo-convencoes]]
- [[wiki/sources/quality-gate-ratchet-multiplos-agentes-ia]] — comentários como contexto recuperável via grep por agentes de IA
