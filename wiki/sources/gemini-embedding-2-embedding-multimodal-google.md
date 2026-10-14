---
type: source
title: "Gemini Embedding 2 — embedding multimodal do Google (resumo técnico)"
aliases: ["Gemini Embedding 2", "embedding multimodal do Google"]
date_created: 2026-10-14
date_updated: 2026-10-14
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/gemini-embedding-2-embedding-multimodal-google.md
source_url: ""
author: "não identificado"
date_published: ""
date_ingested: 2026-10-14
source_count: 1
tags: [tech-mentor-ai, embeddings, multimodal, busca-semantica, rag, gemini, google, cnn, privacidade]
skill: tech-mentor-ai
status: stable
---

## TL;DR

Vídeo (PT-BR) que resume o [[wiki/entities/gemini-embedding-2]], modelo do [[wiki/entities/google]] que coloca **texto, imagem, vídeo, áudio e documentos num único espaço vetorial** ([[wiki/concepts/embedding-multimodal]]), com 100+ idiomas e até 3072 dimensões ([[wiki/concepts/reducao-de-dimensoes-de-embedding]]). O apresentador diz que é "bacana, mas não muda tudo": simplifica pipelines de [[wiki/concepts/busca-semantica]]/RAG, mas tem limites por chamada (obrigam [[wiki/concepts/chunking]]), **custo** de API e **risco de privacidade** ([[wiki/concepts/custo-e-privacidade-de-embedding-via-api]]). Compara com a abordagem leve de CNN/VGG16 ([[wiki/concepts/busca-visual-por-similaridade]]) e explica a intuição dos vetores com rei − homem + mulher ≈ rainha ([[wiki/concepts/aritmetica-de-vetores-semanticos]]).

## Key Claims

**Claim:** O modelo é multimodal: texto, imagens, vídeo, áudio e documentos no mesmo espaço de embedding, servindo a busca e classificação entre mídias; suporta 100+ idiomas, incluindo português.
**Evidence:** descrição do apresentador a partir da página do Google. **Confidence:** alta (afirmação do próprio fabricante, relatada de segunda mão). Ver [[wiki/concepts/embedding-multimodal]].

**Claim:** Limites por chamada: texto até 8.192 tokens; até 6 imagens; vídeo até 120 s (MP4/MOV); áudio sem transcrição (limite não informado); PDF até 6 páginas. Acima disso é preciso quebrar em pedaços, fazer várias chamadas e receber um vetor por pedaço.
**Evidence:** leitura da página do Google no vídeo. **Confidence:** média-alta (números podem mudar; [external] não verificados na doc oficial nesta ingestão). Ver [[wiki/concepts/chunking]].

**Claim:** No espaço unificado, conteúdos semanticamente iguais em mídias distintas (foto, vídeo e som de um cachorro latindo, mais o texto "o cachorro está latindo") formam um cluster; a distância usual é [[wiki/concepts/similaridade-de-cosseno]] (ou euclidiana).
**Evidence:** explicação com o diagrama do Google. **Confidence:** alta como princípio. Ver [[wiki/concepts/embedding-vectors]].

**Claim:** O máximo é 3072 dimensões; pedir menos faz o modelo calcular as 3072 e projetar para o tamanho menor. O Google recomenda o máximo; mais dimensões = mais dados para armazenar/buscar.
**Evidence:** fala do apresentador + documentação (Vertex). **Confidence:** média-alta ([skill: tech-mentor-ai] `embeddings-semantic-search.md` descreve o mesmo padrão de redução via *Matryoshka Embeddings* no `text-embedding-3-large`, 3072 dims reduzíveis; que o Gemini use MRL especificamente não foi dito no vídeo). Ver [[wiki/concepts/reducao-de-dimensoes-de-embedding]].

**Claim:** Embeddings têm significado nas **direções** do espaço, não em cada dimensão isolada; a aritmética rei − homem + mulher ≈ rainha ilustra isso (exemplo 3D didático, valores inventados).
**Evidence:** exemplo numérico no vídeo. **Confidence:** alta como intuição; o exemplo é ilustrativo e simplificado (a analogia vale aproximadamente em embeddings de palavras, não é exata). Ver [[wiki/concepts/aritmetica-de-vetores-semanticos]].

**Claim:** Nem sempre vale migrar: para busca visual de catálogo, um modelo CNN leve (ex.: VGG16 sem a cabeça de classificação) + cosseno já resolve e roda em hardware modesto; o multimodal compensa quando o cliente quer busca textual semântica ("blusa azul de telinha com botões"), vários vetores por produto e consulta por voz direto como áudio.
**Evidence:** cenário hipotético do apresentador (site de roupas). **Confidence:** média (raciocínio de engenharia, sem benchmark; ele diz que ainda não testou o modelo). Ver [[wiki/concepts/busca-visual-por-similaridade]], [[wiki/concepts/cnn-rede-neural-convolucional]].

**Claim:** Desvantagens: custo por chamada de API proprietária (alternativa: modelos open source separados) e necessidade de enviar dados ao Google, com provável autorização de uso para treino; para dados sensíveis, não usar.
**Evidence:** opinião do apresentador, que **não leu os termos de serviço**. **Confidence:** baixa-média para a parte de treino (especulação); alta para o trade-off geral. Ver [[wiki/concepts/custo-e-privacidade-de-embedding-via-api]], [[wiki/concepts/confidencialidade-de-dados-em-prompts-ia]].

**Claim:** O lançamento tende a estimular outros laboratórios a criar embeddings multimodais parecidos.
**Evidence:** previsão do apresentador. **Confidence:** opinião.

## Entities

[[wiki/entities/gemini-embedding-2]] (novo), [[wiki/entities/google]]. Apresentador não identificado.

## Concepts

Novos: [[wiki/concepts/embedding-multimodal]], [[wiki/concepts/aritmetica-de-vetores-semanticos]], [[wiki/concepts/reducao-de-dimensoes-de-embedding]], [[wiki/concepts/busca-visual-por-similaridade]], [[wiki/concepts/cnn-rede-neural-convolucional]], [[wiki/concepts/custo-e-privacidade-de-embedding-via-api]].
Ligados: [[wiki/concepts/embedding-vectors]], [[wiki/concepts/busca-semantica]], [[wiki/concepts/similaridade-de-cosseno]], [[wiki/concepts/vector-store]], [[wiki/concepts/chunking]], [[wiki/concepts/busca-por-palavra-chave]], [[wiki/concepts/rag-como-ferramenta-de-busca]], [[wiki/concepts/ocr]], [[wiki/concepts/recurrent-neural-network]].

## Open Questions

- Qual a precisão real do Gemini Embedding 2 vs. CLIP/ImageBind e vs. pipelines separados? (nenhum teste no vídeo)
- Preço por modalidade e política de dados/treino nos termos de serviço (não verificados).
- Como combinar vários vetores por item (imagem + metadados) no ranking final?

## Raw quotes

> "ele é bacana mas ele não vai mudar tudo"
> "não necessariamente os multimodais eles são alguma coisa mais texto, então não necessariamente você precisa usar esse"
> "não dá para confiar nas big techs"
