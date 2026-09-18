---
type: concept
title: "Embedding Vectors"
aliases: ["embeddings de token", "word embeddings", "token embeddings", "matriz de embeddings"]
date_created: 2026-09-18
date_updated: 2026-09-18
source_count: 1
tags: [embeddings, llm-fundamentals, tokenizacao, transformers, self-attention]
skill: tech-mentor-ai
status: stable
---

## Definição

Representação numérica (um vetor de N números) do significado de um [[tokenizacao|token]]. Diferente do ID de vocabulário do token (que só indica sua posição numa lista, sem carregar significado), o embedding vector é o resultado de um treinamento que posiciona cada token num espaço multidimensional onde proximidade espacial reflete proximidade semântica.

> Nota: esta página cobre especificamente **token/word embeddings** dentro da arquitetura Transformer (fase de input). Para embeddings de **busca semântica/RAG** (ex. `text-embedding-3-small`, cosine similarity, vector stores), ver a seção "Embeddings e Busca Semântica" em `tech-mentor-ai/references/ai/fundamentals.md` — aplicação de produto distinta, mesmo princípio matemático de base.

## Como a Matriz de Embeddings é Formada

1. Cada token do vocabulário recebe um vetor **aleatório** no início do treinamento. O tamanho do vetor é decidido previamente (ex.: GPT-2 usa 768 posições) e é fixo para todo o vocabulário daquele modelo.
2. Durante o treinamento, o modelo é exposto a volumes massivos de texto e ajusta esses vetores para capturar padrões linguísticos: quais palavras aparecem juntas, quais são semanticamente opostas, etc. — um mapa multidimensional, não redutível a 2 eixos.
3. Ao final do treino, a matriz de embeddings fica fixa: uma tabela de lookup ID → vetor, usada em toda inferência subsequente daquele modelo.

## Limitação Central: Significado Geral, Não Contextual

Um embedding vector representa a média de **todos** os usos do token no corpus de treino — não o significado específico numa frase. Exemplo: o embedding de "banco" carrega sinais tanto para "instituição financeira" quanto para "assento", porque o modelo viu ambos os usos durante o treino. Resolver qual significado se aplica a uma frase específica é o trabalho do [[self-attention|mecanismo de self-attention]], não do embedding isoladamente.

## Demonstrações Visuais do Espaço de Embeddings

- **Hugging Face** — guia intuitivo de embeddings mostra palavras plotadas por proximidade semântica (ex. "golden" no lado oposto de "owl"; "ocean" perto de "cobra"). Ver [[wiki/entities/hugging-face]].
- **TensorFlow Embedding Projector** ([[wiki/entities/google]]) — ferramenta de busca por vizinhos no espaço multidimensional: "Apple" → "Macintosh", "Microsoft", "IBM"; "tree" → "forest", "leaf", "plant", "flowers".

## Conexões

- [[tokenizacao]] — etapa anterior: texto → tokens → IDs; embeddings traduzem o ID em significado
- [[self-attention]] — usa embeddings como input para calcular contexto (Q/K/V derivados deles)
- [[positional-encoding]] — vetor somado ao embedding para injetar informação de ordem
- [[transformer-architecture]] — arquitetura onde embeddings são a primeira camada de processamento

## Key Sources

- [[wiki/sources/self-attention-mecanismo-transformers]] — explicação didática de como a matriz de embeddings é treinada e por que sozinha não resolve ambiguidade contextual; cita demonstrações do Hugging Face e do TensorFlow Embedding Projector
