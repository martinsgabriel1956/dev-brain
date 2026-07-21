---
type: concept
title: "Interface como Máquina de Estados"
aliases: ["UI state machine", "estados de componente", "componente como máquina de estados"]
date_created: 2026-07-21
date_updated: 2026-07-21
source_count: 1
tags: [ui, ux, design, frontend, estado, state-machine]
skill: tech-mentor-frontend
status: draft
---

# Interface como Máquina de Estados

Todo componente de UI que interage com o usuário, ou que muda em resposta a um evento do sistema, deveria ser modelado como uma máquina de [[wiki/concepts/estado]] — com estados explícitos e transições bem definidas — mesmo quando isso não vira um diagrama formal.

## Sintoma de não ter feito esse mapeamento

O caso mais comum: uma tela que busca dados (fetch) sem exibir nenhum estado de loading. O usuário clica, a tela fica parada, e o conteúdo aparece de repente. Esse estado intermediário (loading) só é esquecido porque ninguém mapeou explicitamente os estados possíveis do componente antes de implementar.

## Exemplo — máquina de estados de um formulário

```
incompleto (botão disabled)
   → preenchido (botão enabled)
      → loading (ao submeter)
         → erro (mostra mensagem)
         → sucesso (mostra confirmação)
```

Cada estado bloqueia coisas diferentes em tela (o que pode ser clicado, o que é exibido). Quanto mais complexo o componente, mais estados possíveis existem (idle, parcialmente preenchido, loading, sucesso, erro) — e mais crítico é mapeá-los antes de implementar.

## Anti-padrão: estados mutuamente exclusivos coexistindo

Um componente não deveria conseguir exibir, ao mesmo tempo, dois estados que uma máquina de estados bem desenhada trataria como mutuamente exclusivos — por exemplo, mensagem de erro e mensagem de sucesso simultâneas. Isso indica que a transição de estados não foi modelada, e sim tratada como múltiplas flags booleanas independentes que podem ficar `true` ao mesmo tempo.

## Aplicação prática

Não exige desenhar um diagrama de estados formal para todo componente simples — mas exige, ao pedir para uma IA gerar um componente (ou ao implementá-lo manualmente), declarar explicitamente quais estados esse componente pode assumir e pedir que a IA preveja essas transições (loading, erro, sucesso, disabled) em vez de assumir só o "caminho feliz".

## Relação com outros conceitos

- [[wiki/concepts/estado]] — definição geral de estado em sistemas; este conceito é a aplicação específica a componentes de UI.
- [[wiki/concepts/affordance]] — o estado de um componente deveria se refletir visualmente na sua affordance (ex.: botão disabled parece diferente de um botão clicável).
- [[wiki/concepts/caminho-feliz]] — máquinas de estado mal mapeadas tendem a só cobrir o caminho feliz, deixando erro e loading como afterthought.

## Key Sources

- [[wiki/sources/5-boas-praticas-uiux-ux-pilot]]
