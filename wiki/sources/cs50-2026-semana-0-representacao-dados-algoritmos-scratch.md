---
type: source
title: "CS50 2026 — Semana 0: IA, Representação de Dados, Algoritmos e Scratch"
aliases: ["CS50 semana 0", "CS50 aula de abertura 2026", "David Malan aula 1 CS50"]
date_created: 2026-08-24
date_updated: 2026-08-24
source_count: 0
tags: [cs50, david-malan, cs-fundamentals, binario, ascii, unicode, algoritmos, big-o, scratch, harvard, openai, system-prompt, pseudocodigo]
skill: cs-fundamentals
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/cs50-2026-semana-0-representacao-dados-algoritmos-scratch.md
source_url:
author: David Malan
date_published:
date_ingested: 2026-08-24
---

# CS50 2026 — Semana 0: IA, Representação de Dados, Algoritmos e Scratch

## TL;DR

Transcrição da aula de abertura do [[wiki/concepts/cs50|CS50]] (Harvard) por [[wiki/entities/david-malan]], cobrindo a semana 0 do curso na íntegra: (1) uma demo ao vivo de chatbot em ~10 linhas de Python usando a API da [[wiki/entities/openai]], introduzindo **system prompt vs. user prompt** da forma mais crua possível (chamada direta à API, sem harness); (2) representação de dados — unário, binário, [[wiki/concepts/sistema-binario-bit-byte|bit e byte]], [[wiki/concepts/ascii|ASCII]], [[wiki/concepts/unicode|Unicode]]/emoji, cores RGB, vídeo e som, todos reduzidos ao mesmo princípio (zeros e uns + convenção de interpretação); (3) [[wiki/concepts/algoritmos-de-busca|algoritmos de busca]] via a analogia física de um catálogo telefônico (linear vs. binária) e as curvas de [[wiki/concepts/big-o|Big O]] resultantes; (4) pseudocódigo e a terminologia central de funções/condicionais/booleanos/loops; e (5) uma introdução extensa e prática ao [[wiki/concepts/scratch-linguagem-de-blocos|Scratch]], incluindo dois projetos completos construídos incrementalmente ("Oscar Time" e "IB's Hardest Game"). É a fonte mais didática e "primeiros princípios" que a wiki tem hoje para ASCII/binário/Big O — as fontes anteriores (`10-conceitos-fundamentais-computacao`, `conceitos-que-regem-a-computacao-bits-turing-complexidade`, `codificacao-de-caracteres-ascii-iso-8859-1-unicode`) já cobriam o conteúdo técnico, mas esta acrescenta as analogias físicas exatas usadas em sala (demonstração com voluntários soletrando "BOW", lâmpadas contando de 0 a 7, catálogo telefônico de "John Harvard") e, pela primeira vez na wiki, uma demo mínima e totalmente sem harness da distinção system prompt/user prompt.

## Key Claims

**Claim:** O bit é representável fisicamente por eletricidade presente/ausente (transistor ligado/desligado) porque distinguir dois estados (fluindo/não fluindo) é mais simples e robusto de construir em hardware do que distinguir múltiplos níveis de voltagem — e é esse motivo de robustez de engenharia, não uma limitação matemática, que explica por que os computadores usam base 2 e não base 10.
**Evidence:** Demonstração com lâmpadas físicas contando de 0 a 7 usando 3 posições de peso 4/2/1, espelhando exatamente o mesmo sistema aplicado a dedos humanos (base 2) vs. contagem ingênua de dedos levantados (que só chega a 5).
**Confidence:** alta — consistente com [[wiki/concepts/sistema-binario-bit-byte]], que já registrava esse ponto de forma mais textual ("confiabilidade é a razão de fundo"); esta fonte acrescenta a demonstração física passo a passo que não estava documentada antes.

**Claim:** Diferença entre maiúscula e minúscula em ASCII é de exatamente 32 posições na tabela (ex.: 'A'=65, 'a'=97) — o que significa que, em binário, alternar caixa alta/baixa de uma letra é literalmente ligar/desligar um único bit (o bit de valor 32) no padrão de 8 bits do caractere.
**Evidence:** Comparação lado a lado dos códigos ASCII de A–G (65–71) e a–g (97–103) na aula, com a subtração explícita (97−65=32, 98−66=32...) e a demonstração de que somar 32 ao padrão binário de 'A' produz exatamente o padrão de 'a'.
**Confidence:** alta — fato tabular verificável; primeira vez que a wiki registra esse detalhe específico (a relação matemática exata entre caixa alta e baixa em ASCII), apesar de [[wiki/concepts/ascii]] já ter a tabela geral de mapeamento.

**Claim:** Um emoji não é uma imagem — é um caractere, cujo padrão de bits é padronizado globalmente pelo Unicode Consortium; a aparência visual (o desenho gráfico específico) é decidida individualmente por cada fabricante (Apple, Google, Microsoft, Telegram), o que explica por que o "mesmo" emoji parece (ou se anima) diferente em plataformas diferentes.
**Evidence:** Exemplo concreto do emoji "rosto chorando de rir" (32 bits, valor decimal ~4.036.991.106) mostrado em três renderizações visuais diferentes (iOS, Google, Telegram animado) representando o mesmo codepoint.
**Confidence:** alta — consistente com [[wiki/concepts/unicode]] (que já distingue charset de encoding), mas esta é a primeira fonte da wiki a aplicar essa distinção especificamente a emoji e a mostrar o exemplo visual de divergência entre plataformas.

**Claim:** Busca linear em um catálogo telefônico ordenado, mesmo "otimizada" para pular 2 páginas por vez, continua sendo uma curva **linear** (O(n)) — apenas com constante melhor — enquanto o algoritmo de "dividir sempre ao meio" produz uma curva **logarítmica** (O(log n)), cuja vantagem prática cresce dramaticamente à medida que o problema dobra de tamanho (catálogo de 1000 → 2000 páginas: os dois primeiros algoritmos dobram de tempo; o terceiro precisa de só mais um passo de divisão).
**Evidence:** Três algoritmos passo a passo demonstrados fisicamente com um catálogo telefônico real de ~1000 páginas, buscando "John Harvard"; gráfico de tempo × tamanho do problema desenhado ao vivo comparando as três curvas.
**Confidence:** alta — reforça o que [[wiki/concepts/big-o]] e [[wiki/concepts/algoritmos-de-busca]] já documentavam formalmente (O(n) vs. O(log n), 30 comparações em 1 bilhão de elementos), mas com uma analogia física passo a passo (incluindo o algoritmo intermediário "pule 2 páginas", que ilustra que otimizar a constante não muda a classe de complexidade) que a wiki não tinha registrada.

**Claim:** Todo algoritmo correto de busca binária/divisão precisa tratar explicitamente o caso de borda "o item não está na coleção" — sem esse ramo, o pseudocódigo (e, por extensão, o programa real) fica com comportamento indefinido, o que na prática se manifesta como travamentos ou reinícios espontâneos de software.
**Evidence:** Construção incremental do pseudocódigo do algoritmo de busca binária no catálogo telefônico, adicionando o passo "senão, desista" apenas depois de a plateia apontar a ausência desse caso.
**Confidence:** alta — ponto pedagógico específico sobre engenharia defensiva/casos de borda que não estava registrado na wiki associado a busca binária; complementa [[wiki/concepts/algoritmos-de-busca]] com a motivação de *por que* tratar esse caso.

**Claim:** A distinção entre system prompt (instruções fixas, injetadas pelo programador, controlando o comportamento do modelo em toda chamada) e user prompt (a entrada específica do usuário) pode ser demonstrada da forma mais crua possível: uma chamada direta e sem harness à API da OpenAI (`client.responses.create`, parâmetros `input` e `instructions` separados), sem nenhuma camada de rules/skills/MCP por cima.
**Evidence:** Progressão ao vivo do código: (1) prompt hard-coded → (2) prompt dinâmico via `input()` → (3) separação explícita em `user_prompt` (parâmetro `input`) e `system_prompt` (parâmetro `instructions`, ex.: "Limite sua resposta a uma frase" ou "Finja que você é um gato") — o modelo usado é `gpt-5` via a Responses API.
**Confidence:** alta — [[wiki/concepts/system-prompt-arquitetura]] já documentava a distinção em contexto de harness de codificação (Claude Code, Cursor); esta é a primeira fonte da wiki a mostrar a distinção isolada da complexidade de um harness, no nível mais elementar possível — útil como material didático de referência para "o que é system prompt, sem nenhuma camada extra".

**Claim:** Scratch (MIT Media Lab, ~20 anos de existência) representa graficamente, via blocos de drag-and-drop, exatamente os mesmos quatro conceitos fundamentais que sustentam linguagens textuais como C e Python: funções (blocos como `fale`, que recebem argumentos e podem ter efeito colateral ou retornar valor), condicionais (`se/senão`), expressões booleanas (perguntas como `tocando no ponteiro do mouse?`) e loops (`repita`, `para sempre`).
**Evidence:** Sequência completa de exemplos construídos ao vivo — de "Hello world" a um chatbot de voz, passando por um bug clássico de sincronização (duas falas sequenciais rápidas demais para o olho humano perceber, corrigido com `wait` ou composição via `join`), blocos customizados (abstração/definição de função própria) e dois jogos completos (Oscar Time, IB's Hardest Game).
**Confidence:** alta — primeira fonte da wiki dedicada inteiramente a Scratch como linguagem introdutória; não havia página própria para o conceito antes desta ingestão.

**Claim:** Em Scratch, a diferença entre "efeito colateral" (side effect) e "valor de retorno" (return value) é didaticamente visível: o bloco `fale` produz um efeito colateral imediato e visível ao humano (balão de fala na tela); o bloco `pergunte...e espere` não tem efeito colateral imediato — ele retorna um valor (armazenado na variável `resposta`), visível apenas ao código, que só se torna visível ao humano quando explicitamente usado (ex.: composto dentro de outro `fale`).
**Evidence:** Demonstração ao vivo com bug incluído: encadear `pergunte` e `fale` sequencialmente falha visualmente (a fala do "hello" já desapareceu antes do usuário digitar a resposta) até a introdução de `wait` ou, de forma mais elegante, o bloco `junte` (join) compondo as duas strings em uma única chamada de `fale`.
**Confidence:** alta — distinção conceitual (side effect vs. return value) que a wiki não tinha nomeada explicitamente antes desta fonte, embora [[wiki/concepts/system-prompt-arquitetura]] e outras páginas de programação já usassem os termos implicitamente.

## Entities & Concepts Touched

- [[wiki/concepts/cs50]]
- [[wiki/entities/david-malan]]
- [[wiki/concepts/ascii]]
- [[wiki/concepts/unicode]]
- [[wiki/concepts/sistema-binario-bit-byte]]
- [[wiki/concepts/big-o]]
- [[wiki/concepts/algoritmos-de-busca]]
- [[wiki/concepts/algoritmos-e-estruturas-de-dados]]
- [[wiki/concepts/system-prompt-arquitetura]]
- [[wiki/entities/openai]]
- [[wiki/concepts/scratch-linguagem-de-blocos]]
- [[wiki/entities/mit-media-lab]]
- [[wiki/entities/harvard-university]]

## Open Questions

- A aula usa `client.responses.create(...)` com `model="gpt-5"` — a wiki (via [[wiki/entities/openai]]) já registra "GPT 5.6" e "Sol" como apelidos de modelos frontier recentes citados em outras fontes, mas não tem uma linha do tempo clara de nomenclatura de versões GPT-5.x; não é possível, a partir só desta fonte, situar "gpt-5" na cronologia de versões já documentada.
- A fonte não detalha a implementação de baixo nível de nenhum dos algoritmos de ordenação usados como pré-requisito da busca binária no catálogo telefônico (que já vem ordenado por convenção editorial, não por um algoritmo executado em tela) — complementar com [[wiki/concepts/algoritmos-de-ordenacao]] se uma fonte futura cobrir isso no contexto de Scratch/CS50.
- Não fica claro no material se o CS50.ai (o "pato de borracha virtual" citado) é construído sobre a mesma Responses API demonstrada na aula, ou uma stack diferente — ponto em aberto para uma eventual fonte futura sobre a arquitetura interna das ferramentas de IA do próprio curso.
