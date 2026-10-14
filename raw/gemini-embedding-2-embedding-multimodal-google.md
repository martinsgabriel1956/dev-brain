---
title: "Gemini Embedding 2 — o novo modelo de embedding multimodal do Google (resumo técnico)"
source_type: transcrição de vídeo (PT-BR, legenda automática)
author: "não identificado"
date_ingested: 2026-10-14
---

# Gemini Embedding 2 — o novo modelo de embedding multimodal do Google

> Transcrição limpa (pontuação, parágrafos e termos corrigidos). Já em português; sem tradução. Correções de ASR: "Bering 2" / "beding 2" / "Embeding 2" → Gemini Embedding 2 (inferido do contexto: "Gemini Embeding 2", "embeding do Gemini"); "Rug" → RAG; "Ligo" → leigo; "mat" → match; "BTECs" → big techs; "mo" → MOV (formato de vídeo, inferido); "VGG 16" mantido; "Ering" (marca de blusa) mantido como no original; "Vertex" = Google Vertex AI (inferido). Trechos confusos de ASR foram resolvidos pelo contexto. Nome do apresentador não identificado.

## Abertura (para o leigo)

O Google lançou nesta semana o novo modelo de embedding, o Gemini Embedding 2. O apresentador avisa que não vai dizer que isso "muda tudo em IA daqui pra frente"; o modelo é bacana, mas não vai mudar tudo.

Resumo: é um modelo de embedding **multimodal**. Suporta **texto, imagens, vídeo, áudio e documentos, tudo em um único espaço de embedding**. Serve para busca e classificação entre vários tipos de mídia.

Principal motivo de ser multimodal: **simplifica pipelines complexos**. Se você tem um pipeline complicado por lidar com vários tipos de documento, ele simplifica isso, obviamente com o custo da chamada da API. Também suporta **mais de 100 idiomas**, incluindo o português.

Para que serve, do ponto de vista do leigo: ferramentas de RAG para retornar informação. Se você tem vários arquivos no computador (textos, imagens, vídeos) e quer buscar neles, o agente consegue buscar com base em **busca semântica**: não por termos nem metadados específicos, mas por características internas do conteúdo. Exemplo: "me traga uma foto em que a pessoa está de camisa azul" na pasta de fotos; o modelo processa a expressão e traz as fotos que casam com a camisa azul.

Para o leigo o vídeo termina aqui; daqui em diante é uma discussão mais técnica, para quem tem interesse na área de dados.

## Limites por chamada (página do Google)

- **Texto:** até 8.192 tokens.
- **Imagens:** até 6 imagens por chamada.
- **Vídeo:** até 120 segundos, em MP4 ou MOV.
- **Áudio:** sem necessidade de transcrição de texto; a página não informa o tamanho máximo do áudio (o apresentador acha interessante).
- **Documentos:** PDFs de até 6 páginas.

Primeira pergunta técnica: e se o vídeo tiver mais de 120 s ou o documento mais de 6 páginas? Pode, mas é preciso um **script que quebre o conteúdo em pedaços (chunks)**, faça várias chamadas em loop e receba **um vetor para cada pedaço**. Vale para texto, vídeos, imagens e lotes de imagens: respeitar o máximo em cada chamada.

## Espaço de embedding unificado

O apresentador usa o desenho da página do Google: texto em azul, imagem em verde, vídeo em vermelho, etc. Um vídeo de um cachorrinho e um texto sobre cachorrinho ficam **próximos no espaço vetorial (espaço latente)**, em coordenadas vizinhas. Medindo a distância por **similaridade de cosseno** ou distância euclidiana (normalmente se usa cosseno nessas tarefas), os pontos ficam muito próximos. Uma foto de cachorro, um vídeo de cachorro latindo, o som do latido e o texto "o cachorro está latindo" formam praticamente um **cluster**. Cada conjunto de vetores semanticamente similares fica agrupado.

**Dimensões:** máximo de **3072**. É possível pedir metade ou um quarto disso: o modelo calcula as 3072 de qualquer forma e faz uma **projeção** para o número menor de dimensões, se o usuário quiser. O Google recomenda usar o máximo ("quanto mais dimensões, melhor"), o que implica lidar com mais dados.

**Demo do Google (busca por imagem):** o apresentador busca "animais"; o resultado inicial é uma onça atrás de grades e a busca devolve várias onças. Busca por voz não funcionou (a demo não grava a voz). Há também a documentação no Vertex com as especificações: até 3072 dimensões, comprimentos máximos, nome do modelo a chamar via API, MIME types compatíveis e **OCR de documentos**.

## O que significam os embeddings (intuição em 3D)

Exemplo clássico de Transformers/embeddings, em um espaço tridimensional:

- **rei** = (2, 1.3, 0) → semanticamente "rei".
- **homem** = (0, 0.5, 0) (só deslocamento no eixo Y, para facilitar).
- **mulher** = (0, 0.1, 0.1) (feminino).
- Rei − homem = (2, 0.8, 0); somando mulher: rei − homem + mulher ≈ (2, 0.9, 0.1) ≈ **rainha**.

Matematicamente isso se sustenta pela forma como o espaço foi treinado: tirar o masculino de "rei" e incluir o feminino leva a um ponto muito próximo do embedding de "rainha". Ou seja, o espaço tem **significados semânticos**.

O exemplo usa 3 dimensões; o Google trabalha com ~3.000. Cada dimensão isolada **não** significa algo como "masculinidade"; o que tem significado são as **direções** no espaço.

## Quando vale trocar pelo Gemini Embedding 2?

Hoje há modelos de visão com linguagem e de áudio com linguagem, mas ele é o único que usa todas as modalidades ao mesmo tempo. A maioria dos modelos usados hoje passa pela linguagem (não são necessariamente multimodais "de verdade"), então **nem sempre é preciso usar este**.

**Exemplo: busca visual para um site de roupas.**

1. *Abordagem atual, leve:* modelo baseado em **CNN** (ex.: **VGG16**). Tira-se a cabeça de classificação e pega-se o vetor anterior a ela (representação no espaço latente). Pré-calculam-se os vetores de todos os produtos do cliente. Na consulta (foto de alguém com camiseta azul), calcula-se o vetor e a **similaridade de cosseno** contra os vetores do catálogo e devolve-se a blusa mais parecida (pode não ser idêntica; a gola pode diferir, mas é uma blusa azul). Roda em equipamento de baixa sofisticação.
2. *Busca por metadados (maioria dos sites hoje):* descrição "blusa Ering, marca Ering, tamanho P, feminina, azul" e busca por termos. Adicionar busca visual (tipo **Google Lens**) já foi um grande upgrade.
3. *Pedido do cliente: busca textual semântica,* não só por descrição. Com modelos de visão-linguagem o usuário escreve "blusa azul de telinha com botões", mesmo que os metadados não digam se tem telinha ou botões. O embedding muitas vezes capta isso, **principalmente este do Google, que é muito poderoso** (o apresentador ainda não testou). Na indexação gera-se **mais de um vetor por produto** (imagens da blusa e metadados), e a consulta é comparada com todos por cosseno, devolvendo a melhor resposta.
4. *Busca multimodal por voz:* a pessoa fala como quer a blusa e o **áudio vai direto, sem passar por texto**, para ser comparado com os embeddings do banco. Resultado: **pipeline unificado e simplificado**.

## Desvantagens

1. **Custo:** são chamadas à API do Google; poderia ser feito com modelos separados open source, mas com modelo proprietário passa a haver custo por chamada.
2. **Privacidade/confidencialidade:** é preciso enviar os documentos à API do Google. O apresentador ainda não leu os termos de serviço, mas imagina que se esteja dando autorização para usar os dados no treino de modelos. Para documentos sensíveis da empresa, "de jeito nenhum", porque "não dá para confiar nas big techs".

## Fechamento

Apesar disso, é um modelo bacana e o apresentador acha que vai estimular outros laboratórios a criar soluções parecidas. Pede like e pergunta se o público prefere conteúdo técnico como este ou vídeos mais curtos só com novidades do mercado.
