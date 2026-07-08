---
type: concept
title: "Code Review"
aliases: ["revisão de código", "pull request review", "PR review"]
date_created: 2026-07-03
date_updated: 2026-07-03
source_count: 1
tags: [code-review, qualidade, carreira, júnior, mentoria]
skill: tech-mentor-leadership
status: draft
---

# Code Review

Processo de revisão do código de um pull request por outra pessoa antes de ele ir para produção. Existe para pegar problemas de regra de negócio, legibilidade e padrão antes que virem custo em produção — não para avaliar a pessoa.

## Prioridade na revisão

1. **Regra de negócio primeiro:** o código faz o que a tarefa pedia? Código limpo que não resolve o pedido do PO não serve.
2. **Estilo e padrão depois:** formatação, nomes, convenções específicas da empresa.

Inverter essa ordem — obcecar por estilo antes de confirmar que a funcionalidade está correta — é o erro mais comum em quem está aprendendo a revisar.

## Por que o primeiro code review de um júnior costuma vir cheio de comentários

Na maioria dos casos não é sobre competência: é sobre desconhecimento do padrão específico daquela empresa (framework, convenções, jeito de estruturar código). Leva tempo até internalizar esse padrão — e enquanto isso, comentários recorrentes são esperados, não um sinal de fracasso.

Quem revisa também costuma ter pouco tempo e pouca prática em dar feedback com tato — comentários secos refletem falta de tempo, não intenção de humilhar.

## Antes de abrir o PR

- Confirmar com o PO/time que não há outra prioridade na fila.
- Testar em [[wiki/concepts/paridade-local-producao|ambiente externo]] (dev/homologação), não só localmente.
- Revisar o próprio código (com IA ou colega mais experiente) pedindo explicação do "porquê" de cada sugestão — ver [[wiki/concepts/dependencia-ia]] para o risco de fazer isso sem entender.

## Depois de receber comentários

A crítica é ao código, não à pessoa — ver [[wiki/concepts/inteligencia-emocional]]. Reagir defensivamente atrapalha mais do que ajuda. Vale manter um registro dos apontamentos recorrentes para não repetir o mesmo erro no próximo PR.

## Depois do merge

O trabalho não termina no merge: validar manualmente em produção após o deploy faz parte do ciclo — ver [[wiki/concepts/pensamento-em-producao]].

## Relacionado

- [[wiki/concepts/definicao-de-pronto]] — code review é um dos critérios de "pronto"
- [[wiki/concepts/mentoria-tecnica]] — quem revisa está, na prática, mentorando
- [[wiki/concepts/sindrome-do-impostor]] — reação emocional comum a comentários de review

## Key Sources

- [[wiki/sources/como-nao-ser-humilhado-no-primeiro-code-review]]
