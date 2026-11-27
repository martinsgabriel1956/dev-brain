---
type: concept
title: "Deriva em Edição Iterativa de Imagem"
aliases: ["generation loss com IA", "a imagem piora a cada edição", "identity drift", "deriva de identidade", "cópia da cópia"]
date_created: 2026-11-27
date_updated: 2026-11-27
source_count: 1
tags: [ia-generativa, geracao-de-imagem, edicao-de-imagem, qualidade, fluxo-de-trabalho]
skill: tech-mentor-ai
status: stub
---

## Definição

Perda progressiva de qualidade e de fidelidade quando uma imagem é editada várias vezes em sequência por um modelo generativo. Cada edição regenera a imagem a partir da versão anterior, não do original. Pequenas perdas, reinterpretações de detalhe e desvios de rosto e proporção se acumulam, como numa cópia da cópia.

## Exemplo

Em [[wiki/sources/frontpush-ia-meu-workflow-de-ia-midia]], a corrente da foto do autor "deu uma bombeadinha" depois do primeiro pedido de capacete. Depois de mais pedidos no mesmo chat, "olha o tanto que já piorou a qualidade", e o rosto deixou de ficar "parecido comigo".

## Não confundir com

- [[wiki/concepts/context-compaction]] e [[wiki/concepts/degradacao-de-contexto]]: afetam as *instruções* em chats longos (o modelo esquece ou pesa mal o que foi pedido). A deriva afeta os *pixels*, mesmo com o contexto curto. A aula atribui tudo à compactação; na prática, os dois efeitos se somam.

## O que fazer

- Guardar a melhor versão e editar sempre a partir dela, ou do original, e não da última.
- Pedir mudanças grandes em um pedido só, em vez de vários pequenos encadeados.
- Quando degringolar, começar outro chat e reanexar o original e as referências, como o autor faz ("já exclua aquele chat, já inicio outro"). Pedir ao modelo que "recupere o contexto" não funciona.
- Para manter o rosto, usar referência de identidade (várias fotos e descrição estruturada) em vez de iterar sobre a saída.

## Key Sources

- [[wiki/sources/frontpush-ia-meu-workflow-de-ia-midia]]: FrontPUSH, módulo de IA, aula 7: a corrente "bombeada" e o rosto que se perde no site do robô
