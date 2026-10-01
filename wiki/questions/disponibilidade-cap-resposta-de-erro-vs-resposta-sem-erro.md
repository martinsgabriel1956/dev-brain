---
type: question
title: "Disponibilidade no CAP: resposta de erro conta ou não?"
aliases: ["definição de availability divergente"]
date_created: 2026-10-01
date_updated: 2026-10-01
source_count: 3
tags: [cap-theorem, disponibilidade, contradicao]
skill: tech-mentor-system-design
status: draft
---

# Disponibilidade no CAP: resposta de erro conta ou não?

## Divergência

- [[wiki/sources/teorema-cap-p-e-pre-condicao-escolha-entre-c-e-a-pedro-camaforte]]: disponibilidade = "toda requisição recebe uma resposta, positiva ou negativa", inclusive 404/erro.
- [[wiki/concepts/disponibilidade-no-teorema-cap]] (via [[wiki/sources/github-2018-cap-pacelc-particao-video]]) e [[wiki/concepts/cap-theorem]]: todo nó vivo responde **sem erro**; recusar para preservar consistência = indisponível no CAP.

## Leitura proposta

A segunda é a definição formal [external] (Gilbert & Lynch, 2002: toda requisição a um nó não falho deve resultar em resposta "non-error"; não verificada em fonte primária nesta sessão). A primeira é uma simplificação que se contradiz: o próprio exemplo do vídeo de "página indisponível" é a escolha por **consistência**. Para entrevista, usar a definição formal.

## Pendente

Verificar o paper de Gilbert & Lynch e, se confirmado, marcar a divergência como resolvida.

## Fontes adicionais
- [[wiki/sources/teorema-cap-decisao-de-arquitetura-quando-a-comunicacao-falha-bernardo-lobato]] — terceira voz: usa a definição formal (nó que recebe responde), reforçando a leitura proposta
