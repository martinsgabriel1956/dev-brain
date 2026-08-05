---
type: source
title: "Recriando o Zustand com JavaScript Puro (sem Provider)"
aliases: ["contas do zustand javascript puro", "zustand sem provider", "createDataSet useDataSet"]
date_created: 2026-08-03
date_updated: 2026-08-03
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/recriando-zustand-javascript-puro-sem-provider.md
source_url: ""
author: "Pedro (canal YouTube não identificado na transcrição)"
date_published: null
date_ingested: 2026-08-03
source_count: 0
tags: [react, zustand, observer-pattern, hooks, estado-global, javascript, frontend]
skill: tech-mentor-frontend
status: stable
---

# Recriando o Zustand com JavaScript Puro (sem Provider)

## TL;DR

Transcrição de vídeo (YouTube, autor identificado só como "Pedro" na fala, canal e URL não constam na fonte) que recria, em ~43 linhas de JavaScript puro, o mecanismo central do [[wiki/concepts/zustand]]: um estado global fora da árvore do React, sincronizado com componentes via um Hook customizado, sem precisar de `Provider`/Context. A implementação combina três peças: um [[wiki/concepts/observer-pattern]] (`createSubscriber`, usando `Set` para os listeners), um `Map` para guardar o valor do estado, e um Hook (`useDataSet`) que usa [[wiki/concepts/useState]] + [[wiki/concepts/useEffect]] para espelhar esse estado externo dentro do React. O vídeo demonstra funcionamento com um exemplo de color picker (`react-color`) sincronizado em três pontos diferentes da árvore de componentes.

## Claims Principais

| Claim | Evidência | Confiança |
|---|---|---|
| Zustand, Context API e Redux resolvem o mesmo problema — prop drilling | Afirmação de abertura do vídeo, alinhada com [[wiki/concepts/context-api]] | Alta |
| É possível recriar o mecanismo essencial do Zustand (estado externo à árvore + hook de sincronização) sem `Provider`, usando só `Set`, `Map`, `useState` e `useEffect` | Implementação completa demonstrada e testada em 3 componentes diferentes no vídeo | Alta — implementação funcional mostrada, não só teórica |
| `Set` é preferível a `Array` para gerenciar uma lista de listeners porque `add`/`delete` são diretos (sem `indexOf`/`filter` manual) | Justificativa do autor ao escolher `Set` em vez de `Array` para os `listeners` | Alta — vantagem real e verificável da API de `Set` |
| O padrão de "updater function" (`typeof event === "function"`) permite que o setter do estado global aceite tanto um valor direto quanto uma função que recebe o valor atual — replicando a API do `useState` do React | Trecho de código do `useDataSet`, mesmo padrão documentado em [[wiki/concepts/useState]] | Alta |
| A solução tem limitações reconhecidas pelo próprio autor: possíveis problemas de concorrência (race conditions em updates simultâneos) e de re-render, tornando-a inadequada para "apps gigantes" sem cuidado adicional | Ressalva explícita do autor na conclusão do vídeo | Média — o autor não detalha *quais* cenários de concorrência quebram, nem faz benchmark de re-render |
| A implementação não usa `useSyncExternalStore` (o hook do React 18+ desenhado especificamente para sincronizar estado externo com segurança em Concurrent Mode) | Ausência do hook no código mostrado — o autor usa `useState` + `useEffect` manualmente | Alta (observação direta do código) — ponto de atenção, não contradição: a fonte não menciona `useSyncExternalStore` em nenhum momento |

## Conceitos Abordados

- [[wiki/concepts/zustand]] (criado nesta ingestão)
- [[wiki/concepts/observer-pattern]]
- [[wiki/concepts/context-api]]
- [[wiki/concepts/custom-hooks]]
- [[wiki/concepts/useState]]
- [[wiki/concepts/useEffect]]
- [[wiki/concepts/singleton-pattern]]
- [[wiki/concepts/design-patterns]]

## Entidades Abordadas

- [[wiki/entities/react]]

## Observações / Contradições

Nenhuma contradição de fato com o que já está na wiki. O vídeo é um exercício didático de "reinventar a roda" para ensinar o mecanismo por trás de bibliotecas de estado global — ele próprio reconhece que a solução final não é production-ready para aplicações grandes (ver claim de concorrência/re-render acima). Um ponto que vale registrar como lacuna técnica: a implementação do `useDataSet` é essencialmente um `useSyncExternalStore` artesanal (sincronizar um estado externo ao React com um estado local via subscribe/unsubscribe é exatamente o problema que `useSyncExternalStore` foi desenhado para resolver, incluindo casos de tearing em Concurrent Mode que a implementação manual do vídeo não trata) — isso não invalida a demonstração didática, mas é uma ressalva técnica que o vídeo não menciona.

A transcrição original continha vários erros de reconhecimento de fala (ASR) que foram corrigidos por contexto técnico ao transformar em Markdown — por exemplo "contas do Yeti"/"contas do Oi" → **Zustand**, "j7"/"sete" → **`Set`** (a estrutura nativa, não o número), "os state"/"iOS state" → **`useState`**, "Twitter" → **setter**, "rhastion Têxtil Redux" → **Recoil, Jotai, Redux**. Essas correções são inferências de domínio (nomes de APIs/libs React reais que fazem sentido no contexto), não estão explicitamente confirmadas por uma fonte externa — sinalizado aqui para transparência.

## Perguntas Abertas

- Não há indicação de canal/autor/URL na transcrição fornecida — a atribuição ("Pedro") vem apenas da fala de abertura do vídeo, sem sobrenome ou nome do canal.
- O vídeo não detalha os cenários exatos de "concorrência" e "problemas de renda(rização)" mencionados na conclusão — fica como questão aberta comparar com os mecanismos reais que o Zustand usa para evitar tearing (`useSyncExternalStore`).

## Raw Quotes

> "A gente vai recriar o Zustand, na realidade, porém sem a necessidade de ficar usando um Provider."

> "Com essas ~14 linhas de código a gente já tem uma estrutura básica de Observer pronta."

> "Como vocês podem ver, com simples ~43 linhas de código, a gente recriou o Zustand de uma maneira bem simples, só com JavaScript puro."

> "Talvez a solução não seja a melhor do mundo — você não conseguiria criar apps gigantes com ela sem cuidado. Tem alguns probleminhas: talvez concorrência [...] ou alguns problemas de re-render."
