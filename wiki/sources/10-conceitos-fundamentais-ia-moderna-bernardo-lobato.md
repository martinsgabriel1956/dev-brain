---
type: source
title: "10 conceitos fundamentais para entender a IA moderna"
aliases: ["10 conceitos ia moderna", "mapa mental da ia", "ia generativa llm agentes bernardo lobato"]
date_created: 2026-10-14
date_updated: 2026-10-14
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/10-conceitos-fundamentais-ia-moderna-bernardo-lobato.md
source_url: ""
author: "Bernardo Lobato"
date_published: ""
date_ingested: 2026-10-14
source_count: 1
tags: [ia, machine-learning, deep-learning, redes-neurais, transformers, tokens, llm, ia-generativa, agentes-ia, fundamentos, hype]
skill: tech-mentor-ai
status: stable
---

## TL;DR

[[wiki/entities/bernardo-lobato|Bernardo Lobato]] constrói um **mapa mental** da IA moderna em cadeia histórica, em que cada conceito resolve a limitação do anterior: [[wiki/concepts/inteligencia-artificial]] (guarda-chuva, 1956) → [[wiki/concepts/sistema-especialista]] (regras escritas à mão) → [[wiki/concepts/machine-learning]] (aprender de exemplos) → [[wiki/concepts/modelo-de-machine-learning|modelo]] → [[wiki/concepts/rede-neural-artificial]] (+ [[wiki/concepts/backpropagation]]) → [[wiki/concepts/deep-learning]] (profundidade) → [[wiki/concepts/ia-generativa]] (objetivo: criar conteúdo) → [[wiki/concepts/transformer-architecture|Transformer]] e [[wiki/concepts/self-attention|atenção]] → [[wiki/concepts/tokenizacao|tokens]] → [[wiki/concepts/llm-large-language-model|LLM]] (probabilístico) → [[wiki/concepts/agente-ia|agentes]]. Tese: entender a evolução separa **fundamento de buzzword** ([[wiki/concepts/hype-de-ia]]). Um LLM não é tecnologia nova, e sim a combinação de deep learning + Transformer em escala; um agente não é um modelo novo, e sim uma aplicação em volta de um modelo.

## Key Claims

**Claim:** IA é a área ampla (1956, Dartmouth); ChatGPT é só uma aplicação recente.
**Evidence:** definição + marco histórico citado.
**Confidence:** alta. [external] Proposta de Dartmouth, 1956 (https://www-formal.stanford.edu/jmc/history/dartmouth/dartmouth.html).

**Claim:** Sistemas especialistas (anos 70–80) são declarativos: base de conhecimento + motor de inferência, em Prolog/Lisp; só escalam enquanto alguém consegue escrever todas as regras.
**Evidence:** exemplo do empréstimo (renda/score); contraste com código imperativo.
**Confidence:** alta; o autor avisa que é simplificação grosseira. Ver [[wiki/concepts/sistema-especialista]].

**Claim:** ML troca "ensinar regras" por "ensinar com exemplos": algoritmo ajusta parâmetros para reduzir o erro (otimização matemática). Termo cunhado por Arthur Samuel em 1959 (damas, IBM).
**Evidence:** filtro de spam; exemplo `preço = A × área + B` com ajustes sucessivos de A.
**Confidence:** alta. [external] Samuel, 1959, *IBM Journal of Research and Development*. Ver [[wiki/concepts/machine-learning]], [[wiki/concepts/aprendizado-supervisionado]], [[wiki/entities/arthur-samuel]].

**Claim:** O **modelo** é o artefato treinado (representação matemática dos padrões); o que se salva e roda em produção é o modelo, não os dados de treino. GPT-4, Claude 3 Opus, Gemini são modelos diferentes — por isso respondem diferente à mesma pergunta.
**Evidence:** exemplo do imóvel.
**Confidence:** alta; ver [[wiki/concepts/modelo-de-machine-learning]].

**Claim:** Redes neurais = neurônios simples (entradas × pesos → saída) em cadeia; a inteligência emerge do conjunto. Treino por erro → backpropagation → ajuste de pesos; a rede descobre sozinha quais traços importam (sem regra do tipo "o 5 tem curva embaixo").
**Evidence:** exemplo dos dígitos 28×28 (784 entradas, 10 saídas).
**Confidence:** alta; simplificação didática (o exemplo omite função de ativação, viés e descida de gradiente). Ver [[wiki/concepts/rede-neural-artificial]], [[wiki/concepts/backpropagation]].

**Claim:** Linha do tempo: McCulloch–Pitts (1943), Perceptron (Rosenblatt, 1958), *Perceptrons* de Minsky–Papert (1969) → primeiro inverno da IA; backpropagation popularizado em 1986; AlexNet vence a ImageNet em 2012.
**Evidence:** cronologia narrada.
**Confidence:** alta. [external] Rumelhart, Hinton & Williams, *Nature*, 1986 (https://www.nature.com/articles/323533a0); Krizhevsky, Sutskever & Hinton, NIPS 2012. Nuance: a limitação provada em 1969 vale para o perceptron **de camada única** (ex.: XOR), não para redes multicamada em geral. Ver [[wiki/concepts/inverno-da-ia]], [[wiki/entities/frank-rosenblatt]], [[wiki/entities/alexnet]].

**Claim:** Deep learning = redes com muitas camadas ocultas; cada camada aprende um nível de abstração (bordas → olhos/nariz/boca → rosto), sem ninguém programar isso; ocorreu a convergência de dados + GPUs + técnicas de treino.
**Evidence:** exemplo de reconhecimento de rosto; visualização de ativações citada sem detalhe.
**Confidence:** média-alta (hierarquia de features é bem documentada em visão computacional, mas não vale por igual para todas as arquiteturas). Ver [[wiki/concepts/deep-learning]].

**Claim:** IA generativa define-se pelo **objetivo** (criar conteúdo novo a partir de um prompt), não por uma tecnologia específica; combina padrões aprendidos, não "criatividade" humana.
**Evidence:** ChatGPT (texto) vs. Midjourney (imagem).
**Confidence:** alta; ver [[wiki/concepts/ia-generativa]].

**Claim:** O Transformer (Google, 2017) processa todos os tokens de um trecho **simultaneamente** e usa **atenção** para pesar quais importam para cada token; isso permite treino paralelo em GPUs e modelos maiores. É uma arquitetura de rede neural (continua sendo deep learning).
**Evidence:** exemplos "ele/ela" (animal/rua) e "banco" (instituição/praça).
**Confidence:** alta. Ver [[wiki/concepts/transformer-architecture]], [[wiki/concepts/self-attention]], [[wiki/entities/attention-is-all-you-need-paper]].

**Claim:** A geração é **token a token**: prevê o próximo token mais provável, anexa à entrada e repete ("autocomplete com lasers"); a rede "nunca planeja o texto inteiro antes".
**Evidence:** exemplo "O céu é azul…".
**Confidence:** média. Boa descrição do laço autorregressivo, mas a afirmação de "nunca planeja" é contestada. [external] pesquisa de interpretabilidade da Anthropic encontrou planejamento antecipado (ex.: escolher a rima antes de escrever o verso) — https://www.anthropic.com/research/tracing-thoughts-language-model. Tratar como simplificação didática. Ver [[wiki/concepts/llm-large-language-model]].

**Claim:** O modelo nunca vê palavras, só IDs numéricos de tokens; o ID não tem significado próprio. Janela de contexto e cobrança são medidas em tokens, não palavras; em português ≈ 1,3–1,7 tokens/palavra.
**Evidence:** exemplo "cachorro correu"; janela de 128k tokens ≠ 128k palavras.
**Confidence:** média-alta (a razão varia por tokenizador; o autor avisa que é aproximação). [skill: tech-mentor-ai] consistente com `fundamentals.md` (1 token ≈ 0,75 palavra em inglês, menos em português). Ver [[wiki/concepts/tokenizacao]], [[wiki/concepts/janela-de-contexto]], [[wiki/concepts/token-tax-multilingual]].

**Claim:** LLM = Transformer treinado em escala massiva de texto (centenas de bilhões de parâmetros); é **probabilístico**: pode responder diferente à mesma pergunta e não tem garantia de correção, porque prevê tokens e não consulta uma base de fatos.
**Evidence:** explicação do laço de previsão e consequências.
**Confidence:** alta; [skill: tech-mentor-ai] a variabilidade é controlável por temperatura (0 ≈ quase determinístico; não garante reprodutibilidade absoluta). Ver [[wiki/concepts/determinismo-vs-probabilismo-em-ia]], [[wiki/concepts/alucinacao-llm]].

**Claim:** Agente = sistema que usa um modelo como parte da tomada de decisão **e** interage com ferramentas/informação externa, executa ações e adapta-se aos resultados; o modelo vira um componente, cercado por infraestrutura (contexto, bancos, APIs). Não é um modelo novo.
**Evidence:** exemplo da viagem (sugerir vs. pesquisar, comparar, pedir aprovação e reservar).
**Confidence:** alta; alinhado com [[wiki/concepts/agente-ia]] e [[wiki/concepts/engenharia-de-ia-ao-redor-do-modelo]]. Opinião do autor (cautela com agentes e segurança até passarem no "teste do tempo") é **juízo pessoal**, sem dado empírico.

## Entities

[[wiki/entities/bernardo-lobato]] (autor), [[wiki/entities/arthur-samuel]], [[wiki/entities/frank-rosenblatt]], [[wiki/entities/alexnet]], [[wiki/entities/attention-is-all-you-need-paper]]. Citados sem página: Warren McCulloch e Walter Pitts (1943), Marvin Minsky e Seymour Papert (1969), Dartmouth (1956), Google, OpenAI/ChatGPT, Midjourney.

## Concepts

[[wiki/concepts/inteligencia-artificial]], [[wiki/concepts/sistema-especialista]], [[wiki/concepts/machine-learning]], [[wiki/concepts/aprendizado-supervisionado]], [[wiki/concepts/modelo-de-machine-learning]], [[wiki/concepts/rede-neural-artificial]], [[wiki/concepts/backpropagation]], [[wiki/concepts/inverno-da-ia]], [[wiki/concepts/deep-learning]], [[wiki/concepts/ia-generativa]], [[wiki/concepts/llm-large-language-model]], [[wiki/concepts/transformer-architecture]], [[wiki/concepts/self-attention]], [[wiki/concepts/tokenizacao]], [[wiki/concepts/janela-de-contexto]], [[wiki/concepts/agente-ia]], [[wiki/concepts/determinismo-vs-probabilismo-em-ia]], [[wiki/concepts/alucinacao-llm]], [[wiki/concepts/hype-de-ia]], [[wiki/concepts/ai-washing]], [[wiki/concepts/recurrent-neural-network]].

## Open Questions

- O título promete "10 conceitos", mas o vídeo cobre ~11 (IA, sistemas especialistas, ML, modelo, redes neurais, deep learning, IA generativa, Transformers/atenção, tokens, LLM, agentes); a contagem não é explícita.
- Não cobre: aprendizado não supervisionado/por reforço (só citados), RLHF/pós-treino, fine-tuning, RAG, embeddings, multimodalidade, MCP. Ligação natural com [[wiki/concepts/embedding-vectors]] fica implícita.
- "Agente" é definido de forma ampla; sem critério de fronteira entre workflow com LLM e agente autônomo.
- "Nunca planeja o texto" vs. evidência de planejamento interno (ver Key Claims).
- Não há dados que sustentem a cautela do autor sobre agentes e segurança.

## Raw Quotes

> "A inteligência vem do especialista que escreve as regras e não é gerada automaticamente."

> "Em vez de ensinar regras passamos a ensinar através de exemplos."

> "É basicamente um autocomplete com lasers."

> "Um agente não é necessariamente um novo modelo. Na maioria das vezes ele é uma aplicação construída sobre modelos que já conhecemos."

> "Cada conceito surgiu para resolver um nicho de problema específico."
