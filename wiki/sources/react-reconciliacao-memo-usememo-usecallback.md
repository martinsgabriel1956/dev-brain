---
type: source
title: "React: Algoritmo de Reconciliação, memo, useMemo e useCallback"
aliases: ["reconciliação react memo usememo usecallback", "quando usar memo usememo usecallback"]
date_created: 2026-08-04
date_updated: 2026-08-04
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/react-reconciliacao-memo-usememo-usecallback.md
source_url: ""
author: "desconhecido (ver Perguntas Abertas)"
date_published: 2026-08-04
date_ingested: 2026-08-04
source_count: 0
tags: [react, frontend, hooks, performance, reconciliacao, memo, usememo, usecallback, shallow-compare]
skill: tech-mentor-frontend
status: stable
---

# React: Algoritmo de Reconciliação, memo, useMemo e useCallback

## TL;DR

Transcrição de vídeo (transcrição de fala fornecida diretamente pelo usuário como texto bruto de ASR, sem pontuação; limpa e formatada em Markdown em `raw/` antes da ingestão — conteúdo já em português, sem necessidade de tradução) sobre performance no React: explica o algoritmo de reconciliação (por que "renderizar" não significa "reescrever o DOM real"), demonstra com React DevTools Profiler o comportamento `did not render` do `React.memo`, e cobre as quatro situações onde `memo` compensa, o problema de igualdade referencial resolvido por `useCallback`, e o uso de `useMemo` tanto para evitar recálculo caro quanto para estabilizar referência de objetos. Fecha com o mesmo alerta de otimização prematura já presente em outras fontes da wiki.

## Claims Principais

| Claim | Evidência | Confiança |
|---|---|---|
| Renderizar é um processo de 3 etapas (criar Virtual DOM, comparar com versão anterior via reconciliação, aplicar mudanças em tela) e um componente pode completar só a etapa 1 sem nunca tocar o DOM real | Demonstração no React DevTools Profiler: itens de lista aparecem "renderizados" no profiler mesmo sem mudança visual, porque só a etapa de gerar a nova Virtual DOM ocorreu | Alta — consistente com [[wiki/concepts/virtual-dom]] e [[wiki/concepts/reconciliacao]] já documentados |
| `React.memo` intercepta *antes* da etapa 1: se props/estado não mudaram (shallow compare), o componente nem entra no fluxo de renderização (`did not render` no Profiler) | Demonstração prática: envolver `Item` em `memo` muda o resultado no Profiler de "renderizou, sem mudança de DOM" para "did not render" | Alta |
| `memo` só compensa em 4 cenários: componente puro, componente que renderiza com muita frequência, props estáveis entre renders, componente médio/grande (não trivial) | Argumentação do autor, sem benchmark numérico citado | Média — plausível e alinhado com `references/frameworks/react-performance.md` da skill, mas sem medição real |
| Funções e objetos declarados no corpo do componente são recriados (nova referência de memória) a cada renderização — quebra `memo` em componentes filhos que os recebem como prop | Demonstração: função `onAddToWishlist` sem `useCallback` causa "did not render" a desaparecer em todos os itens ao digitar no input | Alta |
| Comparação usada por `memo`/`useMemo`/`useCallback` é rasa (shallow/`===`), não profunda — por isso objetos/arrays/funções recriados com conteúdo idêntico são tratados como "diferentes" | Exemplos com `{} === {}` retornando `false`; citação da documentação do React sobre shallow compare | Alta |
| Passar uma função para o setter de estado (`setState(prev => ...)`) em vez de ler a variável de estado diretamente remove a necessidade de incluir aquele estado no array de dependências do `useCallback` | Exemplo prático de `useCallback` para `addItemToWishlist` | Alta — padrão amplamente documentado (functional updates do React) |
| `useMemo`/`useCallback`/`memo` têm custo de comparação — usá-los em cálculos/componentes triviais pode deixar a aplicação mais lenta, não mais rápida | Argumentação repetida três vezes ao longo do vídeo, sem benchmark citado | Média — mesma ressalva qualitativa já presente em [[wiki/concepts/useMemo]] e `references/frameworks/react-performance.md` |
| `key` de índice/aleatória em lista dinâmica impede o React de rastrear identidade de item entre reordenações, causando re-render da lista inteira | Exemplo de drag-and-drop numa lista de 2.000 itens | Alta — já documentado com mais detalhe em [[wiki/concepts/reconciliacao]] |

## Conceitos Abordados

- [[wiki/concepts/reconciliacao]]
- [[wiki/concepts/virtual-dom]]
- [[wiki/concepts/react-memo]] (criado nesta ingestão)
- [[wiki/concepts/shallow-compare]] (criado nesta ingestão)
- [[wiki/concepts/useMemo]]
- [[wiki/concepts/useCallback]]

## Entidades Abordadas

- [[wiki/entities/react]]

## Observações / Contradições

Nenhuma contradição com a wiki existente. A fonte é essencialmente uma versão em vídeo, com demonstração prática no React DevTools Profiler, do mesmo território já coberto em texto por [[wiki/sources/react-tudo-que-voce-precisa-saber]] e [[wiki/sources/react-19-memoization-sem-usememo-usecallback]] — mas com dois ganhos que não existiam ainda na wiki: (1) a distinção explícita entre "o componente entrou no fluxo de renderização" (gerou nova Virtual DOM) e "o DOM real foi tocado", capturada visualmente no Profiler como itens coloridos que ainda assim não geram nenhuma mutação visível; e (2) o mecanismo de shallow compare/igualdade referencial explicado com exemplos concretos de `{} === {}` e por que objetos recriados quebram `memo` mesmo com conteúdo idêntico — território que só existia como menção lateral (uma frase) em [[wiki/concepts/useCallback]], sem página própria. Isso justificou criar [[wiki/concepts/react-memo]] (que não tinha página dedicada, apesar de citado em várias outras) e [[wiki/concepts/shallow-compare]] como conceito autônomo.

## Perguntas Abertas

- Autoria não identificada com confiança: o narrador se autorrefere como "Diego" em determinado ponto ("beleza Diego, tu me convenceu" / "aí o Diego me quebrou"), mas o nome do canal ficou ilegível no ASR ("canal da vaca hesite" — provável erro de reconhecimento de fala para o nome real do canal). Não foi criada entidade para o criador por falta de confiança suficiente na identificação.
- Não há benchmark numérico citado para nenhuma das afirmações sobre "quando `memo`/`useMemo`/`useCallback` compensam" — todas as recomendações são qualitativas, mesma limitação já registrada em [[wiki/sources/react-19-memoization-sem-usememo-usecallback]].

## Raw Quotes

> "Renderizar nada mais é do que um conjunto de três etapas: criar o seu HTML, verificar se existe uma mudança desse HTML criado para o HTML anterior [...] e caso existam essas mudanças, ele aplica um algoritmo de reconciliação."

> "O mesmo [memo] ele faz essa verificação: opa, mudou alguma propriedade, não mudou o estado, não mudou alguma informação que justificaria renderizar esse componente de novo? Não. Então nem entra no fluxo de renderização."

> "Quando o JavaScript faz uma comparação se uma função é igual à outra, ele verifica se ambas as funções ocupam a mesma posição na memória."
