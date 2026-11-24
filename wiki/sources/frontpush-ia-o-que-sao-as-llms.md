---
type: source
title: "FrontPUSH, módulo de IA: o que são as LLMs? (parte 2)"
aliases: ["o que são as LLMs FrontPUSH", "LLM cospe texto", "quatro pilares de uma LLM", "módulo de IA FrontPUSH aula teórica 2"]
date_created: 2026-11-24
date_updated: 2026-11-24
source_count: 0
tags: [llm, transformer, tokenizacao, janela-de-contexto, attention, parametros, harness, alucinacao, context-compaction, sycophancy, probabilidade, fundamentos, ia]
skill: tech-mentor-ai
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/frontpush-ia-o-que-sao-as-llms.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-24
---

# FrontPUSH, módulo de IA: o que são as LLMs? (parte 2)

## TL;DR

Continuação de [[wiki/sources/frontpush-ia-o-que-voce-deve-saber-de-ia]], com cerca de 21 min e dois slides ("O que são LLM's?", pt. 1 e 2). [[wiki/entities/nasser|Násser]] retoma no [[wiki/concepts/deep-learning]] e define o [[wiki/concepts/llm-large-language-model|LLM]] como "modelos gigantescos de Deep Learning baseados em Transformers treinados em enormes volumes de texto". A imagem central é a de um **tradutor**: o deep learning seria "o árabe", e o LLM aprendeu a língua das pessoas (texto, cultura, contexto). Por isso "ela prevê o próximo token. Só isso. Mas em escala gigantesca. Feito pra 'cuspir' texto". A aula mostra o fluxo prompt → [[wiki/concepts/tokenizacao|tokens]] → [[wiki/concepts/janela-de-contexto|janela de contexto]] → [[wiki/concepts/transformer-architecture|Transformer]] → probabilidades → próximo token → repete. Fecha com os **quatro pilares**: tokens, contexto, [[wiki/concepts/self-attention|attention]] e parâmetros. No meio, trata de [[wiki/concepts/alucinacao-llm|alucinação]] por falta de contexto, da perda de informação em chats longos ([[wiki/concepts/degradacao-de-contexto]], [[wiki/concepts/context-compaction]]) e do recurso finito (energia, água, GPUs). O fluxo e os pilares do slide estão certos. A fala erra em cinco pontos: chama de "[[wiki/concepts/harness]]" a arquitetura do modelo e o raciocínio interno; trata o LLM como uma camada sobre "outro" deep learning; afirma que o modelo reajusta os pesos quando o usuário diz "você errou"; confunde parâmetros com janela de contexto; e compara tokens a "palavras-chave" de um mapa mental. Ver Contradições.

## Key Claims

### Do deep learning ao LLM

- Recap: o deep learning resolve "os milhões de parâmetros" das redes neurais, que imitam o cérebro ("milhões de sinapses"), com GPU, CPU, Big Data, arquiteturas e modelos. O Big Data serve "para poder essa primeira probabilidade ser mais rápida"; a GPU "é a resposta do cálculo da probabilidade em si".
- **Definição (slide pt. 1):** "Modelos gigantescos de Deep Learning baseados em Transformers treinados em enormes volumes de texto" ([[wiki/concepts/llm-large-language-model]], [[wiki/concepts/transformer-architecture]]).
- Ele avisa que a aula é "uma forma didática, não é extremamente técnica", "pelo menos é um guia", e que é preciso estudar à parte.

### O LLM como tradutor

- Programador "sabe mexer" com ML, redes neurais e deep learning porque precisa do conhecimento técnico; com ChatGPT, Gemini e [[wiki/entities/claude-code|Claude Code]], "você consegue conversar com ele como um ser humano normal".
- "Vai lá conversar com rede neural sem um LLM [...] ela não vai entender nada." O LLM "veio como um agente para poder atuar como um tradutor": "o árabe é o machine learning, é a rede neural, é o deep learning".
- Para isso, o LLM "teve que aprender como o ser humano se comunica": como conecta palavras e ideias, cultura, contexto. Analogia: um estrangeiro vindo da Índia pode até "saber brasileiro", mas sem a cultura "não vai entender".

### Próximo token em escala gigantesca

- **Slide pt. 1:** "Ela prevê o próximo token. Só isso. Mas em escala gigantesca. Feito pra 'cuspir' texto." Três escalas: dados massivos (livros, artigos, código, internet, fóruns), parâmetros massivos ("bilhões, trilhões") e computação absurda ("GPUs, velocidade...").
- **ENEM (slide):** "Imagine que você vai fazer o ENEM mas pode consultar a internet inteira e você tem a velocidade de um computador." Conclusão: "Uma LLM não sabe respostas. Ela calcula probabilidades."
- **Exemplo (slide):** "O céu está..." → azul 74%, limpo 13%, bonito 7%, escuro 3%. Na fala, ela "define a próxima palavra com uma árvore de possibilidades".

### "Harness", contexto e prompt

- "A gente vai começar a falar dos conceitos de [...] harness, que são os modelos da ligada à arquitetura. [...] contexto e a construção disso é o prompt." Também: "sempre que eu falar harness, pensa e lembre-se da arquitetura do modelo". Ver Contradições.
- "Dependendo do modelo ela fica perguntando para ela mesma até ela chegar em uma resposta que você não precise corrigir." Quando "a inteligência artificial está pensando, ela está lá atrás perguntando para o harness" ([[wiki/concepts/reasoning-level]]).
- O ChatGPT antigo errava, "principalmente o código", e respondia "nossa, é verdade, você tem razão" ([[wiki/concepts/bajulacao-llm]]). Hoje melhora "a cada versão do ChatGPT, a cada versão do Claude Code", e ele cita o "modelo Mythos lá da [[wiki/entities/anthropic|Anthropic]]". O mercado fica para aulas futuras.

### Contexto, alucinação e recurso finito

- Sem contexto "minimamente correto", "ela vai começar a alucinar, vai começar a inventar" ([[wiki/concepts/alucinacao-llm]]). Pedido genérico → resposta genérica; no trabalho, "a gente precisa especificar".
- "Definir um bom contexto, mas ao mesmo tempo não estourar quantidade de parâmetros": "a inteligência artificial sempre vai tentar resumir e quando você resume, você perde informação" ([[wiki/concepts/context-compaction]]).
- Confiabilidade: o modelo "confirma" informações "em vários lugares"; "quanto mais lugares falam a mesma coisa", mais confiável. Talvez haja "um parâmetro de quais são as fontes mais confiáveis".
- **Recurso finito:** "não existe só você no mundo"; não há energia nem "água no mundo para poder resfriar" computadores infinitos. A IA "não vai gastar todo o dinheiro dele com você", ou cobra mais.
- "Não adianta você colocar mais parâmetro, mais poder computacional, então tem um gráfico que mostra isso." O gráfico não aparece nesta aula ([[wiki/concepts/scaling-laws]]).
- Quanto mais tempo no chat "mais informação se perde", porque o contexto "vai aumentando" e o sistema tenta "enxugar" num "mapa mental" ([[wiki/concepts/degradacao-de-contexto]]).

### Do prompt à resposta final (slide pt. 2)

- "As pessoas acreditam que uma LLM entende exatamente o que está escrevendo. Na realidade, ela foi treinada em bilhões de exemplos de linguagem humana."
- Fluxo: usuário escreve um prompt → texto dividido em tokens → tokens entram na janela de contexto → o Transformer analisa as relações entre todos os tokens → o modelo calcula probabilidades → escolhe o próximo token → repete "centenas de vezes" → resposta final.
- **Os quatro pilares de uma LLM:** (1) **Tokens**: "a menor unidade de informação que o modelo consegue processar" ([[wiki/concepts/tokenizacao]]). (2) **Contexto**: "toda a informação que a IA consegue 'enxergar' naquele momento" ([[wiki/concepts/janela-de-contexto]]). (3) **Attention**: "o mecanismo que determina quais partes do contexto são mais importantes para gerar a próxima resposta"; na fala, "mais ou menos é a rede neural, colocando um peso matemático" ([[wiki/concepts/self-attention]]). (4) **Parâmetros**: "os bilhões de pesos matemáticos ajustados durante o treinamento que armazenam os padrões aprendidos".
- Ele compara a abstração à de aprender orientação a objetos e diz que vai reforçar tudo "por meio da prática".

## Contradições e precisões

- **"Harness" ≠ arquitetura do modelo.** Na wiki, [[wiki/concepts/harness]] é tudo *ao redor* do modelo: laço do agente, tools, contexto, memória, system prompt. A arquitetura é o Transformer e seus pesos. O "perguntar para ela mesma" é raciocínio interno, com tokens de thinking ([[wiki/concepts/reasoning-level]], [[wiki/concepts/chain-of-thought]]), um comportamento do modelo treinado para isso. A compactação de chats longos, por outro lado, é mesmo tarefa do harness ([[wiki/concepts/context-compaction]]). Na escada da [[wiki/sources/frontpush-ia-o-que-voce-deve-saber-de-ia|parte 1]], "Harness" é um degrau próprio, depois de LLMs, o que contradiz a definição desta aula. Confiança alta.
- **O LLM não é um tradutor sobre outro deep learning.** O próprio slide diz que o LLM *é* um modelo de deep learning. Não existe uma rede "árabe" separada que ele traduza; a linguagem e o "conhecimento" ficam nos mesmos pesos. A metáfora serve para a interface (falar em linguagem natural), não para a arquitetura. Confiança alta.
- **Corrigir o modelo não muda os pesos.** Na inferência, os pesos estão congelados. "Nossa, é verdade, você tem razão" é **bajulação** (*sycophancy*), uma tendência que vem do treino com preferência humana ([[wiki/concepts/bajulacao-llm]]). A correção vale para a conversa só porque fica no contexto; feedback de usuários pode entrar num treino *futuro*, mas não ajusta "novos parâmetros de pesos matemáticos" ali, na hora. [external] Sharma et al., "Towards Understanding Sycophancy in Language Models" (2023), https://arxiv.org/abs/2310.13548. Confiança alta.
- **Parâmetros ≠ contexto.** "Estourar a quantidade de parâmetros" com um prompt grande não acontece: parâmetros são os pesos fixos do modelo, e o limite é a janela de contexto, em tokens. O slide separa os dois pilares corretamente. O modelo também não "sempre vai tentar resumir" a cada prompt: quem resume é o harness, ao chegar perto do limite (por exemplo, o auto-compact do [[wiki/entities/claude-code|Claude Code]]). Antes disso, o problema é a [[wiki/concepts/degradacao-de-contexto|degradação]], porque o modelo usa pior o meio de contextos longos. [external] Liu et al., "Lost in the Middle" (2023), https://arxiv.org/abs/2307.03172. Confiança alta.
- **Token não é palavra-chave.** Tokens são pedaços de subpalavra definidos pelo tokenizador (BPE etc.), incluindo conjunções, pontuação e espaços. Não há seleção de "palavras-chave" nem "mapa mental" na tokenização. O mapa mental descreve a compactação de contexto, não os tokens ([[wiki/concepts/tokenizacao]]). Confiança alta.
- **"Confirma em vários lugares".** Sem ferramenta de busca, o modelo não consulta fontes na hora: a repetição de um fato nos dados de treino aumenta a chance de reproduzi-lo, mas não é verificação. A busca na web, quando existe, é uma tool do harness. Confiança alta.
- **"Não adianta mais parâmetro".** As [[wiki/concepts/scaling-laws]] mostram retorno decrescente (lei de potência), não retorno nulo; o ganho recente veio também de dados, pós-treino e computação no tempo de inferência. O gráfico prometido ficou para depois. Confiança média-alta.
- **Recurso finito.** Correto como ordem de grandeza: data centers consumiram cerca de 1,5% da eletricidade mundial em 2024, com a IA puxando o crescimento. [external] IEA, "Energy and AI" (2025), https://www.iea.org/reports/energy-and-ai. Confiança média-alta (sem fetch).
- **Mythos.** [external] A Anthropic anunciou o Claude Mythos Preview em abril de 2026, com acesso restrito. Confiança média (sem fetch).
- **Lapsos literais no raw:** "modelos da ligada à arquitetura", "qualquer pessoa utilizada em inteligência artificial", "a inteligência artificial, que antes era uma árabe", "das probabilidades que ela travou", "um número mais maior de dados", "esse tante computador", "como extraiu melhor dela".

## Entities

- [[wiki/entities/nasser]]: instrutor.
- [[wiki/entities/frontpush]]: curso, módulo de IA.
- [[wiki/entities/anthropic]]: Mythos, Claude.
- [[wiki/entities/claude-code]]: exemplo de chat e de agente de código.
- [[wiki/entities/openai]]: ChatGPT e Codex.

## Concepts

- [[wiki/concepts/llm-large-language-model]], [[wiki/concepts/transformer-architecture]], [[wiki/concepts/deep-learning]]
- [[wiki/concepts/tokenizacao]], [[wiki/concepts/janela-de-contexto]], [[wiki/concepts/self-attention]]
- [[wiki/concepts/harness]], [[wiki/concepts/reasoning-level]], [[wiki/concepts/chain-of-thought]]
- [[wiki/concepts/alucinacao-llm]], [[wiki/concepts/degradacao-de-contexto]], [[wiki/concepts/context-compaction]]
- [[wiki/concepts/bajulacao-llm]], [[wiki/concepts/scaling-laws]]

## Open Questions

- O "gráfico" da limitação: são as scaling laws, retornos decrescentes de pré-treino ou outro? Prometido para depois.
- Nas próximas aulas, "harness" vai virar o sentido usado na wiki (o entorno do modelo) ou continuar como "arquitetura"?
- Os percentuais do "céu está" (74/13/7/3) são ilustrativos ou vêm de algum modelo real? Não há fonte.

## Raw Quotes

- "O LLM veio meio que como se fosse um tradutor."
- "Ela prevê o próximo token, mas em uma escala gigantesca, feita para cuspir texto."
- "Se você der um contexto muito grande, por mais específico que seja, você estoura a quantidade de parâmetros."
- "Não existe água no mundo para poder resfriar esse tante computador para poder ter um recurso infinito."
- "Sempre que eu falar harness, pensa e lembre-se da arquitetura do modelo."
