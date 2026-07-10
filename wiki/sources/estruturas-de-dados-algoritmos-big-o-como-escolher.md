---
type: source
title: "Estruturas de Dados, Algoritmos e Big O — Como Escolher"
aliases: ["big o na pratica", "como escolher estrutura de dados", "quatro curvas essenciais"]
date_created: 2026-07-10
date_updated: 2026-07-10
source_count: 0
tags: [cs-fundamentals, big-o, estruturas-de-dados, algoritmos, complexidade, entrevista-tecnica]
skill: cs-fundamentals
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/estruturas-de-dados-algoritmos-big-o-como-escolher.md
source_url: ""
author: "desconhecido (canal parceiro da Rocket City)"
date_published: ""
date_ingested: 2026-07-10
---

# Estruturas de Dados, Algoritmos e Big O — Como Escolher

## TL;DR

Continuação de [[wiki/sources/estruturas-de-dados-pratica-array-hashmap-fila-pilha-arvore]] (que já anunciava esta parte sobre Big O). Formaliza como escolher estrutura de dados a partir da operação que precisa ser priorizada, distingue estrutura de dados (como os dados ficam guardados) de algoritmo (a sequência de passos sobre esses dados), introduz as quatro curvas essenciais de Big O (O(1), O(n), O(log n), O(n²)), o trade-off tempo vs. memória, a distinção melhor/pior/caso médio, e fecha com um framework de quatro perguntas para escolher estrutura antes de escrever código — incluindo como ler sinais de um enunciado de entrevista técnica.

## Key Claims

**Claim:** A escolha da estrutura de dados deve partir da operação que mais importa no caso de uso, não da estrutura em si.
**Evidence:** Buscar por e-mail pede "caminho direto" (chave); pegar o próximo job de uma fila pede ordem de chegada. Toda estrutura prioriza algumas operações (buscar, inserir, remover, percorrer, manter ordem, consultar por chave) e torna outras mais caras — não existe estrutura ótima para tudo.
**Confidence:** alta

**Claim:** Estrutura de dados e algoritmo são conceitos separados mas interdependentes — a melhor estrutura simplifica o algoritmo necessário.
**Evidence:** Exemplo de busca de conta por e-mail: numa lista simples, o algoritmo testa item por item (O(n)); com um índice por e-mail, o algoritmo vai direto à chave (O(1)). O ganho de performance às vezes vem de mudar o algoritmo, às vezes vem de guardar os dados de outro jeito.
**Confidence:** alta

**Claim:** Big O mede como o número de passos cresce em função do tamanho da entrada (n) — não tempo real em milissegundos.
**Evidence:** Medir em milissegundos é enganoso porque depende de máquina, linguagem, banco, cache e ambiente. A pergunta correta é: se n dobra, o número de passos fica igual, dobra, ou cresce muito mais que o dobro? "n" pode representar usuários, produtos, linhas, nós de grafo — qualquer medida do tamanho do problema.
**Confidence:** alta

**Claim:** Quatro curvas de Big O são suficientes para começar: O(1), O(n), O(log n) e O(n²).
**Evidence:** O(1) — passos quase não mudam com mais dados. O(n) — passos crescem na mesma proporção (um loop). O(log n) — cada passo corta uma parte grande do problema (busca que descarta metade a cada iteração). O(n²) — cada item é comparado com vários outros (dois loops aninhados); cresce muito mais rápido que o dobro quando a entrada dobra.
**Confidence:** alta

**Claim:** Gastar mais memória para economizar passos (trade-off tempo vs. espaço) é o raciocínio por trás de índices e estruturas auxiliares.
**Evidence:** Guardar só a lista original força busca item por item. Manter um índice por fora ocupa mais espaço mas acelera o acesso — "você prepara uma estrutura antes para não pagar a busca inteira toda vez". A notação Big O mais baixa nem sempre é a melhor opção: depende do limite real do problema (espaço disponível vs. latência aceitável).
**Confidence:** alta

**Claim:** Complexidade tem melhor caso, pior caso e caso médio — e "complexidade" sem qualificação numa entrevista quase sempre significa pior caso.
**Evidence:** Numa busca linear: item no começo = melhor caso (rápido); item no final = pior caso (percorre tudo); comportamento típico em produção com milhares de execuções = caso médio, que é o que geralmente importa na prática.
**Confidence:** alta

**Claim:** Enunciados de entrevista técnica carregam sinais lexicais que apontam para a família certa de estrutura/algoritmo.
**Evidence:** "Dados duplicados" → existe solução melhor que comparar todo mundo com todo mundo. "Busca por chave" → estrutura com O(1) por chave (hashmap). "Próximo item, menor valor, caminho ou prefixo" → cada termo aponta para uma família específica (fila/heap, árvore, grafo, trie).
**Confidence:** média — o vídeo lista os sinais sem detalhar a estrutura de destino de cada um

**Claim:** Framework de quatro perguntas antes de escrever a solução: qual é o N? qual a operação mais comum? qual estrutura ajuda essa operação? como o custo cresce com o N?
**Evidence:** Apresentado como o fechamento prático do vídeo, unindo os pontos anteriores — n como tamanho de entrada, operação como critério de escolha, estrutura como resposta, Big O como métrica de crescimento.
**Confidence:** alta

## Entities & Concepts Touched

- [[wiki/concepts/big-o]] — enriquecido com o framing das "quatro curvas essenciais" e a introdução informal ("se eu dobrar os dados, quantos passos a mais?")
- [[wiki/concepts/algoritmos-e-estruturas-de-dados]] — enriquecido com o framework de decisão por operação e as quatro perguntas
- [[wiki/concepts/array]] — citado como exemplo de acesso direto vs. varredura vs. deslocamento
- [[wiki/concepts/hashmap]] — citado no exemplo de busca por e-mail com índice
- [[wiki/concepts/fila]] — citado no exemplo de "próximo job"
- [[wiki/concepts/melhor-caso-pior-caso-caso-medio]] — novo conceito
- [[wiki/concepts/time-space-tradeoff]] — novo conceito (também fecha link quebrado citado por [[wiki/sources/two-sum-explicacao]], que já referenciava este conceito sem a página existir)
- [[wiki/concepts/algoritmos-de-busca]] — citado como exemplo do O(log n) (busca que descarta metade a cada passo)

## Open Questions

- O vídeo lista sinais de entrevista (duplicados, busca por chave, próximo/menor/caminho/prefixo) mas não mapeia explicitamente cada sinal à estrutura de destino — vale detalhar isso numa página futura de "padrões de entrevista técnica"?
- O framework de quatro perguntas é apresentado como ponto de partida — como ele se relaciona com os "três perguntas de decisão" já registradas em [[wiki/sources/estruturas-de-dados-pratica-array-hashmap-fila-pilha-arvore]]? Parecem complementares (um foca em qual estrutura, o outro em quando parar e medir custo), mas não foram explicitamente reconciliados pela fonte.
